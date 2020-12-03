```{module} MeshCleanup.Face()
:synopsis: change topology face
```

(MeshCleanup.Face)=

# MeshCleanup.Face

## Description

change topology face

## Syntax

```python
MeshCleanup.Face(crlFace=[], crlPart=[], bCreateNewPart=False)
```

Macro: {ref}`Macro-MeshCleanup-ChangeTopoFaceCr`

Ribbon: {menuselection}`MeshCleanup --> Face`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`bCreateNewPart`**
: A _Boolean_ specifying the create new part. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Face(crlFace=[], crlPart=[], bCreateNewPart=False)
```
