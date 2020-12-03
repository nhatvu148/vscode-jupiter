```{module} Meshing.CADProjection.NodeToEdge()
:synopsis: CadProject for Node to Edge
```

(Meshing.CADProjection.NodeToEdge)=

# Meshing.CADProjection.NodeToEdge

## Description

CadProject for Node to Edge

## Syntax

```python
Meshing.CADProjection.NodeToEdge(iMethod=5, crCadEdge=None, crlMeshedNode=[], iDirection=0)
```

Macro: {ref}`Macro-Meshing-CadProject_NodeToEdge`

Ribbon: {menuselection}`Meshing --> CADProjection --> NodeToEdge`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 5.

**`crCadEdge`**
: A _Cursor_ specifying the CAD edge. The default value is None.

**`crlMeshedNode`**
: A _Cursor List_ specifying the meshed node. The default value is [].

**`iDirection`**
: An _Integer_ specifying the direction. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.CADProjection.NodeToEdge(iMethod=5, crCadEdge=None, crlMeshedNode=[], iDirection=0)
```
