```{module} MeshEdit.MoveNode.CoincidentNodes()
:synopsis: Coincident Nodes
```

(MeshEdit.MoveNode.CoincidentNodes)=

# MeshEdit.MoveNode.CoincidentNodes

## Description

Coincident Nodes

## Syntax

```python
MeshEdit.MoveNode.CoincidentNodes(crlNode=[], dTol=0.01, bDesOrder=False)
```

Macro: {ref}`Macro-MeshEdit-Coincident_Nodes`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> CoincidentNodes`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`dTol`**
: A _Double_ specifying the tolerance. The default value is 0.01.

**`bDesOrder`**
: A _Boolean_ specifying the des order. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.CoincidentNodes(crlNode=[], dTol=0.01, bDesOrder=False)
```
