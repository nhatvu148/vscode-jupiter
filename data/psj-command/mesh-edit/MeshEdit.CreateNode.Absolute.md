```{module} MeshEdit.CreateNode.Absolute()
:synopsis: create node by input direct value
```

(MeshEdit.CreateNode.Absolute)=

# MeshEdit.CreateNode.Absolute

## Description

create node by input direct value

## Syntax

```python
MeshEdit.CreateNode.Absolute(veclNodeCoord=[], ilNewNodeID=[])
```

Macro: {ref}`Macro-MeshEdit-CreateNode`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> Absolute`

## Inputs

**`veclNodeCoord`**
: A _Vector List_ specifying the node coordinate. The default value is [].

**`ilNewNodeID`**
: A _Integer List_ specifying the new node ID. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.Absolute(veclNodeCoord=[], ilNewNodeID=[])
```
