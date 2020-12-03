```{module} Meshing.LocalRemesh.Surfase()
:synopsis: local surface remesh
```

(Meshing.LocalRemesh.Surfase)=

# Meshing.LocalRemesh.Surfase

## Description

local surface remesh

## Syntax

```python
Meshing.LocalRemesh.Surfase(crlTarget=[], surfaceMesh = SURFACE_MESH(), bUseSetting=True, bGrading=False, bFMesher=False, iOverrideType=1, bKeepConnection=False, bProjCAD=True, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001,bIDchcek = False, bKeepRemeshEdge = False)
```

Macro: {ref}`Macro-Meshing-LocalRemeshTriQuad`

Ribbon: {menuselection}`Meshing --> LocalRemesh --> Surfase`

## Inputs

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`surfaceMesh`**
: A _SURFACE_MESH_ specifying the mesh. The default value is SURFACE_MESH().

**`bUseSetting`**
: A _Boolean_ specifying the use setting. The default value is True.

**`bGrading`**
: A _Boolean_ specifying the grading. The default value is False.

**`bFMesher`**
: A _Boolean_ specifying the mesher. The default value is False.

**`iOverrideType`**
: An _Integer_ specifying the override type. The default value is 1.

**`bKeepConnection`**
: A _Boolean_ specifying the keep connection. The default value is False.

**`bProjCAD`**
: A _Boolean_ specifying the projection CAD. The default value is True.

**`bTinyFaceMerge`**
: A _Boolean_ specifying the tiny face merge. The default value is False.

**`dMinFaceWidth`**
: A _Double_ specifying the minimum face width. The default value is 0.

**`dMaxFaceWidth`**
: A _Double_ specifying the maximum face width. This is a required input.

**`bKeepRemeshEdge`**
: A _Boolean_ specifying the keep remesh edge. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.LocalRemesh.Surfase(crlTarget=[], surfaceMesh = SURFACE_MESH(), bUseSetting=True, bGrading=False, bFMesher=False, iOverrideType=1, bKeepConnection=False, bProjCAD=True, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001,bIDchcek = False, bKeepRemeshEdge = False)
```
