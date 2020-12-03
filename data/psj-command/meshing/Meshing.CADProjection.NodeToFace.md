```{module} Meshing.CADProjection.NodeToFace()
:synopsis: CadProject for Node to Face
```

(Meshing.CADProjection.NodeToFace)=

# Meshing.CADProjection.NodeToFace

## Description

CadProject for Node to Face

## Syntax

```python
Meshing.CADProjection.NodeToFace(iMethod=4, crlCadFace=[], crlMeshedNode=[], iDirection=0, iImproveQuality=0)
```

Macro: {ref}`Macro-Meshing-CadProject_NodeToFace`

Ribbon: {menuselection}`Meshing --> CADProjection --> NodeToFace`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 4.

**`crlCadFace`**
: A _Cursor List_ specifying the CAD face. The default value is [].

**`crlMeshedNode`**
: A _Cursor List_ specifying the meshed node. The default value is [].

**`iDirection`**
: An _Integer_ specifying the direction. The default value is 0.

**`iImproveQuality`**
: An _Integer_ specifying the improve quality. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.CADProjection.NodeToFace(iMethod=4, crlCadFace=[], crlMeshedNode=[], iDirection=0, iImproveQuality=0)
```
