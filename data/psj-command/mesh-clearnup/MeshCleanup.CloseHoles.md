```{module} MeshCleanup.CloseHoles()
:synopsis: close holes
```

(MeshCleanup.CloseHoles)=

# MeshCleanup.CloseHoles

## Description

close holes

## Syntax

```python
MeshCleanup.CloseHoles(crlEdge=[], dAreaMin=0.0, dAreaMax=543210.0, bMergeFace=False, bMergeEdge=False)
```

Macro: {ref}`Macro-MeshCleanup-FindHoles`

Ribbon: {menuselection}`MeshCleanup --> CloseHoles`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. The default value is [].

**`dAreaMin`**
: A _Double_ specifying the area minimum. The default value is 0.0.

**`dAreaMax`**
: A _Double_ specifying the area maximum. The default value is 543210.0.

**`bMergeFace`**
: A _Boolean_ specifying the merge face. The default value is False.

**`bMergeEdge`**
: A _Boolean_ specifying the merge edge. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.CloseHoles(crlEdge=[], dAreaMin=0.0, dAreaMax=543210.0, bMergeFace=False, bMergeEdge=False)
```
