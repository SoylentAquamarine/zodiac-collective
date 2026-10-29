#!/usr/bin/env node
// Random-start F stress test; see logs/2026-10-29-sq2-pr12-review-and-random-start-holdout-selfreview.md
// Run from repo root: node data/scripts/sq2_f_random_start_holdout.js <seedStart> <seedEnd>
const fs = require("node:fs");
const read = p => fs.readFileSync(process.cwd() + "/" + p, "utf8");
const ct = read("data/external-sources/azdecrypt-doranchak-2026-09-27/z408-cipher.txt").split(/\r?\n/).join("");
const raw = read("data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt");
const C = raw.slice(raw.indexOf("*** START OF"), raw.indexOf("*** END OF")).toUpperCase().replace(/[^A-Z]/g, "");
if (ct.length !== 408 || C.length !== 563955) throw Error("input length changed");
const syms = [...new Set(ct)].sort(), si = new Map(syms.map((s, i) => [s, i]));
const ci = Uint8Array.from(ct, c => si.get(c)), n = syms.length;
const cnt = new Int32Array(26 ** 4), ctx = new Int32Array(26 ** 3), uni = new Float64Array(26);
const codes = Uint8Array.from(C, c => c.charCodeAt(0) - 65);
for (const c of codes) uni[c]++;
for (let i = 0; i < codes.length - 3; i++) { const k = (codes[i] * 26 + codes[i + 1]) * 26 + codes[i + 2]; ctx[k]++; cnt[k * 26 + codes[i + 3]]++; }
const lp = new Float64Array(26 ** 4);
for (let k = 0; k < lp.length; k++) lp[k] = Math.log((cnt[k] + 0.5) / (ctx[(k / 26) | 0] + 13));
const score = m => { let s = 0; for (let i = 0; i < ci.length - 3; i++) s += lp[((m[ci[i]] * 26 + m[ci[i + 1]]) * 26 + m[ci[i + 2]]) * 26 + m[ci[i + 3]]]; return s; };
const truth = read("data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt").split(/\r?\n/).join("");
const tc = Uint8Array.from(truth, c => c.charCodeAt(0) - 65);
let truthScore = 0; for (let i = 0; i < tc.length - 3; i++) truthScore += lp[((tc[i] * 26 + tc[i + 1]) * 26 + tc[i + 2]) * 26 + tc[i + 3]];
const total = codes.length, out = [];
for (let seed = +process.argv[2]; seed <= +process.argv[3]; seed++) {
  let st = seed;
  const rand = () => { st ^= st << 13; st ^= st >>> 17; st ^= st << 5; return (st >>> 0) / 4294967296; };
  for (let i = 0; i < 20; i++) rand();
  const m = new Uint8Array(n);
  for (let j = 0; j < n; j++) { let r = rand() * total, k = 0; while (k < 25 && r >= uni[k]) { r -= uni[k]; k++; } m[j] = k; }
  const P = 1000000; let cur = score(m), best = cur, bm = Uint8Array.from(m);
  for (let t = 0; t < P; t++) {
    const temp = 4 * Math.pow(0.05 / 4, t / P), a = (rand() * n) | 0, old = m[a], sw = rand() < 0.5; let b = -1, ob = -1;
    if (sw) { b = (rand() * n) | 0; if (a === b) continue; ob = m[b]; m[a] = ob; m[b] = old; }
    else { const nv = (rand() * 26) | 0; if (nv === old) continue; m[a] = nv; }
    const v = score(m), d = v - cur;
    if (d >= 0 || rand() < Math.exp(Math.max(d, -50) / temp)) { cur = v; if (cur > best) { best = cur; bm = Uint8Array.from(m); } }
    else { m[a] = old; if (sw) m[b] = ob; }
  }
  const dec = Array.from(ci, j => String.fromCharCode(65 + bm[j])).join("");
  let mt = 0; for (let i = 0; i < 408; i++) mt += dec[i] === truth[i];
  out.push({ seed, best, truthScore, margin: best - truthScore, matches: mt, decode: dec });
  console.error(seed, best.toFixed(3), mt);
}
console.log(JSON.stringify(out));
