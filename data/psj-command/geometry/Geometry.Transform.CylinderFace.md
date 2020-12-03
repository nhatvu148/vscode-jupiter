```{module} Geometry.Transform.CylinderFace()
:synopsis: transform position
```

(Geometry.Transform.CylinderFace)=

# Geometry.Transform.CylinderFace

## Description

transform position

## Syntax

```python
Geometry.Transform.CylinderFace(crlPart, veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False)
```

Macro: {ref}`Macro-Geometry-Transform_CylinderFace`

Ribbon: {menuselection}`Geometry --> Transform --> CylinderFace`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`veclPoint`**
: A _Vector List_ specifying the point. The default value is [[0.0, 0.0, 0.0]].

**`bCreateNewPart`**
: A _Boolean_ specifying the create new part. The default value is False.

**`bCopyLBC`**
: A _Boolean_ specifying the copy load boundary condition. The default value is False.

**`bCopyProperty`**
: A _Boolean_ specifying the copy property. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Transform.CylinderFace(crlPart, veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False)
```
