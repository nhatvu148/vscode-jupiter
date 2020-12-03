```{module} MeshEdit.MoveNode.Point()
:synopsis: Move node(s) to an Face(Edge) Point position
```

(MeshEdit.MoveNode.Point)=

# MeshEdit.MoveNode.Point

## Description

Move node(s) to an Face(Edge) Point position

## Syntax

```python
MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])
```

Macro: {ref}`Macro-MeshEdit-MoveNodePoint`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> Point`

## Inputs

**`dX`**
: A _Double_ specifying the x. The default value is 0.0.

**`dY`**
: A _Double_ specifying the y. The default value is 0.0.

**`dZ`**
: A _Double_ specifying the z. The default value is 0.0.

**`ilNodeList`**
: A _Integer List_ specifying the node list. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])
```
