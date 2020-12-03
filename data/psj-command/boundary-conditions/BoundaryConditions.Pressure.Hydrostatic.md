```{module} BoundaryConditions.Pressure.Hydrostatic()
:synopsis: Boundary Conditions HPressure
```

(BoundaryConditions.Pressure.Hydrostatic)=

# BoundaryConditions.Pressure.Hydrostatic

## Description

Boundary Conditions HPressure

## Syntax

```python
BoundaryConditions.Pressure.Hydrostatic(strName="PressureHydrostatic1", dFHPressure=0.0, dFDensity=0.0, iDensityUnit=0, dFGravity=0.0, iGravityUnit=0, iGravityDir=0, dFWaterSuface=0.0, iSufaceUnit=0, iDistributionMethod=0, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-PressureHydrostatic`

Ribbon: {menuselection}`BoundaryConditions --> Pressure --> Hydrostatic`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "PressureHydrostatic1".

**`dFHPressure`**
: A _Double_ specifying the h pressure. The default value is 0.0.

**`dFDensity`**
: A _Double_ specifying the density. The default value is 0.0.

**`iDensityUnit`**
: An _Integer_ specifying the density unit. The default value is 0.

**`dFGravity`**
: A _Double_ specifying the gravity. The default value is 0.0.

**`iGravityUnit`**
: An _Integer_ specifying the gravity unit. The default value is 0.

**`iGravityDir`**
: An _Integer_ specifying the gravity direction. The default value is 0.

**`dFWaterSuface`**
: A _Double_ specifying the water suface. The default value is 0.0.

**`iSufaceUnit`**
: An _Integer_ specifying the suface unit. The default value is 0.

**`iDistributionMethod`**
: An _Integer_ specifying the distribution method. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Pressure.Hydrostatic(strName="PressureHydrostatic1", dFHPressure=0.0, dFDensity=0.0, iDensityUnit=0, dFGravity=0.0, iGravityUnit=0, iGravityDir=0, dFWaterSuface=0.0, iSufaceUnit=0, iDistributionMethod=0, crlTarget=[], crEdit=None)
```
