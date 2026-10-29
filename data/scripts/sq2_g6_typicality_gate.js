#!/usr/bin/env node
// G6 typicality gate; see logs/2026-10-29-sq2-g6-typicality-gate-selfreview.md
// Run from repo root: node data/scripts/sq2_g6_typicality_gate.js
const fs = require("node:fs");
const read = p => fs.readFileSync(p, "utf8");
const raw = read("data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt");
const body = raw.slice(raw.indexOf("*** START OF"), raw.indexOf("*** END OF"));
const lettersOnly = s => s.toUpperCase().replace(/[^A-Z]/g, "");
let t = body.slice(body.indexOf("It is a truth universally acknowledged"));
const te = t.search(/^\s*THE END\s*$/m); if (te >= 0) t = t.slice(0, te);
t = t.replace(/\[Illustration[^\]]*\]/g, "").split(/\r?\n/).filter(l => !/^\s*CHAPTER [IVXLC]+\.?\s*$/.test(l)).join("\n");
const CC = lettersOnly(t);
const truth = lettersOnly(read("data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt"));
const mk = C => {
  const codes = Uint8Array.from(C, c => c.charCodeAt(0) - 65), cnt = new Int32Array(26 ** 4), ctx = new Int32Array(26 ** 3);
  for (let i = 0; i < codes.length - 3; i++) { const k = (codes[i] * 26 + codes[i + 1]) * 26 + codes[i + 2]; ctx[k]++; cnt[k * 26 + codes[i + 3]]++; }
  const lp = new Float64Array(26 ** 4);
  for (let k = 0; k < lp.length; k++) lp[k] = Math.log((cnt[k] + 0.5) / (ctx[(k / 26) | 0] + 13));
  return s => { let r = 0; for (let i = 0; i < s.length - 3; i++) r += lp[(((s.charCodeAt(i) - 65) * 26 + s.charCodeAt(i + 1) - 65) * 26 + s.charCodeAt(i + 2) - 65) * 26 + s.charCodeAt(i + 3) - 65]; return r / (s.length - 3); };
};
const ent = s => { const c = new Array(26).fill(0); for (const ch of s) c[ch.charCodeAt(0) - 65]++; let h = 0; for (const n of c) if (n) h -= (n / s.length) * Math.log2(n / s.length); return h; };
const pct = (a, p) => { const b = [...a].sort((x, y) => x - y); return b[Math.min(b.length - 1, Math.max(0, Math.round(p / 100 * (b.length - 1))))]; };
function mulberry32(a) { return () => { a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
const A = [...Array(26).keys()].map(i => String.fromCharCode(65 + i));
const T = [];
for (const x of A) T.push({ kind: "const", id: x, s: x.repeat(408) });
for (const x of A) for (const y of A) if (x !== y) T.push({ kind: "per2", id: x + y, s: (x + y).repeat(204) });
function run(frac, lo, hi) {
  const cut = Math.floor(CC.length * frac), sc = mk(CC.slice(0, cut)), K = CC.slice(cut);
  const W = []; for (let i = 0; i + 408 <= K.length; i += 408) W.push(K.slice(i, i + 408));
  const ws = W.map(sc), wh = W.map(ent);
  const b = { sLo: pct(ws, lo), sHi: pct(ws, hi), hLo: pct(wh, lo), hHi: pct(wh, hi) };
  const verdict = x => { const s = sc(x), h = ent(x); return { s, h, sOK: s >= b.sLo && s <= b.sHi, hOK: h >= b.hLo && h <= b.hHi, typical: s >= b.sLo && s <= b.sHi && h >= b.hLo && h <= b.hHi }; };
  const deg = T.map(o => ({ ...o, ...verdict(o.s) })), tv = verdict(truth);
  const rng = mulberry32(408); let shufTypical = 0, shufSok = 0, shufHok = 0;
  for (let n = 0; n < 20; n++) { const a = [...truth]; for (let i = a.length - 1; i > 0; i--) { const j = Math.floor(rng() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } const v = verdict(a.join("")); shufTypical += v.typical; shufSok += v.sOK; shufHok += v.hOK; }
  const winTypical = W.filter((w, i) => ws[i] >= b.sLo && ws[i] <= b.sHi && wh[i] >= b.hLo && wh[i] <= b.hHi).length;
  const accepted = deg.filter(d => d.typical);
  return { split: frac, band: [lo, hi], nWindows: W.length, cutoffs: b, winTypicalFrac: winTypical / W.length, truth: tv, degAccepted: accepted.length, degAcceptedIds: accepted.map(d => d.id), degRejectedByEntropyOnly: deg.filter(d => !d.hOK && d.sOK).length, degRejectedByScoreOnly: deg.filter(d => d.hOK && !d.sOK).length, degRejectedByBoth: deg.filter(d => !d.hOK && !d.sOK).length, G6: accepted.length === 0 && tv.typical ? "PASS" : "FAIL", shuffles20: { typical: shufTypical, sOK: shufSok, hOK: shufHok } };
}
console.log(JSON.stringify({ lenCC: CC.length, truthLen: truth.length, primary: run(0.7, 1, 99), sens_P5_P95: run(0.7, 5, 95), sens_60_40: run(0.6, 1, 99) }, null, 1));
