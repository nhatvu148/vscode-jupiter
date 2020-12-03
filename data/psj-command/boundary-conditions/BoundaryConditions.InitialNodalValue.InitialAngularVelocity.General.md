```{module} BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General()
:synopsis: Unknown Description
```

(BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General)=

# BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General

## Description

Unknown Description

## Syntax

```python
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General(strName="InitialAngularVelocity1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-InitialDynamic`

Ribbon: {menuselection}`BoundaryConditions --> InitialNodalValue --> InitialAngularVelocity --> General`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "InitialAngularVelocity1".

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
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General(strName="InitialAngularVelocity1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None)
```
