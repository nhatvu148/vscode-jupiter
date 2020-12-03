```{module} MufflerHA.CopyMeshCount()
:synopsis:
```

(MufflerHA.CopyMeshCount)=

# MufflerHA.CopyMeshCount

## Description

## Syntax

```python
MufflerHA.CopyMeshCount(crlMasterEdge, crlSlaveEdge, strBaseName)
```

Macro: {ref}`Macro-MufflerHA-LocalSettingEdgeNodeCountAuto`

Ribbon: {menuselection}`MufflerHA --> CopyMeshCount`

## Inputs

**`crlMasterEdge`**
: A _Cursor List_ specifying the master edge. This is a required input.

**`crlSlaveEdge`**
: A _Cursor List_ specifying the slave edge. This is a required input.

**`strBaseName`**
: A _String_ specifying the base name. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MufflerHA.CopyMeshCount(crlMasterEdge, crlSlaveEdge, strBaseName)
```
