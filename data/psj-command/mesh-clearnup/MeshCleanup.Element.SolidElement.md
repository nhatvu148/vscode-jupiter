```{module} MeshCleanup.Element.SolidElement()
:synopsis: Change Topology for Solid Element
```

(MeshCleanup.Element.SolidElement)=

# MeshCleanup.Element.SolidElement

## Description

Change Topology for Solid Element

## Syntax

```python
MeshCleanup.Element.SolidElement(crlElem, crPart=None)
```

Macro: {ref}`Macro-MeshCleanup-ChangeTopoSolidElem`

Ribbon: {menuselection}`MeshCleanup --> Element --> SolidElement`

## Inputs

**`crlElem`**
: A _Cursor List_ specifying the element. This is a required input.

**`crPart`**
: A _Cursor_ specifying the part. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Element.SolidElement(crlElem, crPart=None)
```
