```{module} Geometry.FindFeature.Fillet()
:synopsis: Find feature in part by typical description
```

(Geometry.FindFeature.Fillet)=

# Geometry.FindFeature.Fillet

## Description

Find feature in part by typical description

## Syntax

```python
Geometry.FindFeature.Fillet(crlPart=[], crlFace=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0)
```

Macro: {ref}`Macro-Geometry-FindFeatureFillet`

Ribbon: {menuselection}`Geometry --> FindFeature --> Fillet`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`dMinAngle`**
: A _Double_ specifying the minimum angle. The default value is 1.0.

**`dMaxAngle`**
: A _Double_ specifying the maximum angle. The default value is 10.0.

**`dMinFaceWidth`**
: A _Double_ specifying the minimum face width. The default value is 1.0.

**`dMaxFaceWidth`**
: A _Double_ specifying the maximum face width. The default value is 10.0.

**`dMinCurveRadius`**
: A _Double_ specifying the minimum curve radius. The default value is 0.0.

**`dMaxCurveRadius`**
: A _Double_ specifying the maximum curve radius. The default value is 171.

**`dScale`**
: A _Double_ specifying the scale. The default value is 1.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.FindFeature.Fillet(crlPart=[], crlFace=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0)
```
