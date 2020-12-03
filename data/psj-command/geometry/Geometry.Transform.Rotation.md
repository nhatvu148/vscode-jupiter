```{module} Geometry.Transform.Rotation()
:synopsis: Rotate the selected Part.
```

(Geometry.Transform.Rotation)=

# Geometry.Transform.Rotation

## Description

Rotate the selected Part.

## Syntax

```python
Geometry.Transform.Rotation(crlPart=[], posCenter=[0,0,0], vecAxis=[1,0,0], dAngle=0, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, iCopyCount=1, bMergeNode=False, dTol=1.0e-5)
```

Macro: {ref}`Macro-Geometry-RotateBody`

Ribbon: {menuselection}`Geometry --> Transform --> Rotation`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`posCenter`**
: A _Position_ specifying the center. The default value is [0,0,0].

**`vecAxis`**
: A _Vector_ specifying the axis. The default value is [1,0,0].

**`dAngle`**
: A _Double_ specifying the angle. The default value is 0.

**`bCreateNewPart`**
: A _Boolean_ specifying the create new part. The default value is False.

**`bCopyLBC`**
: A _Boolean_ specifying the copy load boundary condition. The default value is False.

**`bCopyProperty`**
: A _Boolean_ specifying the copy property. The default value is False.

**`iCopyCount`**
: An _Integer_ specifying the copy count. The default value is 1.

**`bMergeNode`**
: A _Boolean_ specifying the merge node. The default value is False.

**`dTol`**
: A _Double_ specifying the tolerance. The default value is 1.0e-5.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Transform.Rotation(crlPart=[], posCenter=[0,0,0], vecAxis=[1,0,0], dAngle=0, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, iCopyCount=1, bMergeNode=False, dTol=1.0e-5)
```
