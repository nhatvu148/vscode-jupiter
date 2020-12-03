```{module} BoundaryConditions.InitialNodalValue.RotationAngle()
:synopsis: Unknown Description
```

(BoundaryConditions.InitialNodalValue.RotationAngle)=

# BoundaryConditions.InitialNodalValue.RotationAngle

## Description

Unknown Description

## Syntax

```python
BoundaryConditions.InitialNodalValue.RotationAngle(strName="InitialVelocity1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-InitialDynamic`

Ribbon: {menuselection}`BoundaryConditions --> InitialNodalValue --> RotationAngle`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "InitialVelocity1".

**`stData`**
: A _ST_DATA_ specifying the data. The default value is LBC_DYNAMIC_INITIAL_CONDITION_DATA().

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.InitialNodalValue.RotationAngle(strName="InitialVelocity1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None)
```
