```{module} MeshEdit.OneNode()
:synopsis: morphing one node
```

(MeshEdit.OneNode)=

# MeshEdit.OneNode

## Description

morphing one node

## Syntax

```python
MeshEdit.OneNode(crlNode=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDisttype=0, dDiststrong=10, dDistweak=20)
```

Macro: {ref}`Macro-MeshEdit-MeshEditMorphingOneNode`

Ribbon: {menuselection}`MeshEdit --> OneNode`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crlFaceFixed`**
: A _Cursor List_ specifying the face fixed. The default value is [].

**`bOffsetvector`**
: A _Boolean_ specifying the offsetvector. The default value is False.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`dlOffset`**
: A _Double List_ specifying the offset. The default value is [0, 1, 0].

**`dOffset`**
: A _Double_ specifying the offset. The default value is 1.0.

**`iDisttype`**
: An _Integer_ specifying the disttype. The default value is 0.

**`dDiststrong`**
: A _Double_ specifying the diststrong. The default value is 10.

**`dDistweak`**
: A _Double_ specifying the distweak. The default value is 20.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.OneNode(crlNode=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDisttype=0, dDiststrong=10, dDistweak=20)
```
