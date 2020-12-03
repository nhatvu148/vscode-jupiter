```{module} HexModeling.Circular()
:synopsis: create Hexa mesh by revolving a surface
```

(HexModeling.Circular)=

# HexModeling.Circular

## Description

create Hexa mesh by revolving a surface

## Syntax

```python
HexModeling.Circular(crlFace=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0)
```

Macro: {ref}`Macro-HexModeling-HexSweepCircular`

Ribbon: {menuselection}`HexModeling --> Circular`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`dAngle`**
: A _Double_ specifying the angle. The default value is 360.

**`dTol`**
: A _Double_ specifying the tolerance. The default value is 0.0000001.

**`iLayer`**
: An _Integer_ specifying the layer. The default value is 36.

**`vecAxisPt`**
: A _Vector_ specifying the axis point. The default value is [0.0,0.0,0.0].

**`vecAxisVect`**
: A _Vector_ specifying the axis vector. The default value is [1.0,0.0,0.0].

**`bInterfaceElem`**
: A _Boolean_ specifying the interface element. The default value is False.

**`bExtrusion`**
: A _Boolean_ specifying the extrusion. The default value is False.

**`dTranslationExtrusion`**
: A _Double_ specifying the translation extrusion. The default value is 0.0.

**`dBDeleteOriginalParts`**
: A _Double_ specifying the delete original parts. The default value is 0.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
HexModeling.Circular(crlFace=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0)
```
