```{module} Home.ImportMesh.LSDYNA()
:synopsis: Import Ls-Dyna file
```

(Home.ImportMesh.LSDYNA)=

# Home.ImportMesh.LSDYNA

## Description

Import Ls-Dyna file

## Syntax

```python
Home.ImportMesh.LSDYNA(strlPath, dFaceAngle=60.0, dEdgeAngle=60.0)
```

Macro: {ref}`Macro-Home-ImportLsDyna`

Ribbon: {menuselection}`Home --> ImportMesh --> LSDYNA`

## Inputs

**`strlPath`**
: A _String List_ specifying the path. This is a required input.

**`dFaceAngle`**
: A _Double_ specifying the face angle. The default value is 60.0.

**`dEdgeAngle`**
: A _Double_ specifying the edge angle. The default value is 60.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ImportMesh.LSDYNA(strlPath, dFaceAngle=60.0, dEdgeAngle=60.0)
```
