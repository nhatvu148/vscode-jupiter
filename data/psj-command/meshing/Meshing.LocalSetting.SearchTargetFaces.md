```{module} Meshing.LocalSetting.SearchTargetFaces()
:synopsis: Search Target Faces for Local mesh setting
```

(Meshing.LocalSetting.SearchTargetFaces)=

# Meshing.LocalSetting.SearchTargetFaces

## Description

Search Target Faces for Local mesh setting

## Syntax

```python
Meshing.LocalSetting.SearchTargetFaces(iPartType=0, dlOrigin=[0, 0, 0], dlLength=[0.1, 0.1, 0.1], dlCenterPt=[0.0,0.0,0.0], dlAxisPt1=[0.0,0.0,0.1], dlAxisPt2=[0.0,0.0,0.0], bEnclosed=False)
```

Macro: {ref}`Macro-Meshing-SearchTargetFacesInModel`

Ribbon: {menuselection}`Meshing --> LocalSetting --> SearchTargetFaces`

## Inputs

**`iPartType`**
: An _Integer_ specifying the part type. The default value is 0.

**`dlOrigin`**
: A _Double List_ specifying the original. The default value is [0, 0, 0].

**`dlLength`**
: A _Double List_ specifying the length. The default value is [0.1, 0.1, 0.1].

**`dlCenterPt`**
: A _Double List_ specifying the center point. The default value is [0.0,0.0,0.0].

**`dlAxisPt1`**
: A _Double List_ specifying the axis point 1. The default value is [0.0,0.0,0.1].

**`dlAxisPt2`**
: A _Double List_ specifying the axis point 2. The default value is [0.0,0.0,0.0].

**`bEnclosed`**
: A _Boolean_ specifying the enclosed. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.LocalSetting.SearchTargetFaces(iPartType=0, dlOrigin=[0, 0, 0], dlLength=[0.1, 0.1, 0.1], dlCenterPt=[0.0,0.0,0.0], dlAxisPt1=[0.0,0.0,0.1], dlAxisPt2=[0.0,0.0,0.0], bEnclosed=False)
```
