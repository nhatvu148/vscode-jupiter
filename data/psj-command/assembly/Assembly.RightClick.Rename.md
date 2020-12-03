```{module} Assembly.RightClick.Rename()
:synopsis: Rename item
```

(Assembly.RightClick.Rename)=

# Assembly.RightClick.Rename

## Description

Rename item

## Syntax

```python
Assembly.RightClick.Rename(strNewName="New name", crItem=None)
```

Macro: {ref}`Macro-Assembly-RenameItem`

Ribbon: {menuselection}`Assembly --> RightClick --> Rename`

## Inputs

**`strNewName`**
: A _String_ specifying the new name. The default value is "New name".

**`crItem`**
: A _Cursor_ specifying the item. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assembly.RightClick.Rename(strNewName="New name", crItem=None)
```
