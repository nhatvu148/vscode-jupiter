```{module} Tools.Measure.Distance.EdgeNode()
:synopsis: Measure Distance From Node to Edge
```

(Tools.Measure.Distance.EdgeNode)=

# Tools.Measure.Distance.EdgeNode

## Description

Measure Distance From Node to Edge

## Syntax

```python
Tools.Measure.Distance.EdgeNode(crEdge, crNode, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureDistanceByEdge_Node`

Ribbon: {menuselection}`Tools --> Measure --> Distance --> EdgeNode`

## Inputs

**`crEdge`**
: A _Cursor_ specifying the edge. This is a required input.

**`crNode`**
: A _Cursor_ specifying the node. This is a required input.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Distance.EdgeNode(crEdge, crNode, iPrecision=6)
```
