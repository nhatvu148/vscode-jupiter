```{module} MeshCleanup.Manual3D.Swap()
:synopsis: cleanup element edge by swap
```

(MeshCleanup.Manual3D.Swap)=

# MeshCleanup.Manual3D.Swap

## Description

cleanup element edge by swap

## Syntax

```python
MeshCleanup.Manual3D.Swap(crplElemEdge)
```

Macro: {ref}`Macro-MeshCleanup-CleanupSwap`

Ribbon: {menuselection}`MeshCleanup --> Manual3D --> Swap`

## Inputs

**`crplElemEdge`**
: A _Cursor Pair List_ specifying the element edge. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual3D.Swap(crplElemEdge)
```
