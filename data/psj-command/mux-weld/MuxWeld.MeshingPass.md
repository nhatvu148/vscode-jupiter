```{module} MuxWeld.MeshingPass()
:synopsis: sweep cross section to create welding
```

(MuxWeld.MeshingPass)=

# MuxWeld.MeshingPass

## Description

sweep cross section to create welding

## Syntax

```python
MuxWeld.MeshingPass(crPart=None, crlEdge=[], dMeshSize=0.0)
```

Macro: {ref}`Macro-MuxWeld-WeldHexSweepBodyCr`

Ribbon: {menuselection}`MuxWeld --> MeshingPass`

## Inputs

**`crPart`**
: A _Cursor_ specifying the part. The default value is None.

**`crlEdge`**
: A _Cursor List_ specifying the edge. The default value is [].

**`dMeshSize`**
: A _Double_ specifying the mesh size. The default value is 0.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MuxWeld.MeshingPass(crPart=None, crlEdge=[], dMeshSize=0.0)
```
