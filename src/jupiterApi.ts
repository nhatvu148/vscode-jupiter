import { callTips, keywordGroups } from "./data";

export interface JupiterApiEntry {
  /** Fully-qualified command/utility name, e.g. "FileMenu.Save" or "JPT.GetVersion". */
  name: string;
  /** Leaf identifier used as completion label/insert text, e.g. "Save". */
  prefix: string;
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
  ([name, tip]) => ({ name, prefix: tip.prefix, doc: tip.text }),
);

const byName = new Map<string, JupiterApiEntry>(
  entries.map((entry) => [entry.name, entry]),
);

/** All known PSJ/JPT API entries (commands and utilities). */
export function allApiEntries(): readonly JupiterApiEntry[] {
  return entries;
}

/** Look up an API entry by its fully-qualified name, e.g. "FileMenu.Save". */
export function lookupApi(name: string): JupiterApiEntry | undefined {
  return byName.get(name);
}

const keywords: JupiterKeyword[] = [
  ...keywordGroups.psjUtility.map((label) => ({ label, group: "PSJ Utility" })),
  ...keywordGroups.psjGui.map((label) => ({ label, group: "PSJ GUI" })),
];

/** PSJ utility constants and GUI-builder keywords offered as completions. */
export function allKeywords(): readonly JupiterKeyword[] {
  return keywords;
}
