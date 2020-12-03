```{module} Geometry.BreakEntity.Part()
:synopsis: Separate Part
```

(Geometry.BreakEntity.Part)=

# Geometry.BreakEntity.Part

## Description

Separate Part

## Syntax

```python
Geometry.BreakEntity.Part(crlPart=[])
```

Macro: {ref}`Macro-Geometry-SeparatePart`

Ribbon: {menuselection}`Geometry --> BreakEntity --> Part`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.BreakEntity.Part(crlPart=[])
```
