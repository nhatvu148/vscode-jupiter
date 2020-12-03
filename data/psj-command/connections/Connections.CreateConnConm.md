```{module} Connections.CreateConnConm()
:synopsis:
```

(Connections.CreateConnConm)=

# Connections.CreateConnConm

## Description

## Syntax

```python
Connections.CreateConnConm(strName, iEType, iMethod, iCoordSys, iConmId, crMatCoord, dMass, dlX=[0, 0, 0], dlVintertia0=[0, 0, 0], dlVintertia1=[0, 0, 0])
```

Macro: {ref}`Macro-Connections-CreateConnConm`

Ribbon: {menuselection}`Connections --> CreateConnConm`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`iEType`**
: An _Integer_ specifying the e type. This is a required input.

**`iMethod`**
: An _Integer_ specifying the method. This is a required input.

**`iCoordSys`**
: An _Integer_ specifying the coordinate system. This is a required input.

**`iConmId`**
: An _Integer_ specifying the conm ID. This is a required input.

**`crMatCoord`**
: A _Cursor_ specifying the material coordinate. This is a required input.

**`dMass`**
: A _Double_ specifying the mass. This is a required input.

**`dlX`**
: A _Double List_ specifying the x. The default value is [0, 0, 0].

**`dlVintertia0`**
: A _Double List_ specifying the vintertia0. The default value is [0, 0, 0].

**`dlVintertia1`**
: A _Double List_ specifying the vintertia1. The default value is [0, 0, 0].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.CreateConnConm(strName, iEType, iMethod, iCoordSys, iConmId, crMatCoord, dMass, dlX=[0, 0, 0], dlVintertia0=[0, 0, 0], dlVintertia1=[0, 0, 0])
```
