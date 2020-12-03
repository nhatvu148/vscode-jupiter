```{module} MeshEdit.MoveNode.AlongDirection()
:synopsis:
```

(MeshEdit.MoveNode.AlongDirection)=

# MeshEdit.MoveNode.AlongDirection

## Description

## Syntax

```python
MeshEdit.MoveNode.AlongDirection(crlNode=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False)
```

Macro: {ref}`Macro-MeshEdit-NodeMovedByDirection`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> AlongDirection`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crElem`**
: A _Cursor_ specifying the element. The default value is None.

**`crFace`**
: A _Cursor_ specifying the face. The default value is None.

**`vecDirection`**
: A _Vector_ specifying the direction. The default value is [0,0,0].

**`dMagnitude`**
: A _Double_ specifying the magnitude. The default value is 0.0.

**`bDestination`**
: A _Boolean_ specifying the destination. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.AlongDirection(crlNode=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False)
```
