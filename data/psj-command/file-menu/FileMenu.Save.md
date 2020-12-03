```{module} FileMenu.Save()
:synopsis: Save file JTDB
```

(FileMenu.Save)=

# FileMenu.Save

## Description

Save file JTDB

## Syntax

```python
FileMenu.Save(strFileName="")
```

Macro: {ref}`Macro-FileMenu-SaveJTDB`

Ribbon: {menuselection}`FileMenu --> Save`

## Inputs

**`strFileName`**
: A _String_ specifying the file name. The default value is "".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
FileMenu.Save(strFileName="")
```
