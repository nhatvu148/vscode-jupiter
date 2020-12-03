```{module} Geometry.BodyCut.By3Points()
:synopsis: Body Cut by 3 Points
```

(Geometry.BodyCut.By3Points)=

# Geometry.BodyCut.By3Points

## Description

Body Cut by 3 Points

## Syntax

```python
Geometry.BodyCut.By3Points(crPart=None, poslPosition=[], dOffset=0.0, bSplitonly=False, bMakesectionface=True, bShareface=False)
```

Macro: {ref}`Macro-Geometry-BodyCutBy3PointsS`

Ribbon: {menuselection}`Geometry --> BodyCut --> By3Points`

## Inputs

**`crPart`**
: A _Cursor_ specifying the part. The default value is None.

**`poslPosition`**
: A _Position List_ specifying the position. The default value is [].

**`dOffset`**
: A _Double_ specifying the offset. The default value is 0.0.

**`bSplitonly`**
: A _Boolean_ specifying the splitonly. The default value is False.

**`bMakesectionface`**
: A _Boolean_ specifying the makesectionface. The default value is True.

**`bShareface`**
: A _Boolean_ specifying the shareface. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.BodyCut.By3Points(crPart=None, poslPosition=[], dOffset=0.0, bSplitonly=False, bMakesectionface=True, bShareface=False)
```
