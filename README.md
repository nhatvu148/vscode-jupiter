# JUPITER

Language support for **PSJ** (Python Script in Jupiter) and **JPL** (Jupiter Macro) in Visual Studio Code — built for the CAD/CAE engineers who automate [Jupiter](https://psjdoc.e-technostar.com/) with Python.

## Features

- **PSJ / JPT / GUI completion** — IntelliSense for 2,200+ Jupiter commands, `JPT` utilities, and `JDGCreator` GUI-builder methods, each with an accurate signature (real parameter names, defaults, and types).
- **Signature help** — parameter hints appear as you type a call, with the active argument highlighted.
- **Hover docs** — hover any known PSJ/JPT call for its full signature, description, and inputs, plus a one-click link to the official reference page.
- **Keyword completions** — PSJ utility constants (`ELEMTYPE_HEX8`, …) and PSJ-GUI keywords.
- **Syntax highlighting** — a TextMate grammar for `.jpl` Jupiter macro files.
- **Lightweight & fast** — no background processes and no native binaries; just static, in-editor data.

## Usage

Open a Python (PSJ) or `.jpl` (JPL) file and start typing a Jupiter command — completions appear automatically. Type `(` after a call such as `FileMenu.AddJTDB(` to see signature hints, or hover `JPT.GetThicknessOfEntity(...)` to read its documentation.

## About PSJ

**PSJ** (_Python Script in Jupiter_) lets engineers customize and automate Jupiter. Operations performed in the Jupiter UI generate a Python macro that can be replayed or extended into advanced scripting across different models and specifications.

Typical users:

- **CAD designers** automating simple, repeated analysis with their own design rules.
- **CAE engineers** shortening modelling time and reducing manual workload.
- **CAE experts** doing advanced modelling that needs software interaction and data I/O.
- **CAE teams** building an in-house CAD–CAE automation pipeline, from concept design to analysis report.

## Notes

- This is a community project maintained by [@nhatvu148](https://github.com/nhatvu148); it is not an official e-technostar product.
- As of **v1.3.0** the bundled TabNine autocompleter was removed (it caused high CPU load). For AI completions, use a dedicated tool such as GitHub Copilot alongside this extension.

## Contributing

Issues and PRs welcome at <https://github.com/nhatvu148/vscode-jupiter>.

```bash
yarn install
yarn compile      # esbuild bundle -> dist/
yarn test         # @vscode/test-cli integration tests
yarn package      # produce a .vsix
```

### API data

`src/data.ts` is generated (not hand-edited) from the internal Jupiter API
sources via `yarn generate`, so signatures, defaults and docstrings stay
accurate. Regenerating it requires access to those internal sources and is a
maintainer-only task — see `scripts/generate.mjs`.

## License

[MIT](LICENSE)
