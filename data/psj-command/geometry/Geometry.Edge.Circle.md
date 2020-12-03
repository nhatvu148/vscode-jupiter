```{module} Geometry.Edge.Circle()
:synopsis: Imprint Cirlcle Line S
```

(Geometry.Edge.Circle)=

# Geometry.Edge.Circle

## Description

Imprint Cirlcle Line S

## Syntax

```python
Geometry.Edge.Circle(veclPositions, crlTargetFace, dInRadius=1, dOutRadius=4, iNoOfLayer=1, iNoOfDiv=30, bBreakFace=True)
```

Macro: {ref}`Macro-Geometry-ImprintCircleS`

Ribbon: {menuselection}`Geometry --> Edge --> Circle`

## Inputs

**`veclPositions`**
: A _Vector List_ specifying the positions. This is a required input.

**`crlTargetFace`**
: A _Cursor List_ specifying the target face. This is a required input.

**`dInRadius`**
: A _Double_ specifying the in radius. The default value is 1.

**`dOutRadius`**
: A _Double_ specifying the out radius. The default value is 4.

**`iNoOfLayer`**
: An _Integer_ specifying the no of layer. The default value is 1.

**`iNoOfDiv`**
: An _Integer_ specifying the no of divide. The default value is 30.

**`bBreakFace`**
: A _Boolean_ specifying the break face. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Edge.Circle(veclPositions, crlTargetFace, dInRadius=1, dOutRadius=4, iNoOfLayer=1, iNoOfDiv=30, bBreakFace=True)
```
