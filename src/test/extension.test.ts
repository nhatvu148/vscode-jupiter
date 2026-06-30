import * as assert from "assert";
import * as vscode from "vscode";
import { buildReferenceLink } from "../extension";
import { allApiEntries, allKeywords, lookupApi } from "../jupiterApi";

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
  test("exposes the merged API surface (~1800+ entries)", () => {
    assert.ok(
      allApiEntries().length > 1800,
      `expected >1800 entries, got ${allApiEntries().length}`,
    );
  });

  test("preserves rich docs for an existing command", () => {
    const entry = lookupApi("FileMenu.Save");
    assert.ok(entry, "FileMenu.Save should be a known API entry");
    assert.strictEqual(entry.prefix, "Save");
    assert.match(entry.doc, /Save file JTDB/); // rich text preserved, not a stub
  });

  test("returns undefined for an unknown name", () => {
    assert.strictEqual(lookupApi("Not.A.Real.Command"), undefined);
  });

  test("exposes PSJ utility + GUI keywords", () => {
    const labels = new Set(allKeywords().map((k) => k.label));
    assert.ok(labels.has("add_button"), "GUI keyword add_button missing");
    assert.ok(allKeywords().length > 500);
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
