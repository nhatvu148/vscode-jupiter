```{module} MeshCleanup.Manual3D.Split()
:synopsis: Merge two Quad elements into one Quad element
```

(MeshCleanup.Manual3D.Split)=

# MeshCleanup.Manual3D.Split

## Description

Merge two Quad elements into one Quad element

## Syntax

```python
MeshCleanup.Manual3D.Split(crplElemEdge, crlNode=[], dRatioDistance=0.5)
```

Macro: {ref}`Macro-MeshCleanup-CleanupSplit`

Ribbon: {menuselection}`MeshCleanup --> Manual3D --> Split`

## Inputs

**`crplElemEdge`**
: A _Cursor Pair List_ specifying the element edge. This is a required input.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`dRatioDistance`**
: A _Double_ specifying the ratio distance. The default value is 0.5.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual3D.Split(crplElemEdge, crlNode=[], dRatioDistance=0.5)
```
