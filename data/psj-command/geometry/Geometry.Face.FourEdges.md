```{module} Geometry.Face.FourEdges()
:synopsis: Create face by four edges
```

(Geometry.Face.FourEdges)=

# Geometry.Face.FourEdges

## Description

Create face by four edges

## Syntax

```python
Geometry.Face.FourEdges(crlEdge)
```

Macro: {ref}`Macro-Geometry-CreateFaceFromFourEdges`

Ribbon: {menuselection}`Geometry --> Face --> FourEdges`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Face.FourEdges(crlEdge)
```
