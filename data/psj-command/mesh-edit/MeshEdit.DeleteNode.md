```{module} MeshEdit.DeleteNode()
:synopsis: Delete floating nodes in db
```

(MeshEdit.DeleteNode)=

# MeshEdit.DeleteNode

## Description

Delete floating nodes in db

## Syntax

```python
MeshEdit.DeleteNode(crlNode=[], bRemoveVertex=True)
```

Macro: {ref}`Macro-MeshEdit-DeleteNode`

Ribbon: {menuselection}`MeshEdit --> DeleteNode`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`bRemoveVertex`**
: A _Boolean_ specifying the remove vertex. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.DeleteNode(crlNode=[], bRemoveVertex=True)
```
