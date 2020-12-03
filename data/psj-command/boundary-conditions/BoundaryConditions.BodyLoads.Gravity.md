```{module} BoundaryConditions.BodyLoads.Gravity()
:synopsis: create gravity
```

(BoundaryConditions.BodyLoads.Gravity)=

# BoundaryConditions.BodyLoads.Gravity

## Description

create gravity

## Syntax

```python
BoundaryConditions.BodyLoads.Gravity(strName, dlGravity, crCurCoord=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-Gravity`

Ribbon: {menuselection}`BoundaryConditions --> BodyLoads --> Gravity`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`dlGravity`**
: A _Double List_ specifying the gravity. This is a required input.

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
BoundaryConditions.BodyLoads.Gravity(strName, dlGravity, crCurCoord=None, crlTarget=[], crEdit=None)
```
