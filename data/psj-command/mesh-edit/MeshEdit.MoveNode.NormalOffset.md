```{module} MeshEdit.MoveNode.NormalOffset()
:synopsis: Move node(s) in Normal Direction of plane
```

(MeshEdit.MoveNode.NormalOffset)=

# MeshEdit.MoveNode.NormalOffset

## Description

Move node(s) in Normal Direction of plane

## Syntax

```python
MeshEdit.MoveNode.NormalOffset(dMagnitude=0.0, ilNodeList=[])
```

Macro: {ref}`Macro-MeshEdit-MoveNodeNormalOffset`

Ribbon: {menuselection}`MeshEdit --> MoveNode --> NormalOffset`

## Inputs

**`dMagnitude`**
: A _Double_ specifying the magnitude. The default value is 0.0.

**`ilNodeList`**
: A _Integer List_ specifying the node list. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MoveNode.NormalOffset(dMagnitude=0.0, ilNodeList=[])
```
