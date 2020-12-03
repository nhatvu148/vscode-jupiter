```{module} Tools.Group.CreateGroup()
:synopsis: Unknown Description
```

(Tools.Group.CreateGroup)=

# Tools.Group.CreateGroup

## Description

Unknown Description

## Syntax

```python
Tools.Group.CreateGroup(strGroupName, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-Tools-CreateGroup`

Ribbon: {menuselection}`Tools --> Group --> CreateGroup`

## Inputs

**`strGroupName`**
: A _String_ specifying the group name. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Group.CreateGroup(strGroupName, crlTarget=[], crEdit=None)
```
