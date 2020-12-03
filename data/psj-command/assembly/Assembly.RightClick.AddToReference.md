```{module} Assembly.RightClick.AddToReference()
:synopsis: Add Reference to Body
```

(Assembly.RightClick.AddToReference)=

# Assembly.RightClick.AddToReference

## Description

Add Reference to Body

## Syntax

```python
Assembly.RightClick.AddToReference(crSrcPart, crDestPart)
```

Macro: {ref}`Macro-Assembly-AddReference`

Ribbon: {menuselection}`Assembly --> RightClick --> AddToReference`

## Inputs

**`crSrcPart`**
: A _Cursor_ specifying the source part. This is a required input.

**`crDestPart`**
: A _Cursor_ specifying the dest part. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assembly.RightClick.AddToReference(crSrcPart, crDestPart)
```
