```{module} MeshEdit.MoveNode.MoveNodeOffset()
:synopsis: Unknown Description
```

(MeshEdit.MoveNode.MoveNodeOffset)=

# MeshEdit.MoveNode.MoveNodeOffset

## Description

Unknown Description

## Syntax

```python
MeshEdit.MoveNode.MoveNodeOffset(dDeltaX, dDeltaY, dDeltaZ, crlNode, crCoord)
```

Macro: {ref}`Macro-MeshEdit-MoveNodeOffset`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> MoveNodeOffset`

## Inputs

**`dDeltaX`**
: A _Double_ specifying the delta x. This is a required input.

**`dDeltaY`**
: A _Double_ specifying the delta y. This is a required input.

**`dDeltaZ`**
: A _Double_ specifying the delta z. This is a required input.

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

**`crCoord`**
: A _Cursor_ specifying the coordinate. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.MoveNodeOffset(dDeltaX, dDeltaY, dDeltaZ, crlNode, crCoord)
```
