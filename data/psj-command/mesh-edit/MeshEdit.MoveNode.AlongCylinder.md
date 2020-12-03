```{module} MeshEdit.MoveNode.AlongCylinder()
:synopsis: Move node along cylinder surface
```

(MeshEdit.MoveNode.AlongCylinder)=

# MeshEdit.MoveNode.AlongCylinder

## Description

Move node along cylinder surface

## Syntax

```python
MeshEdit.MoveNode.AlongCylinder(crlFace=[], crlNode=[], dIrX=0, dIrY=0, dIrZ=0, dCircleX=0, dCircleY=0, dCircleZ=0, dRadius=0, dHeight=0)
```

Macro: {ref}`Macro-MeshEdit-MoveNodeAlongCylinder`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> AlongCylinder`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`dIrX`**
: A _Double_ specifying the direction x. The default value is 0.

**`dIrY`**
: A _Double_ specifying the direction y. The default value is 0.

**`dIrZ`**
: A _Double_ specifying the direction z. The default value is 0.

**`dCircleX`**
: A _Double_ specifying the circle x. The default value is 0.

**`dCircleY`**
: A _Double_ specifying the circle y. The default value is 0.

**`dCircleZ`**
: A _Double_ specifying the circle z. The default value is 0.

**`dRadius`**
: A _Double_ specifying the radius. The default value is 0.

**`dHeight`**
: A _Double_ specifying the height. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.AlongCylinder(crlFace=[], crlNode=[], dIrX=0, dIrY=0, dIrZ=0, dCircleX=0, dCircleY=0, dCircleZ=0, dRadius=0, dHeight=0)
```
