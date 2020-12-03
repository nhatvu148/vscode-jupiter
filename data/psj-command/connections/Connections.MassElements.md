```{module} Connections.MassElements()
:synopsis: Connection new mass
```

(Connections.MassElements)=

# Connections.MassElements

## Description

Connection new mass

## Syntax

```python
Connections.MassElements(strName, crlTarget, dMass=0.01, iDof=1, bDesigner=True, crCoordinate=None, dOffset0=0.0, dOffset1=0.0, dOffset2=0.0, dInertia0=0.0, dInertia1=0.0, dInertia2=0.0, dInertia3=0.0, dInertia4=0.0, dInertia5=0.0, crEdit=None, bUpdateDispCS=True)
```

Macro: {ref}`Macro-Connections-ConnectionNewMass`

Ribbon: {menuselection}`Connections --> MassElements`

## Inputs

**`strName`**
: A _String_ specifying the name. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

**`dMass`**
: A _Double_ specifying the mass. The default value is 0.01.

**`iDof`**
: An _Integer_ specifying the dof. The default value is 1.

**`bDesigner`**
: A _Boolean_ specifying the designer. The default value is True.

**`crCoordinate`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`dOffset0`**
: A _Double_ specifying the offset0. The default value is 0.0.

**`dOffset1`**
: A _Double_ specifying the offset1. The default value is 0.0.

**`dOffset2`**
: A _Double_ specifying the offset2. The default value is 0.0.

**`dInertia0`**
: A _Double_ specifying the inertia0. The default value is 0.0.

**`dInertia1`**
: A _Double_ specifying the inertia1. The default value is 0.0.

**`dInertia2`**
: A _Double_ specifying the inertia2. The default value is 0.0.

**`dInertia3`**
: A _Double_ specifying the inertia3. The default value is 0.0.

**`dInertia4`**
: A _Double_ specifying the inertia4. The default value is 0.0.

**`dInertia5`**
: A _Double_ specifying the inertia5. The default value is 0.0.

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`bUpdateDispCS`**
: A _Boolean_ specifying the update displacement coordinate system. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.MassElements(strName, crlTarget, dMass=0.01, iDof=1, bDesigner=True, crCoordinate=None, dOffset0=0.0, dOffset1=0.0, dOffset2=0.0, dInertia0=0.0, dInertia1=0.0, dInertia2=0.0, dInertia3=0.0, dInertia4=0.0, dInertia5=0.0, crEdit=None, bUpdateDispCS=True)
```
