```{module} Connections.SpringsDampers.Bush.AnyEntities()
:synopsis: Create bush connection
```

(Connections.SpringsDampers.Bush.AnyEntities)=

# Connections.SpringsDampers.Bush.AnyEntities

## Description

Create bush connection

## Syntax

```python
Connections.SpringsDampers.Bush.AnyEntities(iMethod=16, strName="BUSH_1", crlMaster=[], crlSlave=[], crCoord=None, dTol=DFLT_DBL, iGround=0, iOriMode=0, iEqual=1, poslVector=[], dlStiffness=[], dlDampCoef=[], dlDampConst=[], dRotStrain=DFLT_DBL, dTransStrain=DFLT_DBL, dRotStress=DFLT_DBL, dTransStress=DFLT_DBL, crEditObj=None)
```

Macro: {ref}`Macro-Connections-ConnBush_AnyEntity`

Ribbon: {menuselection}`Connections --> SpringsDampers --> Bush --> AnyEntities`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 16.

**`strName`**
: A _String_ specifying the name. The default value is "BUSH_1".

**`crlMaster`**
: A _Cursor List_ specifying the master. The default value is [].

**`crlSlave`**
: A _Cursor List_ specifying the slave. The default value is [].

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`dTol`**
: A _Double_ specifying the tolerance. The default value is DFLT_DBL.

**`iGround`**
: An _Integer_ specifying the ground. The default value is 0.

**`iOriMode`**
: An _Integer_ specifying the ori mode. The default value is 0.

**`iEqual`**
: An _Integer_ specifying the equal. The default value is 1.

**`poslVector`**
: A _Position List_ specifying the vector. The default value is [].

**`dlStiffness`**
: A _Double List_ specifying the stiffness. The default value is [].

**`dlDampCoef`**
: A _Double List_ specifying the damp coefficient . The default value is [].

**`dlDampConst`**
: A _Double List_ specifying the damp const. The default value is [].

**`dRotStrain`**
: A _Double_ specifying the rotation strain. The default value is DFLT_DBL.

**`dTransStrain`**
: A _Double_ specifying the trans strain. The default value is DFLT_DBL.

**`dRotStress`**
: A _Double_ specifying the rotation stress. The default value is DFLT_DBL.

**`dTransStress`**
: A _Double_ specifying the trans stress. The default value is DFLT_DBL.

**`crEditObj`**
: A _Cursor_ specifying the edit object. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.SpringsDampers.Bush.AnyEntities(iMethod=16, strName="BUSH_1", crlMaster=[], crlSlave=[], crCoord=None, dTol=DFLT_DBL, iGround=0, iOriMode=0, iEqual=1, poslVector=[], dlStiffness=[], dlDampCoef=[], dlDampConst=[], dRotStrain=DFLT_DBL, dTransStrain=DFLT_DBL, dRotStress=DFLT_DBL, dTransStress=DFLT_DBL, crEditObj=None)
```
