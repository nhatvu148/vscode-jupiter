```{module} MeshEdit.MoveNode.Absolute()
:synopsis: move node absolute
```

(MeshEdit.MoveNode.Absolute)=

# MeshEdit.MoveNode.Absolute

## Description

move node absolute

## Syntax

```python
MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNode=[], crCoord=None)
```

Macro: {ref}`Macro-MeshEdit-MoveNodeAbsoluteCr`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> Absolute`

## Inputs

**`dDeltaX`**
: A _Double_ specifying the delta x. The default value is 0.0.

**`dDeltaY`**
: A _Double_ specifying the delta y. The default value is 0.0.

**`dDeltaZ`**
: A _Double_ specifying the delta z. The default value is 0.0.

**`b1stCoord`**
: A _B1ST_COORD_ specifying the coordinate. The default value is True.

**`b2ndCoord`**
: A _B2ND_COORD_ specifying the coordinate. The default value is True.

**`b3rdCoord`**
: A _B3RD_COORD_ specifying the coordinate. The default value is True.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNode=[], crCoord=None)
```
