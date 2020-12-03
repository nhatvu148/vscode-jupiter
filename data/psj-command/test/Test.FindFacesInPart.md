```{module} Test.FindFacesInPart()
:synopsis: Find faces in part by typical description
```

(Test.FindFacesInPart)=

# Test.FindFacesInPart

## Description

Find faces in part by typical description

## Syntax

```python
Test.FindFacesInPart(crPart, strIdentical)
```

Macro: {ref}`Macro-Test-FindFacesInPart`

Ribbon: {menuselection}`Test --> FindFacesInPart`

## Inputs

**`crPart`**
: A _Cursor_ specifying the part. This is a required input.

**`strIdentical`**
: A _String_ specifying the identical. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Test.FindFacesInPart(crPart, strIdentical)
```
