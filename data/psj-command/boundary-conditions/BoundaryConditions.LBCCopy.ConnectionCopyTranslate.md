```{module} BoundaryConditions.LBCCopy.ConnectionCopyTranslate()
:synopsis: Copy connection translate
```

(BoundaryConditions.LBCCopy.ConnectionCopyTranslate)=

# BoundaryConditions.LBCCopy.ConnectionCopyTranslate

## Description

Copy connection translate

## Syntax

```python
BoundaryConditions.LBCCopy.ConnectionCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTarget=[])
```

Macro: {ref}`Macro-BoundaryConditions-ConnectionCopyTranslate`

Ribbon: {menuselection}`BoundaryConditions --> LBCCopy --> ConnectionCopyTranslate`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iMatchMethod`**
: An _Integer_ specifying the match method. The default value is 0.

**`posVecTrans`**
: A _Position_ specifying the vector trans. The default value is [0,0,0].

**`dMagnitude`**
: A _Double_ specifying the magnitude. The default value is 1.

**`dTrandataDoffset`**
: A _Double_ specifying the trandata offset. The default value is 0.0.

**`dTol`**
: A _Double_ specifying the tolerance. The default value is 1.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.LBCCopy.ConnectionCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTarget=[])
```
