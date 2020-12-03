```{module} MeshEdit.MoveNode.ProjectToLine()
:synopsis: move node by project to line
```

(MeshEdit.MoveNode.ProjectToLine)=

# MeshEdit.MoveNode.ProjectToLine

## Description

move node by project to line

## Syntax

```python
MeshEdit.MoveNode.ProjectToLine(crlRefNodes=[], crlObjNodes=[], iType=0)
```

Macro: {ref}`Macro-MeshEdit-MoveNodeAlignNodeCr`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> ProjectToLine`

## Inputs

**`crlRefNodes`**
: A _Cursor List_ specifying the reference nodes. The default value is [].

**`crlObjNodes`**
: A _Cursor List_ specifying the object nodes. The default value is [].

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.ProjectToLine(crlRefNodes=[], crlObjNodes=[], iType=0)
```
