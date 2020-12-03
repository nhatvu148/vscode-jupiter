```{module} Geometry.FCircVertexAdjust()
:synopsis: FCirc Vertex Adjust
```

(Geometry.FCircVertexAdjust)=

# Geometry.FCircVertexAdjust

## Description

FCirc Vertex Adjust

## Syntax

```python
Geometry.FCircVertexAdjust(crlPart, dMinRadius=0.0, bFullCylinder=True, bCylinderMorethan90=False, bSkipFaceHaveLocalSetting=False)
```

Macro: {ref}`Macro-Geometry-MeshEditGeomEditDivideCylinderBy90Deg`

Ribbon: {menuselection}`Geometry --> FCircVertexAdjust`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`dMinRadius`**
: A _Double_ specifying the minimum radius. The default value is 0.0.

**`bFullCylinder`**
: A _Boolean_ specifying the full cylinder. The default value is True.

**`bCylinderMorethan90`**
: A _Boolean_ specifying the cylinder morethan90. The default value is False.

**`bSkipFaceHaveLocalSetting`**
: A _Boolean_ specifying the skip face have local setting. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.FCircVertexAdjust(crlPart, dMinRadius=0.0, bFullCylinder=True, bCylinderMorethan90=False, bSkipFaceHaveLocalSetting=False)
```
