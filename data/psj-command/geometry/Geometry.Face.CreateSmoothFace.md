```{module} Geometry.Face.CreateSmoothFace()
:synopsis: Geometry Face CreateSmoothFace
```

(Geometry.Face.CreateSmoothFace)=

# Geometry.Face.CreateSmoothFace

## Description

Geometry Face CreateSmoothFace

## Syntax

```python
Geometry.Face.CreateSmoothFace(bInterPoration, crlTarget, iElemGeneration, dGradation, iEnableFaceSmooth, crTargetPart)
```

Macro: {ref}`Macro-Geometry-CreateSmoothFace`

Ribbon: {menuselection}`Geometry --> Face --> CreateSmoothFace`

## Inputs

**`bInterPoration`**
: A _Boolean_ specifying the inter poration. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

**`iElemGeneration`**
: An _Integer_ specifying the element generation. This is a required input.

**`dGradation`**
: A _Double_ specifying the gradation. This is a required input.

**`iEnableFaceSmooth`**
: An _Integer_ specifying the enable face smooth. This is a required input.

**`crTargetPart`**
: A _Cursor_ specifying the target part. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Face.CreateSmoothFace(bInterPoration, crlTarget, iElemGeneration, dGradation, iEnableFaceSmooth, crTargetPart)
```
