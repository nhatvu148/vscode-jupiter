```{module} BoundaryConditions.BoundaryTemperature.Constant()
:synopsis: Create boundary temperature
```

(BoundaryConditions.BoundaryTemperature.Constant)=

# BoundaryConditions.BoundaryTemperature.Constant

## Description

Create boundary temperature

## Syntax

```python
BoundaryConditions.BoundaryTemperature.Constant(strName="BoundaryTemperature_1", dFTemp=0.0, crTable=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-BoundaryTemperature`

Ribbon: {menuselection}`BoundaryConditions --> BoundaryTemperature --> Constant`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "BoundaryTemperature_1".

**`dFTemp`**
: A _Double_ specifying the temperature. The default value is 0.0.

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
BoundaryConditions.BoundaryTemperature.Constant(strName="BoundaryTemperature_1", dFTemp=0.0, crTable=None, crlTarget=[], crEdit=None)
```
