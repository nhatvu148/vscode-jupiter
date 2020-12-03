```{module} Home.ImportMesh.AnsysDat()
:synopsis: Import Ansys file
```

(Home.ImportMesh.AnsysDat)=

# Home.ImportMesh.AnsysDat

## Description

Import Ansys file

## Syntax

```python
Home.ImportMesh.AnsysDat(strlPath, dFaceAngle=60.0, dEdgeAngle=60.0)
```

Macro: {ref}`Macro-Home-ImportAnsys`

Ribbon: {menuselection}`Home --> ImportMesh --> AnsysDat`

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
Home.ImportMesh.AnsysDat(strlPath, dFaceAngle=60.0, dEdgeAngle=60.0)
```
