```{module} Geometry.BreakEntity.StlPart()
:synopsis: break STL part
```

(Geometry.BreakEntity.StlPart)=

# Geometry.BreakEntity.StlPart

## Description

break STL part

## Syntax

```python
Geometry.BreakEntity.StlPart(crlPart=[], iMinNoOfFaces=0, iMethod=0)
```

Macro: {ref}`Macro-Geometry-SeparateSTLPart`

Ribbon: {menuselection}`Geometry --> BreakEntity --> StlPart`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`iMinNoOfFaces`**
: An _Integer_ specifying the minimum no of faces. The default value is 0.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.BreakEntity.StlPart(crlPart=[], iMinNoOfFaces=0, iMethod=0)
```
