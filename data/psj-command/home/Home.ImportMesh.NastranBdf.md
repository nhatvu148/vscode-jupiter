```{module} Home.ImportMesh.NastranBdf()
:synopsis: import Nastran bdf file
```

(Home.ImportMesh.NastranBdf)=

# Home.ImportMesh.NastranBdf

## Description

import Nastran bdf file

## Syntax

```python
Home.ImportMesh.NastranBdf(strlFilePaths, iImportType=2, dFaceAngle=60.0, dEdgeAngle=60.0, bReadNameComment=False, iCreateDup1DElemAnswer=-1)
```

Macro: {ref}`Macro-Home-ImportBdf`

Ribbon: {menuselection}`Home --> ImportMesh --> NastranBdf`

## Inputs

**`strlFilePaths`**
: A _String List_ specifying the file paths. This is a required input.

**`iImportType`**
: An _Integer_ specifying the import type. The default value is 2.

**`dFaceAngle`**
: A _Double_ specifying the face angle. The default value is 60.0.

**`dEdgeAngle`**
: A _Double_ specifying the edge angle. The default value is 60.0.

**`bReadNameComment`**
: A _Boolean_ specifying the read name comment. The default value is False.

**`iCreateDup1DElemAnswer`**
: An _Integer_ specifying the create dup1 d element answer. The default value is -1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ImportMesh.NastranBdf(strlFilePaths, iImportType=2, dFaceAngle=60.0, dEdgeAngle=60.0, bReadNameComment=False, iCreateDup1DElemAnswer=-1)
```
