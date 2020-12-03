```{module} Tools.Coordinates.Align()
:synopsis: create Coordinate by Align
```

(Tools.Coordinates.Align)=

# Tools.Coordinates.Align

## Description

create Coordinate by Align

## Syntax

```python
Tools.Coordinates.Align(strName="CRect1", iCoordType=0, iCoordAxis=0, bCreateNew=True, crlNode=[], crEdge=None, crEdit=None)
```

Macro: {ref}`Macro-Tools-CreateCoordinateAlign`

Ribbon: {menuselection}`Tools --> Coordinates --> Align`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "CRect1".

**`iCoordType`**
: An _Integer_ specifying the coordinate type. The default value is 0.

**`iCoordAxis`**
: An _Integer_ specifying the coordinate axis. The default value is 0.

**`bCreateNew`**
: A _Boolean_ specifying the create new. The default value is True.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crEdge`**
: A _Cursor_ specifying the edge. The default value is None.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Coordinates.Align(strName="CRect1", iCoordType=0, iCoordAxis=0, bCreateNew=True, crlNode=[], crEdge=None, crEdit=None)
```
