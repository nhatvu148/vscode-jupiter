```{module} Geometry.LogoRemoval()
:synopsis: Create Face From Edges
```

(Geometry.LogoRemoval)=

# Geometry.LogoRemoval

## Description

Create Face From Edges

## Syntax

```python
Geometry.LogoRemoval(crlStartFaces=[], crlStopFaces=[], iLayers=5, bMergeFaces=False)
```

Macro: {ref}`Macro-Geometry-LogoRemoval`

Ribbon: {menuselection}`Geometry --> LogoRemoval`

## Inputs

**`crlStartFaces`**
: A _Cursor List_ specifying the start faces. The default value is [].

**`crlStopFaces`**
: A _Cursor List_ specifying the stop faces. The default value is [].

**`iLayers`**
: An _Integer_ specifying the layers. The default value is 5.

**`bMergeFaces`**
: A _Boolean_ specifying the merge faces. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.LogoRemoval(crlStartFaces=[], crlStopFaces=[], iLayers=5, bMergeFaces=False)
```
