```{module} Connections.BoltConnections.Edge.TypeD()
:synopsis: create bolt connection typeD
```

(Connections.BoltConnections.Edge.TypeD)=

# Connections.BoltConnections.Edge.TypeD

## Description

create bolt connection typeD

## Syntax

```python
Connections.BoltConnections.Edge.TypeD(crlEdgeCur1, crlEdgeCur2, strMpcName="MPC", dConnRadius=0.0, dPlaneTol=20.0)
```

Macro: {ref}`Macro-Connections-Lbc_Bolt_Modeling_Type_D`

Ribbon: {menuselection}`Connections --> BoltConnections --> Edge --> TypeD`

## Inputs

**`crlEdgeCur1`**
: A _Cursor List_ specifying the edge cur1. This is a required input.

**`crlEdgeCur2`**
: A _Cursor List_ specifying the edge cur2. This is a required input.

**`strMpcName`**
: A _String_ specifying the mpc name. The default value is "MPC".

**`dConnRadius`**
: A _Double_ specifying the conn radius. The default value is 0.0.

**`dPlaneTol`**
: A _Double_ specifying the plane tolerance. The default value is 20.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.BoltConnections.Edge.TypeD(crlEdgeCur1, crlEdgeCur2, strMpcName="MPC", dConnRadius=0.0, dPlaneTol=20.0)
```
