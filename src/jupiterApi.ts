import { callTips, keywordGroups } from "./data";

export interface JupiterApiEntry {
  /** Fully-qualified command/utility name, e.g. "FileMenu.AddJTDB" or "JPT.GetVersion". */
  name: string;
  /** Leaf identifier used as completion label/insert text, e.g. "AddJTDB". */
  prefix: string;
  /** Full call signature, e.g. `FileMenu.AddJTDB(strFileName, strMethod="AUTO", ...)`. */
  signature: string;
  /** Individual parameter tokens, e.g. ["strFileName", "strMethod=\"AUTO\""]. */
  params: string[];
  /** Rich Markdown documentation: signature, args, return, examples. */
  doc: string;
}

export interface JupiterKeyword {
  /** The keyword/constant token, e.g. "ELEMTYPE_HEX8" or "add_button". */
  label: string;
  /** Human-readable origin shown in the completion detail. */
  group: string;
}

const entries: JupiterApiEntry[] = Object.entries(callTips).map(
  ([name, tip]) => ({
    name,
    prefix: tip.prefix,
    signature: tip.signature,
    params: tip.params,
    doc: tip.text,
  }),
);

const byName = new Map<string, JupiterApiEntry>(
  entries.map((entry) => [entry.name, entry]),
);

// Secondary index by leaf name so instance-style calls (e.g. `dlg.add_button`)
// resolve to JDGCreator.add_button. First definition wins on collisions.
const byLeaf = new Map<string, JupiterApiEntry>();
for (const entry of entries) {
  if (!byLeaf.has(entry.prefix)) {
    byLeaf.set(entry.prefix, entry);
  }
}

/** All known PSJ/JPT API entries (commands, utilities, GUI builders). */
export function allApiEntries(): readonly JupiterApiEntry[] {
  return entries;
}

/**
 * Look up an API entry by fully-qualified name (e.g. "FileMenu.AddJTDB"),
 * falling back to the leaf identifier (e.g. "add_button") for instance calls.
 */
export function lookupApi(name: string): JupiterApiEntry | undefined {
  return byName.get(name) ?? byLeaf.get(name.split(".").pop() ?? name);
}

const keywords: JupiterKeyword[] = [
  ...keywordGroups.psjUtility.map((label) => ({ label, group: "PSJ Utility" })),
  ...keywordGroups.psjGui.map((label) => ({ label, group: "PSJ GUI" })),
];

/** PSJ utility constants and GUI-builder keywords offered as completions. */
export function allKeywords(): readonly JupiterKeyword[] {
  return keywords;
}
