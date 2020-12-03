```{module} Tools.Coordinates.AttachNode()
:synopsis: create Coordinate by AttachNode
```

(Tools.Coordinates.AttachNode)=

# Tools.Coordinates.AttachNode

## Description

create Coordinate by AttachNode

## Syntax

```python
Tools.Coordinates.AttachNode(strName="CRect1", iCoordType=0, crNode=None, bCreateNew=True, crRefCoord=None, crEdit=None)
```

Macro: {ref}`Macro-Tools-CreateCoordinateAttachNode`

Ribbon: {menuselection}`Tools --> Coordinates --> AttachNode`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "CRect1".

**`iCoordType`**
: An _Integer_ specifying the coordinate type. The default value is 0.

**`crNode`**
: A _Cursor_ specifying the node. The default value is None.

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
Tools.Coordinates.AttachNode(strName="CRect1", iCoordType=0, crNode=None, bCreateNew=True, crRefCoord=None, crEdit=None)
```
