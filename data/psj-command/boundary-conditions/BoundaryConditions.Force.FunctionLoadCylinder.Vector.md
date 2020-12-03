```{module} BoundaryConditions.Force.FunctionLoadCylinder.Vector()
:synopsis: Define the force load on selected entity based on the distribution of the vector function.
```

(BoundaryConditions.Force.FunctionLoadCylinder.Vector)=

# BoundaryConditions.Force.FunctionLoadCylinder.Vector

## Description

Define the force load on selected entity based on the distribution of the vector function.

## Syntax

```python
BoundaryConditions.Force.FunctionLoadCylinder.Vector(strName="ForceVector1", dFTotalForce=DFLT_DBL, dA=DFLT_DBL, dX=DFLT_DBL, dY=DFLT_DBL, crCoord=None, iEnDirection=0, dAngleRange=0.0, iArrowDir=0, bDistributeInAxis=False, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-ForceVector`

Ribbon: {menuselection}`BoundaryConditions --> Force --> FunctionLoadCylinder --> Vector`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "ForceVector1".

**`dFTotalForce`**
: A _Double_ specifying the total force. The default value is DFLT_DBL.

**`dA`**
: A _Double_ specifying the a. The default value is DFLT_DBL.

**`dX`**
: A _Double_ specifying the x. The default value is DFLT_DBL.

**`dY`**
: A _Double_ specifying the y. The default value is DFLT_DBL.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`iEnDirection`**
: An _Integer_ specifying the en direction. The default value is 0.

**`dAngleRange`**
: A _Double_ specifying the angle range. The default value is 0.0.

**`iArrowDir`**
: An _Integer_ specifying the arrow direction. The default value is 0.

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
BoundaryConditions.Force.FunctionLoadCylinder.Vector(strName="ForceVector1", dFTotalForce=DFLT_DBL, dA=DFLT_DBL, dX=DFLT_DBL, dY=DFLT_DBL, crCoord=None, iEnDirection=0, dAngleRange=0.0, iArrowDir=0, bDistributeInAxis=False, crlTarget=[], crEdit=None)
```
