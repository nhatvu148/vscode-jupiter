```{module} Connections.BoltConnections.Face.TypeA()
:synopsis:
```

(Connections.BoltConnections.Face.TypeA)=

# Connections.BoltConnections.Face.TypeA

## Description

## Syntax

```python
Connections.BoltConnections.Face.TypeA(crlFaceCur1, crlFaceCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, dMaxDiameter=0.0, dMinDiameter=0.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, iBotSlot=0, dRBE2=0.0, dScale1=1.10, bIfCreate2ADVCStaticProcessForBoltFixLength=False)
```

Macro: {ref}`Macro-Connections-Lbc_Bolt_Modeling_Type_A_Face`

Ribbon: {menuselection}`Connections --> BoltConnections --> Face --> TypeA`

## Inputs

**`crlFaceCur1`**
: A _Cursor List_ specifying the face cur1. This is a required input.

**`crlFaceCur2`**
: A _Cursor List_ specifying the face cur2. This is a required input.

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

**`dMaxDiameter`**
: A _Double_ specifying the maximum diameter. The default value is 0.0.

**`dMinDiameter`**
: A _Double_ specifying the minimum diameter. The default value is 0.0.

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

**`iBotSlot`**
: An _Integer_ specifying the bot slot. The default value is 0.

**`dRBE2`**
: A _Double_ specifying the r e2. The default value is 0.0.

**`dScale1`**
: A _Double_ specifying the scale1. The default value is 1.10.

**`bIfCreate2ADVCStaticProcessForBoltFixLength`**
: A _Boolean_ specifying the if create2 ADVC static process for bolt fix length. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.BoltConnections.Face.TypeA(crlFaceCur1, crlFaceCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, dMaxDiameter=0.0, dMinDiameter=0.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, iBotSlot=0, dRBE2=0.0, dScale1=1.10, bIfCreate2ADVCStaticProcessForBoltFixLength=False)
```
