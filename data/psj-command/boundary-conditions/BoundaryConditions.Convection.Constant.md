```{module} BoundaryConditions.Convection.Constant()
:synopsis: Create load boundary condition of convection
```

(BoundaryConditions.Convection.Constant)=

# BoundaryConditions.Convection.Constant

## Description

Create load boundary condition of convection

## Syntax

```python
BoundaryConditions.Convection.Constant(strName="Convection_1", dExtTemp=DFLT_DBL, crTableTimeTemp=None, dDcoef=DFLT_DBL, crTableTimeCoeff=None, crTableTempCoeff=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-Convection`

Ribbon: {menuselection}`BoundaryConditions --> Convection --> Constant`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "Convection_1".

**`dExtTemp`**
: A _Double_ specifying the extend temperature. The default value is DFLT_DBL.

**`crTableTimeTemp`**
: A _Cursor_ specifying the table time temperature. The default value is None.

**`dDcoef`**
: A _Double_ specifying the coefficient. The default value is DFLT_DBL.

**`crTableTimeCoeff`**
: A _Cursor_ specifying the table time coeff. The default value is None.

**`crTableTempCoeff`**
: A _Cursor_ specifying the table temperature coeff. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Convection.Constant(strName="Convection_1", dExtTemp=DFLT_DBL, crTableTimeTemp=None, dDcoef=DFLT_DBL, crTableTimeCoeff=None, crTableTempCoeff=None, crlTarget=[], crEdit=None)
```
