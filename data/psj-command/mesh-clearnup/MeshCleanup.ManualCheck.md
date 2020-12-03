```{module} MeshCleanup.ManualCheck()
:synopsis: MeshCleanup ManualCheck
```

(MeshCleanup.ManualCheck)=

# MeshCleanup.ManualCheck

## Description

MeshCleanup ManualCheck

## Syntax

```python
MeshCleanup.ManualCheck(crlPart=[], iElemType=0, iVeQuality=0, iCheckCondition=0, dLimitValue=0.0, dCFLValue=0.0, iNonManifold=0, iCleanupMode=0, crlElem=[])
```

Macro: {ref}`Macro-MeshCleanup-CleanupManual`

Ribbon: {menuselection}`MeshCleanup --> ManualCheck`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`iElemType`**
: An _Integer_ specifying the element type. The default value is 0.

**`iVeQuality`**
: An _Integer_ specifying the ve quality. The default value is 0.

**`iCheckCondition`**
: An _Integer_ specifying the check condition. The default value is 0.

**`dLimitValue`**
: A _Double_ specifying the limit value. The default value is 0.0.

**`dCFLValue`**
: A _Double_ specifying the c l value. The default value is 0.0.

**`iNonManifold`**
: An _Integer_ specifying the non manifold. The default value is 0.

**`iCleanupMode`**
: An _Integer_ specifying the cleanup mode. The default value is 0.

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.ManualCheck(crlPart=[], iElemType=0, iVeQuality=0, iCheckCondition=0, dLimitValue=0.0, dCFLValue=0.0, iNonManifold=0, iCleanupMode=0, crlElem=[])
```
