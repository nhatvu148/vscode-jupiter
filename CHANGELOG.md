# Change Log

All notable changes to the "jupiter" extension will be documented in this file.

Check [Keep a Changelog](http://keepachangelog.com/) for recommendations on how to structure this file.

## [1.7.0]

- The bundled data is now **interface-facts only**: command/utility/GUI names,
  accurate signatures, and a typed parameter list (types inferred locally from
  the parameter names). e-technostar's documentation prose, descriptions, and
  examples are **no longer bundled**. Completions and signature help are
  unchanged; hovers show the signature + typed parameters instead of prose.
- `data.ts` shrank ~40% (3.4 MB → 2.1 MB). Regenerate with
  `yarn generate --src <path>` (interface-facts-only is the default; pass
  `--with-prose` to include docstrings).
- Updated NOTICE / attribution to reflect that only interface facts are
  included.

## [1.6.1]

- Removed the "See reference here" hover link. The documentation site
  (`psjdoc.e-technostar.com`) is now entirely behind authentication, so the
  link returned 401 for everyone. Hovers keep their inline signature +
  description, which is the useful part.
- Added a `NOTICE` clarifying that the MIT license covers the extension's source
  code only; the bundled PSJ/JPT API names and documentation are the property of
  e-technostar.

## [1.6.0]

- **Signature help**: typing `(` after a PSJ/JPT call shows the parameter hints,
  with the active argument highlighted as you type commas — powered by the real
  signatures from jupiterutils.
- **GUI dialog completions**: parsed `pyjdg.py` (the `JDGCreator` builder), adding
  184 documented GUI methods (`add_button`, `add_combobox`, …) with signatures
  and docstrings. Instance-style calls like `dlg.add_button(` resolve in hovers
  and signature help via a leaf-name lookup.

## [1.5.0]

- Regenerated the API data directly from the **jupiterutils** package via a new
  `yarn generate` script. Every command now carries its **accurate signature**
  (real parameter names, defaults, and types inferred from Hungarian prefixes),
  and ~960 commands/utilities include their full `## Description` docstring
  (description, inputs, examples). Stale/renamed commands are dropped.
- `src/data.ts` is now generated, not hand-maintained — refreshing it when the
  PSJ docs change is a single command.

## [1.4.0]

- Refreshed the PSJ/JPT data against the latest `psj-editor` sources: command
  coverage grew to **1,983** entries (+1,255 commands). Existing rich docs are
  preserved; newly added commands link to the reference.
- Added **PSJ utility constants and PSJ-GUI keyword** completions (~980 tokens
  such as `ELEMTYPE_HEX8`, `add_button`), ranked below the documented methods.

## [1.3.0]

- **Removed the bundled TabNine autocompleter** (the cause of the high-CPU
  reports) and its 54MB of native binaries. The extension is now a single
  ~270KB esbuild bundle with no background processes — the `.vsix` dropped
  from 27MB to ~370KB.
- **PSJ/JPT API IntelliSense**: completion for ~700 Jupiter commands and `JPT`
  utilities, each with its documented signature.
- **Richer hovers**: known PSJ/JPT calls now show their full signature inline,
  in addition to the reference link.
- Modernized the toolchain (TypeScript 5.7, ESLint 9, `@types/vscode` 1.84),
  added integration tests and GitHub Actions CI, and resolved the dependency
  security advisories (88 → 0 shipped).

## [1.2.7]

- fix high CPU load (#1): activate only for Jupiter/Python files and scope
  completions to those languages instead of running on every file/keystroke

## [1.2.6]

- fix reference link - only displays at function names

## [1.2.5]

- fix reference link bug

## [1.2.4]

- update reference links

## [1.2.3]

- update latest PSJ command and utility

## [1.2.2]

- add link for every PSJ command and utility

## [1.2.1]

- use only TabNine binary for Windows

## [1.2.0]

- simplify keywords due to already used python package

## [1.1.9]

- add TabNine binaries to supply machine learning based autocompleter

## [1.1.8]

- remove snippets, pass to jupiterutils for intellisense

## [1.1.7]

- update latest PSJ commands and snippets

## [1.1.6]

- fix error: cannot write number in function names

## [1.1.5]

- add call tips to PSJ Utility

## [1.1.4]

- narrow down definition to specific methods

## [1.1.3]

- adding Go to definition

## [1.1.2]

- add missing "\_" in call tip function names

## [1.1.1]

- add missing "\_" in call tip function names

## [1.1.0]

- fix call tips bugs

## [1.0.9]

- adding Markdown string to functions' call tips

## [1.0.8]

- Restrict use to Python, adding Markdown string call tips

## [1.0.7]

- Update README.md

## [1.0.6]

- Add PSJ snippets tab into array and string

## [1.0.5]

- Add PSJ snippets

## [1.0.4]

- Add Python snippets

## [1.0.3]

- Fix vscode engines revision error

## [1.0.2]

- Fix untrimmed string bug

## [1.0.1]

- Add IntelliSense for PSJUtilityCalltips, PSJUtilityCalltips, Keywords

## [1.0.0]

- Initial release
