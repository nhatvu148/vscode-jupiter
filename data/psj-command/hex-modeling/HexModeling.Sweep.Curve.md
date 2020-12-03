```{module} HexModeling.Sweep.Curve()
:synopsis: Unknown Description
```

(HexModeling.Sweep.Curve)=

# HexModeling.Sweep.Curve

## Description

Unknown Description

## Syntax

```python
HexModeling.Sweep.Curve(crFace=None, crlEdge=[], crlRefEdge=[], dMeshSize=0.1)
```

Macro: {ref}`Macro-HexModeling-SweepCloseLoopShape`

Ribbon: {menuselection}`HexModeling --> Sweep --> Curve`

## Inputs

**`crFace`**
: A _Cursor_ specifying the face. The default value is None.

**`crlEdge`**
: A _Cursor List_ specifying the edge. The default value is [].

**`crlRefEdge`**
: A _Cursor List_ specifying the reference edge. The default value is [].

**`dMeshSize`**
: A _Double_ specifying the mesh size. The default value is 0.1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
HexModeling.Sweep.Curve(crFace=None, crlEdge=[], crlRefEdge=[], dMeshSize=0.1)
```
