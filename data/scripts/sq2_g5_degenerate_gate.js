#!/usr/bin/env node
// G5 degenerate-string gate; see logs/2026-10-29-sq2-g5-degenerate-gate-selfreview.md
// Run from repo root: node data/scripts/sq2_g5_degenerate_gate.js
const fs = require("node:fs");
const read = p => fs.readFileSync(p, "utf8");
const raw = read("data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt");
const body = raw.slice(raw.indexOf("*** START OF"), raw.indexOf("*** END OF"));
const lettersOnly = s => s.toUpperCase().replace(/[^A-Z]/g, "");
const CF = lettersOnly(body);
let t = body.slice(body.indexOf("It is a truth universally acknowledged"));
const te = t.search(/^\s*THE END\s*$/m); if (te >= 0) t = t.slice(0, te);
t = t.replace(/\[Illustration[^\]]*\]/g, "").split(/\r?\n/).filter(l => !/^\s*CHAPTER [IVXLC]+\.?\s*$/.test(l)).join("\n");
const CC = lettersOnly(t);
const residue = { chapter: (t.match(/CHAPTER/g) || []).length, illustration: (t.match(/Illustration/g) || []).length };
const truth = lettersOnly(read("data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt"));
const mk = C => {
  const codes = Uint8Array.from(C, c => c.charCodeAt(0) - 65), cnt = new Int32Array(26 ** 4), ctx = new Int32Array(26 ** 3);
  for (let i = 0; i < codes.length - 3; i++) { const k = (codes[i] * 26 + codes[i + 1]) * 26 + codes[i + 2]; ctx[k]++; cnt[k * 26 + codes[i + 3]]++; }
  const lp = new Float64Array(26 ** 4);
  for (let k = 0; k < lp.length; k++) lp[k] = Math.log((cnt[k] + 0.5) / (ctx[(k / 26) | 0] + 13));
  return s => { let r = 0; for (let i = 0; i < s.length - 3; i++) r += lp[(((s.charCodeAt(i) - 65) * 26 + s.charCodeAt(i + 1) - 65) * 26 + s.charCodeAt(i + 2) - 65) * 26 + s.charCodeAt(i + 3) - 65]; return r; };
};
const A = [...Array(26).keys()].map(i => String.fromCharCode(65 + i));
const T = [];
for (const x of A) T.push({ kind: "const", id: x, s: x.repeat(408) });
for (const x of A) for (const y of A) if (x !== y) T.push({ kind: "per2", id: x + y, s: (x + y).repeat(204) });
const out = { lens: { CF: CF.length, CC: CC.length, truth: truth.length }, residue, nT: T.length, scorers: {} };
for (const [name, C] of [["F", CF], ["Fprime", CC]]) {
  const sc = mk(C), ts = sc(truth), rows = T.map(o => ({ kind: o.kind, id: o.id, score: sc(o.s) })).sort((a, b) => b.score - a.score);
  const above = rows.filter(r => r.score > ts);
  out.scorers[name] = { truthScore: ts, nAbove: above.length, nAboveConst: above.filter(r => r.kind === "const").length, nAbovePer2: above.filter(r => r.kind === "per2").length, G5: above.length === 0 ? "PASS" : "FAIL", top5: rows.slice(0, 5), bestMarginToTruth: rows[0].score - ts, aboveIds: above.map(r => r.id) };
}
console.log(JSON.stringify(out, null, 1));
