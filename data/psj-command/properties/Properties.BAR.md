```{module} Properties.BAR()
:synopsis: create 1D bar property
```

(Properties.BAR)=

# Properties.BAR

## Description

create 1D bar property

## Syntax

```python
Properties.BAR(strName="", iId=1, crSection=None, iShapeDataType=0, crDatacrMat=None, dDatadArea=DFLT_DBL, dlDataOrient=[0, 0, 0], dlDataInertia=[0, 0, 0], dDatadTorConst=DFLT_DBL, dDatadNSM=DFLT_DBL, dDataShearAreaFactor0=DFLT_DBL, dDataShearAreaFactor1=DFLT_DBL, dDataStressRecoveryCoeff0=DFLT_DBL, dDataStressRecoveryCoeff1=DFLT_DBL, dDataStressRecoveryCoeff2=DFLT_DBL, dDataStressRecoveryCoeff3=DFLT_DBL, dDataStressRecoveryCoeff4=DFLT_DBL, dDataStressRecoveryCoeff5=DFLT_DBL, dDataStressRecoveryCoeff6=DFLT_DBL, dDataStressRecoveryCoeff7=DFLT_DBL, bDataPinA0=False, bDataPinA1=False, bDataPinA2=False, bDataPinA3=False, bDataPinA4=False, bDataPinA5=False, bDataPinB0=False, bDataPinB1=False, bDataPinB2=False, bDataPinB3=False, bDataPinB4=False, bDataPinB5=False, dlDataOffset0=[DFLT_DBL, DFLT_DBL, DFLT_DBL], dlDataOffset1=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iLocalLengthUnit=0, iLocalMassUnit=0, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-Properties-Property1DBar`

Ribbon: {menuselection}`Properties --> BAR`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iId`**
: An _Integer_ specifying the ID. The default value is 1.

**`crSection`**
: A _Cursor_ specifying the section. The default value is None.

**`iShapeDataType`**
: An _Integer_ specifying the shape data type. The default value is 0.

**`crDatacrMat`**
: A _Cursor_ specifying the datacr material. The default value is None.

**`dDatadArea`**
: A _Double_ specifying the datad area. The default value is DFLT_DBL.

**`dlDataOrient`**
: A _Double List_ specifying the data orient. The default value is [0, 0, 0].

**`dlDataInertia`**
: A _Double List_ specifying the data inertia. The default value is [0, 0, 0].

**`dDatadTorConst`**
: A _Double_ specifying the datad tor const. The default value is DFLT_DBL.

**`dDatadNSM`**
: A _Double_ specifying the datad n s m. The default value is DFLT_DBL.

**`dDataShearAreaFactor0`**
: A _Double_ specifying the data shear area factor0. The default value is DFLT_DBL.

**`dDataShearAreaFactor1`**
: A _Double_ specifying the data shear area factor1. The default value is DFLT_DBL.

**`dDataStressRecoveryCoeff0`**
: A _Double_ specifying the data stress recovery coefficient 0. The default value is DFLT_DBL.

**`dDataStressRecoveryCoeff1`**
: A _Double_ specifying the data stress recovery coefficient 1. The default value is DFLT_DBL.

**`dDataStressRecoveryCoeff2`**
: A _Double_ specifying the data stress recovery coefficient 2. The default value is DFLT_DBL.

**`dDataStressRecoveryCoeff3`**
: A _Double_ specifying the data stress recovery coefficient 3. The default value is DFLT_DBL.

**`dDataStressRecoveryCoeff4`**
: A _Double_ specifying the data stress recovery coefficient 4. The default value is DFLT_DBL.

**`dDataStressRecoveryCoeff5`**
: A _Double_ specifying the data stress recovery coefficient 5. The default value is DFLT_DBL.

**`dDataStressRecoveryCoeff6`**
: A _Double_ specifying the data stress recovery coefficient 6. The default value is DFLT_DBL.

**`dDataStressRecoveryCoeff7`**
: A _Double_ specifying the data stress recovery coefficient 7. The default value is DFLT_DBL.

**`bDataPinA0`**
: A _Boolean_ specifying the data pin a0. The default value is False.

**`bDataPinA1`**
: A _Boolean_ specifying the data pin a1. The default value is False.

**`bDataPinA2`**
: A _Boolean_ specifying the data pin a2. The default value is False.

**`bDataPinA3`**
: A _Boolean_ specifying the data pin a3. The default value is False.

**`bDataPinA4`**
: A _Boolean_ specifying the data pin a4. The default value is False.

**`bDataPinA5`**
: A _Boolean_ specifying the data pin a5. The default value is False.

**`bDataPinB0`**
: A _Boolean_ specifying the data pin b0. The default value is False.

**`bDataPinB1`**
: A _Boolean_ specifying the data pin b1. The default value is False.

**`bDataPinB2`**
: A _Boolean_ specifying the data pin b2. The default value is False.

**`bDataPinB3`**
: A _Boolean_ specifying the data pin b3. The default value is False.

**`bDataPinB4`**
: A _Boolean_ specifying the data pin b4. The default value is False.

**`bDataPinB5`**
: A _Boolean_ specifying the data pin b5. The default value is False.

**`dlDataOffset0`**
: A _Double List_ specifying the data offset0. The default value is [DFLT_DBL, DFLT_DBL, DFLT_DBL].

**`dlDataOffset1`**
: A _Double List_ specifying the data offset1. The default value is [DFLT_DBL, DFLT_DBL, DFLT_DBL].

**`iLocalLengthUnit`**
: An _Integer_ specifying the local length unit. The default value is 0.

**`iLocalMassUnit`**
: An _Integer_ specifying the local mass unit. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Properties.BAR(strName="", iId=1, crSection=None, iShapeDataType=0, crDatacrMat=None, dDatadArea=DFLT_DBL, dlDataOrient=[0, 0, 0], dlDataInertia=[0, 0, 0], dDatadTorConst=DFLT_DBL, dDatadNSM=DFLT_DBL, dDataShearAreaFactor0=DFLT_DBL, dDataShearAreaFactor1=DFLT_DBL, dDataStressRecoveryCoeff0=DFLT_DBL, dDataStressRecoveryCoeff1=DFLT_DBL, dDataStressRecoveryCoeff2=DFLT_DBL, dDataStressRecoveryCoeff3=DFLT_DBL, dDataStressRecoveryCoeff4=DFLT_DBL, dDataStressRecoveryCoeff5=DFLT_DBL, dDataStressRecoveryCoeff6=DFLT_DBL, dDataStressRecoveryCoeff7=DFLT_DBL, bDataPinA0=False, bDataPinA1=False, bDataPinA2=False, bDataPinA3=False, bDataPinA4=False, bDataPinA5=False, bDataPinB0=False, bDataPinB1=False, bDataPinB2=False, bDataPinB3=False, bDataPinB4=False, bDataPinB5=False, dlDataOffset0=[DFLT_DBL, DFLT_DBL, DFLT_DBL], dlDataOffset1=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iLocalLengthUnit=0, iLocalMassUnit=0, crlTarget=[], crEdit=None)
```
