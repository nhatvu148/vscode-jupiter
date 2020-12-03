```{module} BoundaryConditions.LBCCopy.ConnectionCopyMirror()
:synopsis: Copy Connection mirror
```

(BoundaryConditions.LBCCopy.ConnectionCopyMirror)=

# BoundaryConditions.LBCCopy.ConnectionCopyMirror

## Description

Copy Connection mirror

## Syntax

```python
BoundaryConditions.LBCCopy.ConnectionCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTarget=[])
```

Macro: {ref}`Macro-BoundaryConditions-ConnectionCopyMirror`

Ribbon: {menuselection}`BoundaryConditions --> LBCCopy --> ConnectionCopyMirror`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 2.

**`iMatchMethod`**
: An _Integer_ specifying the match method. The default value is 0.

**`poslPoints`**
: A _Position List_ specifying the points. The default value is [].

**`dOffset`**
: A _Double_ specifying the offset. The default value is 0.

**`dTol`**
: A _Double_ specifying the tolerance. The default value is 1.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.LBCCopy.ConnectionCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTarget=[])
```
