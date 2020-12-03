```{module} Geometry.BreakEntity.Face()
:synopsis: break entity for face
```

(Geometry.BreakEntity.Face)=

# Geometry.BreakEntity.Face

## Description

break entity for face

## Syntax

```python
Geometry.BreakEntity.Face(crlFace)
```

Macro: {ref}`Macro-Geometry-BreakFace`

Ribbon: {menuselection}`Geometry --> BreakEntity --> Face`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.BreakEntity.Face(crlFace)
```
