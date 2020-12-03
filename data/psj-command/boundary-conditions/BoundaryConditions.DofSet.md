```{module} BoundaryConditions.DofSet()
:synopsis: Lbc Dof Set
```

(BoundaryConditions.DofSet)=

# BoundaryConditions.DofSet

## Description

Lbc Dof Set

## Syntax

```python
BoundaryConditions.DofSet(strName="", iDwDof=0, crCurCoord=None, crTable=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-DofSet`

Ribbon: {menuselection}`BoundaryConditions --> DofSet`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iDwDof`**
: An _Integer_ specifying the dw dof. The default value is 0.

**`crCurCoord`**
: A _Cursor_ specifying the cur coordinate. The default value is None.

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.DofSet(strName="", iDwDof=0, crCurCoord=None, crTable=None, crlTarget=[], crEdit=None)
```
