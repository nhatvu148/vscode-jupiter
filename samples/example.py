# Sample PSJ (Python Script in Jupiter) file for testing the extension.
#
# How to use:
#   1. Press F5 in the extension project -> a new "Extension Development Host"
#      window opens with THIS folder loaded.
#   2. Open this file there.
#   3. HOVER any of the calls below -> you should see the documented signature
#      (arguments, types, return) plus a "See reference here" link.
#   4. On a blank line, start typing a command name (e.g. "Save", "FindEntities",
#      "GetThickness") -> Jupiter API completions appear with docs.

# --- Hover over these known commands/utilities ---

FileMenu.Open("model.jtdb")
FileMenu.Save("model.jtdb")
FileMenu.AddJTDB("part.jtdb", "merge", "main", "")

Utility.FindEntities("Bracket", "Name", True)

ACModeling.CloseHoleAuto(parts)

thickness = JPT.GetThicknessOfEntity(JPT.EntityType.FACE, 1)
lbcs = JPT.GetAllLoadBoundaryConditions()


# --- Try completion here: type a command name on the next line ---
# e.g. start typing:  AddJTDB  /  FindEntities  /  GetThickness  /  add_button

# --- Try SIGNATURE HELP: type the "(" and watch the parameter hints ---
# FileMenu.AddJTDB(
# dlg.add_button(
