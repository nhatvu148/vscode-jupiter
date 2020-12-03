```{module} MeshCleanup.Manual3D.CreateTetra()
:synopsis: create element Tet
```

(MeshCleanup.Manual3D.CreateTetra)=

# MeshCleanup.Manual3D.CreateTetra

## Description

create element Tet

## Syntax

```python
MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNode=[], crlElem=[])
```

Macro: {ref}`Macro-MeshCleanup-CreateElementTET4`

Ribbon: {menuselection}`MeshCleanup --> Manual3D --> CreateTetra`

## Inputs

**`iParentEntityId`**
: An _Integer_ specifying the parent entity ID. The default value is 0.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNode=[], crlElem=[])
```
