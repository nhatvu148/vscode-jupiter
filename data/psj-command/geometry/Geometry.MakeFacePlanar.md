```{module} Geometry.MakeFacePlanar()
:synopsis: Make planar faces by given plane points
```

(Geometry.MakeFacePlanar)=

# Geometry.MakeFacePlanar

## Description

Make planar faces by given plane points

## Syntax

```python
Geometry.MakeFacePlanar(dlPlanePt1=[0.0,0.0,0.0], dlPlanePt2=[0.0,0.0,0.0], dlPlanePt3=[0.0,0.0,0.0], ilFaceIds=[], iMergeFace=0)
```

Macro: {ref}`Macro-Geometry-MakeFacePlanar`

Ribbon: {menuselection}`Geometry --> MakeFacePlanar`

## Inputs

**`dlPlanePt1`**
: A _Double List_ specifying the plane point 1. The default value is [0.0,0.0,0.0].

**`dlPlanePt2`**
: A _Double List_ specifying the plane point 2. The default value is [0.0,0.0,0.0].

**`dlPlanePt3`**
: A _Double List_ specifying the plane pt3. The default value is [0.0,0.0,0.0].

**`ilFaceIds`**
: A _Integer List_ specifying the face ids. The default value is [].

**`iMergeFace`**
: An _Integer_ specifying the merge face. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.MakeFacePlanar(dlPlanePt1=[0.0,0.0,0.0], dlPlanePt2=[0.0,0.0,0.0], dlPlanePt3=[0.0,0.0,0.0], ilFaceIds=[], iMergeFace=0)
```
