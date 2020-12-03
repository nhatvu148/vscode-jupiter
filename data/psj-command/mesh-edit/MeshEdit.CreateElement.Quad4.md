```{module} MeshEdit.CreateElement.Quad4()
:synopsis: Create element
```

(MeshEdit.CreateElement.Quad4)=

# MeshEdit.CreateElement.Quad4

## Description

Create element

## Syntax

```python
MeshEdit.CreateElement.Quad4(iElemType=0, crParentEntity=None, crlNode=[])
```

Macro: {ref}`Macro-MeshEdit-CreateElementQUAD4Cr`

Ribbon: {menuselection}`MeshEdit --> CreateElement --> Quad4`

## Inputs

**`iElemType`**
: An _Integer_ specifying the element type. The default value is 0.

**`crParentEntity`**
: A _Cursor_ specifying the parent entity. The default value is None.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateElement.Quad4(iElemType=0, crParentEntity=None, crlNode=[])
```
