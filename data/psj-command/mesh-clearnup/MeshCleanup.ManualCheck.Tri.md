```{module} MeshCleanup.ManualCheck.Tri()
:synopsis: Unknown Description
```

(MeshCleanup.ManualCheck.Tri)=

# MeshCleanup.ManualCheck.Tri

## Description

Unknown Description

## Syntax

```python
MeshCleanup.ManualCheck.Tri(crlPart=[], nElemType=0, veQuality=0, nCheckCondition=0, dLimitValue=0.0, CFLValue=0.0, nNonManifold=0, nCleanupMode=0, crlElem=[])
```

Macro: {ref}`Macro-MeshCleanup-CleanupManual`

Ribbon: {menuselection}`MeshCleanup --> ManualCheck --> Tri`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`nElemType`**
: A _N_ELEM_TYPE_ specifying the element type. The default value is 0.

**`veQuality`**
: A _VE_QUALITY_ specifying the quality. The default value is 0.

**`nCheckCondition`**
: A _N_CHECK_CONDITION_ specifying the check condition. The default value is 0.

**`dLimitValue`**
: A _Double_ specifying the limit value. The default value is 0.0.

**`CFLValue`**
: A _CFLVALUE_ specifying the l value. The default value is 0.0.

**`nNonManifold`**
: A _N_NON_MANIFOLD_ specifying the non manifold. The default value is 0.

**`nCleanupMode`**
: A _N_CLEANUP_MODE_ specifying the cleanup mode. The default value is 0.

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.ManualCheck.Tri(crlPart=[], nElemType=0, veQuality=0, nCheckCondition=0, dLimitValue=0.0, CFLValue=0.0, nNonManifold=0, nCleanupMode=0, crlElem=[])
```
