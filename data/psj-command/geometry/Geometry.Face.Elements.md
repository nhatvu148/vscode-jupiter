```{module} Geometry.Face.Elements()
:synopsis: Create Face By Elements
```

(Geometry.Face.Elements)=

# Geometry.Face.Elements

## Description

Create Face By Elements

## Syntax

```python
Geometry.Face.Elements(crlElem, bShareFace=False)
```

Macro: {ref}`Macro-Geometry-CreateFaceByElem`

Ribbon: {menuselection}`Geometry --> Face --> Elements`

## Inputs

**`crlElem`**
: A _Cursor List_ specifying the element. This is a required input.

**`bShareFace`**
: A _Boolean_ specifying the share face. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Face.Elements(crlElem, bShareFace=False)
```
