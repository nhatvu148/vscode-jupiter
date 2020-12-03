```{module} Designer.Load.Moment()
:synopsis: Create moment
```

(Designer.Load.Moment)=

# Designer.Load.Moment

## Description

Create moment

## Syntax

```python
Designer.Load.Moment(strName="", crlFace=[], dlVecMomentXYZ=[0.0,0.0,0.0], crCoord=None, crEdit=None)
```

Macro: {ref}`Macro-Designer-Moment`

Ribbon: {menuselection}`Designer --> Load --> Moment`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`dlVecMomentXYZ`**
: A _Double List_ specifying the vector moment x y z. The default value is [0.0,0.0,0.0].

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Designer.Load.Moment(strName="", crlFace=[], dlVecMomentXYZ=[0.0,0.0,0.0], crCoord=None, crEdit=None)
```
