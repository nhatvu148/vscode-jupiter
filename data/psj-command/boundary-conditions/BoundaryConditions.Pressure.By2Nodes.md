```{module} BoundaryConditions.Pressure.By2Nodes()
:synopsis: Create load boundary condition of 2nodes pressure
```

(BoundaryConditions.Pressure.By2Nodes)=

# BoundaryConditions.Pressure.By2Nodes

## Description

Create load boundary condition of 2nodes pressure

## Syntax

```python
BoundaryConditions.Pressure.By2Nodes(strName="PressureLinear1", crNodeA=None, dPressureA=0.0, iNodeAUnit=0, crNodeB=None, dPressureB=0.0, iNodeBUnit=0, iDirection=0, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-Pressure2Nodes`

Ribbon: {menuselection}`BoundaryConditions --> Pressure --> By2Nodes`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "PressureLinear1".

**`crNodeA`**
: A _Cursor_ specifying the node a. The default value is None.

**`dPressureA`**
: A _Double_ specifying the pressure a. The default value is 0.0.

**`iNodeAUnit`**
: An _Integer_ specifying the node a unit. The default value is 0.

**`crNodeB`**
: A _Cursor_ specifying the node . The default value is None.

**`dPressureB`**
: A _Double_ specifying the pressure . The default value is 0.0.

**`iNodeBUnit`**
: An _Integer_ specifying the node unit. The default value is 0.

**`iDirection`**
: An _Integer_ specifying the direction. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.Pressure.By2Nodes(strName="PressureLinear1", crNodeA=None, dPressureA=0.0, iNodeAUnit=0, crNodeB=None, dPressureB=0.0, iNodeBUnit=0, iDirection=0, crlTarget=[], crEdit=None)
```
