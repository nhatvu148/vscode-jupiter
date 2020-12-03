```{module} Geometry.DeleteEntity.Part()
:synopsis: Delete Part
```

(Geometry.DeleteEntity.Part)=

# Geometry.DeleteEntity.Part

## Description

Delete Part

## Syntax

```python
Geometry.DeleteEntity.Part(crlPart)
```

Macro: {ref}`Macro-Geometry-DeletePartCr`

Ribbon: {menuselection}`Geometry --> DeleteEntity --> Part`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.DeleteEntity.Part(crlPart)
```
