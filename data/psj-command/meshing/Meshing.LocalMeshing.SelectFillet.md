```{module} Meshing.LocalMeshing.SelectFillet()
:synopsis: Unknown Description
```

(Meshing.LocalMeshing.SelectFillet)=

# Meshing.LocalMeshing.SelectFillet

## Description

Unknown Description

## Syntax

```python
Meshing.LocalMeshing.SelectFillet(crlItems=[], dSelectWidthMin=1, dSelectWidthMax=10, dSelectRMin=1, dSelectRMax=10, dAngleMin=0.0, dAngleMax=171.0, bConvex=True, bConcave=True)
```

Macro: {ref}`Macro-Meshing-MeshingLocalMeshingFilletSelect`

Ribbon: {menuselection}`Meshing --> LocalMeshing --> SelectFillet`

## Inputs

**`crlItems`**
: A _Cursor List_ specifying the items. The default value is [].

**`dSelectWidthMin`**
: A _Double_ specifying the select width minimum. The default value is 1.

**`dSelectWidthMax`**
: A _Double_ specifying the select width maximum. The default value is 10.

**`dSelectRMin`**
: A _Double_ specifying the select radius minimum. The default value is 1.

**`dSelectRMax`**
: A _Double_ specifying the select radius maximum. The default value is 10.

**`dAngleMin`**
: A _Double_ specifying the angle minimum. The default value is 0.0.

**`dAngleMax`**
: A _Double_ specifying the angle maximum. The default value is 171.0.

**`bConvex`**
: A _Boolean_ specifying the convex. The default value is True.

**`bConcave`**
: A _Boolean_ specifying the concave. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.LocalMeshing.SelectFillet(crlItems=[], dSelectWidthMin=1, dSelectWidthMax=10, dSelectRMin=1, dSelectRMax=10, dAngleMin=0.0, dAngleMax=171.0, bConvex=True, bConcave=True)
```
