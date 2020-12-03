```{module} BoundaryConditions.LBCCopy.LBCCopyRotate()
:synopsis: Copy LBC rotate
```

(BoundaryConditions.LBCCopy.LBCCopyRotate)=

# BoundaryConditions.LBCCopy.LBCCopyRotate

## Description

Copy LBC rotate

## Syntax

```python
BoundaryConditions.LBCCopy.LBCCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTarget=[])
```

Macro: {ref}`Macro-BoundaryConditions-LBCCopyRotate`

Ribbon: {menuselection}`BoundaryConditions --> LBCCopy --> LBCCopyRotate`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 1.

**`iMatchMethod`**
: An _Integer_ specifying the match method. The default value is 0.

**`posAxis`**
: A _Position_ specifying the axis. The default value is [0,0,0].

**`posCenter`**
: A _Position_ specifying the center. The default value is [0,0,0].

**`dAngle`**
: A _Double_ specifying the angle. The default value is 0.0.

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
BoundaryConditions.LBCCopy.LBCCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTarget=[])
```
