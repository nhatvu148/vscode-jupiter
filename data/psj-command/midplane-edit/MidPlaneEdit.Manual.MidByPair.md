```{module} MidPlaneEdit.Manual.MidByPair()
:synopsis: Midplane Manual MidByPair
```

(MidPlaneEdit.Manual.MidByPair)=

# MidPlaneEdit.Manual.MidByPair

## Description

Midplane Manual MidByPair

## Syntax

```python
MidPlaneEdit.Manual.MidByPair(crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces)
```

Macro: {ref}`Macro-MidPlaneEdit-MidplaneManualMidByPair`

Ribbon: {menuselection}`MidPlaneEdit --> Manual --> MidByPair`

## Inputs

**`crlBaseFaces`**
: A _Cursor List_ specifying the base faces. This is a required input.

**`crlPairFaces`**
: A _Cursor List_ specifying the pair faces. This is a required input.

**`crlRefFaces`**
: A _Cursor List_ specifying the reference faces. This is a required input.

**`crPart`**
: A _Cursor_ specifying the part. This is a required input.

**`bMergeFaces`**
: A _Boolean_ specifying the merge faces. This is a required input.

**`bExtendFaces`**
: A _Boolean_ specifying the extend faces. This is a required input.

**`bHideFaces`**
: A _Boolean_ specifying the hide faces. This is a required input.

**`dExtendTol`**
: A _Double_ specifying the extend tolerance. This is a required input.

**`dMergeEdgesAngle`**
: A _Double_ specifying the merge edges angle. This is a required input.

**`dStitchFaces`**
: A _Double_ specifying the stitch faces. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.Manual.MidByPair(crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces)
```
