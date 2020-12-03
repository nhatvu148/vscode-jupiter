```{module} MeshEdit.MoveNode.StraightenMidnodes()
:synopsis: move node by straighten_mid_nodes
```

(MeshEdit.MoveNode.StraightenMidnodes)=

# MeshEdit.MoveNode.StraightenMidnodes

## Description

move node by straighten_mid_nodes

## Syntax

```python
MeshEdit.MoveNode.StraightenMidnodes(crlPart=[], crlFace=[], crlEdge=[], crlNode=[])
```

Macro: {ref}`Macro-MeshEdit-MoveNodeStraightenMidNodesCr`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> StraightenMidnodes`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`crlEdge`**
: A _Cursor List_ specifying the edge. The default value is [].

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.StraightenMidnodes(crlPart=[], crlFace=[], crlEdge=[], crlNode=[])
```
