```{module} Tools.Coordinates.AttachCircle()
:synopsis: create Coordinate by AttachCircle
```

(Tools.Coordinates.AttachCircle)=

# Tools.Coordinates.AttachCircle

## Description

create Coordinate by AttachCircle

## Syntax

```python
Tools.Coordinates.AttachCircle(strName="CRect1", iCoordType=0, crEdge=None, bCreateNew=True, crRefCoord=None, crEdit=None)
```

Macro: {ref}`Macro-Tools-CreateCoordinateAttachCircle`

Ribbon: {menuselection}`Tools --> Coordinates --> AttachCircle`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "CRect1".

**`iCoordType`**
: An _Integer_ specifying the coordinate type. The default value is 0.

**`crEdge`**
: A _Cursor_ specifying the edge. The default value is None.

**`bCreateNew`**
: A _Boolean_ specifying the create new. The default value is True.

**`crRefCoord`**
: A _Cursor_ specifying the reference coordinate. The default value is None.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.Coordinates.AttachCircle(strName="CRect1", iCoordType=0, crEdge=None, bCreateNew=True, crRefCoord=None, crEdit=None)
```
