```{module} Home.ImportMesh.AbaqusINP()
:synopsis: import Abaqus INP file
```

(Home.ImportMesh.AbaqusINP)=

# Home.ImportMesh.AbaqusINP

## Description

import Abaqus INP file

## Syntax

```python
Home.ImportMesh.AbaqusINP(strlFilePaths, dFaceAngle=60.0, dEdgeAngle=60.0, iImportType=1)
```

Macro: {ref}`Macro-Home-ImportInp`

Ribbon: {menuselection}`Home --> ImportMesh --> AbaqusINP`

## Inputs

**`strlFilePaths`**
: A _String List_ specifying the file paths. This is a required input.

**`dFaceAngle`**
: A _Double_ specifying the face angle. The default value is 60.0.

**`dEdgeAngle`**
: A _Double_ specifying the edge angle. The default value is 60.0.

**`iImportType`**
: An _Integer_ specifying the import type. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ImportMesh.AbaqusINP(strlFilePaths, dFaceAngle=60.0, dEdgeAngle=60.0, iImportType=1)
```
