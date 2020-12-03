```{module} Geometry.DeleteEntity.Face()
:synopsis: Delete Face
```

(Geometry.DeleteEntity.Face)=

# Geometry.DeleteEntity.Face

## Description

Delete Face

## Syntax

```python
Geometry.DeleteEntity.Face(crlFace=[], bKeepSolid=True)
```

Macro: {ref}`Macro-Geometry-DeleteFaceCr`

Ribbon: {menuselection}`Geometry --> DeleteEntity --> Face`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`bKeepSolid`**
: A _Boolean_ specifying the keep solid. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.DeleteEntity.Face(crlFace=[], bKeepSolid=True)
```
