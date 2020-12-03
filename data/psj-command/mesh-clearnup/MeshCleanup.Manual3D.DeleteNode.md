```{module} MeshCleanup.Manual3D.DeleteNode()
:synopsis: remove node for solid element.
```

(MeshCleanup.Manual3D.DeleteNode)=

# MeshCleanup.Manual3D.DeleteNode

## Description

remove node for solid element.

## Syntax

```python
MeshCleanup.Manual3D.DeleteNode(crlNode)
```

Macro: {ref}`Macro-MeshCleanup-CleanupRemoveNode`

Ribbon: {menuselection}`MeshCleanup --> Manual3D --> DeleteNode`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual3D.DeleteNode(crlNode)
```
