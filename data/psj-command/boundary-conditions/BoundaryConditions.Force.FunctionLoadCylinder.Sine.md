```{module} BoundaryConditions.Force.FunctionLoadCylinder.Sine()
:synopsis: Define the force load on selected entity based on the distribution of the sine function.
```

(BoundaryConditions.Force.FunctionLoadCylinder.Sine)=

# BoundaryConditions.Force.FunctionLoadCylinder.Sine

## Description

Define the force load on selected entity based on the distribution of the sine function.

## Syntax

```python
BoundaryConditions.Force.FunctionLoadCylinder.Sine(strName="ForceSine1", dFTotalForce=0.0, dA=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, bDistributeInAxis=False, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-ForceSine`

Ribbon: {menuselection}`BoundaryConditions --> Force --> FunctionLoadCylinder --> Sine`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "ForceSine1".

**`dFTotalForce`**
: A _Double_ specifying the total force. The default value is 0.0.

**`dA`**
: A _Double_ specifying the a. The default value is 0.0.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`iAngleBase`**
: An _Integer_ specifying the angle base. The default value is 0.

**`dAngleRange`**
: A _Double_ specifying the angle range. The default value is 0.0.

**`iEnArrowDir`**
: An _Integer_ specifying the en arrow direction. The default value is 0.

**`bDistributeInAxis`**
: A _Boolean_ specifying the distribute in axis. The default value is False.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Force.FunctionLoadCylinder.Sine(strName="ForceSine1", dFTotalForce=0.0, dA=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, bDistributeInAxis=False, crlTarget=[], crEdit=None)
```
