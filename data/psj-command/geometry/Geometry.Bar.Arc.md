```{module} Geometry.Bar.Arc()
:synopsis: Create Edge by spline
```

(Geometry.Bar.Arc)=

# Geometry.Bar.Arc

## Description

Create Edge by spline

## Syntax

```python
Geometry.Bar.Arc(crlNode, crPart=None, strBarName="")
```

Macro: {ref}`Macro-Geometry-CreateBarArc`

Ribbon: {menuselection}`Geometry --> Bar --> Arc`

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
Geometry.Bar.Arc(crlNode, crPart=None, strBarName="")
```
