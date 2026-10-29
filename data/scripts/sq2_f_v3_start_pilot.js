#!/usr/bin/env node
// Exploratory Z408 F-objective control; see logs/2026-10-28-sq2-f-v3-start-pilot.md.
// Run from the repository root: node data/scripts/sq2_f_v3_start_pilot.js
const fs = require("node:fs");
const root = process.cwd();
const read = p => fs.readFileSync(root + "/" + p, "utf8");
const cipherPath = "data/external-sources/azdecrypt-doranchak-2026-09-27/z408-cipher.txt";
const truthPath = "data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt";
const corpusPath = "data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt";
const v3Path = "data/derived/sq2-z408-hillclimb-v3-result.md";
const ct = read(cipherPath).split(/\r?\n/).join("");
const v3 = read(v3Path).match(/```\s*([A-Z]+)\s*```/)[1];
const raw = read(corpusPath);
const C = raw.slice(raw.indexOf("*** START OF"), raw.indexOf("*** END OF")).toUpperCase().replace(/[^A-Z]/g, "");
if (ct.length !== 408 || v3.length !== 408 || C.length !== 563955) throw Error("input length changed");
const syms = [...new Set(ct)].sort();
const si = new Map(syms.map((s,i) => [s,i]));
const ci = Uint8Array.from(ct, c => si.get(c));
const m = new Uint8Array(syms.length), seen = new Uint8Array(syms.length);
for (let i=0; i<ct.length; i++) {
  const j=ci[i], k=v3.charCodeAt(i)-65;
  if (seen[j] && m[j] !== k) throw Error("v3 mapping inconsistent");
  m[j]=k; seen[j]=1;
}
const cnt = new Int32Array(26**4), ctx = new Int32Array(26**3);
const codes = Uint8Array.from(C, c => c.charCodeAt(0)-65);
for (let i=0; i<codes.length-3; i++) {
  const k=(codes[i]*26+codes[i+1])*26+codes[i+2];
  ctx[k]++; cnt[k*26+codes[i+3]]++;
}
const lp = new Float64Array(26**4);
for (let k=0; k<lp.length; k++) lp[k]=Math.log((cnt[k]+0.5)/(ctx[(k/26)|0]+13));
function score(map) {
  let s=0;
  for (let i=0; i<ci.length-3; i++)
    s+=lp[((map[ci[i]]*26+map[ci[i+1]])*26+map[ci[i+2]])*26+map[ci[i+3]]];
  return s;
}
let state=20261028;
const rand=()=>{state^=state<<13;state^=state>>>17;state^=state<<5;return (state>>>0)/4294967296};
const start=Date.now(), initial=score(m);
let cur=initial, best=cur, bestM=Uint8Array.from(m), evaluated=0;
for (let t=0; t<100000; t++) {
  if (Date.now()-start>60000) break;
  const temp=4*Math.pow(0.9999,t);
  const a=Math.floor(rand()*m.length), old=m[a], swap=rand()<0.5;
  let b=-1, oldB=-1;
  if (swap) {
    b=Math.floor(rand()*m.length);
    if (a===b) continue;
    oldB=m[b]; m[a]=oldB; m[b]=old;
  } else {
    const nv=Math.floor(rand()*26);
    if (nv===old) continue;
    m[a]=nv;
  }
  const val=score(m), delta=val-cur;
  if (delta>=0 || rand()<Math.exp(Math.max(delta,-50)/Math.max(temp,1e-6))) {
    cur=val;
    if (cur>best) {best=cur; bestM=Uint8Array.from(m);}
  } else {m[a]=old; if (swap) m[b]=oldB;}
  evaluated++;
}
// Known plaintext is loaded only after the optimization loop.
const truth=read(truthPath).split(/\r?\n/).join("");
const tc=Uint8Array.from(truth, c=>c.charCodeAt(0)-65);
let truthScore=0;
for (let i=0; i<tc.length-3; i++)
  truthScore+=lp[((tc[i]*26+tc[i+1])*26+tc[i+2])*26+tc[i+3]];
const decode=Array.from(ci,j=>String.fromCharCode(65+bestM[j])).join("");
let matches=0;
for (let i=0; i<truth.length; i++) matches+=decode[i]===truth[i];
console.log(JSON.stringify({seed:20261028,budget:100000,evaluated,initialScore:initial,bestScore:best,truthScore,margin:best-truthScore,matches,accuracy:matches/truth.length,elapsedMs:Date.now()-start,decode},null,2));
