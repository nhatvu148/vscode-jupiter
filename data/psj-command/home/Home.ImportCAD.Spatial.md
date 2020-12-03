```{module} Home.ImportCAD.Spatial()
:synopsis: import CAD by Spatial
```

(Home.ImportCAD.Spatial)=

# Home.ImportCAD.Spatial

## Description

import CAD by Spatial

## Syntax

```python
Home.ImportCAD.Spatial(strlPath, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=20.0, dMaxFacetWidth=1000.0, bNXMultipart=True, bHealing=True, bIsNXDirect=False, bSetFaceColor=False, strCsvFilePath="")
```

Macro: {ref}`Macro-Home-ImportSpatial`

Ribbon: {menuselection}`Home --> ImportCAD --> Spatial`

## Inputs

**`strlPath`**
: A _String List_ specifying the path. This is a required input.

**`dSurfacePlaneTolerance`**
: A _Double_ specifying the surface plane tolerance. The default value is 0.0.

**`dSufacePlaneAngle`**
: A _Double_ specifying the suface plane angle. The default value is 20.0.

**`dMaxFacetWidth`**
: A _Double_ specifying the maximum facet width. The default value is 1000.0.

**`bNXMultipart`**
: A _Boolean_ specifying the NX multipart. The default value is True.

**`bHealing`**
: A _Boolean_ specifying the healing. The default value is True.

**`bIsNXDirect`**
: A _Boolean_ specifying the is NX direct. The default value is False.

**`bSetFaceColor`**
: A _Boolean_ specifying the set face color. The default value is False.

**`strCsvFilePath`**
: A _String_ specifying the csv file path. The default value is "".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ImportCAD.Spatial(strlPath, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=20.0, dMaxFacetWidth=1000.0, bNXMultipart=True, bHealing=True, bIsNXDirect=False, bSetFaceColor=False, strCsvFilePath="")
```
