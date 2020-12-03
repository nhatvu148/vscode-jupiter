```{module} BoundaryConditions.Force.ForceNormalDirection()
:synopsis: Create Force (normal direction)
```

(BoundaryConditions.Force.ForceNormalDirection)=

# BoundaryConditions.Force.ForceNormalDirection

## Description

Create Force (normal direction)

## Syntax

```python
BoundaryConditions.Force.ForceNormalDirection(strName, vecForce=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iEnArrowDir=0, iDistributionMethod=0, crCurCoord=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-ForceNormalDirection`

Ribbon: {menuselection}`BoundaryConditions --> Force --> ForceNormalDirection`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`vecForce`**
: A _Vector_ specifying the force. The default value is [DFLT_DBL, DFLT_DBL, DFLT_DBL].

**`iEnArrowDir`**
: An _Integer_ specifying the en arrow direction. The default value is 0.

**`iDistributionMethod`**
: An _Integer_ specifying the distribution method. The default value is 0.

**`crCurCoord`**
: A _Cursor_ specifying the cur coordinate. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Force.ForceNormalDirection(strName, vecForce=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iEnArrowDir=0, iDistributionMethod=0, crCurCoord=None, crlTarget=[], crEdit=None)
```
