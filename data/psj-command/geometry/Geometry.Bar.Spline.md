```{module} Geometry.Bar.Spline()
:synopsis: Create Edge by spline
```

(Geometry.Bar.Spline)=

# Geometry.Bar.Spline

## Description

Create Edge by spline

## Syntax

```python
Geometry.Bar.Spline(crlNode, crPart=None, strBarName="")
```

Macro: {ref}`Macro-Geometry-CreateBarSpline`

Ribbon: {menuselection}`Geometry --> Bar --> Spline`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

**`crPart`**
: A _Cursor_ specifying the part. The default value is None.

**`strBarName`**
: A _String_ specifying the bar name. The default value is "".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Bar.Spline(crlNode, crPart=None, strBarName="")
```
