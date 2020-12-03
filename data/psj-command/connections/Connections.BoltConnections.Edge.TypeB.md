```{module} Connections.BoltConnections.Edge.TypeB()
:synopsis:
```

(Connections.BoltConnections.Edge.TypeB)=

# Connections.BoltConnections.Edge.TypeB

## Description

## Syntax

```python
Connections.BoltConnections.Edge.TypeB(crlEdgeCur1, crlEdgeCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, dRBE2=0.0, dBotDtDia=0.0, dPitch=10.0, iBotRbeConnType=0, bIfCreate2ADVCStaticProcessForBoltFixLength=False)
```

Macro: {ref}`Macro-Connections-Lbc_Bolt_Modeling_Type_B_Edge`

Ribbon: {menuselection}`Connections --> BoltConnections --> Edge --> TypeB`

## Inputs

**`crlEdgeCur1`**
: A _Cursor List_ specifying the edge cur1. This is a required input.

**`crlEdgeCur2`**
: A _Cursor List_ specifying the edge cur2. This is a required input.

**`strRbeName`**
: A _String_ specifying the rbe name. The default value is "RBE".

**`strBarName`**
: A _String_ specifying the bar name. The default value is "".

**`iShaftType`**
: An _Integer_ specifying the shaft type. The default value is 0.

**`crCurBarProperty`**
: A _Cursor_ specifying the cur bar property. The default value is None.

**`dPlaneTol`**
: A _Double_ specifying the plane tolerance. The default value is 20.0.

**`dMaxBoltHeight`**
: A _Double_ specifying the maximum bolt height. The default value is 100.0.

**`bPretensionLoad`**
: A _Boolean_ specifying the pretension load. The default value is False.

**`iSolverType`**
: An _Integer_ specifying the solver type. The default value is 0.

**`dForceValue`**
: A _Double_ specifying the force value. The default value is 0.0.

**`iPreTenDof`**
: An _Integer_ specifying the pre ten dof. The default value is 0.

**`crCurCoord`**
: A _Cursor_ specifying the cur coordinate. The default value is None.

**`iBoltFixLength`**
: An _Integer_ specifying the bolt fix length. The default value is 0.

**`iTopSlot`**
: An _Integer_ specifying the top slot. The default value is 0.

**`dRBE1`**
: A _Double_ specifying the r e1. The default value is 0.0.

**`dRBE2`**
: A _Double_ specifying the r e2. The default value is 0.0.

**`dBotDtDia`**
: A _Double_ specifying the bot data dia. The default value is 0.0.

**`dPitch`**
: A _Double_ specifying the pitch. The default value is 10.0.

**`iBotRbeConnType`**
: An _Integer_ specifying the bot rbe conn type. The default value is 0.

**`bIfCreate2ADVCStaticProcessForBoltFixLength`**
: A _Boolean_ specifying the if create2 ADVC static process for bolt fix length. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.BoltConnections.Edge.TypeB(crlEdgeCur1, crlEdgeCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, dRBE2=0.0, dBotDtDia=0.0, dPitch=10.0, iBotRbeConnType=0, bIfCreate2ADVCStaticProcessForBoltFixLength=False)
```
