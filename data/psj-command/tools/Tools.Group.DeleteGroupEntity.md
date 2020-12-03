```{module} Tools.Group.DeleteGroupEntity()
:synopsis: Delete Entity in Group
```

(Tools.Group.DeleteGroupEntity)=

# Tools.Group.DeleteGroupEntity

## Description

Delete Entity in Group

## Syntax

```python
Tools.Group.DeleteGroupEntity(crlDelGroup)
```

Macro: {ref}`Macro-Tools-DeleteGroupEntity`

Ribbon: {menuselection}`Tools --> Group --> DeleteGroupEntity`

## Inputs

**`crlDelGroup`**
: A _Cursor List_ specifying the del group. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Group.DeleteGroupEntity(crlDelGroup)
```
