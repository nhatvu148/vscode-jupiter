```{module} BoundaryConditions.TemperatureLoads.Constant()
:synopsis: create temperature load constant
```

(BoundaryConditions.TemperatureLoads.Constant)=

# BoundaryConditions.TemperatureLoads.Constant

## Description

create temperature load constant

## Syntax

```python
BoundaryConditions.TemperatureLoads.Constant(strName, dTemperature=0.0, crTable=None, crlTarget=[], crEdit=None, bUseDefaultTemp=False)
```

Macro: {ref}`Macro-BoundaryConditions-TemperatureLoadGeneral`

Ribbon: {menuselection}`BoundaryConditions --> TemperatureLoads --> Constant`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`dTemperature`**
: A _Double_ specifying the temperature. The default value is 0.0.

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`bUseDefaultTemp`**
: A _Boolean_ specifying the use default temperature. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.TemperatureLoads.Constant(strName, dTemperature=0.0, crTable=None, crlTarget=[], crEdit=None, bUseDefaultTemp=False)
```
