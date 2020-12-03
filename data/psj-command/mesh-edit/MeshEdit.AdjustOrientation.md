```{module} MeshEdit.AdjustOrientation()
:synopsis: Adjust Orientation
```

(MeshEdit.AdjustOrientation)=

# MeshEdit.AdjustOrientation

## Description

Adjust Orientation

## Syntax

```python
MeshEdit.AdjustOrientation(crlPart=[], crlFace=[], crlElem=[])
```

Macro: {ref}`Macro-MeshEdit-GeomEditAdjustOrientation`

Ribbon: {menuselection}`MeshEdit --> AdjustOrientation`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.AdjustOrientation(crlPart=[], crlFace=[], crlElem=[])
```
