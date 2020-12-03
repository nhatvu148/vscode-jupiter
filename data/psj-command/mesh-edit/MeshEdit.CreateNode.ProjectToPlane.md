```{module} MeshEdit.CreateNode.ProjectToPlane()
:synopsis: create node point
```

(MeshEdit.CreateNode.ProjectToPlane)=

# MeshEdit.CreateNode.ProjectToPlane

## Description

create node point

## Syntax

```python
MeshEdit.CreateNode.ProjectToPlane(dX=0.0, dY=0.0, dZ=0.0, crlNode=[], crlFace=[])
```

Macro: {ref}`Macro-MeshEdit-MeshEditCreateNodeProjectNode`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> ProjectToPlane`

## Inputs

**`dX`**
: A _Double_ specifying the x. The default value is 0.0.

**`dY`**
: A _Double_ specifying the y. The default value is 0.0.

**`dZ`**
: A _Double_ specifying the z. The default value is 0.0.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.ProjectToPlane(dX=0.0, dY=0.0, dZ=0.0, crlNode=[], crlFace=[])
```
