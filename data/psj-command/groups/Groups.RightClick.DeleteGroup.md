```{module} Groups.RightClick.DeleteGroup()
:synopsis: Delete Group
```

(Groups.RightClick.DeleteGroup)=

# Groups.RightClick.DeleteGroup

## Description

Delete Group

## Syntax

```python
Groups.RightClick.DeleteGroup(crlDelGroup, bRemoveAll=False)
```

Macro: {ref}`Macro-Groups-DeleteGroup`

Ribbon: {menuselection}`Groups --> RightClick --> DeleteGroup`

## Inputs

**`crlDelGroup`**
: A _Cursor List_ specifying the del group. This is a required input.

**`bRemoveAll`**
: A _Boolean_ specifying the remove all. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Groups.RightClick.DeleteGroup(crlDelGroup, bRemoveAll=False)
```
