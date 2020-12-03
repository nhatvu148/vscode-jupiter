```{module} Tools.Measure.Distance.TwoNodes()
:synopsis: Measure Distance Two Nodes
```

(Tools.Measure.Distance.TwoNodes)=

# Tools.Measure.Distance.TwoNodes

## Description

Measure Distance Two Nodes

## Syntax

```python
Tools.Measure.Distance.TwoNodes(crNode1=None, crNode2=None, strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```

Macro: {ref}`Macro-Tools-MeasureDistanceBy2Nodes`

Ribbon: {menuselection}`Tools --> Measure --> Distance --> TwoNodes`

## Inputs

**`crNode1`**
: A _Cursor_ specifying the node1. The default value is None.

**`crNode2`**
: A _Cursor_ specifying the node2. The default value is None.

**`strTarget`**
: A _String_ specifying the target. The default value is "ALL".

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

**`crCoordinateSystem`**
: A _Cursor_ specifying the coordinate system. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Distance.TwoNodes(crNode1=None, crNode2=None, strTarget="ALL", iPrecision=6, crCoordinateSystem=None)
```
