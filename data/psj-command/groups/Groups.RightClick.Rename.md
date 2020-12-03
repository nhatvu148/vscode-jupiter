```{module} Groups.RightClick.Rename()
:synopsis: Unknown Description
```

(Groups.RightClick.Rename)=

# Groups.RightClick.Rename

## Description

Unknown Description

## Syntax

```python
Groups.RightClick.Rename(strNewName, crItem)
```

Macro: {ref}`Macro-Groups-RenameItem`

Ribbon: {menuselection}`Groups --> RightClick --> Rename`

## Inputs

**`strNewName`**
: A _String_ specifying the new name. This is a required input.

**`crItem`**
: A _Cursor_ specifying the item. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Groups.RightClick.Rename(strNewName, crItem)
```
