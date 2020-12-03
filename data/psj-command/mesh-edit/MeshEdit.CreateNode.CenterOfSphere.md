```{module} MeshEdit.CreateNode.CenterOfSphere()
:synopsis: Create node of center sphere
```

(MeshEdit.CreateNode.CenterOfSphere)=

# MeshEdit.CreateNode.CenterOfSphere

## Description

Create node of center sphere

## Syntax

```python
MeshEdit.CreateNode.CenterOfSphere(crlNodeOrFace=[], iNodeID=1)
```

Macro: {ref}`Macro-MeshEdit-MeshEditCreateNodeSphereCenter`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> CenterOfSphere`

## Inputs

**`crlNodeOrFace`**
: A _Cursor List_ specifying the node or face. The default value is [].

**`iNodeID`**
: An _Integer_ specifying the node ID. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.CenterOfSphere(crlNodeOrFace=[], iNodeID=1)
```
