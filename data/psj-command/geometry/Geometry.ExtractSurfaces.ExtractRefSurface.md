```{module} Geometry.ExtractSurfaces.ExtractRefSurface()
:synopsis: Unknown Description
```

(Geometry.ExtractSurfaces.ExtractRefSurface)=

# Geometry.ExtractSurfaces.ExtractRefSurface

## Description

Unknown Description

## Syntax

```python
Geometry.ExtractSurfaces.ExtractRefSurface(listFace, dAngle=60.0, strName="ExtractFace_1", isMergePart=False)
```

Macro: {ref}`Macro-Geometry-MeshEditExtractRefSurfaces`

Ribbon: {menuselection}`Geometry --> ExtractSurfaces --> ExtractRefSurface`

## Inputs

**`listFace`**
: A _FACE List_ specifying the face. This is a required input.

**`dAngle`**
: A _Double_ specifying the angle. The default value is 60.0.

**`strName`**
: A _String_ specifying the name. The default value is "ExtractFace_1".

**`isMergePart`**
: A _IS_MERGE_PART_ specifying the merge part. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.ExtractSurfaces.ExtractRefSurface(listFace, dAngle=60.0, strName="ExtractFace_1", isMergePart=False)
```
