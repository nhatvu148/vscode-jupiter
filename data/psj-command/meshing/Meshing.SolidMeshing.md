```{module} Meshing.SolidMeshing()
:synopsis: Solid Meshing
```

(Meshing.SolidMeshing)=

# Meshing.SolidMeshing

## Description

Solid Meshing

## Syntax

```python
Meshing.SolidMeshing(crlPart=[], bTet10=False, dGradingFactor=0, bGravCenter=False, dStretchLimit=0, iSpeedVsQual=0, iSpeedVsMem=0, iRegion=0, bInternalNodes=True, bSafeMode=True, iParallel=0, bSurfaceNodes=True, bEdgeNodes=True, bPreservation=True, bInternalMeshOnly=True, bMeshColor=False, iPartColor=2763429)
```

Macro: {ref}`Macro-Meshing-VolMeshing`

Ribbon: {menuselection}`Meshing --> SolidMeshing`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`bTet10`**
: A _Boolean_ specifying the tet10. The default value is False.

**`dGradingFactor`**
: A _Double_ specifying the grading factor. The default value is 0.

**`bGravCenter`**
: A _Boolean_ specifying the grav center. The default value is False.

**`dStretchLimit`**
: A _Double_ specifying the stretch limit. The default value is 0.

**`iSpeedVsQual`**
: An _Integer_ specifying the speed vs qual. The default value is 0.

**`iSpeedVsMem`**
: An _Integer_ specifying the speed vs mem. The default value is 0.

**`iRegion`**
: An _Integer_ specifying the region. The default value is 0.

**`bInternalNodes`**
: A _Boolean_ specifying the internal nodes. The default value is True.

**`bSafeMode`**
: A _Boolean_ specifying the safe mode. The default value is True.

**`iParallel`**
: An _Integer_ specifying the parallel. The default value is 0.

**`bSurfaceNodes`**
: A _Boolean_ specifying the surface nodes. The default value is True.

**`bEdgeNodes`**
: A _Boolean_ specifying the edge nodes. The default value is True.

**`bPreservation`**
: A _Boolean_ specifying the preservation. The default value is True.

**`bInternalMeshOnly`**
: A _Boolean_ specifying the internal mesh only. The default value is True.

**`bMeshColor`**
: A _Boolean_ specifying the mesh color. The default value is False.

**`iPartColor`**
: An _Integer_ specifying the part color. The default value is 2763429.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.SolidMeshing(crlPart=[], bTet10=False, dGradingFactor=0, bGravCenter=False, dStretchLimit=0, iSpeedVsQual=0, iSpeedVsMem=0, iRegion=0, bInternalNodes=True, bSafeMode=True, iParallel=0, bSurfaceNodes=True, bEdgeNodes=True, bPreservation=True, bInternalMeshOnly=True, bMeshColor=False, iPartColor=2763429)
```
