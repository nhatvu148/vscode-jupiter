```{module} Properties.Beam()
:synopsis: add property of 1D beam
```

(Properties.Beam)=

# Properties.Beam

## Description

add property of 1D beam

## Syntax

```python
Properties.Beam(strNewName="BEAM1", iPId=1, crSection=None, iShapeDataType=0, crMat=None, dArea=0.0, dlVecOrient=[0,0,0], dlVecInertia=[0,0,0], dTorConst=0.0, dNSM=DFLT_DBL, dNSMA=DFLT_DBL, dNSMB=DFLT_DBL, dNSMNode1=DFLT_DBL, dNSMNode2=DFLT_DBL, dNSMNode3=DFLT_DBL, dNSMNode4=DFLT_DBL, dShearStiffnessK1=0.0, dShearStiffnessK2=0.0, dShearAreaReliefS1=DFLT_DBL, dShearAreaReliefS2=DFLT_DBL, dWrapCoeff1=DFLT_DBL, dWrapCoeff2=DFLT_DBL, dNA1=DFLT_DBL, dNA2=DFLT_DBL, dNA3=DFLT_DBL, dNA4=DFLT_DBL, dStressRecoveryCoeffCy=0.0, dStressRecoveryCoeffCz=0.0, dStressRecoveryCoeffDy=0.0, dStressRecoveryCoeffDz=0.0, dStressRecoveryCoeffEy=0.0, dStressRecoveryCoeffEz=0.0, dStressRecoveryCoeffFy=0.0, dStressRecoveryCoeffFz=0.0, bPinA1=False, bPinA2=False, bPinA3=False, bPinA4=False, bPinA5=False, bPinA6=False, bPinB1=False, bPinB2=False, bPinB3=False, bPinB4=False, bPinB5=False, bPinB6=False, dlOffsetA=[DFLT_DBL,DFLT_DBL,DFLT_DBL], dlOffsetB=[DFLT_DBL,DFLT_DBL,DFLT_DBL], iLengthUnit=0, iMassUnit=0, crlTarget=[], crEdit=None, bTapped=False, dTapArea=DFLT_DBL, dlVecTapInertia=[DFLT_DBL,DFLT_DBL,DFLT_DBL], dTapTorConst=DFLT_DBL, dTapNSM=DFLT_DBL, dTapStressRecoveryCoeffCy=DFLT_DBL, dTapStressRecoveryCoeffCz=DFLT_DBL, dTapStressRecoveryCoeffDy=DFLT_DBL, dTapStressRecoveryCoeffDz=DFLT_DBL, dTapStressRecoveryCoeffEy=DFLT_DBL, dTapStressRecoveryCoeffEz=DFLT_DBL, dTapStressRecoveryCoeffFy=DFLT_DBL, dTapStressRecoveryCoeffFz=DFLT_DBL, iIntePtNum=DFLT_INT)
```

Macro: {ref}`Macro-Properties-Property1DBeamN`

Ribbon: {menuselection}`Properties --> Beam`

## Inputs

**`strNewName`**
: A _String_ specifying the new name. The default value is "BEAM1".

**`iPId`**
: An _Integer_ specifying the p ID. The default value is 1.

**`crSection`**
: A _Cursor_ specifying the section. The default value is None.

**`iShapeDataType`**
: An _Integer_ specifying the shape data type. The default value is 0.

**`crMat`**
: A _Cursor_ specifying the material. The default value is None.

**`dArea`**
: A _Double_ specifying the area. The default value is 0.0.

**`dlVecOrient`**
: A _Double List_ specifying the vector orient. The default value is [0,0,0].

**`dlVecInertia`**
: A _Double List_ specifying the vector inertia. The default value is [0,0,0].

**`dTorConst`**
: A _Double_ specifying the tor const. The default value is 0.0.

**`dNSM`**
: A _Double_ specifying the n s m. The default value is DFLT_DBL.

**`dNSMA`**
: A _Double_ specifying the n s m a. The default value is DFLT_DBL.

**`dNSMB`**
: A _Double_ specifying the n s m . The default value is DFLT_DBL.

**`dNSMNode1`**
: A _Double_ specifying the n s m node1. The default value is DFLT_DBL.

**`dNSMNode2`**
: A _Double_ specifying the n s m node2. The default value is DFLT_DBL.

**`dNSMNode3`**
: A _Double_ specifying the n s m node3. The default value is DFLT_DBL.

**`dNSMNode4`**
: A _Double_ specifying the n s m node4. The default value is DFLT_DBL.

**`dShearStiffnessK1`**
: A _Double_ specifying the shear stiffness k1. The default value is 0.0.

**`dShearStiffnessK2`**
: A _Double_ specifying the shear stiffness k2. The default value is 0.0.

**`dShearAreaReliefS1`**
: A _Double_ specifying the shear area relief s1. The default value is DFLT_DBL.

**`dShearAreaReliefS2`**
: A _Double_ specifying the shear area relief s2. The default value is DFLT_DBL.

**`dWrapCoeff1`**
: A _Double_ specifying the wrap coefficient 1. The default value is DFLT_DBL.

**`dWrapCoeff2`**
: A _Double_ specifying the wrap coefficient 2. The default value is DFLT_DBL.

**`dNA1`**
: A _Double_ specifying the n a1. The default value is DFLT_DBL.

**`dNA2`**
: A _Double_ specifying the n a2. The default value is DFLT_DBL.

**`dNA3`**
: A _Double_ specifying the n a3. The default value is DFLT_DBL.

**`dNA4`**
: A _Double_ specifying the n a4. The default value is DFLT_DBL.

**`dStressRecoveryCoeffCy`**
: A _Double_ specifying the stress recovery coeff cy. The default value is 0.0.

**`dStressRecoveryCoeffCz`**
: A _Double_ specifying the stress recovery coeff cz. The default value is 0.0.

**`dStressRecoveryCoeffDy`**
: A _Double_ specifying the stress recovery coeff dy. The default value is 0.0.

**`dStressRecoveryCoeffDz`**
: A _Double_ specifying the stress recovery coeff dz. The default value is 0.0.

**`dStressRecoveryCoeffEy`**
: A _Double_ specifying the stress recovery coeff ey. The default value is 0.0.

**`dStressRecoveryCoeffEz`**
: A _Double_ specifying the stress recovery coeff ez. The default value is 0.0.

**`dStressRecoveryCoeffFy`**
: A _Double_ specifying the stress recovery coeff fy. The default value is 0.0.

**`dStressRecoveryCoeffFz`**
: A _Double_ specifying the stress recovery coeff fz. The default value is 0.0.

**`bPinA1`**
: A _Boolean_ specifying the pin a1. The default value is False.

**`bPinA2`**
: A _Boolean_ specifying the pin a2. The default value is False.

**`bPinA3`**
: A _Boolean_ specifying the pin a3. The default value is False.

**`bPinA4`**
: A _Boolean_ specifying the pin a4. The default value is False.

**`bPinA5`**
: A _Boolean_ specifying the pin a5. The default value is False.

**`bPinA6`**
: A _Boolean_ specifying the pin a6. The default value is False.

**`bPinB1`**
: A _Boolean_ specifying the pin b1. The default value is False.

**`bPinB2`**
: A _Boolean_ specifying the pin b2. The default value is False.

**`bPinB3`**
: A _Boolean_ specifying the pin b3. The default value is False.

**`bPinB4`**
: A _Boolean_ specifying the pin b4. The default value is False.

**`bPinB5`**
: A _Boolean_ specifying the pin b5. The default value is False.

**`bPinB6`**
: A _Boolean_ specifying the pin b6. The default value is False.

**`dlOffsetA`**
: A _Double List_ specifying the offset a. The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

**`dlOffsetB`**
: A _Double List_ specifying the offset . The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

**`iLengthUnit`**
: An _Integer_ specifying the length unit. The default value is 0.

**`iMassUnit`**
: An _Integer_ specifying the mass unit. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`bTapped`**
: A _Boolean_ specifying the tapped. The default value is False.

**`dTapArea`**
: A _Double_ specifying the tapered area. The default value is DFLT_DBL.

**`dlVecTapInertia`**
: A _Double List_ specifying the vector tapered inertia. The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

**`dTapTorConst`**
: A _Double_ specifying the tapered tor const. The default value is DFLT_DBL.

**`dTapNSM`**
: A _Double_ specifying the tapered n s m. The default value is DFLT_DBL.

**`dTapStressRecoveryCoeffCy`**
: A _Double_ specifying the tapered stress recovery coeff cy. The default value is DFLT_DBL.

**`dTapStressRecoveryCoeffCz`**
: A _Double_ specifying the tapered stress recovery coeff cz. The default value is DFLT_DBL.

**`dTapStressRecoveryCoeffDy`**
: A _Double_ specifying the tapered stress recovery coeff dy. The default value is DFLT_DBL.

**`dTapStressRecoveryCoeffDz`**
: A _Double_ specifying the tapered stress recovery coeff dz. The default value is DFLT_DBL.

**`dTapStressRecoveryCoeffEy`**
: A _Double_ specifying the tapered stress recovery coeff ey. The default value is DFLT_DBL.

**`dTapStressRecoveryCoeffEz`**
: A _Double_ specifying the tapered stress recovery coeff ez. The default value is DFLT_DBL.

**`dTapStressRecoveryCoeffFy`**
: A _Double_ specifying the tapered stress recovery coeff fy. The default value is DFLT_DBL.

**`dTapStressRecoveryCoeffFz`**
: A _Double_ specifying the tapered stress recovery coeff fz. The default value is DFLT_DBL.

**`iIntePtNum`**
: An _Integer_ specifying the inte point number. The default value is DFLT_INT.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.Beam(strNewName="BEAM1", iPId=1, crSection=None, iShapeDataType=0, crMat=None, dArea=0.0, dlVecOrient=[0,0,0], dlVecInertia=[0,0,0], dTorConst=0.0, dNSM=DFLT_DBL, dNSMA=DFLT_DBL, dNSMB=DFLT_DBL, dNSMNode1=DFLT_DBL, dNSMNode2=DFLT_DBL, dNSMNode3=DFLT_DBL, dNSMNode4=DFLT_DBL, dShearStiffnessK1=0.0, dShearStiffnessK2=0.0, dShearAreaReliefS1=DFLT_DBL, dShearAreaReliefS2=DFLT_DBL, dWrapCoeff1=DFLT_DBL, dWrapCoeff2=DFLT_DBL, dNA1=DFLT_DBL, dNA2=DFLT_DBL, dNA3=DFLT_DBL, dNA4=DFLT_DBL, dStressRecoveryCoeffCy=0.0, dStressRecoveryCoeffCz=0.0, dStressRecoveryCoeffDy=0.0, dStressRecoveryCoeffDz=0.0, dStressRecoveryCoeffEy=0.0, dStressRecoveryCoeffEz=0.0, dStressRecoveryCoeffFy=0.0, dStressRecoveryCoeffFz=0.0, bPinA1=False, bPinA2=False, bPinA3=False, bPinA4=False, bPinA5=False, bPinA6=False, bPinB1=False, bPinB2=False, bPinB3=False, bPinB4=False, bPinB5=False, bPinB6=False, dlOffsetA=[DFLT_DBL,DFLT_DBL,DFLT_DBL], dlOffsetB=[DFLT_DBL,DFLT_DBL,DFLT_DBL], iLengthUnit=0, iMassUnit=0, crlTarget=[], crEdit=None, bTapped=False, dTapArea=DFLT_DBL, dlVecTapInertia=[DFLT_DBL,DFLT_DBL,DFLT_DBL], dTapTorConst=DFLT_DBL, dTapNSM=DFLT_DBL, dTapStressRecoveryCoeffCy=DFLT_DBL, dTapStressRecoveryCoeffCz=DFLT_DBL, dTapStressRecoveryCoeffDy=DFLT_DBL, dTapStressRecoveryCoeffDz=DFLT_DBL, dTapStressRecoveryCoeffEy=DFLT_DBL, dTapStressRecoveryCoeffEz=DFLT_DBL, dTapStressRecoveryCoeffFy=DFLT_DBL, dTapStressRecoveryCoeffFz=DFLT_DBL, iIntePtNum=DFLT_INT)
```
