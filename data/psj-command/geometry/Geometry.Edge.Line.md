```{module} Geometry.Edge.Line()
:synopsis: Imprint line 2 point
```

(Geometry.Edge.Line)=

# Geometry.Edge.Line

## Description

Imprint line 2 point

## Syntax

```python
Geometry.Edge.Line(poslPositions, crlTargetFace, bBreakFace=True)
```

Macro: {ref}`Macro-Geometry-ImprintLineS`

Ribbon: {menuselection}`Geometry --> Edge --> Line`

## Inputs

**`poslPositions`**
: A _Position List_ specifying the positions. This is a required input.

**`crlTargetFace`**
: A _Cursor List_ specifying the target face. This is a required input.

**`bBreakFace`**
: A _Boolean_ specifying the break face. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.Line(poslPositions, crlTargetFace, bBreakFace=True)
```
