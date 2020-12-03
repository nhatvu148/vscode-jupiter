```{module} MeshEdit.CreateElement.Tri3()
:synopsis: Create element
```

(MeshEdit.CreateElement.Tri3)=

# MeshEdit.CreateElement.Tri3

## Description

Create element

## Syntax

```python
MeshEdit.CreateElement.Tri3(iElemType=0, crParentEntity=None, crlNode=[])
```

Macro: {ref}`Macro-MeshEdit-CreateElementTRI3Cr`

Ribbon: {menuselection}`MeshEdit --> CreateElement --> Tri3`

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
MeshEdit.CreateElement.Tri3(iElemType=0, crParentEntity=None, crlNode=[])
```
