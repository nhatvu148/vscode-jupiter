```{module} Tools.Measure.Angle.TwoNodesAxis()
:synopsis: Measure the angle created by 2 nodes and Axis.
```

(Tools.Measure.Angle.TwoNodesAxis)=

# Tools.Measure.Angle.TwoNodesAxis

## Description

Measure the angle created by 2 nodes and Axis.

## Syntax

```python
Tools.Measure.Angle.TwoNodesAxis(crNode1, crNode2, dlAxis=[1,0,0], strTarget="Angle", iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureAngleBy2Nodes_Axis`

Ribbon: {menuselection}`Tools --> Measure --> Angle --> TwoNodesAxis`

## Inputs

**`crNode1`**
: A _Cursor_ specifying the node1. This is a required input.

**`crNode2`**
: A _Cursor_ specifying the node2. This is a required input.

**`dlAxis`**
: A _Double List_ specifying the axis. The default value is [1,0,0].

**`strTarget`**
: A _String_ specifying the target. The default value is "Angle".

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Angle.TwoNodesAxis(crNode1, crNode2, dlAxis=[1,0,0], strTarget="Angle", iPrecision=6)
```
