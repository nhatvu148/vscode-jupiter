```{module} Geometry.BreakEntity.Edge()
:synopsis: Break selected edge
```

(Geometry.BreakEntity.Edge)=

# Geometry.BreakEntity.Edge

## Description

Break selected edge

## Syntax

```python
Geometry.BreakEntity.Edge(crlPart=[], crlFace=[], crlEdge=[], crlNode=[], bAutoByAngle=False, dEdgeAngle=60.0)
```

Macro: {ref}`Macro-Geometry-BreakEdgeCr`

Ribbon: {menuselection}`Geometry --> BreakEntity --> Edge`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`crlEdge`**
: A _Cursor List_ specifying the edge. The default value is [].

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`bAutoByAngle`**
: A _Boolean_ specifying the auto by angle. The default value is False.

**`dEdgeAngle`**
: A _Double_ specifying the edge angle. The default value is 60.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.BreakEntity.Edge(crlPart=[], crlFace=[], crlEdge=[], crlNode=[], bAutoByAngle=False, dEdgeAngle=60.0)
```
