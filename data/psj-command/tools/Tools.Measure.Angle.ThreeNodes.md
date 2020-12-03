```{module} Tools.Measure.Angle.ThreeNodes()
:synopsis:
```

(Tools.Measure.Angle.ThreeNodes)=

# Tools.Measure.Angle.ThreeNodes

## Description

## Syntax

```python
Tools.Measure.Angle.ThreeNodes(crNode1, crNode2, crNode3, strTarget="All", iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureAngleBy3Nodes`

Ribbon: {menuselection}`Tools --> Measure --> Angle --> ThreeNodes`

## Inputs

**`crNode1`**
: A _Cursor_ specifying the node1. This is a required input.

**`crNode2`**
: A _Cursor_ specifying the node2. This is a required input.

**`crNode3`**
: A _Cursor_ specifying the node3. This is a required input.

**`strTarget`**
: A _String_ specifying the target. The default value is "All".

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Angle.ThreeNodes(crNode1, crNode2, crNode3, strTarget="All", iPrecision=6)
```
