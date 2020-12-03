```{module} Geometry.Edge.ExtendLine()
:synopsis: make edge by extend line
```

(Geometry.Edge.ExtendLine)=

# Geometry.Edge.ExtendLine

## Description

make edge by extend line

## Syntax

```python
Geometry.Edge.ExtendLine(crlEdge, iMethod=0, iEnd=0, iNoFittingPoints=3, iDiv=2, iEnableBreakFace=1)
```

Macro: {ref}`Macro-Geometry-ImprintExtendLine`

Ribbon: {menuselection}`Geometry --> Edge --> ExtendLine`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iEnd`**
: An _Integer_ specifying the end. The default value is 0.

**`iNoFittingPoints`**
: An _Integer_ specifying the no fitting points. The default value is 3.

**`iDiv`**
: An _Integer_ specifying the divide. The default value is 2.

**`iEnableBreakFace`**
: An _Integer_ specifying the enable break face. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.ExtendLine(crlEdge, iMethod=0, iEnd=0, iNoFittingPoints=3, iDiv=2, iEnableBreakFace=1)
```
