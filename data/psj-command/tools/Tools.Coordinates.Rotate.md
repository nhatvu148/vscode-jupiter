```{module} Tools.Coordinates.Rotate()
:synopsis: create Coordinate by Rotate
```

(Tools.Coordinates.Rotate)=

# Tools.Coordinates.Rotate

## Description

create Coordinate by Rotate

## Syntax

```python
Tools.Coordinates.Rotate(strName="CRect1", iCoordType=0, vecRotate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None)
```

Macro: {ref}`Macro-Tools-CreateCoordinateRotate`

Ribbon: {menuselection}`Tools --> Coordinates --> Rotate`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "CRect1".

**`iCoordType`**
: An _Integer_ specifying the coordinate type. The default value is 0.

**`vecRotate`**
: A _Vector_ specifying the rotate. The default value is [0.0,0.0,0.0].

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
Tools.Coordinates.Rotate(strName="CRect1", iCoordType=0, vecRotate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None)
```
