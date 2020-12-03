```{module} Meshing.BarMeshing()
:synopsis: meshing 1D edge/bar
```

(Meshing.BarMeshing)=

# Meshing.BarMeshing

## Description

meshing 1D edge/bar

## Syntax

```python
Meshing.BarMeshing(crlCadEdge, crlBarEdge, crlBarPart, dDocMeshSize=0, iDocNumofElem=4)
```

Macro: {ref}`Macro-Meshing-BeamMeshing`

Ribbon: {menuselection}`Meshing --> BarMeshing`

## Inputs

**`crlCadEdge`**
: A _Cursor List_ specifying the CAD edge. This is a required input.

**`crlBarEdge`**
: A _Cursor List_ specifying the bar edge. This is a required input.

**`crlBarPart`**
: A _Cursor List_ specifying the bar part. This is a required input.

**`dDocMeshSize`**
: A _Double_ specifying the doc mesh size. The default value is 0.

**`iDocNumofElem`**
: An _Integer_ specifying the doc number of element. The default value is 4.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.BarMeshing(crlCadEdge, crlBarEdge, crlBarPart, dDocMeshSize=0, iDocNumofElem=4)
```
