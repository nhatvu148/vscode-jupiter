```{module} Geometry.ExtractSurfaces.ExtractSurfaces()
:synopsis: Unknown Description
```

(Geometry.ExtractSurfaces.ExtractSurfaces)=

# Geometry.ExtractSurfaces.ExtractSurfaces

## Description

Unknown Description

## Syntax

```python
Geometry.ExtractSurfaces.ExtractSurfaces(crlFace, dAngle=60.0, strName="ExtractFace_1", bMergePart=False)
```

Macro: {ref}`Macro-Geometry-MeshEditExtractSurfaces`

Ribbon: {menuselection}`Geometry --> ExtractSurfaces --> ExtractSurfaces`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`dAngle`**
: A _Double_ specifying the angle. The default value is 60.0.

**`strName`**
: A _String_ specifying the name. The default value is "ExtractFace_1".

**`bMergePart`**
: A _Boolean_ specifying the merge part. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.ExtractSurfaces.ExtractSurfaces(crlFace, dAngle=60.0, strName="ExtractFace_1", bMergePart=False)
```
