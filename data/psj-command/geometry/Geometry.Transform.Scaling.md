```{module} Geometry.Transform.Scaling()
:synopsis: Scale Body
```

(Geometry.Transform.Scaling)=

# Geometry.Transform.Scaling

## Description

Scale Body

## Syntax

```python
Geometry.Transform.Scaling(crlPart, dlScaleVector=[1.0,1.0,1.0], dlScaleCentre=[0.0,0.0,0.0], crCoordinate=None, bCreateNew=False, bCopyLbc=False, bCopyProperty=False, bUsepartcenter=True)
```

Macro: {ref}`Macro-Geometry-ScaleBody`

Ribbon: {menuselection}`Geometry --> Transform --> Scaling`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`dlScaleVector`**
: A _Double List_ specifying the scale vector. The default value is [1.0,1.0,1.0].

**`dlScaleCentre`**
: A _Double List_ specifying the scale centre. The default value is [0.0,0.0,0.0].

**`crCoordinate`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`bCreateNew`**
: A _Boolean_ specifying the create new. The default value is False.

**`bCopyLbc`**
: A _Boolean_ specifying the copy load boundary condition. The default value is False.

**`bCopyProperty`**
: A _Boolean_ specifying the copy property. The default value is False.

**`bUsepartcenter`**
: A _Boolean_ specifying the usepartcenter. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Transform.Scaling(crlPart, dlScaleVector=[1.0,1.0,1.0], dlScaleCentre=[0.0,0.0,0.0], crCoordinate=None, bCreateNew=False, bCopyLbc=False, bCopyProperty=False, bUsepartcenter=True)
```
