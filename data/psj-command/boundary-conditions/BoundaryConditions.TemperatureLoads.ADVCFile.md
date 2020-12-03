```{module} BoundaryConditions.TemperatureLoads.ADVCFile()
:synopsis: create temperature load by advc file
```

(BoundaryConditions.TemperatureLoads.ADVCFile)=

# BoundaryConditions.TemperatureLoads.ADVCFile

## Description

create temperature load by advc file

## Syntax

```python
BoundaryConditions.TemperatureLoads.ADVCFile(strName="TemperatureLoadsADVC1", strFilePathName="", crTable=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-TemperatureLoadADVCFile`

Ribbon: {menuselection}`BoundaryConditions --> TemperatureLoads --> ADVCFile`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "TemperatureLoadsADVC1".

**`strFilePathName`**
: A _String_ specifying the file path name. The default value is "".

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
BoundaryConditions.TemperatureLoads.ADVCFile(strName="TemperatureLoadsADVC1", strFilePathName="", crTable=None, crlTarget=[], crEdit=None)
```
