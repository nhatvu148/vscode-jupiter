```{module} Utility.FindEntities()
:synopsis: Search entity by ID, Name ...etc
```

(Utility.FindEntities)=

# Utility.FindEntities

## Description

Search entity by ID, Name ...etc

## Syntax

```python
Utility.FindEntities(strTarget, strFindType, bFindMatch=False)
```

Macro: {ref}`Macro-Utility-FindEntities`

Ribbon: {menuselection}`Utility --> FindEntities`

## Inputs

**`strTarget`**
: A _String_ specifying the target. This is a required input.

**`strFindType`**
: A _String_ specifying the find type. This is a required input.

**`bFindMatch`**
: A _Boolean_ specifying the find match. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Utility.FindEntities(strTarget, strFindType, bFindMatch=False)
```
