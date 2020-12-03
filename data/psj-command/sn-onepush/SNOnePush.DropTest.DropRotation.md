```{module} SNOnePush.DropTest.DropRotation()
:synopsis: Assemble cylinder layer
```

(SNOnePush.DropTest.DropRotation)=

# SNOnePush.DropTest.DropRotation

## Description

Assemble cylinder layer

## Syntax

```python
SNOnePush.DropTest.DropRotation(strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumberOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None)
```

Macro: {ref}`Macro-SNOnePush-DropRotation`

Ribbon: {menuselection}`SNOnePush --> DropTest --> DropRotation`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iDir`**
: An _Integer_ specifying the direction. The default value is 0.

**`dRopHeight`**
: A _Double_ specifying the drop height. The default value is 0.0.

**`dSolutionTime`**
: A _Double_ specifying the solution time. The default value is 0.0.

**`iNumberOutput`**
: An _Integer_ specifying the number output. The default value is 20.

**`dContactFriction`**
: A _Double_ specifying the contact friction. The default value is 0.1.

**`iRotAxis`**
: An _Integer_ specifying the rotation axis. The default value is 0.

**`dRotAngle`**
: A _Double_ specifying the rotation angle. The default value is 0.0.

**`dRelevantElemRate`**
: A _Double_ specifying the relevant element rate. The default value is 0.0.

**`dChangeMassRate`**
: A _Double_ specifying the change mass rate. The default value is 0.0.

**`dMinTimeStep`**
: A _Double_ specifying the minimum time step. The default value is 0.0.

**`strSolverFile`**
: A _String_ specifying the solver file. The default value is "".

**`dFloorSize`**
: A _Double_ specifying the floor size. The default value is 0.0.

**`bRename`**
: A _Boolean_ specifying the rename. The default value is True.

**`crMat`**
: A _Cursor_ specifying the material. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
SNOnePush.DropTest.DropRotation(strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumberOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None)
```
