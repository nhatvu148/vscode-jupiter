```{module} Geometry.MergeEntities.PartFaces()
:synopsis: Merge by Part Faces
```

(Geometry.MergeEntities.PartFaces)=

# Geometry.MergeEntities.PartFaces

## Description

Merge by Part Faces

## Syntax

```python
Geometry.MergeEntities.PartFaces(crlPart=[], crlFace=[], bAngle=True, dTolAngle=20, bWidth=True, dTolWidth=0.2)
```

Macro: {ref}`Macro-Geometry-MergeBodyFaceCr`

Ribbon: {menuselection}`Geometry --> MergeEntities --> PartFaces`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`bAngle`**
: A _Boolean_ specifying the angle. The default value is True.

**`dTolAngle`**
: A _Double_ specifying the tolerance angle. The default value is 20.

**`bWidth`**
: A _Boolean_ specifying the width. The default value is True.

**`dTolWidth`**
: A _Double_ specifying the tolerance width. The default value is 0.2.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.MergeEntities.PartFaces(crlPart=[], crlFace=[], bAngle=True, dTolAngle=20, bWidth=True, dTolWidth=0.2)
```
