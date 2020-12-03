```{module} Analysis.ExportAnsys()
:synopsis: Find faces in part by typical description
```

(Analysis.ExportAnsys)=

# Analysis.ExportAnsys

## Description

Find faces in part by typical description

## Syntax

```python
Analysis.ExportAnsys(strName="", crAnsysJob=None)
```

Macro: {ref}`Macro-Analysis-ExportAnsys`

Ribbon: {menuselection}`Analysis --> ExportAnsys`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`crAnsysJob`**
: A _Cursor_ specifying the ansys job. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.ExportAnsys(strName="", crAnsysJob=None)
```
