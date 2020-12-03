```{module} Tools.NodeCS()
:synopsis: create Node CS
```

(Tools.NodeCS)=

# Tools.NodeCS

## Description

create Node CS

## Syntax

```python
Tools.NodeCS(crlInst=[], crCoordSystem=None)
```

Macro: {ref}`Macro-Tools-AddNodeCS`

Ribbon: {menuselection}`Tools --> NodeCS`

## Inputs

**`crlInst`**
: A _Cursor List_ specifying the inst. The default value is [].

**`crCoordSystem`**
: A _Cursor_ specifying the coordinate system. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.NodeCS(crlInst=[], crCoordSystem=None)
```
