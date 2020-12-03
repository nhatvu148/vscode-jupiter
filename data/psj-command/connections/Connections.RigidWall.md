```{module} Connections.RigidWall()
:synopsis:
```

(Connections.RigidWall)=

# Connections.RigidWall

## Description

## Syntax

```python
Connections.RigidWall(strName="RigidWall1", iObject=0, iType=0, iMotion=0, iFriction=0, iOrtho=0, iForces=0, dFinite1=DFLT_DBL, dFinite2=DFLT_DBL, dMotionMass=DFLT_DBL, dMotionInitVelo=DFLT_DBL, dFricCoulombCoeff=DFLT_DBL, dFricWeldVelo=DFLT_DBL, iForcesCirclesNum=0, dOrthoStaticCoeff1=DFLT_DBL, dOrthoStaticCoeff2=DFLT_DBL, dOrthoDynamicCoeff1=DFLT_DBL, dOrthoDynamicCoeff2=DFLT_DBL, dOrthoDecayConst1=DFLT_DBL, dOrthoDecayConst2=DFLT_DBL, dOrthoFricVector1=DFLT_DBL, dOrthoFricVector2=DFLT_DBL, dOrthoFricVector3=DFLT_DBL, bAllNodeSlave=False, crCoord=None, crAreaFaceSet=None, crVisualNodeSet=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-Connections-LBCRigdWall`

Ribbon: {menuselection}`Connections --> RigidWall`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "RigidWall1".

**`iObject`**
: An _Integer_ specifying the object. The default value is 0.

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`iMotion`**
: An _Integer_ specifying the motion. The default value is 0.

**`iFriction`**
: An _Integer_ specifying the friction. The default value is 0.

**`iOrtho`**
: An _Integer_ specifying the ortho. The default value is 0.

**`iForces`**
: An _Integer_ specifying the forces. The default value is 0.

**`dFinite1`**
: A _Double_ specifying the finite1. The default value is DFLT_DBL.

**`dFinite2`**
: A _Double_ specifying the finite2. The default value is DFLT_DBL.

**`dMotionMass`**
: A _Double_ specifying the motion mass. The default value is DFLT_DBL.

**`dMotionInitVelo`**
: A _Double_ specifying the motion initial velo. The default value is DFLT_DBL.

**`dFricCoulombCoeff`**
: A _Double_ specifying the fric coulomb coeff. The default value is DFLT_DBL.

**`dFricWeldVelo`**
: A _Double_ specifying the fric weld velo. The default value is DFLT_DBL.

**`iForcesCirclesNum`**
: An _Integer_ specifying the forces circles number. The default value is 0.

**`dOrthoStaticCoeff1`**
: A _Double_ specifying the ortho static coefficient 1. The default value is DFLT_DBL.

**`dOrthoStaticCoeff2`**
: A _Double_ specifying the ortho static coefficient 2. The default value is DFLT_DBL.

**`dOrthoDynamicCoeff1`**
: A _Double_ specifying the ortho dynamic coefficient 1. The default value is DFLT_DBL.

**`dOrthoDynamicCoeff2`**
: A _Double_ specifying the ortho dynamic coefficient 2. The default value is DFLT_DBL.

**`dOrthoDecayConst1`**
: A _Double_ specifying the ortho decay const1. The default value is DFLT_DBL.

**`dOrthoDecayConst2`**
: A _Double_ specifying the ortho decay const2. The default value is DFLT_DBL.

**`dOrthoFricVector1`**
: A _Double_ specifying the ortho fric vector1. The default value is DFLT_DBL.

**`dOrthoFricVector2`**
: A _Double_ specifying the ortho fric vector2. The default value is DFLT_DBL.

**`dOrthoFricVector3`**
: A _Double_ specifying the ortho fric vector3. The default value is DFLT_DBL.

**`bAllNodeSlave`**
: A _Boolean_ specifying the all node slave. The default value is False.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`crAreaFaceSet`**
: A _Cursor_ specifying the area face set. The default value is None.

**`crVisualNodeSet`**
: A _Cursor_ specifying the visual node set. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.RigidWall(strName="RigidWall1", iObject=0, iType=0, iMotion=0, iFriction=0, iOrtho=0, iForces=0, dFinite1=DFLT_DBL, dFinite2=DFLT_DBL, dMotionMass=DFLT_DBL, dMotionInitVelo=DFLT_DBL, dFricCoulombCoeff=DFLT_DBL, dFricWeldVelo=DFLT_DBL, iForcesCirclesNum=0, dOrthoStaticCoeff1=DFLT_DBL, dOrthoStaticCoeff2=DFLT_DBL, dOrthoDynamicCoeff1=DFLT_DBL, dOrthoDynamicCoeff2=DFLT_DBL, dOrthoDecayConst1=DFLT_DBL, dOrthoDecayConst2=DFLT_DBL, dOrthoFricVector1=DFLT_DBL, dOrthoFricVector2=DFLT_DBL, dOrthoFricVector3=DFLT_DBL, bAllNodeSlave=False, crCoord=None, crAreaFaceSet=None, crVisualNodeSet=None, crlTarget=[], crEdit=None)
```
