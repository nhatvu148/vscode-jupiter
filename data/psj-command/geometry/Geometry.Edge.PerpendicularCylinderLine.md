```{module} Geometry.Edge.PerpendicularCylinderLine()
:synopsis:
```

(Geometry.Edge.PerpendicularCylinderLine)=

# Geometry.Edge.PerpendicularCylinderLine

## Description

## Syntax

```python
Geometry.Edge.PerpendicularCylinderLine(crlNode=[], crlFace=[], iMethod=0, dOffset=0.0, bOppositeSide=False, bBreakFace=True)
```

Macro: {ref}`Macro-Geometry-ImprintPerpendicularCylinderLineS`

Ribbon: {menuselection}`Geometry --> Edge --> PerpendicularCylinderLine`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`dOffset`**
: A _Double_ specifying the offset. The default value is 0.0.

**`bOppositeSide`**
: A _Boolean_ specifying the opposite side. The default value is False.

**`bBreakFace`**
: A _Boolean_ specifying the break face. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.PerpendicularCylinderLine(crlNode=[], crlFace=[], iMethod=0, dOffset=0.0, bOppositeSide=False, bBreakFace=True)
```
