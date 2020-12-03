```{module} MeshEdit.CreateNode.CenterOfGravity()
:synopsis: create node Center Of Gravity
```

(MeshEdit.CreateNode.CenterOfGravity)=

# MeshEdit.CreateNode.CenterOfGravity

## Description

create node Center Of Gravity

## Syntax

```python
MeshEdit.CreateNode.CenterOfGravity(iCreationType=1, iNodeID=0, dX=0.0, dY=0.0, dZ=0.0, crlPart=[], crlBarPart=[], crlFace=[])
```

Macro: {ref}`Macro-MeshEdit-MeshEditCreateNodeCenterofGravity`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> CenterOfGravity`

## Inputs

**`iCreationType`**
: An _Integer_ specifying the creation type. The default value is 1.

**`iNodeID`**
: An _Integer_ specifying the node ID. The default value is 0.

**`dX`**
: A _Double_ specifying the x. The default value is 0.0.

**`dY`**
: A _Double_ specifying the y. The default value is 0.0.

**`dZ`**
: A _Double_ specifying the z. The default value is 0.0.

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlBarPart`**
: A _Cursor List_ specifying the bar part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.CenterOfGravity(iCreationType=1, iNodeID=0, dX=0.0, dY=0.0, dZ=0.0, crlPart=[], crlBarPart=[], crlFace=[])
```
