```{module} BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus()
:synopsis: Create load boundary condition of initial angular velocity for abaqus
```

(BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus)=

# BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus

## Description

Create load boundary condition of initial angular velocity for abaqus

## Syntax

```python
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus(strName="InitialAngularVelocityAbaqus1", dVelocity=DFLT_DBL, strFirstCoord="", strSecondCoord="", crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-InitialAngularVelAbaqus`

Ribbon: {menuselection}`BoundaryConditions --> InitialNodalValue --> InitialAngularVelocity --> Abaqus`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "InitialAngularVelocityAbaqus1".

**`dVelocity`**
: A _Double_ specifying the velocity. The default value is DFLT_DBL.

**`strFirstCoord`**
: A _String_ specifying the first coordinate. The default value is "".

**`strSecondCoord`**
: A _String_ specifying the second coordinate. The default value is "".

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus(strName="InitialAngularVelocityAbaqus1", dVelocity=DFLT_DBL, strFirstCoord="", strSecondCoord="", crlTarget=[], crEdit=None)
```
