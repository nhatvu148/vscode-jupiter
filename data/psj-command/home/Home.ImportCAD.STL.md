```{module} Home.ImportCAD.STL()
:synopsis: Import STL
```

(Home.ImportCAD.STL)=

# Home.ImportCAD.STL

## Description

Import STL

## Syntax

```python
Home.ImportCAD.STL(strlFiles, dChordHeightTolerance=0.0, dAngleToleranceDegree=0.0, iConvertIsolatedCurve=0, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=7.0, dMaxFacetWidth=0.0, dMinFacetWidth=0.0, bICAD=False, iVRMLColorGroups=-227253959, dScale=0.001)
```

Macro: {ref}`Macro-Home-ImportDirect_STL`

Ribbon: {menuselection}`Home --> ImportCAD --> STL`

## Inputs

**`strlFiles`**
: A _String List_ specifying the files. This is a required input.

**`dChordHeightTolerance`**
: A _Double_ specifying the chord height tolerance. The default value is 0.0.

**`dAngleToleranceDegree`**
: A _Double_ specifying the angle tolerance degree. The default value is 0.0.

**`iConvertIsolatedCurve`**
: An _Integer_ specifying the convert isolated curve. The default value is 0.

**`dSurfacePlaneTolerance`**
: A _Double_ specifying the surface plane tolerance. The default value is 0.0.

**`dSufacePlaneAngle`**
: A _Double_ specifying the suface plane angle. The default value is 7.0.

**`dMaxFacetWidth`**
: A _Double_ specifying the maximum facet width. The default value is 0.0.

**`dMinFacetWidth`**
: A _Double_ specifying the minimum facet width. The default value is 0.0.

**`bICAD`**
: A _Boolean_ specifying the i CAD. The default value is False.

**`iVRMLColorGroups`**
: An _Integer_ specifying the VRML color groups. The default value is -227253959.

**`dScale`**
: A _Double_ specifying the scale. The default value is 0.001.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ImportCAD.STL(strlFiles, dChordHeightTolerance=0.0, dAngleToleranceDegree=0.0, iConvertIsolatedCurve=0, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=7.0, dMaxFacetWidth=0.0, dMinFacetWidth=0.0, bICAD=False, iVRMLColorGroups=-227253959, dScale=0.001)
```
