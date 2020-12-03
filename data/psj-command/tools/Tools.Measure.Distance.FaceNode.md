```{module} Tools.Measure.Distance.FaceNode()
:synopsis: Measure Distance By FaceNode
```

(Tools.Measure.Distance.FaceNode)=

# Tools.Measure.Distance.FaceNode

## Description

Measure Distance By FaceNode

## Syntax

```python
Tools.Measure.Distance.FaceNode(crlFace, crlNode, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureDistanceByNode2Face`

Ribbon: {menuselection}`Tools --> Measure --> Distance --> FaceNode`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Distance.FaceNode(crlFace, crlNode, iPrecision=6)
```
