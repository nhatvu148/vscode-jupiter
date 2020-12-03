```{module} Assemble.GeneralLayer()
:synopsis:
```

(Assemble.GeneralLayer)=

# Assemble.GeneralLayer

## Description

## Syntax

```python
Assemble.GeneralLayer(crlFace=[], dWidth=1.0, iLayer=1, bSeparatePart=False, bForceStitchToSide=False, bSmoothingEdge=False, bNoImprint=False, bWidthOnSurface=False, bMakeHexa=False)
```

Macro: {ref}`Macro-Assemble-AssembleGeneralLayer`

Ribbon: {menuselection}`Assemble --> GeneralLayer`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`dWidth`**
: A _Double_ specifying the width. The default value is 1.0.

**`iLayer`**
: An _Integer_ specifying the layer. The default value is 1.

**`bSeparatePart`**
: A _Boolean_ specifying the separate part. The default value is False.

**`bForceStitchToSide`**
: A _Boolean_ specifying the force stitch to side. The default value is False.

**`bSmoothingEdge`**
: A _Boolean_ specifying the smoothing edge. The default value is False.

**`bNoImprint`**
: A _Boolean_ specifying the no imprint. The default value is False.

**`bWidthOnSurface`**
: A _Boolean_ specifying the width on surface. The default value is False.

**`bMakeHexa`**
: A _Boolean_ specifying the make hexa. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assemble.GeneralLayer(crlFace=[], dWidth=1.0, iLayer=1, bSeparatePart=False, bForceStitchToSide=False, bSmoothingEdge=False, bNoImprint=False, bWidthOnSurface=False, bMakeHexa=False)
```
