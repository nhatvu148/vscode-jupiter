```{module} BoundaryConditions.InitialTemperature.WholeMapping()
:synopsis: Create initial temperature whole mapping
```

(BoundaryConditions.InitialTemperature.WholeMapping)=

# BoundaryConditions.InitialTemperature.WholeMapping

## Description

Create initial temperature whole mapping

## Syntax

```python
BoundaryConditions.InitialTemperature.WholeMapping(strName="TemperatureInitsWholeMapping1", iMapSourceType=0, strPath="", iMappingMethod=0, iIsubcase=0, crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-WholeMappingInitTemperature`

Ribbon: {menuselection}`BoundaryConditions --> InitialTemperature --> WholeMapping`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "TemperatureInitsWholeMapping1".

**`iMapSourceType`**
: An _Integer_ specifying the map source type. The default value is 0.

**`strPath`**
: A _String_ specifying the path. The default value is "".

**`iMappingMethod`**
: An _Integer_ specifying the mapping method. The default value is 0.

**`iIsubcase`**
: An _Integer_ specifying the isubcase. The default value is 0.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.InitialTemperature.WholeMapping(strName="TemperatureInitsWholeMapping1", iMapSourceType=0, strPath="", iMappingMethod=0, iIsubcase=0, crEdit=None)
```
