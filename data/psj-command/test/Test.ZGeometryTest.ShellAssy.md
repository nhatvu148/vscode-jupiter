```{module} Test.ZGeometryTest.ShellAssy()
:synopsis: Unknown Description
```

(Test.ZGeometryTest.ShellAssy)=

# Test.ZGeometryTest.ShellAssy

## Description

Unknown Description

## Syntax

```python
Test.ZGeometryTest.ShellAssy(taPart=[], crlFace=[], _iMeshType=0, _bSelfIntersection=False, _iMethod=3, _dGapTol=2.1)
```

Macro: {ref}`Macro-Test-ShellAssyGeneral`

Ribbon: {menuselection}`Test --> ZGeometryTest --> ShellAssy`

## Inputs

**`taPart`**
: A _TA_PART_ specifying the part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`_iMeshType`**
: A \__I_MESH_TYPE_ specifying the mesh type. The default value is 0.

**`_bSelfIntersection`**
: A \__B_SELF_INTERSECTION_ specifying the self intersection. The default value is False.

**`_iMethod`**
: A \__I_METHOD_ specifying the method. The default value is 3.

**`_dGapTol`**
: A \__D_GAP_TOL_ specifying the gap tolerance. The default value is 2.1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Test.ZGeometryTest.ShellAssy(taPart=[], crlFace=[], _iMeshType=0, _bSelfIntersection=False, _iMethod=3, _dGapTol=2.1)
```
