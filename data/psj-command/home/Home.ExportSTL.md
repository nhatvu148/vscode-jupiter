```{module} Home.ExportSTL()
:synopsis: export stl
```

(Home.ExportSTL)=

# Home.ExportSTL

## Description

export stl

## Syntax

```python
Home.ExportSTL(strFile="", crlPart=[], dScale=1, bFilterIndex=False)
```

Macro: {ref}`Macro-Home-ExportSTL`

Ribbon: {menuselection}`Home --> ExportSTL`

## Inputs

**`strFile`**
: A _String_ specifying the file. The default value is "".

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`dScale`**
: A _Double_ specifying the scale. The default value is 1.

**`bFilterIndex`**
: A _Boolean_ specifying the filter index. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ExportSTL(strFile="", crlPart=[], dScale=1, bFilterIndex=False)
```
