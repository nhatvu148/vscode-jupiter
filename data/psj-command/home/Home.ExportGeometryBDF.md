```{module} Home.ExportGeometryBDF()
:synopsis: Unknown Description
```

(Home.ExportGeometryBDF)=

# Home.ExportGeometryBDF

## Description

Unknown Description

## Syntax

```python
Home.ExportGeometryBDF(strFileName, crlPart=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True)
```

Macro: {ref}`Macro-Home-ExportGeomBDF`

Ribbon: {menuselection}`Home --> ExportGeometryBDF`

## Inputs

**`strFileName`**
: A _String_ specifying the file name. This is a required input.

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`bBigID`**
: A _Boolean_ specifying the big ID. The default value is False.

**`bUseUnit`**
: A _Boolean_ specifying the use unit. The default value is True.

**`bVert`**
: A _Boolean_ specifying the vert. The default value is True.

**`bEdge`**
: A _Boolean_ specifying the edge. The default value is True.

**`bFace`**
: A _Boolean_ specifying the face. The default value is True.

**`bSolid`**
: A _Boolean_ specifying the solid. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ExportGeometryBDF(strFileName, crlPart=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True)
```
