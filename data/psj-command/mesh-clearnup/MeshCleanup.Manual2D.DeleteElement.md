```{module} MeshCleanup.Manual2D.DeleteElement()
:synopsis: Delete Element
```

(MeshCleanup.Manual2D.DeleteElement)=

# MeshCleanup.Manual2D.DeleteElement

## Description

Delete Element

## Syntax

```python
MeshCleanup.Manual2D.DeleteElement(crlElem, bKeepShareElem=False)
```

Macro: {ref}`Macro-MeshCleanup-DeleteElement`

Ribbon: {menuselection}`MeshCleanup --> Manual2D --> DeleteElement`

## Inputs

**`crlElem`**
: A _Cursor List_ specifying the element. This is a required input.

**`bKeepShareElem`**
: A _Boolean_ specifying the keep share element. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual2D.DeleteElement(crlElem, bKeepShareElem=False)
```
