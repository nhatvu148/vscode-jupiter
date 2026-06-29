import * as assert from "assert";
import * as vscode from "vscode";
import { buildReferenceLink } from "../extension";
import { allApiEntries, lookupApi } from "../jupiterApi";

const EXTENSION_ID = "nhatvu148.jupiter";

suite("buildReferenceLink", () => {
  test("maps a JPT utility to the psj-utility docs path", () => {
    assert.strictEqual(
      buildReferenceLink("JPT.GetVersion"),
      "https://psjdoc.e-technostar.com/docs/psj-utility/JPT.GetVersion",
    );
  });

  test("maps a PSJ command to a kebab-cased category path", () => {
    assert.strictEqual(
      buildReferenceLink("MeshControl.SetSize"),
      "https://psjdoc.e-technostar.com/docs/psj-command/mesh-control/MeshControl.SetSize",
    );
  });

  test("handles a single-word command category", () => {
    assert.strictEqual(
      buildReferenceLink("Solver.Run"),
      "https://psjdoc.e-technostar.com/docs/psj-command/solver/Solver.Run",
    );
  });
});

suite("jupiterApi", () => {
  test("exposes a non-empty API surface", () => {
    assert.ok(allApiEntries().length > 100);
  });

  test("looks up a known command with its docs and leaf prefix", () => {
    const entry = lookupApi("FileMenu.Save");
    assert.ok(entry, "FileMenu.Save should be a known API entry");
    assert.strictEqual(entry.prefix, "Save");
    assert.match(entry.doc, /FileMenu\.Save/);
  });

  test("returns undefined for an unknown name", () => {
    assert.strictEqual(lookupApi("Not.A.Real.Command"), undefined);
  });
});

suite("extension", () => {
  test("is present and activates", async () => {
    const ext = vscode.extensions.getExtension(EXTENSION_ID);
    assert.ok(ext, `extension ${EXTENSION_ID} should be installed`);
    await ext.activate();
    assert.strictEqual(ext.isActive, true);
  });
});
