```{module} HexModeling.FaceToFace()
:synopsis:
```

(HexModeling.FaceToFace)=

# HexModeling.FaceToFace

## Description

## Syntax

```python
HexModeling.FaceToFace(crSrcFace, crDstFace, bDeleteOriginalParts=True)
```

Macro: {ref}`Macro-HexModeling-HexSweepFaceToFace`

Ribbon: {menuselection}`HexModeling --> FaceToFace`

## Inputs

**`crSrcFace`**
: A _Cursor_ specifying the source face. This is a required input.

**`crDstFace`**
: A _Cursor_ specifying the dst face. This is a required input.

**`bDeleteOriginalParts`**
: A _Boolean_ specifying the delete original parts. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
HexModeling.FaceToFace(crSrcFace, crDstFace, bDeleteOriginalParts=True)
```
