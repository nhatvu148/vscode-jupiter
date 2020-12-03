```{module} MeshCleanup.CloseGap()
:synopsis: MeshCleanup Cleanup CloseGap
```

(MeshCleanup.CloseGap)=

# MeshCleanup.CloseGap

## Description

MeshCleanup Cleanup CloseGap

## Syntax

```python
MeshCleanup.CloseGap(crlPartCur=[], dDistanceTol=0.01)
```

Macro: {ref}`Macro-MeshCleanup-CloseGaps`

Ribbon: {menuselection}`MeshCleanup --> CloseGap`

## Inputs

**`crlPartCur`**
: A _Cursor List_ specifying the part cur. The default value is [].

**`dDistanceTol`**
: A _Double_ specifying the distance tolerance. The default value is 0.01.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.CloseGap(crlPartCur=[], dDistanceTol=0.01)
```
