```{module} Geometry.BodyCut.XXYYOnOnePoint()
:synopsis: Cut body by one point
```

(Geometry.BodyCut.XXYYOnOnePoint)=

# Geometry.BodyCut.XXYYOnOnePoint

## Description

Cut body by one point

## Syntax

```python
Geometry.BodyCut.XXYYOnOnePoint(crPart, posCutPos=[0,0,0], iType=0, dOffset=0.0, bSplit=False, bSectionFace=True, bShateFace=False, crLocalCoor=None)
```

Macro: {ref}`Macro-Geometry-CutBodyByPlane`

Ribbon: {menuselection}`Geometry --> BodyCut --> XXYYOnOnePoint`

## Inputs

**`crPart`**
: A _Cursor_ specifying the part. This is a required input.

**`posCutPos`**
: A _Position_ specifying the cut position. The default value is [0,0,0].

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`dOffset`**
: A _Double_ specifying the offset. The default value is 0.0.

**`bSplit`**
: A _Boolean_ specifying the split. The default value is False.

**`bSectionFace`**
: A _Boolean_ specifying the section face. The default value is True.

**`bShateFace`**
: A _Boolean_ specifying the shate face. The default value is False.

**`crLocalCoor`**
: A _Cursor_ specifying the local coordinate. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.BodyCut.XXYYOnOnePoint(crPart, posCutPos=[0,0,0], iType=0, dOffset=0.0, bSplit=False, bSectionFace=True, bShateFace=False, crLocalCoor=None)
```
