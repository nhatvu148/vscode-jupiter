```{module} BoundaryConditions.FixedConstraint()
:synopsis: create FixedConstraint
```

(BoundaryConditions.FixedConstraint)=

# BoundaryConditions.FixedConstraint

## Description

create FixedConstraint

## Syntax

```python
BoundaryConditions.FixedConstraint(strName="Constraint1", iDwDof=7, crCurCoord=None, iType=0, iUsetType=0, crTable=None, bAbaqusFixed=False, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-FixedConstraint`

Ribbon: {menuselection}`BoundaryConditions --> FixedConstraint`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "Constraint1".

**`iDwDof`**
: An _Integer_ specifying the dw dof. The default value is 7.

**`crCurCoord`**
: A _Cursor_ specifying the cur coordinate. The default value is None.

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`iUsetType`**
: An _Integer_ specifying the uset type. The default value is 0.

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`bAbaqusFixed`**
: A _Boolean_ specifying the abaqus fixed. The default value is False.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.FixedConstraint(strName="Constraint1", iDwDof=7, crCurCoord=None, iType=0, iUsetType=0, crTable=None, bAbaqusFixed=False, crlTarget=[], crEdit=None)
```
