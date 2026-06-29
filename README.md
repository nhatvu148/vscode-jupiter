# JUPITER

Language support for **PSJ** (Python Script in Jupiter) and **JPL** (Jupiter Macro) in Visual Studio Code — built for the CAD/CAE engineers who automate [Jupiter](https://psjdoc.e-technostar.com/) with Python.

## Features

- **PSJ / JPT API completion** — IntelliSense for ~700 Jupiter commands and `JPT` utilities, each with a documented signature (arguments, types, return value, examples) pulled straight from the PSJ command reference.
- **Hover docs** — hover any known PSJ/JPT call to see its full signature inline, plus a one-click link to the official reference page.
- **Syntax highlighting** — a TextMate grammar for `.jpl` Jupiter macro files.
- **Lightweight & fast** — no background processes, no native binaries; the whole extension is a single ~270 KB bundle.

## Usage

Open a Python (PSJ) or `.jpl` (JPL) file and start typing a Jupiter command — completions appear automatically. Hover a call such as `FileMenu.Save(...)` or `JPT.GetVersion()` to read its documentation.

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

## License

[MIT](LICENSE)
