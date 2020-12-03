```{module} Tools.Coordinates.Face()
:synopsis: create Coordinate by Face
```

(Tools.Coordinates.Face)=

# Tools.Coordinates.Face

## Description

create Coordinate by Face

## Syntax

```python
Tools.Coordinates.Face(strName="CRect1", iCoordType=0, iOrder=0, veclPoint=[], crlNode=[], crItem=None, crRefCoord=None, crEdit=None)
```

Macro: {ref}`Macro-Tools-CreateCoordinateFace`

Ribbon: {menuselection}`Tools --> Coordinates --> Face`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "CRect1".

**`iCoordType`**
: An _Integer_ specifying the coordinate type. The default value is 0.

**`iOrder`**
: An _Integer_ specifying the order. The default value is 0.

**`veclPoint`**
: A _Vector List_ specifying the point. The default value is [].

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crItem`**
: A _Cursor_ specifying the item. The default value is None.

**`crRefCoord`**
: A _Cursor_ specifying the reference coordinate. The default value is None.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Coordinates.Face(strName="CRect1", iCoordType=0, iOrder=0, veclPoint=[], crlNode=[], crItem=None, crRefCoord=None, crEdit=None)
```
