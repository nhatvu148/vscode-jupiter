```{module} MeshCleanup.Manual3D.CreateHex()
:synopsis: create hex8 elements
```

(MeshCleanup.Manual3D.CreateHex)=

# MeshCleanup.Manual3D.CreateHex

## Description

create hex8 elements

## Syntax

```python
MeshCleanup.Manual3D.CreateHex(iParentEntityId=0, crlElem=[], iSeprateN=1)
```

Macro: {ref}`Macro-MeshCleanup-CreateElementHEX8`

Ribbon: {menuselection}`MeshCleanup --> Manual3D --> CreateHex`

## Inputs

**`iParentEntityId`**
: An _Integer_ specifying the parent entity ID. The default value is 0.

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

**`iSeprateN`**
: An _Integer_ specifying the seprate n. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual3D.CreateHex(iParentEntityId=0, crlElem=[], iSeprateN=1)
```
