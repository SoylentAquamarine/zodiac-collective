#!/usr/bin/env node
// G7 diagnosis; see logs/2026-10-29-sq2-g7-truth-deficit-diagnosis-selfreview.md
// Run from repo root: node data/scripts/sq2_g7_truth_deficit_diagnosis.js
const fs = require("node:fs");
const read = p => fs.readFileSync(p, "utf8");
const raw = read("data/external-sources/gutenberg-1342-2026-09-29/pride_prejudice.txt");
const body = raw.slice(raw.indexOf("*** START OF"), raw.indexOf("*** END OF"));
const L = s => s.toUpperCase().replace(/[^A-Z]/g, "");
let t = body.slice(body.indexOf("It is a truth universally acknowledged"));
const te = t.search(/^\s*THE END\s*$/m); if (te >= 0) t = t.slice(0, te);
t = t.replace(/\[Illustration[^\]]*\]/g, "").split(/\r?\n/).filter(l => !/^\s*CHAPTER [IVXLC]+\.?\s*$/.test(l)).join("\n");
const CC = L(t);
const truth = L(read("data/external-sources/azdecrypt-doranchak-2026-09-27/z408-solved.txt"));
const cut = Math.floor(CC.length * 0.7);
const M = CC.slice(0, cut), K = CC.slice(cut);
const codes = Uint8Array.from(M, c => c.charCodeAt(0) - 65), cnt = new Int32Array(26 ** 4), ctx = new Int32Array(26 ** 3);
for (let i = 0; i < codes.length - 3; i++) { const k = (codes[i] * 26 + codes[i + 1]) * 26 + codes[i + 2]; ctx[k]++; cnt[k * 26 + codes[i + 3]]++; }
const lp = new Float64Array(26 ** 4);
for (let k = 0; k < lp.length; k++) lp[k] = Math.log((cnt[k] + 0.5) / (ctx[(k / 26) | 0] + 13));
const sc = s => { let r = 0; for (let i = 0; i < s.length - 3; i++) r += lp[(((s.charCodeAt(i) - 65) * 26 + s.charCodeAt(i + 1) - 65) * 26 + s.charCodeAt(i + 2) - 65) * 26 + s.charCodeAt(i + 3) - 65]; return r / (s.length - 3); };
const pct = (a, p) => { const b = [...a].sort((x, y) => x - y); return b[Math.min(b.length - 1, Math.max(0, Math.round(p / 100 * (b.length - 1))))]; };
const wins = (S, n) => { const W = []; for (let i = 0; i + n <= S.length; i += n) W.push(S.slice(i, i + n)); return W; };
const rank = (arr, x) => arr.filter(v => v < x).length / arr.length;
// D1
const k51 = wins(K, 51).map(sc), P1_51 = pct(k51, 1);
const D1 = wins(truth.slice(0, 408), 51).map((c, i) => ({ chunk: i, text: c, s: sc(c), pctile: rank(k51, sc(c)), belowP1: sc(c) < P1_51 }));
// D2
const k390 = wins(K, 390).map(sc), P1_390 = pct(k390, 1);
const t390 = truth.slice(0, truth.length - 18);
const D2 = { tail: truth.slice(-18), sFull: sc(truth), s390: sc(t390), P1_390, P1_408: pct(wins(K, 408).map(sc), 1), pctile390: rank(k390, sc(t390)), below: sc(t390) < P1_390 };
// D3 register: quoted speech vs narrative (letters outside quotes), from the same K region of raw text
const rawK = t; // use the raw cleaned text, then split by quotes
const inQ = [], outQ = []; let q = false, cur = "";
for (const ch of rawK) { if (ch === "“" || ch === "”" || ch === '"') { (q ? inQ : outQ).push(cur); cur = ""; q = !q; } else cur += ch; }
(q ? inQ : outQ).push(cur);
const KQ = L(inQ.join("")), KN = L(outQ.join(""));
// score only the held-out tail of each stream by the same 70% cut (position-matched approx.)
const qs = KQ.slice(Math.floor(KQ.length * 0.7)), ns = KN.slice(Math.floor(KN.length * 0.7));
const wq = wins(qs, 408).map(sc), wn = wins(ns, 408).map(sc);
const mean = a => a.reduce((x, y) => x + y, 0) / a.length;
const D3 = { quotedLetters: KQ.length, narrLetters: KN.length, nWinQ: wq.length, nWinN: wn.length, meanQ: mean(wq), meanN: mean(wn), shift: mean(wq) - mean(wn), meanAllK: mean(wins(K, 408).map(sc)) };
console.log(JSON.stringify({ D1, D2, D3, P1_51 }, null, 1));
