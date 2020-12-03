```{module} Geometry.FindFeature.DelCircChamfer()
:synopsis: Delete Circ Chamfer
```

(Geometry.FindFeature.DelCircChamfer)=

# Geometry.FindFeature.DelCircChamfer

## Description

Delete Circ Chamfer

## Syntax

```python
Geometry.FindFeature.DelCircChamfer(crlPart, dMaxThick=0.1, dMinThick=2)
```

Macro: {ref}`Macro-Geometry-DelCircChamfer`

Ribbon: {menuselection}`Geometry --> FindFeature --> DelCircChamfer`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`dMaxThick`**
: A _Double_ specifying the maximum thickness. The default value is 0.1.

**`dMinThick`**
: A _Double_ specifying the minimum thickness. The default value is 2.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.FindFeature.DelCircChamfer(crlPart, dMaxThick=0.1, dMinThick=2)
```
