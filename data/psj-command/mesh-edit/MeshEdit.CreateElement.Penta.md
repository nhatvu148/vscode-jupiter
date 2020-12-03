```{module} MeshEdit.CreateElement.Penta()
:synopsis: Create penta element
```

(MeshEdit.CreateElement.Penta)=

# MeshEdit.CreateElement.Penta

## Description

Create penta element

## Syntax

```python
MeshEdit.CreateElement.Penta(iParentEntityId=0, crlElem=[])
```

Macro: {ref}`Macro-MeshEdit-MeshEditCreatePenta`

Ribbon: {menuselection}`MeshEdit --> CreateElement --> Penta`

## Inputs

**`iParentEntityId`**
: An _Integer_ specifying the parent entity ID. The default value is 0.

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateElement.Penta(iParentEntityId=0, crlElem=[])
```
