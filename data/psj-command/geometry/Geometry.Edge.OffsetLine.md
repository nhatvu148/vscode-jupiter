```{module} Geometry.Edge.OffsetLine()
:synopsis: Imprint geometry edge offset line
```

(Geometry.Edge.OffsetLine)=

# Geometry.Edge.OffsetLine

## Description

Imprint geometry edge offset line

## Syntax

```python
Geometry.Edge.OffsetLine(crlFace=[], crlEdge=[], bBreakFace=True, dOffsetDistance=0.0, iNumberLayer=1, bMerge=True, bExtend=True, iLayerMethod=0, dlVlayerOffset=[], bAutoCollapse=False, iRLType=2)
```

Macro: {ref}`Macro-Geometry-ImprintOffsetLineS`

Ribbon: {menuselection}`Geometry --> Edge --> OffsetLine`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`crlEdge`**
: A _Cursor List_ specifying the edge. The default value is [].

**`bBreakFace`**
: A _Boolean_ specifying the break face. The default value is True.

**`dOffsetDistance`**
: A _Double_ specifying the offset distance. The default value is 0.0.

**`iNumberLayer`**
: An _Integer_ specifying the number layer. The default value is 1.

**`bMerge`**
: A _Boolean_ specifying the merge. The default value is True.

**`bExtend`**
: A _Boolean_ specifying the extend. The default value is True.

**`iLayerMethod`**
: An _Integer_ specifying the layer method. The default value is 0.

**`dlVlayerOffset`**
: A _Double List_ specifying the vlayer offset. The default value is [].

**`bAutoCollapse`**
: A _Boolean_ specifying the auto collapse. The default value is False.

**`iRLType`**
: An _Integer_ specifying the r l type. The default value is 2.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.OffsetLine(crlFace=[], crlEdge=[], bBreakFace=True, dOffsetDistance=0.0, iNumberLayer=1, bMerge=True, bExtend=True, iLayerMethod=0, dlVlayerOffset=[], bAutoCollapse=False, iRLType=2)
```
