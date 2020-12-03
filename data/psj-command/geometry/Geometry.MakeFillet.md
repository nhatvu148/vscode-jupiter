```{module} Geometry.MakeFillet()
:synopsis:
```

(Geometry.MakeFillet)=

# Geometry.MakeFillet

## Description

## Syntax

```python
Geometry.MakeFillet(crlEdge=[], dRadius=1.0)
```

Macro: {ref}`Macro-Geometry-MakeFillet`

Ribbon: {menuselection}`Geometry --> MakeFillet`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. The default value is [].

**`dRadius`**
: A _Double_ specifying the radius. The default value is 1.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.MakeFillet(crlEdge=[], dRadius=1.0)
```
