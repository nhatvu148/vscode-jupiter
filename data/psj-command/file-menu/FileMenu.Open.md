```{module} FileMenu.Open()
:synopsis: Load JTDB file
```

(FileMenu.Open)=

# FileMenu.Open

## Description

Load JTDB file

## Syntax

```python
FileMenu.Open(strFileName="", bUseTmpTable=False)
```

Macro: {ref}`Macro-FileMenu-LoadJTDB`

Ribbon: {menuselection}`FileMenu --> Open`

## Inputs

**`strFileName`**
: A _String_ specifying the file name. The default value is "".

**`bUseTmpTable`**
: A _Boolean_ specifying the use temporary table. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
FileMenu.Open(strFileName="", bUseTmpTable=False)
```
