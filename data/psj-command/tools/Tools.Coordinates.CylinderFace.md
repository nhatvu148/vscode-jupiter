```{module} Tools.Coordinates.CylinderFace()
:synopsis: create Coordinate by Cylinder Face
```

(Tools.Coordinates.CylinderFace)=

# Tools.Coordinates.CylinderFace

## Description

create Coordinate by Cylinder Face

## Syntax

```python
Tools.Coordinates.CylinderFace(strName="CRect1", iCoordType=0, crFace=None)
```

Macro: {ref}`Macro-Tools-CreateCoordinateCylinderFace`

Ribbon: {menuselection}`Tools --> Coordinates --> CylinderFace`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "CRect1".

**`iCoordType`**
: An _Integer_ specifying the coordinate type. The default value is 0.

**`crFace`**
: A _Cursor_ specifying the face. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Coordinates.CylinderFace(strName="CRect1", iCoordType=0, crFace=None)
```
