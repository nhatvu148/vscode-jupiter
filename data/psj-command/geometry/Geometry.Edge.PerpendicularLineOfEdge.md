```{module} Geometry.Edge.PerpendicularLineOfEdge()
:synopsis: Imprint the perpendicular line of edge
```

(Geometry.Edge.PerpendicularLineOfEdge)=

# Geometry.Edge.PerpendicularLineOfEdge

## Description

Imprint the perpendicular line of edge

## Syntax

```python
Geometry.Edge.PerpendicularLineOfEdge(crlNode, crlFace, dOffset=0, bReakFace=True)
```

Macro: {ref}`Macro-Geometry-ImprintPerpendicularLine`

Ribbon: {menuselection}`Geometry --> Edge --> PerpendicularLineOfEdge`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`dOffset`**
: A _Double_ specifying the offset. The default value is 0.

**`bReakFace`**
: A _Boolean_ specifying the reak face. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.PerpendicularLineOfEdge(crlNode, crlFace, dOffset=0, bReakFace=True)
```
