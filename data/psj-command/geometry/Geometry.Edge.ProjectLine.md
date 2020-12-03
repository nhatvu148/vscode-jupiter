```{module} Geometry.Edge.ProjectLine()
:synopsis:
```

(Geometry.Edge.ProjectLine)=

# Geometry.Edge.ProjectLine

## Description

## Syntax

```python
Geometry.Edge.ProjectLine(crlEdge=[], crlFaces=[], crlNode=[], bBreakFace=True, iType=0, bCheckGap=False, dGap=0.0)
```

Macro: {ref}`Macro-Geometry-Imprint_Projection_LineS`

Ribbon: {menuselection}`Geometry --> Edge --> ProjectLine`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. The default value is [].

**`crlFaces`**
: A _Cursor List_ specifying the faces. The default value is [].

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`bBreakFace`**
: A _Boolean_ specifying the break face. The default value is True.

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`bCheckGap`**
: A _Boolean_ specifying the check gap. The default value is False.

**`dGap`**
: A _Double_ specifying the gap. The default value is 0.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.ProjectLine(crlEdge=[], crlFaces=[], crlNode=[], bBreakFace=True, iType=0, bCheckGap=False, dGap=0.0)
```
