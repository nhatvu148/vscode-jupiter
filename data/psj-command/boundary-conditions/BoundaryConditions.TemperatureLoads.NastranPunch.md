```{module} BoundaryConditions.TemperatureLoads.NastranPunch()
:synopsis: create temperature load of nastran punch
```

(BoundaryConditions.TemperatureLoads.NastranPunch)=

# BoundaryConditions.TemperatureLoads.NastranPunch

## Description

create temperature load of nastran punch

## Syntax

```python
BoundaryConditions.TemperatureLoads.NastranPunch(strName="TemperatureLoadsPunch1", strFilePathName="", crTable=None, crlTarget=[], crEdit=None, bUseAsMaterialReferenceTemp=False)
```

Macro: {ref}`Macro-BoundaryConditions-TemperatureLoadNastran`

Ribbon: {menuselection}`BoundaryConditions --> TemperatureLoads --> NastranPunch`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "TemperatureLoadsPunch1".

**`strFilePathName`**
: A _String_ specifying the file path name. The default value is "".

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`bUseAsMaterialReferenceTemp`**
: A _Boolean_ specifying the use as material reference temperature. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.TemperatureLoads.NastranPunch(strName="TemperatureLoadsPunch1", strFilePathName="", crTable=None, crlTarget=[], crEdit=None, bUseAsMaterialReferenceTemp=False)
```
