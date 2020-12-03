```{module} BoundaryConditions.Force.FunctionLoadCylinder.Quadratic()
:synopsis: Create Force (Quadratic) y = a*x^2 +
```

(BoundaryConditions.Force.FunctionLoadCylinder.Quadratic)=

# BoundaryConditions.Force.FunctionLoadCylinder.Quadratic

## Description

Create Force (Quadratic) y = a\*x^2 +

## Syntax

```python
BoundaryConditions.Force.FunctionLoadCylinder.Quadratic(strName="ForceQuadratic1", dFTotalForce=0.0, dA=0.0, dB=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-ForceQuadratic`

Ribbon: {menuselection}`BoundaryConditions --> Force --> FunctionLoadCylinder --> Quadratic`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "ForceQuadratic1".

**`dFTotalForce`**
: A _Double_ specifying the total force. The default value is 0.0.

**`dA`**
: A _Double_ specifying the a. The default value is 0.0.

**`dB`**
: A _Double_ specifying the . The default value is 0.0.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`iAngleBase`**
: An _Integer_ specifying the angle base. The default value is 0.

**`dAngleRange`**
: A _Double_ specifying the angle range. The default value is 0.0.

**`iEnArrowDir`**
: An _Integer_ specifying the en arrow direction. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Force.FunctionLoadCylinder.Quadratic(strName="ForceQuadratic1", dFTotalForce=0.0, dA=0.0, dB=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, crlTarget=[], crEdit=None)
```
