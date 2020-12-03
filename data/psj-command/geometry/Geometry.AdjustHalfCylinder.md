```{module} Geometry.AdjustHalfCylinder()
:synopsis: Adjust half cylinder
```

(Geometry.AdjustHalfCylinder)=

# Geometry.AdjustHalfCylinder

## Description

Adjust half cylinder

## Syntax

```python
Geometry.AdjustHalfCylinder(poslPoint=[], crlFace=[], crCoord=None, iAxisPlane=0, bDivideFace=True, crlPart=[], bMergeEdge=True)
```

Macro: {ref}`Macro-Geometry-MeshEditAdjustHalfCylinderCoordinateCr`

Ribbon: {menuselection}`Geometry --> AdjustHalfCylinder`

## Inputs

**`poslPoint`**
: A _Position List_ specifying the point. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`iAxisPlane`**
: An _Integer_ specifying the axis plane. The default value is 0.

**`bDivideFace`**
: A _Boolean_ specifying the divide face. The default value is True.

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`bMergeEdge`**
: A _Boolean_ specifying the merge edge. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.AdjustHalfCylinder(poslPoint=[], crlFace=[], crCoord=None, iAxisPlane=0, bDivideFace=True, crlPart=[], bMergeEdge=True)
```
