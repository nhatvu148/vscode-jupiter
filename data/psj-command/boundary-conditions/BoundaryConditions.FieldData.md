```{module} BoundaryConditions.FieldData()
:synopsis: create field data table
```

(BoundaryConditions.FieldData)=

# BoundaryConditions.FieldData

## Description

create field data table

## Syntax

```python
BoundaryConditions.FieldData(strName="", iType=0, ilSheet=[], crEdit=None, bAbaqusAmp=False, iAmpType=0)
```

Macro: {ref}`Macro-BoundaryConditions-FieldData`

Ribbon: {menuselection}`BoundaryConditions --> FieldData`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`ilSheet`**
: A _Integer List_ specifying the sheet. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`bAbaqusAmp`**
: A _Boolean_ specifying the abaqus amp. The default value is False.

**`iAmpType`**
: An _Integer_ specifying the amp type. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.FieldData(strName="", iType=0, ilSheet=[], crEdit=None, bAbaqusAmp=False, iAmpType=0)
```
