```{module} MeshEdit.MoveNode.Scale()
:synopsis: Move node scale
```

(MeshEdit.MoveNode.Scale)=

# MeshEdit.MoveNode.Scale

## Description

Move node scale

## Syntax

```python
MeshEdit.MoveNode.Scale(crlNode=[], crlNodeOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0])
```

Macro: {ref}`Macro-MeshEdit-MeshEditMoveNodeScale`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> Scale`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crlNodeOrigin`**
: A _Cursor List_ specifying the node original. The default value is [].

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`posDeltaXYZ`**
: A _Position_ specifying the delta x y z. The default value is [10.0, 10.0, 10.0].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.Scale(crlNode=[], crlNodeOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0])
```
