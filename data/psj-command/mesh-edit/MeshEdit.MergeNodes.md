```{module} MeshEdit.MergeNodes()
:synopsis: Merge nodes
```

(MeshEdit.MergeNodes)=

# MeshEdit.MergeNodes

## Description

Merge nodes

## Syntax

```python
MeshEdit.MergeNodes(dTolerance=0.01, iKeepType=0, crlTarget=[], bGroup=False, bEquivalence=True)
```

Macro: {ref}`Macro-MeshEdit-MergeNode`

Ribbon: {menuselection}`MeshEdit --> MergeNodes`

## Inputs

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 0.01.

**`iKeepType`**
: An _Integer_ specifying the keep type. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`bGroup`**
: A _Boolean_ specifying the group. The default value is False.

**`bEquivalence`**
: A _Boolean_ specifying the equivalence. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MergeNodes(dTolerance=0.01, iKeepType=0, crlTarget=[], bGroup=False, bEquivalence=True)
```
