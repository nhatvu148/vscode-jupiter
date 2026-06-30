// Maintainer-only: regenerates src/data.ts from a local checkout of the
// internal Jupiter API sources (not publicly available). Point --src at that
// checkout; the layout/flags are documented for maintainers via `--help`-style
// usage below. Requires the proprietary jupiterutils package to be present.
//
//   node scripts/generate.mjs --src <path>
//
// It reads the jupiterutils Python modules (PSJ commands + JPT utilities) and
// the keyword list, emitting an accurate signature (real param names +
// defaults, types inferred from Hungarian prefixes) plus the description
// docstring when present.

import { existsSync, readFileSync, writeFileSync, readdirSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";

const SCRIPT_DIR = dirname(fileURLToPath(import.meta.url));
const REPO = join(SCRIPT_DIR, "..");

function flag(name, fallback) {
  const i = process.argv.indexOf(`--${name}`);
  return i >= 0 && process.argv[i + 1] ? process.argv[i + 1] : fallback;
}

const srcRoot =
  flag("src", process.env.JUPITER_API_SRC) ?? join(REPO, "..", "jupiter-api-src");
const utilsPkg = flag("utils", join(srcRoot, "jupiter_utils", "jupiterutils"));
const keywordsDat = join(srcRoot, "IDEData", "Keywords.dat");

if (!existsSync(utilsPkg)) {
  console.error(
    `jupiterutils package not found at ${utilsPkg}\n` +
      `Pass --src <path to the internal Jupiter API checkout>, or --utils <path>.`,
  );
  process.exit(1);
}

// --- type inference from Hungarian prefixes (longest prefix wins) -----------
const TYPE_BY_PREFIX = [
  ["crl", "Cursor List"],
  ["str", "String"],
  ["listl", "List"],
  ["list", "List"],
  ["vec", "Vector"],
  ["dl", "Double List"],
  ["il", "Integer List"],
  ["cr", "Cursor"],
  ["b", "Boolean"],
  ["i", "Integer"],
  ["d", "Double"],
].sort((a, b) => b[0].length - a[0].length);

function inferType(name) {
  for (const [p, t] of TYPE_BY_PREFIX) {
    if (
      name.startsWith(p) &&
      name.length > p.length &&
      name[p.length] === name[p.length].toUpperCase() &&
      name[p.length] !== "_"
    ) {
      return t;
    }
  }
  return undefined;
}

// Split a Python arg list on top-level commas (ignores (), [], {} nesting).
function splitArgs(s) {
  const out = [];
  let depth = 0;
  let cur = "";
  for (const ch of s) {
    if ("([{".includes(ch)) depth++;
    else if (")]}".includes(ch)) depth--;
    if (ch === "," && depth === 0) {
      out.push(cur);
      cur = "";
    } else {
      cur += ch;
    }
  }
  if (cur.trim()) out.push(cur);
  return out;
}

function parseParams(raw) {
  return splitArgs(raw)
    .map((p) => p.trim())
    .filter((p) => p && p !== "self")
    .map((p) => {
      const eq = p.indexOf("=");
      const name = (eq >= 0 ? p.slice(0, eq) : p).trim();
      const def = eq >= 0 ? p.slice(eq + 1).trim() : undefined;
      return { name, def, type: inferType(name) };
    });
}

// --- parse one python module into {fullName: {prefix, params, doc}} ---------
function parseModule(file) {
  const lines = readFileSync(file, "utf8").split(/\r?\n/);
  const stack = []; // {indent, name}
  const result = {};

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    if (!line.trim() || line.trim().startsWith("#")) continue;
    const indent = line.length - line.trimStart().length;

    const cls = line.match(/^(\s*)class\s+([A-Za-z0-9_]+)/);
    if (cls) {
      while (stack.length && stack[stack.length - 1].indent >= indent) stack.pop();
      stack.push({ indent, name: cls[2] });
      continue;
    }

    const def = line.match(/^(\s*)def\s+([A-Za-z0-9_]+)\s*\(/);
    if (!def) continue;

    // gather the (possibly multi-line) signature until parens balance
    let sig = line.slice(line.indexOf("(") + 1);
    let depth = 1;
    let j = i;
    const consume = (text) => {
      for (const ch of text) {
        if (ch === "(") depth++;
        else if (ch === ")") depth--;
        if (depth === 0) return true;
      }
      return false;
    };
    let balanced = consume(line.slice(line.indexOf("(") + 1));
    while (!balanced && ++j < lines.length) {
      sig += "\n" + lines[j];
      balanced = consume(lines[j]);
    }
    const rawParams = sig.slice(0, sig.lastIndexOf(")"));

    while (stack.length && stack[stack.length - 1].indent >= indent) stack.pop();
    const namespace = stack
      .map((s) => s.name.replace(/_/g, "."))
      .join(".");
    const method = def[2];
    if (method.startsWith("_")) continue; // skip dunders/private
    const fullName = namespace ? `${namespace}.${method}` : method;

    // docstring: look for a triple-quote opening in the next few lines
    let doc = "";
    let k = j + 1;
    while (k < lines.length && !lines[k].trim()) k++;
    const open = lines[k]?.match(/^\s*[rubRUB]*("""|''')/);
    if (open) {
      const q = open[1];
      const body = [];
      let rest = lines[k].slice(lines[k].indexOf(q) + 3);
      let closed = rest.includes(q);
      if (!closed) {
        body.push(rest);
        while (++k < lines.length) {
          if (lines[k].includes(q)) {
            body.push(lines[k].slice(0, lines[k].indexOf(q)));
            break;
          }
          body.push(lines[k]);
        }
      }
      const text = body.join("\n");
      const dIdx = text.indexOf("## Description");
      doc = (dIdx >= 0 ? text.slice(dIdx) : text)
        .split("\n")
        .map((l) => l.replace(/^\s{0,8}/, ""))
        .join("\n")
        .trim();
    }

    result[fullName] = { prefix: method, params: parseParams(rawParams), doc };
  }
  return result;
}

function signatureLine(name, params) {
  const inner = params
    .map((p) => (p.def !== undefined ? `${p.name}=${p.def}` : p.name))
    .join(", ");
  return `${name}(${inner})`;
}

function paramTable(params) {
  if (!params.length) return "";
  return (
    "**Parameters:**  \n" +
    params
      .map(
        (p) =>
          `- \`${p.name}\`${p.type ? ` *(${p.type})*` : ""}` +
          `${p.def !== undefined ? ` = \`${p.def}\`` : ""}`,
      )
      .join("  \n")
  );
}

// Drop a "## <heading>" section from a markdown doc (its content duplicates
// the signature line we render ourselves).
function stripSection(doc, heading) {
  const out = [];
  let skip = false;
  for (const l of doc.split("\n")) {
    if (/^##\s+/.test(l)) skip = l.includes(heading);
    if (!skip) out.push(l);
  }
  return out.join("\n").replace(/\n{3,}/g, "\n\n").trim();
}

function toCallTip(name, entry) {
  const params = entry.params.map((p) =>
    p.def !== undefined ? `${p.name}=${p.def}` : p.name,
  );
  const signature = `${name}(${params.join(", ")})`;
  const sig = "```python\n" + signature + "\n```";
  const desc = entry.doc
    ? stripSection(entry.doc, "Syntax")
    : paramTable(entry.params);
  return {
    prefix: entry.prefix,
    signature,
    params,
    text: desc ? `${sig}\n\n${desc}` : sig,
  };
}

// --- keywords ---------------------------------------------------------------
function keywordGroups() {
  if (!existsSync(keywordsDat)) {
    return { python: [], psjUtility: [], psjGui: [], psjCommand: [] };
  }
  const HEADERS = {
    "Python Standard": "python",
    "PSJ Utility": "psjUtility",
    "PSJ-GUI": "psjGui",
    "PSJ Commands": "psjCommand",
  };
  const groups = { python: [], psjUtility: [], psjGui: [], psjCommand: [] };
  let cur = null;
  for (const line of readFileSync(keywordsDat, "utf8").split("\n")) {
    const t = line.trim();
    if (t.startsWith("//")) {
      const hit = Object.keys(HEADERS).find((h) => t.includes(h));
      if (hit) cur = HEADERS[hit];
      continue;
    }
    if (!t || !cur) continue;
    for (const tok of t.split(",")) {
      const k = tok.trim();
      if (k) groups[cur].push(k);
    }
  }
  for (const g of Object.keys(groups)) groups[g] = [...new Set(groups[g])].sort();
  return groups;
}

// --- build ------------------------------------------------------------------
const commands = parseModule(join(utilsPkg, "PSJ_Classes.py"));
const utility = parseModule(join(utilsPkg, "Utility.py"));
const gui = parseModule(join(utilsPkg, "pyjdg.py"));

const callTips = {};
let docs = 0;
for (const [name, entry] of [
  ...Object.entries(commands),
  ...Object.entries(utility),
  ...Object.entries(gui),
]) {
  // keep only JPT.* utilities from Utility.py (skip enum classes / helpers)
  if (utility[name] && !name.startsWith("JPT.")) continue;
  // GUI dialog builder methods live on JDGCreator (used as `dlg.<method>(...)`)
  if (gui[name] && !name.startsWith("JDGCreator.")) continue;
  callTips[name] = toCallTip(name, entry);
  if (entry.doc && !/Unknown Description/.test(entry.doc)) docs++;
}

const groups = keywordGroups();

const out =
  `// AUTO-GENERATED by scripts/generate.mjs from the jupiter_utils package.\n` +
  `// Do not edit by hand — run \`yarn generate --src <path>\` instead.\n` +
  `// callTips: ${Object.keys(callTips).length} entries (${docs} with descriptions).\n\n` +
  `export interface CallTip {\n  prefix: string;\n  signature: string;\n  params: string[];\n  text: string;\n}\n\n` +
  `export const callTips: Record<string, CallTip> = ${JSON.stringify(callTips, null, 2)};\n\n` +
  `export type KeywordGroup = "python" | "psjUtility" | "psjGui" | "psjCommand";\n\n` +
  `export const keywordGroups: Record<KeywordGroup, string[]> = ${JSON.stringify(groups, null, 2)};\n`;

writeFileSync(join(REPO, "src/data.ts"), out);

console.log(`src/data.ts regenerated from ${utilsPkg}`);
console.log(
  `  callTips: ${Object.keys(callTips).length} (${docs} with descriptions)`,
);
console.log(
  `  keywords: psjUtility=${groups.psjUtility.length} psjGui=${groups.psjGui.length}`,
);
void readdirSync; // (reserved for future multi-file parsing)
