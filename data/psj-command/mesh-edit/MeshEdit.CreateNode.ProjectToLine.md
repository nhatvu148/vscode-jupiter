```{module} MeshEdit.CreateNode.ProjectToLine()
:synopsis: create node by projection to line
```

(MeshEdit.CreateNode.ProjectToLine)=

# MeshEdit.CreateNode.ProjectToLine

## Description

create node by projection to line

## Syntax

```python
MeshEdit.CreateNode.ProjectToLine(crlTa)
```

Macro: {ref}`Macro-MeshEdit-CreateNodeProjectToLine`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> ProjectToLine`

## Inputs

**`crlTa`**
: A _Cursor List_ specifying the list node. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.ProjectToLine(crlTa)
```
