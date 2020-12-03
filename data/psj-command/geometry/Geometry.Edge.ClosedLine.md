```{module} Geometry.Edge.ClosedLine()
:synopsis: imprint closed line
```

(Geometry.Edge.ClosedLine)=

# Geometry.Edge.ClosedLine

## Description

imprint closed line

## Syntax

```python
Geometry.Edge.ClosedLine(veclPositions, crlTargetFace, iEnableBreakFace=1)
```

Macro: {ref}`Macro-Geometry-ImprintCloseLineS`

Ribbon: {menuselection}`Geometry --> Edge --> ClosedLine`

## Inputs

**`veclPositions`**
: A _Vector List_ specifying the positions. This is a required input.

**`crlTargetFace`**
: A _Cursor List_ specifying the target face. This is a required input.

**`iEnableBreakFace`**
: An _Integer_ specifying the enable break face. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.ClosedLine(veclPositions, crlTargetFace, iEnableBreakFace=1)
```
