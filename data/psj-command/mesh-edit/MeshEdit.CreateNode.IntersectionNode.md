```{module} MeshEdit.CreateNode.IntersectionNode()
:synopsis: create node by intersection node
```

(MeshEdit.CreateNode.IntersectionNode)=

# MeshEdit.CreateNode.IntersectionNode

## Description

create node by intersection node

## Syntax

```python
MeshEdit.CreateNode.IntersectionNode(crlFace, crlPart, crlEdge, crlNode)
```

Macro: {ref}`Macro-MeshEdit-CreateNodeIntersectionNode`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> IntersectionNode`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.IntersectionNode(crlFace, crlPart, crlEdge, crlNode)
```
