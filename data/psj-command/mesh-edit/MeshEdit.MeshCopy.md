```{module} MeshEdit.MeshCopy()
:synopsis: Mesh Copy Pattern
```

(MeshEdit.MeshCopy)=

# MeshEdit.MeshCopy

## Description

Mesh Copy Pattern

## Syntax

```python
MeshEdit.MeshCopy(crlFace=[], crlNode=[])
```

Macro: {ref}`Macro-MeshEdit-MeshCopy`

Ribbon: {menuselection}`MeshEdit --> MeshCopy`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.MeshCopy(crlFace=[], crlNode=[])
```
