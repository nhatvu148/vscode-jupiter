```{module} MeshEdit.MoveNode.AlongEdge()
:synopsis:
```

(MeshEdit.MoveNode.AlongEdge)=

# MeshEdit.MoveNode.AlongEdge

## Description

## Syntax

```python
MeshEdit.MoveNode.AlongEdge(crlNode=[], bMoveX=False, bMoveY=False, bMoveZ=False, dPosX=0.0, dPosY=0.0, dPosZ=0.0, iMoveType=0)
```

Macro: {ref}`Macro-MeshEdit-MeshEditMoveNodeOnEdge`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> AlongEdge`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`bMoveX`**
: A _Boolean_ specifying the move x. The default value is False.

**`bMoveY`**
: A _Boolean_ specifying the move y. The default value is False.

**`bMoveZ`**
: A _Boolean_ specifying the move z. The default value is False.

**`dPosX`**
: A _Double_ specifying the position x. The default value is 0.0.

**`dPosY`**
: A _Double_ specifying the position y. The default value is 0.0.

**`dPosZ`**
: A _Double_ specifying the position z. The default value is 0.0.

**`iMoveType`**
: An _Integer_ specifying the move type. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.AlongEdge(crlNode=[], bMoveX=False, bMoveY=False, bMoveZ=False, dPosX=0.0, dPosY=0.0, dPosZ=0.0, iMoveType=0)
```
