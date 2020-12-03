```{module} ExManifoldModeling.SZ.WeldLine2()
:synopsis:
```

(ExManifoldModeling.SZ.WeldLine2)=

# ExManifoldModeling.SZ.WeldLine2

## Description

## Syntax

```python
ExManifoldModeling.SZ.WeldLine2(crlFace, crlPart, dLayerWidth, iLayerNumber)
```

Macro: {ref}`Macro-ExManifoldModeling-SZWeldLine2`

Ribbon: {menuselection}`ExManifoldModeling --> SZ --> WeldLine2`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`dLayerWidth`**
: A _Double_ specifying the layer width. This is a required input.

**`iLayerNumber`**
: An _Integer_ specifying the layer number. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
ExManifoldModeling.SZ.WeldLine2(crlFace, crlPart, dLayerWidth, iLayerNumber)
```
