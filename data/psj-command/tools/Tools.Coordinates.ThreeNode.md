```{module} Tools.Coordinates.ThreeNode()
:synopsis: create Coordinate by Cylinder Face
```

(Tools.Coordinates.ThreeNode)=

# Tools.Coordinates.ThreeNode

## Description

create Coordinate by Cylinder Face

## Syntax

```python
Tools.Coordinates.ThreeNode(strName="CRect1", iCoordType=0, iOrder=0, crlNode=[], veclPoints=[], crRefCoord=None, crEdit=None)
```

Macro: {ref}`Macro-Tools-CreateCoordinateThreeNode`

Ribbon: {menuselection}`Tools --> Coordinates --> ThreeNode`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "CRect1".

**`iCoordType`**
: An _Integer_ specifying the coordinate type. The default value is 0.

**`iOrder`**
: An _Integer_ specifying the order. The default value is 0.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`veclPoints`**
: A _Vector List_ specifying the points. The default value is [].

**`crRefCoord`**
: A _Cursor_ specifying the reference coordinate. The default value is None.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Coordinates.ThreeNode(strName="CRect1", iCoordType=0, iOrder=0, crlNode=[], veclPoints=[], crRefCoord=None, crEdit=None)
```
