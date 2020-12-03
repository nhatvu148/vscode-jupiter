```{module} MeshEdit.RibThickness()
:synopsis: Mesh Edit Morphing Rib Thickness
```

(MeshEdit.RibThickness)=

# MeshEdit.RibThickness

## Description

Mesh Edit Morphing Rib Thickness

## Syntax

```python
MeshEdit.RibThickness(crlFaceMove=[], crlFaceFixed=[], dMove=3.00, dDistStrong=10.00, dDistWeak=20.00)
```

Macro: {ref}`Macro-MeshEdit-MeshEditMorphingRibThickness`

Ribbon: {menuselection}`MeshEdit --> RibThickness`

## Inputs

**`crlFaceMove`**
: A _Cursor List_ specifying the face move. The default value is [].

**`crlFaceFixed`**
: A _Cursor List_ specifying the face fixed. The default value is [].

**`dMove`**
: A _Double_ specifying the move. The default value is 3.00.

**`dDistStrong`**
: A _Double_ specifying the dist strong. The default value is 10.00.

**`dDistWeak`**
: A _Double_ specifying the dist weak. The default value is 20.00.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.RibThickness(crlFaceMove=[], crlFaceFixed=[], dMove=3.00, dDistStrong=10.00, dDistWeak=20.00)
```
