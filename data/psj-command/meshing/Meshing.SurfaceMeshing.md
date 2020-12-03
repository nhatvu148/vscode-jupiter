```{module} Meshing.SurfaceMeshing()
:synopsis: Surface Meshing
```

(Meshing.SurfaceMeshing)=

# Meshing.SurfaceMeshing

## Description

Surface Meshing

## Syntax

```python
Meshing.SurfaceMeshing(crlPart=[], surfaceMesh=SURFACE_MESH(), bUseSetting=True, bFMesher=False, iThreadNum=8, bRefData=True, bMeshColor=False, iPartColor=65280)
```

Macro: {ref}`Macro-Meshing-SurfaceMeshing2D`

Ribbon: {menuselection}`Meshing --> SurfaceMeshing`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`surfaceMesh`**
: A _SURFACE_MESH_ specifying the mesh. The default value is SURFACE_MESH().

**`bUseSetting`**
: A _Boolean_ specifying the use setting. The default value is True.

**`bFMesher`**
: A _Boolean_ specifying the mesher. The default value is False.

**`iThreadNum`**
: An _Integer_ specifying the thread number. The default value is 8.

**`bRefData`**
: A _Boolean_ specifying the reference data. The default value is True.

**`bMeshColor`**
: A _Boolean_ specifying the mesh color. The default value is False.

**`iPartColor`**
: An _Integer_ specifying the part color. The default value is 65280.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.SurfaceMeshing(crlPart=[], surfaceMesh=SURFACE_MESH(), bUseSetting=True, bFMesher=False, iThreadNum=8, bRefData=True, bMeshColor=False, iPartColor=65280)
```
