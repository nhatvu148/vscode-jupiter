```{module} MeshEdit.MoveNode.Offset()
:synopsis: MeshEdit MoveNode MoveNodeOffset
```

(MeshEdit.MoveNode.Offset)=

# MeshEdit.MoveNode.Offset

## Description

MeshEdit MoveNode MoveNodeOffset

## Syntax

```python
MeshEdit.MoveNode.Offset(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crCoord=None, crlNode=[])
```

Macro: {ref}`Macro-MeshEdit-MeshEditMoveNodeOffset`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> Offset`

## Inputs

**`dDeltaX`**
: A _Double_ specifying the delta x. The default value is 0.0.

**`dDeltaY`**
: A _Double_ specifying the delta y. The default value is 0.0.

**`dDeltaZ`**
: A _Double_ specifying the delta z. The default value is 0.0.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.Offset(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crCoord=None, crlNode=[])
```
