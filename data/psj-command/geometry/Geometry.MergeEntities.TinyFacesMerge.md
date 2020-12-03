```{module} Geometry.MergeEntities.TinyFacesMerge()
:synopsis: merge tiny faces
```

(Geometry.MergeEntities.TinyFacesMerge)=

# Geometry.MergeEntities.TinyFacesMerge

## Description

merge tiny faces

## Syntax

```python
Geometry.MergeEntities.TinyFacesMerge(crlPart=[], crlFace=[], dMinFaceWidth=0.0, dMaxFaceWidth=0.001, dFaceAngle=30, bReferLocalSetting=False, bConnectFace=False)
```

Macro: {ref}`Macro-Geometry-GeometryMergeEntitiesTinyFacesMerge`

Ribbon: {menuselection}`Geometry --> MergeEntities --> TinyFacesMerge`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`dMinFaceWidth`**
: A _Double_ specifying the minimum face width. The default value is 0.0.

**`dMaxFaceWidth`**
: A _Double_ specifying the maximum face width. The default value is 0.001.

**`dFaceAngle`**
: A _Double_ specifying the face angle. The default value is 30.

**`bReferLocalSetting`**
: A _Boolean_ specifying the refer local setting. The default value is False.

**`bConnectFace`**
: A _Boolean_ specifying the connect face. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.MergeEntities.TinyFacesMerge(crlPart=[], crlFace=[], dMinFaceWidth=0.0, dMaxFaceWidth=0.001, dFaceAngle=30, bReferLocalSetting=False, bConnectFace=False)
```
