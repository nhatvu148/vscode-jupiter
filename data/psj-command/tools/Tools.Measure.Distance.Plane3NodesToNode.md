```{module} Tools.Measure.Distance.Plane3NodesToNode()
:synopsis: measure the distance from node to plane(defined by 3 nodes)
```

(Tools.Measure.Distance.Plane3NodesToNode)=

# Tools.Measure.Distance.Plane3NodesToNode

## Description

measure the distance from node to plane(defined by 3 nodes)

## Syntax

```python
Tools.Measure.Distance.Plane3NodesToNode(crNode1, crNode2, crNode3, crNode, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureDistanceByPlane3Nodes_Node`

Ribbon: {menuselection}`Tools --> Measure --> Distance --> Plane3NodesToNode`

## Inputs

**`crNode1`**
: A _Cursor_ specifying the node1. This is a required input.

**`crNode2`**
: A _Cursor_ specifying the node2. This is a required input.

**`crNode3`**
: A _Cursor_ specifying the node3. This is a required input.

**`crNode`**
: A _Cursor_ specifying the node. This is a required input.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Distance.Plane3NodesToNode(crNode1, crNode2, crNode3, crNode, iPrecision=6)
```
