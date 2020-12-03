```{module} MeshEdit.Deform()
:synopsis: geometry deformation
```

(MeshEdit.Deform)=

# MeshEdit.Deform

## Description

geometry deformation

## Syntax

```python
MeshEdit.Deform(crlFaceSrcObverse=[], crlFaceDstReverse=[], crlFaceSrcReverse=[], crlFaceDstObverse=[], crlFaceFixed=[], dDistEffect=0.02)
```

Macro: {ref}`Macro-MeshEdit-GeometryDeform`

Ribbon: {menuselection}`MeshEdit --> Deform`

## Inputs

**`crlFaceSrcObverse`**
: A _Cursor List_ specifying the face source obverse. The default value is [].

**`crlFaceDstReverse`**
: A _Cursor List_ specifying the face dst reverse. The default value is [].

**`crlFaceSrcReverse`**
: A _Cursor List_ specifying the face source reverse. The default value is [].

**`crlFaceDstObverse`**
: A _Cursor List_ specifying the face dst obverse. The default value is [].

**`crlFaceFixed`**
: A _Cursor List_ specifying the face fixed. The default value is [].

**`dDistEffect`**
: A _Double_ specifying the dist effect. The default value is 0.02.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.Deform(crlFaceSrcObverse=[], crlFaceDstReverse=[], crlFaceSrcReverse=[], crlFaceDstObverse=[], crlFaceFixed=[], dDistEffect=0.02)
```
