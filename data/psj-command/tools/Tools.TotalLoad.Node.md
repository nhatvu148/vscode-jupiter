```{module} Tools.TotalLoad.Node()
:synopsis:
```

(Tools.TotalLoad.Node)=

# Tools.TotalLoad.Node

## Description

## Syntax

```python
Tools.TotalLoad.Node(crlTarget=[], crCoordinate=None, strOutput="Total", iPrecision=6)
```

Macro: {ref}`Macro-Tools-MeasureTotalLoad_ForNode`

Ribbon: {menuselection}`Tools --> TotalLoad --> Node`

## Inputs

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crCoordinate`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`strOutput`**
: A _String_ specifying the output. The default value is "Total".

**`iPrecision`**
: An _Integer_ specifying the precision. The default value is 6.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.TotalLoad.Node(crlTarget=[], crCoordinate=None, strOutput="Total", iPrecision=6)
```
