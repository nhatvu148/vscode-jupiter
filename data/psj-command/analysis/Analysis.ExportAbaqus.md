```{module} Analysis.ExportAbaqus()
:synopsis: export inp file
```

(Analysis.ExportAbaqus)=

# Analysis.ExportAbaqus

## Description

export inp file

## Syntax

```python
Analysis.ExportAbaqus(crAbaJob=None, crlSelectPart=[], strInpPath="")
```

Macro: {ref}`Macro-Analysis-ExportAbaqusInp`

Ribbon: {menuselection}`Analysis --> ExportAbaqus`

## Inputs

**`crAbaJob`**
: A _Cursor_ specifying the aba job. The default value is None.

**`crlSelectPart`**
: A _Cursor List_ specifying the select part. The default value is [].

**`strInpPath`**
: A _String_ specifying the inp path. The default value is "".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Analysis.ExportAbaqus(crAbaJob=None, crlSelectPart=[], strInpPath="")
```
