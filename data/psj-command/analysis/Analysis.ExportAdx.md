```{module} Analysis.ExportAdx()
:synopsis: export adx file
```

(Analysis.ExportAdx)=

# Analysis.ExportAdx

## Description

export adx file

## Syntax

```python
Analysis.ExportAdx(crJob=None, strPath="", iNumType=0, iUiWidth=10, iUiPrecision=1)
```

Macro: {ref}`Macro-Analysis-ExportAdx`

Ribbon: {menuselection}`Analysis --> ExportAdx`

## Inputs

**`crJob`**
: A _Cursor_ specifying the job. The default value is None.

**`strPath`**
: A _String_ specifying the path. The default value is "".

**`iNumType`**
: An _Integer_ specifying the number type. The default value is 0.

**`iUiWidth`**
: An _Integer_ specifying the UI width. The default value is 10.

**`iUiPrecision`**
: An _Integer_ specifying the UI precision. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.ExportAdx(crJob=None, strPath="", iNumType=0, iUiWidth=10, iUiPrecision=1)
```
