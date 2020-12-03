```{module} MeshEdit.CreateElement.Hex()
:synopsis: create hex8 elements
```

(MeshEdit.CreateElement.Hex)=

# MeshEdit.CreateElement.Hex

## Description

create hex8 elements

## Syntax

```python
MeshEdit.CreateElement.Hex(iParentEntityId=0, crlElem=[], iSeprateN=1)
```

Macro: {ref}`Macro-MeshEdit-CreateElementHEX8_ME`

Ribbon: {menuselection}`MeshEdit --> CreateElement --> Hex`

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
MeshEdit.CreateElement.Hex(iParentEntityId=0, crlElem=[], iSeprateN=1)
```
