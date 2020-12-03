```{module} MeshCleanup.Manual2D.CreateElement()
:synopsis: Create element
```

(MeshCleanup.Manual2D.CreateElement)=

# MeshCleanup.Manual2D.CreateElement

## Description

Create element

## Syntax

```python
MeshCleanup.Manual2D.CreateElement(iElemType=0, crParentEntity=None, crlNode=[])
```

Macro: {ref}`Macro-MeshCleanup-CreateElementCr`

Ribbon: {menuselection}`MeshCleanup --> Manual2D --> CreateElement`

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
MeshCleanup.Manual2D.CreateElement(iElemType=0, crParentEntity=None, crlNode=[])
```
