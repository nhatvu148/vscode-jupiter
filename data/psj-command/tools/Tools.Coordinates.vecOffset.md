```{module} Tools.Coordinates.vecOffset()
:synopsis: Unknown Description
```

(Tools.Coordinates.vecOffset)=

# Tools.Coordinates.vecOffset

## Description

Unknown Description

## Syntax

```python
Tools.Coordinates.vecOffset(strName="CRect1", iCoordType=0, vTranslate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None)
```

Macro: {ref}`Macro-Tools-CreateCoordinateOffset`

Ribbon: {menuselection}`Tools --> Coordinates --> vecOffset`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "CRect1".

**`iCoordType`**
: An _Integer_ specifying the coordinate type. The default value is 0.

**`vTranslate`**
: A _V_TRANSLATE_ specifying the translate. The default value is [0.0,0.0,0.0].

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
Tools.Coordinates.vecOffset(strName="CRect1", iCoordType=0, vTranslate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None)
```
