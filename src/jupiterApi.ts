import { callTips } from "./data";

export interface JupiterApiEntry {
  /** Fully-qualified command/utility name, e.g. "FileMenu.Save" or "JPT.GetVersion". */
  name: string;
  /** Leaf identifier used as completion label/insert text, e.g. "Save". */
  prefix: string;
  /** Rich Markdown documentation: signature, args, return, examples. */
  doc: string;
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
