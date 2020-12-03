```{module} Geometry.CADTrim()
:synopsis: CAD Trim
```

(Geometry.CADTrim)=

# Geometry.CADTrim

## Description

CAD Trim

## Syntax

```python
Geometry.CADTrim(crlFace, crlPart, dTrimSize=1, dTrimAngle=15)
```

Macro: {ref}`Macro-Geometry-GeometryCADTrim`

Ribbon: {menuselection}`Geometry --> CADTrim`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`dTrimSize`**
: A _Double_ specifying the trim size. The default value is 1.

**`dTrimAngle`**
: A _Double_ specifying the trim angle. The default value is 15.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.CADTrim(crlFace, crlPart, dTrimSize=1, dTrimAngle=15)
```
