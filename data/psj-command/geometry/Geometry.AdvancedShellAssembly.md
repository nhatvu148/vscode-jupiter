```{module} Geometry.AdvancedShellAssembly()
:synopsis: Test shell assembly
```

(Geometry.AdvancedShellAssembly)=

# Geometry.AdvancedShellAssembly

## Description

Test shell assembly

## Syntax

```python
Geometry.AdvancedShellAssembly(crlPart=[], crlFace=[], iMeshType=0, bSelfIntersection=False, iMethod=3, dGapTol=2.1)
```

Macro: {ref}`Macro-Geometry-ShellAssyGeneral`

Ribbon: {menuselection}`Geometry --> AdvancedShellAssembly`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`iMeshType`**
: An _Integer_ specifying the mesh type. The default value is 0.

**`bSelfIntersection`**
: A _Boolean_ specifying the self intersection. The default value is False.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 3.

**`dGapTol`**
: A _Double_ specifying the gap tolerance. The default value is 2.1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.AdvancedShellAssembly(crlPart=[], crlFace=[], iMeshType=0, bSelfIntersection=False, iMethod=3, dGapTol=2.1)
```
