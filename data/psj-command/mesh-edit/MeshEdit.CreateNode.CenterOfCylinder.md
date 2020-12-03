```{module} MeshEdit.CreateNode.CenterOfCylinder()
:synopsis: Create node of center cylinder
```

(MeshEdit.CreateNode.CenterOfCylinder)=

# MeshEdit.CreateNode.CenterOfCylinder

## Description

Create node of center cylinder

## Syntax

```python
MeshEdit.CreateNode.CenterOfCylinder(crlFace=[], iNodeID=1)
```

Macro: {ref}`Macro-MeshEdit-MeshEditCreateNodeCylindCenter`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> CenterOfCylinder`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`iNodeID`**
: An _Integer_ specifying the node ID. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.CenterOfCylinder(crlFace=[], iNodeID=1)
```
