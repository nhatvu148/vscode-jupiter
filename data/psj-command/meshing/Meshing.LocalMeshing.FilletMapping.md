```{module} Meshing.LocalMeshing.FilletMapping()
:synopsis:
```

(Meshing.LocalMeshing.FilletMapping)=

# Meshing.LocalMeshing.FilletMapping

## Description

## Syntax

```python
Meshing.LocalMeshing.FilletMapping(crlFace=[], iIsoDiv=4, dIsoSize=5, dIsoError=0.5)
```

Macro: {ref}`Macro-Meshing-MeshingLocalMeshingFilletMapped`

Ribbon: {menuselection}`Meshing --> LocalMeshing --> FilletMapping`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`iIsoDiv`**
: An _Integer_ specifying the iso divide. The default value is 4.

**`dIsoSize`**
: A _Double_ specifying the iso size. The default value is 5.

**`dIsoError`**
: A _Double_ specifying the iso error. The default value is 0.5.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.LocalMeshing.FilletMapping(crlFace=[], iIsoDiv=4, dIsoSize=5, dIsoError=0.5)
```
