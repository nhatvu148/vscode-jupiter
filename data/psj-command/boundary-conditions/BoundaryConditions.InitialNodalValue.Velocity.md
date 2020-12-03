```{module} BoundaryConditions.InitialNodalValue.Velocity()
:synopsis: Unknown Description
```

(BoundaryConditions.InitialNodalValue.Velocity)=

# BoundaryConditions.InitialNodalValue.Velocity

## Description

Unknown Description

## Syntax

```python
BoundaryConditions.InitialNodalValue.Velocity(strName="InitialRotationAngle1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-InitialDynamic`

Ribbon: {menuselection}`BoundaryConditions --> InitialNodalValue --> Velocity`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "InitialRotationAngle1".

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
BoundaryConditions.InitialNodalValue.Velocity(strName="InitialRotationAngle1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None)
```
