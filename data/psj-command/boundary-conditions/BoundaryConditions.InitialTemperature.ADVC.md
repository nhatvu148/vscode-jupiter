```{module} BoundaryConditions.InitialTemperature.ADVC()
:synopsis: Unknown Description
```

(BoundaryConditions.InitialTemperature.ADVC)=

# BoundaryConditions.InitialTemperature.ADVC

## Description

Unknown Description

## Syntax

```python
BoundaryConditions.InitialTemperature.ADVC(strName="InitialTemperature1",dTemperatureValue=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-InitialTemperature`

Ribbon: {menuselection}`BoundaryConditions --> InitialTemperature --> ADVC`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`strFilePathName`**
: A _String_ specifying the file path name. The default value is "".

**`bUseDefault`**
: A _Boolean_ specifying the use default. The default value is False.

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
BoundaryConditions.InitialTemperature.ADVC(strName="InitialTemperature1",dTemperatureValue=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTarget=[], crEdit=None)
```
