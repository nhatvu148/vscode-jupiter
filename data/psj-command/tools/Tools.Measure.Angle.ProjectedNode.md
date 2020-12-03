```{module} Tools.Measure.Angle.ProjectedNode()
:synopsis: measure angle on projected node
```

(Tools.Measure.Angle.ProjectedNode)=

# Tools.Measure.Angle.ProjectedNode

## Description

measure angle on projected node

## Syntax

```python
Tools.Measure.Angle.ProjectedNode(crNode, strTarget="All", iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureAngleByProjected_Node`

Ribbon: {menuselection}`Tools --> Measure --> Angle --> ProjectedNode`

## Inputs

**`crNode`**
: A _Cursor_ specifying the node. This is a required input.

**`strTarget`**
: A _String_ specifying the target. The default value is "All".

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Angle.ProjectedNode(crNode, strTarget="All", iPrecision=6)
```
