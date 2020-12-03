```{module} MeshCleanup.Cleanup.CloseGap()
:synopsis: Unknown Description
```

(MeshCleanup.Cleanup.CloseGap)=

# MeshCleanup.Cleanup.CloseGap

## Description

Unknown Description

## Syntax

```python
MeshCleanup.Cleanup.CloseGap(crlPartCur, dDistanceTol)
```

Macro: {ref}`Macro-MeshCleanup-CloseGaps`

Ribbon: {menuselection}`MeshCleanup --> Cleanup --> CloseGap`

## Inputs

**`crlPartCur`**
: A _Cursor List_ specifying the part cur. This is a required input.

**`dDistanceTol`**
: A _Double_ specifying the distance tolerance. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Cleanup.CloseGap(crlPartCur, dDistanceTol)
```
