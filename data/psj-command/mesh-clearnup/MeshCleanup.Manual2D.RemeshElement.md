```{module} MeshCleanup.Manual2D.RemeshElement()
:synopsis: local surface remesh
```

(MeshCleanup.Manual2D.RemeshElement)=

# MeshCleanup.Manual2D.RemeshElement

## Description

local surface remesh

## Syntax

```python
MeshCleanup.Manual2D.RemeshElement(crlTarget=[], surfaceMesh=SURFACE_MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False)
```

Macro: {ref}`Macro-MeshCleanup-LocalRemeshTriQuad_MC2D`

Ribbon: {menuselection}`MeshCleanup --> Manual2D --> RemeshElement`

## Inputs

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`surfaceMesh`**
: A _SURFACE_MESH_ specifying the mesh. The default value is SURFACE_MESH().

**`bUseSetting`**
: A _Boolean_ specifying the use setting. The default value is False.

**`bGrading`**
: A _Boolean_ specifying the grading. The default value is False.

**`bFMesher`**
: A _Boolean_ specifying the mesher. The default value is False.

**`iOverrideType`**
: An _Integer_ specifying the override type. The default value is 0.

**`bKeepConnection`**
: A _Boolean_ specifying the keep connection. The default value is False.

**`bProjCAD`**
: A _Boolean_ specifying the projection CAD. The default value is False.

**`bTinyFaceMerge`**
: A _Boolean_ specifying the tiny face merge. The default value is False.

**`dMinFaceWidth`**
: A _Double_ specifying the minimum face width. The default value is 0.

**`dMaxFaceWidth`**
: A _Double_ specifying the maximum face width. The default value is 0.001.

**`bIDchcek`**
: A _Boolean_ specifying the i dchcek. The default value is False.

**`bKeepRemeshEdge`**
: A _Boolean_ specifying the keep remesh edge. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual2D.RemeshElement(crlTarget=[], surfaceMesh=SURFACE_MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False)
```
