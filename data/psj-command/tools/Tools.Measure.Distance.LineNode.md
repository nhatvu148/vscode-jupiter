```{module} Tools.Measure.Distance.LineNode()
:synopsis: Measures the distance of a perpendicular line from a node toward the line defined by the two nodes.
```

(Tools.Measure.Distance.LineNode)=

# Tools.Measure.Distance.LineNode

## Description

Measures the distance of a perpendicular line from a node toward the line defined by the two nodes.

## Syntax

```python
Tools.Measure.Distance.LineNode(crlTargetNode, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureDistanceByLine2Nodes_Node`

Ribbon: {menuselection}`Tools --> Measure --> Distance --> LineNode`

## Inputs

**`crlTargetNode`**
: A _Cursor List_ specifying the target node. This is a required input.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Distance.LineNode(crlTargetNode, iPrecision=6)
```
