```{module} Home.ImportMesh.ADVCADX()
:synopsis: import adx files
```

(Home.ImportMesh.ADVCADX)=

# Home.ImportMesh.ADVCADX

## Description

import adx files

## Syntax

```python
Home.ImportMesh.ADVCADX(strPath, dFaceAngle=60.0, dEdgeAngle=60.0)
```

Macro: {ref}`Macro-Home-ImportAdx`

Ribbon: {menuselection}`Home --> ImportMesh --> ADVCADX`

## Inputs

**`strPath`**
: A _String_ specifying the path. This is a required input.

**`dFaceAngle`**
: A _Double_ specifying the face angle. The default value is 60.0.

**`dEdgeAngle`**
: A _Double_ specifying the edge angle. The default value is 60.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ImportMesh.ADVCADX(strPath, dFaceAngle=60.0, dEdgeAngle=60.0)
```
