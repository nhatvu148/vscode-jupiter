```{module} MeshEdit.CreateNode.CircleCenter()
:synopsis: create node at center of circle
```

(MeshEdit.CreateNode.CircleCenter)=

# MeshEdit.CreateNode.CircleCenter

## Description

create node at center of circle

## Syntax

```python
MeshEdit.CreateNode.CircleCenter(crlEdge, iNodeID, bImprint=False, crFace=None)
```

Macro: {ref}`Macro-MeshEdit-CreateNodeEdgeCenter`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> CircleCenter`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

**`iNodeID`**
: An _Integer_ specifying the node ID. This is a required input.

**`bImprint`**
: A _Boolean_ specifying the imprint. The default value is False.

**`crFace`**
: A _Cursor_ specifying the face. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.CircleCenter(crlEdge, iNodeID, bImprint=False, crFace=None)
```
