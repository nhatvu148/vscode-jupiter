```{module} BoundaryConditions.InitialNodalValue.Displacement()
:synopsis: Create Initial Dynamic
```

(BoundaryConditions.InitialNodalValue.Displacement)=

# BoundaryConditions.InitialNodalValue.Displacement

## Description

Create Initial Dynamic

## Syntax

```python
BoundaryConditions.InitialNodalValue.Displacement(strName="InitialDisplacement1", iType=0, vecInit=[DFLT_DBL,DFLT_DBL,DFLT_DBL], bSelNode=False, crNodeSet=None, crTable=None, crCoord=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-BoundaryConditions-InitialDynamic`

Ribbon: {menuselection}`BoundaryConditions --> InitialNodalValue --> Displacement`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "InitialDisplacement1".

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`vecInit`**
: A _Vector_ specifying the initial. The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

**`bSelNode`**
: A _Boolean_ specifying the selection node. The default value is False.

**`crNodeSet`**
: A _Cursor_ specifying the node set. The default value is None.

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
BoundaryConditions.InitialNodalValue.Displacement(strName="InitialDisplacement1", iType=0, vecInit=[DFLT_DBL,DFLT_DBL,DFLT_DBL], bSelNode=False, crNodeSet=None, crTable=None, crCoord=None, crlTarget=[], crEdit=None)
```
