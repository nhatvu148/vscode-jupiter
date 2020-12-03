```{module} MeshCleanup.Manual2D.Split()
:synopsis: manual cleanup by split
```

(MeshCleanup.Manual2D.Split)=

# MeshCleanup.Manual2D.Split

## Description

manual cleanup by split

## Syntax

```python
MeshCleanup.Manual2D.Split(crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None)
```

Macro: {ref}`Macro-MeshCleanup-SplitElemEdge`

Ribbon: {menuselection}`MeshCleanup --> Manual2D --> Split`

## Inputs

**`crplElemEdge`**
: A _Cursor Pair List_ specifying the element edge. This is a required input.

**`dRatio`**
: A _Double_ specifying the ratio. The default value is 0.0.

**`crNodeRef`**
: A _Cursor_ specifying the node reference. The default value is None.

**`crProjectPart`**
: A _Cursor_ specifying the project part. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual2D.Split(crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None)
```
