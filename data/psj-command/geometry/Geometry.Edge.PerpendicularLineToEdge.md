```{module} Geometry.Edge.PerpendicularLineToEdge()
:synopsis:
```

(Geometry.Edge.PerpendicularLineToEdge)=

# Geometry.Edge.PerpendicularLineToEdge

## Description

## Syntax

```python
Geometry.Edge.PerpendicularLineToEdge(crNode=None, crEdge=None, crlFace=[], bBreakFace=True)
```

Macro: {ref}`Macro-Geometry-ImprintPerpendicularLine2`

Ribbon: {menuselection}`Geometry --> Edge --> PerpendicularLineToEdge`

## Inputs

**`crNode`**
: A _Cursor_ specifying the node. The default value is None.

**`crEdge`**
: A _Cursor_ specifying the edge. The default value is None.

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`bBreakFace`**
: A _Boolean_ specifying the break face. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.PerpendicularLineToEdge(crNode=None, crEdge=None, crlFace=[], bBreakFace=True)
```
