```{module} Connections.Contacts.Abaqus.ContactShareFace()
:synopsis: Create LBC contact abaqus manual group
```

(Connections.Contacts.Abaqus.ContactShareFace)=

# Connections.Contacts.Abaqus.ContactShareFace

## Description

Create LBC contact abaqus manual group

## Syntax

```python
Connections.Contacts.Abaqus.ContactShareFace(strName="", iContactMethod=3, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)
```

Macro: {ref}`Macro-Connections-ContactAbaqus_ShareFace`

Ribbon: {menuselection}`Connections --> Contacts --> Abaqus --> ContactShareFace`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iContactMethod`**
: An _Integer_ specifying the contact method. The default value is 3.

**`iContactType`**
: An _Integer_ specifying the contact type. The default value is 0.

**`iAlg`**
: An _Integer_ specifying the algorithm. The default value is 0.

**`dAdjustVal`**
: A _Double_ specifying the adjust value. The default value is 0.0.

**`dExtensionZone`**
: A _Double_ specifying the extension zone. The default value is 0.0.

**`dMaxPenetration`**
: A _Double_ specifying the maximum penetration. The default value is 0.0.

**`iSmallSliding`**
: An _Integer_ specifying the small sliding. The default value is 0.

**`dSmooth`**
: A _Double_ specifying the smooth. The default value is 0.0.

**`iFrictionType`**
: An _Integer_ specifying the friction type. The default value is 0.

**`dFrictionCoef1`**
: A _Double_ specifying the friction coefficient 1. The default value is 0.0.

**`dFrictionCoef2`**
: A _Double_ specifying the friction coefficient 2. The default value is 0.0.

**`dShearLimit`**
: A _Double_ specifying the shear limit. The default value is 0.0.

**`dSlipTol`**
: A _Double_ specifying the slip tolerance. The default value is 0.0.

**`dStaticFrictionCoef`**
: A _Double_ specifying the static friction coefficient . The default value is 0.0.

**`dKineticFrictionCoef`**
: A _Double_ specifying the kinetic friction coefficient . The default value is 0.0.

**`dDecayCoef`**
: A _Double_ specifying the decay coefficient . The default value is 0.0.

**`iAdjust`**
: An _Integer_ specifying the adjust. The default value is 0.

**`dPositonTol`**
: A _Double_ specifying the positon tolerance. The default value is 0.0.

**`iFormula`**
: An _Integer_ specifying the formula. The default value is 0.

**`iTie`**
: An _Integer_ specifying the tie. The default value is 0.

**`iPOCType`**
: An _Integer_ specifying the POC type. The default value is 0.

**`iAllowSeparation`**
: An _Integer_ specifying the allow separation. The default value is 0.

**`dSlope`**
: A _Double_ specifying the slope. The default value is 0.0.

**`tshPOCTsheet`**
: A _Table Sheet_ specifying the POC table sheet. The default value is [].

**`iClearanceType`**
: An _Integer_ specifying the clearance type. The default value is 0.

**`iClearanceTypeId`**
: An _Integer_ specifying the clearance type ID. The default value is 0.

**`bTemperatureDependency`**
: A _Boolean_ specifying the temperature dependency. The default value is False.

**`iDependencies`**
: An _Integer_ specifying the dependencies. The default value is 0.

**`tshCDTsheet`**
: A _Table Sheet_ specifying the CD table sheet. The default value is [].

**`iPrsTypeId`**
: An _Integer_ specifying the pressure type ID. The default value is 0.

**`bPrsTemperatureDependency`**
: A _Boolean_ specifying the pressure temperature dependency. The default value is False.

**`iPrsDependencies`**
: An _Integer_ specifying the pressure dependencies. The default value is 0.

**`tshPrsDTsheet`**
: A _Table Sheet_ specifying the pressure d table sheet. The default value is [].

**`crplTarget`**
: A _Cursor Pair List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`iColor`**
: An _Integer_ specifying the color. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.Abaqus.ContactShareFace(strName="", iContactMethod=3, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)
```
