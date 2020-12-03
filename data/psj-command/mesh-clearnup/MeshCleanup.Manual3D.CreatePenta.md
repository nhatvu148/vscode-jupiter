```{module} MeshCleanup.Manual3D.CreatePenta()
:synopsis: Create penta5 element
```

(MeshCleanup.Manual3D.CreatePenta)=

# MeshCleanup.Manual3D.CreatePenta

## Description

Create penta5 element

## Syntax

```python
MeshCleanup.Manual3D.CreatePenta(iParentEntityId=0, crlElem=[])
```

Macro: {ref}`Macro-MeshCleanup-CreateElementPENTA5`

Ribbon: {menuselection}`MeshCleanup --> Manual3D --> CreatePenta`

## Inputs

**`iParentEntityId`**
: An _Integer_ specifying the parent entity ID. The default value is 0.

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual3D.CreatePenta(iParentEntityId=0, crlElem=[])
```
