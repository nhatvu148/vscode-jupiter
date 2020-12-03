```{module} BoundaryConditions.InitialElementalValue.InitialStress()
:synopsis: create mapping stress
```

(BoundaryConditions.InitialElementalValue.InitialStress)=

# BoundaryConditions.InitialElementalValue.InitialStress

## Description

create mapping stress

## Syntax

```python
BoundaryConditions.InitialElementalValue.InitialStress(strName="InitialStress1", iDimension=2, iElemCs=0, dSXX=DFLT_DBL, dSYY=DFLT_DBL, dSXY=DFLT_DBL, crTable=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-InitialStressGeneral`

Ribbon: {menuselection}`BoundaryConditions --> InitialElementalValue --> InitialStress`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "InitialStress1".

**`iDimension`**
: An _Integer_ specifying the dimension. The default value is 2.

**`iElemCs`**
: An _Integer_ specifying the element cs. The default value is 0.

**`dSXX`**
: A _Double_ specifying the s x x. The default value is DFLT_DBL.

**`dSYY`**
: A _Double_ specifying the s y y. The default value is DFLT_DBL.

**`dSXY`**
: A _Double_ specifying the s x y. The default value is DFLT_DBL.

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
BoundaryConditions.InitialElementalValue.InitialStress(strName="InitialStress1", iDimension=2, iElemCs=0, dSXX=DFLT_DBL, dSYY=DFLT_DBL, dSXY=DFLT_DBL, crTable=None, crlTarget=[], crEdit=None)
```
