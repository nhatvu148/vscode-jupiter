```{module} MeshCleanup.Manual2D.Equivalence()
:synopsis: Equivalence Nodes
```

(MeshCleanup.Manual2D.Equivalence)=

# MeshCleanup.Manual2D.Equivalence

## Description

Equivalence Nodes

## Syntax

```python
MeshCleanup.Manual2D.Equivalence(crlNode, iTypeEquiva=0, dTolerance=1.0)
```

Macro: {ref}`Macro-MeshCleanup-Equivalence`

Ribbon: {menuselection}`MeshCleanup --> Manual2D --> Equivalence`

## Inputs

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

**`iTypeEquiva`**
: An _Integer_ specifying the type equiva. The default value is 0.

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 1.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshCleanup.Manual2D.Equivalence(crlNode, iTypeEquiva=0, dTolerance=1.0)
```
