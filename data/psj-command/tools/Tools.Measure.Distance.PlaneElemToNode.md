```{module} Tools.Measure.Distance.PlaneElemToNode()
:synopsis: Measure Distance between Node and plane (created by element).
```

(Tools.Measure.Distance.PlaneElemToNode)=

# Tools.Measure.Distance.PlaneElemToNode

## Description

Measure Distance between Node and plane (created by element).

## Syntax

```python
Tools.Measure.Distance.PlaneElemToNode(crNode=None, crElem=None, iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureDistanceByPlaneElem_Node`

Ribbon: {menuselection}`Tools --> Measure --> Distance --> PlaneElemToNode`

## Inputs

**`crNode`**
: A _Cursor_ specifying the node. The default value is None.

**`crElem`**
: A _Cursor_ specifying the element. The default value is None.

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Measure.Distance.PlaneElemToNode(crNode=None, crElem=None, iPrecision=6)
```
