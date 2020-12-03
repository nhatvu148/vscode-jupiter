```{module} Geometry.Face.Edges()
:synopsis: Create Face From Edges
```

(Geometry.Face.Edges)=

# Geometry.Face.Edges

## Description

Create Face From Edges

## Syntax

```python
Geometry.Face.Edges(crlEdge, crlPart=[], crlNode=[], bSharedFace=False, bSmoothFace=False, bCreatePart=False, bImproved=False, bBarsOnly=False, bOnlyOnePart=True, bUseMidNodes=False)
```

Macro: {ref}`Macro-Geometry-CreateFaceFromEdges`

Ribbon: {menuselection}`Geometry --> Face --> Edges`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`bSharedFace`**
: A _Boolean_ specifying the shared face. The default value is False.

**`bSmoothFace`**
: A _Boolean_ specifying the smooth face. The default value is False.

**`bCreatePart`**
: A _Boolean_ specifying the create part. The default value is False.

**`bImproved`**
: A _Boolean_ specifying the improved. The default value is False.

**`bBarsOnly`**
: A _Boolean_ specifying the bars only. The default value is False.

**`bOnlyOnePart`**
: A _Boolean_ specifying the only one part. The default value is True.

**`bUseMidNodes`**
: A _Boolean_ specifying the use mid nodes. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Face.Edges(crlEdge, crlPart=[], crlNode=[], bSharedFace=False, bSmoothFace=False, bCreatePart=False, bImproved=False, bBarsOnly=False, bOnlyOnePart=True, bUseMidNodes=False)
```
