# Export.STL

## Wrapper Macro

ExportSTL(...)

## Ribbon-GUI-Location

Export > STL

## Command Description

to export stl file

## Argument List

**Arg1: strFile**

Description: definition string of input file

Data Type: string

Default Value : ""

Syntax: strFile = "string input"

**Arg2: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg3: dScale**

Description: double value of scale

Data Type: double

Default Value : 1

Syntax: dScale = 1.0

**Arg4: bFilterIndex**

Description: enable or disable feature filter index

Data Type: bool

Default Value : False

Syntax: bFilterIndex = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Export.STL(strFile="", crlPart=[], dScale=1, bFilterIndex=False)

```

==========================================================

# FileMenu.AddJTDB

## Wrapper Macro

AddJTDB(...)

## Ribbon-GUI-Location

FileMenu > AddJTDB

## Command Description

add jtdb into model

## Argument List

**Arg1: strFileName**

Description: definition string of input file name

Data Type: string

Default Value : ""

Syntax: strFileName = "string input"

**Arg2: strMethod**

Description: definition string of input method

Data Type: string

Default Value : "AUTO"

Syntax: strMethod = "string input"

**Arg3: strTargetModel**

Description: definition string of input target model

Data Type: string

Default Value : "IMPORTED"

Syntax: strTargetModel = "string input"

**Arg4: strOption**

Description: definition string of input option

Data Type: string

Default Value : "OFFSET"

Syntax: strOption = "string input"

**Arg5: iInputNode**

Description: option for input node

Data Type: integer

Default Value : 0

Syntax: iInputNode = 1

**Arg6: iInputElem**

Description: option for input element

Data Type: integer

Default Value : 0

Syntax: iInputElem = 1

**Arg7: iInputPart**

Description: option for input part

Data Type: integer

Default Value : 0

Syntax: iInputPart = 1

**Arg8: iInputMaterial**

Description: option for input material

Data Type: integer

Default Value : 0

Syntax: iInputMaterial = 1

**Arg9: iInputProperty**

Description: option for input property

Data Type: integer

Default Value : 0

Syntax: iInputProperty = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

FileMenu.AddJTDB(strFileName="", strMethod="AUTO", strTargetModel="IMPORTED", strOption="OFFSET", iInputNode=0, iInputElem=0, iInputPart=0, iInputMaterial=0, iInputProperty=0)

```

==========================================================

# FileMenu.Save

## Wrapper Macro

SaveDB(...)

## Ribbon-GUI-Location

FileMenu > Save

## Command Description

Save file

## Argument List

**Arg1: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg2: strHistoryTree**

Description: definition string of input history tree

Data Type: string

Default Value : ""

Syntax: strHistoryTree = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

FileMenu.Save(strPath="", strHistoryTree="")

```

==========================================================

# FileMenu.LoadDB

## Wrapper Macro

LoadDB(...)

## Ribbon-GUI-Location

FileMenu > LoadDB

## Command Description

Load JTDB file

## Argument List

**Arg1: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg2: bUseTmpTable**

Description: enable or disable feature use tmp table

Data Type: bool

Default Value : False

Syntax: bUseTmpTable = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

FileMenu.LoadDB(strPath="", bUseTmpTable=False)

```

==========================================================

# HGTMufflerModeling.CreateBeadWeld

## Wrapper Macro

CreateBeadWeld(...)

## Ribbon-GUI-Location

HGTMufflerModeling > CreateBeadWeld

## Command Description

create bead weld

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg2: crlPrjtedEdge**

Description: array entities in model with type prjted edge

Data Type: cursor list

Default Value : []

Syntax: crlPrjtedEdge = [EntityType(id1, id2, id3)]

**Arg3: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg4: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTol = 1.0

**Arg5: dRatio**

Description: double value of ratio

Data Type: double

Default Value : 0.0

Syntax: dRatio = 1.0

**Arg6: crRefElem**

Description: entity in database model with type ref element

Data Type: cursor

Default Value : None

Syntax: crRefElem = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HGTMufflerModeling.CreateBeadWeld(crlEdge=[], crlPrjtedEdge=[], crlPart=[], dTol=0.0, dRatio=0.0, crRefElem=None)

```

==========================================================

# ImportCAD.Spatial

## Wrapper Macro

ImportSpatial(...)

## Ribbon-GUI-Location

ImportCAD > Spatial

## Command Description

Command use for ImportCAD Spatial

## Argument List

**Arg1: strlPath**

Description: list definition string of path

Data Type: string list

Default Value : []

Syntax: strlPath = ["str1", "str2", "str3"]

**Arg2: cadSpatialParamData**

Description: data structure of CAD_SPATIAL_PARAM_DATA (refer PSJ Command Data Structure Document)

Data Type: CAD_SPATIAL_PARAM_DATA

Default Value : CAD_SPATIAL_PARAM_DATA()

Syntax: cadSpatialParamData = CAD_SPATIAL_PARAM_DATA(,,,)

**Arg3: bIsNXDirect**

Description: enable or disable feature is n x direct

Data Type: bool

Default Value : False

Syntax: bIsNXDirect = True/False

**Arg4: bSetFaceColor**

Description: enable or disable feature set face color

Data Type: bool

Default Value : False

Syntax: bSetFaceColor = True/False

**Arg5: strCsvFilePath**

Description: definition string of input csv file path

Data Type: string

Default Value : ""

Syntax: strCsvFilePath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportCAD.Spatial(strlPath=[], cadSpatialParamData=CAD_SPATIAL_PARAM_DATA(), bIsNXDirect=False, bSetFaceColor=False, strCsvFilePath="")

```

==========================================================

# ImportCAD.TechnoStarGeometry

## Wrapper Macro

ImportGeomBDF(...)

## Ribbon-GUI-Location

ImportCAD > TechnoStarGeometry

## Command Description

Import Geometry bdf file

## Argument List

**Arg1: strlPath**

Description: list definition string of path

Data Type: string list

Default Value : []

Syntax: strlPath = ["str1", "str2", "str3"]

**Arg2: bUseUnit**

Description: enable or disable feature use unit

Data Type: bool

Default Value : True

Syntax: bUseUnit = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportCAD.TechnoStarGeometry(strlPath=[], bUseUnit=True)

```

==========================================================

# ImportCAD.CreoDirect

## Wrapper Macro

ImportCreo(...)

## Ribbon-GUI-Location

ImportCAD > CreoDirect

## Command Description

Command use for ImportCAD CreoDirect

## Argument List

**Arg1: vecPath**

Description: array values of path

Data Type: vector

Default Value : []

Syntax: vecPath = [value1, value2, value3]

**Arg2: cadProeParamData**

Description: data structure of CAD_PROE_PARAM_DATA (refer PSJ Command Data Structure Document)

Data Type: CAD_PROE_PARAM_DATA

Default Value : CAD_PROE_PARAM_DATA()

Syntax: cadProeParamData = CAD_PROE_PARAM_DATA(,,,)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportCAD.CreoDirect(vecPath=[], cadProeParamData=CAD_PROE_PARAM_DATA())

```

==========================================================

# ImportCAD.Elysium

## Wrapper Macro

ImportElysium(...)

## Ribbon-GUI-Location

ImportCAD > Elysium

## Command Description

Command use for ImportCAD Elysium

## Argument List

**Arg1: strlPath**

Description: list definition string of path

Data Type: string list

Default Value : []

Syntax: strlPath = ["str1", "str2", "str3"]

**Arg2: cadElysiumParamData**

Description: data structure of CAD_ELYSIUM_PARAM_DATA (refer PSJ Command Data Structure Document)

Data Type: CAD_ELYSIUM_PARAM_DATA

Default Value : CAD_ELYSIUM_PARAM_DATA()

Syntax: cadElysiumParamData = CAD_ELYSIUM_PARAM_DATA(,,,)

**Arg3: bFaceColor**

Description: enable or disable feature face color

Data Type: bool

Default Value : True

Syntax: bFaceColor = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportCAD.Elysium(strlPath=[], cadElysiumParamData=CAD_ELYSIUM_PARAM_DATA(), bFaceColor=True)

```

==========================================================

# ImportMesh.NastranBdf

## Wrapper Macro

ImportBdf(...)

## Ribbon-GUI-Location

ImportMesh > NastranBdf

## Command Description

Command use for ImportMesh NastranBdf

## Argument List

**Arg1: strlFilePaths**

Description: list definition string of file paths

Data Type: string list

Default Value : []

Syntax: strlFilePaths = ["str1", "str2", "str3"]

**Arg2: iImportType**

Description: option for import type

Data Type: integer

Default Value : 2

Syntax: iImportType = 1

**Arg3: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 60.0

Syntax: dFaceAngle = 1.0

**Arg4: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

**Arg5: bReadNameComment**

Description: enable or disable feature read name comment

Data Type: bool

Default Value : False

Syntax: bReadNameComment = True/False

**Arg6: iCreateDup1DElemAnswer**

Description: option for create dup1 d element answer

Data Type: integer

Default Value : 0

Syntax: iCreateDup1DElemAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportMesh.NastranBdf(strlFilePaths=[], iImportType=2, dFaceAngle=60.0, dEdgeAngle=60.0, bReadNameComment=False, iCreateDup1DElemAnswer=0)

```

==========================================================

# ImportMesh.AbaqusINP

## Wrapper Macro

ImportInp(...)

## Ribbon-GUI-Location

ImportMesh > AbaqusINP

## Command Description

Command use for ImportMesh AbaqusINP

## Argument List

**Arg1: strlFilePaths**

Description: list definition string of file paths

Data Type: string list

Default Value : []

Syntax: strlFilePaths = ["str1", "str2", "str3"]

**Arg2: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 60.0

Syntax: dFaceAngle = 1.0

**Arg3: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

**Arg4: iImportType**

Description: option for import type

Data Type: integer

Default Value : 1

Syntax: iImportType = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportMesh.AbaqusINP(strlFilePaths=[], dFaceAngle=60.0, dEdgeAngle=60.0, iImportType=1)

```

==========================================================

# ImportMesh.LSDYNA

## Wrapper Macro

ImportLsDyna(...)

## Ribbon-GUI-Location

ImportMesh > LSDYNA

## Command Description

Command use for ImportMesh LSDYNA

## Argument List

**Arg1: strlPath**

Description: list definition string of path

Data Type: string list

Default Value : []

Syntax: strlPath = ["str1", "str2", "str3"]

**Arg2: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 60.0

Syntax: dFaceAngle = 1.0

**Arg3: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportMesh.LSDYNA(strlPath=[], dFaceAngle=60.0, dEdgeAngle=60.0)

```

==========================================================

# ImportMesh.ADVCADX

## Wrapper Macro

ImportAdx(...)

## Ribbon-GUI-Location

ImportMesh > ADVCADX

## Command Description

Command use for ImportMesh ADVCADX

## Argument List

**Arg1: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg2: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 60.0

Syntax: dFaceAngle = 1.0

**Arg3: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportMesh.ADVCADX(strPath="", dFaceAngle=60.0, dEdgeAngle=60.0)

```

==========================================================

# ImportMesh.Universal

## Wrapper Macro

ImportUnv(...)

## Ribbon-GUI-Location

ImportMesh > Universal

## Command Description

Command use for ImportMesh Universal

## Argument List

**Arg1: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportMesh.Universal(strPath="")

```

==========================================================

# ImportMesh.AnsysDat

## Wrapper Macro

ImportAnsys(...)

## Ribbon-GUI-Location

ImportMesh > AnsysDat

## Command Description

Command use for ImportMesh AnsysDat

## Argument List

**Arg1: strlPath**

Description: list definition string of path

Data Type: string list

Default Value : []

Syntax: strlPath = ["str1", "str2", "str3"]

**Arg2: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 60.0

Syntax: dFaceAngle = 1.0

**Arg3: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportMesh.AnsysDat(strlPath=[], dFaceAngle=60.0, dEdgeAngle=60.0)

```

==========================================================

# ImportMesh.TSVPre

## Wrapper Macro

ImportVDB(...)

## Ribbon-GUI-Location

ImportMesh > TSVPre

## Command Description

Convert a old TSV-Pre/Designer file into one or more jtdb files.

## Argument List

**Arg1: strImportPath**

Description: definition string of input import path

Data Type: string

Default Value : ""

Syntax: strImportPath = "string input"

**Arg2: strExportPath**

Description: definition string of input export path

Data Type: string

Default Value : ""

Syntax: strExportPath = "string input"

**Arg3: ilModelIndex**

Description: array int values of model index

Data Type: int list

Default Value : None

Syntax: ilModelIndex = [1,2,3,4]

**Arg4: iMerge**

Description: option for merge

Data Type: integer

Default Value : None

Syntax: iMerge = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ImportMesh.TSVPre(strImportPath="", strExportPath="", ilModelIndex=None, iMerge=None)

```

==========================================================

# Utility.FindEntities

## Wrapper Macro

FindEntities(...)

## Ribbon-GUI-Location

Utility > FindEntities

## Command Description

Search entity by ID, Name ...etc

## Argument List

**Arg1: strTarget**

Description: definition string of input target

Data Type: string

Default Value : ""

Syntax: strTarget = "string input"

**Arg2: strFindType**

Description: definition string of input find type

Data Type: string

Default Value : ""

Syntax: strFindType = "string input"

**Arg3: bFindMatch**

Description: enable or disable feature find match

Data Type: bool

Default Value : False

Syntax: bFindMatch = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Utility.FindEntities(strTarget="", strFindType="", bFindMatch=False)

```

==========================================================

# Utility.MeasureDistanceBy2Edges

## Wrapper Macro

MeasureDistanceBy2Edges(...)

## Ribbon-GUI-Location

Utility > MeasureDistanceBy2Edges

## Command Description

Command use for Utility MeasureDistanceBy2Edges

## Argument List

**Arg1: crEdgeFirst**

Description: entity in database model with type edge first

Data Type: cursor

Default Value : None

Syntax: crEdgeFirst = EntityType(id)

**Arg2: crEdgeLast**

Description: entity in database model with type edge last

Data Type: cursor

Default Value : None

Syntax: crEdgeLast = EntityType(id)

**Arg3: iPrecision**

Description: option for precision

Data Type: integer

Default Value : 6

Syntax: iPrecision = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Utility.MeasureDistanceBy2Edges(crEdgeFirst=None, crEdgeLast=None, iPrecision=6)

```

==========================================================

# ACModeling.ACBoundary.Method1

## Wrapper Macro

ACBoundaryMethod1(...)

## Ribbon-GUI-Location

ACModeling > ACBoundary > Method1

## Command Description

AC boundary method 1

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: bIsMergePart**

Description: enable or disable feature is merge part

Data Type: bool

Default Value : False

Syntax: bIsMergePart = True/False

**Arg3: bIsRenumber**

Description: enable or disable feature is renumber

Data Type: bool

Default Value : False

Syntax: bIsRenumber = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ACModeling.ACBoundary.Method1(crlPart=[], bIsMergePart=False, bIsRenumber=False)

```

==========================================================

# ACModeling.Create.Convex

## Wrapper Macro

CreateConvex(...)

## Ribbon-GUI-Location

ACModeling > Create > Convex

## Command Description

Create Convex In Boundary

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: dMeshSize**

Description: double value of mesh size

Data Type: double

Default Value : 0.005

Syntax: dMeshSize = 1.0

**Arg3: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0.02

Syntax: dOffset = 1.0

**Arg4: dRadius**

Description: double value of radius

Data Type: double

Default Value : 0.02

Syntax: dRadius = 1.0

**Arg5: iDAxisGround**

Description: option for d axis ground

Data Type: integer

Default Value : 0

Syntax: iDAxisGround = 1

**Arg6: dScale**

Description: double value of scale

Data Type: double

Default Value : 0.001

Syntax: dScale = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ACModeling.Create.Convex(crlPart=[], dMeshSize=0.005, dOffset=0.02, dRadius=0.02, iDAxisGround=0, dScale=0.001)

```

==========================================================

# ACModeling.CloseHoleAuto

## Wrapper Macro

ACModelingCloseHoleAuto(...)

## Ribbon-GUI-Location

ACModeling > CloseHoleAuto

## Command Description

ACModeling CloseHoleAuto

## Argument List

**Arg1: crlClosedHoleParts**

Description: array entities in model with type closed hole parts

Data Type: cursor list

Default Value : []

Syntax: crlClosedHoleParts = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ACModeling.CloseHoleAuto(crlClosedHoleParts=[])

```

==========================================================

# ACModeling.Cut

## Wrapper Macro

ACModellingCut(...)

## Ribbon-GUI-Location

ACModeling > Cut

## Command Description

cut for ACModeling

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ACModeling.Cut(crlPart=[])

```

==========================================================

# Analysis.AbaqusStep.DynamicStep

## Wrapper Macro

AbaqusDynamicStep(...)

## Ribbon-GUI-Location

Analysis > AbaqusStep > DynamicStep

## Command Description

Command use for Analysis AbaqusStep DynamicStep

## Argument List

**Arg1: abaqusDynamic**

Description: data structure of ABAQUS_DYNAMIC (refer PSJ Command Data Structure Document)

Data Type: ABAQUS_DYNAMIC

Default Value : ABAQUS_DYNAMIC()

Syntax: abaqusDynamic = ABAQUS_DYNAMIC(,,,)

**Arg2: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.AbaqusStep.DynamicStep(abaqusDynamic=ABAQUS_DYNAMIC(), crEdit=None)

```

==========================================================

# Analysis.AbaqusStep.TransientStep

## Wrapper Macro

AbaqusTransientStep(...)

## Ribbon-GUI-Location

Analysis > AbaqusStep > TransientStep

## Command Description

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDesp**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDesp = "string input"

**Arg3: iEnableAutomatic**

Description: option for enable automatic

Data Type: integer

Default Value : 0

Syntax: iEnableAutomatic = 1

**Arg4: iMaxInc**

Description: option for maximize inc

Data Type: integer

Default Value : 0

Syntax: iMaxInc = 1

**Arg5: dInitSize**

Description: double value of init size

Data Type: double

Default Value : DFLT_DBL

Syntax: dInitSize = 1.0

**Arg6: dMinSize**

Description: double value of minimize size

Data Type: double

Default Value : DFLT_DBL

Syntax: dMinSize = 1.0

**Arg7: dMaxSize**

Description: double value of maximize size

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxSize = 1.0

**Arg8: dMaxAllowTChange**

Description: double value of maximize allow t change

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxAllowTChange = 1.0

**Arg9: iEndsteptBchecked**

Description: option for endstept bchecked

Data Type: integer

Default Value : 0

Syntax: iEndsteptBchecked = 1

**Arg10: dlEndsteptTlist**

Description: array double values of endstept tlist

Data Type: double list

Default Value : []

Syntax: dlEndsteptTlist = [1.0, 2.0]

**Arg11: dMaxAllowEmissivityChange**

Description: double value of maximize allow emissivity change

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxAllowEmissivityChange = 1.0

**Arg12: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg13: iMatrixStorage**

Description: option for matrix storage

Data Type: integer

Default Value : 0

Syntax: iMatrixStorage = 1

**Arg14: iSolutionTech**

Description: option for solution tech

Data Type: integer

Default Value : 0

Syntax: iSolutionTech = 1

**Arg15: iAllowedIters**

Description: option for allowed iterator

Data Type: integer

Default Value : 0

Syntax: iAllowedIters = 1

**Arg16: dAdjustFactor**

Description: double value of adjust factor

Data Type: double

Default Value : DFLT_DBL

Syntax: dAdjustFactor = 1.0

**Arg17: iMaxContactIter**

Description: option for maximize contact iterator

Data Type: integer

Default Value : 0

Syntax: iMaxContactIter = 1

**Arg18: iEnableNlgeom**

Description: option for enable nlgeom

Data Type: integer

Default Value : 0

Syntax: iEnableNlgeom = 1

**Arg19: dTimePeriod**

Description: double value of time period

Data Type: double

Default Value : DFLT_DBL

Syntax: dTimePeriod = 1.0

**Arg20: iConvertDscntIter**

Description: option for convert dscnt iterator

Data Type: integer

Default Value : 0

Syntax: iConvertDscntIter = 1

**Arg21: iRamp**

Description: option for ramp

Data Type: integer

Default Value : 0

Syntax: iRamp = 1

**Arg22: iExtrapolateMethod**

Description: option for extrapolate method

Data Type: integer

Default Value : 0

Syntax: iExtrapolateMethod = 1

**Arg23: listAbaqusOutputRequest**

Description: list data structure of ABAQUS_OUTPUT_REQUEST (refer PSJ Command Data Structure Document)

Data Type: ABAQUS_OUTPUT_REQUEST

Default Value : ABAQUS_OUTPUT_REQUEST()

Syntax: listAbaqusOutputRequest = [ABAQUS_OUTPUT_REQUEST(,,,), ABAQUS_OUTPUT_REQUEST(,,,)]

**Arg24: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.AbaqusStep.TransientStep(strName="", strDesp="", iEnableAutomatic=0, iMaxInc=0, dInitSize=DFLT_DBL, dMinSize=DFLT_DBL, dMaxSize=DFLT_DBL, dMaxAllowTChange=DFLT_DBL, iEndsteptBchecked=0, dlEndsteptTlist=[], dMaxAllowEmissivityChange=DFLT_DBL, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=0, dAdjustFactor=DFLT_DBL, iMaxContactIter=0, iEnableNlgeom=0, dTimePeriod=DFLT_DBL, iConvertDscntIter=0, iRamp=0, iExtrapolateMethod=0, listAbaqusOutputRequest=[], crEdit=None)

```

==========================================================

# Analysis.AbaqusStep.CoupledTDStep

## Wrapper Macro

AbaqusCoupledTDStep(...)

## Ribbon-GUI-Location

Analysis > AbaqusStep > CoupledTDStep

## Command Description

create abaqus step of coupled temperature-Displacement

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDesp**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDesp = "string input"

**Arg3: iEnableAutomatic**

Description: option for enable automatic

Data Type: integer

Default Value : 0

Syntax: iEnableAutomatic = 1

**Arg4: iMaxInc**

Description: option for maximize inc

Data Type: integer

Default Value : 100

Syntax: iMaxInc = 1

**Arg5: dInitSize**

Description: double value of init size

Data Type: double

Default Value : 1.0

Syntax: dInitSize = 1.0

**Arg6: dMinSize**

Description: double value of minimize size

Data Type: double

Default Value : 1.0e-5

Syntax: dMinSize = 1.0

**Arg7: dMaxSize**

Description: double value of maximize size

Data Type: double

Default Value : 1.0

Syntax: dMaxSize = 1.0

**Arg8: abaqusPair1**

Description: data structure of ABAQUS_PAIR (refer PSJ Command Data Structure Document)

Data Type: ABAQUS_PAIR

Default Value : ABAQUS_PAIR()

Syntax: abaqusPair1 = ABAQUS_PAIR(,,,)

**Arg9: abaqusPair2**

Description: data structure of ABAQUS_PAIR (refer PSJ Command Data Structure Document)

Data Type: ABAQUS_PAIR

Default Value : ABAQUS_PAIR()

Syntax: abaqusPair2 = ABAQUS_PAIR(,,,)

**Arg10: iCSVIntegration**

Description: option for c s v integration

Data Type: integer

Default Value : 0

Syntax: iCSVIntegration = 1

**Arg11: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg12: iMatrixStorage**

Description: option for matrix storage

Data Type: integer

Default Value : 0

Syntax: iMatrixStorage = 1

**Arg13: iSolutionTech**

Description: option for solution tech

Data Type: integer

Default Value : 0

Syntax: iSolutionTech = 1

**Arg14: iAllowedIters**

Description: option for allowed iterator

Data Type: integer

Default Value : 8

Syntax: iAllowedIters = 1

**Arg15: dAdjustFactor**

Description: double value of adjust factor

Data Type: double

Default Value : 1.0

Syntax: dAdjustFactor = 1.0

**Arg16: iMaxContactIter**

Description: option for maximize contact iterator

Data Type: integer

Default Value : 30

Syntax: iMaxContactIter = 1

**Arg17: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg18: iEnableUseAdaptive**

Description: option for enable use adaptive

Data Type: integer

Default Value : 1

Syntax: iEnableUseAdaptive = 1

**Arg19: dDampingfactor**

Description: double value of dampingfactor

Data Type: double

Default Value : 0.0002

Syntax: dDampingfactor = 1.0

**Arg20: dMaxRationofStrainEnergy**

Description: double value of maximize rationof strain energy

Data Type: double

Default Value : 0.05

Syntax: dMaxRationofStrainEnergy = 1.0

**Arg21: iEnableNlgeom**

Description: option for enable nlgeom

Data Type: integer

Default Value : 0

Syntax: iEnableNlgeom = 1

**Arg22: dTimePeriod**

Description: double value of time period

Data Type: double

Default Value : 1.0

Syntax: dTimePeriod = 1.0

**Arg23: iTransient**

Description: option for transient

Data Type: integer

Default Value : 1

Syntax: iTransient = 1

**Arg24: iConvertDscntIter**

Description: option for convert dscnt iterator

Data Type: integer

Default Value : 0

Syntax: iConvertDscntIter = 1

**Arg25: iRamp**

Description: option for ramp

Data Type: integer

Default Value : 1

Syntax: iRamp = 1

**Arg26: iExtrapolateMethod**

Description: option for extrapolate method

Data Type: integer

Default Value : 0

Syntax: iExtrapolateMethod = 1

**Arg27: iEnableIncludeCSV**

Description: option for enable include c s v

Data Type: integer

Default Value : 0

Syntax: iEnableIncludeCSV = 1

**Arg28: listAbaqusOutputRequest**

Description: list data structure of ABAQUS_OUTPUT_REQUEST (refer PSJ Command Data Structure Document)

Data Type: ABAQUS_OUTPUT_REQUEST

Default Value : ABAQUS_OUTPUT_REQUEST()

Syntax: listAbaqusOutputRequest = [ABAQUS_OUTPUT_REQUEST(,,,), ABAQUS_OUTPUT_REQUEST(,,,)]

**Arg29: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.AbaqusStep.CoupledTDStep(strName="", strDesp="", iEnableAutomatic=0, iMaxInc=100, dInitSize=1.0, dMinSize=1.0e-5, dMaxSize=1.0, abaqusPair1=ABAQUS_PAIR(), abaqusPair2=ABAQUS_PAIR(), iCSVIntegration=0, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=8, dAdjustFactor=1.0, iMaxContactIter=30, iType=0, iEnableUseAdaptive=1, dDampingfactor=0.0002, dMaxRationofStrainEnergy=0.05, iEnableNlgeom=0, dTimePeriod=1.0, iTransient=1, iConvertDscntIter=0, iRamp=1, iExtrapolateMethod=0, iEnableIncludeCSV=0, listAbaqusOutputRequest=[], crEdit=None)

```

==========================================================

# Analysis.AbaqusStep.DynamicExplicitStep

## Wrapper Macro

AbaqusDynamicExplicitStep(...)

## Ribbon-GUI-Location

Analysis > AbaqusStep > DynamicExplicitStep

## Command Description

create abaqus step of dynamic explicit

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDesp**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDesp = "string input"

**Arg3: iEnableAutomatic**

Description: option for enable automatic

Data Type: integer

Default Value : 1

Syntax: iEnableAutomatic = 1

**Arg4: iIncrmtEstimator**

Description: option for incrmt estimator

Data Type: integer

Default Value : 0

Syntax: iIncrmtEstimator = 1

**Arg5: abaqusPair1**

Description: data structure of ABAQUS_PAIR (refer PSJ Command Data Structure Document)

Data Type: ABAQUS_PAIR

Default Value : ABAQUS_PAIR()

Syntax: abaqusPair1 = ABAQUS_PAIR(,,,)

**Arg6: dTimeScalfactor**

Description: double value of time scalfactor

Data Type: double

Default Value : 1.0

Syntax: dTimeScalfactor = 1.0

**Arg7: abaqusPair2**

Description: data structure of ABAQUS_PAIR (refer PSJ Command Data Structure Document)

Data Type: ABAQUS_PAIR

Default Value : ABAQUS_PAIR()

Syntax: abaqusPair2 = ABAQUS_PAIR(,,,)

**Arg8: iEnableNlgeom**

Description: option for enable nlgeom

Data Type: integer

Default Value : 1

Syntax: iEnableNlgeom = 1

**Arg9: dTimePeriod**

Description: double value of time period

Data Type: double

Default Value : 1.0

Syntax: dTimePeriod = 1.0

**Arg10: iEnableIncludeHeatEffect**

Description: option for enable include heat effect

Data Type: integer

Default Value : 0

Syntax: iEnableIncludeHeatEffect = 1

**Arg11: dLinearBlkVisco**

Description: double value of linear blk visco

Data Type: double

Default Value : 0.06

Syntax: dLinearBlkVisco = 1.0

**Arg12: dQuadrBlkVisco**

Description: double value of quadr blk visco

Data Type: double

Default Value : 1.2

Syntax: dQuadrBlkVisco = 1.0

**Arg13: listAbaqusOutputRequest**

Description: list data structure of ABAQUS_OUTPUT_REQUEST (refer PSJ Command Data Structure Document)

Data Type: ABAQUS_OUTPUT_REQUEST

Default Value : ABAQUS_OUTPUT_REQUEST()

Syntax: listAbaqusOutputRequest = [ABAQUS_OUTPUT_REQUEST(,,,), ABAQUS_OUTPUT_REQUEST(,,,)]

**Arg14: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.AbaqusStep.DynamicExplicitStep(strName="", strDesp="", iEnableAutomatic=1, iIncrmtEstimator=0, abaqusPair1=ABAQUS_PAIR(), dTimeScalfactor=1.0, abaqusPair2=ABAQUS_PAIR(), iEnableNlgeom=1, dTimePeriod=1.0, iEnableIncludeHeatEffect=0, dLinearBlkVisco=0.06, dQuadrBlkVisco=1.2, listAbaqusOutputRequest=[], crEdit=None)

```

==========================================================

# Analysis.AbaqusStep.ModalStep

## Wrapper Macro

AbaqusModalStep(...)

## Ribbon-GUI-Location

Analysis > AbaqusStep > ModalStep

## Command Description

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDesp**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDesp = "string input"

**Arg3: iEigenSolver**

Description: option for eigen solver

Data Type: integer

Default Value : 0

Syntax: iEigenSolver = 1

**Arg4: iNFreqRequestbchecked**

Description: option for n frequency requestbchecked

Data Type: integer

Default Value : 0

Syntax: iNFreqRequestbchecked = 1

**Arg5: ilNFreqRequestTList**

Description: array int values of n frequency request TList

Data Type: int list

Default Value : []

Syntax: ilNFreqRequestTList = [1,2,3,4]

**Arg6: iFreqShiftbchecked**

Description: option for frequency shiftbchecked

Data Type: integer

Default Value : 0

Syntax: iFreqShiftbchecked = 1

**Arg7: ilFreqShiftTList**

Description: array int values of frequency shift TList

Data Type: int list

Default Value : []

Syntax: ilFreqShiftTList = [1,2,3,4]

**Arg8: iFreqRangebchecked**

Description: option for frequency rangebchecked

Data Type: integer

Default Value : 0

Syntax: iFreqRangebchecked = 1

**Arg9: ilFreqRangeTList**

Description: array int values of frequency range TList

Data Type: int list

Default Value : []

Syntax: ilFreqRangeTList = [1,2,3,4]

**Arg10: iIncldAcoustic**

Description: option for incld acoustic

Data Type: integer

Default Value : 0

Syntax: iIncldAcoustic = 1

**Arg11: iBlockSizebchecked**

Description: option for block sizebchecked

Data Type: integer

Default Value : 0

Syntax: iBlockSizebchecked = 1

**Arg12: ilBlockSizeTList**

Description: array int values of block size TList

Data Type: int list

Default Value : []

Syntax: ilBlockSizeTList = [1,2,3,4]

**Arg13: iMaxBlkNumofLanczosStepbchecked**

Description: option for maximize blk numof lanczos stepbchecked

Data Type: integer

Default Value : 0

Syntax: iMaxBlkNumofLanczosStepbchecked = 1

**Arg14: ilMaxBlkNumofLanczosStepTList**

Description: array int values of maximize blk numof lanczos step TList

Data Type: int list

Default Value : []

Syntax: ilMaxBlkNumofLanczosStepTList = [1,2,3,4]

**Arg15: iEnableUseSIM**

Description: option for enable use s i m

Data Type: integer

Default Value : 0

Syntax: iEnableUseSIM = 1

**Arg16: iEnableIncludeResMods**

Description: option for enable include res mods

Data Type: integer

Default Value : 0

Syntax: iEnableIncludeResMods = 1

**Arg17: iNEigenRequest**

Description: option for n eigen request

Data Type: integer

Default Value : 2147483647

Syntax: iNEigenRequest = 1

**Arg18: iMaxItersUsed**

Description: option for maximize iterator used

Data Type: integer

Default Value : 30

Syntax: iMaxItersUsed = 1

**Arg19: iVectorsUsed**

Description: option for vectors used

Data Type: integer

Default Value : 2147483647

Syntax: iVectorsUsed = 1

**Arg20: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg21: iMatrixStorage**

Description: option for matrix storage

Data Type: integer

Default Value : 0

Syntax: iMatrixStorage = 1

**Arg22: iNormalizeEigenBy**

Description: option for normalize eigen by

Data Type: integer

Default Value : 1

Syntax: iNormalizeEigenBy = 1

**Arg23: iEvalPropFreqbchecked**

Description: option for eval property freqbchecked

Data Type: integer

Default Value : 0

Syntax: iEvalPropFreqbchecked = 1

**Arg24: ilEvalPropFreqTList**

Description: array int values of eval property frequency TList

Data Type: int list

Default Value : []

Syntax: ilEvalPropFreqTList = [1,2,3,4]

**Arg25: abaqusOutputRequest**

Description: data structure of ABAQUS_OUTPUT_REQUEST (refer PSJ Command Data Structure Document)

Data Type: ABAQUS_OUTPUT_REQUEST

Default Value : ABAQUS_OUTPUT_REQUEST()

Syntax: abaqusOutputRequest = ABAQUS_OUTPUT_REQUEST(,,,)

**Arg26: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.AbaqusStep.ModalStep(strName="", strDesp="", iEigenSolver=0, iNFreqRequestbchecked=0, ilNFreqRequestTList=[], iFreqShiftbchecked=0, ilFreqShiftTList=[], iFreqRangebchecked=0, ilFreqRangeTList=[], iIncldAcoustic=0, iBlockSizebchecked=0, ilBlockSizeTList=[], iMaxBlkNumofLanczosStepbchecked=0, ilMaxBlkNumofLanczosStepTList=[], iEnableUseSIM=0, iEnableIncludeResMods=0, iNEigenRequest=2147483647, iMaxItersUsed=30, iVectorsUsed=2147483647, iMethod=0, iMatrixStorage=0, iNormalizeEigenBy=1, iEvalPropFreqbchecked=0, ilEvalPropFreqTList=[], abaqusOutputRequest=ABAQUS_OUTPUT_REQUEST(), crEdit=None)

```

==========================================================

# Analysis.AbaqusStep.StaticRiskStep

## Wrapper Macro

AbaqusStaticRiskStep(...)

## Ribbon-GUI-Location

Analysis > AbaqusStep > StaticRiskStep

## Command Description

Abaqus Static Risk Step

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDesp**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDesp = "string input"

**Arg3: iEnableAutomatic**

Description: option for enable automatic

Data Type: integer

Default Value : 0

Syntax: iEnableAutomatic = 1

**Arg4: iMaxInc**

Description: option for maximize inc

Data Type: integer

Default Value : 100

Syntax: iMaxInc = 1

**Arg5: dInitSize**

Description: double value of init size

Data Type: double

Default Value : 1.0

Syntax: dInitSize = 1.0

**Arg6: dMinSize**

Description: double value of minimize size

Data Type: double

Default Value : 1.0e-5

Syntax: dMinSize = 1.0

**Arg7: dMaxSize**

Description: double value of maximize size

Data Type: double

Default Value : 1.0

Syntax: dMaxSize = 1.0

**Arg8: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg9: iMatrixStorage**

Description: option for matrix storage

Data Type: integer

Default Value : 0

Syntax: iMatrixStorage = 1

**Arg10: dMaxLdPropFactor**

Description: double value of maximize ld property factor

Data Type: double

Default Value : 0.0

Syntax: dMaxLdPropFactor = 1.0

**Arg11: iEnableMaxLdPropFactor**

Description: option for enable maximize ld property factor

Data Type: integer

Default Value : 0

Syntax: iEnableMaxLdPropFactor = 1

**Arg12: iEnableMaxDisp**

Description: option for enable maximize disp

Data Type: integer

Default Value : 0

Syntax: iEnableMaxDisp = 1

**Arg13: dMaxDisp**

Description: double value of maximize disp

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxDisp = 1.0

**Arg14: iEnableMaxDispDof**

Description: option for enable maximize disp dof

Data Type: integer

Default Value : DFLT_INT

Syntax: iEnableMaxDispDof = 1

**Arg15: strNdRgn**

Description: definition string of input nd rgn

Data Type: string

Default Value : ""

Syntax: strNdRgn = "string input"

**Arg16: iEnableNlgeom**

Description: option for enable nlgeom

Data Type: integer

Default Value : 0

Syntax: iEnableNlgeom = 1

**Arg17: iEnableIncludeHeatEffect**

Description: option for enable include heat effect

Data Type: integer

Default Value : 0

Syntax: iEnableIncludeHeatEffect = 1

**Arg18: iConvertDscntIter**

Description: option for convert dscnt iterator

Data Type: integer

Default Value : 0

Syntax: iConvertDscntIter = 1

**Arg19: dTotalArcLength**

Description: double value of total arc length

Data Type: double

Default Value : 1.0

Syntax: dTotalArcLength = 1.0

**Arg20: iExtrapolateMethod**

Description: option for extrapolate method

Data Type: integer

Default Value : 0

Syntax: iExtrapolateMethod = 1

**Arg21: iEnableAcceptByMaxIters**

Description: option for enable accept by maximize iterator

Data Type: integer

Default Value : 0

Syntax: iEnableAcceptByMaxIters = 1

**Arg22: iEnableLongTerm**

Description: option for enable long term

Data Type: integer

Default Value : 0

Syntax: iEnableLongTerm = 1

**Arg23: iEnablePerturbation**

Description: option for enable perturbation

Data Type: integer

Default Value : 0

Syntax: iEnablePerturbation = 1

**Arg24: iFullplasticregionBchecked**

Description: option for fullplasticregion bchecked

Data Type: integer

Default Value : 0

Syntax: iFullplasticregionBchecked = 1

**Arg25: strlFullplasticregionTlist**

Description: list definition string of fullplasticregion tlist

Data Type: string list

Default Value : []

Syntax: strlFullplasticregionTlist = ["str1", "str2", "str3"]

**Arg26: iOutput**

Description: option for output

Data Type: integer

Default Value : 0

Syntax: iOutput = 1

**Arg27: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.AbaqusStep.StaticRiskStep(strName="", strDesp="", iEnableAutomatic=0, iMaxInc=100, dInitSize=1.0, dMinSize=1.0e-5, dMaxSize=1.0, iMethod=0, iMatrixStorage=0, dMaxLdPropFactor=0.0, iEnableMaxLdPropFactor=0, iEnableMaxDisp=0, dMaxDisp=DFLT_DBL, iEnableMaxDispDof=DFLT_INT, strNdRgn="", iEnableNlgeom=0, iEnableIncludeHeatEffect=0, iConvertDscntIter=0, dTotalArcLength=1.0, iExtrapolateMethod=0, iEnableAcceptByMaxIters=0, iEnableLongTerm=0, iEnablePerturbation=0, iFullplasticregionBchecked=0, strlFullplasticregionTlist=[], iOutput=0, crEdit=None)

```

==========================================================

# Analysis.AbaqusStep.SteadyStateStep

## Wrapper Macro

AbaqusSteadyStateStep(...)

## Ribbon-GUI-Location

Analysis > AbaqusStep > SteadyStateStep

## Command Description

Abaqus Steady State Step

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDesp**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDesp = "string input"

**Arg3: iEnableAutomatic**

Description: option for enable automatic

Data Type: integer

Default Value : 0

Syntax: iEnableAutomatic = 1

**Arg4: iMaxInc**

Description: option for maximize inc

Data Type: integer

Default Value : 100

Syntax: iMaxInc = 1

**Arg5: iNitSize**

Description: option for nit size

Data Type: integer

Default Value : 1

Syntax: iNitSize = 1

**Arg6: dMinSize**

Description: double value of minimize size

Data Type: double

Default Value : 1.0e-5

Syntax: dMinSize = 1.0

**Arg7: dMaxSize**

Description: double value of maximize size

Data Type: double

Default Value : 1.0

Syntax: dMaxSize = 1.0

**Arg8: dMaxAllowTChange**

Description: double value of maximize allow t change

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxAllowTChange = 1.0

**Arg9: iEndStepbchecked**

Description: option for end stepbchecked

Data Type: integer

Default Value : 0

Syntax: iEndStepbchecked = 1

**Arg10: dlEndStepTList**

Description: array double values of end step TList

Data Type: double list

Default Value : []

Syntax: dlEndStepTList = [1.0, 2.0]

**Arg11: dMaxAllowEmissivityChange**

Description: double value of maximize allow emissivity change

Data Type: double

Default Value : 0.1

Syntax: dMaxAllowEmissivityChange = 1.0

**Arg12: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg13: iMatrixStorage**

Description: option for matrix storage

Data Type: integer

Default Value : 0

Syntax: iMatrixStorage = 1

**Arg14: iSolutionTech**

Description: option for solution tech

Data Type: integer

Default Value : 0

Syntax: iSolutionTech = 1

**Arg15: iAllowedIters**

Description: option for allowed iterator

Data Type: integer

Default Value : 8

Syntax: iAllowedIters = 1

**Arg16: iAdjustFactor**

Description: option for adjust factor

Data Type: integer

Default Value : 1

Syntax: iAdjustFactor = 1

**Arg17: iMaxContactIter**

Description: option for maximize contact iterator

Data Type: integer

Default Value : 30

Syntax: iMaxContactIter = 1

**Arg18: iEnableNlgeom**

Description: option for enable nlgeom

Data Type: integer

Default Value : 0

Syntax: iEnableNlgeom = 1

**Arg19: dTimePeriod**

Description: double value of time period

Data Type: double

Default Value : 1.0

Syntax: dTimePeriod = 1.0

**Arg20: iConvertDscntIter**

Description: option for convert dscnt iterator

Data Type: integer

Default Value : 0

Syntax: iConvertDscntIter = 1

**Arg21: iRamp**

Description: option for ramp

Data Type: integer

Default Value : 0

Syntax: iRamp = 1

**Arg22: iExtrapolateMethod**

Description: option for extrapolate method

Data Type: integer

Default Value : 0

Syntax: iExtrapolateMethod = 1

**Arg23: iOutput**

Description: option for output

Data Type: integer

Default Value : 0

Syntax: iOutput = 1

**Arg24: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.AbaqusStep.SteadyStateStep(strName="", strDesp="", iEnableAutomatic=0, iMaxInc=100, iNitSize=1, dMinSize=1.0e-5, dMaxSize=1.0, dMaxAllowTChange=DFLT_DBL, iEndStepbchecked=0, dlEndStepTList=[], dMaxAllowEmissivityChange=0.1, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=8, iAdjustFactor=1, iMaxContactIter=30, iEnableNlgeom=0, dTimePeriod=1.0, iConvertDscntIter=0, iRamp=0, iExtrapolateMethod=0, iOutput=0, crEdit=None)

```

==========================================================

# Analysis.ACTRAN.ExportBdf

## Wrapper Macro

ExportActranBdf(...)

## Ribbon-GUI-Location

Analysis > ACTRAN > ExportBdf

## Command Description

## Argument List

**Arg1: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ACTRAN.ExportBdf(strPath="")

```

==========================================================

# Analysis.ACTRAN.Run

## Wrapper Macro

AnalysisActranRun(...)

## Ribbon-GUI-Location

Analysis > ACTRAN > Run

## Command Description

Command use for Analysis ACTRAN Run

## Argument List

**Arg1: actranAnalysis**

Description: data structure of ACTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: ACTRAN_ANALYSIS

Default Value : ACTRAN_ANALYSIS()

Syntax: actranAnalysis = ACTRAN_ANALYSIS(,,,)

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ACTRAN.Run(actranAnalysis=ACTRAN_ANALYSIS(), crlTarget=[], crEdit=None)

```

==========================================================

# Analysis.ACTRAN.CreateEdat

## Wrapper Macro

AnalysisActranJob(...)

## Ribbon-GUI-Location

Analysis > ACTRAN > CreateEdat

## Command Description

Command use for Analysis ACTRAN CreateEdat

## Argument List

**Arg1: actranAnalysis**

Description: data structure of ACTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: ACTRAN_ANALYSIS

Default Value : ACTRAN_ANALYSIS()

Syntax: actranAnalysis = ACTRAN_ANALYSIS(,,,)

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ACTRAN.CreateEdat(actranAnalysis=ACTRAN_ANALYSIS(), crlTarget=[], crEdit=None)

```

==========================================================

# Analysis.Analysis.Abaqus

## Wrapper Macro

CreateAbaqusJob(...)

## Ribbon-GUI-Location

Analysis > Analysis > Abaqus

## Command Description

Command use for Analysis Abaqus

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: bRBE2toMPC**

Description: enable or disable feature r b e2to m p c

Data Type: bool

Default Value : False

Syntax: bRBE2toMPC = True/False

**Arg3: bRenameProcess**

Description: enable or disable feature rename process

Data Type: bool

Default Value : False

Syntax: bRenameProcess = True/False

**Arg4: iCodeType**

Description: option for code type

Data Type: integer

Default Value : 0

Syntax: iCodeType = 1

**Arg5: iSurfDefType**

Description: option for surf def type

Data Type: integer

Default Value : 0

Syntax: iSurfDefType = 1

**Arg6: iUnit**

Description: option for unit

Data Type: integer

Default Value : 0

Syntax: iUnit = 1

**Arg7: iWriteType**

Description: option for write type

Data Type: integer

Default Value : 0

Syntax: iWriteType = 1

**Arg8: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg9: crlStepSequence**

Description: array entities in model with type step sequence

Data Type: cursor list

Default Value : []

Syntax: crlStepSequence = [EntityType(id1, id2, id3)]

**Arg10: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg11: strlUserText**

Description: list definition string of user text

Data Type: string list

Default Value : []

Syntax: strlUserText = ["str1", "str2", "str3"]

**Arg12: bExptNdEleGroups**

Description: enable or disable feature expt nd ele groups

Data Type: bool

Default Value : False

Syntax: bExptNdEleGroups = True/False

**Arg13: bDeleteFloatingNodes**

Description: enable or disable feature delete floating nodes

Data Type: bool

Default Value : False

Syntax: bDeleteFloatingNodes = True/False

**Arg14: bExptFaceElemGroups2Surface**

Description: enable or disable feature expt face element groups2 surface

Data Type: bool

Default Value : False

Syntax: bExptFaceElemGroups2Surface = True/False

**Arg15: bLoadCase**

Description: enable or disable feature load case

Data Type: bool

Default Value : False

Syntax: bLoadCase = True/False

**Arg16: bAutoAssignDummyProperty**

Description: enable or disable feature auto assign dummy property

Data Type: bool

Default Value : False

Syntax: bAutoAssignDummyProperty = True/False

**Arg17: crDummyMat**

Description: entity in database model with type dummy material

Data Type: cursor

Default Value : None

Syntax: crDummyMat = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Analysis.Abaqus(strName="", bRBE2toMPC=False, bRenameProcess=False, iCodeType=0, iSurfDefType=0, iUnit=0, iWriteType=0, strDescription="", crlStepSequence=[], crEdit=None, strlUserText=[], bExptNdEleGroups=False, bDeleteFloatingNodes=False, bExptFaceElemGroups2Surface=False, bLoadCase=False, bAutoAssignDummyProperty=False, crDummyMat=None)

```

==========================================================

# Analysis.Ansys.HeadTransferSteady

## Wrapper Macro

CreateAnsysJob(...)

## Ribbon-GUI-Location

Analysis > Ansys > HeadTransferSteady

## Command Description

Set parameters

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iJobdataAnatype**

Description: option for job data anatype

Data Type: integer

Default Value : 0

Syntax: iJobdataAnatype = 1

**Arg3: iJobdataSoltype**

Description: option for job data solution type

Data Type: integer

Default Value : 0

Syntax: iJobdataSoltype = 1

**Arg4: strJobdataJobname**

Description: definition string of input job data job name

Data Type: string

Default Value : "Job1"

Syntax: strJobdataJobname = "string input"

**Arg5: strJobdataJobdescription**

Description: definition string of input job data jobdescription

Data Type: string

Default Value : ""

Syntax: strJobdataJobdescription = "string input"

**Arg6: bBasicdataBoutputdisplacements**

Description: enable or disable feature basicdata boutputdisplacements

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputdisplacements = True/False

**Arg7: bBasicdataBoutputreactionload**

Description: enable or disable feature basicdata boutputreactionload

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputreactionload = True/False

**Arg8: bBasicdataBoutputstrain**

Description: enable or disable feature basicdata boutputstrain

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputstrain = True/False

**Arg9: bBasicdataBoutputstress**

Description: enable or disable feature basicdata boutputstress

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputstress = True/False

**Arg10: iBasicdataIanalysisopt**

Description: option for basicdata ianalysisopt

Data Type: integer

Default Value : 0

Syntax: iBasicdataIanalysisopt = 1

**Arg11: bBasicdataBcalPressEffects**

Description: enable or disable feature basic data caculation press effects

Data Type: bool

Default Value : False

Syntax: bBasicdataBcalPressEffects = True/False

**Arg12: dBasicdataFunitem**

Description: double value of basic data fun item

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFunitem = 1.0

**Arg13: dBasicdataFreftemp**

Description: double value of basic reference temperature

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFreftemp = 1.0

**Arg14: dBasicdataFendloadtime**

Description: double value of basic data end load time

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFendloadtime = 1.0

**Arg15: iBasicdataItimestep**

Description: option for basic data time step value

Data Type: integer

Default Value : 0

Syntax: iBasicdataItimestep = 1

**Arg16: iBasicdataIstepchosen**

Description: option for basic data step chosen value

Data Type: integer

Default Value : 0

Syntax: iBasicdataIstepchosen = 1

**Arg17: iBasicdataIsubstepnum**

Description: option for basic data substep number

Data Type: integer

Default Value : 0

Syntax: iBasicdataIsubstepnum = 1

**Arg18: iBasicdataImaxsubstep**

Description: option for basic data maximum substep value

Data Type: integer

Default Value : 0

Syntax: iBasicdataImaxsubstep = 1

**Arg19: iBasicdataIminstepnum**

Description: option for basic data minimum step number

Data Type: integer

Default Value : 0

Syntax: iBasicdataIminstepnum = 1

**Arg20: dBasicdataFtimestepsize**

Description: double value of basic data time step size

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFtimestepsize = 1.0

**Arg21: dBasicdataFmintimestep**

Description: double value of basic data minimum time step

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFmintimestep = 1.0

**Arg22: dBasicdataFmaxtimestep**

Description: double value of basic data maximum time step

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFmaxtimestep = 1.0

**Arg23: iBasicdataIwritereslutfre**

Description: option for basic data write result frequency

Data Type: integer

Default Value : 1

Syntax: iBasicdataIwritereslutfre = 1

**Arg24: iBasicdataIn**

Description: option for basic data in

Data Type: integer

Default Value : 1

Syntax: iBasicdataIn = 1

**Arg25: bRunAPDL**

Description: enable or disable feature run APDL

Data Type: bool

Default Value : False

Syntax: bRunAPDL = True/False

**Arg26: bWriteResultDB**

Description: enable or disable feature write result database

Data Type: bool

Default Value : False

Syntax: bWriteResultDB = True/False

**Arg27: dFEndFreq**

Description: double value of end frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dFEndFreq = 1.0

**Arg28: dFStartFreq**

Description: double value of start frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dFStartFreq = 1.0

**Arg29: iFulltransdataIsolutionoption**

Description: option for fulltransdata isolutionoption

Data Type: integer

Default Value : 0

Syntax: iFulltransdataIsolutionoption = 1

**Arg30: dFulltransdataFpropchange**

Description: double value of fulltransdata fpropchange

Data Type: double

Default Value : 0.05

Syntax: dFulltransdataFpropchange = 1.0

**Arg31: iFulltransdataIpointnum**

Description: option for fulltransdata ipointnum

Data Type: integer

Default Value : 64

Syntax: iFulltransdataIpointnum = 1

**Arg32: dFulltransdataFmintemp**

Description: double value of fulltransdata fmintemp

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmintemp = 1.0

**Arg33: dFulltransdataFmaxtemp**

Description: double value of fulltransdata fmaxtemp

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmaxtemp = 1.0

**Arg34: iFulltransdataIequationsolv**

Description: option for fulltransdata iequationsolv

Data Type: integer

Default Value : 0

Syntax: iFulltransdataIequationsolv = 1

**Arg35: dFulltransdataFtollevel**

Description: double value of fulltransdata ftollevel

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFtollevel = 1.0

**Arg36: dFulltransdataFmultiplier**

Description: double value of fulltransdata fmultiplier

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmultiplier = 1.0

**Arg37: bFulltransdataBsignleprecision**

Description: enable or disable feature fulltransdata bsignleprecision

Data Type: bool

Default Value : False

Syntax: bFulltransdataBsignleprecision = True/False

**Arg38: bFulltransdataBmemorysave**

Description: enable or disable feature fulltransdata bmemorysave

Data Type: bool

Default Value : False

Syntax: bFulltransdataBmemorysave = True/False

**Arg39: dFulltransdataFtempdiff**

Description: double value of fulltransdata ftempdiff

Data Type: double

Default Value : 1.1

Syntax: dFulltransdataFtempdiff = 1.0

**Arg40: dHarmonicdataFstartfreq**

Description: double value of harmonicdata fstartfreq

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFstartfreq = 1.0

**Arg41: dHarmonicdataFendfreq**

Description: double value of harmonicdata fendfreq

Data Type: double

Default Value : 1.0

Syntax: dHarmonicdataFendfreq = 1.0

**Arg42: iHarmonicdataNsubsteps**

Description: option for harmonicdata nsubsteps

Data Type: integer

Default Value : 0

Syntax: iHarmonicdataNsubsteps = 1

**Arg43: dHarmonicdataFalphad**

Description: double value of harmonicdata falphad

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFalphad = 1.0

**Arg44: dHarmonicdataFbetad**

Description: double value of harmonicdata fbetad

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFbetad = 1.0

**Arg45: dHarmonicdataFdmprat**

Description: double value of harmonicdata fdmprat

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFdmprat = 1.0

**Arg46: bHarmonicdataBoutputdisplacements**

Description: enable or disable feature harmonicdata boutputdisplacements

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputdisplacements = True/False

**Arg47: bHarmonicdataBoutputstrain**

Description: enable or disable feature harmonicdata boutputstrain

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputstrain = True/False

**Arg48: bHarmonicdataBoutputstress**

Description: enable or disable feature harmonicdata boutputstress

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputstress = True/False

**Arg49: iLCId**

Description: option for l c id

Data Type: integer

Default Value : 0

Syntax: iLCId = 1

**Arg50: iModeShape**

Description: option for mode shape

Data Type: integer

Default Value : 0

Syntax: iModeShape = 1

**Arg51: iModaldataImodemethod**

Description: option for modaldata imodemethod

Data Type: integer

Default Value : 0

Syntax: iModaldataImodemethod = 1

**Arg52: iModaldataIextractnum**

Description: option for modaldata iextractnum

Data Type: integer

Default Value : 1

Syntax: iModaldataIextractnum = 1

**Arg53: bModaldataBexpandshape**

Description: enable or disable feature modaldata bexpandshape

Data Type: bool

Default Value : True

Syntax: bModaldataBexpandshape = True/False

**Arg54: iModaldataIexpandnum**

Description: option for modaldata iexpandnum

Data Type: integer

Default Value : 0

Syntax: iModaldataIexpandnum = 1

**Arg55: bModaldataBuseapprox**

Description: enable or disable feature modaldata buseapprox

Data Type: bool

Default Value : False

Syntax: bModaldataBuseapprox = True/False

**Arg56: bModaldataBinclprsseff**

Description: enable or disable feature modaldata binclprsseff

Data Type: bool

Default Value : False

Syntax: bModaldataBinclprsseff = True/False

**Arg57: bModaldataBmemorysave**

Description: enable or disable feature modaldata bmemorysave

Data Type: bool

Default Value : False

Syntax: bModaldataBmemorysave = True/False

**Arg58: bModaldataBrsvec**

Description: enable or disable feature modaldata brsvec

Data Type: bool

Default Value : False

Syntax: bModaldataBrsvec = True/False

**Arg59: bModaldataBoutputdisplacements**

Description: enable or disable feature modaldata boutputdisplacements

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputdisplacements = True/False

**Arg60: bModaldataBoutputstrain**

Description: enable or disable feature modaldata boutputstrain

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputstrain = True/False

**Arg61: bModaldataBoutputstress**

Description: enable or disable feature modaldata boutputstress

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputstress = True/False

**Arg62: iReduceddataIprintnum**

Description: option for reduceddata iprintnum

Data Type: integer

Default Value : 0

Syntax: iReduceddataIprintnum = 1

**Arg63: bSsdataBmemorysave**

Description: enable or disable feature ssdata bmemorysave

Data Type: bool

Default Value : False

Syntax: bSsdataBmemorysave = True/False

**Arg64: bSsdataBoutputheatflux**

Description: enable or disable feature ssdata boutputheatflux

Data Type: bool

Default Value : False

Syntax: bSsdataBoutputheatflux = True/False

**Arg65: bSsdataBoutputtemperature**

Description: enable or disable feature ssdata boutputtemperature

Data Type: bool

Default Value : False

Syntax: bSsdataBoutputtemperature = True/False

**Arg66: bSsdataBpivotscheck**

Description: enable or disable feature ssdata bpivotscheck

Data Type: bool

Default Value : True

Syntax: bSsdataBpivotscheck = True/False

**Arg67: bSsdataBsignleprecision**

Description: enable or disable feature ssdata bsignleprecision

Data Type: bool

Default Value : False

Syntax: bSsdataBsignleprecision = True/False

**Arg68: dSsdataFmultiplier**

Description: double value of ssdata fmultiplier

Data Type: double

Default Value : 0.0

Syntax: dSsdataFmultiplier = 1.0

**Arg69: dSsdataFtempdiff**

Description: double value of ssdata ftempdiff

Data Type: double

Default Value : 0.0

Syntax: dSsdataFtempdiff = 1.0

**Arg70: dSsdataFtollevel**

Description: double value of ssdata ftollevel

Data Type: double

Default Value : 0.0

Syntax: dSsdataFtollevel = 1.0

**Arg71: iSsdataIadaptivedes**

Description: option for ssdata iadaptivedes

Data Type: integer

Default Value : 0

Syntax: iSsdataIadaptivedes = 1

**Arg72: iSsdataIequationsolv**

Description: option for ssdata iequationsolv

Data Type: integer

Default Value : 0

Syntax: iSsdataIequationsolv = 1

**Arg73: iSsdataInpoption**

Description: option for ssdata inpoption

Data Type: integer

Default Value : 0

Syntax: iSsdataInpoption = 1

**Arg74: strAnsysVersion**

Description: definition string of input ansys version

Data Type: string

Default Value : ""

Syntax: strAnsysVersion = "string input"

**Arg75: strCommandLineOption**

Description: definition string of input command line option

Data Type: string

Default Value : ""

Syntax: strCommandLineOption = "string input"

**Arg76: bOutputSOLVE**

Description: enable or disable feature output s o l v e

Data Type: bool

Default Value : False

Syntax: bOutputSOLVE = True/False

**Arg77: iSubspacedataIrigidmode**

Description: option for subspacedata irigidmode

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIrigidmode = 1

**Arg78: iSubspacedataIworksize**

Description: option for subspacedata iworksize

Data Type: integer

Default Value : 8

Syntax: iSubspacedataIworksize = 1

**Arg79: iSubspacedataInpadnum**

Description: option for subspacedata inpadnum

Data Type: integer

Default Value : 4

Syntax: iSubspacedataInpadnum = 1

**Arg80: iSubspacedataIblocknum**

Description: option for subspacedata iblocknum

Data Type: integer

Default Value : 5

Syntax: iSubspacedataIblocknum = 1

**Arg81: iSubspacedataImaxiteratcnt**

Description: option for subspacedata imaxiteratcnt

Data Type: integer

Default Value : 0

Syntax: iSubspacedataImaxiteratcnt = 1

**Arg82: iSubspacedataIminnshift**

Description: option for subspacedata iminnshift

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIminnshift = 1

**Arg83: iSubspacedataIseqcheck**

Description: option for subspacedata iseqcheck

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIseqcheck = 1

**Arg84: bTransientdataBtraneffect**

Description: enable or disable feature transientdata btraneffect

Data Type: bool

Default Value : True

Syntax: bTransientdataBtraneffect = True/False

**Arg85: iTransientdataIloadingtype**

Description: option for transientdata iloadingtype

Data Type: integer

Default Value : 0

Syntax: iTransientdataIloadingtype = 1

**Arg86: dTransientdataFmassmatrixmult**

Description: double value of transientdata fmassmatrixmult

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFmassmatrixmult = 1.0

**Arg87: dTransientdataFstiffmatrixmult**

Description: double value of transientdata fstiffmatrixmult

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFstiffmatrixmult = 1.0

**Arg88: bTransientdataBmidstep**

Description: enable or disable feature transientdata bmidstep

Data Type: bool

Default Value : False

Syntax: bTransientdataBmidstep = True/False

**Arg89: dTransientdataFtolerancebisection**

Description: double value of transientdata ftolerancebisection

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFtolerancebisection = 1.0

**Arg90: dTransientdataFtolerancetimestep**

Description: double value of transientdata ftolerancetimestep

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFtolerancetimestep = 1.0

**Arg91: iTransientdataItimeinteralgor**

Description: option for transientdata itimeinteralgor

Data Type: integer

Default Value : 0

Syntax: iTransientdataItimeinteralgor = 1

**Arg92: iTransientdataItimeinter**

Description: option for transientdata itimeinter

Data Type: integer

Default Value : 0

Syntax: iTransientdataItimeinter = 1

**Arg93: dTransientdataFgamma**

Description: double value of transientdata fgamma

Data Type: double

Default Value : 0.005

Syntax: dTransientdataFgamma = 1.0

**Arg94: dTransientdataFalpha**

Description: double value of transientdata falpha

Data Type: double

Default Value : 0.25250625

Syntax: dTransientdataFalpha = 1.0

**Arg95: dTransientdataFdelta**

Description: double value of transientdata fdelta

Data Type: double

Default Value : 0.505

Syntax: dTransientdataFdelta = 1.0

**Arg96: dTransientdataFalphaf**

Description: double value of transientdata falphaf

Data Type: double

Default Value : 0.005

Syntax: dTransientdataFalphaf = 1.0

**Arg97: dTransientdataFalpham**

Description: double value of transientdata falpham

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFalpham = 1.0

**Arg98: bTransientdataBoutputtemperature**

Description: enable or disable feature transientdata boutputtemperature

Data Type: bool

Default Value : False

Syntax: bTransientdataBoutputtemperature = True/False

**Arg99: bTransientdataBoutputheatflux**

Description: enable or disable feature transientdata boutputheatflux

Data Type: bool

Default Value : False

Syntax: bTransientdataBoutputheatflux = True/False

**Arg100: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Ansys.HeadTransferSteady(strName="", iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None)

```

==========================================================

# Analysis.Ansys.LinearStatic

## Wrapper Macro

Ansys_LinearStaticStructural(...)

## Ribbon-GUI-Location

Analysis > Ansys > LinearStatic

## Command Description

Create and export Ansys job for Linear Static Structural

## Argument List

**Arg1: strJobName**

Description: definition string of input job name

Data Type: string

Default Value : ""

Syntax: strJobName = "string input"

**Arg2: iJobdataAnatype**

Description: option for job data anatype

Data Type: integer

Default Value : 0

Syntax: iJobdataAnatype = 1

**Arg3: iJobdataSoltype**

Description: option for job data solution type

Data Type: integer

Default Value : 0

Syntax: iJobdataSoltype = 1

**Arg4: strJobdataJobname**

Description: definition string of input job data job name

Data Type: string

Default Value : "Job1"

Syntax: strJobdataJobname = "string input"

**Arg5: strJobdataJobdescription**

Description: definition string of input job data jobdescription

Data Type: string

Default Value : ""

Syntax: strJobdataJobdescription = "string input"

**Arg6: bBasicdataBoutputdisplacements**

Description: enable or disable feature basic data boutputdisplacements

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputdisplacements = True/False

**Arg7: bBasicdataBoutputreactionload**

Description: enable or disable feature basic data boutputreactionload

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputreactionload = True/False

**Arg8: bBasicdataBoutputstrain**

Description: enable or disable feature basic data boutputstrain

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputstrain = True/False

**Arg9: bBasicdataBoutputstress**

Description: enable or disable feature basic data boutputstress

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputstress = True/False

**Arg10: iBasicdataIanalysisopt**

Description: option for basic data ianalysisopt

Data Type: integer

Default Value : 0

Syntax: iBasicdataIanalysisopt = 1

**Arg11: bBasicdataBcalPressEffects**

Description: enable or disable feature basic data caculation press effects

Data Type: bool

Default Value : False

Syntax: bBasicdataBcalPressEffects = True/False

**Arg12: dBasicdataFunitem**

Description: double value of basic data funitem

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFunitem = 1.0

**Arg13: dBasicdataFreftemp**

Description: double value of basic data freftemp

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFreftemp = 1.0

**Arg14: dBasicdataFendloadtime**

Description: double value of basic data fendloadtime

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFendloadtime = 1.0

**Arg15: iBasicdataItimestep**

Description: option for basic data time step value

Data Type: integer

Default Value : 0

Syntax: iBasicdataItimestep = 1

**Arg16: iBasicdataIstepchosen**

Description: option for basic data step chosen value

Data Type: integer

Default Value : 0

Syntax: iBasicdataIstepchosen = 1

**Arg17: iBasicdataIsubstepnum**

Description: option for basic data substep number

Data Type: integer

Default Value : 0

Syntax: iBasicdataIsubstepnum = 1

**Arg18: iBasicdataImaxsubstep**

Description: option for basic data maximum substep value

Data Type: integer

Default Value : 0

Syntax: iBasicdataImaxsubstep = 1

**Arg19: iBasicdataIminstepnum**

Description: option for basic data minimum step number

Data Type: integer

Default Value : 0

Syntax: iBasicdataIminstepnum = 1

**Arg20: dBasicdataFtimestepsize**

Description: double value of basic data time step size

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFtimestepsize = 1.0

**Arg21: dBasicdataFmintimestep**

Description: double value of basic data minimum time step

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFmintimestep = 1.0

**Arg22: dBasicdataFmaxtimestep**

Description: double value of basic data maximum time step

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFmaxtimestep = 1.0

**Arg23: iBasicdataIwritereslutfre**

Description: option for basic data write result frequency

Data Type: integer

Default Value : 1

Syntax: iBasicdataIwritereslutfre = 1

**Arg24: iBasicdataIn**

Description: option for basic data in

Data Type: integer

Default Value : 1

Syntax: iBasicdataIn = 1

**Arg25: bRunAPDL**

Description: enable or disable feature run APDL

Data Type: bool

Default Value : False

Syntax: bRunAPDL = True/False

**Arg26: bWriteResultDB**

Description: enable or disable feature write result database

Data Type: bool

Default Value : False

Syntax: bWriteResultDB = True/False

**Arg27: dFEndFreq**

Description: double value of end frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dFEndFreq = 1.0

**Arg28: dFStartFreq**

Description: double value of start frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dFStartFreq = 1.0

**Arg29: iFulltransdataIsolutionoption**

Description: option for fulltransdata isolutionoption

Data Type: integer

Default Value : 0

Syntax: iFulltransdataIsolutionoption = 1

**Arg30: dFulltransdataFpropchange**

Description: double value of fulltransdata fpropchange

Data Type: double

Default Value : 0.05

Syntax: dFulltransdataFpropchange = 1.0

**Arg31: iFulltransdataIpointnum**

Description: option for fulltransdata ipointnum

Data Type: integer

Default Value : 64

Syntax: iFulltransdataIpointnum = 1

**Arg32: dFulltransdataFmintemp**

Description: double value of fulltransdata fmintemp

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmintemp = 1.0

**Arg33: dFulltransdataFmaxtemp**

Description: double value of fulltransdata fmaxtemp

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmaxtemp = 1.0

**Arg34: iFulltransdataIequationsolv**

Description: option for fulltransdata iequationsolv

Data Type: integer

Default Value : 0

Syntax: iFulltransdataIequationsolv = 1

**Arg35: dFulltransdataFtollevel**

Description: double value of fulltransdata ftollevel

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFtollevel = 1.0

**Arg36: dFulltransdataFmultiplier**

Description: double value of fulltransdata fmultiplier

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmultiplier = 1.0

**Arg37: bFulltransdataBsignleprecision**

Description: enable or disable feature fulltransdata bsignleprecision

Data Type: bool

Default Value : False

Syntax: bFulltransdataBsignleprecision = True/False

**Arg38: bFulltransdataBmemorysave**

Description: enable or disable feature fulltransdata bmemorysave

Data Type: bool

Default Value : False

Syntax: bFulltransdataBmemorysave = True/False

**Arg39: dFulltransdataFtempdiff**

Description: double value of fulltransdata ftempdiff

Data Type: double

Default Value : 1.1

Syntax: dFulltransdataFtempdiff = 1.0

**Arg40: dHarmonicdataFstartfreq**

Description: double value of harmonicdata fstartfreq

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFstartfreq = 1.0

**Arg41: dHarmonicdataFendfreq**

Description: double value of harmonicdata fendfreq

Data Type: double

Default Value : 1.0

Syntax: dHarmonicdataFendfreq = 1.0

**Arg42: iHarmonicdataNsubsteps**

Description: option for harmonicdata nsubsteps

Data Type: integer

Default Value : 0

Syntax: iHarmonicdataNsubsteps = 1

**Arg43: dHarmonicdataFalphad**

Description: double value of harmonicdata falphad

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFalphad = 1.0

**Arg44: dHarmonicdataFbetad**

Description: double value of harmonicdata fbetad

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFbetad = 1.0

**Arg45: dHarmonicdataFdmprat**

Description: double value of harmonicdata fdmprat

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFdmprat = 1.0

**Arg46: bHarmonicdataBoutputdisplacements**

Description: enable or disable feature harmonicdata boutputdisplacements

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputdisplacements = True/False

**Arg47: bHarmonicdataBoutputstrain**

Description: enable or disable feature harmonicdata boutputstrain

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputstrain = True/False

**Arg48: bHarmonicdataBoutputstress**

Description: enable or disable feature harmonicdata boutputstress

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputstress = True/False

**Arg49: iLCId**

Description: option for l c id

Data Type: integer

Default Value : 0

Syntax: iLCId = 1

**Arg50: iModeShape**

Description: option for mode shape

Data Type: integer

Default Value : 0

Syntax: iModeShape = 1

**Arg51: iModaldataImodemethod**

Description: option for modaldata imodemethod

Data Type: integer

Default Value : 0

Syntax: iModaldataImodemethod = 1

**Arg52: iModaldataIextractnum**

Description: option for modaldata iextractnum

Data Type: integer

Default Value : 1

Syntax: iModaldataIextractnum = 1

**Arg53: bModaldataBexpandshape**

Description: enable or disable feature modaldata bexpandshape

Data Type: bool

Default Value : True

Syntax: bModaldataBexpandshape = True/False

**Arg54: iModaldataIexpandnum**

Description: option for modaldata iexpandnum

Data Type: integer

Default Value : 0

Syntax: iModaldataIexpandnum = 1

**Arg55: bModaldataBuseapprox**

Description: enable or disable feature modaldata buseapprox

Data Type: bool

Default Value : False

Syntax: bModaldataBuseapprox = True/False

**Arg56: bModaldataBinclprsseff**

Description: enable or disable feature modaldata binclprsseff

Data Type: bool

Default Value : False

Syntax: bModaldataBinclprsseff = True/False

**Arg57: bModaldataBmemorysave**

Description: enable or disable feature modaldata bmemorysave

Data Type: bool

Default Value : False

Syntax: bModaldataBmemorysave = True/False

**Arg58: bModaldataBrsvec**

Description: enable or disable feature modaldata brsvec

Data Type: bool

Default Value : False

Syntax: bModaldataBrsvec = True/False

**Arg59: bModaldataBoutputdisplacements**

Description: enable or disable feature modaldata boutputdisplacements

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputdisplacements = True/False

**Arg60: bModaldataBoutputstrain**

Description: enable or disable feature modaldata boutputstrain

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputstrain = True/False

**Arg61: bModaldataBoutputstress**

Description: enable or disable feature modaldata boutputstress

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputstress = True/False

**Arg62: iReduceddataIprintnum**

Description: option for reduceddata iprintnum

Data Type: integer

Default Value : 0

Syntax: iReduceddataIprintnum = 1

**Arg63: bSsdataBmemorysave**

Description: enable or disable feature ssdata bmemorysave

Data Type: bool

Default Value : False

Syntax: bSsdataBmemorysave = True/False

**Arg64: bSsdataBoutputheatflux**

Description: enable or disable feature ssdata boutputheatflux

Data Type: bool

Default Value : False

Syntax: bSsdataBoutputheatflux = True/False

**Arg65: bSsdataBoutputtemperature**

Description: enable or disable feature ssdata boutputtemperature

Data Type: bool

Default Value : False

Syntax: bSsdataBoutputtemperature = True/False

**Arg66: bSsdataBpivotscheck**

Description: enable or disable feature ssdata bpivotscheck

Data Type: bool

Default Value : True

Syntax: bSsdataBpivotscheck = True/False

**Arg67: bSsdataBsignleprecision**

Description: enable or disable feature ssdata bsignleprecision

Data Type: bool

Default Value : False

Syntax: bSsdataBsignleprecision = True/False

**Arg68: dSsdataFmultiplier**

Description: double value of ssdata fmultiplier

Data Type: double

Default Value : 0.0

Syntax: dSsdataFmultiplier = 1.0

**Arg69: dSsdataFtempdiff**

Description: double value of ssdata ftempdiff

Data Type: double

Default Value : 0.0

Syntax: dSsdataFtempdiff = 1.0

**Arg70: dSsdataFtollevel**

Description: double value of ssdata ftollevel

Data Type: double

Default Value : 0.0

Syntax: dSsdataFtollevel = 1.0

**Arg71: iSsdataIadaptivedes**

Description: option for ssdata iadaptivedes

Data Type: integer

Default Value : 0

Syntax: iSsdataIadaptivedes = 1

**Arg72: iSsdataIequationsolv**

Description: option for ssdata iequationsolv

Data Type: integer

Default Value : 0

Syntax: iSsdataIequationsolv = 1

**Arg73: iSsdataInpoption**

Description: option for ssdata inpoption

Data Type: integer

Default Value : 0

Syntax: iSsdataInpoption = 1

**Arg74: strAnsysVersion**

Description: definition string of input ansys version

Data Type: string

Default Value : ""

Syntax: strAnsysVersion = "string input"

**Arg75: strCommandLineOption**

Description: definition string of input command line option

Data Type: string

Default Value : ""

Syntax: strCommandLineOption = "string input"

**Arg76: bOutputSOLVE**

Description: enable or disable feature output s o l v e

Data Type: bool

Default Value : False

Syntax: bOutputSOLVE = True/False

**Arg77: iSubspacedataIrigidmode**

Description: option for subspacedata irigidmode

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIrigidmode = 1

**Arg78: iSubspacedataIworksize**

Description: option for subspacedata iworksize

Data Type: integer

Default Value : 8

Syntax: iSubspacedataIworksize = 1

**Arg79: iSubspacedataInpadnum**

Description: option for subspacedata inpadnum

Data Type: integer

Default Value : 4

Syntax: iSubspacedataInpadnum = 1

**Arg80: iSubspacedataIblocknum**

Description: option for subspacedata iblocknum

Data Type: integer

Default Value : 5

Syntax: iSubspacedataIblocknum = 1

**Arg81: iSubspacedataImaxiteratcnt**

Description: option for subspacedata imaxiteratcnt

Data Type: integer

Default Value : 0

Syntax: iSubspacedataImaxiteratcnt = 1

**Arg82: iSubspacedataIminnshift**

Description: option for subspacedata iminnshift

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIminnshift = 1

**Arg83: iSubspacedataIseqcheck**

Description: option for subspacedata iseqcheck

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIseqcheck = 1

**Arg84: bTransientdataBtraneffect**

Description: enable or disable feature transientdata btraneffect

Data Type: bool

Default Value : True

Syntax: bTransientdataBtraneffect = True/False

**Arg85: iTransientdataIloadingtype**

Description: option for transientdata iloadingtype

Data Type: integer

Default Value : 0

Syntax: iTransientdataIloadingtype = 1

**Arg86: dTransientdataFmassmatrixmult**

Description: double value of transientdata fmassmatrixmult

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFmassmatrixmult = 1.0

**Arg87: dTransientdataFstiffmatrixmult**

Description: double value of transientdata fstiffmatrixmult

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFstiffmatrixmult = 1.0

**Arg88: bTransientdataBmidstep**

Description: enable or disable feature transientdata bmidstep

Data Type: bool

Default Value : False

Syntax: bTransientdataBmidstep = True/False

**Arg89: dTransientdataFtolerancebisection**

Description: double value of transientdata ftolerancebisection

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFtolerancebisection = 1.0

**Arg90: dTransientdataFtolerancetimestep**

Description: double value of transientdata ftolerancetimestep

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFtolerancetimestep = 1.0

**Arg91: iTransientdataItimeinteralgor**

Description: option for transientdata itimeinteralgor

Data Type: integer

Default Value : 0

Syntax: iTransientdataItimeinteralgor = 1

**Arg92: iTransientdataItimeinter**

Description: option for transientdata itimeinter

Data Type: integer

Default Value : 0

Syntax: iTransientdataItimeinter = 1

**Arg93: dTransientdataFgamma**

Description: double value of transientdata fgamma

Data Type: double

Default Value : 0.005

Syntax: dTransientdataFgamma = 1.0

**Arg94: dTransientdataFalpha**

Description: double value of transientdata falpha

Data Type: double

Default Value : 0.25250625

Syntax: dTransientdataFalpha = 1.0

**Arg95: dTransientdataFdelta**

Description: double value of transientdata fdelta

Data Type: double

Default Value : 0.505

Syntax: dTransientdataFdelta = 1.0

**Arg96: dTransientdataFalphaf**

Description: double value of transientdata falphaf

Data Type: double

Default Value : 0.005

Syntax: dTransientdataFalphaf = 1.0

**Arg97: dTransientdataFalpham**

Description: double value of transientdata falpham

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFalpham = 1.0

**Arg98: bTransientdataBoutputtemperature**

Description: enable or disable feature transientdata boutputtemperature

Data Type: bool

Default Value : False

Syntax: bTransientdataBoutputtemperature = True/False

**Arg99: bTransientdataBoutputheatflux**

Description: enable or disable feature transientdata boutputheatflux

Data Type: bool

Default Value : False

Syntax: bTransientdataBoutputheatflux = True/False

**Arg100: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg101: strFileName**

Description: definition string of input file name

Data Type: string

Default Value : ""

Syntax: strFileName = "string input"

**Arg102: crAnsysJob**

Description: entity in database model with type ansys job

Data Type: cursor

Default Value : None

Syntax: crAnsysJob = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Ansys.LinearStatic(strJobName="", iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None, strFileName="", crAnsysJob=None)

```

==========================================================

# Analysis.Ansys.NormalModes

## Wrapper Macro

Ansys_NormalModesStructural(...)

## Ribbon-GUI-Location

Analysis > Ansys > NormalModes

## Command Description

Create and export Ansys job for Normal Modes Structural

## Argument List

**Arg1: strJobName**

Description: definition string of input job name

Data Type: string

Default Value : ""

Syntax: strJobName = "string input"

**Arg2: iJobdataAnatype**

Description: option for job data anatype

Data Type: integer

Default Value : 0

Syntax: iJobdataAnatype = 1

**Arg3: iJobdataSoltype**

Description: option for job data solution type

Data Type: integer

Default Value : 0

Syntax: iJobdataSoltype = 1

**Arg4: strJobdataJobname**

Description: definition string of input job data job name

Data Type: string

Default Value : "Job1"

Syntax: strJobdataJobname = "string input"

**Arg5: strJobdataJobdescription**

Description: definition string of input job data jobdescription

Data Type: string

Default Value : ""

Syntax: strJobdataJobdescription = "string input"

**Arg6: bBasicdataBoutputdisplacements**

Description: enable or disable feature basic data boutputdisplacements

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputdisplacements = True/False

**Arg7: bBasicdataBoutputreactionload**

Description: enable or disable feature basic data boutputreactionload

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputreactionload = True/False

**Arg8: bBasicdataBoutputstrain**

Description: enable or disable feature basic data boutputstrain

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputstrain = True/False

**Arg9: bBasicdataBoutputstress**

Description: enable or disable feature basic data boutputstress

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputstress = True/False

**Arg10: iBasicdataIanalysisopt**

Description: option for basic data ianalysisopt

Data Type: integer

Default Value : 0

Syntax: iBasicdataIanalysisopt = 1

**Arg11: bBasicdataBcalPressEffects**

Description: enable or disable feature basic data caculation press effects

Data Type: bool

Default Value : False

Syntax: bBasicdataBcalPressEffects = True/False

**Arg12: dBasicdataFunitem**

Description: double value of basic data funitem

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFunitem = 1.0

**Arg13: dBasicdataFreftemp**

Description: double value of basic data freftemp

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFreftemp = 1.0

**Arg14: dBasicdataFendloadtime**

Description: double value of basic data fendloadtime

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFendloadtime = 1.0

**Arg15: iBasicdataItimestep**

Description: option for basic data time step value

Data Type: integer

Default Value : 0

Syntax: iBasicdataItimestep = 1

**Arg16: iBasicdataIstepchosen**

Description: option for basic data step chosen value

Data Type: integer

Default Value : 0

Syntax: iBasicdataIstepchosen = 1

**Arg17: iBasicdataIsubstepnum**

Description: option for basic data substep number

Data Type: integer

Default Value : 0

Syntax: iBasicdataIsubstepnum = 1

**Arg18: iBasicdataImaxsubstep**

Description: option for basic data maximum substep value

Data Type: integer

Default Value : 0

Syntax: iBasicdataImaxsubstep = 1

**Arg19: iBasicdataIminstepnum**

Description: option for basic data minimum step number

Data Type: integer

Default Value : 0

Syntax: iBasicdataIminstepnum = 1

**Arg20: dBasicdataFtimestepsize**

Description: double value of basic data time step size

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFtimestepsize = 1.0

**Arg21: dBasicdataFmintimestep**

Description: double value of basic data minimum time step

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFmintimestep = 1.0

**Arg22: dBasicdataFmaxtimestep**

Description: double value of basic data maximum time step

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFmaxtimestep = 1.0

**Arg23: iBasicdataIwritereslutfre**

Description: option for basic data write result frequency

Data Type: integer

Default Value : 1

Syntax: iBasicdataIwritereslutfre = 1

**Arg24: iBasicdataIn**

Description: option for basic data in

Data Type: integer

Default Value : 1

Syntax: iBasicdataIn = 1

**Arg25: bRunAPDL**

Description: enable or disable feature run APDL

Data Type: bool

Default Value : False

Syntax: bRunAPDL = True/False

**Arg26: bWriteResultDB**

Description: enable or disable feature write result database

Data Type: bool

Default Value : False

Syntax: bWriteResultDB = True/False

**Arg27: dFEndFreq**

Description: double value of end frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dFEndFreq = 1.0

**Arg28: dFStartFreq**

Description: double value of start frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dFStartFreq = 1.0

**Arg29: iFulltransdataIsolutionoption**

Description: option for fulltransdata isolutionoption

Data Type: integer

Default Value : 0

Syntax: iFulltransdataIsolutionoption = 1

**Arg30: dFulltransdataFpropchange**

Description: double value of fulltransdata fpropchange

Data Type: double

Default Value : 0.05

Syntax: dFulltransdataFpropchange = 1.0

**Arg31: iFulltransdataIpointnum**

Description: option for fulltransdata ipointnum

Data Type: integer

Default Value : 64

Syntax: iFulltransdataIpointnum = 1

**Arg32: dFulltransdataFmintemp**

Description: double value of fulltransdata fmintemp

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmintemp = 1.0

**Arg33: dFulltransdataFmaxtemp**

Description: double value of fulltransdata fmaxtemp

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmaxtemp = 1.0

**Arg34: iFulltransdataIequationsolv**

Description: option for fulltransdata iequationsolv

Data Type: integer

Default Value : 0

Syntax: iFulltransdataIequationsolv = 1

**Arg35: dFulltransdataFtollevel**

Description: double value of fulltransdata ftollevel

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFtollevel = 1.0

**Arg36: dFulltransdataFmultiplier**

Description: double value of fulltransdata fmultiplier

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmultiplier = 1.0

**Arg37: bFulltransdataBsignleprecision**

Description: enable or disable feature fulltransdata bsignleprecision

Data Type: bool

Default Value : False

Syntax: bFulltransdataBsignleprecision = True/False

**Arg38: bFulltransdataBmemorysave**

Description: enable or disable feature fulltransdata bmemorysave

Data Type: bool

Default Value : False

Syntax: bFulltransdataBmemorysave = True/False

**Arg39: dFulltransdataFtempdiff**

Description: double value of fulltransdata ftempdiff

Data Type: double

Default Value : 1.1

Syntax: dFulltransdataFtempdiff = 1.0

**Arg40: dHarmonicdataFstartfreq**

Description: double value of harmonicdata fstartfreq

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFstartfreq = 1.0

**Arg41: dHarmonicdataFendfreq**

Description: double value of harmonicdata fendfreq

Data Type: double

Default Value : 1.0

Syntax: dHarmonicdataFendfreq = 1.0

**Arg42: iHarmonicdataNsubsteps**

Description: option for harmonicdata nsubsteps

Data Type: integer

Default Value : 0

Syntax: iHarmonicdataNsubsteps = 1

**Arg43: dHarmonicdataFalphad**

Description: double value of harmonicdata falphad

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFalphad = 1.0

**Arg44: dHarmonicdataFbetad**

Description: double value of harmonicdata fbetad

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFbetad = 1.0

**Arg45: dHarmonicdataFdmprat**

Description: double value of harmonicdata fdmprat

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFdmprat = 1.0

**Arg46: bHarmonicdataBoutputdisplacements**

Description: enable or disable feature harmonicdata boutputdisplacements

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputdisplacements = True/False

**Arg47: bHarmonicdataBoutputstrain**

Description: enable or disable feature harmonicdata boutputstrain

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputstrain = True/False

**Arg48: bHarmonicdataBoutputstress**

Description: enable or disable feature harmonicdata boutputstress

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputstress = True/False

**Arg49: iLCId**

Description: option for l c id

Data Type: integer

Default Value : 0

Syntax: iLCId = 1

**Arg50: iModeShape**

Description: option for mode shape

Data Type: integer

Default Value : 0

Syntax: iModeShape = 1

**Arg51: iModaldataImodemethod**

Description: option for modaldata imodemethod

Data Type: integer

Default Value : 0

Syntax: iModaldataImodemethod = 1

**Arg52: iModaldataIextractnum**

Description: option for modaldata iextractnum

Data Type: integer

Default Value : 1

Syntax: iModaldataIextractnum = 1

**Arg53: bModaldataBexpandshape**

Description: enable or disable feature modaldata bexpandshape

Data Type: bool

Default Value : True

Syntax: bModaldataBexpandshape = True/False

**Arg54: iModaldataIexpandnum**

Description: option for modaldata iexpandnum

Data Type: integer

Default Value : 0

Syntax: iModaldataIexpandnum = 1

**Arg55: bModaldataBuseapprox**

Description: enable or disable feature modaldata buseapprox

Data Type: bool

Default Value : False

Syntax: bModaldataBuseapprox = True/False

**Arg56: bModaldataBinclprsseff**

Description: enable or disable feature modaldata binclprsseff

Data Type: bool

Default Value : False

Syntax: bModaldataBinclprsseff = True/False

**Arg57: bModaldataBmemorysave**

Description: enable or disable feature modaldata bmemorysave

Data Type: bool

Default Value : False

Syntax: bModaldataBmemorysave = True/False

**Arg58: bModaldataBrsvec**

Description: enable or disable feature modaldata brsvec

Data Type: bool

Default Value : False

Syntax: bModaldataBrsvec = True/False

**Arg59: bModaldataBoutputdisplacements**

Description: enable or disable feature modaldata boutputdisplacements

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputdisplacements = True/False

**Arg60: bModaldataBoutputstrain**

Description: enable or disable feature modaldata boutputstrain

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputstrain = True/False

**Arg61: bModaldataBoutputstress**

Description: enable or disable feature modaldata boutputstress

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputstress = True/False

**Arg62: iReduceddataIprintnum**

Description: option for reduceddata iprintnum

Data Type: integer

Default Value : 0

Syntax: iReduceddataIprintnum = 1

**Arg63: bSsdataBmemorysave**

Description: enable or disable feature ssdata bmemorysave

Data Type: bool

Default Value : False

Syntax: bSsdataBmemorysave = True/False

**Arg64: bSsdataBoutputheatflux**

Description: enable or disable feature ssdata boutputheatflux

Data Type: bool

Default Value : False

Syntax: bSsdataBoutputheatflux = True/False

**Arg65: bSsdataBoutputtemperature**

Description: enable or disable feature ssdata boutputtemperature

Data Type: bool

Default Value : False

Syntax: bSsdataBoutputtemperature = True/False

**Arg66: bSsdataBpivotscheck**

Description: enable or disable feature ssdata bpivotscheck

Data Type: bool

Default Value : True

Syntax: bSsdataBpivotscheck = True/False

**Arg67: bSsdataBsignleprecision**

Description: enable or disable feature ssdata bsignleprecision

Data Type: bool

Default Value : False

Syntax: bSsdataBsignleprecision = True/False

**Arg68: dSsdataFmultiplier**

Description: double value of ssdata fmultiplier

Data Type: double

Default Value : 0.0

Syntax: dSsdataFmultiplier = 1.0

**Arg69: dSsdataFtempdiff**

Description: double value of ssdata ftempdiff

Data Type: double

Default Value : 0.0

Syntax: dSsdataFtempdiff = 1.0

**Arg70: dSsdataFtollevel**

Description: double value of ssdata ftollevel

Data Type: double

Default Value : 0.0

Syntax: dSsdataFtollevel = 1.0

**Arg71: iSsdataIadaptivedes**

Description: option for ssdata iadaptivedes

Data Type: integer

Default Value : 0

Syntax: iSsdataIadaptivedes = 1

**Arg72: iSsdataIequationsolv**

Description: option for ssdata iequationsolv

Data Type: integer

Default Value : 0

Syntax: iSsdataIequationsolv = 1

**Arg73: iSsdataInpoption**

Description: option for ssdata inpoption

Data Type: integer

Default Value : 0

Syntax: iSsdataInpoption = 1

**Arg74: strAnsysVersion**

Description: definition string of input ansys version

Data Type: string

Default Value : ""

Syntax: strAnsysVersion = "string input"

**Arg75: strCommandLineOption**

Description: definition string of input command line option

Data Type: string

Default Value : ""

Syntax: strCommandLineOption = "string input"

**Arg76: bOutputSOLVE**

Description: enable or disable feature output s o l v e

Data Type: bool

Default Value : False

Syntax: bOutputSOLVE = True/False

**Arg77: iSubspacedataIrigidmode**

Description: option for subspacedata irigidmode

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIrigidmode = 1

**Arg78: iSubspacedataIworksize**

Description: option for subspacedata iworksize

Data Type: integer

Default Value : 8

Syntax: iSubspacedataIworksize = 1

**Arg79: iSubspacedataInpadnum**

Description: option for subspacedata inpadnum

Data Type: integer

Default Value : 4

Syntax: iSubspacedataInpadnum = 1

**Arg80: iSubspacedataIblocknum**

Description: option for subspacedata iblocknum

Data Type: integer

Default Value : 5

Syntax: iSubspacedataIblocknum = 1

**Arg81: iSubspacedataImaxiteratcnt**

Description: option for subspacedata imaxiteratcnt

Data Type: integer

Default Value : 0

Syntax: iSubspacedataImaxiteratcnt = 1

**Arg82: iSubspacedataIminnshift**

Description: option for subspacedata iminnshift

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIminnshift = 1

**Arg83: iSubspacedataIseqcheck**

Description: option for subspacedata iseqcheck

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIseqcheck = 1

**Arg84: bTransientdataBtraneffect**

Description: enable or disable feature transientdata btraneffect

Data Type: bool

Default Value : True

Syntax: bTransientdataBtraneffect = True/False

**Arg85: iTransientdataIloadingtype**

Description: option for transientdata iloadingtype

Data Type: integer

Default Value : 0

Syntax: iTransientdataIloadingtype = 1

**Arg86: dTransientdataFmassmatrixmult**

Description: double value of transientdata fmassmatrixmult

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFmassmatrixmult = 1.0

**Arg87: dTransientdataFstiffmatrixmult**

Description: double value of transientdata fstiffmatrixmult

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFstiffmatrixmult = 1.0

**Arg88: bTransientdataBmidstep**

Description: enable or disable feature transientdata bmidstep

Data Type: bool

Default Value : False

Syntax: bTransientdataBmidstep = True/False

**Arg89: dTransientdataFtolerancebisection**

Description: double value of transientdata ftolerancebisection

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFtolerancebisection = 1.0

**Arg90: dTransientdataFtolerancetimestep**

Description: double value of transientdata ftolerancetimestep

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFtolerancetimestep = 1.0

**Arg91: iTransientdataItimeinteralgor**

Description: option for transientdata itimeinteralgor

Data Type: integer

Default Value : 0

Syntax: iTransientdataItimeinteralgor = 1

**Arg92: iTransientdataItimeinter**

Description: option for transientdata itimeinter

Data Type: integer

Default Value : 0

Syntax: iTransientdataItimeinter = 1

**Arg93: dTransientdataFgamma**

Description: double value of transientdata fgamma

Data Type: double

Default Value : 0.005

Syntax: dTransientdataFgamma = 1.0

**Arg94: dTransientdataFalpha**

Description: double value of transientdata falpha

Data Type: double

Default Value : 0.25250625

Syntax: dTransientdataFalpha = 1.0

**Arg95: dTransientdataFdelta**

Description: double value of transientdata fdelta

Data Type: double

Default Value : 0.505

Syntax: dTransientdataFdelta = 1.0

**Arg96: dTransientdataFalphaf**

Description: double value of transientdata falphaf

Data Type: double

Default Value : 0.005

Syntax: dTransientdataFalphaf = 1.0

**Arg97: dTransientdataFalpham**

Description: double value of transientdata falpham

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFalpham = 1.0

**Arg98: bTransientdataBoutputtemperature**

Description: enable or disable feature transientdata boutputtemperature

Data Type: bool

Default Value : False

Syntax: bTransientdataBoutputtemperature = True/False

**Arg99: bTransientdataBoutputheatflux**

Description: enable or disable feature transientdata boutputheatflux

Data Type: bool

Default Value : False

Syntax: bTransientdataBoutputheatflux = True/False

**Arg100: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg101: strFileName**

Description: definition string of input file name

Data Type: string

Default Value : ""

Syntax: strFileName = "string input"

**Arg102: crAnsysJob**

Description: entity in database model with type ansys job

Data Type: cursor

Default Value : None

Syntax: crAnsysJob = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Ansys.NormalModes(strJobName="", iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None, strFileName="", crAnsysJob=None)

```

==========================================================

# Analysis.Ansys.Harmonic

## Wrapper Macro

Ansys_HarmonicStructural(...)

## Ribbon-GUI-Location

Analysis > Ansys > Harmonic

## Command Description

Create and export Ansys job for Harmonic Structural

## Argument List

**Arg1: strJobName**

Description: definition string of input job name

Data Type: string

Default Value : ""

Syntax: strJobName = "string input"

**Arg2: iJobdataAnatype**

Description: option for job data anatype

Data Type: integer

Default Value : 0

Syntax: iJobdataAnatype = 1

**Arg3: iJobdataSoltype**

Description: option for job data solution type

Data Type: integer

Default Value : 0

Syntax: iJobdataSoltype = 1

**Arg4: strJobdataJobname**

Description: definition string of input job data job name

Data Type: string

Default Value : "Job1"

Syntax: strJobdataJobname = "string input"

**Arg5: strJobdataJobdescription**

Description: definition string of input job data job description

Data Type: string

Default Value : ""

Syntax: strJobdataJobdescription = "string input"

**Arg6: bBasicdataBoutputdisplacements**

Description: enable or disable feature basic data output displacements

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputdisplacements = True/False

**Arg7: bBasicdataBoutputreactionload**

Description: enable or disable feature basic data output reaction load

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputreactionload = True/False

**Arg8: bBasicdataBoutputstrain**

Description: enable or disable feature basic data output strain

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputstrain = True/False

**Arg9: bBasicdataBoutputstress**

Description: enable or disable feature basic data output stress

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputstress = True/False

**Arg10: iBasicdataIanalysisopt**

Description: option for basic data ianalysisopt

Data Type: integer

Default Value : 0

Syntax: iBasicdataIanalysisopt = 1

**Arg11: bBasicdataBcalPressEffects**

Description: enable or disable feature basic data caculation press effects

Data Type: bool

Default Value : False

Syntax: bBasicdataBcalPressEffects = True/False

**Arg12: dBasicdataFunitem**

Description: double value of basic data funitem

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFunitem = 1.0

**Arg13: dBasicdataFreftemp**

Description: double value of basic data freftemp

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFreftemp = 1.0

**Arg14: dBasicdataFendloadtime**

Description: double value of basic data fendloadtime

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFendloadtime = 1.0

**Arg15: iBasicdataItimestep**

Description: option for basic data time step value

Data Type: integer

Default Value : 0

Syntax: iBasicdataItimestep = 1

**Arg16: iBasicdataIstepchosen**

Description: option for basic data step chosen value

Data Type: integer

Default Value : 0

Syntax: iBasicdataIstepchosen = 1

**Arg17: iBasicdataIsubstepnum**

Description: option for basic data substep number

Data Type: integer

Default Value : 0

Syntax: iBasicdataIsubstepnum = 1

**Arg18: iBasicdataImaxsubstep**

Description: option for basic data maximum substep value

Data Type: integer

Default Value : 0

Syntax: iBasicdataImaxsubstep = 1

**Arg19: iBasicdataIminstepnum**

Description: option for basic data minimum step number

Data Type: integer

Default Value : 0

Syntax: iBasicdataIminstepnum = 1

**Arg20: dBasicdataFtimestepsize**

Description: double value of basic data time step size

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFtimestepsize = 1.0

**Arg21: dBasicdataFmintimestep**

Description: double value of basic data minimum time step

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFmintimestep = 1.0

**Arg22: dBasicdataFmaxtimestep**

Description: double value of basic data maximum time step

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFmaxtimestep = 1.0

**Arg23: iBasicdataIwritereslutfre**

Description: option for basic data write result frequency

Data Type: integer

Default Value : 1

Syntax: iBasicdataIwritereslutfre = 1

**Arg24: iBasicdataIn**

Description: option for basic data in

Data Type: integer

Default Value : 1

Syntax: iBasicdataIn = 1

**Arg25: bRunAPDL**

Description: enable or disable feature run APDL

Data Type: bool

Default Value : False

Syntax: bRunAPDL = True/False

**Arg26: bWriteResultDB**

Description: enable or disable feature write result database

Data Type: bool

Default Value : False

Syntax: bWriteResultDB = True/False

**Arg27: dFEndFreq**

Description: double value of end frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dFEndFreq = 1.0

**Arg28: dFStartFreq**

Description: double value of start frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dFStartFreq = 1.0

**Arg29: iFulltransdataIsolutionoption**

Description: option for fulltransdata isolutionoption

Data Type: integer

Default Value : 0

Syntax: iFulltransdataIsolutionoption = 1

**Arg30: dFulltransdataFpropchange**

Description: double value of fulltransdata fpropchange

Data Type: double

Default Value : 0.05

Syntax: dFulltransdataFpropchange = 1.0

**Arg31: iFulltransdataIpointnum**

Description: option for fulltransdata ipointnum

Data Type: integer

Default Value : 64

Syntax: iFulltransdataIpointnum = 1

**Arg32: dFulltransdataFmintemp**

Description: double value of fulltransdata fmintemp

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmintemp = 1.0

**Arg33: dFulltransdataFmaxtemp**

Description: double value of fulltransdata fmaxtemp

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmaxtemp = 1.0

**Arg34: iFulltransdataIequationsolv**

Description: option for fulltransdata iequationsolv

Data Type: integer

Default Value : 0

Syntax: iFulltransdataIequationsolv = 1

**Arg35: dFulltransdataFtollevel**

Description: double value of fulltransdata ftollevel

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFtollevel = 1.0

**Arg36: dFulltransdataFmultiplier**

Description: double value of fulltransdata fmultiplier

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmultiplier = 1.0

**Arg37: bFulltransdataBsignleprecision**

Description: enable or disable feature fulltransdata bsignleprecision

Data Type: bool

Default Value : False

Syntax: bFulltransdataBsignleprecision = True/False

**Arg38: bFulltransdataBmemorysave**

Description: enable or disable feature fulltransdata bmemorysave

Data Type: bool

Default Value : False

Syntax: bFulltransdataBmemorysave = True/False

**Arg39: dFulltransdataFtempdiff**

Description: double value of fulltransdata ftempdiff

Data Type: double

Default Value : 1.1

Syntax: dFulltransdataFtempdiff = 1.0

**Arg40: dHarmonicdataFstartfreq**

Description: double value of harmonicdata fstartfreq

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFstartfreq = 1.0

**Arg41: dHarmonicdataFendfreq**

Description: double value of harmonicdata fendfreq

Data Type: double

Default Value : 1.0

Syntax: dHarmonicdataFendfreq = 1.0

**Arg42: iHarmonicdataNsubsteps**

Description: option for harmonicdata nsubsteps

Data Type: integer

Default Value : 0

Syntax: iHarmonicdataNsubsteps = 1

**Arg43: dHarmonicdataFalphad**

Description: double value of harmonicdata falphad

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFalphad = 1.0

**Arg44: dHarmonicdataFbetad**

Description: double value of harmonicdata fbetad

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFbetad = 1.0

**Arg45: dHarmonicdataFdmprat**

Description: double value of harmonicdata fdmprat

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFdmprat = 1.0

**Arg46: bHarmonicdataBoutputdisplacements**

Description: enable or disable feature harmonicdata output displacements

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputdisplacements = True/False

**Arg47: bHarmonicdataBoutputstrain**

Description: enable or disable feature harmonicdata output strain

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputstrain = True/False

**Arg48: bHarmonicdataBoutputstress**

Description: enable or disable feature harmonicdata output stress

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputstress = True/False

**Arg49: iLCId**

Description: option for l c id

Data Type: integer

Default Value : 0

Syntax: iLCId = 1

**Arg50: iModeShape**

Description: option for mode shape

Data Type: integer

Default Value : 0

Syntax: iModeShape = 1

**Arg51: iModaldataImodemethod**

Description: option for modaldata imodemethod

Data Type: integer

Default Value : 0

Syntax: iModaldataImodemethod = 1

**Arg52: iModaldataIextractnum**

Description: option for modaldata iextractnum

Data Type: integer

Default Value : 1

Syntax: iModaldataIextractnum = 1

**Arg53: bModaldataBexpandshape**

Description: enable or disable feature modaldata bexpandshape

Data Type: bool

Default Value : True

Syntax: bModaldataBexpandshape = True/False

**Arg54: iModaldataIexpandnum**

Description: option for modaldata iexpandnum

Data Type: integer

Default Value : 0

Syntax: iModaldataIexpandnum = 1

**Arg55: bModaldataBuseapprox**

Description: enable or disable feature modaldata buseapprox

Data Type: bool

Default Value : False

Syntax: bModaldataBuseapprox = True/False

**Arg56: bModaldataBinclprsseff**

Description: enable or disable feature modaldata binclprsseff

Data Type: bool

Default Value : False

Syntax: bModaldataBinclprsseff = True/False

**Arg57: bModaldataBmemorysave**

Description: enable or disable feature modaldata bmemorysave

Data Type: bool

Default Value : False

Syntax: bModaldataBmemorysave = True/False

**Arg58: bModaldataBrsvec**

Description: enable or disable feature modaldata brsvec

Data Type: bool

Default Value : False

Syntax: bModaldataBrsvec = True/False

**Arg59: bModaldataBoutputdisplacements**

Description: enable or disable feature modaldata output displacements

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputdisplacements = True/False

**Arg60: bModaldataBoutputstrain**

Description: enable or disable feature modaldata output strain

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputstrain = True/False

**Arg61: bModaldataBoutputstress**

Description: enable or disable feature modaldata output stress

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputstress = True/False

**Arg62: iReduceddataIprintnum**

Description: option for reduceddata iprintnum

Data Type: integer

Default Value : 0

Syntax: iReduceddataIprintnum = 1

**Arg63: bSsdataBmemorysave**

Description: enable or disable feature ssdata bmemorysave

Data Type: bool

Default Value : False

Syntax: bSsdataBmemorysave = True/False

**Arg64: bSsdataBoutputheatflux**

Description: enable or disable feature ssdata boutputheatflux

Data Type: bool

Default Value : False

Syntax: bSsdataBoutputheatflux = True/False

**Arg65: bSsdataBoutputtemperature**

Description: enable or disable feature ssdata boutputtemperature

Data Type: bool

Default Value : False

Syntax: bSsdataBoutputtemperature = True/False

**Arg66: bSsdataBpivotscheck**

Description: enable or disable feature ssdata bpivotscheck

Data Type: bool

Default Value : True

Syntax: bSsdataBpivotscheck = True/False

**Arg67: bSsdataBsignleprecision**

Description: enable or disable feature ssdata bsignleprecision

Data Type: bool

Default Value : False

Syntax: bSsdataBsignleprecision = True/False

**Arg68: dSsdataFmultiplier**

Description: double value of ssdata fmultiplier

Data Type: double

Default Value : 0.0

Syntax: dSsdataFmultiplier = 1.0

**Arg69: dSsdataFtempdiff**

Description: double value of ssdata ftempdiff

Data Type: double

Default Value : 0.0

Syntax: dSsdataFtempdiff = 1.0

**Arg70: dSsdataFtollevel**

Description: double value of ssdata ftollevel

Data Type: double

Default Value : 0.0

Syntax: dSsdataFtollevel = 1.0

**Arg71: iSsdataIadaptivedes**

Description: option for ssdata iadaptivedes

Data Type: integer

Default Value : 0

Syntax: iSsdataIadaptivedes = 1

**Arg72: iSsdataIequationsolv**

Description: option for ssdata iequationsolv

Data Type: integer

Default Value : 0

Syntax: iSsdataIequationsolv = 1

**Arg73: iSsdataInpoption**

Description: option for ssdata inpoption

Data Type: integer

Default Value : 0

Syntax: iSsdataInpoption = 1

**Arg74: strAnsysVersion**

Description: definition string of input ansys version

Data Type: string

Default Value : ""

Syntax: strAnsysVersion = "string input"

**Arg75: strCommandLineOption**

Description: definition string of input command line option

Data Type: string

Default Value : ""

Syntax: strCommandLineOption = "string input"

**Arg76: bOutputSOLVE**

Description: enable or disable feature output s o l v e

Data Type: bool

Default Value : False

Syntax: bOutputSOLVE = True/False

**Arg77: iSubspacedataIrigidmode**

Description: option for subspacedata irigidmode

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIrigidmode = 1

**Arg78: iSubspacedataIworksize**

Description: option for subspacedata iworksize

Data Type: integer

Default Value : 8

Syntax: iSubspacedataIworksize = 1

**Arg79: iSubspacedataInpadnum**

Description: option for subspacedata inpadnum

Data Type: integer

Default Value : 4

Syntax: iSubspacedataInpadnum = 1

**Arg80: iSubspacedataIblocknum**

Description: option for subspacedata iblocknum

Data Type: integer

Default Value : 5

Syntax: iSubspacedataIblocknum = 1

**Arg81: iSubspacedataImaxiteratcnt**

Description: option for subspacedata imaxiteratcnt

Data Type: integer

Default Value : 0

Syntax: iSubspacedataImaxiteratcnt = 1

**Arg82: iSubspacedataIminnshift**

Description: option for subspacedata iminnshift

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIminnshift = 1

**Arg83: iSubspacedataIseqcheck**

Description: option for subspacedata iseqcheck

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIseqcheck = 1

**Arg84: bTransientdataBtraneffect**

Description: enable or disable feature transientdata btraneffect

Data Type: bool

Default Value : True

Syntax: bTransientdataBtraneffect = True/False

**Arg85: iTransientdataIloadingtype**

Description: option for transientdata iloadingtype

Data Type: integer

Default Value : 0

Syntax: iTransientdataIloadingtype = 1

**Arg86: dTransientdataFmassmatrixmult**

Description: double value of transientdata fmassmatrixmult

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFmassmatrixmult = 1.0

**Arg87: dTransientdataFstiffmatrixmult**

Description: double value of transientdata fstiffmatrixmult

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFstiffmatrixmult = 1.0

**Arg88: bTransientdataBmidstep**

Description: enable or disable feature transientdata bmidstep

Data Type: bool

Default Value : False

Syntax: bTransientdataBmidstep = True/False

**Arg89: dTransientdataFtolerancebisection**

Description: double value of transientdata ftolerancebisection

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFtolerancebisection = 1.0

**Arg90: dTransientdataFtolerancetimestep**

Description: double value of transientdata ftolerancetimestep

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFtolerancetimestep = 1.0

**Arg91: iTransientdataItimeinteralgor**

Description: option for transientdata itimeinteralgor

Data Type: integer

Default Value : 0

Syntax: iTransientdataItimeinteralgor = 1

**Arg92: iTransientdataItimeinter**

Description: option for transientdata itimeinter

Data Type: integer

Default Value : 0

Syntax: iTransientdataItimeinter = 1

**Arg93: dTransientdataFgamma**

Description: double value of transientdata fgamma

Data Type: double

Default Value : 0.005

Syntax: dTransientdataFgamma = 1.0

**Arg94: dTransientdataFalpha**

Description: double value of transientdata falpha

Data Type: double

Default Value : 0.25250625

Syntax: dTransientdataFalpha = 1.0

**Arg95: dTransientdataFdelta**

Description: double value of transientdata fdelta

Data Type: double

Default Value : 0.505

Syntax: dTransientdataFdelta = 1.0

**Arg96: dTransientdataFalphaf**

Description: double value of transientdata falphaf

Data Type: double

Default Value : 0.005

Syntax: dTransientdataFalphaf = 1.0

**Arg97: dTransientdataFalpham**

Description: double value of transientdata falpham

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFalpham = 1.0

**Arg98: bTransientdataBoutputtemperature**

Description: enable or disable feature transientdata boutputtemperature

Data Type: bool

Default Value : False

Syntax: bTransientdataBoutputtemperature = True/False

**Arg99: bTransientdataBoutputheatflux**

Description: enable or disable feature transientdata boutputheatflux

Data Type: bool

Default Value : False

Syntax: bTransientdataBoutputheatflux = True/False

**Arg100: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg101: strFileName**

Description: definition string of input file name

Data Type: string

Default Value : ""

Syntax: strFileName = "string input"

**Arg102: crAnsysJob**

Description: entity in database model with type ansys job

Data Type: cursor

Default Value : None

Syntax: crAnsysJob = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Ansys.Harmonic(strJobName="", iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None, strFileName="", crAnsysJob=None)

```

==========================================================

# Analysis.Ansys.Steady

## Wrapper Macro

Ansys_SteadyHeatTransfer(...)

## Ribbon-GUI-Location

Analysis > Ansys > Steady

## Command Description

Create and export Ansys job for Steady Heat Transfer

## Argument List

**Arg1: strJobName**

Description: definition string of input job name

Data Type: string

Default Value : ""

Syntax: strJobName = "string input"

**Arg2: iJobdataAnatype**

Description: option for job data anatype

Data Type: integer

Default Value : 0

Syntax: iJobdataAnatype = 1

**Arg3: iJobdataSoltype**

Description: option for job data soltype

Data Type: integer

Default Value : 0

Syntax: iJobdataSoltype = 1

**Arg4: strJobdataJobname**

Description: definition string of input job data job name

Data Type: string

Default Value : "Job1"

Syntax: strJobdataJobname = "string input"

**Arg5: strJobdataJobdescription**

Description: definition string of input job data job description

Data Type: string

Default Value : ""

Syntax: strJobdataJobdescription = "string input"

**Arg6: bBasicdataBoutputdisplacements**

Description: enable or disable feature basic data output displacements

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputdisplacements = True/False

**Arg7: bBasicdataBoutputreactionload**

Description: enable or disable feature basic data output reaction load

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputreactionload = True/False

**Arg8: bBasicdataBoutputstrain**

Description: enable or disable feature basic data output strain

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputstrain = True/False

**Arg9: bBasicdataBoutputstress**

Description: enable or disable feature basic data output stress

Data Type: bool

Default Value : False

Syntax: bBasicdataBoutputstress = True/False

**Arg10: iBasicdataIanalysisopt**

Description: option for basic data ianalysisopt

Data Type: integer

Default Value : 0

Syntax: iBasicdataIanalysisopt = 1

**Arg11: bBasicdataBcalPressEffects**

Description: enable or disable feature basic data caculation press effects

Data Type: bool

Default Value : False

Syntax: bBasicdataBcalPressEffects = True/False

**Arg12: dBasicdataFunitem**

Description: double value of basic data funitem

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFunitem = 1.0

**Arg13: dBasicdataFreftemp**

Description: double value of basic data freftemp

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFreftemp = 1.0

**Arg14: dBasicdataFendloadtime**

Description: double value of basic data fendloadtime

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFendloadtime = 1.0

**Arg15: iBasicdataItimestep**

Description: option for basic data time step value

Data Type: integer

Default Value : 0

Syntax: iBasicdataItimestep = 1

**Arg16: iBasicdataIstepchosen**

Description: option for basic data step chosen value

Data Type: integer

Default Value : 0

Syntax: iBasicdataIstepchosen = 1

**Arg17: iBasicdataIsubstepnum**

Description: option for basic data substep number

Data Type: integer

Default Value : 0

Syntax: iBasicdataIsubstepnum = 1

**Arg18: iBasicdataImaxsubstep**

Description: option for basic data maximum substep value

Data Type: integer

Default Value : 0

Syntax: iBasicdataImaxsubstep = 1

**Arg19: iBasicdataIminstepnum**

Description: option for basic data minimum step number

Data Type: integer

Default Value : 0

Syntax: iBasicdataIminstepnum = 1

**Arg20: dBasicdataFtimestepsize**

Description: double value of basic data time step size

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFtimestepsize = 1.0

**Arg21: dBasicdataFmintimestep**

Description: double value of basic data minimum time step

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFmintimestep = 1.0

**Arg22: dBasicdataFmaxtimestep**

Description: double value of basic data maximum time step

Data Type: double

Default Value : 0.0

Syntax: dBasicdataFmaxtimestep = 1.0

**Arg23: iBasicdataIwritereslutfre**

Description: option for basic data write result frequency

Data Type: integer

Default Value : 1

Syntax: iBasicdataIwritereslutfre = 1

**Arg24: iBasicdataIn**

Description: option for basic data in

Data Type: integer

Default Value : 1

Syntax: iBasicdataIn = 1

**Arg25: bRunAPDL**

Description: enable or disable feature run ADPL

Data Type: bool

Default Value : False

Syntax: bRunAPDL = True/False

**Arg26: bWriteResultDB**

Description: enable or disable feature write result database

Data Type: bool

Default Value : False

Syntax: bWriteResultDB = True/False

**Arg27: dFEndFreq**

Description: double value of end frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dFEndFreq = 1.0

**Arg28: dFStartFreq**

Description: double value of start frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dFStartFreq = 1.0

**Arg29: iFulltransdataIsolutionoption**

Description: option for fulltransdata isolutionoption

Data Type: integer

Default Value : 0

Syntax: iFulltransdataIsolutionoption = 1

**Arg30: dFulltransdataFpropchange**

Description: double value of fulltransdata fpropchange

Data Type: double

Default Value : 0.05

Syntax: dFulltransdataFpropchange = 1.0

**Arg31: iFulltransdataIpointnum**

Description: option for fulltransdata ipointnum

Data Type: integer

Default Value : 64

Syntax: iFulltransdataIpointnum = 1

**Arg32: dFulltransdataFmintemp**

Description: double value of fulltransdata fmintemp

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmintemp = 1.0

**Arg33: dFulltransdataFmaxtemp**

Description: double value of fulltransdata fmaxtemp

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmaxtemp = 1.0

**Arg34: iFulltransdataIequationsolv**

Description: option for fulltransdata iequationsolv

Data Type: integer

Default Value : 0

Syntax: iFulltransdataIequationsolv = 1

**Arg35: dFulltransdataFtollevel**

Description: double value of fulltransdata ftollevel

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFtollevel = 1.0

**Arg36: dFulltransdataFmultiplier**

Description: double value of fulltransdata fmultiplier

Data Type: double

Default Value : 0.0

Syntax: dFulltransdataFmultiplier = 1.0

**Arg37: bFulltransdataBsignleprecision**

Description: enable or disable feature fulltransdata bsignleprecision

Data Type: bool

Default Value : False

Syntax: bFulltransdataBsignleprecision = True/False

**Arg38: bFulltransdataBmemorysave**

Description: enable or disable feature fulltransdata bmemorysave

Data Type: bool

Default Value : False

Syntax: bFulltransdataBmemorysave = True/False

**Arg39: dFulltransdataFtempdiff**

Description: double value of fulltransdata ftempdiff

Data Type: double

Default Value : 1.1

Syntax: dFulltransdataFtempdiff = 1.0

**Arg40: dHarmonicdataFstartfreq**

Description: double value of harmonicdata fstartfreq

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFstartfreq = 1.0

**Arg41: dHarmonicdataFendfreq**

Description: double value of harmonicdata fendfreq

Data Type: double

Default Value : 1.0

Syntax: dHarmonicdataFendfreq = 1.0

**Arg42: iHarmonicdataNsubsteps**

Description: option for harmonicdata nsubsteps

Data Type: integer

Default Value : 0

Syntax: iHarmonicdataNsubsteps = 1

**Arg43: dHarmonicdataFalphad**

Description: double value of harmonicdata falphad

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFalphad = 1.0

**Arg44: dHarmonicdataFbetad**

Description: double value of harmonicdata fbetad

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFbetad = 1.0

**Arg45: dHarmonicdataFdmprat**

Description: double value of harmonicdata fdmprat

Data Type: double

Default Value : 0.0

Syntax: dHarmonicdataFdmprat = 1.0

**Arg46: bHarmonicdataBoutputdisplacements**

Description: enable or disable feature harmonicdata output displacements

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputdisplacements = True/False

**Arg47: bHarmonicdataBoutputstrain**

Description: enable or disable feature harmonicdata output strain

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputstrain = True/False

**Arg48: bHarmonicdataBoutputstress**

Description: enable or disable feature harmonicdata output stress

Data Type: bool

Default Value : False

Syntax: bHarmonicdataBoutputstress = True/False

**Arg49: iLCId**

Description: option for l c id

Data Type: integer

Default Value : 0

Syntax: iLCId = 1

**Arg50: iModeShape**

Description: option for mode shape

Data Type: integer

Default Value : 0

Syntax: iModeShape = 1

**Arg51: iModaldataImodemethod**

Description: option for modaldata imodemethod

Data Type: integer

Default Value : 0

Syntax: iModaldataImodemethod = 1

**Arg52: iModaldataIextractnum**

Description: option for modaldata iextractnum

Data Type: integer

Default Value : 1

Syntax: iModaldataIextractnum = 1

**Arg53: bModaldataBexpandshape**

Description: enable or disable feature modaldata bexpandshape

Data Type: bool

Default Value : True

Syntax: bModaldataBexpandshape = True/False

**Arg54: iModaldataIexpandnum**

Description: option for modaldata iexpandnum

Data Type: integer

Default Value : 0

Syntax: iModaldataIexpandnum = 1

**Arg55: bModaldataBuseapprox**

Description: enable or disable feature modaldata buseapprox

Data Type: bool

Default Value : False

Syntax: bModaldataBuseapprox = True/False

**Arg56: bModaldataBinclprsseff**

Description: enable or disable feature modaldata binclprsseff

Data Type: bool

Default Value : False

Syntax: bModaldataBinclprsseff = True/False

**Arg57: bModaldataBmemorysave**

Description: enable or disable feature modaldata bmemorysave

Data Type: bool

Default Value : False

Syntax: bModaldataBmemorysave = True/False

**Arg58: bModaldataBrsvec**

Description: enable or disable feature modaldata brsvec

Data Type: bool

Default Value : False

Syntax: bModaldataBrsvec = True/False

**Arg59: bModaldataBoutputdisplacements**

Description: enable or disable feature modaldata output displacements

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputdisplacements = True/False

**Arg60: bModaldataBoutputstrain**

Description: enable or disable feature modaldata output strain

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputstrain = True/False

**Arg61: bModaldataBoutputstress**

Description: enable or disable feature modaldata output stress

Data Type: bool

Default Value : False

Syntax: bModaldataBoutputstress = True/False

**Arg62: iReduceddataIprintnum**

Description: option for reduceddata iprintnum

Data Type: integer

Default Value : 0

Syntax: iReduceddataIprintnum = 1

**Arg63: bSsdataBmemorysave**

Description: enable or disable feature ssdata bmemorysave

Data Type: bool

Default Value : False

Syntax: bSsdataBmemorysave = True/False

**Arg64: bSsdataBoutputheatflux**

Description: enable or disable feature ssdata boutputheatflux

Data Type: bool

Default Value : False

Syntax: bSsdataBoutputheatflux = True/False

**Arg65: bSsdataBoutputtemperature**

Description: enable or disable feature ssdata boutputtemperature

Data Type: bool

Default Value : False

Syntax: bSsdataBoutputtemperature = True/False

**Arg66: bSsdataBpivotscheck**

Description: enable or disable feature ssdata bpivotscheck

Data Type: bool

Default Value : True

Syntax: bSsdataBpivotscheck = True/False

**Arg67: bSsdataBsignleprecision**

Description: enable or disable feature ssdata bsignleprecision

Data Type: bool

Default Value : False

Syntax: bSsdataBsignleprecision = True/False

**Arg68: dSsdataFmultiplier**

Description: double value of ssdata fmultiplier

Data Type: double

Default Value : 0.0

Syntax: dSsdataFmultiplier = 1.0

**Arg69: dSsdataFtempdiff**

Description: double value of ssdata ftempdiff

Data Type: double

Default Value : 0.0

Syntax: dSsdataFtempdiff = 1.0

**Arg70: dSsdataFtollevel**

Description: double value of ssdata ftollevel

Data Type: double

Default Value : 0.0

Syntax: dSsdataFtollevel = 1.0

**Arg71: iSsdataIadaptivedes**

Description: option for ssdata iadaptivedes

Data Type: integer

Default Value : 0

Syntax: iSsdataIadaptivedes = 1

**Arg72: iSsdataIequationsolv**

Description: option for ssdata iequationsolv

Data Type: integer

Default Value : 0

Syntax: iSsdataIequationsolv = 1

**Arg73: iSsdataInpoption**

Description: option for ssdata inpoption

Data Type: integer

Default Value : 0

Syntax: iSsdataInpoption = 1

**Arg74: strAnsysVersion**

Description: definition string of input ansys version

Data Type: string

Default Value : ""

Syntax: strAnsysVersion = "string input"

**Arg75: strCommandLineOption**

Description: definition string of input command line option

Data Type: string

Default Value : ""

Syntax: strCommandLineOption = "string input"

**Arg76: bOutputSOLVE**

Description: enable or disable feature output s o l v e

Data Type: bool

Default Value : False

Syntax: bOutputSOLVE = True/False

**Arg77: iSubspacedataIrigidmode**

Description: option for subspacedata irigidmode

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIrigidmode = 1

**Arg78: iSubspacedataIworksize**

Description: option for subspacedata iworksize

Data Type: integer

Default Value : 8

Syntax: iSubspacedataIworksize = 1

**Arg79: iSubspacedataInpadnum**

Description: option for subspacedata inpadnum

Data Type: integer

Default Value : 4

Syntax: iSubspacedataInpadnum = 1

**Arg80: iSubspacedataIblocknum**

Description: option for subspacedata iblocknum

Data Type: integer

Default Value : 5

Syntax: iSubspacedataIblocknum = 1

**Arg81: iSubspacedataImaxiteratcnt**

Description: option for subspacedata imaxiteratcnt

Data Type: integer

Default Value : 0

Syntax: iSubspacedataImaxiteratcnt = 1

**Arg82: iSubspacedataIminnshift**

Description: option for subspacedata iminnshift

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIminnshift = 1

**Arg83: iSubspacedataIseqcheck**

Description: option for subspacedata iseqcheck

Data Type: integer

Default Value : 0

Syntax: iSubspacedataIseqcheck = 1

**Arg84: bTransientdataBtraneffect**

Description: enable or disable feature transientdata btraneffect

Data Type: bool

Default Value : True

Syntax: bTransientdataBtraneffect = True/False

**Arg85: iTransientdataIloadingtype**

Description: option for transientdata iloadingtype

Data Type: integer

Default Value : 0

Syntax: iTransientdataIloadingtype = 1

**Arg86: dTransientdataFmassmatrixmult**

Description: double value of transientdata fmassmatrixmult

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFmassmatrixmult = 1.0

**Arg87: dTransientdataFstiffmatrixmult**

Description: double value of transientdata fstiffmatrixmult

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFstiffmatrixmult = 1.0

**Arg88: bTransientdataBmidstep**

Description: enable or disable feature transientdata bmidstep

Data Type: bool

Default Value : False

Syntax: bTransientdataBmidstep = True/False

**Arg89: dTransientdataFtolerancebisection**

Description: double value of transientdata ftolerancebisection

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFtolerancebisection = 1.0

**Arg90: dTransientdataFtolerancetimestep**

Description: double value of transientdata ftolerancetimestep

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFtolerancetimestep = 1.0

**Arg91: iTransientdataItimeinteralgor**

Description: option for transientdata itimeinteralgor

Data Type: integer

Default Value : 0

Syntax: iTransientdataItimeinteralgor = 1

**Arg92: iTransientdataItimeinter**

Description: option for transientdata itimeinter

Data Type: integer

Default Value : 0

Syntax: iTransientdataItimeinter = 1

**Arg93: dTransientdataFgamma**

Description: double value of transientdata fgamma

Data Type: double

Default Value : 0.005

Syntax: dTransientdataFgamma = 1.0

**Arg94: dTransientdataFalpha**

Description: double value of transientdata falpha

Data Type: double

Default Value : 0.25250625

Syntax: dTransientdataFalpha = 1.0

**Arg95: dTransientdataFdelta**

Description: double value of transientdata fdelta

Data Type: double

Default Value : 0.505

Syntax: dTransientdataFdelta = 1.0

**Arg96: dTransientdataFalphaf**

Description: double value of transientdata falphaf

Data Type: double

Default Value : 0.005

Syntax: dTransientdataFalphaf = 1.0

**Arg97: dTransientdataFalpham**

Description: double value of transientdata falpham

Data Type: double

Default Value : 0.0

Syntax: dTransientdataFalpham = 1.0

**Arg98: bTransientdataBoutputtemperature**

Description: enable or disable feature transientdata boutputtemperature

Data Type: bool

Default Value : False

Syntax: bTransientdataBoutputtemperature = True/False

**Arg99: bTransientdataBoutputheatflux**

Description: enable or disable feature transientdata boutputheatflux

Data Type: bool

Default Value : False

Syntax: bTransientdataBoutputheatflux = True/False

**Arg100: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg101: strFileName**

Description: definition string of input file name

Data Type: string

Default Value : ""

Syntax: strFileName = "string input"

**Arg102: crAnsysJob**

Description: entity in database model with type ansys job

Data Type: cursor

Default Value : None

Syntax: crAnsysJob = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Ansys.Steady(strJobName="", iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None, strFileName="", crAnsysJob=None)

```

==========================================================

# Analysis.Nastran.ModalTransientResponse

## Wrapper Macro

Nastran_ModalTransientResponse(...)

## Ribbon-GUI-Location

Analysis > Nastran > ModalTransientResponse

## Command Description

Export Nastran Modal Transient Response

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: bDummyPropAutoAssign**

Description: enable or disable feature dummy property auto assign

Data Type: bool

Default Value : False

Syntax: bDummyPropAutoAssign = True/False

**Arg6: iDummyPropMaterialID**

Description: option for dummy property material ID

Data Type: integer

Default Value : 0

Syntax: iDummyPropMaterialID = 1

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Nastran.ModalTransientResponse(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.Nastran.LinearBuckling

## Wrapper Macro

Nastran_LinearBuckling(...)

## Ribbon-GUI-Location

Analysis > Nastran > LinearBuckling

## Command Description

Export Nastran Linear Buckling

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: bDummyPropAutoAssign**

Description: enable or disable feature dummy property auto assign

Data Type: bool

Default Value : False

Syntax: bDummyPropAutoAssign = True/False

**Arg6: iDummyPropMaterialID**

Description: option for dummy property material ID

Data Type: integer

Default Value : 0

Syntax: iDummyPropMaterialID = 1

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Nastran.LinearBuckling(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.Nastran.Transient

## Wrapper Macro

Nastran_Transient(...)

## Ribbon-GUI-Location

Analysis > Nastran > Transient

## Command Description

Export Nastran Transient

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: bDummyPropAutoAssign**

Description: enable or disable feature dummy property auto assign

Data Type: bool

Default Value : False

Syntax: bDummyPropAutoAssign = True/False

**Arg6: iDummyPropMaterialID**

Description: option for dummy property material ID

Data Type: integer

Default Value : 0

Syntax: iDummyPropMaterialID = 1

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Nastran.Transient(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.Nastran.SteadyState

## Wrapper Macro

Nastran_SteadyState(...)

## Ribbon-GUI-Location

Analysis > Nastran > SteadyState

## Command Description

Export Nastran Steady State

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: bDummyPropAutoAssign**

Description: enable or disable feature dummy property auto assign

Data Type: bool

Default Value : False

Syntax: bDummyPropAutoAssign = True/False

**Arg6: iDummyPropMaterialID**

Description: option for dummy property material ID

Data Type: integer

Default Value : 0

Syntax: iDummyPropMaterialID = 1

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Nastran.SteadyState(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.Nastran.ModalFrequencyResponse

## Wrapper Macro

Nastran_ModalFrequencyResponse(...)

## Ribbon-GUI-Location

Analysis > Nastran > ModalFrequencyResponse

## Command Description

Export Nastran Modal Frequency Response

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: bDummyPropAutoAssign**

Description: enable or disable feature dummy property auto assign

Data Type: bool

Default Value : False

Syntax: bDummyPropAutoAssign = True/False

**Arg6: iDummyPropMaterialID**

Description: option for dummy property material ID

Data Type: integer

Default Value : 0

Syntax: iDummyPropMaterialID = 1

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Nastran.ModalFrequencyResponse(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.Nastran.LinearStatic

## Wrapper Macro

Nastran_LinearStatic(...)

## Ribbon-GUI-Location

Analysis > Nastran > LinearStatic

## Command Description

Export Nastran Linear Static

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: bDummyPropAutoAssign**

Description: enable or disable feature dummy property auto assign

Data Type: bool

Default Value : False

Syntax: bDummyPropAutoAssign = True/False

**Arg6: iDummyPropMaterialID**

Description: option for dummy property material ID

Data Type: integer

Default Value : 0

Syntax: iDummyPropMaterialID = 1

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Nastran.LinearStatic(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.Nastran.NormalModes

## Wrapper Macro

Nastran_NormalModes(...)

## Ribbon-GUI-Location

Analysis > Nastran > NormalModes

## Command Description

Export Nastran Normal Modes

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: bDummyPropAutoAssign**

Description: enable or disable feature dummy property auto assign

Data Type: bool

Default Value : False

Syntax: bDummyPropAutoAssign = True/False

**Arg6: iDummyPropMaterialID**

Description: option for dummy property material ID

Data Type: integer

Default Value : 0

Syntax: iDummyPropMaterialID = 1

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Nastran.NormalModes(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.Permas.Job

## Wrapper Macro

PermasJob(...)

## Ribbon-GUI-Location

Analysis > Permas > Job

## Command Description

permas output

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg5: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg6: bElStress**

Description: enable or disable feature el stress

Data Type: bool

Default Value : False

Syntax: bElStress = True/False

**Arg7: bElStress**

Description: enable or disable feature el stress

Data Type: bool

Default Value : FalseMis

Syntax: bElStress = True/False

**Arg8: bElStrain**

Description: enable or disable feature el strain

Data Type: bool

Default Value : False

Syntax: bElStrain = True/False

**Arg9: bNodeStess**

Description: enable or disable feature node stess

Data Type: bool

Default Value : False

Syntax: bNodeStess = True/False

**Arg10: bGZip**

Description: enable or disable feature g zip

Data Type: bool

Default Value : False

Syntax: bGZip = True/False

**Arg11: bIdeas**

Description: enable or disable feature ideas

Data Type: bool

Default Value : False

Syntax: bIdeas = True/False

**Arg12: bNLResult**

Description: enable or disable feature non linear result

Data Type: bool

Default Value : False

Syntax: bNLResult = True/False

**Arg13: iNLStepType**

Description: option for non linear step type

Data Type: integer

Default Value : 0

Syntax: iNLStepType = 1

**Arg14: dEquiStart**

Description: double value of equi start

Data Type: double

Default Value : 0.0

Syntax: dEquiStart = 1.0

**Arg15: dEquiStep**

Description: double value of equi step

Data Type: double

Default Value : 0.0

Syntax: dEquiStep = 1.0

**Arg16: dEquiEnd**

Description: double value of equi end

Data Type: double

Default Value : 0.0

Syntax: dEquiEnd = 1.0

**Arg17: strNLStepList**

Description: definition string of input non linear step list

Data Type: string

Default Value : ""

Syntax: strNLStepList = "string input"

**Arg18: bTimeStep**

Description: enable or disable feature time step

Data Type: bool

Default Value : False

Syntax: bTimeStep = True/False

**Arg19: iTimeStepKind**

Description: option for time step kind

Data Type: integer

Default Value : 0

Syntax: iTimeStepKind = 1

**Arg20: dTimeStart**

Description: double value of time start

Data Type: double

Default Value : 0.0

Syntax: dTimeStart = 1.0

**Arg21: dTimeStep**

Description: double value of time step

Data Type: double

Default Value : 0.0

Syntax: dTimeStep = 1.0

**Arg22: dTimeEnd**

Description: double value of time end

Data Type: double

Default Value : 0.0

Syntax: dTimeEnd = 1.0

**Arg23: iLCId**

Description: option for l c id

Data Type: integer

Default Value : 0

Syntax: iLCId = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Permas.Job(strName="", strDescription="", iType=0, crEdit=None, crlTarget=[], bElStress=False, bElStress=FalseMis, bElStrain=False, bNodeStess=False, bGZip=False, bIdeas=False, bNLResult=False, iNLStepType=0, dEquiStart=0.0, dEquiStep=0.0, dEquiEnd=0.0, strNLStepList="", bTimeStep=False, iTimeStepKind=0, dTimeStart=0.0, dTimeStep=0.0, dTimeEnd=0.0, iLCId=0)

```

==========================================================

# Analysis.TSSolver.ExportDynamisBdf

## Wrapper Macro

ExportDynamisBdf(...)

## Ribbon-GUI-Location

Analysis > TSSolver > ExportDynamisBdf

## Command Description

## Argument List

**Arg1: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg2: crJob**

Description: entity in database model with type job

Data Type: cursor

Default Value : None

Syntax: crJob = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.ExportDynamisBdf(strPath="", crJob=None)

```

==========================================================

# Analysis.TSSolver.Job

## Wrapper Macro

DynamisJob(...)

## Ribbon-GUI-Location

Analysis > TSSolver > Job

## Command Description

Create TS-Solver Job

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.Job(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None)

```

==========================================================

# Analysis.TSSolver.LinearBucking

## Wrapper Macro

TSSolver_LinearBuckling(...)

## Ribbon-GUI-Location

Analysis > TSSolver > LinearBucking

## Command Description

Export TS-Solver Linear Bucking

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.LinearBucking(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")

```

==========================================================

# Analysis.TSSolver.LinearStatic

## Wrapper Macro

TSSolverLinearStatic(...)

## Ribbon-GUI-Location

Analysis > TSSolver > LinearStatic

## Command Description

Export TS-Solver Linear Static

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.LinearStatic(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")

```

==========================================================

# Analysis.TSSolver.NonlinearStatic

## Wrapper Macro

TSSolverNonlinearStatic(...)

## Ribbon-GUI-Location

Analysis > TSSolver > NonlinearStatic

## Command Description

Export TS-Solver Nonlinear Static

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.NonlinearStatic(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")

```

==========================================================

# Analysis.TSSolver.NormalModes

## Wrapper Macro

TSSolverNormalModes(...)

## Ribbon-GUI-Location

Analysis > TSSolver > NormalModes

## Command Description

Export TS-Solver Normal Modes

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.NormalModes(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")

```

==========================================================

# Analysis.TSSolver.NonlinearFrequency

## Wrapper Macro

TSSolverNonlinearFrequency(...)

## Ribbon-GUI-Location

Analysis > TSSolver > NonlinearFrequency

## Command Description

Export TS-Solver Nonlinear Frequency

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.NonlinearFrequency(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")

```

==========================================================

# Analysis.TSSolver.ModalTransientResponse

## Wrapper Macro

TSSolverModalTransientResponse(...)

## Ribbon-GUI-Location

Analysis > TSSolver > ModalTransientResponse

## Command Description

Export TS-Solver Modal Transient Response

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.ModalTransientResponse(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")

```

==========================================================

# Analysis.TSSolver.TransientHeatTransfer

## Wrapper Macro

TSSolverTransientHeatTransfer(...)

## Ribbon-GUI-Location

Analysis > TSSolver > TransientHeatTransfer

## Command Description

Export TS-Solver Transient Heat Transfer

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.TransientHeatTransfer(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")

```

==========================================================

# Analysis.TSSolver.ModalFrequencyResponse

## Wrapper Macro

TSSolver_ModalFrequencyResponse(...)

## Ribbon-GUI-Location

Analysis > TSSolver > ModalFrequencyResponse

## Command Description

Export TS-Solver Modal Frequency Response

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.ModalFrequencyResponse(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")

```

==========================================================

# Analysis.TSSolver.SteadyStateHeatTransfer

## Wrapper Macro

TSSolver_SteadyStateHeatTransfer(...)

## Ribbon-GUI-Location

Analysis > TSSolver > SteadyStateHeatTransfer

## Command Description

Export TS-Solver Steady State Heat Transfer

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSolver.SteadyStateHeatTransfer(strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath="")

```

==========================================================

# Analysis.TSSS.TransientHeatTransfer

## Wrapper Macro

TSSS_TransientHeatTransfer(...)

## Ribbon-GUI-Location

Analysis > TSSS > TransientHeatTransfer

## Command Description

Export TS-SS Transient Heat Transfer

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: iRadialReturn**

Description: option for radial return

Data Type: integer

Default Value : 0

Syntax: iRadialReturn = 1

**Arg6: listNastranNonlinear**

Description: list data structure of NASTRAN_NONLINEAR (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_NONLINEAR

Default Value : NASTRAN_NONLINEAR()

Syntax: listNastranNonlinear = [NASTRAN_NONLINEAR(,,,), NASTRAN_NONLINEAR(,,,)]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSS.TransientHeatTransfer(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.TSSS.LinearStatic

## Wrapper Macro

TSSS_LinearStatic(...)

## Ribbon-GUI-Location

Analysis > TSSS > LinearStatic

## Command Description

Export TS-SS Linear Static

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: iRadialReturn**

Description: option for radial return

Data Type: integer

Default Value : 0

Syntax: iRadialReturn = 1

**Arg6: listNastranNonlinear**

Description: list data structure of NASTRAN_NONLINEAR (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_NONLINEAR

Default Value : NASTRAN_NONLINEAR()

Syntax: listNastranNonlinear = [NASTRAN_NONLINEAR(,,,), NASTRAN_NONLINEAR(,,,)]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

**Arg11: iNitTempType**

Description: option for nit temperature type

Data Type: integer

Default Value : 0

Syntax: iNitTempType = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSS.LinearStatic(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0, iNitTempType=0)

```

==========================================================

# Analysis.TSSS.NonlinearStatic

## Wrapper Macro

TSSS_NonlinearStatic(...)

## Ribbon-GUI-Location

Analysis > TSSS > NonlinearStatic

## Command Description

Export TS-SS Nonlinear Static

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: iRadialReturn**

Description: option for radial return

Data Type: integer

Default Value : 0

Syntax: iRadialReturn = 1

**Arg6: listNastranNonlinear**

Description: list data structure of NASTRAN_NONLINEAR (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_NONLINEAR

Default Value : NASTRAN_NONLINEAR()

Syntax: listNastranNonlinear = [NASTRAN_NONLINEAR(,,,), NASTRAN_NONLINEAR(,,,)]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSS.NonlinearStatic(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.TSSS.NormalModes

## Wrapper Macro

TSSS_NormalModes(...)

## Ribbon-GUI-Location

Analysis > TSSS > NormalModes

## Command Description

Export TS-SS Normal Modes

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: iRadialReturn**

Description: option for radial return

Data Type: integer

Default Value : 0

Syntax: iRadialReturn = 1

**Arg6: listNastranNonlinear**

Description: list data structure of NASTRAN_NONLINEAR (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_NONLINEAR

Default Value : NASTRAN_NONLINEAR()

Syntax: listNastranNonlinear = [NASTRAN_NONLINEAR(,,,), NASTRAN_NONLINEAR(,,,)]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSS.NormalModes(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.TSSS.LinearBuckling

## Wrapper Macro

TSSS_LinearBuckling(...)

## Ribbon-GUI-Location

Analysis > TSSS > LinearBuckling

## Command Description

Export TS-SS Linear Buckling

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: iRadialReturn**

Description: option for radial return

Data Type: integer

Default Value : 0

Syntax: iRadialReturn = 1

**Arg6: listNastranNonlinear**

Description: list data structure of NASTRAN_NONLINEAR (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_NONLINEAR

Default Value : NASTRAN_NONLINEAR()

Syntax: listNastranNonlinear = [NASTRAN_NONLINEAR(,,,), NASTRAN_NONLINEAR(,,,)]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSS.LinearBuckling(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.TSSS.ModalFrequencyResponse

## Wrapper Macro

TSSS_ModalFrequencyResponse(...)

## Ribbon-GUI-Location

Analysis > TSSS > ModalFrequencyResponse

## Command Description

Export TS-SS Modal Frequency Response

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: iRadialReturn**

Description: option for radial return

Data Type: integer

Default Value : 0

Syntax: iRadialReturn = 1

**Arg6: listNastranNonlinear**

Description: list data structure of NASTRAN_NONLINEAR (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_NONLINEAR

Default Value : NASTRAN_NONLINEAR()

Syntax: listNastranNonlinear = [NASTRAN_NONLINEAR(,,,), NASTRAN_NONLINEAR(,,,)]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSS.ModalFrequencyResponse(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.TSSS.SteadyStateHeatTransfer

## Wrapper Macro

TSSS_SteadyStateHeatTransfer(...)

## Ribbon-GUI-Location

Analysis > TSSS > SteadyStateHeatTransfer

## Command Description

Export TS-SS Steady State Heat Transfer

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: iRadialReturn**

Description: option for radial return

Data Type: integer

Default Value : 0

Syntax: iRadialReturn = 1

**Arg6: listNastranNonlinear**

Description: list data structure of NASTRAN_NONLINEAR (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_NONLINEAR

Default Value : NASTRAN_NONLINEAR()

Syntax: listNastranNonlinear = [NASTRAN_NONLINEAR(,,,), NASTRAN_NONLINEAR(,,,)]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg9: iModelCheckAnswer**

Description: option for model check answer

Data Type: integer

Default Value : 0

Syntax: iModelCheckAnswer = 1

**Arg10: iDeleteSlaveNodesAnswer**

Description: option for delete slave nodes answer

Data Type: integer

Default Value : 0

Syntax: iDeleteSlaveNodesAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.TSSS.SteadyStateHeatTransfer(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0)

```

==========================================================

# Analysis.Abaqus

## Wrapper Macro

CreateAbaqusJob(...)

## Ribbon-GUI-Location

Analysis > Abaqus

## Command Description

abaqus exporting

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: bRBE2toMPC**

Description: enable or disable feature r b e2to m p c

Data Type: bool

Default Value : False

Syntax: bRBE2toMPC = True/False

**Arg3: bRenameProcess**

Description: enable or disable feature rename process

Data Type: bool

Default Value : False

Syntax: bRenameProcess = True/False

**Arg4: iCodeType**

Description: option for code type

Data Type: integer

Default Value : 0

Syntax: iCodeType = 1

**Arg5: iSurfDefType**

Description: option for surf def type

Data Type: integer

Default Value : 0

Syntax: iSurfDefType = 1

**Arg6: iUnit**

Description: option for unit

Data Type: integer

Default Value : 0

Syntax: iUnit = 1

**Arg7: iWriteType**

Description: option for write type

Data Type: integer

Default Value : 0

Syntax: iWriteType = 1

**Arg8: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg9: crlStepSequence**

Description: array entities in model with type step sequence

Data Type: cursor list

Default Value : []

Syntax: crlStepSequence = [EntityType(id1, id2, id3)]

**Arg10: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg11: strlUserText**

Description: list definition string of user text

Data Type: string list

Default Value : []

Syntax: strlUserText = ["str1", "str2", "str3"]

**Arg12: bExptNdEleGroups**

Description: enable or disable feature expt nd ele groups

Data Type: bool

Default Value : False

Syntax: bExptNdEleGroups = True/False

**Arg13: bDeleteFloatingNodes**

Description: enable or disable feature delete floating nodes

Data Type: bool

Default Value : False

Syntax: bDeleteFloatingNodes = True/False

**Arg14: bExptFaceElemGroups2Surface**

Description: enable or disable feature expt face element groups2 surface

Data Type: bool

Default Value : False

Syntax: bExptFaceElemGroups2Surface = True/False

**Arg15: bLoadCase**

Description: enable or disable feature load case

Data Type: bool

Default Value : False

Syntax: bLoadCase = True/False

**Arg16: bAutoAssignDummyProperty**

Description: enable or disable feature auto assign dummy property

Data Type: bool

Default Value : True

Syntax: bAutoAssignDummyProperty = True/False

**Arg17: crDummyMat**

Description: entity in database model with type dummy material

Data Type: cursor

Default Value : None

Syntax: crDummyMat = EntityType(id)

**Arg18: bOutputGeometryId**

Description: enable or disable feature output geometry id

Data Type: bool

Default Value : True

Syntax: bOutputGeometryId = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.Abaqus(strName="", bRBE2toMPC=False, bRenameProcess=False, iCodeType=0, iSurfDefType=0, iUnit=0, iWriteType=0, strDescription="", crlStepSequence=[], crEdit=None, strlUserText=[], bExptNdEleGroups=False, bDeleteFloatingNodes=False, bExptFaceElemGroups2Surface=False, bLoadCase=False, bAutoAssignDummyProperty=True, crDummyMat=None, bOutputGeometryId=True)

```

==========================================================

# Analysis.ExportAnsys

## Wrapper Macro

ExportAnsys(...)

## Ribbon-GUI-Location

Analysis > ExportAnsys

## Command Description

Find faces in part by typical description

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: crAnsysJob**

Description: entity in database model with type ansys job

Data Type: cursor

Default Value : None

Syntax: crAnsysJob = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ExportAnsys(strName="", crAnsysJob=None)

```

==========================================================

# Analysis.ExportAbaqus

## Wrapper Macro

ExportAbaqusInp(...)

## Ribbon-GUI-Location

Analysis > ExportAbaqus

## Command Description

export inp file

## Argument List

**Arg1: crAbaJob**

Description: entity in database model with type abaqus job

Data Type: cursor

Default Value : None

Syntax: crAbaJob = EntityType(id)

**Arg2: crlSelectPart**

Description: array entities in model with type select part

Data Type: cursor list

Default Value : []

Syntax: crlSelectPart = [EntityType(id1, id2, id3)]

**Arg3: strInpPath**

Description: definition string of input inp path

Data Type: string

Default Value : ""

Syntax: strInpPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ExportAbaqus(crAbaJob=None, crlSelectPart=[], strInpPath="")

```

==========================================================

# Analysis.ModifyLbcToStep

## Wrapper Macro

AbaModifyLbcToStep(...)

## Ribbon-GUI-Location

Analysis > ModifyLbcToStep

## Command Description

Abaqus analysis output data setting

## Argument List

**Arg1: listAbaqusLbcStepInfo**

Description: list data structure of ABAQUS_LBC_STEP_INFO (refer PSJ Command Data Structure Document)

Data Type: ABAQUS_LBC_STEP_INFO

Default Value : ABAQUS_LBC_STEP_INFO()

Syntax: listAbaqusLbcStepInfo = [ABAQUS_LBC_STEP_INFO(,,,), ABAQUS_LBC_STEP_INFO(,,,)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ModifyLbcToStep(listAbaqusLbcStepInfo=[])

```

==========================================================

# Analysis.ExportAdx

## Wrapper Macro

ExportAdx(...)

## Ribbon-GUI-Location

Analysis > ExportAdx

## Command Description

export adx file

## Argument List

**Arg1: crJob**

Description: entity in database model with type job

Data Type: cursor

Default Value : None

Syntax: crJob = EntityType(id)

**Arg2: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg3: iNumType**

Description: option for number type

Data Type: integer

Default Value : 0

Syntax: iNumType = 1

**Arg4: iUiWidth**

Description: option for ui width

Data Type: integer

Default Value : 10

Syntax: iUiWidth = 1

**Arg5: iUiPrecision**

Description: option for ui precision

Data Type: integer

Default Value : 1

Syntax: iUiPrecision = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ExportAdx(crJob=None, strPath="", iNumType=0, iUiWidth=10, iUiPrecision=1)

```

==========================================================

# Analysis.ExportLsdyna

## Wrapper Macro

ExportLsdyna(...)

## Ribbon-GUI-Location

Analysis > ExportLsdyna

## Command Description

Analysis LSDYNA ExportLsdyna

## Argument List

**Arg1: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg2: crJob**

Description: entity in database model with type job

Data Type: cursor

Default Value : None

Syntax: crJob = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ExportLsdyna(strPath="", crJob=None)

```

==========================================================

# Analysis.NastranJob

## Wrapper Macro

NastranJob(...)

## Ribbon-GUI-Location

Analysis > NastranJob

## Command Description

Create nastran Job

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Job_1"

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: nastranAnalysis**

Description: data structure of NASTRAN_ANALYSIS (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_ANALYSIS

Default Value : NASTRAN_ANALYSIS()

Syntax: nastranAnalysis = NASTRAN_ANALYSIS(,,,)

**Arg5: bDummyPropAutoAssign**

Description: enable or disable feature dummy property auto assign

Data Type: bool

Default Value : False

Syntax: bDummyPropAutoAssign = True/False

**Arg6: iDummyPropMaterialID**

Description: option for dummy property material ID

Data Type: integer

Default Value : 0

Syntax: iDummyPropMaterialID = 1

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.NastranJob(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None)

```

==========================================================

# Analysis.LSDYNAJob

## Wrapper Macro

LsdynaJob(...)

## Ribbon-GUI-Location

Analysis > LSDYNAJob

## Command Description

Create analysis LSDYNA job

## Argument List

**Arg1: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.LSDYNAJob(crEdit=None)

```

==========================================================

# Analysis.ADVC.MakeProcess.Static

## Wrapper Macro

AdvcStaticProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > Static

## Command Description

create static process

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iGeomNonlinear**

Description: option for geom nonlinear

Data Type: integer

Default Value : 0

Syntax: iGeomNonlinear = 1

**Arg3: advcStructTimeStep**

Description: data structure of ADVC_STRUCT_TIME_STEP (refer PSJ Command Data Structure Document)

Data Type: ADVC_STRUCT_TIME_STEP

Default Value : ADVC_STRUCT_TIME_STEP()

Syntax: advcStructTimeStep = ADVC_STRUCT_TIME_STEP(,,,)

**Arg4: bConvergence**

Description: enable or disable feature convergence

Data Type: bool

Default Value : False

Syntax: bConvergence = True/False

**Arg5: advcConvergence**

Description: data structure of ADVC_CONVERGENCE (refer PSJ Command Data Structure Document)

Data Type: ADVC_CONVERGENCE

Default Value : ADVC_CONVERGENCE()

Syntax: advcConvergence = ADVC_CONVERGENCE(,,,)

**Arg6: bContact**

Description: enable or disable feature contact

Data Type: bool

Default Value : False

Syntax: bContact = True/False

**Arg7: advcContactIter**

Description: data structure of ADVC_CONTACT_ITER (refer PSJ Command Data Structure Document)

Data Type: ADVC_CONTACT_ITER

Default Value : ADVC_CONTACT_ITER()

Syntax: advcContactIter = ADVC_CONTACT_ITER(,,,)

**Arg8: bAutoIncrement**

Description: enable or disable feature auto increment

Data Type: bool

Default Value : False

Syntax: bAutoIncrement = True/False

**Arg9: advcAutoIncrement**

Description: data structure of ADVC_AUTO_INCREMENT (refer PSJ Command Data Structure Document)

Data Type: ADVC_AUTO_INCREMENT

Default Value : ADVC_AUTO_INCREMENT()

Syntax: advcAutoIncrement = ADVC_AUTO_INCREMENT(,,,)

**Arg10: dStabilizationFactor**

Description: double value of stabilization factor

Data Type: double

Default Value : 0.0

Syntax: dStabilizationFactor = 1.0

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg12: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg13: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg14: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg15: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

**Arg16: iRefType**

Description: option for ref type

Data Type: integer

Default Value : -1

Syntax: iRefType = 1

**Arg17: strRefPath**

Description: definition string of input ref path

Data Type: string

Default Value : ""

Syntax: strRefPath = "string input"

**Arg18: listAdvcRefStressResult**

Description: list data structure of ADVC_REF_STRESS_RESULT (refer PSJ Command Data Structure Document)

Data Type: ADVC_REF_STRESS_RESULT

Default Value : ADVC_REF_STRESS_RESULT()

Syntax: listAdvcRefStressResult = [ADVC_REF_STRESS_RESULT(,,,), ADVC_REF_STRESS_RESULT(,,,)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.Static(strName="", iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), dStabilizationFactor=0.0, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])

```

==========================================================

# Analysis.ADVC.MakeProcess.Creep

## Wrapper Macro

AdvcCreepProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > Creep

## Command Description

create creep process

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iGeomNonlinear**

Description: option for geom nonlinear

Data Type: integer

Default Value : 0

Syntax: iGeomNonlinear = 1

**Arg3: advcStructTimeStep**

Description: data structure of ADVC_STRUCT_TIME_STEP (refer PSJ Command Data Structure Document)

Data Type: ADVC_STRUCT_TIME_STEP

Default Value : ADVC_STRUCT_TIME_STEP()

Syntax: advcStructTimeStep = ADVC_STRUCT_TIME_STEP(,,,)

**Arg4: bConvergence**

Description: enable or disable feature convergence

Data Type: bool

Default Value : False

Syntax: bConvergence = True/False

**Arg5: advcConvergence**

Description: data structure of ADVC_CONVERGENCE (refer PSJ Command Data Structure Document)

Data Type: ADVC_CONVERGENCE

Default Value : ADVC_CONVERGENCE()

Syntax: advcConvergence = ADVC_CONVERGENCE(,,,)

**Arg6: bContact**

Description: enable or disable feature contact

Data Type: bool

Default Value : False

Syntax: bContact = True/False

**Arg7: advcContactIter**

Description: data structure of ADVC_CONTACT_ITER (refer PSJ Command Data Structure Document)

Data Type: ADVC_CONTACT_ITER

Default Value : ADVC_CONTACT_ITER()

Syntax: advcContactIter = ADVC_CONTACT_ITER(,,,)

**Arg8: bAutoIncrement**

Description: enable or disable feature auto increment

Data Type: bool

Default Value : False

Syntax: bAutoIncrement = True/False

**Arg9: advcAutoIncrement**

Description: data structure of ADVC_AUTO_INCREMENT (refer PSJ Command Data Structure Document)

Data Type: ADVC_AUTO_INCREMENT

Default Value : ADVC_AUTO_INCREMENT()

Syntax: advcAutoIncrement = ADVC_AUTO_INCREMENT(,,,)

**Arg10: dStabilizationFactor**

Description: double value of stabilization factor

Data Type: double

Default Value : DFLT_DBL

Syntax: dStabilizationFactor = 1.0

**Arg11: bThetaDefined**

Description: enable or disable feature theta defined

Data Type: bool

Default Value : False

Syntax: bThetaDefined = True/False

**Arg12: dTheta**

Description: double value of theta

Data Type: double

Default Value : DFLT_DBL

Syntax: dTheta = 1.0

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg15: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg16: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg17: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

**Arg18: iRefType**

Description: option for ref type

Data Type: integer

Default Value : -1

Syntax: iRefType = 1

**Arg19: strRefPath**

Description: definition string of input ref path

Data Type: string

Default Value : ""

Syntax: strRefPath = "string input"

**Arg20: listAdvcRefStressResult**

Description: list data structure of ADVC_REF_STRESS_RESULT (refer PSJ Command Data Structure Document)

Data Type: ADVC_REF_STRESS_RESULT

Default Value : ADVC_REF_STRESS_RESULT()

Syntax: listAdvcRefStressResult = [ADVC_REF_STRESS_RESULT(,,,), ADVC_REF_STRESS_RESULT(,,,)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.Creep(strName="", iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), dStabilizationFactor=DFLT_DBL, bThetaDefined=False, dTheta=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])

```

==========================================================

# Analysis.ADVC.MakeProcess.Dynamic

## Wrapper Macro

AdvcDynamicProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > Dynamic

## Command Description

create dynamic process

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iGeomNonlinear**

Description: option for geom nonlinear

Data Type: integer

Default Value : 0

Syntax: iGeomNonlinear = 1

**Arg3: advcStructTimeStep**

Description: data structure of ADVC_STRUCT_TIME_STEP (refer PSJ Command Data Structure Document)

Data Type: ADVC_STRUCT_TIME_STEP

Default Value : ADVC_STRUCT_TIME_STEP()

Syntax: advcStructTimeStep = ADVC_STRUCT_TIME_STEP(,,,)

**Arg4: bConvergence**

Description: enable or disable feature convergence

Data Type: bool

Default Value : False

Syntax: bConvergence = True/False

**Arg5: advcConvergence**

Description: data structure of ADVC_CONVERGENCE (refer PSJ Command Data Structure Document)

Data Type: ADVC_CONVERGENCE

Default Value : ADVC_CONVERGENCE()

Syntax: advcConvergence = ADVC_CONVERGENCE(,,,)

**Arg6: bContact**

Description: enable or disable feature contact

Data Type: bool

Default Value : False

Syntax: bContact = True/False

**Arg7: advcContactIter**

Description: data structure of ADVC_CONTACT_ITER (refer PSJ Command Data Structure Document)

Data Type: ADVC_CONTACT_ITER

Default Value : ADVC_CONTACT_ITER()

Syntax: advcContactIter = ADVC_CONTACT_ITER(,,,)

**Arg8: bAutoIncrement**

Description: enable or disable feature auto increment

Data Type: bool

Default Value : False

Syntax: bAutoIncrement = True/False

**Arg9: advcAutoIncrement**

Description: data structure of ADVC_AUTO_INCREMENT (refer PSJ Command Data Structure Document)

Data Type: ADVC_AUTO_INCREMENT

Default Value : ADVC_AUTO_INCREMENT()

Syntax: advcAutoIncrement = ADVC_AUTO_INCREMENT(,,,)

**Arg10: bDynamic**

Description: enable or disable feature dynamic

Data Type: bool

Default Value : False

Syntax: bDynamic = True/False

**Arg11: advcDynamic**

Description: data structure of ADVC_DYNAMIC (refer PSJ Command Data Structure Document)

Data Type: ADVC_DYNAMIC

Default Value : ADVC_DYNAMIC()

Syntax: advcDynamic = ADVC_DYNAMIC(,,,)

**Arg12: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg13: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg14: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg15: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg16: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

**Arg17: iRefType**

Description: option for ref type

Data Type: integer

Default Value : -1

Syntax: iRefType = 1

**Arg18: strRefPath**

Description: definition string of input ref path

Data Type: string

Default Value : ""

Syntax: strRefPath = "string input"

**Arg19: listAdvcRefStressResult**

Description: list data structure of ADVC_REF_STRESS_RESULT (refer PSJ Command Data Structure Document)

Data Type: ADVC_REF_STRESS_RESULT

Default Value : ADVC_REF_STRESS_RESULT()

Syntax: listAdvcRefStressResult = [ADVC_REF_STRESS_RESULT(,,,), ADVC_REF_STRESS_RESULT(,,,)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.Dynamic(strName="", iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), bDynamic=False, advcDynamic=ADVC_DYNAMIC(), crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])

```

==========================================================

# Analysis.ADVC.MakeProcess.EigenValue

## Wrapper Macro

AdvcEigenProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > EigenValue

## Command Description

create advc eigen value process

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: bEigenValue**

Description: enable or disable feature eigen value

Data Type: bool

Default Value : False

Syntax: bEigenValue = True/False

**Arg3: iNumberOfModes**

Description: option for number of modes

Data Type: integer

Default Value : 0

Syntax: iNumberOfModes = 1

**Arg4: iEigenvecNorm**

Description: option for eigenvec norm

Data Type: integer

Default Value : 10

Syntax: iEigenvecNorm = 1

**Arg5: dShift**

Description: double value of shift

Data Type: double

Default Value : DFLT_DBL

Syntax: dShift = 1.0

**Arg6: dCgcgpiTol**

Description: double value of cgcgpi tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgcgpiTol = 1.0

**Arg7: dCgcgpiEigTol**

Description: double value of cgcgpi eig tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgcgpiEigTol = 1.0

**Arg8: iCgcgpiLoopMax**

Description: option for cgcgpi loop maximize

Data Type: integer

Default Value : DFLT_INT

Syntax: iCgcgpiLoopMax = 1

**Arg9: dCgcgpiInnerTol**

Description: double value of cgcgpi inner tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgcgpiInnerTol = 1.0

**Arg10: iCgcgpiBlockSize**

Description: option for cgcgpi block size

Data Type: integer

Default Value : DFLT_INT

Syntax: iCgcgpiBlockSize = 1

**Arg11: iCgcgpiExtraMode**

Description: option for cgcgpi extra mode

Data Type: integer

Default Value : DFLT_INT

Syntax: iCgcgpiExtraMode = 1

**Arg12: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg13: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg14: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg15: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg16: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

**Arg17: iRefType**

Description: option for ref type

Data Type: integer

Default Value : -1

Syntax: iRefType = 1

**Arg18: strRefPath**

Description: definition string of input ref path

Data Type: string

Default Value : ""

Syntax: strRefPath = "string input"

**Arg19: listAdvcRefStressResult**

Description: list data structure of ADVC_REF_STRESS_RESULT (refer PSJ Command Data Structure Document)

Data Type: ADVC_REF_STRESS_RESULT

Default Value : ADVC_REF_STRESS_RESULT()

Syntax: listAdvcRefStressResult = [ADVC_REF_STRESS_RESULT(,,,), ADVC_REF_STRESS_RESULT(,,,)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.EigenValue(strName="", bEigenValue=False, iNumberOfModes=0, iEigenvecNorm=10, dShift=DFLT_DBL, dCgcgpiTol=DFLT_DBL, dCgcgpiEigTol=DFLT_DBL, iCgcgpiLoopMax=DFLT_INT, dCgcgpiInnerTol=DFLT_DBL, iCgcgpiBlockSize=DFLT_INT, iCgcgpiExtraMode=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])

```

==========================================================

# Analysis.ADVC.MakeProcess.DynamicExplicit

## Wrapper Macro

AdvcDynamicExplicitProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > DynamicExplicit

## Command Description

create dynamic explicit process.

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iGeomNonlinear**

Description: option for geom nonlinear

Data Type: integer

Default Value : 0

Syntax: iGeomNonlinear = 1

**Arg3: advcStructTimeStep**

Description: data structure of ADVC_STRUCT_TIME_STEP (refer PSJ Command Data Structure Document)

Data Type: ADVC_STRUCT_TIME_STEP

Default Value : ADVC_STRUCT_TIME_STEP()

Syntax: advcStructTimeStep = ADVC_STRUCT_TIME_STEP(,,,)

**Arg4: bConvergence**

Description: enable or disable feature convergence

Data Type: bool

Default Value : False

Syntax: bConvergence = True/False

**Arg5: advcConvergence**

Description: data structure of ADVC_CONVERGENCE (refer PSJ Command Data Structure Document)

Data Type: ADVC_CONVERGENCE

Default Value : ADVC_CONVERGENCE()

Syntax: advcConvergence = ADVC_CONVERGENCE(,,,)

**Arg6: bContact**

Description: enable or disable feature contact

Data Type: bool

Default Value : False

Syntax: bContact = True/False

**Arg7: advcContactIter**

Description: data structure of ADVC_CONTACT_ITER (refer PSJ Command Data Structure Document)

Data Type: ADVC_CONTACT_ITER

Default Value : ADVC_CONTACT_ITER()

Syntax: advcContactIter = ADVC_CONTACT_ITER(,,,)

**Arg8: bAutoIncrement**

Description: enable or disable feature auto increment

Data Type: bool

Default Value : False

Syntax: bAutoIncrement = True/False

**Arg9: advcAutoIncrement**

Description: data structure of ADVC_AUTO_INCREMENT (refer PSJ Command Data Structure Document)

Data Type: ADVC_AUTO_INCREMENT

Default Value : ADVC_AUTO_INCREMENT()

Syntax: advcAutoIncrement = ADVC_AUTO_INCREMENT(,,,)

**Arg10: iLogMessageInterval**

Description: option for log message interval

Data Type: integer

Default Value : DFLT_INT

Syntax: iLogMessageInterval = 1

**Arg11: iLinearApproximation**

Description: option for linear approximation

Data Type: integer

Default Value : -1

Syntax: iLinearApproximation = 1

**Arg12: dBulkViscosityCoef1**

Description: double value of bulk viscosity coef1

Data Type: double

Default Value : DFLT_DBL

Syntax: dBulkViscosityCoef1 = 1.0

**Arg13: dBulkViscosityCoef2**

Description: double value of bulk viscosity coef2

Data Type: double

Default Value : DFLT_DBL

Syntax: dBulkViscosityCoef2 = 1.0

**Arg14: dMassScalingdt**

Description: double value of mass scalingdt

Data Type: double

Default Value : DFLT_DBL

Syntax: dMassScalingdt = 1.0

**Arg15: dDtScaleFactor**

Description: double value of dt scale factor

Data Type: double

Default Value : DFLT_DBL

Syntax: dDtScaleFactor = 1.0

**Arg16: dPenaltyScaleFactor**

Description: double value of penalty scale factor

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyScaleFactor = 1.0

**Arg17: iContactSearchInterval**

Description: option for contact search interval

Data Type: integer

Default Value : DFLT_INT

Syntax: iContactSearchInterval = 1

**Arg18: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg19: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg20: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg21: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg22: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

**Arg23: iRefType**

Description: option for ref type

Data Type: integer

Default Value : -1

Syntax: iRefType = 1

**Arg24: strRefPath**

Description: definition string of input ref path

Data Type: string

Default Value : ""

Syntax: strRefPath = "string input"

**Arg25: listAdvcRefStressResult**

Description: list data structure of ADVC_REF_STRESS_RESULT (refer PSJ Command Data Structure Document)

Data Type: ADVC_REF_STRESS_RESULT

Default Value : ADVC_REF_STRESS_RESULT()

Syntax: listAdvcRefStressResult = [ADVC_REF_STRESS_RESULT(,,,), ADVC_REF_STRESS_RESULT(,,,)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.DynamicExplicit(strName="", iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), iLogMessageInterval=DFLT_INT, iLinearApproximation=-1, dBulkViscosityCoef1=DFLT_DBL, dBulkViscosityCoef2=DFLT_DBL, dMassScalingdt=DFLT_DBL, dDtScaleFactor=DFLT_DBL, dPenaltyScaleFactor=DFLT_DBL, iContactSearchInterval=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])

```

==========================================================

# Analysis.ADVC.MakeProcess.ModalFreqResp

## Wrapper Macro

AdvcModalFreqRespProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > ModalFreqResp

## Command Description

create modal frequency response process of ADVC

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strRefEigenDir**

Description: definition string of input ref eigen dir

Data Type: string

Default Value : ""

Syntax: strRefEigenDir = "string input"

**Arg3: dRefLowFreq**

Description: double value of ref low frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dRefLowFreq = 1.0

**Arg4: dRefHighFreq**

Description: double value of ref high frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dRefHighFreq = 1.0

**Arg5: crModalDampingRatio**

Description: entity in database model with type modal damping ratio

Data Type: cursor

Default Value : None

Syntax: crModalDampingRatio = EntityType(id)

**Arg6: crExcitationFreq**

Description: entity in database model with type excitation frequency

Data Type: cursor

Default Value : None

Syntax: crExcitationFreq = EntityType(id)

**Arg7: bAutoFreqInterval**

Description: enable or disable feature auto frequency interval

Data Type: bool

Default Value : False

Syntax: bAutoFreqInterval = True/False

**Arg8: dMaxFreq**

Description: double value of maximize frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxFreq = 1.0

**Arg9: dMinFreq**

Description: double value of minimize frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dMinFreq = 1.0

**Arg10: iNumFreqPoint**

Description: option for number frequency point

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumFreqPoint = 1

**Arg11: dBiasParam**

Description: double value of bias parameter

Data Type: double

Default Value : DFLT_DBL

Syntax: dBiasParam = 1.0

**Arg12: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg13: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg14: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg15: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg16: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

**Arg17: iRefType**

Description: option for ref type

Data Type: integer

Default Value : -1

Syntax: iRefType = 1

**Arg18: strRefPath**

Description: definition string of input ref path

Data Type: string

Default Value : ""

Syntax: strRefPath = "string input"

**Arg19: listAdvcRefStressResult**

Description: list data structure of ADVC_REF_STRESS_RESULT (refer PSJ Command Data Structure Document)

Data Type: ADVC_REF_STRESS_RESULT

Default Value : ADVC_REF_STRESS_RESULT()

Syntax: listAdvcRefStressResult = [ADVC_REF_STRESS_RESULT(,,,), ADVC_REF_STRESS_RESULT(,,,)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.ModalFreqResp(strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT_DBL, dMinFreq=DFLT_DBL, iNumFreqPoint=DFLT_INT, dBiasParam=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])

```

==========================================================

# Analysis.ADVC.MakeProcess.ResponseSpectrum

## Wrapper Macro

AdvcSpectrumProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > ResponseSpectrum

## Command Description

create advc response spectrum process

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strRefEigenDir**

Description: definition string of input ref eigen dir

Data Type: string

Default Value : ""

Syntax: strRefEigenDir = "string input"

**Arg3: dRefLowFreq**

Description: double value of ref low frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dRefLowFreq = 1.0

**Arg4: dRefHighFreq**

Description: double value of ref high frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dRefHighFreq = 1.0

**Arg5: iPropMethod**

Description: option for property method

Data Type: integer

Default Value : 0

Syntax: iPropMethod = 1

**Arg6: iSpttype**

Description: option for spttype

Data Type: integer

Default Value : 0

Syntax: iSpttype = 1

**Arg7: dSptFactor0**

Description: double value of spt factor0

Data Type: double

Default Value : DFLT_DBL

Syntax: dSptFactor0 = 1.0

**Arg8: crSpt0**

Description: entity in database model with type spt0

Data Type: cursor

Default Value : None

Syntax: crSpt0 = EntityType(id)

**Arg9: dSptFactor1**

Description: double value of spt factor1

Data Type: double

Default Value : DFLT_DBL

Syntax: dSptFactor1 = 1.0

**Arg10: crSpt1**

Description: entity in database model with type spt1

Data Type: cursor

Default Value : None

Syntax: crSpt1 = EntityType(id)

**Arg11: dSptFactor2**

Description: double value of spt factor2

Data Type: double

Default Value : DFLT_DBL

Syntax: dSptFactor2 = 1.0

**Arg12: crSpt2**

Description: entity in database model with type spt2

Data Type: cursor

Default Value : None

Syntax: crSpt2 = EntityType(id)

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg15: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg16: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg17: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

**Arg18: iRefType**

Description: option for ref type

Data Type: integer

Default Value : 0

Syntax: iRefType = 1

**Arg19: strRefPath**

Description: definition string of input ref path

Data Type: string

Default Value : ""

Syntax: strRefPath = "string input"

**Arg20: listAdvcRefStressResult**

Description: list data structure of ADVC_REF_STRESS_RESULT (refer PSJ Command Data Structure Document)

Data Type: ADVC_REF_STRESS_RESULT

Default Value : ADVC_REF_STRESS_RESULT()

Syntax: listAdvcRefStressResult = [ADVC_REF_STRESS_RESULT(,,,), ADVC_REF_STRESS_RESULT(,,,)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.ResponseSpectrum(strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, iPropMethod=0, iSpttype=0, dSptFactor0=DFLT_DBL, crSpt0=None, dSptFactor1=DFLT_DBL, crSpt1=None, dSptFactor2=DFLT_DBL, crSpt2=None, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=0, strRefPath="", listAdvcRefStressResult=[])

```

==========================================================

# Analysis.ADVC.MakeProcess.SteadyState

## Wrapper Macro

AdvcSSHProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > SteadyState

## Command Description

create advc heat transfer steady state process

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iEndType**

Description: option for end type

Data Type: integer

Default Value : 1

Syntax: iEndType = 1

**Arg3: dMaxTime**

Description: double value of maximize time

Data Type: double

Default Value : 1

Syntax: dMaxTime = 1.0

**Arg4: iFixedOrAuto**

Description: option for fixed or auto

Data Type: integer

Default Value : 0

Syntax: iFixedOrAuto = 1

**Arg5: dMaxChange**

Description: double value of maximize change

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxChange = 1.0

**Arg6: dInitDt**

Description: double value of init dt

Data Type: double

Default Value : DFLT_DBL

Syntax: dInitDt = 1.0

**Arg7: iDefineMaxDt**

Description: option for define maximize dt

Data Type: integer

Default Value : 0

Syntax: iDefineMaxDt = 1

**Arg8: dMaxDt**

Description: double value of maximize dt

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxDt = 1.0

**Arg9: iDefineMinDt**

Description: option for define minimize dt

Data Type: integer

Default Value : 0

Syntax: iDefineMinDt = 1

**Arg10: dMinDt**

Description: double value of minimize dt

Data Type: double

Default Value : DFLT_DBL

Syntax: dMinDt = 1.0

**Arg11: dFixedDt**

Description: double value of fixed dt

Data Type: double

Default Value : DFLT_DBL

Syntax: dFixedDt = 1.0

**Arg12: iOutputLast**

Description: option for output last

Data Type: integer

Default Value : -1

Syntax: iOutputLast = 1

**Arg13: iOutputInterval**

Description: option for output interval

Data Type: integer

Default Value : DFLT_INT

Syntax: iOutputInterval = 1

**Arg14: iRestartLast**

Description: option for restart last

Data Type: integer

Default Value : -1

Syntax: iRestartLast = 1

**Arg15: iRestartInterval**

Description: option for restart interval

Data Type: integer

Default Value : DFLT_INT

Syntax: iRestartInterval = 1

**Arg16: dOutputTimeInterval**

Description: double value of output time interval

Data Type: double

Default Value : DFLT_DBL

Syntax: dOutputTimeInterval = 1.0

**Arg17: dRestartTimeInterval**

Description: double value of restart time interval

Data Type: double

Default Value : DFLT_DBL

Syntax: dRestartTimeInterval = 1.0

**Arg18: iOutputInit**

Description: option for output init

Data Type: integer

Default Value : -1

Syntax: iOutputInit = 1

**Arg19: iListOutputInterval**

Description: option for list output interval

Data Type: integer

Default Value : DFLT_INT

Syntax: iListOutputInterval = 1

**Arg20: bConvergence**

Description: enable or disable feature convergence

Data Type: bool

Default Value : False

Syntax: bConvergence = True/False

**Arg21: dCgTol**

Description: double value of cg tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgTol = 1.0

**Arg22: dCgNrTol**

Description: double value of cg nr tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgNrTol = 1.0

**Arg23: dCgDispTol**

Description: double value of cg disp tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgDispTol = 1.0

**Arg24: dCgNrDispTol**

Description: double value of cg nr disp tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgNrDispTol = 1.0

**Arg25: dCgDispLimitTol**

Description: double value of cg disp limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgDispLimitTol = 1.0

**Arg26: dCgTotalDispLimitTol**

Description: double value of cg total disp limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgTotalDispLimitTol = 1.0

**Arg27: dNewtonTol**

Description: double value of newton tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dNewtonTol = 1.0

**Arg28: dNewtonDispTol**

Description: double value of newton disp tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dNewtonDispTol = 1.0

**Arg29: dNewtonDispLimitTol**

Description: double value of newton disp limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dNewtonDispLimitTol = 1.0

**Arg30: dNewtonTotalDispLimitTol**

Description: double value of newton total disp limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dNewtonTotalDispLimitTol = 1.0

**Arg31: iCgloopMax**

Description: option for cgloop maximize

Data Type: integer

Default Value : DFLT_INT

Syntax: iCgloopMax = 1

**Arg32: iNewtonMax**

Description: option for newton maximize

Data Type: integer

Default Value : DFLT_INT

Syntax: iNewtonMax = 1

**Arg33: dHtNlLoopTol**

Description: double value of ht nl loop tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dHtNlLoopTol = 1.0

**Arg34: iHtNlLoopMax**

Description: option for ht nl loop maximize

Data Type: integer

Default Value : DFLT_INT

Syntax: iHtNlLoopMax = 1

**Arg35: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg36: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg37: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg38: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg39: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.SteadyState(strName="", iEndType=1, dMaxTime=1, iFixedOrAuto=0, dMaxChange=DFLT_DBL, dInitDt=DFLT_DBL, iDefineMaxDt=0, dMaxDt=DFLT_DBL, iDefineMinDt=0, dMinDt=DFLT_DBL, dFixedDt=DFLT_DBL, iOutputLast=-1, iOutputInterval=DFLT_INT, iRestartLast=-1, iRestartInterval=DFLT_INT, dOutputTimeInterval=DFLT_DBL, dRestartTimeInterval=DFLT_DBL, iOutputInit=-1, iListOutputInterval=DFLT_INT, bConvergence=False, dCgTol=DFLT_DBL, dCgNrTol=DFLT_DBL, dCgDispTol=DFLT_DBL, dCgNrDispTol=DFLT_DBL, dCgDispLimitTol=DFLT_DBL, dCgTotalDispLimitTol=DFLT_DBL, dNewtonTol=DFLT_DBL, dNewtonDispTol=DFLT_DBL, dNewtonDispLimitTol=DFLT_DBL, dNewtonTotalDispLimitTol=DFLT_DBL, iCgloopMax=DFLT_INT, iNewtonMax=DFLT_INT, dHtNlLoopTol=DFLT_DBL, iHtNlLoopMax=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[])

```

==========================================================

# Analysis.ADVC.MakeProcess.Transient

## Wrapper Macro

AdvcTHProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > Transient

## Command Description

create advc heat transfer transient process

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iEndType**

Description: option for end type

Data Type: integer

Default Value : 1

Syntax: iEndType = 1

**Arg3: dMaxTime**

Description: double value of maximize time

Data Type: double

Default Value : 1

Syntax: dMaxTime = 1.0

**Arg4: dSteadyRate**

Description: double value of steady rate

Data Type: double

Default Value : 0.0

Syntax: dSteadyRate = 1.0

**Arg5: iFixedOrAuto**

Description: option for fixed or auto

Data Type: integer

Default Value : 0

Syntax: iFixedOrAuto = 1

**Arg6: dMaxChange**

Description: double value of maximize change

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxChange = 1.0

**Arg7: dInitDt**

Description: double value of init dt

Data Type: double

Default Value : DFLT_DBL

Syntax: dInitDt = 1.0

**Arg8: iDefineMaxDt**

Description: option for define maximize dt

Data Type: integer

Default Value : 0

Syntax: iDefineMaxDt = 1

**Arg9: dMaxDt**

Description: double value of maximize dt

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxDt = 1.0

**Arg10: iDefineMinDt**

Description: option for define minimize dt

Data Type: integer

Default Value : 0

Syntax: iDefineMinDt = 1

**Arg11: dMinDt**

Description: double value of minimize dt

Data Type: double

Default Value : DFLT_DBL

Syntax: dMinDt = 1.0

**Arg12: dFixedDt**

Description: double value of fixed dt

Data Type: double

Default Value : DFLT_DBL

Syntax: dFixedDt = 1.0

**Arg13: iOutputLast**

Description: option for output last

Data Type: integer

Default Value : -1

Syntax: iOutputLast = 1

**Arg14: iOutputInterval**

Description: option for output interval

Data Type: integer

Default Value : DFLT_INT

Syntax: iOutputInterval = 1

**Arg15: iRestartLast**

Description: option for restart last

Data Type: integer

Default Value : -1

Syntax: iRestartLast = 1

**Arg16: iRestartInterval**

Description: option for restart interval

Data Type: integer

Default Value : DFLT_INT

Syntax: iRestartInterval = 1

**Arg17: dOutputTimeInterval**

Description: double value of output time interval

Data Type: double

Default Value : DFLT_DBL

Syntax: dOutputTimeInterval = 1.0

**Arg18: dRestartTimeInterval**

Description: double value of restart time interval

Data Type: double

Default Value : DFLT_DBL

Syntax: dRestartTimeInterval = 1.0

**Arg19: iOutputInit**

Description: option for output init

Data Type: integer

Default Value : -1

Syntax: iOutputInit = 1

**Arg20: iListOutputInterval**

Description: option for list output interval

Data Type: integer

Default Value : DFLT_INT

Syntax: iListOutputInterval = 1

**Arg21: bConvergence**

Description: enable or disable feature convergence

Data Type: bool

Default Value : False

Syntax: bConvergence = True/False

**Arg22: dCgTol**

Description: double value of cg tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgTol = 1.0

**Arg23: dCgNrTol**

Description: double value of cg nr tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgNrTol = 1.0

**Arg24: dCgDispTol**

Description: double value of cg disp tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgDispTol = 1.0

**Arg25: dCgNrDispTol**

Description: double value of cg nr disp tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgNrDispTol = 1.0

**Arg26: dCgDispLimitTol**

Description: double value of cg disp limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgDispLimitTol = 1.0

**Arg27: dCgTotalDispLimitTol**

Description: double value of cg total disp limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dCgTotalDispLimitTol = 1.0

**Arg28: dNewtonTol**

Description: double value of newton tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dNewtonTol = 1.0

**Arg29: dNewtonDispTol**

Description: double value of newton disp tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dNewtonDispTol = 1.0

**Arg30: dNewtonDispLimitTol**

Description: double value of newton disp limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dNewtonDispLimitTol = 1.0

**Arg31: dNewtonTotalDispLimitTol**

Description: double value of newton total disp limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dNewtonTotalDispLimitTol = 1.0

**Arg32: iCgloopMax**

Description: option for cgloop maximize

Data Type: integer

Default Value : DFLT_INT

Syntax: iCgloopMax = 1

**Arg33: iNewtonMax**

Description: option for newton maximize

Data Type: integer

Default Value : DFLT_INT

Syntax: iNewtonMax = 1

**Arg34: dHtNlLoopTol**

Description: double value of ht nl loop tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dHtNlLoopTol = 1.0

**Arg35: iHtNlLoopMax**

Description: option for ht nl loop maximize

Data Type: integer

Default Value : DFLT_INT

Syntax: iHtNlLoopMax = 1

**Arg36: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg37: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg38: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg39: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg40: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.Transient(strName="", iEndType=1, dMaxTime=1, dSteadyRate=0.0, iFixedOrAuto=0, dMaxChange=DFLT_DBL, dInitDt=DFLT_DBL, iDefineMaxDt=0, dMaxDt=DFLT_DBL, iDefineMinDt=0, dMinDt=DFLT_DBL, dFixedDt=DFLT_DBL, iOutputLast=-1, iOutputInterval=DFLT_INT, iRestartLast=-1, iRestartInterval=DFLT_INT, dOutputTimeInterval=DFLT_DBL, dRestartTimeInterval=DFLT_DBL, iOutputInit=-1, iListOutputInterval=DFLT_INT, bConvergence=False, dCgTol=DFLT_DBL, dCgNrTol=DFLT_DBL, dCgDispTol=DFLT_DBL, dCgNrDispTol=DFLT_DBL, dCgDispLimitTol=DFLT_DBL, dCgTotalDispLimitTol=DFLT_DBL, dNewtonTol=DFLT_DBL, dNewtonDispTol=DFLT_DBL, dNewtonDispLimitTol=DFLT_DBL, dNewtonTotalDispLimitTol=DFLT_DBL, iCgloopMax=DFLT_INT, iNewtonMax=DFLT_INT, dHtNlLoopTol=DFLT_DBL, iHtNlLoopMax=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[])

```

==========================================================

# Analysis.ADVC.MakeProcess.Fatigue

## Wrapper Macro

AdvcFatigueProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > Fatigue

## Command Description

create advc fatigue process

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: bFatigue**

Description: enable or disable feature fatigue

Data Type: bool

Default Value : False

Syntax: bFatigue = True/False

**Arg3: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg4: iStressAxis**

Description: option for stress axis

Data Type: integer

Default Value : 0

Syntax: iStressAxis = 1

**Arg5: iSafetyType**

Description: option for safety type

Data Type: integer

Default Value : 0

Syntax: iSafetyType = 1

**Arg6: dSearchResolution**

Description: double value of search resolution

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchResolution = 1.0

**Arg7: dSafetyMax**

Description: double value of safety maximize

Data Type: double

Default Value : DFLT_DBL

Syntax: dSafetyMax = 1.0

**Arg8: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg9: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg10: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg11: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg12: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

**Arg13: iRefType**

Description: option for ref type

Data Type: integer

Default Value : -1

Syntax: iRefType = 1

**Arg14: strRefPath**

Description: definition string of input ref path

Data Type: string

Default Value : ""

Syntax: strRefPath = "string input"

**Arg15: listAdvcRefStressResult**

Description: list data structure of ADVC_REF_STRESS_RESULT (refer PSJ Command Data Structure Document)

Data Type: ADVC_REF_STRESS_RESULT

Default Value : ADVC_REF_STRESS_RESULT()

Syntax: listAdvcRefStressResult = [ADVC_REF_STRESS_RESULT(,,,), ADVC_REF_STRESS_RESULT(,,,)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.Fatigue(strName="", bFatigue=False, iMethod=0, iStressAxis=0, iSafetyType=0, dSearchResolution=DFLT_DBL, dSafetyMax=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])

```

==========================================================

# Analysis.ADVC.MakeProcess.RandomResponse

## Wrapper Macro

AdvcRandomProcess(...)

## Ribbon-GUI-Location

Analysis > ADVC > MakeProcess > RandomResponse

## Command Description

create advc random response process

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strRefEigenDir**

Description: definition string of input ref eigen dir

Data Type: string

Default Value : ""

Syntax: strRefEigenDir = "string input"

**Arg3: dRefLowFreq**

Description: double value of ref low frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dRefLowFreq = 1.0

**Arg4: dRefHighFreq**

Description: double value of ref high frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dRefHighFreq = 1.0

**Arg5: crModalDampingRatio**

Description: entity in database model with type modal damping ratio

Data Type: cursor

Default Value : None

Syntax: crModalDampingRatio = EntityType(id)

**Arg6: crExcitationFreq**

Description: entity in database model with type excitation frequency

Data Type: cursor

Default Value : None

Syntax: crExcitationFreq = EntityType(id)

**Arg7: bAutoFreqInterval**

Description: enable or disable feature auto frequency interval

Data Type: bool

Default Value : False

Syntax: bAutoFreqInterval = True/False

**Arg8: dMaxFreq**

Description: double value of maximize frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxFreq = 1.0

**Arg9: dMinFreq**

Description: double value of minimize frequency

Data Type: double

Default Value : DFLT_DBL

Syntax: dMinFreq = 1.0

**Arg10: iNumFreqPoint**

Description: option for number frequency point

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumFreqPoint = 1

**Arg11: dBiasParam**

Description: double value of bias parameter

Data Type: double

Default Value : DFLT_DBL

Syntax: dBiasParam = 1.0

**Arg12: iPropMethod**

Description: option for property method

Data Type: integer

Default Value : 0

Syntax: iPropMethod = 1

**Arg13: iPSDtype**

Description: option for p s dtype

Data Type: integer

Default Value : -1

Syntax: iPSDtype = 1

**Arg14: iPSDdir**

Description: option for p s ddir

Data Type: integer

Default Value : 0

Syntax: iPSDdir = 1

**Arg15: crPSDLoad**

Description: entity in database model with type p s d load

Data Type: cursor

Default Value : None

Syntax: crPSDLoad = EntityType(id)

**Arg16: dPSDFactor**

Description: double value of p s d factor

Data Type: double

Default Value : DFLT_DBL

Syntax: dPSDFactor = 1.0

**Arg17: dGravityAccel**

Description: double value of gravity accel

Data Type: double

Default Value : DFLT_DBL

Syntax: dGravityAccel = 1.0

**Arg18: iOutputEigenFreqStep**

Description: option for output eigen frequency step

Data Type: integer

Default Value : -1

Syntax: iOutputEigenFreqStep = 1

**Arg19: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg20: listLoadNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg21: listLoadCaseNode**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadCaseNode = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg22: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg23: ilOutputParamList**

Description: array int values of output parameter list

Data Type: int list

Default Value : []

Syntax: ilOutputParamList = [1,2,3,4]

**Arg24: iRefType**

Description: option for ref type

Data Type: integer

Default Value : -1

Syntax: iRefType = 1

**Arg25: strRefPath**

Description: definition string of input ref path

Data Type: string

Default Value : ""

Syntax: strRefPath = "string input"

**Arg26: listAdvcRefStressResult**

Description: list data structure of ADVC_REF_STRESS_RESULT (refer PSJ Command Data Structure Document)

Data Type: ADVC_REF_STRESS_RESULT

Default Value : ADVC_REF_STRESS_RESULT()

Syntax: listAdvcRefStressResult = [ADVC_REF_STRESS_RESULT(,,,), ADVC_REF_STRESS_RESULT(,,,)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.MakeProcess.RandomResponse(strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT_DBL, dMinFreq=DFLT_DBL, iNumFreqPoint=DFLT_INT, dBiasParam=DFLT_DBL, iPropMethod=0, iPSDtype=-1, iPSDdir=0, crPSDLoad=None, dPSDFactor=DFLT_DBL, dGravityAccel=DFLT_DBL, iOutputEigenFreqStep=-1, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[])

```

==========================================================

# Analysis.ADVC.Structure

## Wrapper Macro

ADVC_Structure(...)

## Ribbon-GUI-Location

Analysis > ADVC > Structure

## Command Description

create advc job

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: iEJobType**

Description: option for e job type

Data Type: integer

Default Value : 0

Syntax: iEJobType = 1

**Arg4: crlProcessSequence**

Description: array entities in model with type process sequence

Data Type: cursor list

Default Value : []

Syntax: crlProcessSequence = [EntityType(id1, id2, id3)]

**Arg5: crlElemLocationGroup**

Description: array entities in model with type element location group

Data Type: cursor list

Default Value : []

Syntax: crlElemLocationGroup = [EntityType(id1, id2, id3)]

**Arg6: crlNodeLocationGroup**

Description: array entities in model with type node location group

Data Type: cursor list

Default Value : []

Syntax: crlNodeLocationGroup = [EntityType(id1, id2, id3)]

**Arg7: bWriteGroup**

Description: enable or disable feature write group

Data Type: bool

Default Value : False

Syntax: bWriteGroup = True/False

**Arg8: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg9: bResultReference**

Description: enable or disable feature result reference

Data Type: bool

Default Value : False

Syntax: bResultReference = True/False

**Arg10: iSeparateFile**

Description: option for separate file

Data Type: integer

Default Value : 0

Syntax: iSeparateFile = 1

**Arg11: bExportRelatedAllLBCs**

Description: enable or disable feature export related all l b cs

Data Type: bool

Default Value : False

Syntax: bExportRelatedAllLBCs = True/False

**Arg12: bUseEntityName**

Description: enable or disable feature use entity name

Data Type: bool

Default Value : False

Syntax: bUseEntityName = True/False

**Arg13: bMatrixSloverParam**

Description: enable or disable feature matrix slover parameter

Data Type: bool

Default Value : False

Syntax: bMatrixSloverParam = True/False

**Arg14: iPreconditionType**

Description: option for precondition type

Data Type: integer

Default Value : 0

Syntax: iPreconditionType = 1

**Arg15: iMatrixStructure**

Description: option for matrix structure

Data Type: integer

Default Value : 0

Syntax: iMatrixStructure = 1

**Arg16: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg17: iLoadType**

Description: option for load type

Data Type: integer

Default Value : 1

Syntax: iLoadType = 1

**Arg18: bSameOutputOnAllProcess**

Description: enable or disable feature same output on all process

Data Type: bool

Default Value : True

Syntax: bSameOutputOnAllProcess = True/False

**Arg19: bDeleteFloatingNode**

Description: enable or disable feature delete floating node

Data Type: bool

Default Value : True

Syntax: bDeleteFloatingNode = True/False

**Arg20: bBC**

Description: enable or disable feature b c

Data Type: bool

Default Value : True

Syntax: bBC = True/False

**Arg21: bCheckBCDuplicate**

Description: enable or disable feature check b c duplicate

Data Type: bool

Default Value : False

Syntax: bCheckBCDuplicate = True/False

**Arg22: bAutoAssignDummyProp**

Description: enable or disable feature auto assign dummy property

Data Type: bool

Default Value : False

Syntax: bAutoAssignDummyProp = True/False

**Arg23: crDummyPropMaterial**

Description: entity in database model with type dummy property material

Data Type: cursor

Default Value : None

Syntax: crDummyPropMaterial = EntityType(id)

**Arg24: bReferenceRestartData**

Description: enable or disable feature reference restart data

Data Type: bool

Default Value : False

Syntax: bReferenceRestartData = True/False

**Arg25: strReferenceRestartDataPath**

Description: definition string of input reference restart data path

Data Type: string

Default Value : ""

Syntax: strReferenceRestartDataPath = "string input"

**Arg26: iReferenceRestartDataProcessNum**

Description: option for reference restart data process number

Data Type: integer

Default Value : DFLT_INT

Syntax: iReferenceRestartDataProcessNum = 1

**Arg27: iReferenceRestartDataStepNum**

Description: option for reference restart data step number

Data Type: integer

Default Value : DFLT_INT

Syntax: iReferenceRestartDataStepNum = 1

**Arg28: iReferenceRestartDataCoordType**

Description: option for reference restart data coordinate type

Data Type: integer

Default Value : 0

Syntax: iReferenceRestartDataCoordType = 1

**Arg29: iReferenceRestartDataUpdateContactSearch**

Description: option for reference restart data update contact search

Data Type: integer

Default Value : 1

Syntax: iReferenceRestartDataUpdateContactSearch = 1

**Arg30: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg31: iHeatConvection**

Description: option for heat convection

Data Type: integer

Default Value : 1

Syntax: iHeatConvection = 1

**Arg32: iCreateProcessForBoltFixedLength**

Description: option for create process for bolt fixed length

Data Type: integer

Default Value : 0

Syntax: iCreateProcessForBoltFixedLength = 1

**Arg33: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg34: iNumType**

Description: option for number type

Data Type: integer

Default Value : 0

Syntax: iNumType = 1

**Arg35: iUiWidth**

Description: option for ui width

Data Type: integer

Default Value : 10

Syntax: iUiWidth = 1

**Arg36: iUiPrecision**

Description: option for ui precision

Data Type: integer

Default Value : 1

Syntax: iUiPrecision = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.Structure(strName="", strDescription="", iEJobType=0, crlProcessSequence=[], crlElemLocationGroup=[], crlNodeLocationGroup=[], bWriteGroup=False, crEdit=None, bResultReference=False, iSeparateFile=0, bExportRelatedAllLBCs=False, bUseEntityName=False, bMatrixSloverParam=False, iPreconditionType=0, iMatrixStructure=0, crlTarget=[], iLoadType=1, bSameOutputOnAllProcess=True, bDeleteFloatingNode=True, bBC=True, bCheckBCDuplicate=False, bAutoAssignDummyProp=False, crDummyPropMaterial=None, bReferenceRestartData=False, strReferenceRestartDataPath="", iReferenceRestartDataProcessNum=DFLT_INT, iReferenceRestartDataStepNum=DFLT_INT, iReferenceRestartDataCoordType=0, iReferenceRestartDataUpdateContactSearch=1, listLoadNodeContact=[], iHeatConvection=1, iCreateProcessForBoltFixedLength=0, strPath="", iNumType=0, iUiWidth=10, iUiPrecision=1)

```

==========================================================

# Analysis.ADVC.HeatTransfer

## Wrapper Macro

ADVC_HeatTransfer(...)

## Ribbon-GUI-Location

Analysis > ADVC > HeatTransfer

## Command Description

create advc job

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: strDescription**

Description: definition string of input description

Data Type: string

Default Value : ""

Syntax: strDescription = "string input"

**Arg3: iEJobType**

Description: option for e job type

Data Type: integer

Default Value : 0

Syntax: iEJobType = 1

**Arg4: crlProcessSequence**

Description: array entities in model with type process sequence

Data Type: cursor list

Default Value : []

Syntax: crlProcessSequence = [EntityType(id1, id2, id3)]

**Arg5: crlElemLocationGroup**

Description: array entities in model with type element location group

Data Type: cursor list

Default Value : []

Syntax: crlElemLocationGroup = [EntityType(id1, id2, id3)]

**Arg6: crlNodeLocationGroup**

Description: array entities in model with type node location group

Data Type: cursor list

Default Value : []

Syntax: crlNodeLocationGroup = [EntityType(id1, id2, id3)]

**Arg7: bWriteGroup**

Description: enable or disable feature write group

Data Type: bool

Default Value : False

Syntax: bWriteGroup = True/False

**Arg8: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg9: bResultReference**

Description: enable or disable feature result reference

Data Type: bool

Default Value : False

Syntax: bResultReference = True/False

**Arg10: iSeparateFile**

Description: option for separate file

Data Type: integer

Default Value : 0

Syntax: iSeparateFile = 1

**Arg11: bExportRelatedAllLBCs**

Description: enable or disable feature export related all l b cs

Data Type: bool

Default Value : False

Syntax: bExportRelatedAllLBCs = True/False

**Arg12: bUseEntityName**

Description: enable or disable feature use entity name

Data Type: bool

Default Value : False

Syntax: bUseEntityName = True/False

**Arg13: bMatrixSloverParam**

Description: enable or disable feature matrix slover parameter

Data Type: bool

Default Value : False

Syntax: bMatrixSloverParam = True/False

**Arg14: iPreconditionType**

Description: option for precondition type

Data Type: integer

Default Value : 0

Syntax: iPreconditionType = 1

**Arg15: iMatrixStructure**

Description: option for matrix structure

Data Type: integer

Default Value : 0

Syntax: iMatrixStructure = 1

**Arg16: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg17: iLoadType**

Description: option for load type

Data Type: integer

Default Value : 1

Syntax: iLoadType = 1

**Arg18: bSameOutputOnAllProcess**

Description: enable or disable feature same output on all process

Data Type: bool

Default Value : True

Syntax: bSameOutputOnAllProcess = True/False

**Arg19: bDeleteFloatingNode**

Description: enable or disable feature delete floating node

Data Type: bool

Default Value : True

Syntax: bDeleteFloatingNode = True/False

**Arg20: bBC**

Description: enable or disable feature b c

Data Type: bool

Default Value : True

Syntax: bBC = True/False

**Arg21: bCheckBCDuplicate**

Description: enable or disable feature check b c duplicate

Data Type: bool

Default Value : False

Syntax: bCheckBCDuplicate = True/False

**Arg22: bAutoAssignDummyProp**

Description: enable or disable feature auto assign dummy property

Data Type: bool

Default Value : False

Syntax: bAutoAssignDummyProp = True/False

**Arg23: crDummyPropMaterial**

Description: entity in database model with type dummy property material

Data Type: cursor

Default Value : None

Syntax: crDummyPropMaterial = EntityType(id)

**Arg24: bReferenceRestartData**

Description: enable or disable feature reference restart data

Data Type: bool

Default Value : False

Syntax: bReferenceRestartData = True/False

**Arg25: strReferenceRestartDataPath**

Description: definition string of input reference restart data path

Data Type: string

Default Value : ""

Syntax: strReferenceRestartDataPath = "string input"

**Arg26: iReferenceRestartDataProcessNum**

Description: option for reference restart data process number

Data Type: integer

Default Value : DFLT_INT

Syntax: iReferenceRestartDataProcessNum = 1

**Arg27: iReferenceRestartDataStepNum**

Description: option for reference restart data step number

Data Type: integer

Default Value : DFLT_INT

Syntax: iReferenceRestartDataStepNum = 1

**Arg28: iReferenceRestartDataCoordType**

Description: option for reference restart data coordinate type

Data Type: integer

Default Value : 0

Syntax: iReferenceRestartDataCoordType = 1

**Arg29: iReferenceRestartDataUpdateContactSearch**

Description: option for reference restart data update contact search

Data Type: integer

Default Value : 1

Syntax: iReferenceRestartDataUpdateContactSearch = 1

**Arg30: listLoadNodeContact**

Description: list data structure of ADVC_LOAD_NODE (refer PSJ Command Data Structure Document)

Data Type: ADVC_LOAD_NODE

Default Value : ADVC_LOAD_NODE()

Syntax: listLoadNodeContact = [ADVC_LOAD_NODE(,,,), ADVC_LOAD_NODE(,,,)]

**Arg31: iHeatConvection**

Description: option for heat convection

Data Type: integer

Default Value : 1

Syntax: iHeatConvection = 1

**Arg32: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg33: iNumType**

Description: option for number type

Data Type: integer

Default Value : 0

Syntax: iNumType = 1

**Arg34: iUiWidth**

Description: option for ui width

Data Type: integer

Default Value : 10

Syntax: iUiWidth = 1

**Arg35: iUiPrecision**

Description: option for ui precision

Data Type: integer

Default Value : 1

Syntax: iUiPrecision = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Analysis.ADVC.HeatTransfer(strName="", strDescription="", iEJobType=0, crlProcessSequence=[], crlElemLocationGroup=[], crlNodeLocationGroup=[], bWriteGroup=False, crEdit=None, bResultReference=False, iSeparateFile=0, bExportRelatedAllLBCs=False, bUseEntityName=False, bMatrixSloverParam=False, iPreconditionType=0, iMatrixStructure=0, crlTarget=[], iLoadType=1, bSameOutputOnAllProcess=True, bDeleteFloatingNode=True, bBC=True, bCheckBCDuplicate=False, bAutoAssignDummyProp=False, crDummyPropMaterial=None, bReferenceRestartData=False, strReferenceRestartDataPath="", iReferenceRestartDataProcessNum=DFLT_INT, iReferenceRestartDataStepNum=DFLT_INT, iReferenceRestartDataCoordType=0, iReferenceRestartDataUpdateContactSearch=1, listLoadNodeContact=[], iHeatConvection=1, strPath="", iNumType=0, iUiWidth=10, iUiPrecision=1)

```

==========================================================

# Assemble.SeparateFaces.AllSharedNodes

## Wrapper Macro

ASMSeparateAll2(...)

## Ribbon-GUI-Location

Assemble > SeparateFaces > AllSharedNodes

## Command Description

create by all shared nodes

## Argument List

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.SeparateFaces.AllSharedNodes()

```

==========================================================

# Assemble.SeparateFaces.Shell

## Wrapper Macro

ASMSeparateShellCr(...)

## Ribbon-GUI-Location

Assemble > SeparateFaces > Shell

## Command Description

Separate Faces for Shell

## Argument List

**Arg1: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg2: crlEntity**

Description: array entities in model with type entity

Data Type: cursor list

Default Value : []

Syntax: crlEntity = [EntityType(id1, id2, id3)]

**Arg3: bCreateGroup**

Description: enable or disable feature create group

Data Type: bool

Default Value : False

Syntax: bCreateGroup = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.SeparateFaces.Shell(iType=0, crlEntity=[], bCreateGroup=False)

```

==========================================================

# Assemble.SeparateFaces.Solid

## Wrapper Macro

ASMSeparateSolidCr(...)

## Ribbon-GUI-Location

Assemble > SeparateFaces > Solid

## Command Description

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: bCreateGroup**

Description: enable or disable feature create group

Data Type: bool

Default Value : False

Syntax: bCreateGroup = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.SeparateFaces.Solid(crlPart=[], crlFace=[], bCreateGroup=False)

```

==========================================================

# Assemble.Boolean

## Wrapper Macro

AssembleBoolean2(...)

## Ribbon-GUI-Location

Assemble > Boolean

## Command Description

Make Boolean between Parts

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: iBooleanType**

Description: option for boolean type

Data Type: integer

Default Value : 0

Syntax: iBooleanType = 1

**Arg3: dToleranceAlignment**

Description: double value of tolerance alignment

Data Type: double

Default Value : 0.01

Syntax: dToleranceAlignment = 1.0

**Arg4: bLeaveOriginalBodies**

Description: enable or disable feature leave original bodies

Data Type: bool

Default Value : False

Syntax: bLeaveOriginalBodies = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.Boolean(crlPart=[], iBooleanType=0, dToleranceAlignment=0.01, bLeaveOriginalBodies=False)

```

==========================================================

# Assemble.AssembleFace

## Wrapper Macro

ASMAssembleFace(...)

## Ribbon-GUI-Location

Assemble > AssembleFace

## Command Description

create assemble face

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTolerance = 1.0

**Arg4: iFitEdge**

Description: option for fit edge

Data Type: integer

Default Value : 0

Syntax: iFitEdge = 1

**Arg5: iMeshSetting**

Description: option for mesh setting

Data Type: integer

Default Value : 0

Syntax: iMeshSetting = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.AssembleFace(crlPart=[], crlFace=[], dTolerance=0.0, iFitEdge=0, iMeshSetting=0)

```

==========================================================

# Assemble.FullLayer

## Wrapper Macro

AssembleFullLayer(...)

## Ribbon-GUI-Location

Assemble > FullLayer

## Command Description

assemble full layer

## Argument List

**Arg1: crPart**

Description: entity in database model with type part

Data Type: cursor

Default Value : None

Syntax: crPart = EntityType(id)

**Arg2: dLayerWidth**

Description: double value of layer width

Data Type: double

Default Value : 1.0

Syntax: dLayerWidth = 1.0

**Arg3: iLayer**

Description: option for layer

Data Type: integer

Default Value : 1

Syntax: iLayer = 1

**Arg4: bUsePyramid**

Description: enable or disable feature use pyramid

Data Type: bool

Default Value : False

Syntax: bUsePyramid = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.FullLayer(crPart=None, dLayerWidth=1.0, iLayer=1, bUsePyramid=False)

```

==========================================================

# Assemble.CylinderLayer

## Wrapper Macro

CylinderLayer(...)

## Ribbon-GUI-Location

Assemble > CylinderLayer

## Command Description

Assemble cylinder layer

## Argument List

**Arg1: crFace**

Description: entity in database model with type face

Data Type: cursor

Default Value : None

Syntax: crFace = EntityType(id)

**Arg2: crNode**

Description: entity in database model with type node

Data Type: cursor

Default Value : None

Syntax: crNode = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.CylinderLayer(crFace=None, crNode=None)

```

==========================================================

# Assemble.SharedFace

## Wrapper Macro

CreateSharedFace(...)

## Ribbon-GUI-Location

Assemble > SharedFace

## Command Description

Create assemble shared face

## Argument List

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.SharedFace()

```

==========================================================

# Assemble.AssembleFaces

## Wrapper Macro

Assemble_Faces(...)

## Ribbon-GUI-Location

Assemble > AssembleFaces

## Command Description

Assemble AssembleFaces

## Argument List

**Arg1: ilPairFaceToMakeShareFace**

Description: array int values of pair face to make share face

Data Type: int list

Default Value : []

Syntax: ilPairFaceToMakeShareFace = [1,2,3,4]

**Arg2: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.1

Syntax: dTolerance = 1.0

**Arg3: iTypeConnectPos**

Description: option for type connect pos

Data Type: integer

Default Value : 1

Syntax: iTypeConnectPos = 1

**Arg4: bUseSnapInput**

Description: enable or disable feature use snap input

Data Type: bool

Default Value : False

Syntax: bUseSnapInput = True/False

**Arg5: dSnapTolerance**

Description: double value of snap tolerance

Data Type: double

Default Value : 0.005

Syntax: dSnapTolerance = 1.0

**Arg6: bFitEdge**

Description: enable or disable feature fit edge

Data Type: bool

Default Value : False

Syntax: bFitEdge = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.AssembleFaces(ilPairFaceToMakeShareFace=[], dTolerance=0.1, iTypeConnectPos=1, bUseSnapInput=False, dSnapTolerance=0.005, bFitEdge=False)

```

==========================================================

# Assemble.GeneralLayer

## Wrapper Macro

AssembleGeneralLayer(...)

## Ribbon-GUI-Location

Assemble > GeneralLayer

## Command Description

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dWidth**

Description: double value of width

Data Type: double

Default Value : 1.0

Syntax: dWidth = 1.0

**Arg3: iLayer**

Description: option for layer

Data Type: integer

Default Value : 1

Syntax: iLayer = 1

**Arg4: bSeparatePart**

Description: enable or disable feature separate part

Data Type: bool

Default Value : False

Syntax: bSeparatePart = True/False

**Arg5: bForceStitchToSide**

Description: enable or disable feature force stitch to side

Data Type: bool

Default Value : False

Syntax: bForceStitchToSide = True/False

**Arg6: bSmoothingEdge**

Description: enable or disable feature smoothing edge

Data Type: bool

Default Value : False

Syntax: bSmoothingEdge = True/False

**Arg7: bNoImprint**

Description: enable or disable feature no imprint

Data Type: bool

Default Value : False

Syntax: bNoImprint = True/False

**Arg8: bWidthOnSurface**

Description: enable or disable feature width on surface

Data Type: bool

Default Value : False

Syntax: bWidthOnSurface = True/False

**Arg9: bMakeHexa**

Description: enable or disable feature make hexa

Data Type: bool

Default Value : False

Syntax: bMakeHexa = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.GeneralLayer(crlFace=[], dWidth=1.0, iLayer=1, bSeparatePart=False, bForceStitchToSide=False, bSmoothingEdge=False, bNoImprint=False, bWidthOnSurface=False, bMakeHexa=False)

```

==========================================================

# Assemble.AddRib

## Wrapper Macro

AddRib(...)

## Ribbon-GUI-Location

Assemble > AddRib

## Command Description

create Rib

## Argument List

**Arg1: crPart**

Description: entity in database model with type part

Data Type: cursor

Default Value : None

Syntax: crPart = EntityType(id)

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: veclPoints**

Description: two dimensional array of points

Data Type: vector list

Default Value : []

Syntax: veclPoints = [[value1, value2, value3], [value1, value2, value3]]

**Arg4: dWidth**

Description: double value of width

Data Type: double

Default Value : 0.0

Syntax: dWidth = 1.0

**Arg5: dDepth**

Description: double value of depth

Data Type: double

Default Value : 0.0

Syntax: dDepth = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.AddRib(crPart=None, crlFace=[], veclPoints=[], dWidth=0.0, dDepth=0.0)

```

==========================================================

# Assemble.FindMatingFace

## Wrapper Macro

Assemble_Faces_MatingStep(...)

## Ribbon-GUI-Location

Assemble > FindMatingFace

## Command Description

Find Mating Face For Assemble Faces

## Argument List

**Arg1: crlMasterFaces**

Description: array entities in model with type master faces

Data Type: cursor list

Default Value : []

Syntax: crlMasterFaces = [EntityType(id1, id2, id3)]

**Arg2: crlSlaveFaces**

Description: array entities in model with type slave faces

Data Type: cursor list

Default Value : []

Syntax: crlSlaveFaces = [EntityType(id1, id2, id3)]

**Arg3: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg4: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTolerance = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.FindMatingFace(crlMasterFaces=[], crlSlaveFaces=[], crlPart=[], dTolerance=0.0)

```

==========================================================

# Assemble.AddBoss

## Wrapper Macro

AssembleAddBoss(...)

## Ribbon-GUI-Location

Assemble > AddBoss

## Command Description

## Argument List

**Arg1: crPart**

Description: entity in database model with type part

Data Type: cursor

Default Value : None

Syntax: crPart = EntityType(id)

**Arg2: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg3: bMerge**

Description: enable or disable feature merge

Data Type: bool

Default Value : True

Syntax: bMerge = True/False

**Arg4: posOrgCenter**

Description: array double value [x, y, z] in coordinate system of org center

Data Type: position

Default Value : [0,0,0]

Syntax: posOrgCenter = [x, y, z]

**Arg5: vecOrgDirection**

Description: array values of org direction

Data Type: vector

Default Value : [0,0,0]

Syntax: vecOrgDirection = [value1, value2, value3]

**Arg6: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg7: iAxis**

Description: option for axis

Data Type: integer

Default Value : 0

Syntax: iAxis = 1

**Arg8: dAngle**

Description: double value of angle

Data Type: double

Default Value : 0.0

Syntax: dAngle = 1.0

**Arg9: bHollow**

Description: enable or disable feature hollow

Data Type: bool

Default Value : False

Syntax: bHollow = True/False

**Arg10: dInnerRadius**

Description: double value of inner radius

Data Type: double

Default Value : 0.0

Syntax: dInnerRadius = 1.0

**Arg11: dOrgOuterRadius**

Description: double value of org outer radius

Data Type: double

Default Value : 1.0

Syntax: dOrgOuterRadius = 1.0

**Arg12: dTaperAngle**

Description: double value of taper angle

Data Type: double

Default Value : 0.0

Syntax: dTaperAngle = 1.0

**Arg13: iNodeOnCircle**

Description: option for node on circle

Data Type: integer

Default Value : 12

Syntax: iNodeOnCircle = 1

**Arg14: iNodeOnAxis**

Description: option for node on axis

Data Type: integer

Default Value : 2

Syntax: iNodeOnAxis = 1

**Arg15: dOriginalHeight**

Description: double value of original height

Data Type: double

Default Value : 5.0

Syntax: dOriginalHeight = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assemble.AddBoss(crPart=None, iType=0, bMerge=True, posOrgCenter=[0,0,0], vecOrgDirection=[0,0,0], crCoord=None, iAxis=0, dAngle=0.0, bHollow=False, dInnerRadius=0.0, dOrgOuterRadius=1.0, dTaperAngle=0.0, iNodeOnCircle=12, iNodeOnAxis=2, dOriginalHeight=5.0)

```

==========================================================

# Assembly.RightClick.AddToReference

## Wrapper Macro

AddReference(...)

## Ribbon-GUI-Location

Assembly > RightClick > AddToReference

## Command Description

Add Reference to Body

## Argument List

**Arg1: crSrcPart**

Description: entity in database model with type src part

Data Type: cursor

Default Value : None

Syntax: crSrcPart = EntityType(id)

**Arg2: crDestPart**

Description: entity in database model with type dest part

Data Type: cursor

Default Value : None

Syntax: crDestPart = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assembly.RightClick.AddToReference(crSrcPart=None, crDestPart=None)

```

==========================================================

# Assembly.RightClick.Suppress

## Wrapper Macro

Suppress(...)

## Ribbon-GUI-Location

Assembly > RightClick > Suppress

## Command Description

Suppress/ Unsuppress part on Tree Assembly

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assembly.RightClick.Suppress(crlPart=[])

```

==========================================================

# Assembly.RightClick.UnSuppress

## Wrapper Macro

Suppress(...)

## Ribbon-GUI-Location

Assembly > RightClick > UnSuppress

## Command Description

Command use for Assembly RightClick UnSuppress

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assembly.RightClick.UnSuppress(taParts=[])

```

==========================================================

# Assembly.RightClick.RestoreOriginalPart

## Wrapper Macro

RestoreBody(...)

## Ribbon-GUI-Location

Assembly > RightClick > RestoreOriginalPart

## Command Description

Restore body

## Argument List

**Arg1: crlBodies**

Description: array entities in model with type bodies

Data Type: cursor list

Default Value : []

Syntax: crlBodies = [EntityType(id1, id2, id3)]

**Arg2: bKeepShareFace**

Description: enable or disable feature keep share face

Data Type: bool

Default Value : False

Syntax: bKeepShareFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assembly.RightClick.RestoreOriginalPart(crlBodies=[], bKeepShareFace=False)

```

==========================================================

# Assembly.RightClick.Rename

## Wrapper Macro

RenameItem(...)

## Ribbon-GUI-Location

Assembly > RightClick > Rename

## Command Description

Rename item

## Argument List

**Arg1: strNewName**

Description: definition string of input new name

Data Type: string

Default Value : "New name"

Syntax: strNewName = "string input"

**Arg2: crItem**

Description: entity in database model with type item

Data Type: cursor

Default Value : None

Syntax: crItem = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assembly.RightClick.Rename(strNewName="New name", crItem=None)

```

==========================================================

# Assembly.RightClick.ChangeEntityColor

## Wrapper Macro

ChangeEntityColor(...)

## Ribbon-GUI-Location

Assembly > RightClick > ChangeEntityColor

## Command Description

Command use for Assembly RightClick ChangeEntityColor

## Argument List

**Arg1: crlEntity**

Description: array entities in model with type entity

Data Type: cursor list

Default Value : []

Syntax: crlEntity = [EntityType(id1, id2, id3)]

**Arg2: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assembly.RightClick.ChangeEntityColor(crlEntity=[], iColor=0)

```

==========================================================

# Assembly.RightClick.AddSubAssembly

## Wrapper Macro

AddSubAssembly(...)

## Ribbon-GUI-Location

Assembly > RightClick > AddSubAssembly

## Command Description

Add sub assembly

## Argument List

**Arg1: crInst**

Description: entity in database model with type inst

Data Type: cursor

Default Value : None

Syntax: crInst = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assembly.RightClick.AddSubAssembly(crInst=None)

```

==========================================================

# Assembly.RightClick.ChangeBodyColor

## Wrapper Macro

ChangeBodyColor(...)

## Ribbon-GUI-Location

Assembly > RightClick > ChangeBodyColor

## Command Description

Change Body Color

## Argument List

**Arg1: listPartColorPair**

Description: list data structure of PART_COLOR_PAIR (refer PSJ Command Data Structure Document)

Data Type: PART_COLOR_PAIR

Default Value : PART_COLOR_PAIR()

Syntax: listPartColorPair = [PART_COLOR_PAIR(,,,), PART_COLOR_PAIR(,,,)]

**Arg2: bResetFaceColor**

Description: enable or disable feature reset face color

Data Type: bool

Default Value : False

Syntax: bResetFaceColor = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assembly.RightClick.ChangeBodyColor(listPartColorPair=[], bResetFaceColor=False)

```

==========================================================

# Assembly.RightClick.ChangeMeshLineColor

## Wrapper Macro

ChangeFaceMeshLineColor(...)

## Ribbon-GUI-Location

Assembly > RightClick > ChangeMeshLineColor

## Command Description

Change Entity color

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Assembly.RightClick.ChangeMeshLineColor(crlFace=[], iColor=0)

```

==========================================================

# BoundaryConditions.BoundaryTemperature.Constant

## Wrapper Macro

BoundaryTemperature(...)

## Ribbon-GUI-Location

BoundaryConditions > BoundaryTemperature > Constant

## Command Description

Create boundary temperature

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "BoundaryTemperature_1"

Syntax: strName = "string input"

**Arg2: dFTemp**

Description: double value of temperature

Data Type: double

Default Value : 0.0

Syntax: dFTemp = 1.0

**Arg3: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg4: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.BoundaryTemperature.Constant(strName="BoundaryTemperature_1", dFTemp=0.0, crTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.BoundaryTemperature.SurfaceMapping

## Wrapper Macro

MappingForcedTemperature(...)

## Ribbon-GUI-Location

BoundaryConditions > BoundaryTemperature > SurfaceMapping

## Command Description

Create mapping boundary temperature

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MappingTemperature"

Syntax: strName = "string input"

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: iMAPPos**

Description: option for m a p pos

Data Type: integer

Default Value : 0

Syntax: iMAPPos = 1

**Arg4: iViewCp**

Description: option for view cp

Data Type: integer

Default Value : 0

Syntax: iViewCp = 1

**Arg5: iCp**

Description: option for cp

Data Type: integer

Default Value : 1

Syntax: iCp = 1

**Arg6: iSrcType**

Description: option for src type

Data Type: integer

Default Value : 0

Syntax: iSrcType = 1

**Arg7: iMappedCpIndexArr0**

Description: option for mapped cp index arr0

Data Type: integer

Default Value : 0

Syntax: iMappedCpIndexArr0 = 1

**Arg8: iMappedCpIndexArr1**

Description: option for mapped cp index arr1

Data Type: integer

Default Value : 0

Syntax: iMappedCpIndexArr1 = 1

**Arg9: dScaleFactor**

Description: double value of scale factor

Data Type: double

Default Value : 1

Syntax: dScaleFactor = 1.0

**Arg10: posOffset**

Description: array double value [x, y, z] in coordinate system of offset

Data Type: position

Default Value : [0,0,0]

Syntax: posOffset = [x, y, z]

**Arg11: posRotate**

Description: array double value [x, y, z] in coordinate system of rotate

Data Type: position

Default Value : [0,0,0]

Syntax: posRotate = [x, y, z]

**Arg12: dCorScale**

Description: double value of cor scale

Data Type: double

Default Value : 1

Syntax: dCorScale = 1.0

**Arg13: dSearchRange**

Description: double value of search range

Data Type: double

Default Value : 0

Syntax: dSearchRange = 1.0

**Arg14: iUnit**

Description: option for unit

Data Type: integer

Default Value : 0

Syntax: iUnit = 1

**Arg15: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg16: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg17: iMappingMethod**

Description: option for mapping method

Data Type: integer

Default Value : 0

Syntax: iMappingMethod = 1

**Arg18: iSubmodeLBCMappingType**

Description: option for submode load-boundary-condition mapping type

Data Type: integer

Default Value : 3

Syntax: iSubmodeLBCMappingType = 1

**Arg19: iMappingFromStepNo**

Description: option for mapping from step

Data Type: integer

Default Value : 0

Syntax: iMappingFromStepNo = 1

**Arg20: bSetADVCFile**

Description: enable or disable feature set advc file

Data Type: bool

Default Value : False

Syntax: bSetADVCFile = True/False

**Arg21: strADVCResultFile**

Description: definition string of input advc result file

Data Type: string

Default Value : ""

Syntax: strADVCResultFile = "string input"

**Arg22: bSetDetATol**

Description: enable or disable feature set det a tolerance

Data Type: bool

Default Value : False

Syntax: bSetDetATol = True/False

**Arg23: dDetATol**

Description: double value of det a tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dDetATol = 1.0

**Arg24: bSetElementSet**

Description: enable or disable feature set element set

Data Type: bool

Default Value : False

Syntax: bSetElementSet = True/False

**Arg25: strElementSet**

Description: definition string of input element set

Data Type: string

Default Value : "all"

Syntax: strElementSet = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.BoundaryTemperature.SurfaceMapping(strName="MappingTemperature", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0, iMappedCpIndexArr1=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strPath="", crEdit=None, iMappingMethod=0, iSubmodeLBCMappingType=3, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="all")

```

==========================================================

# BoundaryConditions.Convection.Constant

## Wrapper Macro

Convection(...)

## Ribbon-GUI-Location

BoundaryConditions > Convection > Constant

## Command Description

Create lbc of convection

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Convection_1"

Syntax: strName = "string input"

**Arg2: dExtTemp**

Description: double value of external temperature

Data Type: double

Default Value : DFLT_DBL

Syntax: dExtTemp = 1.0

**Arg3: crTableTimeTemp**

Description: entity in database model with type table time temperature

Data Type: cursor

Default Value : None

Syntax: crTableTimeTemp = EntityType(id)

**Arg4: dDcoef**

Description: double value of dcoef

Data Type: double

Default Value : DFLT_DBL

Syntax: dDcoef = 1.0

**Arg5: crTableTimeCoeff**

Description: entity in database model with type table time coefficient

Data Type: cursor

Default Value : None

Syntax: crTableTimeCoeff = EntityType(id)

**Arg6: crTableTempCoeff**

Description: entity in database model with type table temperature coefficient

Data Type: cursor

Default Value : None

Syntax: crTableTempCoeff = EntityType(id)

**Arg7: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg8: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Convection.Constant(strName="Convection_1", dExtTemp=DFLT_DBL, crTableTimeTemp=None, dDcoef=DFLT_DBL, crTableTimeCoeff=None, crTableTempCoeff=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Convection.SurfaceMapping

## Wrapper Macro

MappingConvection(...)

## Ribbon-GUI-Location

BoundaryConditions > Convection > SurfaceMapping

## Command Description

Create lbc of convection Surface Mapping

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MappingConvection1"

Syntax: strName = "string input"

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: iPos**

Description: option for pos

Data Type: integer

Default Value : 0

Syntax: iPos = 1

**Arg4: iViewCp**

Description: option for view cp

Data Type: integer

Default Value : 0

Syntax: iViewCp = 1

**Arg5: iCp**

Description: option for cp

Data Type: integer

Default Value : 0

Syntax: iCp = 1

**Arg6: iSrcType**

Description: option for src type

Data Type: integer

Default Value : 0

Syntax: iSrcType = 1

**Arg7: iMappedCpIndex0**

Description: option for mapped cp index0

Data Type: integer

Default Value : 0

Syntax: iMappedCpIndex0 = 1

**Arg8: iMappedCpIndex1**

Description: option for mapped cp index1

Data Type: integer

Default Value : 0

Syntax: iMappedCpIndex1 = 1

**Arg9: dRScale**

Description: double value of r scale

Data Type: double

Default Value : 1.0

Syntax: dRScale = 1.0

**Arg10: posOffset**

Description: array double value [x, y, z] in coordinate system of offset

Data Type: position

Default Value : [0,0,0]

Syntax: posOffset = [x, y, z]

**Arg11: posAxis**

Description: array double value [x, y, z] in coordinate system of axis

Data Type: position

Default Value : [0,0,0]

Syntax: posAxis = [x, y, z]

**Arg12: dTScale**

Description: double value of t scale

Data Type: double

Default Value : 1.0

Syntax: dTScale = 1.0

**Arg13: dSearchRange**

Description: double value of search range

Data Type: double

Default Value : 1.0

Syntax: dSearchRange = 1.0

**Arg14: iHTCUnit**

Description: option for h t c unit

Data Type: integer

Default Value : 0

Syntax: iHTCUnit = 1

**Arg15: iTempUnit**

Description: option for temperature unit

Data Type: integer

Default Value : 0

Syntax: iTempUnit = 1

**Arg16: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg17: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Convection.SurfaceMapping(strName="MappingConvection1", crlTarget=[], iPos=0, iViewCp=0, iCp=0, iSrcType=0, iMappedCpIndex0=0, iMappedCpIndex1=0, dRScale=1.0, posOffset=[0,0,0], posAxis=[0,0,0], dTScale=1.0, dSearchRange=1.0, iHTCUnit=0, iTempUnit=0, strPath="", crEdit=None)

```

==========================================================

# BoundaryConditions.EnforcedLoads.Acceleration

## Wrapper Macro

EnforcedAcceleration(...)

## Ribbon-GUI-Location

BoundaryConditions > EnforcedLoads > Acceleration

## Command Description

Set enforced acceleration

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "EnforcedAcceleration1"

Syntax: strName = "string input"

**Arg2: iDwDof**

Description: option for dw dof

Data Type: integer

Default Value : 0

Syntax: iDwDof = 1

**Arg3: dFVel1**

Description: double value of vel1

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel1 = 1.0

**Arg4: dFVel2**

Description: double value of vel2

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel2 = 1.0

**Arg5: dFVel3**

Description: double value of vel3

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel3 = 1.0

**Arg6: dFVel4**

Description: double value of vel4

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel4 = 1.0

**Arg7: dFVel5**

Description: double value of vel5

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel5 = 1.0

**Arg8: dFVel6**

Description: double value of vel6

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel6 = 1.0

**Arg9: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg10: iEnArrowDir**

Description: option for en arrow dir

Data Type: integer

Default Value : 0

Syntax: iEnArrowDir = 1

**Arg11: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg12: crNodeSet**

Description: entity in database model with type node set

Data Type: cursor

Default Value : None

Syntax: crNodeSet = EntityType(id)

**Arg13: dFPhase**

Description: double value of phase

Data Type: double

Default Value : DFLT_DBL

Syntax: dFPhase = 1.0

**Arg14: dFDelay**

Description: double value of delay

Data Type: double

Default Value : DFLT_DBL

Syntax: dFDelay = 1.0

**Arg15: crPhaseTable**

Description: entity in database model with type phase table

Data Type: cursor

Default Value : None

Syntax: crPhaseTable = EntityType(id)

**Arg16: bExport**

Description: enable or disable feature export

Data Type: bool

Default Value : False

Syntax: bExport = True/False

**Arg17: crMEExport1**

Description: entity in database model with type m e export1

Data Type: cursor

Default Value : None

Syntax: crMEExport1 = EntityType(id)

**Arg18: crMEExport2**

Description: entity in database model with type m e export2

Data Type: cursor

Default Value : None

Syntax: crMEExport2 = EntityType(id)

**Arg19: crMEExport3**

Description: entity in database model with type m e export3

Data Type: cursor

Default Value : None

Syntax: crMEExport3 = EntityType(id)

**Arg20: crMEExport4**

Description: entity in database model with type m e export4

Data Type: cursor

Default Value : None

Syntax: crMEExport4 = EntityType(id)

**Arg21: crMEExport5**

Description: entity in database model with type m e export5

Data Type: cursor

Default Value : None

Syntax: crMEExport5 = EntityType(id)

**Arg22: crMEExport6**

Description: entity in database model with type m e export6

Data Type: cursor

Default Value : None

Syntax: crMEExport6 = EntityType(id)

**Arg23: iAcUnit**

Description: option for ac unit

Data Type: integer

Default Value : 0

Syntax: iAcUnit = 1

**Arg24: iRotUnit**

Description: option for rotation unit

Data Type: integer

Default Value : 0

Syntax: iRotUnit = 1

**Arg25: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg26: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.EnforcedLoads.Acceleration(strName="EnforcedAcceleration1", iDwDof=0, dFVel1=DFLT_DBL, dFVel2=DFLT_DBL, dFVel3=DFLT_DBL, dFVel4=DFLT_DBL, dFVel5=DFLT_DBL, dFVel6=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, bExport=False, crMEExport1=None, crMEExport2=None, crMEExport3=None, crMEExport4=None, crMEExport5=None, crMEExport6=None, iAcUnit=0, iRotUnit=0, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.EnforcedLoads.Velocity

## Wrapper Macro

EnforcedVelocity(...)

## Ribbon-GUI-Location

BoundaryConditions > EnforcedLoads > Velocity

## Command Description

create enforced velocity

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "EnforcedVelocity1"

Syntax: strName = "string input"

**Arg2: iDwDof**

Description: option for dw dof

Data Type: integer

Default Value : 0

Syntax: iDwDof = 1

**Arg3: dFVel0**

Description: double value of vel0

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel0 = 1.0

**Arg4: dFVel1**

Description: double value of vel1

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel1 = 1.0

**Arg5: dFVel2**

Description: double value of vel2

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel2 = 1.0

**Arg6: dFVel3**

Description: double value of vel3

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel3 = 1.0

**Arg7: dFVel4**

Description: double value of vel4

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel4 = 1.0

**Arg8: dFVel5**

Description: double value of vel5

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVel5 = 1.0

**Arg9: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg10: iEnArrowDir**

Description: option for en arrow dir

Data Type: integer

Default Value : 0

Syntax: iEnArrowDir = 1

**Arg11: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg12: crNodeSet**

Description: entity in database model with type node set

Data Type: cursor

Default Value : None

Syntax: crNodeSet = EntityType(id)

**Arg13: dFPhase**

Description: double value of phase

Data Type: double

Default Value : DFLT_DBL

Syntax: dFPhase = 1.0

**Arg14: dFDelay**

Description: double value of delay

Data Type: double

Default Value : DFLT_DBL

Syntax: dFDelay = 1.0

**Arg15: crPhaseTable**

Description: entity in database model with type phase table

Data Type: cursor

Default Value : None

Syntax: crPhaseTable = EntityType(id)

**Arg16: iVelUnit**

Description: option for vel unit

Data Type: integer

Default Value : 0

Syntax: iVelUnit = 1

**Arg17: iRotUnit**

Description: option for rotation unit

Data Type: integer

Default Value : 0

Syntax: iRotUnit = 1

**Arg18: bExport**

Description: enable or disable feature export

Data Type: bool

Default Value : False

Syntax: bExport = True/False

**Arg19: crExportData0**

Description: entity in database model with type export data0

Data Type: cursor

Default Value : None

Syntax: crExportData0 = EntityType(id)

**Arg20: crExportData1**

Description: entity in database model with type export data1

Data Type: cursor

Default Value : None

Syntax: crExportData1 = EntityType(id)

**Arg21: crExportData2**

Description: entity in database model with type export data2

Data Type: cursor

Default Value : None

Syntax: crExportData2 = EntityType(id)

**Arg22: crExportData3**

Description: entity in database model with type export data3

Data Type: cursor

Default Value : None

Syntax: crExportData3 = EntityType(id)

**Arg23: crExportData4**

Description: entity in database model with type export data4

Data Type: cursor

Default Value : None

Syntax: crExportData4 = EntityType(id)

**Arg24: crExportData5**

Description: entity in database model with type export data5

Data Type: cursor

Default Value : None

Syntax: crExportData5 = EntityType(id)

**Arg25: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg26: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg27: bADVCStatic**

Description: enable or disable feature advc static

Data Type: bool

Default Value : False

Syntax: bADVCStatic = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.EnforcedLoads.Velocity(strName="EnforcedVelocity1", iDwDof=0, dFVel0=DFLT_DBL, dFVel1=DFLT_DBL, dFVel2=DFLT_DBL, dFVel3=DFLT_DBL, dFVel4=DFLT_DBL, dFVel5=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, iVelUnit=0, iRotUnit=0, bExport=False, crExportData0=None, crExportData1=None, crExportData2=None, crExportData3=None, crExportData4=None, crExportData5=None, crlTarget=[], crEdit=None, bADVCStatic=False)

```

==========================================================

# BoundaryConditions.EnforcedLoads.Displacement

## Wrapper Macro

EnforcedDisplacement(...)

## Ribbon-GUI-Location

BoundaryConditions > EnforcedLoads > Displacement

## Command Description

create enforced displacement

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iDwDof**

Description: option for dw dof

Data Type: integer

Default Value : 0

Syntax: iDwDof = 1

**Arg3: dFDisp0**

Description: double value of disp0

Data Type: double

Default Value : DFLT_DBL

Syntax: dFDisp0 = 1.0

**Arg4: dFDisp1**

Description: double value of disp1

Data Type: double

Default Value : DFLT_DBL

Syntax: dFDisp1 = 1.0

**Arg5: dFDisp2**

Description: double value of disp2

Data Type: double

Default Value : DFLT_DBL

Syntax: dFDisp2 = 1.0

**Arg6: dFDisp3**

Description: double value of disp3

Data Type: double

Default Value : DFLT_DBL

Syntax: dFDisp3 = 1.0

**Arg7: dFDisp4**

Description: double value of disp4

Data Type: double

Default Value : DFLT_DBL

Syntax: dFDisp4 = 1.0

**Arg8: dFDisp5**

Description: double value of disp5

Data Type: double

Default Value : DFLT_DBL

Syntax: dFDisp5 = 1.0

**Arg9: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg10: iEnArrowDir**

Description: option for en arrow dir

Data Type: integer

Default Value : 0

Syntax: iEnArrowDir = 1

**Arg11: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg12: crNodeSet**

Description: entity in database model with type node set

Data Type: cursor

Default Value : None

Syntax: crNodeSet = EntityType(id)

**Arg13: dFPhase**

Description: double value of phase

Data Type: double

Default Value : DFLT_DBL

Syntax: dFPhase = 1.0

**Arg14: dFDelay**

Description: double value of delay

Data Type: double

Default Value : DFLT_DBL

Syntax: dFDelay = 1.0

**Arg15: crPhaseTable**

Description: entity in database model with type phase table

Data Type: cursor

Default Value : None

Syntax: crPhaseTable = EntityType(id)

**Arg16: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg17: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.EnforcedLoads.Displacement(strName="", iDwDof=0, dFDisp0=DFLT_DBL, dFDisp1=DFLT_DBL, dFDisp2=DFLT_DBL, dFDisp3=DFLT_DBL, dFDisp4=DFLT_DBL, dFDisp5=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.HeatFlux.SurfaceFlux

## Wrapper Macro

SurfaceFlux(...)

## Ribbon-GUI-Location

BoundaryConditions > HeatFlux > SurfaceFlux

## Command Description

create surface flux

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: dFflux**

Description: double value of fflux

Data Type: double

Default Value : 0.0

Syntax: dFflux = 1.0

**Arg3: iDistributionMethod**

Description: option for distribution method

Data Type: integer

Default Value : 0

Syntax: iDistributionMethod = 1

**Arg4: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg5: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg6: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.HeatFlux.SurfaceFlux(strName="", dFflux=0.0, iDistributionMethod=0, crTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.HeatFlux.SurfaceMapping

## Wrapper Macro

MappingHeatFlux(...)

## Ribbon-GUI-Location

BoundaryConditions > HeatFlux > SurfaceMapping

## Command Description

Create mapping heat flux

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MappingHeatFlux"

Syntax: strName = "string input"

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: iMAPPos**

Description: option for m a p pos

Data Type: integer

Default Value : 0

Syntax: iMAPPos = 1

**Arg4: iViewCp**

Description: option for view cp

Data Type: integer

Default Value : 0

Syntax: iViewCp = 1

**Arg5: iCp**

Description: option for cp

Data Type: integer

Default Value : 1

Syntax: iCp = 1

**Arg6: iSrcType**

Description: option for src type

Data Type: integer

Default Value : 0

Syntax: iSrcType = 1

**Arg7: iMappedCpIndexArr0**

Description: option for mapped cp index arr0

Data Type: integer

Default Value : 0

Syntax: iMappedCpIndexArr0 = 1

**Arg8: dScaleFactor**

Description: double value of scale factor

Data Type: double

Default Value : 1

Syntax: dScaleFactor = 1.0

**Arg9: posOffset**

Description: array double value [x, y, z] in coordinate system of offset

Data Type: position

Default Value : [0,0,0]

Syntax: posOffset = [x, y, z]

**Arg10: posRotate**

Description: array double value [x, y, z] in coordinate system of rotate

Data Type: position

Default Value : [0,0,0]

Syntax: posRotate = [x, y, z]

**Arg11: dCorScale**

Description: double value of cor scale

Data Type: double

Default Value : 1

Syntax: dCorScale = 1.0

**Arg12: dSearchRange**

Description: double value of search range

Data Type: double

Default Value : 0

Syntax: dSearchRange = 1.0

**Arg13: iUnit**

Description: option for unit

Data Type: integer

Default Value : 0

Syntax: iUnit = 1

**Arg14: strStrpath**

Description: definition string of input strpath

Data Type: string

Default Value : ""

Syntax: strStrpath = "string input"

**Arg15: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg16: iMappingMethod**

Description: option for mapping method

Data Type: integer

Default Value : 0

Syntax: iMappingMethod = 1

**Arg17: iSubmodeLBCMappingType**

Description: option for submode load-boundary-condition mapping type

Data Type: integer

Default Value : 4

Syntax: iSubmodeLBCMappingType = 1

**Arg18: iMappingFromStepNo**

Description: option for mapping from step

Data Type: integer

Default Value : 0

Syntax: iMappingFromStepNo = 1

**Arg19: bSetADVCFile**

Description: enable or disable feature set advc file

Data Type: bool

Default Value : False

Syntax: bSetADVCFile = True/False

**Arg20: strADVCResultFile**

Description: definition string of input advc result file

Data Type: string

Default Value : ""

Syntax: strADVCResultFile = "string input"

**Arg21: bSetDetATol**

Description: enable or disable feature set det a tolerance

Data Type: bool

Default Value : False

Syntax: bSetDetATol = True/False

**Arg22: dDetATol**

Description: double value of det a tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dDetATol = 1.0

**Arg23: bSetElementSet**

Description: enable or disable feature set element set

Data Type: bool

Default Value : False

Syntax: bSetElementSet = True/False

**Arg24: strElementSet**

Description: definition string of input element set

Data Type: string

Default Value : "all"

Syntax: strElementSet = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.HeatFlux.SurfaceMapping(strName="MappingHeatFlux", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strStrpath="", crEdit=None, iMappingMethod=0, iSubmodeLBCMappingType=4, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="all")

```

==========================================================

# BoundaryConditions.HeatFlux.ConcentrateFlux

## Wrapper Macro

ConcentrateFlux(...)

## Ribbon-GUI-Location

BoundaryConditions > HeatFlux > ConcentrateFlux

## Command Description

Command use for BoundaryConditions HeatFlux ConcentrateFlux

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ConcentrateHeatFlux1"

Syntax: strName = "string input"

**Arg2: stData**

Description: data structure of LBC_CONCENTRATE_FLUX_DATA (refer PSJ Command Data Structure Document)

Data Type: LBC_CONCENTRATE_FLUX_DATA

Default Value : LBC_CONCENTRATE_FLUX_DATA()

Syntax: stData = LBC_CONCENTRATE_FLUX_DATA(,,,)

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.HeatFlux.ConcentrateFlux(strName = "ConcentrateHeatFlux1", stData=LBC_CONCENTRATE_FLUX_DATA(), crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.InitialElementalValue.InitialStress

## Wrapper Macro

InitialStressGeneral(...)

## Ribbon-GUI-Location

BoundaryConditions > InitialElementalValue > InitialStress

## Command Description

create mapping stress

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InitialStress1"

Syntax: strName = "string input"

**Arg2: iDimension**

Description: option for dimension

Data Type: integer

Default Value : 2

Syntax: iDimension = 1

**Arg3: iElemCs**

Description: option for element cs

Data Type: integer

Default Value : 0

Syntax: iElemCs = 1

**Arg4: dSXX**

Description: double value of s x x

Data Type: double

Default Value : DFLT_DBL

Syntax: dSXX = 1.0

**Arg5: dSYY**

Description: double value of s y y

Data Type: double

Default Value : DFLT_DBL

Syntax: dSYY = 1.0

**Arg6: dSXY**

Description: double value of s x y

Data Type: double

Default Value : DFLT_DBL

Syntax: dSXY = 1.0

**Arg7: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg9: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InitialElementalValue.InitialStress(strName="InitialStress1", iDimension=2, iElemCs=0, dSXX=DFLT_DBL, dSYY=DFLT_DBL, dSXY=DFLT_DBL, crTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.InitialTemperature.WholeMapping

## Wrapper Macro

WholeMappingInitTemperature(...)

## Ribbon-GUI-Location

BoundaryConditions > InitialTemperature > WholeMapping

## Command Description

Create initial temperature whole mapping

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "TemperatureInitsWholeMapping1"

Syntax: strName = "string input"

**Arg2: iMapSourceType**

Description: option for map source type

Data Type: integer

Default Value : 0

Syntax: iMapSourceType = 1

**Arg3: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg4: iMappingMethod**

Description: option for mapping method

Data Type: integer

Default Value : 0

Syntax: iMappingMethod = 1

**Arg5: iIsubcase**

Description: option for isubcase

Data Type: integer

Default Value : 0

Syntax: iIsubcase = 1

**Arg6: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InitialTemperature.WholeMapping(strName="TemperatureInitsWholeMapping1", iMapSourceType=0, strPath="", iMappingMethod=0, iIsubcase=0, crEdit=None)

```

==========================================================

# BoundaryConditions.InitialTemperature.Constant

## Wrapper Macro

InitialTemperature(...)

## Ribbon-GUI-Location

BoundaryConditions > InitialTemperature > Constant

## Command Description

Command use for BoundaryConditions InitialTemperature Constant

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InitialTemperature1",dFTemp

Syntax: strName = "string input"

**Arg2: strFilePathName**

Description: definition string of input file path name

Data Type: string

Default Value : ""

Syntax: strFilePathName = "string input"

**Arg3: bUseDefault**

Description: enable or disable feature use default

Data Type: bool

Default Value : False

Syntax: bUseDefault = True/False

**Arg4: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg5: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg6: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InitialTemperature.Constant(strName="InitialTemperature1",dFTemp=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.InitialTemperature.ADVC

## Wrapper Macro

InitialTemperature(...)

## Ribbon-GUI-Location

BoundaryConditions > InitialTemperature > ADVC

## Command Description

Command use for BoundaryConditions InitialTemperature ADVC

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InitialTemperature1",dTemperatureValue

Syntax: strName = "string input"

**Arg2: strFilePathName**

Description: definition string of input file path name

Data Type: string

Default Value : ""

Syntax: strFilePathName = "string input"

**Arg3: bUseDefault**

Description: enable or disable feature use default

Data Type: bool

Default Value : False

Syntax: bUseDefault = True/False

**Arg4: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg5: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg6: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InitialTemperature.ADVC(strName="InitialTemperature1",dTemperatureValue=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.InitialTemperature.NastranPunch

## Wrapper Macro

InitialTemperature(...)

## Ribbon-GUI-Location

BoundaryConditions > InitialTemperature > NastranPunch

## Command Description

Command use for BoundaryConditions InitialTemperature NastranPunch

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InitialTemperature1",dTemperatureValue

Syntax: strName = "string input"

**Arg2: strFilePathName**

Description: definition string of input file path name

Data Type: string

Default Value : ""

Syntax: strFilePathName = "string input"

**Arg3: bUseDefault**

Description: enable or disable feature use default

Data Type: bool

Default Value : False

Syntax: bUseDefault = True/False

**Arg4: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg5: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg6: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InitialTemperature.NastranPunch(strName="InitialTemperature1",dTemperatureValue=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.LBCCopy.PropertiesCopyTranslate

## Wrapper Macro

PropertiesCopyTranslate(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > PropertiesCopyTranslate

## Command Description

Copy property translate

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: posVecTrans**

Description: array double value [x, y, z] in coordinate system of vec translation

Data Type: position

Default Value : [0,0,0]

Syntax: posVecTrans = [x, y, z]

**Arg4: dMagnitude**

Description: double value of magnitude

Data Type: double

Default Value : 1

Syntax: dMagnitude = 1.0

**Arg5: dTrandataDoffset**

Description: double value of trandata doffset

Data Type: double

Default Value : 0.0

Syntax: dTrandataDoffset = 1.0

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.PropertiesCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.PropertiesCopyRotate

## Wrapper Macro

PropertiesCopyRotate(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > PropertiesCopyRotate

## Command Description

Copy property rotate

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: posAxis**

Description: array double value [x, y, z] in coordinate system of axis

Data Type: position

Default Value : [0,0,0]

Syntax: posAxis = [x, y, z]

**Arg4: posCenter**

Description: array double value [x, y, z] in coordinate system of center

Data Type: position

Default Value : [0,0,0]

Syntax: posCenter = [x, y, z]

**Arg5: dAngle**

Description: double value of angle

Data Type: double

Default Value : 0.0

Syntax: dAngle = 1.0

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.PropertiesCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.PropertiesCopyMirror

## Wrapper Macro

PropertiesCopyMirror(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > PropertiesCopyMirror

## Command Description

Copy property mirror

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 2

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: poslPoints**

Description: list positions [x, y, z] in coordinate system of points

Data Type: position list

Default Value : []

Syntax: poslPoints = [[x, y, z], [x, y, z]]

**Arg4: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0

Syntax: dOffset = 1.0

**Arg5: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg6: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.PropertiesCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.ConnectionCopyTranslate

## Wrapper Macro

ConnectionCopyTranslate(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > ConnectionCopyTranslate

## Command Description

Copy connection translate

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: posVecTrans**

Description: array double value [x, y, z] in coordinate system of vec translation

Data Type: position

Default Value : [0,0,0]

Syntax: posVecTrans = [x, y, z]

**Arg4: dMagnitude**

Description: double value of magnitude

Data Type: double

Default Value : 1

Syntax: dMagnitude = 1.0

**Arg5: dTrandataDoffset**

Description: double value of trandata doffset

Data Type: double

Default Value : 0.0

Syntax: dTrandataDoffset = 1.0

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.ConnectionCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.ConnectionCopyRotate

## Wrapper Macro

ConnectionCopyRotate(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > ConnectionCopyRotate

## Command Description

Copy Connection rotate

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: posAxis**

Description: array double value [x, y, z] in coordinate system of axis

Data Type: position

Default Value : [0,0,0]

Syntax: posAxis = [x, y, z]

**Arg4: posCenter**

Description: array double value [x, y, z] in coordinate system of center

Data Type: position

Default Value : [0,0,0]

Syntax: posCenter = [x, y, z]

**Arg5: dAngle**

Description: double value of angle

Data Type: double

Default Value : 0.0

Syntax: dAngle = 1.0

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.ConnectionCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.ConnectionCopyMirror

## Wrapper Macro

ConnectionCopyMirror(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > ConnectionCopyMirror

## Command Description

Copy Connection mirror

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 2

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: poslPoints**

Description: list positions [x, y, z] in coordinate system of points

Data Type: position list

Default Value : []

Syntax: poslPoints = [[x, y, z], [x, y, z]]

**Arg4: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0

Syntax: dOffset = 1.0

**Arg5: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg6: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.ConnectionCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.GroupCopyTranslate

## Wrapper Macro

GroupCopyTranslate(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > GroupCopyTranslate

## Command Description

Copy group translate

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: posVecTrans**

Description: array double value [x, y, z] in coordinate system of vec translation

Data Type: position

Default Value : [0,0,0]

Syntax: posVecTrans = [x, y, z]

**Arg4: dMagnitude**

Description: double value of magnitude

Data Type: double

Default Value : 1

Syntax: dMagnitude = 1.0

**Arg5: dTrandataDoffset**

Description: double value of trandata doffset

Data Type: double

Default Value : 0.0

Syntax: dTrandataDoffset = 1.0

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.GroupCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.GroupCopyRotate

## Wrapper Macro

GroupCopyRotate(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > GroupCopyRotate

## Command Description

Copy Group rotate

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: posAxis**

Description: array double value [x, y, z] in coordinate system of axis

Data Type: position

Default Value : [0,0,0]

Syntax: posAxis = [x, y, z]

**Arg4: posCenter**

Description: array double value [x, y, z] in coordinate system of center

Data Type: position

Default Value : [0,0,0]

Syntax: posCenter = [x, y, z]

**Arg5: dAngle**

Description: double value of angle

Data Type: double

Default Value : 0.0

Syntax: dAngle = 1.0

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.GroupCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.GroupCopyMirror

## Wrapper Macro

GroupCopyMirror(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > GroupCopyMirror

## Command Description

Copy Group mirror

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 2

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: poslPoints**

Description: list positions [x, y, z] in coordinate system of points

Data Type: position list

Default Value : []

Syntax: poslPoints = [[x, y, z], [x, y, z]]

**Arg4: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0

Syntax: dOffset = 1.0

**Arg5: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg6: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.GroupCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.LBCCopyTranslate

## Wrapper Macro

LBCCopyTranslate(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > LBCCopyTranslate

## Command Description

Copy LBC translate

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: posVecTrans**

Description: array double value [x, y, z] in coordinate system of vec translation

Data Type: position

Default Value : [0,0,0]

Syntax: posVecTrans = [x, y, z]

**Arg4: dMagnitude**

Description: double value of magnitude

Data Type: double

Default Value : 1

Syntax: dMagnitude = 1.0

**Arg5: dTrandataDoffset**

Description: double value of trandata doffset

Data Type: double

Default Value : 0.0

Syntax: dTrandataDoffset = 1.0

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.LBCCopyTranslate(iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.LBCCopyRotate

## Wrapper Macro

LBCCopyRotate(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > LBCCopyRotate

## Command Description

Copy LBC rotate

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: posAxis**

Description: array double value [x, y, z] in coordinate system of axis

Data Type: position

Default Value : [0,0,0]

Syntax: posAxis = [x, y, z]

**Arg4: posCenter**

Description: array double value [x, y, z] in coordinate system of center

Data Type: position

Default Value : [0,0,0]

Syntax: posCenter = [x, y, z]

**Arg5: dAngle**

Description: double value of angle

Data Type: double

Default Value : 0.0

Syntax: dAngle = 1.0

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.LBCCopyRotate(iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTarget=[])

```

==========================================================

# BoundaryConditions.LBCCopy.LBCCopyMirror

## Wrapper Macro

LBCCopyMirror(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopy > LBCCopyMirror

## Command Description

Copy LBC mirror

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 2

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: poslPoints**

Description: list positions [x, y, z] in coordinate system of points

Data Type: position list

Default Value : []

Syntax: poslPoints = [[x, y, z], [x, y, z]]

**Arg4: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0

Syntax: dOffset = 1.0

**Arg5: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1

Syntax: dTol = 1.0

**Arg6: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopy.LBCCopyMirror(iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTarget=[])

```

==========================================================

# BoundaryConditions.Pressure.SurfaceLoads

## Wrapper Macro

SurfaceLoads(...)

## Ribbon-GUI-Location

BoundaryConditions > Pressure > SurfaceLoads

## Command Description

create distrubited pressure

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "SurfaceLoads1"

Syntax: strName = "string input"

**Arg2: dlPressure**

Description: array double values of pressure

Data Type: double list

Default Value : [0,0,0]

Syntax: dlPressure = [1.0, 2.0]

**Arg3: iArrowdir**

Description: option for arrowdir

Data Type: integer

Default Value : 0

Syntax: iArrowdir = 1

**Arg4: crCoordinate**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoordinate = EntityType(id)

**Arg5: crlTargetFace**

Description: array entities in database model face

Data Type: cursor list

Default Value : []

Syntax: crlTargetFace = [EntityType(id1, id2, id3)]

**Arg6: crEditCur**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEditCur = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Pressure.SurfaceLoads(strName="SurfaceLoads1", dlPressure=[0,0,0], iArrowdir=0, crCoordinate=None, crlTargetFace=[], crEditCur=None)

```

==========================================================

# BoundaryConditions.Pressure.By2Nodes

## Wrapper Macro

Pressure2Nodes(...)

## Ribbon-GUI-Location

BoundaryConditions > Pressure > By2Nodes

## Command Description

Create lbc of 2nodes pressure

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "PressureLinear1"

Syntax: strName = "string input"

**Arg2: crNodeA**

Description: entity in database model with type node a

Data Type: cursor

Default Value : None

Syntax: crNodeA = EntityType(id)

**Arg3: dPressureA**

Description: double value of pressure a

Data Type: double

Default Value : 0.0

Syntax: dPressureA = 1.0

**Arg4: iNodeAUnit**

Description: option for node a unit

Data Type: integer

Default Value : 0

Syntax: iNodeAUnit = 1

**Arg5: crNodeB**

Description: entity in database model with type node b

Data Type: cursor

Default Value : None

Syntax: crNodeB = EntityType(id)

**Arg6: dPressureB**

Description: double value of pressure b

Data Type: double

Default Value : 0.0

Syntax: dPressureB = 1.0

**Arg7: iNodeBUnit**

Description: option for node b unit

Data Type: integer

Default Value : 0

Syntax: iNodeBUnit = 1

**Arg8: iDirection**

Description: option for direction

Data Type: integer

Default Value : 0

Syntax: iDirection = 1

**Arg9: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg10: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Pressure.By2Nodes(strName="PressureLinear1", crNodeA=None, dPressureA=0.0, iNodeAUnit=0, crNodeB=None, dPressureB=0.0, iNodeBUnit=0, iDirection=0, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Pressure.General

## Wrapper Macro

PressureGeneral(...)

## Ribbon-GUI-Location

BoundaryConditions > Pressure > General

## Command Description

Create general pressure boundary condition

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Pressure1"

Syntax: strName = "string input"

**Arg2: dFpressure**

Description: double value of fpressure

Data Type: double

Default Value : 0.0

Syntax: dFpressure = 1.0

**Arg3: iIdistribute**

Description: option for idistribute

Data Type: integer

Default Value : 0

Syntax: iIdistribute = 1

**Arg4: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg5: dDphase**

Description: double value of dphase

Data Type: double

Default Value : 0.0

Syntax: dDphase = 1.0

**Arg6: dDdelay**

Description: double value of ddelay

Data Type: double

Default Value : 0.0

Syntax: dDdelay = 1.0

**Arg7: crPhaseTable**

Description: entity in database model with type phase table

Data Type: cursor

Default Value : None

Syntax: crPhaseTable = EntityType(id)

**Arg8: strFormularValue**

Description: definition string of input formular value

Data Type: string

Default Value : ""

Syntax: strFormularValue = "string input"

**Arg9: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg10: dlDirection**

Description: array double values of direction

Data Type: double list

Default Value : [DFLT_DBL,DFLT_DBL,DFLT_DBL]

Syntax: dlDirection = [1.0, 2.0]

**Arg11: strFormularDirX**

Description: definition string of input formular dir x

Data Type: string

Default Value : ""

Syntax: strFormularDirX = "string input"

**Arg12: strFormularDirY**

Description: definition string of input formular dir y

Data Type: string

Default Value : ""

Syntax: strFormularDirY = "string input"

**Arg13: strFormularDirZ**

Description: definition string of input formular dir z

Data Type: string

Default Value : ""

Syntax: strFormularDirZ = "string input"

**Arg14: iArrowDir**

Description: option for arrow dir

Data Type: integer

Default Value : 1

Syntax: iArrowDir = 1

**Arg15: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg16: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Pressure.General(strName="Pressure1", dFpressure=0.0, iIdistribute=0, crTable=None, dDphase=0.0, dDdelay=0.0, crPhaseTable=None, strFormularValue="", crCoord=None, dlDirection=[DFLT_DBL,DFLT_DBL,DFLT_DBL], strFormularDirX="", strFormularDirY="", strFormularDirZ="", iArrowDir=1, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Pressure.Quadratic

## Wrapper Macro

PressureQuadratic(...)

## Ribbon-GUI-Location

BoundaryConditions > Pressure > Quadratic

## Command Description

Create Pressure quadratic

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "PressureQuadratic1"

Syntax: strName = "string input"

**Arg2: dA**

Description: double value of a

Data Type: double

Default Value : 0.0

Syntax: dA = 1.0

**Arg3: dB**

Description: double value of b

Data Type: double

Default Value : 0.0

Syntax: dB = 1.0

**Arg4: crCoordinate**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoordinate = EntityType(id)

**Arg5: dAngleRange**

Description: double value of angle range

Data Type: double

Default Value : 0.0

Syntax: dAngleRange = 1.0

**Arg6: iPressureDirectionMode**

Description: option for pressure direction mode

Data Type: integer

Default Value : 0

Syntax: iPressureDirectionMode = 1

**Arg7: dlPressureDirection**

Description: array double values of pressure direction

Data Type: double list

Default Value : [0.0,0.0,0.0]

Syntax: dlPressureDirection = [1.0, 2.0]

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg9: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Pressure.Quadratic(strName="PressureQuadratic1", dA=0.0, dB=0.0, crCoordinate=None, dAngleRange=0.0, iPressureDirectionMode=0, dlPressureDirection=[0.0,0.0,0.0], crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Pressure.FunctionLoadToCylinderSine

## Wrapper Macro

PressureSine(...)

## Ribbon-GUI-Location

BoundaryConditions > Pressure > FunctionLoadToCylinderSine

## Command Description

Command use for BoundaryConditions Pressure FunctionLoadToCylinderSine

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "PressureSine1"

Syntax: strName = "string input"

**Arg2: dA**

Description: double value of a

Data Type: double

Default Value : 0.0

Syntax: dA = 1.0

**Arg3: crCoordinate**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoordinate = EntityType(id)

**Arg4: dAngleRange**

Description: double value of angle range

Data Type: double

Default Value : 0.0

Syntax: dAngleRange = 1.0

**Arg5: bDistributionAxis**

Description: enable or disable feature distribution axis

Data Type: bool

Default Value : False

Syntax: bDistributionAxis = True/False

**Arg6: iPressureDirectionMode**

Description: option for pressure direction mode

Data Type: integer

Default Value : 0

Syntax: iPressureDirectionMode = 1

**Arg7: bIsTotalForceAdjustment**

Description: enable or disable feature is total force adjustment

Data Type: bool

Default Value : False

Syntax: bIsTotalForceAdjustment = True/False

**Arg8: dTotalForce**

Description: double value of total force

Data Type: double

Default Value : 0.0

Syntax: dTotalForce = 1.0

**Arg9: vecPressureDirection**

Description: array values of pressure direction

Data Type: vector

Default Value : [0.0,0.0,0.0]

Syntax: vecPressureDirection = [value1, value2, value3]

**Arg10: crCoordinateSystemForDirection**

Description: entity in database model with type coordinate system for direction

Data Type: cursor

Default Value : None

Syntax: crCoordinateSystemForDirection = EntityType(id)

**Arg11: bIsCornerNodesDistribution**

Description: enable or disable feature is corner nodes distribution

Data Type: bool

Default Value : False

Syntax: bIsCornerNodesDistribution = True/False

**Arg12: strFormulaForA**

Description: definition string of input formula for a

Data Type: string

Default Value : ""

Syntax: strFormulaForA = "string input"

**Arg13: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg14: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Pressure.FunctionLoadToCylinderSine(strName="PressureSine1", dA=0.0, crCoordinate=None, dAngleRange=0.0, bDistributionAxis=False, iPressureDirectionMode=0, bIsTotalForceAdjustment=False, dTotalForce=0.0, vecPressureDirection=[0.0,0.0,0.0], crCoordinateSystemForDirection=None, bIsCornerNodesDistribution=False, strFormulaForA="", crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Pressure.Hydrostatic

## Wrapper Macro

PressureHydrostatic(...)

## Ribbon-GUI-Location

BoundaryConditions > Pressure > Hydrostatic

## Command Description

Boundary Conditions HPressure

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "PressureHydrostatic1"

Syntax: strName = "string input"

**Arg2: dFHPressure**

Description: double value of h pressure

Data Type: double

Default Value : 0.0

Syntax: dFHPressure = 1.0

**Arg3: dFDensity**

Description: double value of density

Data Type: double

Default Value : 0.0

Syntax: dFDensity = 1.0

**Arg4: iDensityUnit**

Description: option for density unit

Data Type: integer

Default Value : 0

Syntax: iDensityUnit = 1

**Arg5: dFGravity**

Description: double value of gravity

Data Type: double

Default Value : 0.0

Syntax: dFGravity = 1.0

**Arg6: iGravityUnit**

Description: option for gravity unit

Data Type: integer

Default Value : 0

Syntax: iGravityUnit = 1

**Arg7: iGravityDir**

Description: option for gravity dir

Data Type: integer

Default Value : 0

Syntax: iGravityDir = 1

**Arg8: dFWaterSuface**

Description: double value of water suface

Data Type: double

Default Value : 0.0

Syntax: dFWaterSuface = 1.0

**Arg9: iSufaceUnit**

Description: option for suface unit

Data Type: integer

Default Value : 0

Syntax: iSufaceUnit = 1

**Arg10: iDistributionMethod**

Description: option for distribution method

Data Type: integer

Default Value : 0

Syntax: iDistributionMethod = 1

**Arg11: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg12: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Pressure.Hydrostatic(strName="PressureHydrostatic1", dFHPressure=0.0, dFDensity=0.0, iDensityUnit=0, dFGravity=0.0, iGravityUnit=0, iGravityDir=0, dFWaterSuface=0.0, iSufaceUnit=0, iDistributionMethod=0, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Pressure.SurfaceMapping

## Wrapper Macro

MappingPressure(...)

## Ribbon-GUI-Location

BoundaryConditions > Pressure > SurfaceMapping

## Command Description

Create mapping pressure

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MappingPressure"

Syntax: strName = "string input"

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: iMAPPos**

Description: option for m a p pos

Data Type: integer

Default Value : 0

Syntax: iMAPPos = 1

**Arg4: iViewCp**

Description: option for view cp

Data Type: integer

Default Value : 0

Syntax: iViewCp = 1

**Arg5: iCp**

Description: option for cp

Data Type: integer

Default Value : 1

Syntax: iCp = 1

**Arg6: iSrcType**

Description: option for src type

Data Type: integer

Default Value : 0

Syntax: iSrcType = 1

**Arg7: iMappedCpIndexArr**

Description: option for mapped cp index arr

Data Type: integer

Default Value : 0

Syntax: iMappedCpIndexArr = 1

**Arg8: dScaleFactor**

Description: double value of scale factor

Data Type: double

Default Value : 1

Syntax: dScaleFactor = 1.0

**Arg9: posOffset**

Description: array double value [x, y, z] in coordinate system of offset

Data Type: position

Default Value : [0,0,0]

Syntax: posOffset = [x, y, z]

**Arg10: posRotate**

Description: array double value [x, y, z] in coordinate system of rotate

Data Type: position

Default Value : [0,0,0]

Syntax: posRotate = [x, y, z]

**Arg11: dCorScale**

Description: double value of cor scale

Data Type: double

Default Value : 1

Syntax: dCorScale = 1.0

**Arg12: dSearchRange**

Description: double value of search range

Data Type: double

Default Value : 0

Syntax: dSearchRange = 1.0

**Arg13: iUnit**

Description: option for unit

Data Type: integer

Default Value : 0

Syntax: iUnit = 1

**Arg14: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg15: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Pressure.SurfaceMapping(strName="MappingPressure", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strPath="", crEdit=None)

```

==========================================================

# BoundaryConditions.Submodel.SubmodelForcedFlux

## Wrapper Macro

SubmodelForcedFlux(...)

## Ribbon-GUI-Location

BoundaryConditions > Submodel > SubmodelForcedFlux

## Command Description

create submodel forced flux

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iSolver**

Description: option for solver

Data Type: integer

Default Value : 0

Syntax: iSolver = 1

**Arg3: strFilePathName**

Description: definition string of input file path name

Data Type: string

Default Value : "/home/"

Syntax: strFilePathName = "string input"

**Arg4: iProcessNo**

Description: option for process no

Data Type: integer

Default Value : 0

Syntax: iProcessNo = 1

**Arg5: iReferType**

Description: option for refer type

Data Type: integer

Default Value : -1

Syntax: iReferType = 1

**Arg6: dExtensionRange**

Description: double value of extension range

Data Type: double

Default Value : DFLT_DBL

Syntax: dExtensionRange = 1.0

**Arg7: dExtensionTol**

Description: double value of extension tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dExtensionTol = 1.0

**Arg8: dExtensionLimitTol**

Description: double value of extension limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dExtensionLimitTol = 1.0

**Arg9: strGlobalElementSet**

Description: definition string of input global element set

Data Type: string

Default Value : ""

Syntax: strGlobalElementSet = "string input"

**Arg10: iUseBucket**

Description: option for use bucket

Data Type: integer

Default Value : -1

Syntax: iUseBucket = 1

**Arg11: iNumBucketMaxX**

Description: option for number bucket maximize x

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumBucketMaxX = 1

**Arg12: iNumBucketMaxY**

Description: option for number bucket maximize y

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumBucketMaxY = 1

**Arg13: iNumBucketMaxZ**

Description: option for number bucket maximize z

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumBucketMaxZ = 1

**Arg14: iPrevBc**

Description: option for prev bc

Data Type: integer

Default Value : -1

Syntax: iPrevBc = 1

**Arg15: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg16: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Submodel.SubmodelForcedFlux(strName="", iSolver=0, strFilePathName="/home/", iProcessNo=0, iReferType=-1, dExtensionRange=DFLT_DBL, dExtensionTol=DFLT_DBL, dExtensionLimitTol=DFLT_DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT_INT, iNumBucketMaxY=DFLT_INT, iNumBucketMaxZ=DFLT_INT, iPrevBc=-1, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Submodel.ForcedTempertature

## Wrapper Macro

SubmodelForcedTemp(...)

## Ribbon-GUI-Location

BoundaryConditions > Submodel > ForcedTempertature

## Command Description

create sub model forced temperature

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "SubmodelForcedTemperature1"

Syntax: strName = "string input"

**Arg2: iSolver**

Description: option for solver

Data Type: integer

Default Value : 0

Syntax: iSolver = 1

**Arg3: strFilePathName**

Description: definition string of input file path name

Data Type: string

Default Value : "/home/"

Syntax: strFilePathName = "string input"

**Arg4: iProcessNo**

Description: option for process no

Data Type: integer

Default Value : 0

Syntax: iProcessNo = 1

**Arg5: iReferType**

Description: option for refer type

Data Type: integer

Default Value : 0

Syntax: iReferType = 1

**Arg6: dExtensionRange**

Description: double value of extension range

Data Type: double

Default Value : DFLT_DBL

Syntax: dExtensionRange = 1.0

**Arg7: dExtensionTol**

Description: double value of extension tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dExtensionTol = 1.0

**Arg8: dExtensionLimitTol**

Description: double value of extension limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dExtensionLimitTol = 1.0

**Arg9: strGlobalElementSet**

Description: definition string of input global element set

Data Type: string

Default Value : ""

Syntax: strGlobalElementSet = "string input"

**Arg10: iUseBucket**

Description: option for use bucket

Data Type: integer

Default Value : -1

Syntax: iUseBucket = 1

**Arg11: iNumBucketMaxX**

Description: option for number bucket maximize x

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumBucketMaxX = 1

**Arg12: iNumBucketMaxY**

Description: option for number bucket maximize y

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumBucketMaxY = 1

**Arg13: iNumBucketMaxZ**

Description: option for number bucket maximize z

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumBucketMaxZ = 1

**Arg14: iPrevBc**

Description: option for prev bc

Data Type: integer

Default Value : -1

Syntax: iPrevBc = 1

**Arg15: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg16: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Submodel.ForcedTempertature(strName="SubmodelForcedTemperature1", iSolver=0, strFilePathName="/home/", iProcessNo=0, iReferType=0, dExtensionRange=DFLT_DBL, dExtensionTol=DFLT_DBL, dExtensionLimitTol=DFLT_DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT_INT, iNumBucketMaxY=DFLT_INT, iNumBucketMaxZ=DFLT_INT, iPrevBc=-1, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Submodel.ForcedDisplacement

## Wrapper Macro

SubmodelForcedDisp(...)

## Ribbon-GUI-Location

BoundaryConditions > Submodel > ForcedDisplacement

## Command Description

Boundary Conditions Lbc Submodel Forced Disp

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "SubmodelForcedDisplacement1"

Syntax: strName = "string input"

**Arg2: iSolver**

Description: option for solver

Data Type: integer

Default Value : 0

Syntax: iSolver = 1

**Arg3: strFilePathName**

Description: definition string of input file path name

Data Type: string

Default Value : "/home/"

Syntax: strFilePathName = "string input"

**Arg4: iProcessNo**

Description: option for process no

Data Type: integer

Default Value : 0

Syntax: iProcessNo = 1

**Arg5: bTranslationX**

Description: enable or disable feature translation x

Data Type: bool

Default Value : True

Syntax: bTranslationX = True/False

**Arg6: bTranslationY**

Description: enable or disable feature translation y

Data Type: bool

Default Value : True

Syntax: bTranslationY = True/False

**Arg7: bTranslationZ**

Description: enable or disable feature translation z

Data Type: bool

Default Value : True

Syntax: bTranslationZ = True/False

**Arg8: iReferType**

Description: option for refer type

Data Type: integer

Default Value : -1

Syntax: iReferType = 1

**Arg9: dExtensionRange**

Description: double value of extension range

Data Type: double

Default Value : DFLT_DBL

Syntax: dExtensionRange = 1.0

**Arg10: dExtensionTol**

Description: double value of extension tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dExtensionTol = 1.0

**Arg11: dExtensionLimitTol**

Description: double value of extension limit tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dExtensionLimitTol = 1.0

**Arg12: strGlobalElementSet**

Description: definition string of input global element set

Data Type: string

Default Value : ""

Syntax: strGlobalElementSet = "string input"

**Arg13: iUseBucket**

Description: option for use bucket

Data Type: integer

Default Value : -1

Syntax: iUseBucket = 1

**Arg14: iNumBucketMaxX**

Description: option for number bucket maximize x

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumBucketMaxX = 1

**Arg15: iNumBucketMaxY**

Description: option for number bucket maximize y

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumBucketMaxY = 1

**Arg16: iNumBucketMaxZ**

Description: option for number bucket maximize z

Data Type: integer

Default Value : DFLT_INT

Syntax: iNumBucketMaxZ = 1

**Arg17: iPrevBc**

Description: option for prev bc

Data Type: integer

Default Value : -1

Syntax: iPrevBc = 1

**Arg18: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg19: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Submodel.ForcedDisplacement(strName="SubmodelForcedDisplacement1", iSolver=0, strFilePathName="/home/", iProcessNo=0, bTranslationX=True, bTranslationY=True, bTranslationZ=True, iReferType=-1, dExtensionRange=DFLT_DBL, dExtensionTol=DFLT_DBL, dExtensionLimitTol=DFLT_DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT_INT, iNumBucketMaxY=DFLT_INT, iNumBucketMaxZ=DFLT_INT, iPrevBc=-1, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.TemperatureLoads.Constant

## Wrapper Macro

TemperatureLoadGeneral(...)

## Ribbon-GUI-Location

BoundaryConditions > TemperatureLoads > Constant

## Command Description

create temperature load constant

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: dTemperature**

Description: double value of temperature

Data Type: double

Default Value : 0.0

Syntax: dTemperature = 1.0

**Arg3: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg4: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: bUseDefaultTemp**

Description: enable or disable feature use default temperature

Data Type: bool

Default Value : False

Syntax: bUseDefaultTemp = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.TemperatureLoads.Constant(strName="", dTemperature=0.0, crTable=None, crlTarget=[], crEdit=None, bUseDefaultTemp=False)

```

==========================================================

# BoundaryConditions.TemperatureLoads.ADVCFile

## Wrapper Macro

TemperatureLoadADVCFile(...)

## Ribbon-GUI-Location

BoundaryConditions > TemperatureLoads > ADVCFile

## Command Description

create temperature load by advc file

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "TemperatureLoadsADVC1"

Syntax: strName = "string input"

**Arg2: strFilePathName**

Description: definition string of input file path name

Data Type: string

Default Value : ""

Syntax: strFilePathName = "string input"

**Arg3: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg4: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.TemperatureLoads.ADVCFile(strName="TemperatureLoadsADVC1", strFilePathName="", crTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.TemperatureLoads.NastranPunch

## Wrapper Macro

TemperatureLoadNastran(...)

## Ribbon-GUI-Location

BoundaryConditions > TemperatureLoads > NastranPunch

## Command Description

create temperature load of nastran punch

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "TemperatureLoadsPunch1"

Syntax: strName = "string input"

**Arg2: strFilePathName**

Description: definition string of input file path name

Data Type: string

Default Value : ""

Syntax: strFilePathName = "string input"

**Arg3: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg4: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: bUseAsMaterialReferenceTemp**

Description: enable or disable feature use as material reference temperature

Data Type: bool

Default Value : False

Syntax: bUseAsMaterialReferenceTemp = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.TemperatureLoads.NastranPunch(strName="TemperatureLoadsPunch1", strFilePathName="", crTable=None, crlTarget=[], crEdit=None, bUseAsMaterialReferenceTemp=False)

```

==========================================================

# BoundaryConditions.TemperatureLoads.WholeMapping

## Wrapper Macro

MappingTemperatureLoad(...)

## Ribbon-GUI-Location

BoundaryConditions > TemperatureLoads > WholeMapping

## Command Description

Create mapping pressure

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "TemperatureLoadsWholeMapping"

Syntax: strName = "string input"

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: iMAPPos**

Description: option for m a p pos

Data Type: integer

Default Value : 0

Syntax: iMAPPos = 1

**Arg4: iViewCp**

Description: option for view cp

Data Type: integer

Default Value : 0

Syntax: iViewCp = 1

**Arg5: iCp**

Description: option for cp

Data Type: integer

Default Value : 1

Syntax: iCp = 1

**Arg6: iSrcType**

Description: option for src type

Data Type: integer

Default Value : 0

Syntax: iSrcType = 1

**Arg7: iMappedCpIndexArr0**

Description: option for mapped cp index arr0

Data Type: integer

Default Value : 0

Syntax: iMappedCpIndexArr0 = 1

**Arg8: iMappedCpIndexArr1**

Description: option for mapped cp index arr1

Data Type: integer

Default Value : 0

Syntax: iMappedCpIndexArr1 = 1

**Arg9: iDScaleFactor**

Description: option for d scale factor

Data Type: integer

Default Value : 1

Syntax: iDScaleFactor = 1

**Arg10: posOffset**

Description: array double value [x, y, z] in coordinate system of offset

Data Type: position

Default Value : [0,0,0]

Syntax: posOffset = [x, y, z]

**Arg11: posRotate**

Description: array double value [x, y, z] in coordinate system of rotate

Data Type: position

Default Value : [0,0,0]

Syntax: posRotate = [x, y, z]

**Arg12: dCorScale**

Description: double value of cor scale

Data Type: double

Default Value : 1

Syntax: dCorScale = 1.0

**Arg13: dSearchRange**

Description: double value of search range

Data Type: double

Default Value : 0

Syntax: dSearchRange = 1.0

**Arg14: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg15: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg16: iMappingMethod**

Description: option for mapping method

Data Type: integer

Default Value : 0

Syntax: iMappingMethod = 1

**Arg17: iSubmodelBCMappingType**

Description: option for submodel b c mapping type

Data Type: integer

Default Value : 2

Syntax: iSubmodelBCMappingType = 1

**Arg18: iMappingFromStepNo**

Description: option for mapping from step no

Data Type: integer

Default Value : 0

Syntax: iMappingFromStepNo = 1

**Arg19: bSetADVCFile**

Description: enable or disable feature set advc file

Data Type: bool

Default Value : False

Syntax: bSetADVCFile = True/False

**Arg20: strADVCResultFile**

Description: definition string of input advc result file

Data Type: string

Default Value : ""

Syntax: strADVCResultFile = "string input"

**Arg21: bSetDetATol**

Description: enable or disable feature set det a tolerance

Data Type: bool

Default Value : False

Syntax: bSetDetATol = True/False

**Arg22: dDetATol**

Description: double value of det a tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dDetATol = 1.0

**Arg23: bSetElementSet**

Description: enable or disable feature set element set

Data Type: bool

Default Value : False

Syntax: bSetElementSet = True/False

**Arg24: strElementSet**

Description: definition string of input element set

Data Type: string

Default Value : ""

Syntax: strElementSet = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.TemperatureLoads.WholeMapping(strName="TemperatureLoadsWholeMapping", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0, iMappedCpIndexArr1=0, iDScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, strPath="", crEdit=None, iMappingMethod=0, iSubmodelBCMappingType=2, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="")

```

==========================================================

# BoundaryConditions.TemperatureLoads.LbcInitialTemperature

## Wrapper Macro

InitialTemperature(...)

## Ribbon-GUI-Location

BoundaryConditions > TemperatureLoads > LbcInitialTemperature

## Command Description

Boundary Conditions Lbc Initial Temperature

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InitialTemperature1"

Syntax: strName = "string input"

**Arg2: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg3: dFTemp**

Description: double value of temperature

Data Type: double

Default Value : 0.0

Syntax: dFTemp = 1.0

**Arg4: strFilePathName**

Description: definition string of input file path name

Data Type: string

Default Value : ""

Syntax: strFilePathName = "string input"

**Arg5: bUseDefault**

Description: enable or disable feature use default

Data Type: bool

Default Value : False

Syntax: bUseDefault = True/False

**Arg6: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg7: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg8: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.TemperatureLoads.LbcInitialTemperature(strName="InitialTemperature1", iType=0, dFTemp=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.LoadCase

## Wrapper Macro

LoadCase(...)

## Ribbon-GUI-Location

BoundaryConditions > LoadCase

## Command Description

create load case

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "LoadCase1"

Syntax: strName = "string input"

**Arg2: dFactor**

Description: double value of factor

Data Type: double

Default Value : 1.0

Syntax: dFactor = 1.0

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: iExportId**

Description: option for export id

Data Type: integer

Default Value : 1

Syntax: iExportId = 1

**Arg5: dlTargetFactor**

Description: array double values of target factor

Data Type: double list

Default Value : []

Syntax: dlTargetFactor = [1.0, 2.0]

**Arg6: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LoadCase(strName="LoadCase1", dFactor=1.0, crlTarget=[], iExportId=1, dlTargetFactor=[], crEdit=None)

```

==========================================================

# BoundaryConditions.InsideHeatGeneration

## Wrapper Macro

InsideHeatGeneration(...)

## Ribbon-GUI-Location

BoundaryConditions > InsideHeatGeneration

## Command Description

Create lbc of inside heat generation

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InsideHeatGeneration1"

Syntax: strName = "string input"

**Arg2: dInsideFlux**

Description: double value of inside flux

Data Type: double

Default Value : DFLT_DBL

Syntax: dInsideFlux = 1.0

**Arg3: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg4: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InsideHeatGeneration(strName="InsideHeatGeneration1", dInsideFlux=DFLT_DBL, crTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.LBCCopyMisc

## Wrapper Macro

CmdLbcCopy(...)

## Ribbon-GUI-Location

BoundaryConditions > LBCCopyMisc

## Command Description

Command use for BoundaryConditions LBCCopyMisc

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: iMatchMethod**

Description: option for match method

Data Type: integer

Default Value : 0

Syntax: iMatchMethod = 1

**Arg3: dlTransVec**

Description: array double values of translation vec

Data Type: double list

Default Value : [0,0,0]

Syntax: dlTransVec = [1.0, 2.0]

**Arg4: dTransMag**

Description: double value of translation mag

Data Type: double

Default Value : 0

Syntax: dTransMag = 1.0

**Arg5: dTransOffset**

Description: double value of translation offset

Data Type: double

Default Value : 0

Syntax: dTransOffset = 1.0

**Arg6: dTransTol**

Description: double value of translation tolerance

Data Type: double

Default Value : 0

Syntax: dTransTol = 1.0

**Arg7: crTranscrCoord**

Description: entity in database model with type transcr coordinate

Data Type: cursor

Default Value : None

Syntax: crTranscrCoord = EntityType(id)

**Arg8: dlTransaxisVec**

Description: array double values of transaxis vec

Data Type: double list

Default Value : [0,0,0]

Syntax: dlTransaxisVec = [1.0, 2.0]

**Arg9: dlTranscenterVec**

Description: array double values of transcenter vec

Data Type: double list

Default Value : [0,0,0]

Syntax: dlTranscenterVec = [1.0, 2.0]

**Arg10: dRotateAngle**

Description: double value of rotate angle

Data Type: double

Default Value : 0

Syntax: dRotateAngle = 1.0

**Arg11: dRotateTol**

Description: double value of rotate tolerance

Data Type: double

Default Value : 0

Syntax: dRotateTol = 1.0

**Arg12: crRotatecrCoord**

Description: entity in database model with type rotatecr coordinate

Data Type: cursor

Default Value : None

Syntax: crRotatecrCoord = EntityType(id)

**Arg13: veclMirrorPoint**

Description: two dimensional array of mirror point

Data Type: vector list

Default Value : []

Syntax: veclMirrorPoint = [[value1, value2, value3], [value1, value2, value3]]

**Arg14: dMirrordOffset**

Description: double value of mirrord offset

Data Type: double

Default Value : 0

Syntax: dMirrordOffset = 1.0

**Arg15: dMirrorTol**

Description: double value of mirror tolerance

Data Type: double

Default Value : 0.1

Syntax: dMirrorTol = 1.0

**Arg16: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LBCCopyMisc(iMethod=0, iMatchMethod=0, dlTransVec=[0,0,0], dTransMag=0, dTransOffset=0, dTransTol=0, crTranscrCoord=None, dlTransaxisVec=[0,0,0], dlTranscenterVec=[0,0,0], dRotateAngle=0, dRotateTol=0, crRotatecrCoord=None, veclMirrorPoint=[], dMirrordOffset=0, dMirrorTol=0.1, crlTarget=[])

```

==========================================================

# BoundaryConditions.LbcContactConvert

## Wrapper Macro

LbcContactConvertTo(...)

## Ribbon-GUI-Location

BoundaryConditions > LbcContactConvert

## Command Description

BoundaryConditions LbcContactConvert

## Argument List

**Arg1: iConvertTo**

Description: option for convert to

Data Type: integer

Default Value : 0

Syntax: iConvertTo = 1

**Arg2: iTieConvType**

Description: option for tie conv type

Data Type: integer

Default Value : 0

Syntax: iTieConvType = 1

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.LbcContactConvert(iConvertTo=0, iTieConvType=0, crlTarget=[])

```

==========================================================

# BoundaryConditions.FieldData

## Wrapper Macro

FieldData(...)

## Ribbon-GUI-Location

BoundaryConditions > FieldData

## Command Description

create field data table

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg3: ilSheet**

Description: array int values of sheet

Data Type: int list

Default Value : []

Syntax: ilSheet = [1,2,3,4]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg5: bAbaqusAmp**

Description: enable or disable feature abaqus amp

Data Type: bool

Default Value : False

Syntax: bAbaqusAmp = True/False

**Arg6: iAmpType**

Description: option for amp type

Data Type: integer

Default Value : 0

Syntax: iAmpType = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.FieldData(strName="", iType=0, ilSheet=[], crEdit=None, bAbaqusAmp=False, iAmpType=0)

```

==========================================================

# BoundaryConditions.FixedConstraint

## Wrapper Macro

FixedConstraint(...)

## Ribbon-GUI-Location

BoundaryConditions > FixedConstraint

## Command Description

create FixedConstraint

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "Constraint1"

Syntax: strName = "string input"

**Arg2: iDwDof**

Description: option for dw dof

Data Type: integer

Default Value : 7

Syntax: iDwDof = 1

**Arg3: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg4: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg5: iUsetType**

Description: option for uset type

Data Type: integer

Default Value : 0

Syntax: iUsetType = 1

**Arg6: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg7: bAbaqusFixed**

Description: enable or disable feature abaqus fixed

Data Type: bool

Default Value : False

Syntax: bAbaqusFixed = True/False

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg9: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.FixedConstraint(strName="Constraint1", iDwDof=7, crCurCoord=None, iType=0, iUsetType=0, crTable=None, bAbaqusFixed=False, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.DofSet

## Wrapper Macro

DofSet(...)

## Ribbon-GUI-Location

BoundaryConditions > DofSet

## Command Description

Lbc Dof Set

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iDwDof**

Description: option for dw dof

Data Type: integer

Default Value : 0

Syntax: iDwDof = 1

**Arg3: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg4: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg5: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg6: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.DofSet(strName="", iDwDof=0, crCurCoord=None, crTable=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems

## Wrapper Macro

CentrifugalForceCoordinateSystem(...)

## Ribbon-GUI-Location

BoundaryConditions > BodyLoads > CentrifugalForce > CoordinateSystems

## Command Description

create centrifugal force by coordinate system

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "CentrifugalForce1"

Syntax: strName = "string input"

**Arg2: dFVelocity**

Description: double value of velocity

Data Type: double

Default Value : DFLT_DBL

Syntax: dFVelocity = 1.0

**Arg3: dFAcceleration**

Description: double value of acceleration

Data Type: double

Default Value : DFLT_DBL

Syntax: dFAcceleration = 1.0

**Arg4: iAxisDirection**

Description: option for axis direction

Data Type: integer

Default Value : 0

Syntax: iAxisDirection = 1

**Arg5: iVelocityUnit**

Description: option for velocity unit

Data Type: integer

Default Value : 0

Syntax: iVelocityUnit = 1

**Arg6: iAccelerationUnit**

Description: option for acceleration unit

Data Type: integer

Default Value : 0

Syntax: iAccelerationUnit = 1

**Arg7: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg9: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems(strName="CentrifugalForce1", dFVelocity=DFLT_DBL, dFAcceleration=DFLT_DBL, iAxisDirection=0, iVelocityUnit=0, iAccelerationUnit=0, crCurCoord=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions

## Wrapper Macro

CentrifugalForce2Positions(...)

## Ribbon-GUI-Location

BoundaryConditions > BodyLoads > CentrifugalForce > TwoPositions

## Command Description

create centrifugal force

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "CentrifugalForce1"

Syntax: strName = "string input"

**Arg2: dFBasePoint1**

Description: double value of base point1

Data Type: double

Default Value : 0.0

Syntax: dFBasePoint1 = 1.0

**Arg3: dFBasePoint2**

Description: double value of base point2

Data Type: double

Default Value : 0.0

Syntax: dFBasePoint2 = 1.0

**Arg4: dFBasePoint3**

Description: double value of base point3

Data Type: double

Default Value : 0.0

Syntax: dFBasePoint3 = 1.0

**Arg5: dFTipPoint1**

Description: double value of tip point1

Data Type: double

Default Value : 0.0

Syntax: dFTipPoint1 = 1.0

**Arg6: dFTipPoint2**

Description: double value of tip point2

Data Type: double

Default Value : 0.0

Syntax: dFTipPoint2 = 1.0

**Arg7: dFTipPoint3**

Description: double value of tip point3

Data Type: double

Default Value : 0.0

Syntax: dFTipPoint3 = 1.0

**Arg8: dFVelocity**

Description: double value of velocity

Data Type: double

Default Value : 0.0

Syntax: dFVelocity = 1.0

**Arg9: dFAcceleration**

Description: double value of acceleration

Data Type: double

Default Value : 0.0

Syntax: dFAcceleration = 1.0

**Arg10: iVelocityUnit**

Description: option for velocity unit

Data Type: integer

Default Value : 0

Syntax: iVelocityUnit = 1

**Arg11: iAccelerationUnit**

Description: option for acceleration unit

Data Type: integer

Default Value : 0

Syntax: iAccelerationUnit = 1

**Arg12: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions(strName="CentrifugalForce1", dFBasePoint1=0.0, dFBasePoint2=0.0, dFBasePoint3=0.0, dFTipPoint1=0.0, dFTipPoint2=0.0, dFTipPoint3=0.0, dFVelocity=0.0, dFAcceleration=0.0, iVelocityUnit=0, iAccelerationUnit=0, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.BodyLoads.Gravity

## Wrapper Macro

Gravity(...)

## Ribbon-GUI-Location

BoundaryConditions > BodyLoads > Gravity

## Command Description

create gravity

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: dlGravity**

Description: array double values of gravity

Data Type: double list

Default Value : []

Syntax: dlGravity = [1.0, 2.0]

**Arg3: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg4: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.BodyLoads.Gravity(strName="", dlGravity=[], crCurCoord=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Force.FunctionLoadCylinder.Quadratic

## Wrapper Macro

ForceQuadratic(...)

## Ribbon-GUI-Location

BoundaryConditions > Force > FunctionLoadCylinder > Quadratic

## Command Description

Create Force (Quadratic) y = a\*x^2 + b

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ForceQuadratic1"

Syntax: strName = "string input"

**Arg2: dFTotalForce**

Description: double value of total force

Data Type: double

Default Value : 0.0

Syntax: dFTotalForce = 1.0

**Arg3: dA**

Description: double value of a

Data Type: double

Default Value : 0.0

Syntax: dA = 1.0

**Arg4: dB**

Description: double value of b

Data Type: double

Default Value : 0.0

Syntax: dB = 1.0

**Arg5: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg6: iAngleBase**

Description: option for angle base

Data Type: integer

Default Value : 0

Syntax: iAngleBase = 1

**Arg7: dAngleRange**

Description: double value of angle range

Data Type: double

Default Value : 0.0

Syntax: dAngleRange = 1.0

**Arg8: iEnArrowDir**

Description: option for en arrow dir

Data Type: integer

Default Value : 0

Syntax: iEnArrowDir = 1

**Arg9: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg10: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Force.FunctionLoadCylinder.Quadratic(strName="ForceQuadratic1", dFTotalForce=0.0, dA=0.0, dB=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Force.FunctionLoadCylinder.Sine

## Wrapper Macro

ForceSine(...)

## Ribbon-GUI-Location

BoundaryConditions > Force > FunctionLoadCylinder > Sine

## Command Description

Define the force load on selected entity based on the distribution of the sine function.

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ForceSine1"

Syntax: strName = "string input"

**Arg2: dFTotalForce**

Description: double value of total force

Data Type: double

Default Value : 0.0

Syntax: dFTotalForce = 1.0

**Arg3: dA**

Description: double value of a

Data Type: double

Default Value : 0.0

Syntax: dA = 1.0

**Arg4: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg5: iAngleBase**

Description: option for angle base

Data Type: integer

Default Value : 0

Syntax: iAngleBase = 1

**Arg6: dAngleRange**

Description: double value of angle range

Data Type: double

Default Value : 0.0

Syntax: dAngleRange = 1.0

**Arg7: iEnArrowDir**

Description: option for en arrow dir

Data Type: integer

Default Value : 0

Syntax: iEnArrowDir = 1

**Arg8: bDistributeInAxis**

Description: enable or disable feature distribute in axis

Data Type: bool

Default Value : False

Syntax: bDistributeInAxis = True/False

**Arg9: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg10: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Force.FunctionLoadCylinder.Sine(strName="ForceSine1", dFTotalForce=0.0, dA=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, bDistributeInAxis=False, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Force.FunctionLoadCylinder.Vector

## Wrapper Macro

ForceVector(...)

## Ribbon-GUI-Location

BoundaryConditions > Force > FunctionLoadCylinder > Vector

## Command Description

Define the force load on selected entity based on the distribution of the vector function.

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ForceVector1"

Syntax: strName = "string input"

**Arg2: dFTotalForce**

Description: double value of total force

Data Type: double

Default Value : DFLT_DBL

Syntax: dFTotalForce = 1.0

**Arg3: dA**

Description: double value of a

Data Type: double

Default Value : DFLT_DBL

Syntax: dA = 1.0

**Arg4: dX**

Description: double value of x

Data Type: double

Default Value : DFLT_DBL

Syntax: dX = 1.0

**Arg5: dY**

Description: double value of y

Data Type: double

Default Value : DFLT_DBL

Syntax: dY = 1.0

**Arg6: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg7: iEnDirection**

Description: option for en direction

Data Type: integer

Default Value : 0

Syntax: iEnDirection = 1

**Arg8: dAngleRange**

Description: double value of angle range

Data Type: double

Default Value : 0.0

Syntax: dAngleRange = 1.0

**Arg9: iArrowDir**

Description: option for arrow dir

Data Type: integer

Default Value : 0

Syntax: iArrowDir = 1

**Arg10: bDistributeInAxis**

Description: enable or disable feature distribute in axis

Data Type: bool

Default Value : False

Syntax: bDistributeInAxis = True/False

**Arg11: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg12: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Force.FunctionLoadCylinder.Vector(strName="ForceVector1", dFTotalForce=DFLT_DBL, dA=DFLT_DBL, dX=DFLT_DBL, dY=DFLT_DBL, crCoord=None, iEnDirection=0, dAngleRange=0.0, iArrowDir=0, bDistributeInAxis=False, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Force.NonlinearForce.NOLIN3

## Wrapper Macro

LbcNolin3Exp(...)

## Ribbon-GUI-Location

BoundaryConditions > Force > NonlinearForce > NOLIN3

## Command Description

create nonlinear force NOLIN3

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: dForceScale**

Description: double value of force scale

Data Type: double

Default Value : 0.0

Syntax: dForceScale = 1.0

**Arg3: dMomentScale**

Description: double value of moment scale

Data Type: double

Default Value : 0.0

Syntax: dMomentScale = 1.0

**Arg4: dForcePowerA**

Description: double value of force power a

Data Type: double

Default Value : 0.0

Syntax: dForcePowerA = 1.0

**Arg5: dMomentPowerA**

Description: double value of moment power a

Data Type: double

Default Value : 0.0

Syntax: dMomentPowerA = 1.0

**Arg6: iForcDir**

Description: option for forc dir

Data Type: integer

Default Value : 0

Syntax: iForcDir = 1

**Arg7: iForceDepends**

Description: option for force depends

Data Type: integer

Default Value : 0

Syntax: iForceDepends = 1

**Arg8: iMomentDir**

Description: option for moment dir

Data Type: integer

Default Value : 0

Syntax: iMomentDir = 1

**Arg9: iMomentDepends**

Description: option for moment depends

Data Type: integer

Default Value : 0

Syntax: iMomentDepends = 1

**Arg10: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg11: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg12: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Force.NonlinearForce.NOLIN3(strName="", dForceScale=0.0, dMomentScale=0.0, dForcePowerA=0.0, dMomentPowerA=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCurCoord=None, crlMasterTarget=[], crlSlaveTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Force.NonlinearForce.NOLIN4

## Wrapper Macro

LbcNolin4Exp(...)

## Ribbon-GUI-Location

BoundaryConditions > Force > NonlinearForce > NOLIN4

## Command Description

create NOLIN4 nonlinear force

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: dForceScale**

Description: double value of force scale

Data Type: double

Default Value : 0.0

Syntax: dForceScale = 1.0

**Arg3: dMomentScale**

Description: double value of moment scale

Data Type: double

Default Value : 0.0

Syntax: dMomentScale = 1.0

**Arg4: dForcePowerA**

Description: double value of force power a

Data Type: double

Default Value : 0.0

Syntax: dForcePowerA = 1.0

**Arg5: dMomentPowerA**

Description: double value of moment power a

Data Type: double

Default Value : 0.0

Syntax: dMomentPowerA = 1.0

**Arg6: iForcDir**

Description: option for forc dir

Data Type: integer

Default Value : 0

Syntax: iForcDir = 1

**Arg7: iForceDepends**

Description: option for force depends

Data Type: integer

Default Value : 0

Syntax: iForceDepends = 1

**Arg8: iMomentDir**

Description: option for moment dir

Data Type: integer

Default Value : 0

Syntax: iMomentDir = 1

**Arg9: iMomentDepends**

Description: option for moment depends

Data Type: integer

Default Value : 0

Syntax: iMomentDepends = 1

**Arg10: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg11: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg12: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Force.NonlinearForce.NOLIN4(strName="", dForceScale=0.0, dMomentScale=0.0, dForcePowerA=0.0, dMomentPowerA=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCurCoord=None, crlMasterTarget=[], crlSlaveTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Force.NonlinearForce.NOLIN1

## Wrapper Macro

LbcNolin1Table(...)

## Ribbon-GUI-Location

BoundaryConditions > Force > NonlinearForce > NOLIN1

## Command Description

Create Nonlinear Force of NOLIN1(Table)

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "NonlinearForce1_1"

Syntax: strName = "string input"

**Arg2: dForceScale**

Description: double value of force scale

Data Type: double

Default Value : 0.0

Syntax: dForceScale = 1.0

**Arg3: dMomentScale**

Description: double value of moment scale

Data Type: double

Default Value : 0.0

Syntax: dMomentScale = 1.0

**Arg4: iForcDir**

Description: option for forc dir

Data Type: integer

Default Value : 0

Syntax: iForcDir = 1

**Arg5: iForceDepends**

Description: option for force depends

Data Type: integer

Default Value : 0

Syntax: iForceDepends = 1

**Arg6: iMomentDir**

Description: option for moment dir

Data Type: integer

Default Value : 0

Syntax: iMomentDir = 1

**Arg7: iMomentDepends**

Description: option for moment depends

Data Type: integer

Default Value : 0

Syntax: iMomentDepends = 1

**Arg8: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg9: crForceTable**

Description: entity in database model with type force table

Data Type: cursor

Default Value : None

Syntax: crForceTable = EntityType(id)

**Arg10: crMomentTable**

Description: entity in database model with type moment table

Data Type: cursor

Default Value : None

Syntax: crMomentTable = EntityType(id)

**Arg11: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg12: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Force.NonlinearForce.NOLIN1(strName="NonlinearForce1_1", dForceScale=0.0, dMomentScale=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCoord=None, crForceTable=None, crMomentTable=None, crlMaster=[], crlSlave=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Force.General

## Wrapper Macro

ForceGeneral(...)

## Ribbon-GUI-Location

BoundaryConditions > Force > General

## Command Description

create force general

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: vecForce**

Description: array values of force

Data Type: vector

Default Value : [DFLT_DBL

Syntax: vecForce = [value1, value2, value3]

**Arg5: vecMoment**

Description: array values of moment

Data Type: vector

Default Value : [DFLT_DBL

Syntax: vecMoment = [value1, value2, value3]

**Arg8: iEnArrowDir**

Description: option for en arrow dir

Data Type: integer

Default Value : 0

Syntax: iEnArrowDir = 1

**Arg9: iDistributionMethod**

Description: option for distribution method

Data Type: integer

Default Value : 0

Syntax: iDistributionMethod = 1

**Arg10: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg11: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg12: crNodeSet**

Description: entity in database model with type node set

Data Type: cursor

Default Value : None

Syntax: crNodeSet = EntityType(id)

**Arg13: dFPhase**

Description: double value of phase

Data Type: double

Default Value : 0.0

Syntax: dFPhase = 1.0

**Arg14: dFDelay**

Description: double value of delay

Data Type: double

Default Value : 0.0

Syntax: dFDelay = 1.0

**Arg15: crPhaseTable**

Description: entity in database model with type phase table

Data Type: cursor

Default Value : None

Syntax: crPhaseTable = EntityType(id)

**Arg16: strFormula1**

Description: definition string of input formula1

Data Type: string

Default Value : ""

Syntax: strFormula1 = "string input"

**Arg17: strFormula2**

Description: definition string of input formula2

Data Type: string

Default Value : ""

Syntax: strFormula2 = "string input"

**Arg18: strFormula3**

Description: definition string of input formula3

Data Type: string

Default Value : ""

Syntax: strFormula3 = "string input"

**Arg19: strFormula4**

Description: definition string of input formula4

Data Type: string

Default Value : ""

Syntax: strFormula4 = "string input"

**Arg20: strFormula5**

Description: definition string of input formula5

Data Type: string

Default Value : ""

Syntax: strFormula5 = "string input"

**Arg21: strFormula6**

Description: definition string of input formula6

Data Type: string

Default Value : ""

Syntax: strFormula6 = "string input"

**Arg22: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg23: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Force.General(strName="", vecForce=[DFLT_DBL, DFLT_DBL, DFLT_DBL], vecMoment=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iEnArrowDir=0, iDistributionMethod=0, crCurCoord=None, crTable=None, crNodeSet=None, dFPhase=0.0, dFDelay=0.0, crPhaseTable=None, strFormula1="", strFormula2="", strFormula3="", strFormula4="", strFormula5="", strFormula6="", crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.Force.ForceNormalDirection

## Wrapper Macro

ForceNormalDirection(...)

## Ribbon-GUI-Location

BoundaryConditions > Force > ForceNormalDirection

## Command Description

Create Force (normal direction)

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: vecForce**

Description: array values of force

Data Type: vector

Default Value : [DFLT_DBL

Syntax: vecForce = [value1, value2, value3]

**Arg5: iEnArrowDir**

Description: option for en arrow dir

Data Type: integer

Default Value : 0

Syntax: iEnArrowDir = 1

**Arg6: iDistributionMethod**

Description: option for distribution method

Data Type: integer

Default Value : 0

Syntax: iDistributionMethod = 1

**Arg7: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg9: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.Force.ForceNormalDirection(strName="", vecForce=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iEnArrowDir=0, iDistributionMethod=0, crCurCoord=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus

## Wrapper Macro

InitialAngularVelAbaqus(...)

## Ribbon-GUI-Location

BoundaryConditions > InitialNodalValue > InitialAngularVelocity > Abaqus

## Command Description

Create lbc of initial angular velocity for abaqus

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InitialAngularVelocityAbaqus1"

Syntax: strName = "string input"

**Arg2: dVelocity**

Description: double value of velocity

Data Type: double

Default Value : DFLT_DBL

Syntax: dVelocity = 1.0

**Arg3: strFirstCoord**

Description: definition string of input first coordinate

Data Type: string

Default Value : ""

Syntax: strFirstCoord = "string input"

**Arg4: strSecondCoord**

Description: definition string of input second coordinate

Data Type: string

Default Value : ""

Syntax: strSecondCoord = "string input"

**Arg5: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg6: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus(strName="InitialAngularVelocityAbaqus1", dVelocity=DFLT_DBL, strFirstCoord="", strSecondCoord="", crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General

## Wrapper Macro

InitialDynamic(...)

## Ribbon-GUI-Location

BoundaryConditions > InitialNodalValue > InitialAngularVelocity > General

## Command Description

Command use for BoundaryConditions InitialNodalValue InitialAngularVelocity General

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InitialAngularVelocity1"

Syntax: strName = "string input"

**Arg2: stData**

Description: data structure of LBC_DYNAMIC_INITIAL_CONDITION_DATA (refer PSJ Command Data Structure Document)

Data Type: LBC_DYNAMIC_INITIAL_CONDITION_DATA

Default Value : LBC_DYNAMIC_INITIAL_CONDITION_DATA()

Syntax: stData = LBC_DYNAMIC_INITIAL_CONDITION_DATA(,,,)

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General(strName="InitialAngularVelocity1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.InitialNodalValue.Displacement

## Wrapper Macro

InitialDynamic(...)

## Ribbon-GUI-Location

BoundaryConditions > InitialNodalValue > Displacement

## Command Description

Create Initial Dynamic

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InitialDisplacement1"

Syntax: strName = "string input"

**Arg2: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg3: vecInit**

Description: array values of init

Data Type: vector

Default Value : [DFLT_DBL,DFLT_DBL,DFLT_DBL]

Syntax: vecInit = [value1, value2, value3]

**Arg4: bSelNode**

Description: enable or disable feature sel node

Data Type: bool

Default Value : False

Syntax: bSelNode = True/False

**Arg5: crNodeSet**

Description: entity in database model with type node set

Data Type: cursor

Default Value : None

Syntax: crNodeSet = EntityType(id)

**Arg6: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg9: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InitialNodalValue.Displacement(strName="InitialDisplacement1", iType=0, vecInit=[DFLT_DBL,DFLT_DBL,DFLT_DBL], bSelNode=False, crNodeSet=None, crTable=None, crCoord=None, crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.InitialNodalValue.Velocity

## Wrapper Macro

InitialDynamic(...)

## Ribbon-GUI-Location

BoundaryConditions > InitialNodalValue > Velocity

## Command Description

Command use for BoundaryConditions InitialNodalValue Velocity

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InitialRotationAngle1"

Syntax: strName = "string input"

**Arg2: stData**

Description: data structure of LBC_DYNAMIC_INITIAL_CONDITION_DATA (refer PSJ Command Data Structure Document)

Data Type: LBC_DYNAMIC_INITIAL_CONDITION_DATA

Default Value : LBC_DYNAMIC_INITIAL_CONDITION_DATA()

Syntax: stData = LBC_DYNAMIC_INITIAL_CONDITION_DATA(,,,)

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InitialNodalValue.Velocity(strName="InitialRotationAngle1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None)

```

==========================================================

# BoundaryConditions.InitialNodalValue.RotationAngle

## Wrapper Macro

InitialDynamic(...)

## Ribbon-GUI-Location

BoundaryConditions > InitialNodalValue > RotationAngle

## Command Description

Command use for BoundaryConditions InitialNodalValue RotationAngle

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "InitialVelocity1"

Syntax: strName = "string input"

**Arg2: stData**

Description: data structure of LBC_DYNAMIC_INITIAL_CONDITION_DATA (refer PSJ Command Data Structure Document)

Data Type: LBC_DYNAMIC_INITIAL_CONDITION_DATA

Default Value : LBC_DYNAMIC_INITIAL_CONDITION_DATA()

Syntax: stData = LBC_DYNAMIC_INITIAL_CONDITION_DATA(,,,)

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

BoundaryConditions.InitialNodalValue.RotationAngle(strName="InitialVelocity1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None)

```

==========================================================

# Connections.Pretension.General

## Wrapper Macro

Pretension(...)

## Ribbon-GUI-Location

Connections > Pretension > General

## Command Description

Pretension general

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "BoltLoad001"

Syntax: strName = "string input"

**Arg2: iDir**

Description: option for dir

Data Type: integer

Default Value : 0

Syntax: iDir = 1

**Arg3: dValue**

Description: double value of value

Data Type: double

Default Value : DFLT_DBL

Syntax: dValue = 1.0

**Arg4: bFixLength**

Description: enable or disable feature fix length

Data Type: bool

Default Value : False

Syntax: bFixLength = True/False

**Arg5: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg6: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg7: iLocalUnit**

Description: option for local unit

Data Type: integer

Default Value : 0

Syntax: iLocalUnit = 1

**Arg8: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg9: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg10: bCreate2ADVCStatic**

Description: enable or disable feature create2 advc static

Data Type: bool

Default Value : False

Syntax: bCreate2ADVCStatic = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Pretension.General(strName="BoltLoad001", iDir=0, dValue=DFLT_DBL, bFixLength=False, crTable=None, crCoord=None, iLocalUnit=0, crlTarget=[], crEdit=None, bCreate2ADVCStatic=False)

```

==========================================================

# Connections.Pretension.Abaqus

## Wrapper Macro

PretensionAbaqus(...)

## Ribbon-GUI-Location

Connections > Pretension > Abaqus

## Command Description

Create Pretension Abaqus

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "PreTensionAbaqus1"

Syntax: strName = "string input"

**Arg2: bFixedLenght**

Description: enable or disable feature fixed lenght

Data Type: bool

Default Value : False

Syntax: bFixedLenght = True/False

**Arg3: crTable**

Description: entity in database model with type table

Data Type: cursor

Default Value : None

Syntax: crTable = EntityType(id)

**Arg4: dValue**

Description: double value of value

Data Type: double

Default Value : DFLT_DBL

Syntax: dValue = 1.0

**Arg5: iLocalUnit**

Description: option for local unit

Data Type: integer

Default Value : 0

Syntax: iLocalUnit = 1

**Arg6: strNormal**

Description: definition string of input normal

Data Type: string

Default Value : ""

Syntax: strNormal = "string input"

**Arg7: dlNodePos**

Description: array double values of node pos

Data Type: double list

Default Value : [DFLT_DBL,DFLT_DBL,DFLT_DBL]

Syntax: dlNodePos = [1.0, 2.0]

**Arg8: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg9: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Pretension.Abaqus(strName="PreTensionAbaqus1", bFixedLenght=False, crTable=None, dValue=DFLT_DBL, iLocalUnit=0, strNormal="", dlNodePos=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crEdit=None, crlTarget=[])

```

==========================================================

# Connections.Pretension.Advc

## Wrapper Macro

LbcPretensionAdvc(...)

## Ribbon-GUI-Location

Connections > Pretension > Advc

## Command Description

Create ADVC pretension

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "PreTensionAdvc1"

Syntax: strName = "string input"

**Arg2: bFixedLength**

Description: enable or disable feature fixed length

Data Type: bool

Default Value : False

Syntax: bFixedLength = True/False

**Arg3: crEnforcedVelocity**

Description: entity in database model with type enforced velocity

Data Type: cursor

Default Value : None

Syntax: crEnforcedVelocity = EntityType(id)

**Arg4: dDvalue**

Description: double value of dvalue

Data Type: double

Default Value : 0.0

Syntax: dDvalue = 1.0

**Arg5: iDirUpdateType**

Description: option for dir update type

Data Type: integer

Default Value : 0

Syntax: iDirUpdateType = 1

**Arg6: dlVnormal**

Description: array double values of vnormal

Data Type: double list

Default Value : [0,0,0]

Syntax: dlVnormal = [1.0, 2.0]

**Arg7: dlCtrolNodePos**

Description: array double values of ctrol node pos

Data Type: double list

Default Value : [0,0,0]

Syntax: dlCtrolNodePos = [1.0, 2.0]

**Arg8: iRefNodeId**

Description: option for ref node id

Data Type: integer

Default Value : 0

Syntax: iRefNodeId = 1

**Arg9: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg10: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Pretension.Advc(strName="PreTensionAdvc1", bFixedLength=False, crEnforcedVelocity=None, dDvalue=0.0, iDirUpdateType=0, dlVnormal=[0,0,0], dlCtrolNodePos=[0,0,0], iRefNodeId=0, crEdit=None, crlTarget=[])

```

==========================================================

# Connections.MassElements

## Wrapper Macro

ConnectionNewMass(...)

## Ribbon-GUI-Location

Connections > MassElements

## Command Description

Connection new mass

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: dMass**

Description: double value of mass

Data Type: double

Default Value : 0.01

Syntax: dMass = 1.0

**Arg4: iDof**

Description: option for dof

Data Type: integer

Default Value : 1

Syntax: iDof = 1

**Arg5: bDesigner**

Description: enable or disable feature designer

Data Type: bool

Default Value : True

Syntax: bDesigner = True/False

**Arg6: crCoordinate**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoordinate = EntityType(id)

**Arg7: dOffset0**

Description: double value of offset0

Data Type: double

Default Value : 0.0

Syntax: dOffset0 = 1.0

**Arg8: dOffset1**

Description: double value of offset1

Data Type: double

Default Value : 0.0

Syntax: dOffset1 = 1.0

**Arg9: dOffset2**

Description: double value of offset2

Data Type: double

Default Value : 0.0

Syntax: dOffset2 = 1.0

**Arg10: dInertia0**

Description: double value of inertia0

Data Type: double

Default Value : 0.0

Syntax: dInertia0 = 1.0

**Arg11: dInertia1**

Description: double value of inertia1

Data Type: double

Default Value : 0.0

Syntax: dInertia1 = 1.0

**Arg12: dInertia2**

Description: double value of inertia2

Data Type: double

Default Value : 0.0

Syntax: dInertia2 = 1.0

**Arg13: dInertia3**

Description: double value of inertia3

Data Type: double

Default Value : 0.0

Syntax: dInertia3 = 1.0

**Arg14: dInertia4**

Description: double value of inertia4

Data Type: double

Default Value : 0.0

Syntax: dInertia4 = 1.0

**Arg15: dInertia5**

Description: double value of inertia5

Data Type: double

Default Value : 0.0

Syntax: dInertia5 = 1.0

**Arg16: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg17: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MassElements(strName="", crlTarget=[], dMass=0.01, iDof=1, bDesigner=True, crCoordinate=None, dOffset0=0.0, dOffset1=0.0, dOffset2=0.0, dInertia0=0.0, dInertia1=0.0, dInertia2=0.0, dInertia3=0.0, dInertia4=0.0, dInertia5=0.0, crEdit=None, bUpdateDispCS=True)

```

==========================================================

# Connections.BarBeam

## Wrapper Macro

ConnectionBarBeam(...)

## Ribbon-GUI-Location

Connections > BarBeam

## Command Description

create Connections Bar or Beam

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iEType**

Description: option for e type

Data Type: integer

Default Value : 10

Syntax: iEType = 1

**Arg3: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg4: crProp**

Description: entity in database model with type property

Data Type: cursor

Default Value : None

Syntax: crProp = EntityType(id)

**Arg5: dlOrient**

Description: array double values of orient

Data Type: double list

Default Value : []

Syntax: dlOrient = [1.0, 2.0]

**Arg6: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg7: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.BarBeam(strName="", iEType=10, iMethod=1, crProp=None, dlOrient=[], crlMasterTarget=[], crlSlaveTarget=[])

```

==========================================================

# Connections.GapsDetail

## Wrapper Macro

ConnectGap(...)

## Ribbon-GUI-Location

Connections > GapsDetail

## Command Description

Command use for Connections GapsDetail

## Argument List

**Arg1: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg2: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg3: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg4: iOriMode**

Description: option for orient mode

Data Type: integer

Default Value : 0

Syntax: iOriMode = 1

**Arg5: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg6: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg7: dU0**

Description: double value of u0

Data Type: double

Default Value : DFLT_DBL

Syntax: dU0 = 1.0

**Arg8: dF0**

Description: double value of f0

Data Type: double

Default Value : DFLT_DBL

Syntax: dF0 = 1.0

**Arg9: dKa**

Description: double value of ka

Data Type: double

Default Value : DFLT_DBL

Syntax: dKa = 1.0

**Arg10: dKb**

Description: double value of kb

Data Type: double

Default Value : DFLT_DBL

Syntax: dKb = 1.0

**Arg11: dKt**

Description: double value of kt

Data Type: double

Default Value : DFLT_DBL

Syntax: dKt = 1.0

**Arg12: dMar**

Description: double value of mar

Data Type: double

Default Value : DFLT_DBL

Syntax: dMar = 1.0

**Arg13: dMu1**

Description: double value of mu1

Data Type: double

Default Value : DFLT_DBL

Syntax: dMu1 = 1.0

**Arg14: dMu2**

Description: double value of mu2

Data Type: double

Default Value : DFLT_DBL

Syntax: dMu2 = 1.0

**Arg15: dlOriVec**

Description: array double values of orient vec

Data Type: double list

Default Value : []

Syntax: dlOriVec = [1.0, 2.0]

**Arg16: dTmax**

Description: double value of tmax

Data Type: double

Default Value : DFLT_DBL

Syntax: dTmax = 1.0

**Arg17: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg18: dTrmin**

Description: double value of trmin

Data Type: double

Default Value : DFLT_DBL

Syntax: dTrmin = 1.0

**Arg19: crEditCur**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEditCur = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.GapsDetail(crlMaster=[], crlSlave=[], iMethod=0, iOriMode=0, crCoord=None, strName="", dU0=DFLT_DBL, dF0=DFLT_DBL, dKa=DFLT_DBL, dKb=DFLT_DBL, dKt=DFLT_DBL, dMar=DFLT_DBL, dMu1=DFLT_DBL, dMu2=DFLT_DBL, dlOriVec=[], dTmax=DFLT_DBL, dTol=DFLT_DBL, dTrmin=DFLT_DBL, crEditCur=None)

```

==========================================================

# Connections.Plot

## Wrapper Macro

Property1DPlot(...)

## Ribbon-GUI-Location

Connections > Plot

## Command Description

Create 1D plot connection

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "PLOT_1"

Syntax: strName = "string input"

**Arg2: iPID**

Description: option for p ID

Data Type: integer

Default Value : 1

Syntax: iPID = 1

**Arg3: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Plot(strName="PLOT_1", iPID=1, crlTarget=[], crEdit=None)

```

==========================================================

# Connections.CreateConnConm

## Wrapper Macro

CreateConnConm(...)

## Ribbon-GUI-Location

Connections > CreateConnConm

## Command Description

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iEType**

Description: option for e type

Data Type: integer

Default Value : 0

Syntax: iEType = 1

**Arg3: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg4: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg5: iConmId**

Description: option for conm id

Data Type: integer

Default Value : 0

Syntax: iConmId = 1

**Arg6: crMatCoord**

Description: entity in database model with type material coordinate

Data Type: cursor

Default Value : None

Syntax: crMatCoord = EntityType(id)

**Arg7: dMass**

Description: double value of mass

Data Type: double

Default Value : 0

Syntax: dMass = 1.0

**Arg8: dlX**

Description: array double values of x

Data Type: double list

Default Value : [0

Syntax: dlX = [1.0, 2.0]

**Arg11: dlVintertia0**

Description: array double values of vintertia0

Data Type: double list

Default Value : []()

Syntax: dlVintertia0 = [1.0, 2.0]

**Arg14: dlVintertia1**

Description: array double values of vintertia1

Data Type: double list

Default Value : [0

Syntax: dlVintertia1 = [1.0, 2.0]

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: listRbe3TermConnection**

Description: list data structure of RBE3_TERM_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: RBE3_TERM_CONNECTION

Default Value : RBE3_TERM_CONNECTION()

Syntax: listRbe3TermConnection = [RBE3_TERM_CONNECTION(,,,), RBE3_TERM_CONNECTION(,,,)]

**Arg5: iTypeRBE3**

Description: option for type r b e3

Data Type: integer

Default Value : 3

Syntax: iTypeRBE3 = 1

**Arg6: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg7: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg9: posVirtualNodePos**

Description: array double value [x, y, z] in coordinate system of virtual node pos

Data Type: position

Default Value : [0

Syntax: posVirtualNodePos = [x, y, z]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg15: bCornerOnly**

Description: enable or disable feature corner only

Data Type: bool

Default Value : False

Syntax: bCornerOnly = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RBE3(iMethod=0, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, posVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, bUpdateDispCS=True, bCornerOnly=False)

```

==========================================================

# Connections.RigidWall

## Wrapper Macro

LBCRigdWall(...)

## Ribbon-GUI-Location

Connections > RigidWall

## Command Description

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "RigidWall1"

Syntax: strName = "string input"

**Arg2: iObject**

Description: option for object

Data Type: integer

Default Value : 0

Syntax: iObject = 1

**Arg3: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg4: iMotion**

Description: option for motion

Data Type: integer

Default Value : 0

Syntax: iMotion = 1

**Arg5: iFriction**

Description: option for friction

Data Type: integer

Default Value : 0

Syntax: iFriction = 1

**Arg6: iOrtho**

Description: option for ortho

Data Type: integer

Default Value : 0

Syntax: iOrtho = 1

**Arg7: iForces**

Description: option for forces

Data Type: integer

Default Value : 0

Syntax: iForces = 1

**Arg8: dFinite1**

Description: double value of finite1

Data Type: double

Default Value : DFLT_DBL

Syntax: dFinite1 = 1.0

**Arg9: dFinite2**

Description: double value of finite2

Data Type: double

Default Value : DFLT_DBL

Syntax: dFinite2 = 1.0

**Arg10: dMotionMass**

Description: double value of motion mass

Data Type: double

Default Value : DFLT_DBL

Syntax: dMotionMass = 1.0

**Arg11: dMotionInitVelo**

Description: double value of motion init velo

Data Type: double

Default Value : DFLT_DBL

Syntax: dMotionInitVelo = 1.0

**Arg12: dFricCoulombCoeff**

Description: double value of fric coulomb coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dFricCoulombCoeff = 1.0

**Arg13: dFricWeldVelo**

Description: double value of fric weld velo

Data Type: double

Default Value : DFLT_DBL

Syntax: dFricWeldVelo = 1.0

**Arg14: iForcesCirclesNum**

Description: option for forces circles number

Data Type: integer

Default Value : 0

Syntax: iForcesCirclesNum = 1

**Arg15: dOrthoStaticCoeff1**

Description: double value of ortho static coeff1

Data Type: double

Default Value : DFLT_DBL

Syntax: dOrthoStaticCoeff1 = 1.0

**Arg16: dOrthoStaticCoeff2**

Description: double value of ortho static coeff2

Data Type: double

Default Value : DFLT_DBL

Syntax: dOrthoStaticCoeff2 = 1.0

**Arg17: dOrthoDynamicCoeff1**

Description: double value of ortho dynamic coeff1

Data Type: double

Default Value : DFLT_DBL

Syntax: dOrthoDynamicCoeff1 = 1.0

**Arg18: dOrthoDynamicCoeff2**

Description: double value of ortho dynamic coeff2

Data Type: double

Default Value : DFLT_DBL

Syntax: dOrthoDynamicCoeff2 = 1.0

**Arg19: dOrthoDecayConst1**

Description: double value of ortho decay const1

Data Type: double

Default Value : DFLT_DBL

Syntax: dOrthoDecayConst1 = 1.0

**Arg20: dOrthoDecayConst2**

Description: double value of ortho decay const2

Data Type: double

Default Value : DFLT_DBL

Syntax: dOrthoDecayConst2 = 1.0

**Arg21: dOrthoFricVector1**

Description: double value of ortho fric vector1

Data Type: double

Default Value : DFLT_DBL

Syntax: dOrthoFricVector1 = 1.0

**Arg22: dOrthoFricVector2**

Description: double value of ortho fric vector2

Data Type: double

Default Value : DFLT_DBL

Syntax: dOrthoFricVector2 = 1.0

**Arg23: dOrthoFricVector3**

Description: double value of ortho fric vector3

Data Type: double

Default Value : DFLT_DBL

Syntax: dOrthoFricVector3 = 1.0

**Arg24: bAllNodeSlave**

Description: enable or disable feature all node slave

Data Type: bool

Default Value : False

Syntax: bAllNodeSlave = True/False

**Arg25: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg26: crAreaFaceSet**

Description: entity in database model with type area face set

Data Type: cursor

Default Value : None

Syntax: crAreaFaceSet = EntityType(id)

**Arg27: crVisualNodeSet**

Description: entity in database model with type visual node set

Data Type: cursor

Default Value : None

Syntax: crVisualNodeSet = EntityType(id)

**Arg28: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg29: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidWall(strName="RigidWall1", iObject=0, iType=0, iMotion=0, iFriction=0, iOrtho=0, iForces=0, dFinite1=DFLT_DBL, dFinite2=DFLT_DBL, dMotionMass=DFLT_DBL, dMotionInitVelo=DFLT_DBL, dFricCoulombCoeff=DFLT_DBL, dFricWeldVelo=DFLT_DBL, iForcesCirclesNum=0, dOrthoStaticCoeff1=DFLT_DBL, dOrthoStaticCoeff2=DFLT_DBL, dOrthoDynamicCoeff1=DFLT_DBL, dOrthoDynamicCoeff2=DFLT_DBL, dOrthoDecayConst1=DFLT_DBL, dOrthoDecayConst2=DFLT_DBL, dOrthoFricVector1=DFLT_DBL, dOrthoFricVector2=DFLT_DBL, dOrthoFricVector3=DFLT_DBL, bAllNodeSlave=False, crCoord=None, crAreaFaceSet=None, crVisualNodeSet=None, crlTarget=[], crEdit=None)

```

==========================================================

# Connections.Connector

## Wrapper Macro

Connector(...)

## Ribbon-GUI-Location

Connections > Connector

## Command Description

create Connector

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg3: iConnectType**

Description: option for connect type

Data Type: integer

Default Value : 0

Syntax: iConnectType = 1

**Arg4: iRefNode**

Description: option for ref node

Data Type: integer

Default Value : 0

Syntax: iRefNode = 1

**Arg5: iElemCs**

Description: option for element cs

Data Type: integer

Default Value : 0

Syntax: iElemCs = 1

**Arg6: crLocalCS**

Description: entity in database model with type local c s

Data Type: cursor

Default Value : None

Syntax: crLocalCS = EntityType(id)

**Arg7: crlElasticity**

Description: array entities in model with type elasticity

Data Type: cursor list

Default Value : []

Syntax: crlElasticity = [EntityType(id1, id2, id3)]

**Arg8: crlDamp**

Description: array entities in model with type damper

Data Type: cursor list

Default Value : []

Syntax: crlDamp = [EntityType(id1, id2, id3)]

**Arg9: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg10: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Connector(strName="", iMethod=1, iConnectType=0, iRefNode=0, iElemCs=0, crLocalCS=None, crlElasticity=[], crlDamp=[], crlMasterTarget=[], crlSlaveTarget=[], crEdit=None)

```

==========================================================

# Connections.BoltMeshingSplitOnly

## Wrapper Macro

BoltMeshing2_SplitOnly(...)

## Ribbon-GUI-Location

Connections > BoltMeshingSplitOnly

## Command Description

Command use for Connections BoltMeshingSplitOnly

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iPartcutparamImethod**

Description: option for partcutparam imethod

Data Type: integer

Default Value : 0

Syntax: iPartcutparamImethod = 1

**Arg3: dPartcutparamDoffset**

Description: double value of partcutparam doffset

Data Type: double

Default Value : 0.0

Syntax: dPartcutparamDoffset = 1.0

**Arg4: iPartcutparamBshareface**

Description: option for partcutparam bshareface

Data Type: integer

Default Value : 0

Syntax: iPartcutparamBshareface = 1

**Arg5: iPartcutparamBseparateface**

Description: option for partcutparam bseparateface

Data Type: integer

Default Value : 0

Syntax: iPartcutparamBseparateface = 1

**Arg6: iPartcutparamBsplitonly**

Description: option for partcutparam bsplitonly

Data Type: integer

Default Value : 0

Syntax: iPartcutparamBsplitonly = 1

**Arg7: iPartcutparamBmakesectionface**

Description: option for partcutparam bmakesectionface

Data Type: integer

Default Value : 0

Syntax: iPartcutparamBmakesectionface = 1

**Arg8: crPartcutparamCoord**

Description: entity in database model with type partcutparam coordinate

Data Type: cursor

Default Value : None

Syntax: crPartcutparamCoord = EntityType(id)

**Arg9: surfaceMesh**

Description: data structure of SURFACE_MESH (refer PSJ Command Data Structure Document)

Data Type: SURFACE_MESH

Default Value : SURFACE_MESH()

Syntax: surfaceMesh = SURFACE_MESH(,,,)

**Arg10: bLBCPRETENSIONABAQUSDATABfixedlenght**

Description: enable or disable feature load-boundary-condition p r e t e n s i o n a b a q u s d a t a bfixedlenght

Data Type: bool

Default Value : False

Syntax: bLBCPRETENSIONABAQUSDATABfixedlenght = True/False

**Arg11: crLBCPRETENSIONABAQUSDATACrtable**

Description: entity in database model with type load-boundary-condition p r e t e n s i o n a b a q u s d a t a crtable

Data Type: cursor

Default Value : None

Syntax: crLBCPRETENSIONABAQUSDATACrtable = EntityType(id)

**Arg12: dLBCPRETENSIONABAQUSDATADvalue**

Description: double value of load-boundary-condition p r e t e n s i o n a b a q u s d a t a dvalue

Data Type: double

Default Value : 0.0

Syntax: dLBCPRETENSIONABAQUSDATADvalue = 1.0

**Arg13: iLBCPRETENSIONABAQUSDATAIlocalunit**

Description: option for load-boundary-condition p r e t e n s i o n a b a q u s d a t a ilocalunit

Data Type: integer

Default Value : 0

Syntax: iLBCPRETENSIONABAQUSDATAIlocalunit = 1

**Arg14: strLBCPRETENSIONABAQUSDATAStrnormal**

Description: definition string of input load-boundary-condition p r e t e n s i o n a b a q u s d a t a strnormal

Data Type: string

Default Value : ""

Syntax: strLBCPRETENSIONABAQUSDATAStrnormal = "string input"

**Arg15: posLBCPRETENSIONABAQUSDATATvctrolnodepos**

Description: array double value [x, y, z] in coordinate system of load-boundary-condition p r e t e n s i o n a b a q u s d a t a tvctrolnodepos

Data Type: position

Default Value : [0,0,0]

Syntax: posLBCPRETENSIONABAQUSDATATvctrolnodepos = [x, y, z]

**Arg16: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg17: poslCutter**

Description: list positions [x, y, z] in coordinate system of cutter

Data Type: position list

Default Value : []

Syntax: poslCutter = [[x, y, z], [x, y, z]]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.BoltMeshingSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE_MESH(), bLBCPRETENSIONABAQUSDATABfixedlenght=False, crLBCPRETENSIONABAQUSDATACrtable=None, dLBCPRETENSIONABAQUSDATADvalue=0.0, iLBCPRETENSIONABAQUSDATAIlocalunit=0, strLBCPRETENSIONABAQUSDATAStrnormal="", posLBCPRETENSIONABAQUSDATATvctrolnodepos=[0,0,0], crlTarget=[], poslCutter=[])

```

==========================================================

# Connections.BoltMeshingNotSplitOnly

## Wrapper Macro

BoltMeshing2_NotSplitOnly(...)

## Ribbon-GUI-Location

Connections > BoltMeshingNotSplitOnly

## Command Description

Command use for Connections BoltMeshingNotSplitOnly

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iPartcutparamImethod**

Description: option for partcutparam imethod

Data Type: integer

Default Value : 0

Syntax: iPartcutparamImethod = 1

**Arg3: dPartcutparamDoffset**

Description: double value of partcutparam doffset

Data Type: double

Default Value : 0.0

Syntax: dPartcutparamDoffset = 1.0

**Arg4: iPartcutparamBshareface**

Description: option for partcutparam bshareface

Data Type: integer

Default Value : 0

Syntax: iPartcutparamBshareface = 1

**Arg5: iPartcutparamBseparateface**

Description: option for partcutparam bseparateface

Data Type: integer

Default Value : 0

Syntax: iPartcutparamBseparateface = 1

**Arg6: iPartcutparamBsplitonly**

Description: option for partcutparam bsplitonly

Data Type: integer

Default Value : 0

Syntax: iPartcutparamBsplitonly = 1

**Arg7: iPartcutparamBmakesectionface**

Description: option for partcutparam bmakesectionface

Data Type: integer

Default Value : 0

Syntax: iPartcutparamBmakesectionface = 1

**Arg8: crPartcutparamCoord**

Description: entity in database model with type partcutparam coordinate

Data Type: cursor

Default Value : None

Syntax: crPartcutparamCoord = EntityType(id)

**Arg9: surfaceMesh**

Description: data structure of SURFACE_MESH (refer PSJ Command Data Structure Document)

Data Type: SURFACE_MESH

Default Value : SURFACE_MESH()

Syntax: surfaceMesh = SURFACE_MESH(,,,)

**Arg10: iLBCPRETENSIONDATAIdir**

Description: option for load-boundary-condition p r e t e n s i o n d a t a idir

Data Type: integer

Default Value : 0

Syntax: iLBCPRETENSIONDATAIdir = 1

**Arg11: dLBCPRETENSIONDATADvalue**

Description: double value of load-boundary-condition p r e t e n s i o n d a t a dvalue

Data Type: double

Default Value : 0.0

Syntax: dLBCPRETENSIONDATADvalue = 1.0

**Arg12: bLBCPRETENSIONDATABfixlength**

Description: enable or disable feature load-boundary-condition p r e t e n s i o n d a t a bfixlength

Data Type: bool

Default Value : False

Syntax: bLBCPRETENSIONDATABfixlength = True/False

**Arg13: crLBCPRETENSIONDATACrtable**

Description: entity in database model with type load-boundary-condition p r e t e n s i o n d a t a crtable

Data Type: cursor

Default Value : None

Syntax: crLBCPRETENSIONDATACrtable = EntityType(id)

**Arg14: crLBCPRETENSIONDATACrcoord**

Description: entity in database model with type load-boundary-condition p r e t e n s i o n d a t a crcoord

Data Type: cursor

Default Value : None

Syntax: crLBCPRETENSIONDATACrcoord = EntityType(id)

**Arg15: iLBCPRETENSIONDATAIlocalunit**

Description: option for load-boundary-condition p r e t e n s i o n d a t a ilocalunit

Data Type: integer

Default Value : 0

Syntax: iLBCPRETENSIONDATAIlocalunit = 1

**Arg16: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg17: poslCutter**

Description: list positions [x, y, z] in coordinate system of cutter

Data Type: position list

Default Value : []

Syntax: poslCutter = [[x, y, z], [x, y, z]]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.BoltMeshingNotSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE_MESH(), iLBCPRETENSIONDATAIdir=0, dLBCPRETENSIONDATADvalue=0.0, bLBCPRETENSIONDATABfixlength=False, crLBCPRETENSIONDATACrtable=None, crLBCPRETENSIONDATACrcoord=None, iLBCPRETENSIONDATAIlocalunit=0, crlTarget=[], poslCutter=[])

```

==========================================================

# Connections.BoltConnections.Edge.TypeC

## Wrapper Macro

Lbc_Bolt_Modeling_Type_C_Edge(...)

## Ribbon-GUI-Location

Connections > BoltConnections > Edge > TypeC

## Command Description

create bolt connections by TypeC edge.

## Argument List

**Arg1: crlEdgeCur1**

Description: array entities in model with type edge cur1

Data Type: cursor list

Default Value : []

Syntax: crlEdgeCur1 = [EntityType(id1, id2, id3)]

**Arg2: crlEdgeCur2**

Description: array entities in model with type edge cur2

Data Type: cursor list

Default Value : []

Syntax: crlEdgeCur2 = [EntityType(id1, id2, id3)]

**Arg3: strRbeName**

Description: definition string of input rbe name

Data Type: string

Default Value : "RBE"

Syntax: strRbeName = "string input"

**Arg4: dPlaneTol**

Description: double value of plane tolerance

Data Type: double

Default Value : 20.0

Syntax: dPlaneTol = 1.0

**Arg5: dMaxBoltHeight**

Description: double value of maximize bolt height

Data Type: double

Default Value : 100.0

Syntax: dMaxBoltHeight = 1.0

**Arg6: iConnectionType**

Description: option for connection type

Data Type: integer

Default Value : 0

Syntax: iConnectionType = 1

**Arg7: iCoincidentNodes**

Description: option for coincident nodes

Data Type: integer

Default Value : 1

Syntax: iCoincidentNodes = 1

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTolerance = 1.0

**Arg9: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg10: dStiffnessX**

Description: double value of stiffness x

Data Type: double

Default Value : 0.0

Syntax: dStiffnessX = 1.0

**Arg11: dStiffnessY**

Description: double value of stiffness y

Data Type: double

Default Value : 0.0

Syntax: dStiffnessY = 1.0

**Arg12: dStiffnessZ**

Description: double value of stiffness z

Data Type: double

Default Value : 0.0

Syntax: dStiffnessZ = 1.0

**Arg13: iLocalStiffUnit**

Description: option for local stiff unit

Data Type: integer

Default Value : 0

Syntax: iLocalStiffUnit = 1

**Arg14: dRotateStiffX**

Description: double value of rotate stiff x

Data Type: double

Default Value : 0.0

Syntax: dRotateStiffX = 1.0

**Arg15: dRotateStiffY**

Description: double value of rotate stiff y

Data Type: double

Default Value : 0.0

Syntax: dRotateStiffY = 1.0

**Arg16: dRotateStiffZ**

Description: double value of rotate stiff z

Data Type: double

Default Value : 0.0

Syntax: dRotateStiffZ = 1.0

**Arg17: iLocalRotateStiffUnit**

Description: option for local rotate stiff unit

Data Type: integer

Default Value : 0

Syntax: iLocalRotateStiffUnit = 1

**Arg18: dDampCoef**

Description: double value of damper coefficient

Data Type: double

Default Value : 0.0

Syntax: dDampCoef = 1.0

**Arg19: dStressCoef**

Description: double value of stress coefficient

Data Type: double

Default Value : 0.0

Syntax: dStressCoef = 1.0

**Arg20: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg21: iTopRbeType**

Description: option for top rbe type

Data Type: integer

Default Value : 0

Syntax: iTopRbeType = 1

**Arg22: dTopPitch**

Description: double value of top pitch

Data Type: double

Default Value : 10

Syntax: dTopPitch = 1.0

**Arg23: dTopRemoveDepth**

Description: double value of top remove depth

Data Type: double

Default Value : 0.0

Syntax: dTopRemoveDepth = 1.0

**Arg24: iBotRbeType**

Description: option for bot rbe type

Data Type: integer

Default Value : 0

Syntax: iBotRbeType = 1

**Arg25: dBotPitch**

Description: double value of bot pitch

Data Type: double

Default Value : 10

Syntax: dBotPitch = 1.0

**Arg26: dBotRemoveDepth**

Description: double value of bot remove depth

Data Type: double

Default Value : 0.0

Syntax: dBotRemoveDepth = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.BoltConnections.Edge.TypeC(crlEdgeCur1=[], crlEdgeCur2=[], strRbeName="RBE", dPlaneTol=20.0, dMaxBoltHeight=100.0, iConnectionType=0, iCoincidentNodes=1, dTolerance=0.0, iGround=0, dStiffnessX=0.0, dStiffnessY=0.0, dStiffnessZ=0.0, iLocalStiffUnit=0, dRotateStiffX=0.0, dRotateStiffY=0.0, dRotateStiffZ=0.0, iLocalRotateStiffUnit=0, dDampCoef=0.0, dStressCoef=0.0, crCurCoord=None, iTopRbeType=0, dTopPitch=10, dTopRemoveDepth=0.0, iBotRbeType=0, dBotPitch=10, dBotRemoveDepth=0.0)

```

==========================================================

# Connections.BoltConnections.Edge.TypeB

## Wrapper Macro

Lbc_Bolt_Modeling_Type_B_Edge(...)

## Ribbon-GUI-Location

Connections > BoltConnections > Edge > TypeB

## Command Description

## Argument List

**Arg1: crlEdgeCur1**

Description: array entities in model with type edge cur1

Data Type: cursor list

Default Value : []

Syntax: crlEdgeCur1 = [EntityType(id1, id2, id3)]

**Arg2: crlEdgeCur2**

Description: array entities in model with type edge cur2

Data Type: cursor list

Default Value : []

Syntax: crlEdgeCur2 = [EntityType(id1, id2, id3)]

**Arg3: strRbeName**

Description: definition string of input rbe name

Data Type: string

Default Value : "RBE"

Syntax: strRbeName = "string input"

**Arg4: strBarName**

Description: definition string of input bar name

Data Type: string

Default Value : ""

Syntax: strBarName = "string input"

**Arg5: iShaftType**

Description: option for shaft type

Data Type: integer

Default Value : 0

Syntax: iShaftType = 1

**Arg6: crCurBarProperty**

Description: entity in database model with type bar property

Data Type: cursor

Default Value : None

Syntax: crCurBarProperty = EntityType(id)

**Arg7: dPlaneTol**

Description: double value of plane tolerance

Data Type: double

Default Value : 20.0

Syntax: dPlaneTol = 1.0

**Arg8: dMaxBoltHeight**

Description: double value of maximize bolt height

Data Type: double

Default Value : 100.0

Syntax: dMaxBoltHeight = 1.0

**Arg9: bPretensionLoad**

Description: enable or disable feature pretension load

Data Type: bool

Default Value : False

Syntax: bPretensionLoad = True/False

**Arg10: iSolverType**

Description: option for solver type

Data Type: integer

Default Value : 0

Syntax: iSolverType = 1

**Arg11: dForceValue**

Description: double value of force value

Data Type: double

Default Value : 0.0

Syntax: dForceValue = 1.0

**Arg12: iPreTenDof**

Description: option for pre ten dof

Data Type: integer

Default Value : 0

Syntax: iPreTenDof = 1

**Arg13: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg14: iBoltFixLength**

Description: option for bolt fix length

Data Type: integer

Default Value : 0

Syntax: iBoltFixLength = 1

**Arg15: iTopSlot**

Description: option for top slot

Data Type: integer

Default Value : 0

Syntax: iTopSlot = 1

**Arg16: dRBE1**

Description: double value of r b e1

Data Type: double

Default Value : 0.0

Syntax: dRBE1 = 1.0

**Arg17: dRBE2**

Description: double value of r b e2

Data Type: double

Default Value : 0.0

Syntax: dRBE2 = 1.0

**Arg18: dBotDtDia**

Description: double value of bot dt dia

Data Type: double

Default Value : 0.0

Syntax: dBotDtDia = 1.0

**Arg19: dPitch**

Description: double value of pitch

Data Type: double

Default Value : 10.0

Syntax: dPitch = 1.0

**Arg20: iBotRbeConnType**

Description: option for bot rbe conn type

Data Type: integer

Default Value : 0

Syntax: iBotRbeConnType = 1

**Arg21: bIfCreate2ADVCStaticProcessForBoltFixLength**

Description: enable or disable feature if create2 advc static process for bolt fix length

Data Type: bool

Default Value : False

Syntax: bIfCreate2ADVCStaticProcessForBoltFixLength = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.BoltConnections.Edge.TypeB(crlEdgeCur1=[], crlEdgeCur2=[], strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, dRBE2=0.0, dBotDtDia=0.0, dPitch=10.0, iBotRbeConnType=0, bIfCreate2ADVCStaticProcessForBoltFixLength=False)

```

==========================================================

# Connections.BoltConnections.Edge.TypeD

## Wrapper Macro

Lbc_Bolt_Modeling_Type_D(...)

## Ribbon-GUI-Location

Connections > BoltConnections > Edge > TypeD

## Command Description

create bolt connection typeD

## Argument List

**Arg1: crlEdgeCur1**

Description: array entities in model with type edge cur1

Data Type: cursor list

Default Value : []

Syntax: crlEdgeCur1 = [EntityType(id1, id2, id3)]

**Arg2: crlEdgeCur2**

Description: array entities in model with type edge cur2

Data Type: cursor list

Default Value : []

Syntax: crlEdgeCur2 = [EntityType(id1, id2, id3)]

**Arg3: strMpcName**

Description: definition string of input mpc name

Data Type: string

Default Value : "MPC"

Syntax: strMpcName = "string input"

**Arg4: dConnRadius**

Description: double value of conn radius

Data Type: double

Default Value : 0.0

Syntax: dConnRadius = 1.0

**Arg5: dPlaneTol**

Description: double value of plane tolerance

Data Type: double

Default Value : 20.0

Syntax: dPlaneTol = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.BoltConnections.Edge.TypeD(crlEdgeCur1=[], crlEdgeCur2=[], strMpcName="MPC", dConnRadius=0.0, dPlaneTol=20.0)

```

==========================================================

# Connections.BoltConnections.Edge.TypeA

## Wrapper Macro

Lbc_Bolt_Modeling_Type_A_Edge(...)

## Ribbon-GUI-Location

Connections > BoltConnections > Edge > TypeA

## Command Description

Create Lbc TypeA Bolt Edge method

## Argument List

**Arg1: crlEdgeCur1**

Description: array entities in model with type edge cur1

Data Type: cursor list

Default Value : []

Syntax: crlEdgeCur1 = [EntityType(id1, id2, id3)]

**Arg2: crlEdgeCur2**

Description: array entities in model with type edge cur2

Data Type: cursor list

Default Value : []

Syntax: crlEdgeCur2 = [EntityType(id1, id2, id3)]

**Arg3: strRbeName**

Description: definition string of input rbe name

Data Type: string

Default Value : "RBE"

Syntax: strRbeName = "string input"

**Arg4: strBarName**

Description: definition string of input bar name

Data Type: string

Default Value : ""

Syntax: strBarName = "string input"

**Arg5: iShaftType**

Description: option for shaft type

Data Type: integer

Default Value : 0

Syntax: iShaftType = 1

**Arg6: crCurBarProperty**

Description: entity in database model with type bar property

Data Type: cursor

Default Value : None

Syntax: crCurBarProperty = EntityType(id)

**Arg7: dPlaneTol**

Description: double value of plane tolerance

Data Type: double

Default Value : 20.0

Syntax: dPlaneTol = 1.0

**Arg8: dMaxBoltHeight**

Description: double value of maximize bolt height

Data Type: double

Default Value : 100.0

Syntax: dMaxBoltHeight = 1.0

**Arg9: bPretensionLoad**

Description: enable or disable feature pretension load

Data Type: bool

Default Value : False

Syntax: bPretensionLoad = True/False

**Arg10: iSolverType**

Description: option for solver type

Data Type: integer

Default Value : 0

Syntax: iSolverType = 1

**Arg11: dForceValue**

Description: double value of force value

Data Type: double

Default Value : 0.0

Syntax: dForceValue = 1.0

**Arg12: iPreTenDof**

Description: option for pre ten dof

Data Type: integer

Default Value : 0

Syntax: iPreTenDof = 1

**Arg13: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg14: iBoltFixLength**

Description: option for bolt fix length

Data Type: integer

Default Value : 0

Syntax: iBoltFixLength = 1

**Arg15: iTopSlot**

Description: option for top slot

Data Type: integer

Default Value : 0

Syntax: iTopSlot = 1

**Arg16: dRBE1**

Description: double value of r b e1

Data Type: double

Default Value : 0.0

Syntax: dRBE1 = 1.0

**Arg17: iBotSlot**

Description: option for bot slot

Data Type: integer

Default Value : 0

Syntax: iBotSlot = 1

**Arg18: dRBE2**

Description: double value of r b e2

Data Type: double

Default Value : 0.0

Syntax: dRBE2 = 1.0

**Arg19: bIsCreate2ADVCStaticProcessForFixLength**

Description: enable or disable feature is create2 advc static process for fix length

Data Type: bool

Default Value : False

Syntax: bIsCreate2ADVCStaticProcessForFixLength = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.BoltConnections.Edge.TypeA(crlEdgeCur1=[], crlEdgeCur2=[], strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, iBotSlot=0, dRBE2=0.0, bIsCreate2ADVCStaticProcessForFixLength=False)

```

==========================================================

# Connections.BoltConnections.Face.TypeC

## Wrapper Macro

Lbc_Bolt_Modeling_Type_C_Face(...)

## Ribbon-GUI-Location

Connections > BoltConnections > Face > TypeC

## Command Description

Create Lbc TypeC Bolt Face method

## Argument List

**Arg1: crlFaceCur1**

Description: array entities in model with type face cur1

Data Type: cursor list

Default Value : []

Syntax: crlFaceCur1 = [EntityType(id1, id2, id3)]

**Arg2: crlFaceCur2**

Description: array entities in model with type face cur2

Data Type: cursor list

Default Value : []

Syntax: crlFaceCur2 = [EntityType(id1, id2, id3)]

**Arg3: strRbeName**

Description: definition string of input rbe name

Data Type: string

Default Value : "RBE"

Syntax: strRbeName = "string input"

**Arg4: dPlaneTol**

Description: double value of plane tolerance

Data Type: double

Default Value : 20

Syntax: dPlaneTol = 1.0

**Arg5: dMaxBoltHeight**

Description: double value of maximize bolt height

Data Type: double

Default Value : 100

Syntax: dMaxBoltHeight = 1.0

**Arg6: dMaxDiameter**

Description: double value of maximize diameter

Data Type: double

Default Value : 0

Syntax: dMaxDiameter = 1.0

**Arg7: dMinDiameter**

Description: double value of minimize diameter

Data Type: double

Default Value : 0

Syntax: dMinDiameter = 1.0

**Arg8: iConnectionType**

Description: option for connection type

Data Type: integer

Default Value : 0

Syntax: iConnectionType = 1

**Arg9: iCoincidentNodes**

Description: option for coincident nodes

Data Type: integer

Default Value : 1

Syntax: iCoincidentNodes = 1

**Arg10: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTolerance = 1.0

**Arg11: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg12: dStiffnessX**

Description: double value of stiffness x

Data Type: double

Default Value : 0.0

Syntax: dStiffnessX = 1.0

**Arg13: dStiffnessY**

Description: double value of stiffness y

Data Type: double

Default Value : 0.0

Syntax: dStiffnessY = 1.0

**Arg14: dStiffnessZ**

Description: double value of stiffness z

Data Type: double

Default Value : 0.0

Syntax: dStiffnessZ = 1.0

**Arg15: iLocalStiffUnit**

Description: option for local stiff unit

Data Type: integer

Default Value : 0

Syntax: iLocalStiffUnit = 1

**Arg16: dRotateStiffX**

Description: double value of rotate stiff x

Data Type: double

Default Value : 0.0

Syntax: dRotateStiffX = 1.0

**Arg17: dRotateStiffY**

Description: double value of rotate stiff y

Data Type: double

Default Value : 0.0

Syntax: dRotateStiffY = 1.0

**Arg18: dRotateStiffZ**

Description: double value of rotate stiff z

Data Type: double

Default Value : 0.0

Syntax: dRotateStiffZ = 1.0

**Arg19: iLocalRotateStiffUnit**

Description: option for local rotate stiff unit

Data Type: integer

Default Value : 0

Syntax: iLocalRotateStiffUnit = 1

**Arg20: dDampCoef**

Description: double value of damper coefficient

Data Type: double

Default Value : 0.0

Syntax: dDampCoef = 1.0

**Arg21: dStressCoef**

Description: double value of stress coefficient

Data Type: double

Default Value : 0.0

Syntax: dStressCoef = 1.0

**Arg22: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg23: iTopRbeType**

Description: option for top rbe type

Data Type: integer

Default Value : 0

Syntax: iTopRbeType = 1

**Arg24: dTopPitch**

Description: double value of top pitch

Data Type: double

Default Value : 10

Syntax: dTopPitch = 1.0

**Arg25: dTopRemoveDepth**

Description: double value of top remove depth

Data Type: double

Default Value : 0.0

Syntax: dTopRemoveDepth = 1.0

**Arg26: iBotRbeType**

Description: option for bot rbe type

Data Type: integer

Default Value : 0

Syntax: iBotRbeType = 1

**Arg27: dBotPitch**

Description: double value of bot pitch

Data Type: double

Default Value : 10

Syntax: dBotPitch = 1.0

**Arg28: dBotRemoveDepth**

Description: double value of bot remove depth

Data Type: double

Default Value : 0.0

Syntax: dBotRemoveDepth = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.BoltConnections.Face.TypeC(crlFaceCur1=[], crlFaceCur2=[], strRbeName="RBE", dPlaneTol=20, dMaxBoltHeight=100, dMaxDiameter=0, dMinDiameter=0, iConnectionType=0, iCoincidentNodes=1, dTolerance=0.0, iGround=0, dStiffnessX=0.0, dStiffnessY=0.0, dStiffnessZ=0.0, iLocalStiffUnit=0, dRotateStiffX=0.0, dRotateStiffY=0.0, dRotateStiffZ=0.0, iLocalRotateStiffUnit=0, dDampCoef=0.0, dStressCoef=0.0, crCurCoord=None, iTopRbeType=0, dTopPitch=10, dTopRemoveDepth=0.0, iBotRbeType=0, dBotPitch=10, dBotRemoveDepth=0.0)

```

==========================================================

# Connections.BoltConnections.Face.TypeB

## Wrapper Macro

Lbc_Bolt_Modeling_Type_B_Face(...)

## Ribbon-GUI-Location

Connections > BoltConnections > Face > TypeB

## Command Description

Create Lbc TypeB Bolt Face method

## Argument List

**Arg1: crlFaceCur1**

Description: array entities in model with type face cur1

Data Type: cursor list

Default Value : []

Syntax: crlFaceCur1 = [EntityType(id1, id2, id3)]

**Arg2: crlFaceCur2**

Description: array entities in model with type face cur2

Data Type: cursor list

Default Value : []

Syntax: crlFaceCur2 = [EntityType(id1, id2, id3)]

**Arg3: strRbeName**

Description: definition string of input rbe name

Data Type: string

Default Value : "RBE"

Syntax: strRbeName = "string input"

**Arg4: strBarName**

Description: definition string of input bar name

Data Type: string

Default Value : ""

Syntax: strBarName = "string input"

**Arg5: iShaftType**

Description: option for shaft type

Data Type: integer

Default Value : 0

Syntax: iShaftType = 1

**Arg6: crCurBarProperty**

Description: entity in database model with type bar property

Data Type: cursor

Default Value : None

Syntax: crCurBarProperty = EntityType(id)

**Arg7: dPlaneTol**

Description: double value of plane tolerance

Data Type: double

Default Value : 20.0

Syntax: dPlaneTol = 1.0

**Arg8: dMaxBoltHeight**

Description: double value of maximize bolt height

Data Type: double

Default Value : 100.0

Syntax: dMaxBoltHeight = 1.0

**Arg9: dMaxDiameter**

Description: double value of maximize diameter

Data Type: double

Default Value : 0.0

Syntax: dMaxDiameter = 1.0

**Arg10: dMinDiameter**

Description: double value of minimize diameter

Data Type: double

Default Value : 0.0

Syntax: dMinDiameter = 1.0

**Arg11: bPretensionLoad**

Description: enable or disable feature pretension load

Data Type: bool

Default Value : False

Syntax: bPretensionLoad = True/False

**Arg12: iSolverType**

Description: option for solver type

Data Type: integer

Default Value : 0

Syntax: iSolverType = 1

**Arg13: dForceValue**

Description: double value of force value

Data Type: double

Default Value : 0.0

Syntax: dForceValue = 1.0

**Arg14: iPreTenDof**

Description: option for pre ten dof

Data Type: integer

Default Value : 0

Syntax: iPreTenDof = 1

**Arg15: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg16: iBoltFixLength**

Description: option for bolt fix length

Data Type: integer

Default Value : 0

Syntax: iBoltFixLength = 1

**Arg17: iTopSlot**

Description: option for top slot

Data Type: integer

Default Value : 0

Syntax: iTopSlot = 1

**Arg18: dRBE1**

Description: double value of r b e1

Data Type: double

Default Value : 0.0

Syntax: dRBE1 = 1.0

**Arg19: dRBE2**

Description: double value of r b e2

Data Type: double

Default Value : 0.0

Syntax: dRBE2 = 1.0

**Arg20: dBotDtDia**

Description: double value of bot dt dia

Data Type: double

Default Value : 0.0

Syntax: dBotDtDia = 1.0

**Arg21: dPitch**

Description: double value of pitch

Data Type: double

Default Value : 10.0

Syntax: dPitch = 1.0

**Arg22: iBotRbeConnType**

Description: option for bot rbe conn type

Data Type: integer

Default Value : 0

Syntax: iBotRbeConnType = 1

**Arg23: dScale1**

Description: double value of scale1

Data Type: double

Default Value : 1.10

Syntax: dScale1 = 1.0

**Arg24: bIsCreate2ADVCStaticProcessForFixLength**

Description: enable or disable feature is create2 advc static process for fix length

Data Type: bool

Default Value : False

Syntax: bIsCreate2ADVCStaticProcessForFixLength = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.BoltConnections.Face.TypeB(crlFaceCur1=[], crlFaceCur2=[], strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, dMaxDiameter=0.0, dMinDiameter=0.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, dRBE2=0.0, dBotDtDia=0.0, dPitch=10.0, iBotRbeConnType=0, dScale1=1.10, bIsCreate2ADVCStaticProcessForFixLength=False)

```

==========================================================

# Connections.BoltConnections.Face.TypeA

## Wrapper Macro

Lbc_Bolt_Modeling_Type_A_Face(...)

## Ribbon-GUI-Location

Connections > BoltConnections > Face > TypeA

## Command Description

## Argument List

**Arg1: crlFaceCur1**

Description: array entities in model with type face cur1

Data Type: cursor list

Default Value : []

Syntax: crlFaceCur1 = [EntityType(id1, id2, id3)]

**Arg2: crlFaceCur2**

Description: array entities in model with type face cur2

Data Type: cursor list

Default Value : []

Syntax: crlFaceCur2 = [EntityType(id1, id2, id3)]

**Arg3: strRbeName**

Description: definition string of input rbe name

Data Type: string

Default Value : "RBE"

Syntax: strRbeName = "string input"

**Arg4: strBarName**

Description: definition string of input bar name

Data Type: string

Default Value : ""

Syntax: strBarName = "string input"

**Arg5: iShaftType**

Description: option for shaft type

Data Type: integer

Default Value : 0

Syntax: iShaftType = 1

**Arg6: crCurBarProperty**

Description: entity in database model with type bar property

Data Type: cursor

Default Value : None

Syntax: crCurBarProperty = EntityType(id)

**Arg7: dPlaneTol**

Description: double value of plane tolerance

Data Type: double

Default Value : 20.0

Syntax: dPlaneTol = 1.0

**Arg8: dMaxBoltHeight**

Description: double value of maximize bolt height

Data Type: double

Default Value : 100.0

Syntax: dMaxBoltHeight = 1.0

**Arg9: dMaxDiameter**

Description: double value of maximize diameter

Data Type: double

Default Value : 0.0

Syntax: dMaxDiameter = 1.0

**Arg10: dMinDiameter**

Description: double value of minimize diameter

Data Type: double

Default Value : 0.0

Syntax: dMinDiameter = 1.0

**Arg11: bPretensionLoad**

Description: enable or disable feature pretension load

Data Type: bool

Default Value : False

Syntax: bPretensionLoad = True/False

**Arg12: iSolverType**

Description: option for solver type

Data Type: integer

Default Value : 0

Syntax: iSolverType = 1

**Arg13: dForceValue**

Description: double value of force value

Data Type: double

Default Value : 0.0

Syntax: dForceValue = 1.0

**Arg14: iPreTenDof**

Description: option for pre ten dof

Data Type: integer

Default Value : 0

Syntax: iPreTenDof = 1

**Arg15: crCurCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCurCoord = EntityType(id)

**Arg16: iBoltFixLength**

Description: option for bolt fix length

Data Type: integer

Default Value : 0

Syntax: iBoltFixLength = 1

**Arg17: iTopSlot**

Description: option for top slot

Data Type: integer

Default Value : 0

Syntax: iTopSlot = 1

**Arg18: dRBE1**

Description: double value of r b e1

Data Type: double

Default Value : 0.0

Syntax: dRBE1 = 1.0

**Arg19: iBotSlot**

Description: option for bot slot

Data Type: integer

Default Value : 0

Syntax: iBotSlot = 1

**Arg20: dRBE2**

Description: double value of r b e2

Data Type: double

Default Value : 0.0

Syntax: dRBE2 = 1.0

**Arg21: dScale1**

Description: double value of scale1

Data Type: double

Default Value : 1.10

Syntax: dScale1 = 1.0

**Arg22: bIfCreate2ADVCStaticProcessForBoltFixLength**

Description: enable or disable feature if create2 advc static process for bolt fix length

Data Type: bool

Default Value : False

Syntax: bIfCreate2ADVCStaticProcessForBoltFixLength = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.BoltConnections.Face.TypeA(crlFaceCur1=[], crlFaceCur2=[], strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, dMaxDiameter=0.0, dMinDiameter=0.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, iBotSlot=0, dRBE2=0.0, dScale1=1.10, bIfCreate2ADVCStaticProcessForBoltFixLength=False)

```

==========================================================

# Connections.Contacts.Abaqus.ContactTable

## Wrapper Macro

ContactTableAbaqus(...)

## Ribbon-GUI-Location

Connections > Contacts > Abaqus > ContactTable

## Command Description

Create LBC contact abaqus manual face

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iContactMethod**

Description: option for contact method

Data Type: integer

Default Value : 0

Syntax: iContactMethod = 1

**Arg3: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg4: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg5: dAdjustVal**

Description: double value of adjust val

Data Type: double

Default Value : 0.0

Syntax: dAdjustVal = 1.0

**Arg6: dExtensionZone**

Description: double value of extension zone

Data Type: double

Default Value : 0.0

Syntax: dExtensionZone = 1.0

**Arg7: dMaxPenetration**

Description: double value of maximize penetration

Data Type: double

Default Value : 0.0

Syntax: dMaxPenetration = 1.0

**Arg8: iSmallSliding**

Description: option for small sliding

Data Type: integer

Default Value : 0

Syntax: iSmallSliding = 1

**Arg9: dSmooth**

Description: double value of smooth

Data Type: double

Default Value : 0.0

Syntax: dSmooth = 1.0

**Arg10: iFrictionType**

Description: option for friction type

Data Type: integer

Default Value : 0

Syntax: iFrictionType = 1

**Arg11: dFrictionCoef1**

Description: double value of friction coef1

Data Type: double

Default Value : 0.0

Syntax: dFrictionCoef1 = 1.0

**Arg12: dFrictionCoef2**

Description: double value of friction coef2

Data Type: double

Default Value : 0.0

Syntax: dFrictionCoef2 = 1.0

**Arg13: dShearLimit**

Description: double value of shear limit

Data Type: double

Default Value : 0.0

Syntax: dShearLimit = 1.0

**Arg14: dSlipTol**

Description: double value of slip tolerance

Data Type: double

Default Value : 0.0

Syntax: dSlipTol = 1.0

**Arg15: dStaticFrictionCoef**

Description: double value of static friction coefficient

Data Type: double

Default Value : 0.0

Syntax: dStaticFrictionCoef = 1.0

**Arg16: dKineticFrictionCoef**

Description: double value of kinetic friction coefficient

Data Type: double

Default Value : 0.0

Syntax: dKineticFrictionCoef = 1.0

**Arg17: dDecayCoef**

Description: double value of decay coefficient

Data Type: double

Default Value : 0.0

Syntax: dDecayCoef = 1.0

**Arg18: iAdjust**

Description: option for adjust

Data Type: integer

Default Value : 0

Syntax: iAdjust = 1

**Arg19: dPositonTol**

Description: double value of positon tolerance

Data Type: double

Default Value : 0.0

Syntax: dPositonTol = 1.0

**Arg20: iFormula**

Description: option for formula

Data Type: integer

Default Value : 0

Syntax: iFormula = 1

**Arg21: iTie**

Description: option for tie

Data Type: integer

Default Value : 0

Syntax: iTie = 1

**Arg22: iPOCType**

Description: option for p o c type

Data Type: integer

Default Value : 0

Syntax: iPOCType = 1

**Arg23: iAllowSeparation**

Description: option for allow separation

Data Type: integer

Default Value : 0

Syntax: iAllowSeparation = 1

**Arg24: dSlope**

Description: double value of slope

Data Type: double

Default Value : 0.0

Syntax: dSlope = 1.0

**Arg25: tshPOCTsheet**

Description: field data (table) of p o c tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshPOCTsheet = [Value1, Value1]

**Arg26: iClearanceType**

Description: option for clearance type

Data Type: integer

Default Value : 0

Syntax: iClearanceType = 1

**Arg27: iClearanceTypeId**

Description: option for clearance type id

Data Type: integer

Default Value : 0

Syntax: iClearanceTypeId = 1

**Arg28: bTemperatureDependency**

Description: enable or disable feature temperature dependency

Data Type: bool

Default Value : False

Syntax: bTemperatureDependency = True/False

**Arg29: iDependencies**

Description: option for dependencies

Data Type: integer

Default Value : 0

Syntax: iDependencies = 1

**Arg30: tshCDTsheet**

Description: field data (table) of CD tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshCDTsheet = [Value1, Value1]

**Arg31: iPrsTypeId**

Description: option for prs type id

Data Type: integer

Default Value : 0

Syntax: iPrsTypeId = 1

**Arg32: bPrsTemperatureDependency**

Description: enable or disable feature prs temperature dependency

Data Type: bool

Default Value : False

Syntax: bPrsTemperatureDependency = True/False

**Arg33: iPrsDependencies**

Description: option for prs dependencies

Data Type: integer

Default Value : 0

Syntax: iPrsDependencies = 1

**Arg34: tshPrsDTsheet**

Description: field data (table) of prs d tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshPrsDTsheet = [Value1, Value1]

**Arg35: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg36: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg37: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.Abaqus.ContactTable(strName="", iContactMethod=0, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)

```

==========================================================

# Connections.Contacts.Abaqus.ManualGroup

## Wrapper Macro

ContactAbaqus_ManualGroup(...)

## Ribbon-GUI-Location

Connections > Contacts > Abaqus > ManualGroup

## Command Description

Create LBC contact abaqus manual group

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iContactMethod**

Description: option for contact method

Data Type: integer

Default Value : 1

Syntax: iContactMethod = 1

**Arg3: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg4: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg5: dAdjustVal**

Description: double value of adjust val

Data Type: double

Default Value : 0.0

Syntax: dAdjustVal = 1.0

**Arg6: dExtensionZone**

Description: double value of extension zone

Data Type: double

Default Value : 0.0

Syntax: dExtensionZone = 1.0

**Arg7: dMaxPenetration**

Description: double value of maximize penetration

Data Type: double

Default Value : 0.0

Syntax: dMaxPenetration = 1.0

**Arg8: iSmallSliding**

Description: option for small sliding

Data Type: integer

Default Value : 0

Syntax: iSmallSliding = 1

**Arg9: dSmooth**

Description: double value of smooth

Data Type: double

Default Value : 0.0

Syntax: dSmooth = 1.0

**Arg10: iFrictionType**

Description: option for friction type

Data Type: integer

Default Value : 0

Syntax: iFrictionType = 1

**Arg11: dFrictionCoef1**

Description: double value of friction coef1

Data Type: double

Default Value : 0.0

Syntax: dFrictionCoef1 = 1.0

**Arg12: dFrictionCoef2**

Description: double value of friction coef2

Data Type: double

Default Value : 0.0

Syntax: dFrictionCoef2 = 1.0

**Arg13: dShearLimit**

Description: double value of shear limit

Data Type: double

Default Value : 0.0

Syntax: dShearLimit = 1.0

**Arg14: dSlipTol**

Description: double value of slip tolerance

Data Type: double

Default Value : 0.0

Syntax: dSlipTol = 1.0

**Arg15: dStaticFrictionCoef**

Description: double value of static friction coefficient

Data Type: double

Default Value : 0.0

Syntax: dStaticFrictionCoef = 1.0

**Arg16: dKineticFrictionCoef**

Description: double value of kinetic friction coefficient

Data Type: double

Default Value : 0.0

Syntax: dKineticFrictionCoef = 1.0

**Arg17: dDecayCoef**

Description: double value of decay coefficient

Data Type: double

Default Value : 0.0

Syntax: dDecayCoef = 1.0

**Arg18: iAdjust**

Description: option for adjust

Data Type: integer

Default Value : 0

Syntax: iAdjust = 1

**Arg19: dPositonTol**

Description: double value of positon tolerance

Data Type: double

Default Value : 0.0

Syntax: dPositonTol = 1.0

**Arg20: iFormula**

Description: option for formula

Data Type: integer

Default Value : 0

Syntax: iFormula = 1

**Arg21: iTie**

Description: option for tie

Data Type: integer

Default Value : 0

Syntax: iTie = 1

**Arg22: iPOCType**

Description: option for p o c type

Data Type: integer

Default Value : 0

Syntax: iPOCType = 1

**Arg23: iAllowSeparation**

Description: option for allow separation

Data Type: integer

Default Value : 0

Syntax: iAllowSeparation = 1

**Arg24: dSlope**

Description: double value of slope

Data Type: double

Default Value : 0.0

Syntax: dSlope = 1.0

**Arg25: tshPOCTsheet**

Description: field data (table) of p o c tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshPOCTsheet = [Value1, Value1]

**Arg26: iClearanceType**

Description: option for clearance type

Data Type: integer

Default Value : 0

Syntax: iClearanceType = 1

**Arg27: iClearanceTypeId**

Description: option for clearance type id

Data Type: integer

Default Value : 0

Syntax: iClearanceTypeId = 1

**Arg28: bTemperatureDependency**

Description: enable or disable feature temperature dependency

Data Type: bool

Default Value : False

Syntax: bTemperatureDependency = True/False

**Arg29: iDependencies**

Description: option for dependencies

Data Type: integer

Default Value : 0

Syntax: iDependencies = 1

**Arg30: tshCDTsheet**

Description: field data (table) of CD tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshCDTsheet = [Value1, Value1]

**Arg31: iPrsTypeId**

Description: option for prs type id

Data Type: integer

Default Value : 0

Syntax: iPrsTypeId = 1

**Arg32: bPrsTemperatureDependency**

Description: enable or disable feature prs temperature dependency

Data Type: bool

Default Value : False

Syntax: bPrsTemperatureDependency = True/False

**Arg33: iPrsDependencies**

Description: option for prs dependencies

Data Type: integer

Default Value : 0

Syntax: iPrsDependencies = 1

**Arg34: tshPrsDTsheet**

Description: field data (table) of prs d tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshPrsDTsheet = [Value1, Value1]

**Arg35: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg36: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg37: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.Abaqus.ManualGroup(strName="", iContactMethod=1, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)

```

==========================================================

# Connections.Contacts.Abaqus.ManualFace

## Wrapper Macro

ContactAbaqus_ManualFace(...)

## Ribbon-GUI-Location

Connections > Contacts > Abaqus > ManualFace

## Command Description

Create LBC contact abaqus manual face

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iContactMethod**

Description: option for contact method

Data Type: integer

Default Value : 0

Syntax: iContactMethod = 1

**Arg3: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg4: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg5: dAdjustVal**

Description: double value of adjust val

Data Type: double

Default Value : 0.0

Syntax: dAdjustVal = 1.0

**Arg6: dExtensionZone**

Description: double value of extension zone

Data Type: double

Default Value : 0.0

Syntax: dExtensionZone = 1.0

**Arg7: dMaxPenetration**

Description: double value of maximize penetration

Data Type: double

Default Value : 0.0

Syntax: dMaxPenetration = 1.0

**Arg8: iSmallSliding**

Description: option for small sliding

Data Type: integer

Default Value : 0

Syntax: iSmallSliding = 1

**Arg9: dSmooth**

Description: double value of smooth

Data Type: double

Default Value : 0.0

Syntax: dSmooth = 1.0

**Arg10: iFrictionType**

Description: option for friction type

Data Type: integer

Default Value : 0

Syntax: iFrictionType = 1

**Arg11: dFrictionCoef1**

Description: double value of friction coef1

Data Type: double

Default Value : 0.0

Syntax: dFrictionCoef1 = 1.0

**Arg12: dFrictionCoef2**

Description: double value of friction coef2

Data Type: double

Default Value : 0.0

Syntax: dFrictionCoef2 = 1.0

**Arg13: dShearLimit**

Description: double value of shear limit

Data Type: double

Default Value : 0.0

Syntax: dShearLimit = 1.0

**Arg14: dSlipTol**

Description: double value of slip tolerance

Data Type: double

Default Value : 0.0

Syntax: dSlipTol = 1.0

**Arg15: dStaticFrictionCoef**

Description: double value of static friction coefficient

Data Type: double

Default Value : 0.0

Syntax: dStaticFrictionCoef = 1.0

**Arg16: dKineticFrictionCoef**

Description: double value of kinetic friction coefficient

Data Type: double

Default Value : 0.0

Syntax: dKineticFrictionCoef = 1.0

**Arg17: dDecayCoef**

Description: double value of decay coefficient

Data Type: double

Default Value : 0.0

Syntax: dDecayCoef = 1.0

**Arg18: iAdjust**

Description: option for adjust

Data Type: integer

Default Value : 0

Syntax: iAdjust = 1

**Arg19: dPositonTol**

Description: double value of positon tolerance

Data Type: double

Default Value : 0.0

Syntax: dPositonTol = 1.0

**Arg20: iFormula**

Description: option for formula

Data Type: integer

Default Value : 0

Syntax: iFormula = 1

**Arg21: iTie**

Description: option for tie

Data Type: integer

Default Value : 0

Syntax: iTie = 1

**Arg22: iPOCType**

Description: option for p o c type

Data Type: integer

Default Value : 0

Syntax: iPOCType = 1

**Arg23: iAllowSeparation**

Description: option for allow separation

Data Type: integer

Default Value : 0

Syntax: iAllowSeparation = 1

**Arg24: dSlope**

Description: double value of slope

Data Type: double

Default Value : 0.0

Syntax: dSlope = 1.0

**Arg25: tshPOCTsheet**

Description: field data (table) of p o c tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshPOCTsheet = [Value1, Value1]

**Arg26: iClearanceType**

Description: option for clearance type

Data Type: integer

Default Value : 0

Syntax: iClearanceType = 1

**Arg27: iClearanceTypeId**

Description: option for clearance type id

Data Type: integer

Default Value : 0

Syntax: iClearanceTypeId = 1

**Arg28: bTemperatureDependency**

Description: enable or disable feature temperature dependency

Data Type: bool

Default Value : False

Syntax: bTemperatureDependency = True/False

**Arg29: iDependencies**

Description: option for dependencies

Data Type: integer

Default Value : 0

Syntax: iDependencies = 1

**Arg30: tshCDTsheet**

Description: field data (table) of CD tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshCDTsheet = [Value1, Value1]

**Arg31: iPrsTypeId**

Description: option for prs type id

Data Type: integer

Default Value : 0

Syntax: iPrsTypeId = 1

**Arg32: bPrsTemperatureDependency**

Description: enable or disable feature prs temperature dependency

Data Type: bool

Default Value : False

Syntax: bPrsTemperatureDependency = True/False

**Arg33: iPrsDependencies**

Description: option for prs dependencies

Data Type: integer

Default Value : 0

Syntax: iPrsDependencies = 1

**Arg34: tshPrsDTsheet**

Description: field data (table) of prs d tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshPrsDTsheet = [Value1, Value1]

**Arg35: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg36: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg37: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.Abaqus.ManualFace(strName="", iContactMethod=0, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)

```

==========================================================

# Connections.Contacts.Abaqus.ContactGroupByMatrix

## Wrapper Macro

ContactAbaqus_GroupByMatrix(...)

## Ribbon-GUI-Location

Connections > Contacts > Abaqus > ContactGroupByMatrix

## Command Description

Create LBC contact abaqus group by matrix

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iContactMethod**

Description: option for contact method

Data Type: integer

Default Value : 1

Syntax: iContactMethod = 1

**Arg3: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg4: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg5: dAdjustVal**

Description: double value of adjust val

Data Type: double

Default Value : 0.0

Syntax: dAdjustVal = 1.0

**Arg6: dExtensionZone**

Description: double value of extension zone

Data Type: double

Default Value : 0.0

Syntax: dExtensionZone = 1.0

**Arg7: dMaxPenetration**

Description: double value of maximize penetration

Data Type: double

Default Value : 0.0

Syntax: dMaxPenetration = 1.0

**Arg8: iSmallSliding**

Description: option for small sliding

Data Type: integer

Default Value : 0

Syntax: iSmallSliding = 1

**Arg9: dSmooth**

Description: double value of smooth

Data Type: double

Default Value : 0.0

Syntax: dSmooth = 1.0

**Arg10: iFrictionType**

Description: option for friction type

Data Type: integer

Default Value : 0

Syntax: iFrictionType = 1

**Arg11: dFrictionCoef1**

Description: double value of friction coef1

Data Type: double

Default Value : 0.0

Syntax: dFrictionCoef1 = 1.0

**Arg12: dFrictionCoef2**

Description: double value of friction coef2

Data Type: double

Default Value : 0.0

Syntax: dFrictionCoef2 = 1.0

**Arg13: dShearLimit**

Description: double value of shear limit

Data Type: double

Default Value : 0.0

Syntax: dShearLimit = 1.0

**Arg14: dSlipTol**

Description: double value of slip tolerance

Data Type: double

Default Value : 0.0

Syntax: dSlipTol = 1.0

**Arg15: dStaticFrictionCoef**

Description: double value of static friction coefficient

Data Type: double

Default Value : 0.0

Syntax: dStaticFrictionCoef = 1.0

**Arg16: dKineticFrictionCoef**

Description: double value of kinetic friction coefficient

Data Type: double

Default Value : 0.0

Syntax: dKineticFrictionCoef = 1.0

**Arg17: dDecayCoef**

Description: double value of decay coefficient

Data Type: double

Default Value : 0.0

Syntax: dDecayCoef = 1.0

**Arg18: iAdjust**

Description: option for adjust

Data Type: integer

Default Value : 0

Syntax: iAdjust = 1

**Arg19: dPositonTol**

Description: double value of positon tolerance

Data Type: double

Default Value : 0.0

Syntax: dPositonTol = 1.0

**Arg20: iFormula**

Description: option for formula

Data Type: integer

Default Value : 0

Syntax: iFormula = 1

**Arg21: iTie**

Description: option for tie

Data Type: integer

Default Value : 0

Syntax: iTie = 1

**Arg22: iPOCType**

Description: option for p o c type

Data Type: integer

Default Value : 0

Syntax: iPOCType = 1

**Arg23: iAllowSeparation**

Description: option for allow separation

Data Type: integer

Default Value : 0

Syntax: iAllowSeparation = 1

**Arg24: dSlope**

Description: double value of slope

Data Type: double

Default Value : 0.0

Syntax: dSlope = 1.0

**Arg25: tshPOCTsheet**

Description: field data (table) of p o c tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshPOCTsheet = [Value1, Value1]

**Arg26: iClearanceType**

Description: option for clearance type

Data Type: integer

Default Value : 0

Syntax: iClearanceType = 1

**Arg27: iClearanceTypeId**

Description: option for clearance type id

Data Type: integer

Default Value : 0

Syntax: iClearanceTypeId = 1

**Arg28: bTemperatureDependency**

Description: enable or disable feature temperature dependency

Data Type: bool

Default Value : False

Syntax: bTemperatureDependency = True/False

**Arg29: iDependencies**

Description: option for dependencies

Data Type: integer

Default Value : 0

Syntax: iDependencies = 1

**Arg30: tshCDTsheet**

Description: field data (table) of CD tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshCDTsheet = [Value1, Value1]

**Arg31: iPrsTypeId**

Description: option for prs type id

Data Type: integer

Default Value : 0

Syntax: iPrsTypeId = 1

**Arg32: bPrsTemperatureDependency**

Description: enable or disable feature prs temperature dependency

Data Type: bool

Default Value : False

Syntax: bPrsTemperatureDependency = True/False

**Arg33: iPrsDependencies**

Description: option for prs dependencies

Data Type: integer

Default Value : 0

Syntax: iPrsDependencies = 1

**Arg34: tshPrsDTsheet**

Description: field data (table) of prs d tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshPrsDTsheet = [Value1, Value1]

**Arg35: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg36: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg37: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.Abaqus.ContactGroupByMatrix(strName="", iContactMethod=1, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)

```

==========================================================

# Connections.Contacts.Abaqus.ContactShareFace

## Wrapper Macro

ContactAbaqus_ShareFace(...)

## Ribbon-GUI-Location

Connections > Contacts > Abaqus > ContactShareFace

## Command Description

Create LBC contact abaqus manual group

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iContactMethod**

Description: option for contact method

Data Type: integer

Default Value : 3

Syntax: iContactMethod = 1

**Arg3: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg4: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg5: dAdjustVal**

Description: double value of adjust val

Data Type: double

Default Value : 0.0

Syntax: dAdjustVal = 1.0

**Arg6: dExtensionZone**

Description: double value of extension zone

Data Type: double

Default Value : 0.0

Syntax: dExtensionZone = 1.0

**Arg7: dMaxPenetration**

Description: double value of maximize penetration

Data Type: double

Default Value : 0.0

Syntax: dMaxPenetration = 1.0

**Arg8: iSmallSliding**

Description: option for small sliding

Data Type: integer

Default Value : 0

Syntax: iSmallSliding = 1

**Arg9: dSmooth**

Description: double value of smooth

Data Type: double

Default Value : 0.0

Syntax: dSmooth = 1.0

**Arg10: iFrictionType**

Description: option for friction type

Data Type: integer

Default Value : 0

Syntax: iFrictionType = 1

**Arg11: dFrictionCoef1**

Description: double value of friction coef1

Data Type: double

Default Value : 0.0

Syntax: dFrictionCoef1 = 1.0

**Arg12: dFrictionCoef2**

Description: double value of friction coef2

Data Type: double

Default Value : 0.0

Syntax: dFrictionCoef2 = 1.0

**Arg13: dShearLimit**

Description: double value of shear limit

Data Type: double

Default Value : 0.0

Syntax: dShearLimit = 1.0

**Arg14: dSlipTol**

Description: double value of slip tolerance

Data Type: double

Default Value : 0.0

Syntax: dSlipTol = 1.0

**Arg15: dStaticFrictionCoef**

Description: double value of static friction coefficient

Data Type: double

Default Value : 0.0

Syntax: dStaticFrictionCoef = 1.0

**Arg16: dKineticFrictionCoef**

Description: double value of kinetic friction coefficient

Data Type: double

Default Value : 0.0

Syntax: dKineticFrictionCoef = 1.0

**Arg17: dDecayCoef**

Description: double value of decay coefficient

Data Type: double

Default Value : 0.0

Syntax: dDecayCoef = 1.0

**Arg18: iAdjust**

Description: option for adjust

Data Type: integer

Default Value : 0

Syntax: iAdjust = 1

**Arg19: dPositonTol**

Description: double value of positon tolerance

Data Type: double

Default Value : 0.0

Syntax: dPositonTol = 1.0

**Arg20: iFormula**

Description: option for formula

Data Type: integer

Default Value : 0

Syntax: iFormula = 1

**Arg21: iTie**

Description: option for tie

Data Type: integer

Default Value : 0

Syntax: iTie = 1

**Arg22: iPOCType**

Description: option for p o c type

Data Type: integer

Default Value : 0

Syntax: iPOCType = 1

**Arg23: iAllowSeparation**

Description: option for allow separation

Data Type: integer

Default Value : 0

Syntax: iAllowSeparation = 1

**Arg24: dSlope**

Description: double value of slope

Data Type: double

Default Value : 0.0

Syntax: dSlope = 1.0

**Arg25: tshPOCTsheet**

Description: field data (table) of p o c tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshPOCTsheet = [Value1, Value1]

**Arg26: iClearanceType**

Description: option for clearance type

Data Type: integer

Default Value : 0

Syntax: iClearanceType = 1

**Arg27: iClearanceTypeId**

Description: option for clearance type id

Data Type: integer

Default Value : 0

Syntax: iClearanceTypeId = 1

**Arg28: bTemperatureDependency**

Description: enable or disable feature temperature dependency

Data Type: bool

Default Value : False

Syntax: bTemperatureDependency = True/False

**Arg29: iDependencies**

Description: option for dependencies

Data Type: integer

Default Value : 0

Syntax: iDependencies = 1

**Arg30: tshCDTsheet**

Description: field data (table) of CD tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshCDTsheet = [Value1, Value1]

**Arg31: iPrsTypeId**

Description: option for prs type id

Data Type: integer

Default Value : 0

Syntax: iPrsTypeId = 1

**Arg32: bPrsTemperatureDependency**

Description: enable or disable feature prs temperature dependency

Data Type: bool

Default Value : False

Syntax: bPrsTemperatureDependency = True/False

**Arg33: iPrsDependencies**

Description: option for prs dependencies

Data Type: integer

Default Value : 0

Syntax: iPrsDependencies = 1

**Arg34: tshPrsDTsheet**

Description: field data (table) of prs d tsheet

Data Type: TSheetd

Default Value : []

Syntax: tshPrsDTsheet = [Value1, Value1]

**Arg35: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg36: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg37: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.Abaqus.ContactShareFace(strName="", iContactMethod=3, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0)

```

==========================================================

# Connections.Contacts.ADVC.ContactClearance

## Wrapper Macro

ContactClearance(...)

## Ribbon-GUI-Location

Connections > Contacts > ADVC > ContactClearance

## Command Description

contact clearance for ADVC contact

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: dClearanceVal**

Description: double value of clearance val

Data Type: double

Default Value : 0.0

Syntax: dClearanceVal = 1.0

**Arg3: iLocalUnit**

Description: option for local unit

Data Type: integer

Default Value : 0

Syntax: iLocalUnit = 1

**Arg4: iSolverType**

Description: option for solver type

Data Type: integer

Default Value : 0

Syntax: iSolverType = 1

**Arg5: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg6: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.ADVC.ContactClearance(strName="", dClearanceVal=0.0, iLocalUnit=0, iSolverType=0, crlTarget=[], crEdit=None)

```

==========================================================

# Connections.Contacts.ADVC.ManualGroup

## Wrapper Macro

ContactADVC(...)

## Ribbon-GUI-Location

Connections > Contacts > ADVC > ManualGroup

## Command Description

create ADVC contact Manual Group

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactADVC"

Syntax: strName = "string input"

**Arg2: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg3: iSlidingType**

Description: option for sliding type

Data Type: integer

Default Value : 0

Syntax: iSlidingType = 1

**Arg4: iInitialState**

Description: option for initial state

Data Type: integer

Default Value : 0

Syntax: iInitialState = 1

**Arg5: dInitialStateTol**

Description: double value of initial state tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dInitialStateTol = 1.0

**Arg6: dKineticFrictionCoef**

Description: double value of kinetic friction coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dKineticFrictionCoef = 1.0

**Arg7: dExponentialCoef**

Description: double value of exponential coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dExponentialCoef = 1.0

**Arg8: iBehavior**

Description: option for behavior

Data Type: integer

Default Value : 0

Syntax: iBehavior = 1

**Arg9: dClearance**

Description: double value of clearance

Data Type: double

Default Value : DFLT_DBL

Syntax: dClearance = 1.0

**Arg10: iAdjust2Clearance**

Description: option for adjust2 clearance

Data Type: integer

Default Value : 0

Syntax: iAdjust2Clearance = 1

**Arg11: dInterference**

Description: double value of interference

Data Type: double

Default Value : DFLT_DBL

Syntax: dInterference = 1.0

**Arg12: iAdjust2Interference**

Description: option for adjust2 interference

Data Type: integer

Default Value : 0

Syntax: iAdjust2Interference = 1

**Arg13: iAutoShrink**

Description: option for auto shrink

Data Type: integer

Default Value : 0

Syntax: iAutoShrink = 1

**Arg14: iAdvAdjust**

Description: option for advc adjust

Data Type: integer

Default Value : 0

Syntax: iAdvAdjust = 1

**Arg15: dAdjustValue**

Description: double value of adjust value

Data Type: double

Default Value : DFLT_DBL

Syntax: dAdjustValue = 1.0

**Arg16: dFrictionCoef**

Description: double value of friction coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dFrictionCoef = 1.0

**Arg17: dMaxShear**

Description: double value of maximize shear

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxShear = 1.0

**Arg18: dElasticSlip**

Description: double value of elastic slip

Data Type: double

Default Value : DFLT_DBL

Syntax: dElasticSlip = 1.0

**Arg19: dSlipTolerance**

Description: double value of slip tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dSlipTolerance = 1.0

**Arg20: dSearchWidth**

Description: double value of search width

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchWidth = 1.0

**Arg21: dSearchGap**

Description: double value of search gap

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchGap = 1.0

**Arg22: dSearchDepth**

Description: double value of search depth

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchDepth = 1.0

**Arg23: dCritialPenetration**

Description: double value of critial penetration

Data Type: double

Default Value : DFLT_DBL

Syntax: dCritialPenetration = 1.0

**Arg24: iEstimationImpactTime**

Description: option for estimation impact time

Data Type: integer

Default Value : 0

Syntax: iEstimationImpactTime = 1

**Arg25: iFormula**

Description: option for formula

Data Type: integer

Default Value : 0

Syntax: iFormula = 1

**Arg26: iConstraintType**

Description: option for constraint type

Data Type: integer

Default Value : 0

Syntax: iConstraintType = 1

**Arg27: iDataType**

Description: option for data type

Data Type: integer

Default Value : 0

Syntax: iDataType = 1

**Arg28: iTypeId**

Description: option for type id

Data Type: integer

Default Value : 0

Syntax: iTypeId = 1

**Arg29: bTemperatureDependency**

Description: enable or disable feature temperature dependency

Data Type: bool

Default Value : False

Syntax: bTemperatureDependency = True/False

**Arg30: iNumDependencies**

Description: option for number dependencies

Data Type: integer

Default Value : 0

Syntax: iNumDependencies = 1

**Arg31: tshTableClearance**

Description: field data (table) of table clearance

Data Type: TSheetd

Default Value : []

Syntax: tshTableClearance = [Value1, Value1]

**Arg32: bStabilized**

Description: enable or disable feature stabilized

Data Type: bool

Default Value : 0

Syntax: bStabilized = True/False

**Arg33: iStabilizeType**

Description: option for stabilize type

Data Type: integer

Default Value : 0

Syntax: iStabilizeType = 1

**Arg34: dResidualFactor**

Description: double value of residual factor

Data Type: double

Default Value : DFLT_DBL

Syntax: dResidualFactor = 1.0

**Arg35: dEffectiveDist**

Description: double value of effective distance

Data Type: double

Default Value : DFLT_DBL

Syntax: dEffectiveDist = 1.0

**Arg36: dCN**

Description: double value of normal factor Cn

Data Type: double

Default Value : DFLT_DBL

Syntax: dCN = 1.0

**Arg37: dCT**

Description: double value of normal factor Ct

Data Type: double

Default Value : DFLT_DBL

Syntax: dCT = 1.0

**Arg38: crlClearance**

Description: array entities in model with type clearance

Data Type: cursor list

Default Value : []

Syntax: crlClearance = [EntityType(id1, id2, id3)]

**Arg39: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg40: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg41: dSearchAngle**

Description: double value of search angle

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchAngle = 1.0

**Arg42: iConstraintTypeExplicit**

Description: option for constraint type explicit

Data Type: integer

Default Value : 0

Syntax: iConstraintTypeExplicit = 1

**Arg43: dPenaltyFact**

Description: double value of penalty fact

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyFact = 1.0

**Arg44: dPenaltyFactExplicit**

Description: double value of penalty fact explicit

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyFactExplicit = 1.0

**Arg45: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

**Arg46: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg47: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.ADVC.ManualGroup(strName="ContactADVC", iContactType=0, iSlidingType=0, iInitialState=0, dInitialStateTol=DFLT_DBL, dKineticFrictionCoef=DFLT_DBL, dExponentialCoef=DFLT_DBL, iBehavior=0, dClearance=DFLT_DBL, iAdjust2Clearance=0, dInterference=DFLT_DBL, iAdjust2Interference=0, iAutoShrink=0, iAdvAdjust=0, dAdjustValue=DFLT_DBL, dFrictionCoef=DFLT_DBL, dMaxShear=DFLT_DBL, dElasticSlip=DFLT_DBL, dSlipTolerance=DFLT_DBL, dSearchWidth=DFLT_DBL, dSearchGap=DFLT_DBL, dSearchDepth=DFLT_DBL, dCritialPenetration=DFLT_DBL, iEstimationImpactTime=0, iFormula=0, iConstraintType=0, iDataType=0, iTypeId=0, bTemperatureDependency=False, iNumDependencies=0, tshTableClearance=[], bStabilized=0, iStabilizeType=0, dResidualFactor=DFLT_DBL, dEffectiveDist=DFLT_DBL, dCN=DFLT_DBL, dCT=DFLT_DBL, crlClearance=[], crplTarget=[], crEdit=None, dSearchAngle=DFLT_DBL, iConstraintTypeExplicit=0, dPenaltyFact=DFLT_DBL, dPenaltyFactExplicit=DFLT_DBL, iColor=16711680, iAlg=0, iMethod=0)

```

==========================================================

# Connections.Contacts.ADVC.ManualFace

## Wrapper Macro

ContactManualFaceADVC(...)

## Ribbon-GUI-Location

Connections > Contacts > ADVC > ManualFace

## Command Description

create ADVC contact by manual face

## Argument List

**Arg1: crlFaceMaster**

Description: array entities in model with type face master

Data Type: cursor list

Default Value : []

Syntax: crlFaceMaster = [EntityType(id1, id2, id3)]

**Arg2: crlFaceSlave**

Description: array entities in model with type face slave

Data Type: cursor list

Default Value : []

Syntax: crlFaceSlave = [EntityType(id1, id2, id3)]

**Arg3: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactADVC"

Syntax: strName = "string input"

**Arg4: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg5: iSlidingType**

Description: option for sliding type

Data Type: integer

Default Value : 0

Syntax: iSlidingType = 1

**Arg6: iInitialState**

Description: option for initial state

Data Type: integer

Default Value : 0

Syntax: iInitialState = 1

**Arg7: dInitialStateTol**

Description: double value of initial state tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dInitialStateTol = 1.0

**Arg8: dKineticFrictionCoef**

Description: double value of kinetic friction coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dKineticFrictionCoef = 1.0

**Arg9: dExponentialCoef**

Description: double value of exponential coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dExponentialCoef = 1.0

**Arg10: iBehavior**

Description: option for behavior

Data Type: integer

Default Value : 0

Syntax: iBehavior = 1

**Arg11: dClearance**

Description: double value of clearance

Data Type: double

Default Value : DFLT_DBL

Syntax: dClearance = 1.0

**Arg12: iAdjust2Clearance**

Description: option for adjust2 clearance

Data Type: integer

Default Value : 0

Syntax: iAdjust2Clearance = 1

**Arg13: dInterference**

Description: double value of interference

Data Type: double

Default Value : DFLT_DBL

Syntax: dInterference = 1.0

**Arg14: iAdjust2Interference**

Description: option for adjust2 interference

Data Type: integer

Default Value : 0

Syntax: iAdjust2Interference = 1

**Arg15: iAutoShrink**

Description: option for auto shrink

Data Type: integer

Default Value : 0

Syntax: iAutoShrink = 1

**Arg16: iAdvAdjust**

Description: option for advc adjust

Data Type: integer

Default Value : 0

Syntax: iAdvAdjust = 1

**Arg17: dAdjustValue**

Description: double value of adjust value

Data Type: double

Default Value : DFLT_DBL

Syntax: dAdjustValue = 1.0

**Arg18: dFrictionCoef**

Description: double value of friction coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dFrictionCoef = 1.0

**Arg19: dMaxShear**

Description: double value of maximize shear

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxShear = 1.0

**Arg20: dElasticSlip**

Description: double value of elastic slip

Data Type: double

Default Value : DFLT_DBL

Syntax: dElasticSlip = 1.0

**Arg21: dSlipTolerance**

Description: double value of slip tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dSlipTolerance = 1.0

**Arg22: dSearchWidth**

Description: double value of search width

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchWidth = 1.0

**Arg23: dSearchGap**

Description: double value of search gap

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchGap = 1.0

**Arg24: dSearchDepth**

Description: double value of search depth

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchDepth = 1.0

**Arg25: dCritialPenetration**

Description: double value of critial penetration

Data Type: double

Default Value : DFLT_DBL

Syntax: dCritialPenetration = 1.0

**Arg26: iEstimationImpactTime**

Description: option for estimation impact time

Data Type: integer

Default Value : 0

Syntax: iEstimationImpactTime = 1

**Arg27: iFormula**

Description: option for formula

Data Type: integer

Default Value : 0

Syntax: iFormula = 1

**Arg28: iConstraintType**

Description: option for constraint type

Data Type: integer

Default Value : 0

Syntax: iConstraintType = 1

**Arg29: iDataType**

Description: option for data type

Data Type: integer

Default Value : 0

Syntax: iDataType = 1

**Arg30: iTypeId**

Description: option for type id

Data Type: integer

Default Value : 0

Syntax: iTypeId = 1

**Arg31: bTemperatureDependency**

Description: enable or disable feature temperature dependency

Data Type: bool

Default Value : False

Syntax: bTemperatureDependency = True/False

**Arg32: iNumDependencies**

Description: option for number dependencies

Data Type: integer

Default Value : 0

Syntax: iNumDependencies = 1

**Arg33: tshTableClearance**

Description: field data (table) of table clearance

Data Type: TSheetd

Default Value : []

Syntax: tshTableClearance = [Value1, Value1]

**Arg34: bStabilized**

Description: enable or disable feature stabilized

Data Type: bool

Default Value : 0

Syntax: bStabilized = True/False

**Arg35: iStabilizeType**

Description: option for stabilize type

Data Type: integer

Default Value : 0

Syntax: iStabilizeType = 1

**Arg36: dResidualFactor**

Description: double value of residual factor

Data Type: double

Default Value : DFLT_DBL

Syntax: dResidualFactor = 1.0

**Arg37: dEffectiveDist**

Description: double value of effective distance

Data Type: double

Default Value : DFLT_DBL

Syntax: dEffectiveDist = 1.0

**Arg38: dCN**

Description: double value of normal factor Cn

Data Type: double

Default Value : DFLT_DBL

Syntax: dCN = 1.0

**Arg39: dCT**

Description: double value of normal factor Ct

Data Type: double

Default Value : DFLT_DBL

Syntax: dCT = 1.0

**Arg40: crlClearance**

Description: array entities in model with type clearance

Data Type: cursor list

Default Value : []

Syntax: crlClearance = [EntityType(id1, id2, id3)]

**Arg41: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg42: dSearchAngle**

Description: double value of search angle

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchAngle = 1.0

**Arg43: iConstraintTypeExplicit**

Description: option for constraint type explicit

Data Type: integer

Default Value : 0

Syntax: iConstraintTypeExplicit = 1

**Arg44: dPenaltyFact**

Description: double value of penalty fact

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyFact = 1.0

**Arg45: dPenaltyFactExplicit**

Description: double value of penalty fact explicit

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyFactExplicit = 1.0

**Arg46: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

**Arg47: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg48: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.ADVC.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactADVC", iContactType=0, iSlidingType=0, iInitialState=0, dInitialStateTol=DFLT_DBL, dKineticFrictionCoef=DFLT_DBL, dExponentialCoef=DFLT_DBL, iBehavior=0, dClearance=DFLT_DBL, iAdjust2Clearance=0, dInterference=DFLT_DBL, iAdjust2Interference=0, iAutoShrink=0, iAdvAdjust=0, dAdjustValue=DFLT_DBL, dFrictionCoef=DFLT_DBL, dMaxShear=DFLT_DBL, dElasticSlip=DFLT_DBL, dSlipTolerance=DFLT_DBL, dSearchWidth=DFLT_DBL, dSearchGap=DFLT_DBL, dSearchDepth=DFLT_DBL, dCritialPenetration=DFLT_DBL, iEstimationImpactTime=0, iFormula=0, iConstraintType=0, iDataType=0, iTypeId=0, bTemperatureDependency=False, iNumDependencies=0, tshTableClearance=[], bStabilized=0, iStabilizeType=0, dResidualFactor=DFLT_DBL, dEffectiveDist=DFLT_DBL, dCN=DFLT_DBL, dCT=DFLT_DBL, crlClearance=[], crEdit=None, dSearchAngle=DFLT_DBL, iConstraintTypeExplicit=0, dPenaltyFact=DFLT_DBL, dPenaltyFactExplicit=DFLT_DBL, iColor=16711680, iAlg=0, iMethod=0)

```

==========================================================

# Connections.Contacts.ADVC.ContactShareFace

## Wrapper Macro

LbcContactShareFaceAdvcCr(...)

## Ribbon-GUI-Location

Connections > Contacts > ADVC > ContactShareFace

## Command Description

create ADVC Contact Share Face

## Argument List

**Arg1: crlShareFace**

Description: array entities in model with type share face

Data Type: cursor list

Default Value : []

Syntax: crlShareFace = [EntityType(id1, id2, id3)]

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactADVC"

Syntax: strName = "string input"

**Arg3: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg4: iSlidingType**

Description: option for sliding type

Data Type: integer

Default Value : 0

Syntax: iSlidingType = 1

**Arg5: iInitialState**

Description: option for initial state

Data Type: integer

Default Value : 0

Syntax: iInitialState = 1

**Arg6: dInitialStateTol**

Description: double value of initial state tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dInitialStateTol = 1.0

**Arg7: dKineticFrictionCoef**

Description: double value of kinetic friction coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dKineticFrictionCoef = 1.0

**Arg8: dExponentialCoef**

Description: double value of exponential coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dExponentialCoef = 1.0

**Arg9: iBehavior**

Description: option for behavior

Data Type: integer

Default Value : 0

Syntax: iBehavior = 1

**Arg10: dClearance**

Description: double value of clearance

Data Type: double

Default Value : DFLT_DBL

Syntax: dClearance = 1.0

**Arg11: iAdjust2Clearance**

Description: option for adjust2 clearance

Data Type: integer

Default Value : 0

Syntax: iAdjust2Clearance = 1

**Arg12: dInterference**

Description: double value of interference

Data Type: double

Default Value : DFLT_DBL

Syntax: dInterference = 1.0

**Arg13: iAdjust2Interference**

Description: option for adjust2 interference

Data Type: integer

Default Value : 0

Syntax: iAdjust2Interference = 1

**Arg14: iAutoShrink**

Description: option for auto shrink

Data Type: integer

Default Value : 0

Syntax: iAutoShrink = 1

**Arg15: iAdvAdjust**

Description: option for advc adjust

Data Type: integer

Default Value : 0

Syntax: iAdvAdjust = 1

**Arg16: dAdjustValue**

Description: double value of adjust value

Data Type: double

Default Value : DFLT_DBL

Syntax: dAdjustValue = 1.0

**Arg17: dFrictionCoef**

Description: double value of friction coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dFrictionCoef = 1.0

**Arg18: dMaxShear**

Description: double value of maximize shear

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxShear = 1.0

**Arg19: dElasticSlip**

Description: double value of elastic slip

Data Type: double

Default Value : DFLT_DBL

Syntax: dElasticSlip = 1.0

**Arg20: dSlipTolerance**

Description: double value of slip tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dSlipTolerance = 1.0

**Arg21: dSearchWidth**

Description: double value of search width

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchWidth = 1.0

**Arg22: dSearchGap**

Description: double value of search gap

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchGap = 1.0

**Arg23: dSearchDepth**

Description: double value of search depth

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchDepth = 1.0

**Arg24: dCritialPenetration**

Description: double value of critial penetration

Data Type: double

Default Value : DFLT_DBL

Syntax: dCritialPenetration = 1.0

**Arg25: iEstimationImpactTime**

Description: option for estimation impact time

Data Type: integer

Default Value : 0

Syntax: iEstimationImpactTime = 1

**Arg26: iFormula**

Description: option for formula

Data Type: integer

Default Value : 0

Syntax: iFormula = 1

**Arg27: iConstraintType**

Description: option for constraint type

Data Type: integer

Default Value : 0

Syntax: iConstraintType = 1

**Arg28: iDataType**

Description: option for data type

Data Type: integer

Default Value : 0

Syntax: iDataType = 1

**Arg29: iTypeId**

Description: option for type id

Data Type: integer

Default Value : 0

Syntax: iTypeId = 1

**Arg30: bTemperatureDependency**

Description: enable or disable feature temperature dependency

Data Type: bool

Default Value : False

Syntax: bTemperatureDependency = True/False

**Arg31: iNumDependencies**

Description: option for number dependencies

Data Type: integer

Default Value : 0

Syntax: iNumDependencies = 1

**Arg32: tshTableClearance**

Description: field data (table) of table clearance

Data Type: TSheetd

Default Value : []

Syntax: tshTableClearance = [Value1, Value1]

**Arg33: bStabilized**

Description: enable or disable feature stabilized

Data Type: bool

Default Value : 0

Syntax: bStabilized = True/False

**Arg34: iStabilizeType**

Description: option for stabilize type

Data Type: integer

Default Value : 0

Syntax: iStabilizeType = 1

**Arg35: dResidualFactor**

Description: double value of residual factor

Data Type: double

Default Value : DFLT_DBL

Syntax: dResidualFactor = 1.0

**Arg36: dEffectiveDist**

Description: double value of effective distance

Data Type: double

Default Value : DFLT_DBL

Syntax: dEffectiveDist = 1.0

**Arg37: dCN**

Description: double value of normal factor Cn

Data Type: double

Default Value : DFLT_DBL

Syntax: dCN = 1.0

**Arg38: dCT**

Description: double value of normal factor Ct

Data Type: double

Default Value : DFLT_DBL

Syntax: dCT = 1.0

**Arg39: crlClearance**

Description: array entities in model with type clearance

Data Type: cursor list

Default Value : []

Syntax: crlClearance = [EntityType(id1, id2, id3)]

**Arg40: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg41: dSearchAngle**

Description: double value of search angle

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchAngle = 1.0

**Arg42: iConstraintTypeExplicit**

Description: option for constraint type explicit

Data Type: integer

Default Value : 0

Syntax: iConstraintTypeExplicit = 1

**Arg43: dPenaltyFact**

Description: double value of penalty fact

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyFact = 1.0

**Arg44: dPenaltyFactExplicit**

Description: double value of penalty fact explicit

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyFactExplicit = 1.0

**Arg45: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

**Arg46: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg47: iMethod**

Description: option for method

Data Type: integer

Default Value : 3

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.ADVC.ContactShareFace(crlShareFace=[], strName="ContactADVC", iContactType=0, iSlidingType=0, iInitialState=0, dInitialStateTol=DFLT_DBL, dKineticFrictionCoef=DFLT_DBL, dExponentialCoef=DFLT_DBL, iBehavior=0, dClearance=DFLT_DBL, iAdjust2Clearance=0, dInterference=DFLT_DBL, iAdjust2Interference=0, iAutoShrink=0, iAdvAdjust=0, dAdjustValue=DFLT_DBL, dFrictionCoef=DFLT_DBL, dMaxShear=DFLT_DBL, dElasticSlip=DFLT_DBL, dSlipTolerance=DFLT_DBL, dSearchWidth=DFLT_DBL, dSearchGap=DFLT_DBL, dSearchDepth=DFLT_DBL, dCritialPenetration=DFLT_DBL, iEstimationImpactTime=0, iFormula=0, iConstraintType=0, iDataType=0, iTypeId=0, bTemperatureDependency=False, iNumDependencies=0, tshTableClearance=[], bStabilized=0, iStabilizeType=0, dResidualFactor=DFLT_DBL, dEffectiveDist=DFLT_DBL, dCN=DFLT_DBL, dCT=DFLT_DBL, crlClearance=[], crEdit=None, dSearchAngle=DFLT_DBL, iConstraintTypeExplicit=0, dPenaltyFact=DFLT_DBL, dPenaltyFactExplicit=DFLT_DBL, iColor=16711680, iAlg=0, iMethod=3)

```

==========================================================

# Connections.Contacts.ADVC.ContactTable

## Wrapper Macro

LbcContactTableAdvc(...)

## Ribbon-GUI-Location

Connections > Contacts > ADVC > ContactTable

## Command Description

create ADVC Contact Table

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactADVC"

Syntax: strName = "string input"

**Arg2: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg3: iSlidingType**

Description: option for sliding type

Data Type: integer

Default Value : 0

Syntax: iSlidingType = 1

**Arg4: iInitialState**

Description: option for initial state

Data Type: integer

Default Value : 0

Syntax: iInitialState = 1

**Arg5: dInitialStateTol**

Description: double value of initial state tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dInitialStateTol = 1.0

**Arg6: dKineticFrictionCoef**

Description: double value of kinetic friction coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dKineticFrictionCoef = 1.0

**Arg7: dExponentialCoef**

Description: double value of exponential coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dExponentialCoef = 1.0

**Arg8: iBehavior**

Description: option for behavior

Data Type: integer

Default Value : 0

Syntax: iBehavior = 1

**Arg9: dClearance**

Description: double value of clearance

Data Type: double

Default Value : DFLT_DBL

Syntax: dClearance = 1.0

**Arg10: iAdjust2Clearance**

Description: option for adjust2 clearance

Data Type: integer

Default Value : 0

Syntax: iAdjust2Clearance = 1

**Arg11: dInterference**

Description: double value of interference

Data Type: double

Default Value : DFLT_DBL

Syntax: dInterference = 1.0

**Arg12: iAdjust2Interference**

Description: option for adjust2 interference

Data Type: integer

Default Value : 0

Syntax: iAdjust2Interference = 1

**Arg13: iAutoShrink**

Description: option for auto shrink

Data Type: integer

Default Value : 0

Syntax: iAutoShrink = 1

**Arg14: iAdvAdjust**

Description: option for advc adjust

Data Type: integer

Default Value : 0

Syntax: iAdvAdjust = 1

**Arg15: dAdjustValue**

Description: double value of adjust value

Data Type: double

Default Value : DFLT_DBL

Syntax: dAdjustValue = 1.0

**Arg16: dFrictionCoef**

Description: double value of friction coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dFrictionCoef = 1.0

**Arg17: dMaxShear**

Description: double value of maximize shear

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxShear = 1.0

**Arg18: dElasticSlip**

Description: double value of elastic slip

Data Type: double

Default Value : DFLT_DBL

Syntax: dElasticSlip = 1.0

**Arg19: dSlipTolerance**

Description: double value of slip tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dSlipTolerance = 1.0

**Arg20: dSearchWidth**

Description: double value of search width

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchWidth = 1.0

**Arg21: dSearchGap**

Description: double value of search gap

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchGap = 1.0

**Arg22: dSearchDepth**

Description: double value of search depth

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchDepth = 1.0

**Arg23: dCritialPenetration**

Description: double value of critial penetration

Data Type: double

Default Value : DFLT_DBL

Syntax: dCritialPenetration = 1.0

**Arg24: iEstimationImpactTime**

Description: option for estimation impact time

Data Type: integer

Default Value : 0

Syntax: iEstimationImpactTime = 1

**Arg25: iFormula**

Description: option for formula

Data Type: integer

Default Value : 0

Syntax: iFormula = 1

**Arg26: iConstraintType**

Description: option for constraint type

Data Type: integer

Default Value : 0

Syntax: iConstraintType = 1

**Arg27: iDataType**

Description: option for data type

Data Type: integer

Default Value : 0

Syntax: iDataType = 1

**Arg28: iTypeId**

Description: option for type id

Data Type: integer

Default Value : 0

Syntax: iTypeId = 1

**Arg29: bTemperatureDependency**

Description: enable or disable feature temperature dependency

Data Type: bool

Default Value : False

Syntax: bTemperatureDependency = True/False

**Arg30: iNumDependencies**

Description: option for number dependencies

Data Type: integer

Default Value : 0

Syntax: iNumDependencies = 1

**Arg31: tshTableClearance**

Description: field data (table) of table clearance

Data Type: TSheetd

Default Value : []

Syntax: tshTableClearance = [Value1, Value1]

**Arg32: bStabilized**

Description: enable or disable feature stabilized

Data Type: bool

Default Value : 0

Syntax: bStabilized = True/False

**Arg33: iStabilizeType**

Description: option for stabilize type

Data Type: integer

Default Value : 0

Syntax: iStabilizeType = 1

**Arg34: dResidualFactor**

Description: double value of residual factor

Data Type: double

Default Value : DFLT_DBL

Syntax: dResidualFactor = 1.0

**Arg35: dEffectiveDist**

Description: double value of effective distance

Data Type: double

Default Value : DFLT_DBL

Syntax: dEffectiveDist = 1.0

**Arg36: dCN**

Description: double value of normal factor Cn

Data Type: double

Default Value : DFLT_DBL

Syntax: dCN = 1.0

**Arg37: dCT**

Description: double value of normal factor Ct

Data Type: double

Default Value : DFLT_DBL

Syntax: dCT = 1.0

**Arg38: crlClearance**

Description: array entities in model with type clearance

Data Type: cursor list

Default Value : []

Syntax: crlClearance = [EntityType(id1, id2, id3)]

**Arg39: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg40: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg41: dSearchAngle**

Description: double value of search angle

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchAngle = 1.0

**Arg42: iConstraintTypeExplicit**

Description: option for constraint type explicit

Data Type: integer

Default Value : 0

Syntax: iConstraintTypeExplicit = 1

**Arg43: dPenaltyFact**

Description: double value of penalty fact

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyFact = 1.0

**Arg44: dPenaltyFactExplicit**

Description: double value of penalty fact explicit

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyFactExplicit = 1.0

**Arg45: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

**Arg46: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg47: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.ADVC.ContactTable(strName="ContactADVC", iContactType=0, iSlidingType=0, iInitialState=0, dInitialStateTol=DFLT_DBL, dKineticFrictionCoef=DFLT_DBL, dExponentialCoef=DFLT_DBL, iBehavior=0, dClearance=DFLT_DBL, iAdjust2Clearance=0, dInterference=DFLT_DBL, iAdjust2Interference=0, iAutoShrink=0, iAdvAdjust=0, dAdjustValue=DFLT_DBL, dFrictionCoef=DFLT_DBL, dMaxShear=DFLT_DBL, dElasticSlip=DFLT_DBL, dSlipTolerance=DFLT_DBL, dSearchWidth=DFLT_DBL, dSearchGap=DFLT_DBL, dSearchDepth=DFLT_DBL, dCritialPenetration=DFLT_DBL, iEstimationImpactTime=0, iFormula=0, iConstraintType=0, iDataType=0, iTypeId=0, bTemperatureDependency=False, iNumDependencies=0, tshTableClearance=[], bStabilized=0, iStabilizeType=0, dResidualFactor=DFLT_DBL, dEffectiveDist=DFLT_DBL, dCN=DFLT_DBL, dCT=DFLT_DBL, crlClearance=[], crplTarget=[], crEdit=None, dSearchAngle=DFLT_DBL, iConstraintTypeExplicit=0, dPenaltyFact=DFLT_DBL, dPenaltyFactExplicit=DFLT_DBL, iColor=16711680, iAlg=0, iMethod=0)

```

==========================================================

# Connections.Contacts.ADVC.ContactGroupByMatrix

## Wrapper Macro

LbcContactAdvc_ContactGroupByMatrix(...)

## Ribbon-GUI-Location

Connections > Contacts > ADVC > ContactGroupByMatrix

## Command Description

create ADVC contact Group By Matrix

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactADVC"

Syntax: strName = "string input"

**Arg2: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg3: iSlidingType**

Description: option for sliding type

Data Type: integer

Default Value : 0

Syntax: iSlidingType = 1

**Arg4: iInitialState**

Description: option for initial state

Data Type: integer

Default Value : 0

Syntax: iInitialState = 1

**Arg5: dInitialStateTol**

Description: double value of initial state tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dInitialStateTol = 1.0

**Arg6: dKineticFrictionCoef**

Description: double value of kinetic friction coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dKineticFrictionCoef = 1.0

**Arg7: dExponentialCoef**

Description: double value of exponential coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dExponentialCoef = 1.0

**Arg8: iBehavior**

Description: option for behavior

Data Type: integer

Default Value : 0

Syntax: iBehavior = 1

**Arg9: dClearance**

Description: double value of clearance

Data Type: double

Default Value : DFLT_DBL

Syntax: dClearance = 1.0

**Arg10: iAdjust2Clearance**

Description: option for adjust2 clearance

Data Type: integer

Default Value : 0

Syntax: iAdjust2Clearance = 1

**Arg11: dInterference**

Description: double value of interference

Data Type: double

Default Value : DFLT_DBL

Syntax: dInterference = 1.0

**Arg12: iAdjust2Interference**

Description: option for adjust2 interference

Data Type: integer

Default Value : 0

Syntax: iAdjust2Interference = 1

**Arg13: iAutoShrink**

Description: option for auto shrink

Data Type: integer

Default Value : 0

Syntax: iAutoShrink = 1

**Arg14: iAdvAdjust**

Description: option for advc adjust

Data Type: integer

Default Value : 0

Syntax: iAdvAdjust = 1

**Arg15: dAdjustValue**

Description: double value of adjust value

Data Type: double

Default Value : DFLT_DBL

Syntax: dAdjustValue = 1.0

**Arg16: dFrictionCoef**

Description: double value of friction coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dFrictionCoef = 1.0

**Arg17: dMaxShear**

Description: double value of maximize shear

Data Type: double

Default Value : DFLT_DBL

Syntax: dMaxShear = 1.0

**Arg18: dElasticSlip**

Description: double value of elastic slip

Data Type: double

Default Value : DFLT_DBL

Syntax: dElasticSlip = 1.0

**Arg19: dSlipTolerance**

Description: double value of slip tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dSlipTolerance = 1.0

**Arg20: dSearchWidth**

Description: double value of search width

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchWidth = 1.0

**Arg21: dSearchGap**

Description: double value of search gap

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchGap = 1.0

**Arg22: dSearchDepth**

Description: double value of search depth

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchDepth = 1.0

**Arg23: dCritialPenetration**

Description: double value of critial penetration

Data Type: double

Default Value : DFLT_DBL

Syntax: dCritialPenetration = 1.0

**Arg24: iEstimationImpactTime**

Description: option for estimation impact time

Data Type: integer

Default Value : 0

Syntax: iEstimationImpactTime = 1

**Arg25: iFormula**

Description: option for formula

Data Type: integer

Default Value : 0

Syntax: iFormula = 1

**Arg26: iConstraintType**

Description: option for constraint type

Data Type: integer

Default Value : 0

Syntax: iConstraintType = 1

**Arg27: iDataType**

Description: option for data type

Data Type: integer

Default Value : 0

Syntax: iDataType = 1

**Arg28: iTypeId**

Description: option for type id

Data Type: integer

Default Value : 0

Syntax: iTypeId = 1

**Arg29: bTemperatureDependency**

Description: enable or disable feature temperature dependency

Data Type: bool

Default Value : False

Syntax: bTemperatureDependency = True/False

**Arg30: iNumDependencies**

Description: option for number dependencies

Data Type: integer

Default Value : 0

Syntax: iNumDependencies = 1

**Arg31: tshTableClearance**

Description: field data (table) of table clearance

Data Type: TSheetd

Default Value : []

Syntax: tshTableClearance = [Value1, Value1]

**Arg32: bStabilized**

Description: enable or disable feature stabilized

Data Type: bool

Default Value : 0

Syntax: bStabilized = True/False

**Arg33: iStabilizeType**

Description: option for stabilize type

Data Type: integer

Default Value : 0

Syntax: iStabilizeType = 1

**Arg34: dResidualFactor**

Description: double value of residual factor

Data Type: double

Default Value : DFLT_DBL

Syntax: dResidualFactor = 1.0

**Arg35: dEffectiveDist**

Description: double value of effective distance

Data Type: double

Default Value : DFLT_DBL

Syntax: dEffectiveDist = 1.0

**Arg36: dCN**

Description: double value of normal factor Cn

Data Type: double

Default Value : DFLT_DBL

Syntax: dCN = 1.0

**Arg37: dCT**

Description: double value of normal factor Ct

Data Type: double

Default Value : DFLT_DBL

Syntax: dCT = 1.0

**Arg38: crlClearance**

Description: array entities in model with type clearance

Data Type: cursor list

Default Value : []

Syntax: crlClearance = [EntityType(id1, id2, id3)]

**Arg39: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg40: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg41: dSearchAngle**

Description: double value of search angle

Data Type: double

Default Value : DFLT_DBL

Syntax: dSearchAngle = 1.0

**Arg42: iConstraintTypeExplicit**

Description: option for constraint type explicit

Data Type: integer

Default Value : 0

Syntax: iConstraintTypeExplicit = 1

**Arg43: dPenaltyFact**

Description: double value of penalty fact

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyFact = 1.0

**Arg44: dPenaltyFactExplicit**

Description: double value of penalty fact explicit

Data Type: double

Default Value : DFLT_DBL

Syntax: dPenaltyFactExplicit = 1.0

**Arg45: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

**Arg46: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg47: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.ADVC.ContactGroupByMatrix(strName="ContactADVC", iContactType=0, iSlidingType=0, iInitialState=0, dInitialStateTol=DFLT_DBL, dKineticFrictionCoef=DFLT_DBL, dExponentialCoef=DFLT_DBL, iBehavior=0, dClearance=DFLT_DBL, iAdjust2Clearance=0, dInterference=DFLT_DBL, iAdjust2Interference=0, iAutoShrink=0, iAdvAdjust=0, dAdjustValue=DFLT_DBL, dFrictionCoef=DFLT_DBL, dMaxShear=DFLT_DBL, dElasticSlip=DFLT_DBL, dSlipTolerance=DFLT_DBL, dSearchWidth=DFLT_DBL, dSearchGap=DFLT_DBL, dSearchDepth=DFLT_DBL, dCritialPenetration=DFLT_DBL, iEstimationImpactTime=0, iFormula=0, iConstraintType=0, iDataType=0, iTypeId=0, bTemperatureDependency=False, iNumDependencies=0, tshTableClearance=[], bStabilized=0, iStabilizeType=0, dResidualFactor=DFLT_DBL, dEffectiveDist=DFLT_DBL, dCN=DFLT_DBL, dCT=DFLT_DBL, crlClearance=[], crplTarget=[], crEdit=None, dSearchAngle=DFLT_DBL, iConstraintTypeExplicit=0, dPenaltyFact=DFLT_DBL, dPenaltyFactExplicit=DFLT_DBL, iColor=16711680, iAlg=0, iMethod=0)

```

==========================================================

# Connections.Contacts.Ansys.ManualGroup

## Wrapper Macro

ContactAnsys(...)

## Ribbon-GUI-Location

Connections > Contacts > Ansys > ManualGroup

## Command Description

create contact ansys Manual Group

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactAnsys_1"

Syntax: strName = "string input"

**Arg2: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg3: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg4: iContactAlgorithm**

Description: option for contact algorithm

Data Type: integer

Default Value : 0

Syntax: iContactAlgorithm = 1

**Arg5: ansysContact**

Description: data structure of ANSYS_CONTACT (refer PSJ Command Data Structure Document)

Data Type: ANSYS_CONTACT

Default Value : ANSYS_CONTACT()

Syntax: ansysContact = ANSYS_CONTACT(,,,)

**Arg6: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.Ansys.ManualGroup(strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)

```

==========================================================

# Connections.Contacts.Ansys.ManualFace

## Wrapper Macro

LbcContactManualFaceAnsys(...)

## Ribbon-GUI-Location

Connections > Contacts > Ansys > ManualFace

## Command Description

create contacts of Ansys Manual Face

## Argument List

**Arg1: crlFaceMaster**

Description: array entities in model with type face master

Data Type: cursor list

Default Value : []

Syntax: crlFaceMaster = [EntityType(id1, id2, id3)]

**Arg2: crlFaceSlave**

Description: array entities in model with type face slave

Data Type: cursor list

Default Value : []

Syntax: crlFaceSlave = [EntityType(id1, id2, id3)]

**Arg3: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactAnsys_1"

Syntax: strName = "string input"

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg5: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg6: iContactAlgorithm**

Description: option for contact algorithm

Data Type: integer

Default Value : 0

Syntax: iContactAlgorithm = 1

**Arg7: ansysContact**

Description: data structure of ANSYS_CONTACT (refer PSJ Command Data Structure Document)

Data Type: ANSYS_CONTACT

Default Value : ANSYS_CONTACT()

Syntax: ansysContact = ANSYS_CONTACT(,,,)

**Arg8: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg9: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.Ansys.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crEdit=None, iColor=16711680)

```

==========================================================

# Connections.Contacts.Ansys.ContactGroupByMatrix

## Wrapper Macro

LbcContactByGroupMatrixANSYS(...)

## Ribbon-GUI-Location

Connections > Contacts > Ansys > ContactGroupByMatrix

## Command Description

create contact ansys Group By Matrix

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactAnsys_1"

Syntax: strName = "string input"

**Arg2: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg3: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg4: iContactAlgorithm**

Description: option for contact algorithm

Data Type: integer

Default Value : 0

Syntax: iContactAlgorithm = 1

**Arg5: ansysContact**

Description: data structure of ANSYS_CONTACT (refer PSJ Command Data Structure Document)

Data Type: ANSYS_CONTACT

Default Value : ANSYS_CONTACT()

Syntax: ansysContact = ANSYS_CONTACT(,,,)

**Arg6: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.Ansys.ContactGroupByMatrix(strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)

```

==========================================================

# Connections.Contacts.Ansys.ContactShareFace

## Wrapper Macro

LbcContactShareFaceANSYSCr(...)

## Ribbon-GUI-Location

Connections > Contacts > Ansys > ContactShareFace

## Command Description

create contact ansys Share Face

## Argument List

**Arg1: crlShareFace**

Description: array entities in model with type share face

Data Type: cursor list

Default Value : []

Syntax: crlShareFace = [EntityType(id1, id2, id3)]

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactAnsys_1"

Syntax: strName = "string input"

**Arg3: iMethod**

Description: option for method

Data Type: integer

Default Value : 3

Syntax: iMethod = 1

**Arg4: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg5: iContactAlgorithm**

Description: option for contact algorithm

Data Type: integer

Default Value : 0

Syntax: iContactAlgorithm = 1

**Arg6: ansysContact**

Description: data structure of ANSYS_CONTACT (refer PSJ Command Data Structure Document)

Data Type: ANSYS_CONTACT

Default Value : ANSYS_CONTACT()

Syntax: ansysContact = ANSYS_CONTACT(,,,)

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.Ansys.ContactShareFace(crlShareFace=[], strName="ContactAnsys_1", iMethod=3, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crEdit=None, iColor=16711680)

```

==========================================================

# Connections.Contacts.Ansys.ContactTable

## Wrapper Macro

LbcContactTableANSYS(...)

## Ribbon-GUI-Location

Connections > Contacts > Ansys > ContactTable

## Command Description

create contact ansys Contact Table

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactAnsys_1"

Syntax: strName = "string input"

**Arg2: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg3: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg4: iContactAlgorithm**

Description: option for contact algorithm

Data Type: integer

Default Value : 0

Syntax: iContactAlgorithm = 1

**Arg5: ansysContact**

Description: data structure of ANSYS_CONTACT (refer PSJ Command Data Structure Document)

Data Type: ANSYS_CONTACT

Default Value : ANSYS_CONTACT()

Syntax: ansysContact = ANSYS_CONTACT(,,,)

**Arg6: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.Ansys.ContactTable(strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680)

```

==========================================================

# Connections.Contacts.MSCNastran.ManualGroup

## Wrapper Macro

ContactMSCNastran(...)

## Ribbon-GUI-Location

Connections > Contacts > MSCNastran > ManualGroup

## Command Description

create contacts of MSC Nastran

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: tssolverContact**

Description: data structure of NASTRAN_CONTACT (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_CONTACT

Default Value : NASTRAN_CONTACT()

Syntax: tssolverContact = NASTRAN_CONTACT(,,,)

**Arg3: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg5: iColor**

Description: option for color

Data Type: integer

Default Value : 65280

Syntax: iColor = 1

**Arg6: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.MSCNastran.ManualGroup(strName="", tssolverContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)

```

==========================================================

# Connections.Contacts.MSCNastran.ContactGroupByMatrix

## Wrapper Macro

LbcContactByGroupMatrixMSCNastran(...)

## Ribbon-GUI-Location

Connections > Contacts > MSCNastran > ContactGroupByMatrix

## Command Description

create contacts of MSC Nastran Contact Group By Matrix

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: nastranContact**

Description: data structure of NASTRAN_CONTACT (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_CONTACT

Default Value : NASTRAN_CONTACT()

Syntax: nastranContact = NASTRAN_CONTACT(,,,)

**Arg3: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg5: iColor**

Description: option for color

Data Type: integer

Default Value : 65280

Syntax: iColor = 1

**Arg6: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.MSCNastran.ContactGroupByMatrix(strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)

```

==========================================================

# Connections.Contacts.MSCNastran.ManualFace

## Wrapper Macro

LbcContactManualFaceMSCNastran(...)

## Ribbon-GUI-Location

Connections > Contacts > MSCNastran > ManualFace

## Command Description

create contacts of MSC Nastran Manual Face

## Argument List

**Arg1: crlFaceMaster**

Description: array entities in model with type face master

Data Type: cursor list

Default Value : []

Syntax: crlFaceMaster = [EntityType(id1, id2, id3)]

**Arg2: crlFaceSlave**

Description: array entities in model with type face slave

Data Type: cursor list

Default Value : []

Syntax: crlFaceSlave = [EntityType(id1, id2, id3)]

**Arg3: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactMSCNastran"

Syntax: strName = "string input"

**Arg4: nastranContact**

Description: data structure of NASTRAN_CONTACT (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_CONTACT

Default Value : NASTRAN_CONTACT()

Syntax: nastranContact = NASTRAN_CONTACT(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: iColor**

Description: option for color

Data Type: integer

Default Value : 65280

Syntax: iColor = 1

**Arg7: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.MSCNastran.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactMSCNastran", nastranContact=NASTRAN_CONTACT(), crEdit=None, iColor=65280, iMethod=0)

```

==========================================================

# Connections.Contacts.MSCNastran.ContactShareFace

## Wrapper Macro

LbcContactShareFaceMSCNastranCr(...)

## Ribbon-GUI-Location

Connections > Contacts > MSCNastran > ContactShareFace

## Command Description

create contacts of MSC Nastran Contact Share Face

## Argument List

**Arg1: crlShareFace**

Description: array entities in model with type share face

Data Type: cursor list

Default Value : []

Syntax: crlShareFace = [EntityType(id1, id2, id3)]

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg3: nastranContact**

Description: data structure of NASTRAN_CONTACT (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_CONTACT

Default Value : NASTRAN_CONTACT()

Syntax: nastranContact = NASTRAN_CONTACT(,,,)

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg5: iColor**

Description: option for color

Data Type: integer

Default Value : 65280

Syntax: iColor = 1

**Arg6: iMethod**

Description: option for method

Data Type: integer

Default Value : 3

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.MSCNastran.ContactShareFace(crlShareFace=[], strName="", nastranContact=NASTRAN_CONTACT(), crEdit=None, iColor=65280, iMethod=3)

```

==========================================================

# Connections.Contacts.MSCNastran.ContactTable

## Wrapper Macro

LbcContactTableMSCNastran(...)

## Ribbon-GUI-Location

Connections > Contacts > MSCNastran > ContactTable

## Command Description

create contacts of MSC Nastran Contact Table

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: nastranContact**

Description: data structure of NASTRAN_CONTACT (refer PSJ Command Data Structure Document)

Data Type: NASTRAN_CONTACT

Default Value : NASTRAN_CONTACT()

Syntax: nastranContact = NASTRAN_CONTACT(,,,)

**Arg3: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg5: iColor**

Description: option for color

Data Type: integer

Default Value : 65280

Syntax: iColor = 1

**Arg6: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.MSCNastran.ContactTable(strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1)

```

==========================================================

# Connections.Contacts.NXNastran.ManualFace

## Wrapper Macro

LbcContactManualFaceNXNastran(...)

## Ribbon-GUI-Location

Connections > Contacts > NXNastran > ManualFace

## Command Description

Create Contact NXNastran Manual Face

## Argument List

**Arg1: crlFaceMaster**

Description: array entities in model with type face master

Data Type: cursor list

Default Value : []

Syntax: crlFaceMaster = [EntityType(id1, id2, id3)]

**Arg2: crlFaceSlave**

Description: array entities in model with type face slave

Data Type: cursor list

Default Value : []

Syntax: crlFaceSlave = [EntityType(id1, id2, id3)]

**Arg3: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactNXNastran_1"

Syntax: strName = "string input"

**Arg4: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg5: iContactAlg**

Description: option for contact algorithm

Data Type: integer

Default Value : 0

Syntax: iContactAlg = 1

**Arg6: dNorPenFactor**

Description: double value of nor pen factor

Data Type: double

Default Value : 10

Syntax: dNorPenFactor = 1.0

**Arg7: dTanPenFactor**

Description: double value of tan pen factor

Data Type: double

Default Value : 1

Syntax: dTanPenFactor = 1.0

**Arg8: dForceConTol**

Description: double value of force con tolerance

Data Type: double

Default Value : 0.01

Syntax: dForceConTol = 1.0

**Arg9: dMaxForceIter**

Description: double value of maximize force iterator

Data Type: double

Default Value : 10

Syntax: dMaxForceIter = 1.0

**Arg10: dMaxStaIter**

Description: double value of maximize sta iterator

Data Type: double

Default Value : 20

Syntax: dMaxStaIter = 1.0

**Arg11: dChangeNum**

Description: double value of change number

Data Type: double

Default Value : 0.02

Syntax: dChangeNum = 1.0

**Arg12: dMinContactPer**

Description: double value of minimize contact per

Data Type: double

Default Value : 100

Syntax: dMinContactPer = 1.0

**Arg13: iShellThickness**

Description: option for shell thickness

Data Type: integer

Default Value : 0

Syntax: iShellThickness = 1

**Arg14: iContactStatus**

Description: option for contact status

Data Type: integer

Default Value : 0

Syntax: iContactStatus = 1

**Arg15: iInitGapPenetra**

Description: option for init gap penetra

Data Type: integer

Default Value : 0

Syntax: iInitGapPenetra = 1

**Arg16: iRegionRefine**

Description: option for region refine

Data Type: integer

Default Value : 0

Syntax: iRegionRefine = 1

**Arg17: iEvaluPts**

Description: option for evalu pts

Data Type: integer

Default Value : 1

Syntax: iEvaluPts = 1

**Arg18: dMinSearDist**

Description: double value of minimize sear distance

Data Type: double

Default Value : 0

Syntax: dMinSearDist = 1.0

**Arg19: dMaxSearDist**

Description: double value of maximize sear distance

Data Type: double

Default Value : 0.01

Syntax: dMaxSearDist = 1.0

**Arg20: dFricCoef**

Description: double value of fric coefficient

Data Type: double

Default Value : 0

Syntax: dFricCoef = 1.0

**Arg21: dSearchDist**

Description: double value of search distance

Data Type: double

Default Value : 0

Syntax: dSearchDist = 1.0

**Arg22: dPenatlyFactor**

Description: double value of penatly factor

Data Type: double

Default Value : 0

Syntax: dPenatlyFactor = 1.0

**Arg23: iShellOffset**

Description: option for shell offset

Data Type: integer

Default Value : 0

Syntax: iShellOffset = 1

**Arg24: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

**Arg25: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg26: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.NXNastran.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=0, crEdit=None)

```

==========================================================

# Connections.Contacts.NXNastran.ContactShareFace

## Wrapper Macro

LbcContactShareFaceNxNastran(...)

## Ribbon-GUI-Location

Connections > Contacts > NXNastran > ContactShareFace

## Command Description

Create Contact NXNastran Contact Share Face

## Argument List

**Arg1: crlShareFace**

Description: array entities in model with type face (share face)

Data Type: cursor list

Default Value : []

Syntax: crlShareFace = [EntityType(id1, id2, id3)]

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactNXNastran_1"

Syntax: strName = "string input"

**Arg3: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg4: iContactAlg**

Description: option for contact algorithm

Data Type: integer

Default Value : 0

Syntax: iContactAlg = 1

**Arg5: dNorPenFactor**

Description: double value of nor pen factor

Data Type: double

Default Value : 10

Syntax: dNorPenFactor = 1.0

**Arg6: dTanPenFactor**

Description: double value of tan pen factor

Data Type: double

Default Value : 1

Syntax: dTanPenFactor = 1.0

**Arg7: dForceConTol**

Description: double value of force con tolerance

Data Type: double

Default Value : 0.01

Syntax: dForceConTol = 1.0

**Arg8: dMaxForceIter**

Description: double value of maximize force iterator

Data Type: double

Default Value : 10

Syntax: dMaxForceIter = 1.0

**Arg9: dMaxStaIter**

Description: double value of maximize sta iterator

Data Type: double

Default Value : 20

Syntax: dMaxStaIter = 1.0

**Arg10: dChangeNum**

Description: double value of change number

Data Type: double

Default Value : 0.02

Syntax: dChangeNum = 1.0

**Arg11: dMinContactPer**

Description: double value of minimize contact per

Data Type: double

Default Value : 100

Syntax: dMinContactPer = 1.0

**Arg12: iShellThickness**

Description: option for shell thickness

Data Type: integer

Default Value : 0

Syntax: iShellThickness = 1

**Arg13: iContactStatus**

Description: option for contact status

Data Type: integer

Default Value : 0

Syntax: iContactStatus = 1

**Arg14: iInitGapPenetra**

Description: option for init gap penetra

Data Type: integer

Default Value : 0

Syntax: iInitGapPenetra = 1

**Arg15: iRegionRefine**

Description: option for region refine

Data Type: integer

Default Value : 0

Syntax: iRegionRefine = 1

**Arg16: iEvaluPts**

Description: option for evalu pts

Data Type: integer

Default Value : 1

Syntax: iEvaluPts = 1

**Arg17: dMinSearDist**

Description: double value of minimize sear distance

Data Type: double

Default Value : 0

Syntax: dMinSearDist = 1.0

**Arg18: dMaxSearDist**

Description: double value of maximize sear distance

Data Type: double

Default Value : 0.01

Syntax: dMaxSearDist = 1.0

**Arg19: dFricCoef**

Description: double value of fric coefficient

Data Type: double

Default Value : 0

Syntax: dFricCoef = 1.0

**Arg20: dSearchDist**

Description: double value of search distance

Data Type: double

Default Value : 0

Syntax: dSearchDist = 1.0

**Arg21: dPenatlyFactor**

Description: double value of penatly factor

Data Type: double

Default Value : 0

Syntax: dPenatlyFactor = 1.0

**Arg22: iShellOffset**

Description: option for shell offset

Data Type: integer

Default Value : 0

Syntax: iShellOffset = 1

**Arg23: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

**Arg24: iMethod**

Description: option for method

Data Type: integer

Default Value : 3

Syntax: iMethod = 1

**Arg25: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.NXNastran.ContactShareFace(crlShareFace=[], strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=3, crEdit=None)

```

==========================================================

# Connections.Contacts.NXNastran.ContactTable

## Wrapper Macro

LbcContactTableNXNastran(...)

## Ribbon-GUI-Location

Connections > Contacts > NXNastran > ContactTable

## Command Description

Create Contact NXNastran Contact Table

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg3: iAlg**

Description: option for algorithm

Data Type: integer

Default Value : 0

Syntax: iAlg = 1

**Arg4: dNorPenFactor**

Description: double value of nor pen factor

Data Type: double

Default Value : 0

Syntax: dNorPenFactor = 1.0

**Arg5: dTanPenFactor**

Description: double value of tan pen factor

Data Type: double

Default Value : 0

Syntax: dTanPenFactor = 1.0

**Arg6: dForceConTol**

Description: double value of force con tolerance

Data Type: double

Default Value : 0

Syntax: dForceConTol = 1.0

**Arg7: dMaxForceIter**

Description: double value of maximize force iterator

Data Type: double

Default Value : 0

Syntax: dMaxForceIter = 1.0

**Arg8: dMaxStaIter**

Description: double value of maximize sta iterator

Data Type: double

Default Value : 0

Syntax: dMaxStaIter = 1.0

**Arg9: dChangeNum**

Description: double value of change number

Data Type: double

Default Value : 0

Syntax: dChangeNum = 1.0

**Arg10: dMinContactPer**

Description: double value of minimize contact per

Data Type: double

Default Value : 0

Syntax: dMinContactPer = 1.0

**Arg11: iShellThickness**

Description: option for shell thickness

Data Type: integer

Default Value : 0

Syntax: iShellThickness = 1

**Arg12: iContactStatus**

Description: option for contact status

Data Type: integer

Default Value : 0

Syntax: iContactStatus = 1

**Arg13: iInitGapPenetra**

Description: option for init gap penetra

Data Type: integer

Default Value : 0

Syntax: iInitGapPenetra = 1

**Arg14: iRegionRefine**

Description: option for region refine

Data Type: integer

Default Value : 0

Syntax: iRegionRefine = 1

**Arg15: iEvaluPts**

Description: option for evalu pts

Data Type: integer

Default Value : 0

Syntax: iEvaluPts = 1

**Arg16: dMinSearDist**

Description: double value of minimize sear distance

Data Type: double

Default Value : 0

Syntax: dMinSearDist = 1.0

**Arg17: dMaxSearDist**

Description: double value of maximize sear distance

Data Type: double

Default Value : 0

Syntax: dMaxSearDist = 1.0

**Arg18: dFricCoef**

Description: double value of fric coefficient

Data Type: double

Default Value : 0

Syntax: dFricCoef = 1.0

**Arg19: dSearchDist**

Description: double value of search distance

Data Type: double

Default Value : 0

Syntax: dSearchDist = 1.0

**Arg20: dPenatlyFactor**

Description: double value of penatly factor

Data Type: double

Default Value : 0

Syntax: dPenatlyFactor = 1.0

**Arg21: iShellOffset**

Description: option for shell offset

Data Type: integer

Default Value : 0

Syntax: iShellOffset = 1

**Arg22: crplTargetPair**

Description: list pair of entities in database model pair

Data Type: cursor pair list

Default Value : []

Syntax: crplTargetPair = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg23: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg24: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

**Arg25: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.NXNastran.ContactTable(strName="", iType=0, iAlg=0, dNorPenFactor=0, dTanPenFactor=0, dForceConTol=0, dMaxForceIter=0, dMaxStaIter=0, dChangeNum=0, dMinContactPer=0, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=0, dMinSearDist=0, dMaxSearDist=0, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, crplTargetPair=[], crEdit=None, iColor=0, iMethod=1)

```

==========================================================

# Connections.Contacts.NXNastran.ManualGroup

## Wrapper Macro

LbcContactManualGroupNXNastran(...)

## Ribbon-GUI-Location

Connections > Contacts > NXNastran > ManualGroup

## Command Description

Create Contact NXNastran Manual Group

## Argument List

**Arg1: crFaceMaster**

Description: entity in database model with type face master

Data Type: cursor

Default Value : None

Syntax: crFaceMaster = EntityType(id)

**Arg2: crFaceSlave**

Description: entity in database model with type face slave

Data Type: cursor

Default Value : None

Syntax: crFaceSlave = EntityType(id)

**Arg3: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactNXNastran_1"

Syntax: strName = "string input"

**Arg4: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg5: iContactAlg**

Description: option for contact algorithm

Data Type: integer

Default Value : 0

Syntax: iContactAlg = 1

**Arg6: dNorPenFactor**

Description: double value of nor pen factor

Data Type: double

Default Value : 10

Syntax: dNorPenFactor = 1.0

**Arg7: dTanPenFactor**

Description: double value of tan pen factor

Data Type: double

Default Value : 1

Syntax: dTanPenFactor = 1.0

**Arg8: dForceConTol**

Description: double value of force con tolerance

Data Type: double

Default Value : 0.01

Syntax: dForceConTol = 1.0

**Arg9: dMaxForceIter**

Description: double value of maximize force iterator

Data Type: double

Default Value : 10

Syntax: dMaxForceIter = 1.0

**Arg10: dMaxStaIter**

Description: double value of maximize sta iterator

Data Type: double

Default Value : 20

Syntax: dMaxStaIter = 1.0

**Arg11: dChangeNum**

Description: double value of change number

Data Type: double

Default Value : 0.02

Syntax: dChangeNum = 1.0

**Arg12: dMinContactPer**

Description: double value of minimize contact per

Data Type: double

Default Value : 100

Syntax: dMinContactPer = 1.0

**Arg13: iShellThickness**

Description: option for shell thickness

Data Type: integer

Default Value : 0

Syntax: iShellThickness = 1

**Arg14: iContactStatus**

Description: option for contact status

Data Type: integer

Default Value : 0

Syntax: iContactStatus = 1

**Arg15: iInitGapPenetra**

Description: option for init gap penetra

Data Type: integer

Default Value : 0

Syntax: iInitGapPenetra = 1

**Arg16: iRegionRefine**

Description: option for region refine

Data Type: integer

Default Value : 0

Syntax: iRegionRefine = 1

**Arg17: iEvaluPts**

Description: option for evalu pts

Data Type: integer

Default Value : 1

Syntax: iEvaluPts = 1

**Arg18: dMinSearDist**

Description: double value of minimize sear distance

Data Type: double

Default Value : 0

Syntax: dMinSearDist = 1.0

**Arg19: dMaxSearDist**

Description: double value of maximize sear distance

Data Type: double

Default Value : 0.01

Syntax: dMaxSearDist = 1.0

**Arg20: dFricCoef**

Description: double value of fric coefficient

Data Type: double

Default Value : 0

Syntax: dFricCoef = 1.0

**Arg21: dSearchDist**

Description: double value of search distance

Data Type: double

Default Value : 0

Syntax: dSearchDist = 1.0

**Arg22: dPenatlyFactor**

Description: double value of penatly factor

Data Type: double

Default Value : 0

Syntax: dPenatlyFactor = 1.0

**Arg23: iShellOffset**

Description: option for shell offset

Data Type: integer

Default Value : 0

Syntax: iShellOffset = 1

**Arg24: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

**Arg25: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg26: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.NXNastran.ManualGroup(crFaceMaster=None, crFaceSlave=None, strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=0, crEdit=None)

```

==========================================================

# Connections.Contacts.NXNastran.ContactGroupByMatrix

## Wrapper Macro

LbcContactContactGroupByMatrixNXNastran(...)

## Ribbon-GUI-Location

Connections > Contacts > NXNastran > ContactGroupByMatrix

## Command Description

Create Contact NXNastran Contact Group By Matrix

## Argument List

**Arg1: crFaceMaster**

Description: entity in database model with type face master

Data Type: cursor

Default Value : None

Syntax: crFaceMaster = EntityType(id)

**Arg2: crFaceSlave**

Description: entity in database model with type face slave

Data Type: cursor

Default Value : None

Syntax: crFaceSlave = EntityType(id)

**Arg3: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactNXNastran_1"

Syntax: strName = "string input"

**Arg4: iContactType**

Description: option for contact type

Data Type: integer

Default Value : 0

Syntax: iContactType = 1

**Arg5: iContactAlg**

Description: option for contact algorithm

Data Type: integer

Default Value : 0

Syntax: iContactAlg = 1

**Arg6: dNorPenFactor**

Description: double value of nor pen factor

Data Type: double

Default Value : 10

Syntax: dNorPenFactor = 1.0

**Arg7: dTanPenFactor**

Description: double value of tan pen factor

Data Type: double

Default Value : 1

Syntax: dTanPenFactor = 1.0

**Arg8: dForceConTol**

Description: double value of force con tolerance

Data Type: double

Default Value : 0.01

Syntax: dForceConTol = 1.0

**Arg9: dMaxForceIter**

Description: double value of maximize force iterator

Data Type: double

Default Value : 10

Syntax: dMaxForceIter = 1.0

**Arg10: dMaxStaIter**

Description: double value of maximize sta iterator

Data Type: double

Default Value : 20

Syntax: dMaxStaIter = 1.0

**Arg11: dChangeNum**

Description: double value of change number

Data Type: double

Default Value : 0.02

Syntax: dChangeNum = 1.0

**Arg12: dMinContactPer**

Description: double value of minimize contact per

Data Type: double

Default Value : 100

Syntax: dMinContactPer = 1.0

**Arg13: iShellThickness**

Description: option for shell thickness

Data Type: integer

Default Value : 0

Syntax: iShellThickness = 1

**Arg14: iContactStatus**

Description: option for contact status

Data Type: integer

Default Value : 0

Syntax: iContactStatus = 1

**Arg15: iInitGapPenetra**

Description: option for init gap penetra

Data Type: integer

Default Value : 0

Syntax: iInitGapPenetra = 1

**Arg16: iRegionRefine**

Description: option for region refine

Data Type: integer

Default Value : 0

Syntax: iRegionRefine = 1

**Arg17: iEvaluPts**

Description: option for evalu pts

Data Type: integer

Default Value : 1

Syntax: iEvaluPts = 1

**Arg18: dMinSearDist**

Description: double value of minimize sear distance

Data Type: double

Default Value : 0

Syntax: dMinSearDist = 1.0

**Arg19: dMaxSearDist**

Description: double value of maximize sear distance

Data Type: double

Default Value : 0.01

Syntax: dMaxSearDist = 1.0

**Arg20: dFricCoef**

Description: double value of fric coefficient

Data Type: double

Default Value : 0

Syntax: dFricCoef = 1.0

**Arg21: dSearchDist**

Description: double value of search distance

Data Type: double

Default Value : 0

Syntax: dSearchDist = 1.0

**Arg22: dPenatlyFactor**

Description: double value of penatly factor

Data Type: double

Default Value : 0

Syntax: dPenatlyFactor = 1.0

**Arg23: iShellOffset**

Description: option for shell offset

Data Type: integer

Default Value : 0

Syntax: iShellOffset = 1

**Arg24: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

**Arg25: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg26: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.NXNastran.ContactGroupByMatrix(crFaceMaster=None, crFaceSlave=None, strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=0, crEdit=None)

```

==========================================================

# Connections.Contacts.TSSolver.ManualFace

## Wrapper Macro

ContactTSSolver(...)

## Ribbon-GUI-Location

Connections > Contacts > TSSolver > ManualFace

## Command Description

Create TSSolver Contact

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactTSSolver_1"

Syntax: strName = "string input"

**Arg2: nastranContact**

Description: data structure of TSSOLVER_CONTACT (refer PSJ Command Data Structure Document)

Data Type: TSSOLVER_CONTACT

Default Value : TSSOLVER_CONTACT()

Syntax: nastranContact = TSSOLVER_CONTACT(,,,)

**Arg3: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg5: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

**Arg6: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.TSSolver.ManualFace(strName="ContactTSSolver_1", nastranContact=TSSOLVER_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680, iMethod=0)

```

==========================================================

# Connections.Contacts.TSSolver.Auto

## Wrapper Macro

FindContact(...)

## Ribbon-GUI-Location

Connections > Contacts > TSSolver > Auto

## Command Description

find contact

## Argument List

**Arg1: strlNames**

Description: list definition string of names

Data Type: string list

Default Value : []

Syntax: strlNames = ["str1", "str2", "str3"]

**Arg2: crllMasterFaceTargets**

Description: list array of entities in model with type master face targets

Data Type: cursor list list

Default Value : [[]]

Syntax: crllMasterFaceTargets = [EntityType(id1, id2, id3), EntityType(id1, id2, id3)]

**Arg3: crllSlaveFaceTargets**

Description: list array of entities in model with type slave face targets

Data Type: cursor list list

Default Value : [[]]

Syntax: crllSlaveFaceTargets = [EntityType(id1, id2, id3), EntityType(id1, id2, id3)]

**Arg4: crlContactTypes**

Description: array entities in model with type contact types

Data Type: cursor list

Default Value : [1]

Syntax: crlContactTypes = [EntityType(id1, id2, id3)]

**Arg5: dlInterferenceClosures**

Description: array double values of interference closures

Data Type: double list

Default Value : [1.0]

Syntax: dlInterferenceClosures = [1.0, 2.0]

**Arg6: dlFrictionCoefficients**

Description: array double values of friction coefficients

Data Type: double list

Default Value : [DFLT_DBL]

Syntax: dlFrictionCoefficients = [1.0, 2.0]

**Arg7: blInitialAdjustments**

Description: list of enable/disable options of initial adjustments

Data Type: bool list

Default Value : [False]

Syntax: blInitialAdjustments = [True, False]

**Arg8: crlColors**

Description: array entities in model with type colors

Data Type: cursor list

Default Value : [65280]

Syntax: crlColors = [EntityType(id1, id2, id3)]

**Arg9: crlEdit**

Description: array entities in model with type edit

Data Type: cursor list

Default Value : []

Syntax: crlEdit = [EntityType(id1, id2, id3)]

**Arg10: crlMasterGroup**

Description: array entities in model with type master group

Data Type: cursor list

Default Value : []

Syntax: crlMasterGroup = [EntityType(id1, id2, id3)]

**Arg11: crlSlaveGroup**

Description: array entities in model with type slave group

Data Type: cursor list

Default Value : []

Syntax: crlSlaveGroup = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.TSSolver.Auto(strlNames=[], crllMasterFaceTargets=[[]], crllSlaveFaceTargets=[[]], crlContactTypes=[1], dlInterferenceClosures=[1.0], dlFrictionCoefficients=[DFLT_DBL], blInitialAdjustments=[False], crlColors=[65280], crlEdit=[], crlMasterGroup=[], crlSlaveGroup=[])

```

==========================================================

# Connections.Contacts.TSSolver.ManualGroup

## Wrapper Macro

LbcContactTSSolver_ManualGroup(...)

## Ribbon-GUI-Location

Connections > Contacts > TSSolver > ManualGroup

## Command Description

Create TSSolver Contact

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactTSSolver_1"

Syntax: strName = "string input"

**Arg2: tssolverContact**

Description: data structure of TSSOLVER_CONTACT (refer PSJ Command Data Structure Document)

Data Type: TSSOLVER_CONTACT

Default Value : TSSOLVER_CONTACT()

Syntax: tssolverContact = TSSOLVER_CONTACT(,,,)

**Arg3: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg5: iColor**

Description: option for color

Data Type: integer

Default Value : 16711680

Syntax: iColor = 1

**Arg6: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.TSSolver.ManualGroup(strName="ContactTSSolver_1", tssolverContact=TSSOLVER_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680, iMethod=0)

```

==========================================================

# Connections.Contacts.TSSS.ManualFace

## Wrapper Macro

ContactManualFaceTSSS(...)

## Ribbon-GUI-Location

Connections > Contacts > TSSS > ManualFace

## Command Description

Create Contact TSSS Manual Face

## Argument List

**Arg1: crlFaceMaster**

Description: array entities in model with type face master

Data Type: cursor list

Default Value : []

Syntax: crlFaceMaster = [EntityType(id1, id2, id3)]

**Arg2: crlFaceSlave**

Description: array entities in model with type face slave

Data Type: cursor list

Default Value : []

Syntax: crlFaceSlave = [EntityType(id1, id2, id3)]

**Arg3: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactTS_SS_1"

Syntax: strName = "string input"

**Arg4: nastranContact**

Description: data structure of SUNSHINE_CONTACT (refer PSJ Command Data Structure Document)

Data Type: SUNSHINE_CONTACT

Default Value : SUNSHINE_CONTACT()

Syntax: nastranContact = SUNSHINE_CONTACT(,,,)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg6: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

**Arg7: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.TSSS.ManualFace(crlFaceMaster=[], crlFaceSlave=[], strName="ContactTS_SS_1", nastranContact=SUNSHINE_CONTACT(), crEdit=None, iColor=0, iMethod=0)

```

==========================================================

# Connections.Contacts.TSSS.ManualGroup

## Wrapper Macro

ContactTSSS(...)

## Ribbon-GUI-Location

Connections > Contacts > TSSS > ManualGroup

## Command Description

Create Contact TSSS Manual FaceGroup

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactTS_SS_1"

Syntax: strName = "string input"

**Arg2: tssolverContact**

Description: data structure of SUNSHINE_CONTACT (refer PSJ Command Data Structure Document)

Data Type: SUNSHINE_CONTACT

Default Value : SUNSHINE_CONTACT()

Syntax: tssolverContact = SUNSHINE_CONTACT(,,,)

**Arg3: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg5: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

**Arg6: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.TSSS.ManualGroup(strName="ContactTS_SS_1", tssolverContact=SUNSHINE_CONTACT(), crplTarget=[], crEdit=None, iColor=0, iMethod=1)

```

==========================================================

# Connections.Contacts.TSSS.ContactTable

## Wrapper Macro

ContactTSSS_ContactTable(...)

## Ribbon-GUI-Location

Connections > Contacts > TSSS > ContactTable

## Command Description

Create Contact TSSS Manual FaceGroup

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "ContactTS_SS_1"

Syntax: strName = "string input"

**Arg2: nastranContact**

Description: data structure of SUNSHINE_CONTACT (refer PSJ Command Data Structure Document)

Data Type: SUNSHINE_CONTACT

Default Value : SUNSHINE_CONTACT()

Syntax: nastranContact = SUNSHINE_CONTACT(,,,)

**Arg3: crplTarget**

Description: list pair of entities in database model

Data Type: cursor pair list

Default Value : []

Syntax: crplTarget = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg4: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg5: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

**Arg6: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.TSSS.ContactTable(strName="ContactTS_SS_1", nastranContact=SUNSHINE_CONTACT(), crplTarget=[], crEdit=None, iColor=0, iMethod=1)

```

==========================================================

# Connections.Contacts.CheckPattern

## Wrapper Macro

CheckPattern(...)

## Ribbon-GUI-Location

Connections > Contacts > CheckPattern

## Command Description

check contact Pattern

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: bShowMismatch**

Description: enable or disable feature show mismatch

Data Type: bool

Default Value : False

Syntax: bShowMismatch = True/False

**Arg3: bShowMatch**

Description: enable or disable feature show match

Data Type: bool

Default Value : True

Syntax: bShowMatch = True/False

**Arg4: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 0.01

Syntax: dTol = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.CheckPattern(crlPart=[], bShowMismatch=False, bShowMatch=True, dTol=0.01)

```

==========================================================

# Connections.Contacts.NXNastranGeneral

## Wrapper Macro

ContactNXNastran(...)

## Ribbon-GUI-Location

Connections > Contacts > NXNastranGeneral

## Command Description

Command use for Connections Contacts NXNastranGeneral

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iPiType**

Description: option for pi type

Data Type: integer

Default Value : 0

Syntax: iPiType = 1

**Arg3: iPiAlg**

Description: option for pi algorithm

Data Type: integer

Default Value : 0

Syntax: iPiAlg = 1

**Arg4: dPdNorPenFactor**

Description: double value of pd nor pen factor

Data Type: double

Default Value : 0

Syntax: dPdNorPenFactor = 1.0

**Arg5: dPdTanPenFactor**

Description: double value of pd tan pen factor

Data Type: double

Default Value : 0

Syntax: dPdTanPenFactor = 1.0

**Arg6: dPdForceConTol**

Description: double value of pd force con tolerance

Data Type: double

Default Value : 0

Syntax: dPdForceConTol = 1.0

**Arg7: dPdMaxForceIter**

Description: double value of pd maximize force iterator

Data Type: double

Default Value : 0

Syntax: dPdMaxForceIter = 1.0

**Arg8: dPdMaxStaIter**

Description: double value of pd maximize sta iterator

Data Type: double

Default Value : 0

Syntax: dPdMaxStaIter = 1.0

**Arg9: dPdChangeNum**

Description: double value of pd change number

Data Type: double

Default Value : 0

Syntax: dPdChangeNum = 1.0

**Arg10: dPdMinContactPer**

Description: double value of pd minimize contact per

Data Type: double

Default Value : 0

Syntax: dPdMinContactPer = 1.0

**Arg11: iPiShellThickness**

Description: option for pi shell thickness

Data Type: integer

Default Value : 0

Syntax: iPiShellThickness = 1

**Arg12: iPiContactStatus**

Description: option for pi contact status

Data Type: integer

Default Value : 0

Syntax: iPiContactStatus = 1

**Arg13: iPiInitGapPenetra**

Description: option for pi init gap penetra

Data Type: integer

Default Value : 0

Syntax: iPiInitGapPenetra = 1

**Arg14: iPiRegionRefine**

Description: option for pi region refine

Data Type: integer

Default Value : 0

Syntax: iPiRegionRefine = 1

**Arg15: iPiEvaluPts**

Description: option for pi evalu pts

Data Type: integer

Default Value : 0

Syntax: iPiEvaluPts = 1

**Arg16: dPdMinSearDist**

Description: double value of pd minimize sear distance

Data Type: double

Default Value : 0

Syntax: dPdMinSearDist = 1.0

**Arg17: dPdMaxSearDist**

Description: double value of pd maximize sear distance

Data Type: double

Default Value : 0

Syntax: dPdMaxSearDist = 1.0

**Arg18: dPdFricCoef**

Description: double value of pd fric coefficient

Data Type: double

Default Value : 0

Syntax: dPdFricCoef = 1.0

**Arg19: dPdSearchDist**

Description: double value of pd search distance

Data Type: double

Default Value : 0

Syntax: dPdSearchDist = 1.0

**Arg20: dPdPenatlyFactor**

Description: double value of pd penatly factor

Data Type: double

Default Value : 0

Syntax: dPdPenatlyFactor = 1.0

**Arg21: iPiShellOffset**

Description: option for pi shell offset

Data Type: integer

Default Value : 0

Syntax: iPiShellOffset = 1

**Arg22: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg23: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg24: iColor**

Description: option for color

Data Type: integer

Default Value : 0

Syntax: iColor = 1

**Arg25: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.NXNastranGeneral(strName="", iPiType=0, iPiAlg=0, dPdNorPenFactor=0, dPdTanPenFactor=0, dPdForceConTol=0, dPdMaxForceIter=0, dPdMaxStaIter=0, dPdChangeNum=0, dPdMinContactPer=0, iPiShellThickness=0, iPiContactStatus=0, iPiInitGapPenetra=0, iPiRegionRefine=0, iPiEvaluPts=0, dPdMinSearDist=0, dPdMaxSearDist=0, dPdFricCoef=0, dPdSearchDist=0, dPdPenatlyFactor=0, iPiShellOffset=0, crlTarget=[], crEdit=None, iColor=0, iMethod=0)

```

==========================================================

# Connections.Contacts.ExportCheckReport

## Wrapper Macro

CreateContactReport(...)

## Ribbon-GUI-Location

Connections > Contacts > ExportCheckReport

## Command Description

Command use for Connections Contacts ExportCheckReport

## Argument List

**Arg1: strFullPath**

Description: definition string of input full path

Data Type: string

Default Value : ""

Syntax: strFullPath = "string input"

**Arg2: dZoomFactor**

Description: double value of zoom factor

Data Type: double

Default Value : 1.2

Syntax: dZoomFactor = 1.0

**Arg3: iFitBy**

Description: option for fit by

Data Type: integer

Default Value : 0

Syntax: iFitBy = 1

**Arg4: iListBy**

Description: option for list by

Data Type: integer

Default Value : 0

Syntax: iListBy = 1

**Arg5: iListOrder**

Description: option for list order

Data Type: integer

Default Value : 0

Syntax: iListOrder = 1

**Arg6: iFormat**

Description: option for format

Data Type: integer

Default Value : 0

Syntax: iFormat = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Contacts.ExportCheckReport(strFullPath="", dZoomFactor=1.2, iFitBy=0, iListBy=0, iListOrder=0, iFormat=0)

```

==========================================================

# Connections.Gaps.TwoNodes

## Wrapper Macro

ConnectGap_2Nodes(...)

## Ribbon-GUI-Location

Connections > Gaps > TwoNodes

## Command Description

create gap connection

## Argument List

**Arg1: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg2: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg3: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg4: iOriMode**

Description: option for orient mode

Data Type: integer

Default Value : 0

Syntax: iOriMode = 1

**Arg5: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg6: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg7: dU0**

Description: double value of u0

Data Type: double

Default Value : DFLT_DBL

Syntax: dU0 = 1.0

**Arg8: dF0**

Description: double value of f0

Data Type: double

Default Value : DFLT_DBL

Syntax: dF0 = 1.0

**Arg9: dKa**

Description: double value of ka

Data Type: double

Default Value : DFLT_DBL

Syntax: dKa = 1.0

**Arg10: dKb**

Description: double value of kb

Data Type: double

Default Value : DFLT_DBL

Syntax: dKb = 1.0

**Arg11: dKt**

Description: double value of kt

Data Type: double

Default Value : DFLT_DBL

Syntax: dKt = 1.0

**Arg12: dMar**

Description: double value of mar

Data Type: double

Default Value : DFLT_DBL

Syntax: dMar = 1.0

**Arg13: dMu1**

Description: double value of mu1

Data Type: double

Default Value : DFLT_DBL

Syntax: dMu1 = 1.0

**Arg14: dMu2**

Description: double value of mu2

Data Type: double

Default Value : DFLT_DBL

Syntax: dMu2 = 1.0

**Arg15: dlOriVec**

Description: array double values of orient vec

Data Type: double list

Default Value : []

Syntax: dlOriVec = [1.0, 2.0]

**Arg16: dTmax**

Description: double value of tmax

Data Type: double

Default Value : DFLT_DBL

Syntax: dTmax = 1.0

**Arg17: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg18: dTrmin**

Description: double value of trmin

Data Type: double

Default Value : DFLT_DBL

Syntax: dTrmin = 1.0

**Arg19: crEditCur**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEditCur = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Gaps.TwoNodes(crlMaster=[], crlSlave=[], iMethod=1, iOriMode=0, crCoord=None, strName="", dU0=DFLT_DBL, dF0=DFLT_DBL, dKa=DFLT_DBL, dKb=DFLT_DBL, dKt=DFLT_DBL, dMar=DFLT_DBL, dMu1=DFLT_DBL, dMu2=DFLT_DBL, dlOriVec=[], dTmax=DFLT_DBL, dTol=DFLT_DBL, dTrmin=DFLT_DBL, crEditCur=None)

```

==========================================================

# Connections.Gaps.TwoEdges

## Wrapper Macro

ConnectGap_2Edges(...)

## Ribbon-GUI-Location

Connections > Gaps > TwoEdges

## Command Description

create gap connection

## Argument List

**Arg1: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg2: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg3: iMethod**

Description: option for method

Data Type: integer

Default Value : 2

Syntax: iMethod = 1

**Arg4: iOriMode**

Description: option for orient mode

Data Type: integer

Default Value : 0

Syntax: iOriMode = 1

**Arg5: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg6: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg7: dU0**

Description: double value of u0

Data Type: double

Default Value : DFLT_DBL

Syntax: dU0 = 1.0

**Arg8: dF0**

Description: double value of f0

Data Type: double

Default Value : DFLT_DBL

Syntax: dF0 = 1.0

**Arg9: dKa**

Description: double value of ka

Data Type: double

Default Value : DFLT_DBL

Syntax: dKa = 1.0

**Arg10: dKb**

Description: double value of kb

Data Type: double

Default Value : DFLT_DBL

Syntax: dKb = 1.0

**Arg11: dKt**

Description: double value of kt

Data Type: double

Default Value : DFLT_DBL

Syntax: dKt = 1.0

**Arg12: dMar**

Description: double value of mar

Data Type: double

Default Value : DFLT_DBL

Syntax: dMar = 1.0

**Arg13: dMu1**

Description: double value of mu1

Data Type: double

Default Value : DFLT_DBL

Syntax: dMu1 = 1.0

**Arg14: dMu2**

Description: double value of mu2

Data Type: double

Default Value : DFLT_DBL

Syntax: dMu2 = 1.0

**Arg15: dlOriVec**

Description: array double values of orient vec

Data Type: double list

Default Value : []

Syntax: dlOriVec = [1.0, 2.0]

**Arg16: dTmax**

Description: double value of tmax

Data Type: double

Default Value : DFLT_DBL

Syntax: dTmax = 1.0

**Arg17: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg18: dTrmin**

Description: double value of trmin

Data Type: double

Default Value : DFLT_DBL

Syntax: dTrmin = 1.0

**Arg19: crEditCur**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEditCur = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Gaps.TwoEdges(crlMaster=[], crlSlave=[], iMethod=2, iOriMode=0, crCoord=None, strName="", dU0=DFLT_DBL, dF0=DFLT_DBL, dKa=DFLT_DBL, dKb=DFLT_DBL, dKt=DFLT_DBL, dMar=DFLT_DBL, dMu1=DFLT_DBL, dMu2=DFLT_DBL, dlOriVec=[], dTmax=DFLT_DBL, dTol=DFLT_DBL, dTrmin=DFLT_DBL, crEditCur=None)

```

==========================================================

# Connections.Gaps.TwoFaces

## Wrapper Macro

ConnectGap_2Faces(...)

## Ribbon-GUI-Location

Connections > Gaps > TwoFaces

## Command Description

create gap connection

## Argument List

**Arg1: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg2: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg3: iMethod**

Description: option for method

Data Type: integer

Default Value : 3

Syntax: iMethod = 1

**Arg4: iOriMode**

Description: option for orient mode

Data Type: integer

Default Value : 0

Syntax: iOriMode = 1

**Arg5: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg6: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg7: dU0**

Description: double value of u0

Data Type: double

Default Value : DFLT_DBL

Syntax: dU0 = 1.0

**Arg8: dF0**

Description: double value of f0

Data Type: double

Default Value : DFLT_DBL

Syntax: dF0 = 1.0

**Arg9: dKa**

Description: double value of ka

Data Type: double

Default Value : DFLT_DBL

Syntax: dKa = 1.0

**Arg10: dKb**

Description: double value of kb

Data Type: double

Default Value : DFLT_DBL

Syntax: dKb = 1.0

**Arg11: dKt**

Description: double value of kt

Data Type: double

Default Value : DFLT_DBL

Syntax: dKt = 1.0

**Arg12: dMar**

Description: double value of mar

Data Type: double

Default Value : DFLT_DBL

Syntax: dMar = 1.0

**Arg13: dMu1**

Description: double value of mu1

Data Type: double

Default Value : DFLT_DBL

Syntax: dMu1 = 1.0

**Arg14: dMu2**

Description: double value of mu2

Data Type: double

Default Value : DFLT_DBL

Syntax: dMu2 = 1.0

**Arg15: dlOriVec**

Description: array double values of orient vec

Data Type: double list

Default Value : []

Syntax: dlOriVec = [1.0, 2.0]

**Arg16: dTmax**

Description: double value of tmax

Data Type: double

Default Value : DFLT_DBL

Syntax: dTmax = 1.0

**Arg17: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg18: dTrmin**

Description: double value of trmin

Data Type: double

Default Value : DFLT_DBL

Syntax: dTrmin = 1.0

**Arg19: crEditCur**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEditCur = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.Gaps.TwoFaces(crlMaster=[], crlSlave=[], iMethod=3, iOriMode=0, crCoord=None, strName="", dU0=DFLT_DBL, dF0=DFLT_DBL, dKa=DFLT_DBL, dKb=DFLT_DBL, dKt=DFLT_DBL, dMar=DFLT_DBL, dMu1=DFLT_DBL, dMu2=DFLT_DBL, dlOriVec=[], dTmax=DFLT_DBL, dTol=DFLT_DBL, dTrmin=DFLT_DBL, crEditCur=None)

```

==========================================================

# Connections.MPC.Equation.MultiNodes

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > Equation > MultiNodes

## Command Description

Command use for Connections MPC Equation MultiNodes

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.Equation.MultiNodes(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.Equation.TwoFace

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > Equation > TwoFace

## Command Description

Command use for Connections MPC Equation TwoFace

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.Equation.TwoFace(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.Equation.SemiAuto

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > Equation > SemiAuto

## Command Description

Command use for Connections MPC Equation SemiAuto

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.Equation.SemiAuto(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.General.NodeToNode

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > General > NodeToNode

## Command Description

Command use for Connections MPC General NodeToNode

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.General.NodeToNode(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.General.NodeToEdges

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > General > NodeToEdges

## Command Description

Command use for Connections MPC General NodeToEdges

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.General.NodeToEdges(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.General.NodeToFaces

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > General > NodeToFaces

## Command Description

Command use for Connections MPC General NodeToFaces

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.General.NodeToFaces(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.General.TwoEdges

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > General > TwoEdges

## Command Description

Command use for Connections MPC General TwoEdges

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.General.TwoEdges(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.General.FacesToFaces

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > General > FacesToFaces

## Command Description

Command use for Connections MPC General FacesToFaces

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.General.FacesToFaces(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.General.NodesToNodes

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > General > NodesToNodes

## Command Description

Command use for Connections MPC General NodesToNodes

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.General.NodesToNodes(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.General.TwoFaces

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > General > TwoFaces

## Command Description

Command use for Connections MPC General TwoFaces

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.General.TwoFaces(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.General.NodeToAny

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > General > NodeToAny

## Command Description

Command use for Connections MPC General NodeToAny

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.General.NodeToAny(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.MPC.General.NodesWithTolerance

## Wrapper Macro

Mpc(...)

## Ribbon-GUI-Location

Connections > MPC > General > NodesWithTolerance

## Command Description

Command use for Connections MPC General NodesWithTolerance

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "MPC_1"

Syntax: strName = "string input"

**Arg2: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg3: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg4: listMpcConnection**

Description: list data structure of MPC_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: MPC_CONNECTION

Default Value : []

Syntax: listMpcConnection = [MPC_CONNECTION(...),MPC_CONNECTION(...)]

**Arg5: dSearchTol**

Description: double value of search tolerance

Data Type: double

Default Value : 0.0

Syntax: dSearchTol = 1.0

**Arg6: dValue**

Description: double value of value

Data Type: double

Default Value : 0.0

Syntax: dValue = 1.0

**Arg7: iMPCType**

Description: option for m p c type

Data Type: integer

Default Value : 0

Syntax: iMPCType = 1

**Arg8: iSearchType**

Description: option for search type

Data Type: integer

Default Value : 1

Syntax: iSearchType = 1

**Arg9: iCoordSys**

Description: option for coordinate sys

Data Type: integer

Default Value : 0

Syntax: iCoordSys = 1

**Arg10: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg11: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.MPC.General.NodesWithTolerance(strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.RigidElements.RBar.OneToOne

## Wrapper Macro

RBarOneToOne(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBar > OneToOne

## Command Description

create RBar

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "RBAR_1"

Syntax: strName = "string input"

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 17

Syntax: iMethod = 1

**Arg5: iUlDOFs**

Description: option for ul d o fs

Data Type: integer

Default Value : 0

Syntax: iUlDOFs = 1

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBar.OneToOne(strName="RBAR_1", crlMasterTarget=[], crlSlaveTarget=[], iMethod=17, iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)

```

==========================================================

# Connections.RigidElements.RBar.OneToMany

## Wrapper Macro

RBarOneToMany(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBar > OneToMany

## Command Description

create RBar

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "RBAR_1"

Syntax: strName = "string input"

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 16

Syntax: iMethod = 1

**Arg5: iUlDOFs**

Description: option for ul d o fs

Data Type: integer

Default Value : 0

Syntax: iUlDOFs = 1

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBar.OneToMany(strName="RBAR_1", crlMasterTarget=[], crlSlaveTarget=[], iMethod=16, iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)

```

==========================================================

# Connections.RigidElements.RBar.OneToOneNodesWithTolerance

## Wrapper Macro

RBarOneToOneNodesWithTolerance(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBar > OneToOneNodesWithTolerance

## Command Description

create RBar

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : "RBAR_1"

Syntax: strName = "string input"

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 21

Syntax: iMethod = 1

**Arg5: iUlDOFs**

Description: option for ul d o fs

Data Type: integer

Default Value : 0

Syntax: iUlDOFs = 1

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg7: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg8: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBar.OneToOneNodesWithTolerance(strName="RBAR_1", crlMasterTarget=[], crlSlaveTarget=[], iMethod=21, iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)

```

==========================================================

# Connections.RigidElements.RBE2.OneToMany

## Wrapper Macro

RBE2OneToMany(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE2 > OneToMany

## Command Description

create RBE2

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 16

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: iEType**

Description: option for e type

Data Type: integer

Default Value : 2

Syntax: iEType = 1

**Arg5: strName**

Description: definition string of input name

Data Type: string

Default Value : "RBE2_1"

Syntax: strName = "string input"

**Arg6: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg7: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg8: iUlDOFs**

Description: option for ul d o fs

Data Type: integer

Default Value : 63

Syntax: iUlDOFs = 1

**Arg9: dlVirtualNodePos**

Description: array double values of virtual node pos

Data Type: double list

Default Value : [0

Syntax: dlVirtualNodePos = [1.0, 2.0]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iEnableUpdateDispCS**

Description: option for enable update display coordinate system

Data Type: integer

Default Value : 1

Syntax: iEnableUpdateDispCS = 1

**Arg15: iEnableCornerOnly**

Description: option for enable corner only

Data Type: integer

Default Value : 0

Syntax: iEnableCornerOnly = 1

**Arg16: iEnableCheckDulplicate**

Description: option for enable check dulplicate

Data Type: integer

Default Value : 1

Syntax: iEnableCheckDulplicate = 1

**Arg17: iDuplicateMode**

Description: option for duplicate mode

Data Type: integer

Default Value : 0

Syntax: iDuplicateMode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE2.OneToMany(iMethod=16, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)

```

==========================================================

# Connections.RigidElements.RBE2.OneToOne

## Wrapper Macro

RBE2OneToOne(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE2 > OneToOne

## Command Description

create RBE2

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 17

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: iEType**

Description: option for e type

Data Type: integer

Default Value : 2

Syntax: iEType = 1

**Arg5: strName**

Description: definition string of input name

Data Type: string

Default Value : "RBE2_1"

Syntax: strName = "string input"

**Arg6: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg7: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg8: iUlDOFs**

Description: option for ul d o fs

Data Type: integer

Default Value : 63

Syntax: iUlDOFs = 1

**Arg9: dlVirtualNodePos**

Description: array double values of virtual node pos

Data Type: double list

Default Value : [0

Syntax: dlVirtualNodePos = [1.0, 2.0]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iEnableUpdateDispCS**

Description: option for enable update display coordinate system

Data Type: integer

Default Value : 1

Syntax: iEnableUpdateDispCS = 1

**Arg15: iEnableCornerOnly**

Description: option for enable corner only

Data Type: integer

Default Value : 0

Syntax: iEnableCornerOnly = 1

**Arg16: iEnableCheckDulplicate**

Description: option for enable check dulplicate

Data Type: integer

Default Value : 1

Syntax: iEnableCheckDulplicate = 1

**Arg17: iDuplicateMode**

Description: option for duplicate mode

Data Type: integer

Default Value : 0

Syntax: iDuplicateMode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE2.OneToOne(iMethod=17, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)

```

==========================================================

# Connections.RigidElements.RBE2.OneToOneNodesWithTolerance

## Wrapper Macro

RBE2OneToOneNodesWithTolerance(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE2 > OneToOneNodesWithTolerance

## Command Description

create RBE2

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 21

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: iEType**

Description: option for e type

Data Type: integer

Default Value : 2

Syntax: iEType = 1

**Arg5: strName**

Description: definition string of input name

Data Type: string

Default Value : "RBE2_1"

Syntax: strName = "string input"

**Arg6: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg7: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg8: iUlDOFs**

Description: option for ul d o fs

Data Type: integer

Default Value : 63

Syntax: iUlDOFs = 1

**Arg9: dlVirtualNodePos**

Description: array double values of virtual node pos

Data Type: double list

Default Value : [0

Syntax: dlVirtualNodePos = [1.0, 2.0]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iEnableUpdateDispCS**

Description: option for enable update display coordinate system

Data Type: integer

Default Value : 1

Syntax: iEnableUpdateDispCS = 1

**Arg15: iEnableCornerOnly**

Description: option for enable corner only

Data Type: integer

Default Value : 0

Syntax: iEnableCornerOnly = 1

**Arg16: iEnableCheckDulplicate**

Description: option for enable check dulplicate

Data Type: integer

Default Value : 1

Syntax: iEnableCheckDulplicate = 1

**Arg17: iDuplicateMode**

Description: option for duplicate mode

Data Type: integer

Default Value : 0

Syntax: iDuplicateMode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE2.OneToOneNodesWithTolerance(iMethod=21, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)

```

==========================================================

# Connections.RigidElements.RBE2.ToCenter

## Wrapper Macro

RBE2ToCenter(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE2 > ToCenter

## Command Description

create RBE2

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 18

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: iEType**

Description: option for e type

Data Type: integer

Default Value : 2

Syntax: iEType = 1

**Arg5: strName**

Description: definition string of input name

Data Type: string

Default Value : "RBE2_1"

Syntax: strName = "string input"

**Arg6: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg7: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg8: iUlDOFs**

Description: option for ul d o fs

Data Type: integer

Default Value : 63

Syntax: iUlDOFs = 1

**Arg9: dlVirtualNodePos**

Description: array double values of virtual node pos

Data Type: double list

Default Value : [0

Syntax: dlVirtualNodePos = [1.0, 2.0]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iEnableUpdateDispCS**

Description: option for enable update display coordinate system

Data Type: integer

Default Value : 1

Syntax: iEnableUpdateDispCS = 1

**Arg15: iEnableCornerOnly**

Description: option for enable corner only

Data Type: integer

Default Value : 0

Syntax: iEnableCornerOnly = 1

**Arg16: iEnableCheckDulplicate**

Description: option for enable check dulplicate

Data Type: integer

Default Value : 1

Syntax: iEnableCheckDulplicate = 1

**Arg17: iDuplicateMode**

Description: option for duplicate mode

Data Type: integer

Default Value : 0

Syntax: iDuplicateMode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE2.ToCenter(iMethod=18, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)

```

==========================================================

# Connections.RigidElements.RBE2.ToCircleCenter

## Wrapper Macro

RBE2ToCircleCenter(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE2 > ToCircleCenter

## Command Description

create RBE2

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 19

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: iEType**

Description: option for e type

Data Type: integer

Default Value : 2

Syntax: iEType = 1

**Arg5: strName**

Description: definition string of input name

Data Type: string

Default Value : "RBE2_1"

Syntax: strName = "string input"

**Arg6: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg7: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg8: iUlDOFs**

Description: option for ul d o fs

Data Type: integer

Default Value : 63

Syntax: iUlDOFs = 1

**Arg9: dlVirtualNodePos**

Description: array double values of virtual node pos

Data Type: double list

Default Value : [0

Syntax: dlVirtualNodePos = [1.0, 2.0]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iEnableUpdateDispCS**

Description: option for enable update display coordinate system

Data Type: integer

Default Value : 1

Syntax: iEnableUpdateDispCS = 1

**Arg15: iEnableCornerOnly**

Description: option for enable corner only

Data Type: integer

Default Value : 0

Syntax: iEnableCornerOnly = 1

**Arg16: iEnableCheckDulplicate**

Description: option for enable check dulplicate

Data Type: integer

Default Value : 1

Syntax: iEnableCheckDulplicate = 1

**Arg17: iDuplicateMode**

Description: option for duplicate mode

Data Type: integer

Default Value : 0

Syntax: iDuplicateMode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE2.ToCircleCenter(iMethod=19, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0)

```

==========================================================

# Connections.RigidElements.RBE3.OneToMany

## Wrapper Macro

RBE3OneToMany(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE3 > OneToMany

## Command Description

Create RBE3

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 16

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: listRbe3TermConnection**

Description: list data structure of RBE3_TERM_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: RBE3_TERM_CONNECTION

Default Value : RBE3_TERM_CONNECTION()

Syntax: listRbe3TermConnection = [RBE3_TERM_CONNECTION(,,,), RBE3_TERM_CONNECTION(,,,)]

**Arg5: iTypeRBE3**

Description: option for type r b e3

Data Type: integer

Default Value : 3

Syntax: iTypeRBE3 = 1

**Arg6: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg7: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg9: dlVirtualNodePos**

Description: array double values of virtual node pos

Data Type: double list

Default Value : [0

Syntax: dlVirtualNodePos = [1.0, 2.0]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iEnableUpdateDispCS**

Description: option for enable update display coordinate system

Data Type: integer

Default Value : True

Syntax: iEnableUpdateDispCS = 1

**Arg15: iEnableCornerOnly**

Description: option for enable corner only

Data Type: integer

Default Value : False

Syntax: iEnableCornerOnly = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE3.OneToMany(iMethod=16, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)

```

==========================================================

# Connections.RigidElements.RBE3.OneToOne

## Wrapper Macro

RBE3OneToOne(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE3 > OneToOne

## Command Description

Create RBE3

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 17

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: listRbe3TermConnection**

Description: list data structure of RBE3_TERM_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: RBE3_TERM_CONNECTION

Default Value : RBE3_TERM_CONNECTION()

Syntax: listRbe3TermConnection = [RBE3_TERM_CONNECTION(,,,), RBE3_TERM_CONNECTION(,,,)]

**Arg5: iTypeRBE3**

Description: option for type r b e3

Data Type: integer

Default Value : 3

Syntax: iTypeRBE3 = 1

**Arg6: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg7: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg9: dlVirtualNodePos**

Description: array double values of virtual node pos

Data Type: double list

Default Value : [0

Syntax: dlVirtualNodePos = [1.0, 2.0]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iEnableUpdateDispCS**

Description: option for enable update display coordinate system

Data Type: integer

Default Value : True

Syntax: iEnableUpdateDispCS = 1

**Arg15: iEnableCornerOnly**

Description: option for enable corner only

Data Type: integer

Default Value : False

Syntax: iEnableCornerOnly = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE3.OneToOne(iMethod=17, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)

```

==========================================================

# Connections.RigidElements.RBE3.ToCenter

## Wrapper Macro

RBE3ToCenter(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE3 > ToCenter

## Command Description

Create RBE3

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 18

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: listRbe3TermConnection**

Description: list data structure of RBE3_TERM_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: RBE3_TERM_CONNECTION

Default Value : RBE3_TERM_CONNECTION()

Syntax: listRbe3TermConnection = [RBE3_TERM_CONNECTION(,,,), RBE3_TERM_CONNECTION(,,,)]

**Arg5: iTypeRBE3**

Description: option for type r b e3

Data Type: integer

Default Value : 3

Syntax: iTypeRBE3 = 1

**Arg6: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg7: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg9: dlVirtualNodePos**

Description: array double values of virtual node pos

Data Type: double list

Default Value : [0

Syntax: dlVirtualNodePos = [1.0, 2.0]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iEnableUpdateDispCS**

Description: option for enable update display coordinate system

Data Type: integer

Default Value : True

Syntax: iEnableUpdateDispCS = 1

**Arg15: iEnableCornerOnly**

Description: option for enable corner only

Data Type: integer

Default Value : False

Syntax: iEnableCornerOnly = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE3.ToCenter(iMethod=18, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)

```

==========================================================

# Connections.RigidElements.RBE3.ToCircleCenter

## Wrapper Macro

RBE3ToCircleCenter(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE3 > ToCircleCenter

## Command Description

Create RBE3

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 19

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: listRbe3TermConnection**

Description: list data structure of RBE3_TERM_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: RBE3_TERM_CONNECTION

Default Value : RBE3_TERM_CONNECTION()

Syntax: listRbe3TermConnection = [RBE3_TERM_CONNECTION(,,,), RBE3_TERM_CONNECTION(,,,)]

**Arg5: iTypeRBE3**

Description: option for type r b e3

Data Type: integer

Default Value : 3

Syntax: iTypeRBE3 = 1

**Arg6: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg7: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg9: dlVirtualNodePos**

Description: array double values of virtual node pos

Data Type: double list

Default Value : [0

Syntax: dlVirtualNodePos = [1.0, 2.0]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iEnableUpdateDispCS**

Description: option for enable update display coordinate system

Data Type: integer

Default Value : True

Syntax: iEnableUpdateDispCS = 1

**Arg15: iEnableCornerOnly**

Description: option for enable corner only

Data Type: integer

Default Value : False

Syntax: iEnableCornerOnly = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE3.ToCircleCenter(iMethod=19, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False)

```

==========================================================

# Connections.RigidElements.RBarGeneral

## Wrapper Macro

RBar(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBarGeneral

## Command Description

Command use for Connections RigidElements RBarGeneral

## Argument List

**Arg1: rbarConnection**

Description: data structure of RBAR_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: RBAR_CONNECTION

Default Value : RBAR_CONNECTION()

Syntax: rbarConnection = RBAR_CONNECTION(,,,)

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: iUlDOFs**

Description: option for ul d o fs

Data Type: integer

Default Value : 0

Syntax: iUlDOFs = 1

**Arg5: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg6: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBarGeneral(rbarConnection=RBAR_CONNECTION(), crlMasterTarget=[], crlSlaveTarget=[], iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None)

```

==========================================================

# Connections.RigidElements.RBE2General

## Wrapper Macro

Rbe2(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE2General

## Command Description

Command use for Connections RigidElements RBE2General

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: iEType**

Description: option for e type

Data Type: integer

Default Value : 2

Syntax: iEType = 1

**Arg5: strName**

Description: definition string of input name

Data Type: string

Default Value : "RBE2_1"

Syntax: strName = "string input"

**Arg6: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg7: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg8: iUlDOFs**

Description: option for ul d o fs

Data Type: integer

Default Value : 63

Syntax: iUlDOFs = 1

**Arg9: dlVirtualNodePos**

Description: array double values of virtual node pos

Data Type: double list

Default Value : [0

Syntax: dlVirtualNodePos = [1.0, 2.0]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iEnableUpdateDispCS**

Description: option for enable update display coordinate system

Data Type: integer

Default Value : 1

Syntax: iEnableUpdateDispCS = 1

**Arg15: iEnableCornerOnly**

Description: option for enable corner only

Data Type: integer

Default Value : 0

Syntax: iEnableCornerOnly = 1

**Arg16: iDuplicateMode**

Description: option for duplicate mode

Data Type: integer

Default Value : -1

Syntax: iDuplicateMode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE2General(iMethod=0, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iDuplicateMode=-1)

```

==========================================================

# Connections.RigidElements.RBE3General

## Wrapper Macro

Rbe3(...)

## Ribbon-GUI-Location

Connections > RigidElements > RBE3General

## Command Description

Command use for Connections RigidElements RBE3General

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg3: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg4: listRbe3TermConnection**

Description: list data structure of RBE3_TERM_CONNECTION (refer PSJ Command Data Structure Document)

Data Type: RBE3_TERM_CONNECTION

Default Value : RBE3_TERM_CONNECTION()

Syntax: listRbe3TermConnection = [RBE3_TERM_CONNECTION(,,,), RBE3_TERM_CONNECTION(,,,)]

**Arg5: iTypeRBE3**

Description: option for type r b e3

Data Type: integer

Default Value : 3

Syntax: iTypeRBE3 = 1

**Arg6: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg7: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg9: posVirtualNodePos**

Description: array double value [x, y, z] in coordinate system of virtual node pos

Data Type: position

Default Value : [0

Syntax: posVirtualNodePos = [x, y, z]

**Arg12: iSurfaceDef**

Description: option for surface def

Data Type: integer

Default Value : 0

Syntax: iSurfaceDef = 1

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg15: bCornerOnly**

Description: enable or disable feature corner only

Data Type: bool

Default Value : False

Syntax: bCornerOnly = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.RigidElements.RBE3General(iMethod=0, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, posVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, bUpdateDispCS=True, bCornerOnly=False)

```

==========================================================

# Connections.SpringsDampers.Damper.AnyEntities11DoFS

## Wrapper Macro

Damper(...)

## Ribbon-GUI-Location

Connections > SpringsDampers > Damper > AnyEntities11DoFS

## Command Description

Create Damper Connection

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg3: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg4: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg5: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg6: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg7: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0

Syntax: dTolerance = 1.0

**Arg8: vecTDamper**

Description: array values of t damper

Data Type: vector

Default Value : [0

Syntax: vecTDamper = [value1, value2, value3]

**Arg11: vecRDamper**

Description: array values of r damper

Data Type: vector

Default Value : [0

Syntax: vecRDamper = [value1, value2, value3]

**Arg14: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg15: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.SpringsDampers.Damper.AnyEntities11DoFS(iMethod=0, strName="", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iGround=0, dTolerance=0.0, vecTDamper=[0, 0, 0], vecRDamper=[0, 0, 0], crEdit=None, bUpdateDispCS=True)

```

==========================================================

# Connections.SpringsDampers.BushGeneral

## Wrapper Macro

Bush(...)

## Ribbon-GUI-Location

Connections > SpringsDampers > BushGeneral

## Command Description

Command use for Connections SpringsDampers BushGeneral

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg3: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg4: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg5: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTol = 1.0

**Arg7: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg8: iOriMode**

Description: option for orient mode

Data Type: integer

Default Value : 0

Syntax: iOriMode = 1

**Arg9: iEqual**

Description: option for equal

Data Type: integer

Default Value : 0

Syntax: iEqual = 1

**Arg10: poslVector**

Description: list positions [x, y, z] in coordinate system

Data Type: position list

Default Value : [[]]

Syntax: poslVector = [[x, y, z], [x, y, z]]

**Arg11: dlStiffness**

Description: array double values of stiffness

Data Type: double list

Default Value : []

Syntax: dlStiffness = [1.0, 2.0]

**Arg12: dlDampCoef**

Description: array double values of damper coefficient

Data Type: double list

Default Value : []

Syntax: dlDampCoef = [1.0, 2.0]

**Arg13: dlDampConst**

Description: array double values of damper const

Data Type: double list

Default Value : []

Syntax: dlDampConst = [1.0, 2.0]

**Arg14: dRotStrain**

Description: double value of rotation strain

Data Type: double

Default Value : 0.0

Syntax: dRotStrain = 1.0

**Arg15: dTransStrain**

Description: double value of translation strain

Data Type: double

Default Value : 0.0

Syntax: dTransStrain = 1.0

**Arg16: dRotStress**

Description: double value of rotation stress

Data Type: double

Default Value : 0.0

Syntax: dRotStress = 1.0

**Arg17: dTransStress**

Description: double value of translation stress

Data Type: double

Default Value : 0.0

Syntax: dTransStress = 1.0

**Arg18: crEditObj**

Description: entity in database model to edit obj

Data Type: cursor

Default Value : None

Syntax: crEditObj = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.SpringsDampers.BushGeneral(iMethod=0, strName="", crlMaster=[], crlSlave=[], crCoord=None, dTol=0.0, iGround=0, iOriMode=0, iEqual=0, poslVector=[[]], dlStiffness=[], dlDampCoef=[], dlDampConst=[], dRotStrain=0.0, dTransStrain=0.0, dRotStress=0.0, dTransStress=0.0, crEditObj=None)

```

==========================================================

# Connections.SpringsDampers.Bush.TwoNodes

## Wrapper Macro

ConnBush_2Nodes(...)

## Ribbon-GUI-Location

Connections > SpringsDampers > Bush > TwoNodes

## Command Description

Create bush connection

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 1

Syntax: iMethod = 1

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "BUSH_1"

Syntax: strName = "string input"

**Arg3: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg4: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg5: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg7: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg8: iOriMode**

Description: option for orient mode

Data Type: integer

Default Value : 0

Syntax: iOriMode = 1

**Arg9: iEqual**

Description: option for equal

Data Type: integer

Default Value : 1

Syntax: iEqual = 1

**Arg10: poslVector**

Description: list positions [x, y, z] in coordinate system

Data Type: position list

Default Value : []

Syntax: poslVector = [[x, y, z], [x, y, z]]

**Arg11: dlStiffness**

Description: array double values of stiffness

Data Type: double list

Default Value : []

Syntax: dlStiffness = [1.0, 2.0]

**Arg12: dlDampCoef**

Description: array double values of damper coefficient

Data Type: double list

Default Value : []

Syntax: dlDampCoef = [1.0, 2.0]

**Arg13: dlDampConst**

Description: array double values of damper const

Data Type: double list

Default Value : []

Syntax: dlDampConst = [1.0, 2.0]

**Arg14: dRotStrain**

Description: double value of rotation strain

Data Type: double

Default Value : DFLT_DBL

Syntax: dRotStrain = 1.0

**Arg15: dTransStrain**

Description: double value of translation strain

Data Type: double

Default Value : DFLT_DBL

Syntax: dTransStrain = 1.0

**Arg16: dRotStress**

Description: double value of rotation stress

Data Type: double

Default Value : DFLT_DBL

Syntax: dRotStress = 1.0

**Arg17: dTransStress**

Description: double value of translation stress

Data Type: double

Default Value : DFLT_DBL

Syntax: dTransStress = 1.0

**Arg18: crEditObj**

Description: entity in database model to edit obj

Data Type: cursor

Default Value : None

Syntax: crEditObj = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.SpringsDampers.Bush.TwoNodes(iMethod=1, strName="BUSH_1", crlMaster=[], crlSlave=[], crCoord=None, dTol=DFLT_DBL, iGround=0, iOriMode=0, iEqual=1, poslVector=[], dlStiffness=[], dlDampCoef=[], dlDampConst=[], dRotStrain=DFLT_DBL, dTransStrain=DFLT_DBL, dRotStress=DFLT_DBL, dTransStress=DFLT_DBL, crEditObj=None)

```

==========================================================

# Connections.SpringsDampers.Bush.AnyEntities

## Wrapper Macro

ConnBush_AnyEntity(...)

## Ribbon-GUI-Location

Connections > SpringsDampers > Bush > AnyEntities

## Command Description

Create bush connection

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 16

Syntax: iMethod = 1

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "BUSH_1"

Syntax: strName = "string input"

**Arg3: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg4: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg5: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg7: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg8: iOriMode**

Description: option for orient mode

Data Type: integer

Default Value : 0

Syntax: iOriMode = 1

**Arg9: iEqual**

Description: option for equal

Data Type: integer

Default Value : 1

Syntax: iEqual = 1

**Arg10: poslVector**

Description: list positions [x, y, z] in coordinate system

Data Type: position list

Default Value : []

Syntax: poslVector = [[x, y, z], [x, y, z]]

**Arg11: dlStiffness**

Description: array double values of stiffness

Data Type: double list

Default Value : []

Syntax: dlStiffness = [1.0, 2.0]

**Arg12: dlDampCoef**

Description: array double values of damper coefficient

Data Type: double list

Default Value : []

Syntax: dlDampCoef = [1.0, 2.0]

**Arg13: dlDampConst**

Description: array double values of damper const

Data Type: double list

Default Value : []

Syntax: dlDampConst = [1.0, 2.0]

**Arg14: dRotStrain**

Description: double value of rotation strain

Data Type: double

Default Value : DFLT_DBL

Syntax: dRotStrain = 1.0

**Arg15: dTransStrain**

Description: double value of translation strain

Data Type: double

Default Value : DFLT_DBL

Syntax: dTransStrain = 1.0

**Arg16: dRotStress**

Description: double value of rotation stress

Data Type: double

Default Value : DFLT_DBL

Syntax: dRotStress = 1.0

**Arg17: dTransStress**

Description: double value of translation stress

Data Type: double

Default Value : DFLT_DBL

Syntax: dTransStress = 1.0

**Arg18: crEditObj**

Description: entity in database model to edit obj

Data Type: cursor

Default Value : None

Syntax: crEditObj = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.SpringsDampers.Bush.AnyEntities(iMethod=16, strName="BUSH_1", crlMaster=[], crlSlave=[], crCoord=None, dTol=DFLT_DBL, iGround=0, iOriMode=0, iEqual=1, poslVector=[], dlStiffness=[], dlDampCoef=[], dlDampConst=[], dRotStrain=DFLT_DBL, dTransStrain=DFLT_DBL, dRotStress=DFLT_DBL, dTransStress=DFLT_DBL, crEditObj=None)

```

==========================================================

# Connections.SpringsDampers.Bush.OnetoOne

## Wrapper Macro

ConnBush_OnetoOne(...)

## Ribbon-GUI-Location

Connections > SpringsDampers > Bush > OnetoOne

## Command Description

Create bush connection

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 21

Syntax: iMethod = 1

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "BUSH_1"

Syntax: strName = "string input"

**Arg3: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg4: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

**Arg5: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg6: dTol**

Description: double value of tolerance

Data Type: double

Default Value : DFLT_DBL

Syntax: dTol = 1.0

**Arg7: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg8: iOriMode**

Description: option for orient mode

Data Type: integer

Default Value : 0

Syntax: iOriMode = 1

**Arg9: iEqual**

Description: option for equal

Data Type: integer

Default Value : 1

Syntax: iEqual = 1

**Arg10: poslVector**

Description: list positions [x, y, z] in coordinate system

Data Type: position list

Default Value : []

Syntax: poslVector = [[x, y, z], [x, y, z]]

**Arg11: dlStiffness**

Description: array double values of stiffness

Data Type: double list

Default Value : []

Syntax: dlStiffness = [1.0, 2.0]

**Arg12: dlDampCoef**

Description: array double values of damper coefficient

Data Type: double list

Default Value : []

Syntax: dlDampCoef = [1.0, 2.0]

**Arg13: dlDampConst**

Description: array double values of damper const

Data Type: double list

Default Value : []

Syntax: dlDampConst = [1.0, 2.0]

**Arg14: dRotStrain**

Description: double value of rotation strain

Data Type: double

Default Value : DFLT_DBL

Syntax: dRotStrain = 1.0

**Arg15: dTransStrain**

Description: double value of translation strain

Data Type: double

Default Value : DFLT_DBL

Syntax: dTransStrain = 1.0

**Arg16: dRotStress**

Description: double value of rotation stress

Data Type: double

Default Value : DFLT_DBL

Syntax: dRotStress = 1.0

**Arg17: dTransStress**

Description: double value of translation stress

Data Type: double

Default Value : DFLT_DBL

Syntax: dTransStress = 1.0

**Arg18: crEditObj**

Description: entity in database model to edit obj

Data Type: cursor

Default Value : None

Syntax: crEditObj = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.SpringsDampers.Bush.OnetoOne(iMethod=21, strName="BUSH_1", crlMaster=[], crlSlave=[], crCoord=None, dTol=DFLT_DBL, iGround=0, iOriMode=0, iEqual=1, poslVector=[], dlStiffness=[], dlDampCoef=[], dlDampConst=[], dRotStrain=DFLT_DBL, dTransStrain=DFLT_DBL, dRotStress=DFLT_DBL, dTransStress=DFLT_DBL, crEditObj=None)

```

==========================================================

# Connections.SpringsDampers.Spring.GroundedSpring

## Wrapper Macro

SpringGrounded(...)

## Ribbon-GUI-Location

Connections > SpringsDampers > Spring > GroundedSpring

## Command Description

Grounded Spring connection

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "SPRING"

Syntax: strName = "string input"

**Arg3: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg4: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg5: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg6: iSpringType**

Description: option for spring type

Data Type: integer

Default Value : 0

Syntax: iSpringType = 1

**Arg7: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTolerance = 1.0

**Arg9: iDirection**

Description: option for direction

Data Type: integer

Default Value : 0

Syntax: iDirection = 1

**Arg10: iDistributeMode**

Description: option for distribute mode

Data Type: integer

Default Value : 0

Syntax: iDistributeMode = 1

**Arg11: iDof1**

Description: option for dof1

Data Type: integer

Default Value : 0

Syntax: iDof1 = 1

**Arg12: iDof2**

Description: option for dof2

Data Type: integer

Default Value : 0

Syntax: iDof2 = 1

**Arg13: dDampCoef**

Description: double value of damper coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dDampCoef = 1.0

**Arg14: dStressCoef**

Description: double value of stress coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dStressCoef = 1.0

**Arg15: posTStiffness**

Description: array double value [x, y, z] in coordinate system of t stiffness

Data Type: position

Default Value : [0,0,0]

Syntax: posTStiffness = [x, y, z]

**Arg16: posRStiffness**

Description: array double value [x, y, z] in coordinate system of r stiffness

Data Type: position

Default Value : [0,0,0]

Syntax: posRStiffness = [x, y, z]

**Arg17: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg18: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.SpringsDampers.Spring.GroundedSpring(iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.SpringsDampers.Spring.Nodeswithtolerance.sameDoFs

## Wrapper Macro

SpringNodesUniformDOFs(...)

## Ribbon-GUI-Location

Connections > SpringsDampers > Spring > Nodeswithtolerance > sameDoFs

## Command Description

Spring connection Nodes with tolerance same DOFs

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "SPRING"

Syntax: strName = "string input"

**Arg3: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg4: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg5: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg6: iSpringType**

Description: option for spring type

Data Type: integer

Default Value : 0

Syntax: iSpringType = 1

**Arg7: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTolerance = 1.0

**Arg9: iDirection**

Description: option for direction

Data Type: integer

Default Value : 0

Syntax: iDirection = 1

**Arg10: iDistributeMode**

Description: option for distribute mode

Data Type: integer

Default Value : 0

Syntax: iDistributeMode = 1

**Arg11: iDof1**

Description: option for dof1

Data Type: integer

Default Value : 0

Syntax: iDof1 = 1

**Arg12: iDof2**

Description: option for dof2

Data Type: integer

Default Value : 0

Syntax: iDof2 = 1

**Arg13: dDampCoef**

Description: double value of damper coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dDampCoef = 1.0

**Arg14: dStressCoef**

Description: double value of stress coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dStressCoef = 1.0

**Arg15: posTStiffness**

Description: array double value [x, y, z] in coordinate system of t stiffness

Data Type: position

Default Value : [0,0,0]

Syntax: posTStiffness = [x, y, z]

**Arg16: posRStiffness**

Description: array double value [x, y, z] in coordinate system of r stiffness

Data Type: position

Default Value : [0,0,0]

Syntax: posRStiffness = [x, y, z]

**Arg17: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg18: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.SpringsDampers.Spring.Nodeswithtolerance.sameDoFs(iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.SpringsDampers.Spring.Nodeswithtolerance.differentDoFs

## Wrapper Macro

SpringNodesDOFs(...)

## Ribbon-GUI-Location

Connections > SpringsDampers > Spring > Nodeswithtolerance > differentDoFs

## Command Description

Spring connection Nodes with tolerance different DOFs

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "SPRING"

Syntax: strName = "string input"

**Arg3: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg4: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg5: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg6: iSpringType**

Description: option for spring type

Data Type: integer

Default Value : 0

Syntax: iSpringType = 1

**Arg7: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTolerance = 1.0

**Arg9: iDirection**

Description: option for direction

Data Type: integer

Default Value : 0

Syntax: iDirection = 1

**Arg10: iDistributeMode**

Description: option for distribute mode

Data Type: integer

Default Value : 0

Syntax: iDistributeMode = 1

**Arg11: iDof1**

Description: option for dof1

Data Type: integer

Default Value : 0

Syntax: iDof1 = 1

**Arg12: iDof2**

Description: option for dof2

Data Type: integer

Default Value : 0

Syntax: iDof2 = 1

**Arg13: dDampCoef**

Description: double value of damper coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dDampCoef = 1.0

**Arg14: dStressCoef**

Description: double value of stress coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dStressCoef = 1.0

**Arg15: posTStiffness**

Description: array double value [x, y, z] in coordinate system of t stiffness

Data Type: position

Default Value : [0,0,0]

Syntax: posTStiffness = [x, y, z]

**Arg16: posRStiffness**

Description: array double value [x, y, z] in coordinate system of r stiffness

Data Type: position

Default Value : [0,0,0]

Syntax: posRStiffness = [x, y, z]

**Arg17: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg18: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.SpringsDampers.Spring.Nodeswithtolerance.differentDoFs(iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.SpringsDampers.Spring.OneToOne.sameDoFs

## Wrapper Macro

SpringOneToOneUniformDOFs(...)

## Ribbon-GUI-Location

Connections > SpringsDampers > Spring > OneToOne > sameDoFs

## Command Description

Spring connection One to One same DOFs

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "SPRING"

Syntax: strName = "string input"

**Arg3: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg4: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg5: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg6: iSpringType**

Description: option for spring type

Data Type: integer

Default Value : 0

Syntax: iSpringType = 1

**Arg7: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTolerance = 1.0

**Arg9: iDirection**

Description: option for direction

Data Type: integer

Default Value : 0

Syntax: iDirection = 1

**Arg10: iDistributeMode**

Description: option for distribute mode

Data Type: integer

Default Value : 0

Syntax: iDistributeMode = 1

**Arg11: iDof1**

Description: option for dof1

Data Type: integer

Default Value : 0

Syntax: iDof1 = 1

**Arg12: iDof2**

Description: option for dof2

Data Type: integer

Default Value : 0

Syntax: iDof2 = 1

**Arg13: dDampCoef**

Description: double value of damper coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dDampCoef = 1.0

**Arg14: dStressCoef**

Description: double value of stress coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dStressCoef = 1.0

**Arg15: posTStiffness**

Description: array double value [x, y, z] in coordinate system of t stiffness

Data Type: position

Default Value : [0,0,0]

Syntax: posTStiffness = [x, y, z]

**Arg16: posRStiffness**

Description: array double value [x, y, z] in coordinate system of r stiffness

Data Type: position

Default Value : [0,0,0]

Syntax: posRStiffness = [x, y, z]

**Arg17: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg18: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.SpringsDampers.Spring.OneToOne.sameDoFs(iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Connections.SpringsDampers.Spring.OneToOne.differentDoFs

## Wrapper Macro

SpringOneToOneDOFs(...)

## Ribbon-GUI-Location

Connections > SpringsDampers > Spring > OneToOne > differentDoFs

## Command Description

Spring connection One to One different DOFs

## Argument List

**Arg1: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg2: strName**

Description: definition string of input name

Data Type: string

Default Value : "SPRING"

Syntax: strName = "string input"

**Arg3: crlMasterTarget**

Description: array entities in model with type master target

Data Type: cursor list

Default Value : []

Syntax: crlMasterTarget = [EntityType(id1, id2, id3)]

**Arg4: crlSlaveTarget**

Description: array entities in model with type slave target

Data Type: cursor list

Default Value : []

Syntax: crlSlaveTarget = [EntityType(id1, id2, id3)]

**Arg5: crCoordSys**

Description: entity in database model with type coordinate sys

Data Type: cursor

Default Value : None

Syntax: crCoordSys = EntityType(id)

**Arg6: iSpringType**

Description: option for spring type

Data Type: integer

Default Value : 0

Syntax: iSpringType = 1

**Arg7: iGround**

Description: option for ground

Data Type: integer

Default Value : 0

Syntax: iGround = 1

**Arg8: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.0

Syntax: dTolerance = 1.0

**Arg9: iDirection**

Description: option for direction

Data Type: integer

Default Value : 0

Syntax: iDirection = 1

**Arg10: iDistributeMode**

Description: option for distribute mode

Data Type: integer

Default Value : 0

Syntax: iDistributeMode = 1

**Arg11: iDof1**

Description: option for dof1

Data Type: integer

Default Value : 0

Syntax: iDof1 = 1

**Arg12: iDof2**

Description: option for dof2

Data Type: integer

Default Value : 0

Syntax: iDof2 = 1

**Arg13: dDampCoef**

Description: double value of damper coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dDampCoef = 1.0

**Arg14: dStressCoef**

Description: double value of stress coefficient

Data Type: double

Default Value : DFLT_DBL

Syntax: dStressCoef = 1.0

**Arg15: posTStiffness**

Description: array double value [x, y, z] in coordinate system of t stiffness

Data Type: position

Default Value : [0,0,0]

Syntax: posTStiffness = [x, y, z]

**Arg16: posRStiffness**

Description: array double value [x, y, z] in coordinate system of r stiffness

Data Type: position

Default Value : [0,0,0]

Syntax: posRStiffness = [x, y, z]

**Arg17: bUpdateDispCS**

Description: enable or disable feature update display coordinate system

Data Type: bool

Default Value : True

Syntax: bUpdateDispCS = True/False

**Arg18: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Connections.SpringsDampers.Spring.OneToOne.differentDoFs(iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None)

```

==========================================================

# Designer.LBC.TemperatureLoad

## Wrapper Macro

TemperatureLoad(...)

## Ribbon-GUI-Location

Designer > LBC > TemperatureLoad

## Command Description

create temperature load Desiner

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: iDnType**

Description: option for dn type

Data Type: integer

Default Value : 0

Syntax: iDnType = 1

**Arg3: dFTemp**

Description: double value of temperature

Data Type: double

Default Value : 0

Syntax: dFTemp = 1.0

**Arg4: strDstrFilePathName**

Description: definition string of input dstr file path name

Data Type: string

Default Value : ""

Syntax: strDstrFilePathName = "string input"

**Arg5: crDcrTable**

Description: entity in database model with type dcr table

Data Type: cursor

Default Value : None

Syntax: crDcrTable = EntityType(id)

**Arg6: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg7: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg8: bDbUseAsMaterialReferenceTemp**

Description: enable or disable feature db use as material reference temperature

Data Type: bool

Default Value : False

Syntax: bDbUseAsMaterialReferenceTemp = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Designer.LBC.TemperatureLoad(strName="", iDnType=0, dFTemp=0, strDstrFilePathName="", crDcrTable=None, crlTarget=[], crEdit=None, bDbUseAsMaterialReferenceTemp=False)

```

==========================================================

# Designer.Load.Moment

## Wrapper Macro

Moment(...)

## Ribbon-GUI-Location

Designer > Load > Moment

## Command Description

Create moment

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: dlVecMomentXYZ**

Description: array double values of vec moment x y z

Data Type: double list

Default Value : [0.0,0.0,0.0]

Syntax: dlVecMomentXYZ = [1.0, 2.0]

**Arg4: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg5: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Designer.Load.Moment(strName="", crlFace=[], dlVecMomentXYZ=[0.0,0.0,0.0], crCoord=None, crEdit=None)

```

==========================================================

# Designer.ContactMerge

## Wrapper Macro

MergeContact(...)

## Ribbon-GUI-Location

Designer > ContactMerge

## Command Description

Build contact for designer

## Argument List

**Arg1: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Designer.ContactMerge(crlTarget=[])

```

==========================================================

# Designer.Material

## Wrapper Macro

Material2DForDesigner(...)

## Ribbon-GUI-Location

Designer > Material

## Command Description

Command use for Designer Material

## Argument List

**Arg1: strMatName**

Description: definition string of input material name

Data Type: string

Default Value : ""

Syntax: strMatName = "string input"

**Arg2: strPropName**

Description: definition string of input property name

Data Type: string

Default Value : ""

Syntax: strPropName = "string input"

**Arg3: dThickness**

Description: double value of thickness

Data Type: double

Default Value : 0.0

Syntax: dThickness = 1.0

**Arg4: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Designer.Material(strMatName="", strPropName="", dThickness=0.0, crlTarget=[])

```

==========================================================

# EngReliability.SubModelBC

## Wrapper Macro

MappingForcedDisplacement(...)

## Ribbon-GUI-Location

EngReliability > SubModelBC

## Command Description

create mapping forced displacement

## Argument List

**Arg1: strName**

Description: definition string of input name

Data Type: string

Default Value : ""

Syntax: strName = "string input"

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: iPos**

Description: option for pos

Data Type: integer

Default Value : 0

Syntax: iPos = 1

**Arg4: iViewCp**

Description: option for view cp

Data Type: integer

Default Value : 0

Syntax: iViewCp = 1

**Arg5: iCp**

Description: option for cp

Data Type: integer

Default Value : 0

Syntax: iCp = 1

**Arg6: iSrcType**

Description: option for src type

Data Type: integer

Default Value : 0

Syntax: iSrcType = 1

**Arg7: iMappedCpIndexArr0**

Description: option for mapped cp index arr0

Data Type: integer

Default Value : 0

Syntax: iMappedCpIndexArr0 = 1

**Arg8: dScaleR**

Description: double value of scale r

Data Type: double

Default Value : 0.0

Syntax: dScaleR = 1.0

**Arg9: vecOffset**

Description: array values of offset

Data Type: vector

Default Value : []

Syntax: vecOffset = [value1, value2, value3]

**Arg10: vecRotate**

Description: array values of rotate

Data Type: vector

Default Value : []

Syntax: vecRotate = [value1, value2, value3]

**Arg11: dScaleT**

Description: double value of scale t

Data Type: double

Default Value : 0.0

Syntax: dScaleT = 1.0

**Arg12: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg13: crEdit**

Description: entity in database model to edit

Data Type: cursor

Default Value : None

Syntax: crEdit = EntityType(id)

**Arg14: iMappingMethod**

Description: option for mapping method

Data Type: integer

Default Value : 0

Syntax: iMappingMethod = 1

**Arg15: iSubmodelBCMappingType**

Description: option for submodel b c mapping type

Data Type: integer

Default Value : 0

Syntax: iSubmodelBCMappingType = 1

**Arg16: iMappingFromStepNo**

Description: option for mapping from step no

Data Type: integer

Default Value : 0

Syntax: iMappingFromStepNo = 1

**Arg17: bSetADVCFile**

Description: enable or disable feature set advc file

Data Type: bool

Default Value : False

Syntax: bSetADVCFile = True/False

**Arg18: strADVCResultFile**

Description: definition string of input advc result file

Data Type: string

Default Value : ""

Syntax: strADVCResultFile = "string input"

**Arg19: bSetDetATol**

Description: enable or disable feature set det a tolerance

Data Type: bool

Default Value : False

Syntax: bSetDetATol = True/False

**Arg20: dDetATol**

Description: double value of det a tolerance

Data Type: double

Default Value : 0.0

Syntax: dDetATol = 1.0

**Arg21: bSetElementSet**

Description: enable or disable feature set element set

Data Type: bool

Default Value : False

Syntax: bSetElementSet = True/False

**Arg22: strElementSet**

Description: definition string of input element set

Data Type: string

Default Value : ""

Syntax: strElementSet = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

EngReliability.SubModelBC(strName="", crlTarget=[], iPos=0, iViewCp=0, iCp=0, iSrcType=0, iMappedCpIndexArr0=0, dScaleR=0.0, vecOffset=[], vecRotate=[], dScaleT=0.0, strPath="", crEdit=None, iMappingMethod=0, iSubmodelBCMappingType=0, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=0.0, bSetElementSet=False, strElementSet="")

```

==========================================================

# ExManifoldModeling.SZ.WeldLine2

## Wrapper Macro

SZWeldLine2(...)

## Ribbon-GUI-Location

ExManifoldModeling > SZ > WeldLine2

## Command Description

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg3: dLayerWidth**

Description: double value of layer width

Data Type: double

Default Value : 0.0

Syntax: dLayerWidth = 1.0

**Arg4: iLayerNumber**

Description: option for layer number

Data Type: integer

Default Value : 0

Syntax: iLayerNumber = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

ExManifoldModeling.SZ.WeldLine2(crlFace=[], crlPart=[], dLayerWidth=0.0, iLayerNumber=0)

```

==========================================================

# Geometry.Bar.TwoNodes

## Wrapper Macro

CreateBar(...)

## Ribbon-GUI-Location

Geometry > Bar > TwoNodes

## Command Description

Create Bar Body

## Argument List

**Arg1: strPartName**

Description: definition string of input part name

Data Type: string

Default Value : "Bar_1"

Syntax: strPartName = "string input"

**Arg2: iMeshCount**

Description: option for mesh count

Data Type: integer

Default Value : 5

Syntax: iMeshCount = 1

**Arg3: crStartNode**

Description: entity in database model with type start node

Data Type: cursor

Default Value : None

Syntax: crStartNode = EntityType(id)

**Arg4: crEndNode**

Description: entity in database model with type end node

Data Type: cursor

Default Value : None

Syntax: crEndNode = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Bar.TwoNodes(strPartName="Bar_1", iMeshCount=5, crStartNode=None, crEndNode=None)

```

==========================================================

# Geometry.Bar.Arc

## Wrapper Macro

CreateBarArc(...)

## Ribbon-GUI-Location

Geometry > Bar > Arc

## Command Description

Create Edge by spline

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: crPart**

Description: entity in database model with type part

Data Type: cursor

Default Value : None

Syntax: crPart = EntityType(id)

**Arg3: strBarName**

Description: definition string of input bar name

Data Type: string

Default Value : ""

Syntax: strBarName = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Bar.Arc(crlNode=[], crPart=None, strBarName="")

```

==========================================================

# Geometry.Bar.Spline

## Wrapper Macro

CreateBarSpline(...)

## Ribbon-GUI-Location

Geometry > Bar > Spline

## Command Description

Create Edge by spline

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: crPart**

Description: entity in database model with type part

Data Type: cursor

Default Value : None

Syntax: crPart = EntityType(id)

**Arg3: strBarName**

Description: definition string of input bar name

Data Type: string

Default Value : ""

Syntax: strBarName = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Bar.Spline(crlNode=[], crPart=None, strBarName="")

```

==========================================================

# Geometry.BodyCut.XXYYOnOnePoint

## Wrapper Macro

CutBodyByPlane(...)

## Ribbon-GUI-Location

Geometry > BodyCut > XXYYOnOnePoint

## Command Description

Cut body by one point

## Argument List

**Arg1: crPart**

Description: entity in database model with type part

Data Type: cursor

Default Value : None

Syntax: crPart = EntityType(id)

**Arg2: posCutPos**

Description: array double value [x, y, z] in coordinate system of cut pos

Data Type: position

Default Value : [0,0,0]

Syntax: posCutPos = [x, y, z]

**Arg3: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg4: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0.0

Syntax: dOffset = 1.0

**Arg5: bSplit**

Description: enable or disable feature split

Data Type: bool

Default Value : False

Syntax: bSplit = True/False

**Arg6: bSectionFace**

Description: enable or disable feature section face

Data Type: bool

Default Value : True

Syntax: bSectionFace = True/False

**Arg7: bShateFace**

Description: enable or disable feature shate face

Data Type: bool

Default Value : False

Syntax: bShateFace = True/False

**Arg8: crLocalCoor**

Description: entity in database model with type local coor

Data Type: cursor

Default Value : None

Syntax: crLocalCoor = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.BodyCut.XXYYOnOnePoint(crPart=None, posCutPos=[0,0,0], iType=0, dOffset=0.0, bSplit=False, bSectionFace=True, bShateFace=False, crLocalCoor=None)

```

==========================================================

# Geometry.BodyCut.BySurface

## Wrapper Macro

BodyCutBySurfaceS(...)

## Ribbon-GUI-Location

Geometry > BodyCut > BySurface

## Command Description

Cut body by surface

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crCutter**

Description: entity in database model with type cutter

Data Type: cursor

Default Value : None

Syntax: crCutter = EntityType(id)

**Arg3: bSplitOnly**

Description: enable or disable feature split only

Data Type: bool

Default Value : False

Syntax: bSplitOnly = True/False

**Arg4: bMakeSectionFace**

Description: enable or disable feature make section face

Data Type: bool

Default Value : True

Syntax: bMakeSectionFace = True/False

**Arg5: bShareFace**

Description: enable or disable feature share face

Data Type: bool

Default Value : False

Syntax: bShareFace = True/False

**Arg6: bSeparateFace**

Description: enable or disable feature separate face

Data Type: bool

Default Value : False

Syntax: bSeparateFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.BodyCut.BySurface(crlPart=[], crCutter=None, bSplitOnly=False, bMakeSectionFace=True, bShareFace=False, bSeparateFace=False)

```

==========================================================

# Geometry.BodyCut.By3Points

## Wrapper Macro

BodyCutBy3PointsS(...)

## Ribbon-GUI-Location

Geometry > BodyCut > By3Points

## Command Description

Body Cut by 3 Points

## Argument List

**Arg1: crPart**

Description: entity in database model with type part

Data Type: cursor

Default Value : None

Syntax: crPart = EntityType(id)

**Arg2: poslPosition**

Description: list positions [x, y, z] in coordinate system of position

Data Type: position list

Default Value : []

Syntax: poslPosition = [[x, y, z], [x, y, z]]

**Arg3: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0.0

Syntax: dOffset = 1.0

**Arg4: bSplitonly**

Description: enable or disable feature splitonly

Data Type: bool

Default Value : False

Syntax: bSplitonly = True/False

**Arg5: bMakesectionface**

Description: enable or disable feature makesectionface

Data Type: bool

Default Value : True

Syntax: bMakesectionface = True/False

**Arg6: bShareface**

Description: enable or disable feature shareface

Data Type: bool

Default Value : False

Syntax: bShareface = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.BodyCut.By3Points(crPart=None, poslPosition=[], dOffset=0.0, bSplitonly=False, bMakesectionface=True, bShareface=False)

```

==========================================================

# Geometry.BreakEntity.StlPart

## Wrapper Macro

SeparateSTLPart(...)

## Ribbon-GUI-Location

Geometry > BreakEntity > StlPart

## Command Description

break STL part

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: iMinNoOfFaces**

Description: option for minimize no of faces

Data Type: integer

Default Value : 0

Syntax: iMinNoOfFaces = 1

**Arg3: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.BreakEntity.StlPart(crlPart=[], iMinNoOfFaces=0, iMethod=0)

```

==========================================================

# Geometry.BreakEntity.Face

## Wrapper Macro

BreakFace(...)

## Ribbon-GUI-Location

Geometry > BreakEntity > Face

## Command Description

break entity for face

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.BreakEntity.Face(crlFace=[])

```

==========================================================

# Geometry.BreakEntity.Edge

## Wrapper Macro

BreakEdgeCr(...)

## Ribbon-GUI-Location

Geometry > BreakEntity > Edge

## Command Description

Break selected edge

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg4: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg5: bAutoByAngle**

Description: enable or disable feature auto by angle

Data Type: bool

Default Value : False

Syntax: bAutoByAngle = True/False

**Arg6: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.BreakEntity.Edge(crlPart=[], crlFace=[], crlEdge=[], crlNode=[], bAutoByAngle=False, dEdgeAngle=60.0)

```

==========================================================

# Geometry.BreakEntity.Part

## Wrapper Macro

SeparatePart(...)

## Ribbon-GUI-Location

Geometry > BreakEntity > Part

## Command Description

Separate Part

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.BreakEntity.Part(crlPart=[])

```

==========================================================

# Geometry.DeleteEntity.Part

## Wrapper Macro

DeletePartCr(...)

## Ribbon-GUI-Location

Geometry > DeleteEntity > Part

## Command Description

Delete Part

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.DeleteEntity.Part(crlPart=[])

```

==========================================================

# Geometry.DeleteEntity.Edge

## Wrapper Macro

DeleteEdgeCr(...)

## Ribbon-GUI-Location

Geometry > DeleteEntity > Edge

## Command Description

Delete Edge

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.DeleteEntity.Edge(crlEdge=[])

```

==========================================================

# Geometry.DeleteEntity.Vertex

## Wrapper Macro

DeleteVertexCr(...)

## Ribbon-GUI-Location

Geometry > DeleteEntity > Vertex

## Command Description

delete vertex

## Argument List

**Arg1: crlVertex**

Description: array entities in model with type vertex

Data Type: cursor list

Default Value : []

Syntax: crlVertex = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.DeleteEntity.Vertex(crlVertex=[])

```

==========================================================

# Geometry.DeleteEntity.Face

## Wrapper Macro

DeleteFaceCr(...)

## Ribbon-GUI-Location

Geometry > DeleteEntity > Face

## Command Description

Delete Face

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: bKeepSolid**

Description: enable or disable feature keep solid

Data Type: bool

Default Value : True

Syntax: bKeepSolid = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.DeleteEntity.Face(crlFace=[], bKeepSolid=True)

```

==========================================================

# Geometry.Edge.Line

## Wrapper Macro

ImprintLineS(...)

## Ribbon-GUI-Location

Geometry > Edge > Line

## Command Description

Imprint line 2 point

## Argument List

**Arg1: poslPositions**

Description: list positions [x, y, z] in coordinate system of positions

Data Type: position list

Default Value : [[]]

Syntax: poslPositions = [[x, y, z], [x, y, z]]

**Arg2: crlTargetFace**

Description: array entities in database model face

Data Type: cursor list

Default Value : []

Syntax: crlTargetFace = [EntityType(id1, id2, id3)]

**Arg3: bBreakFace**

Description: enable or disable feature break face

Data Type: bool

Default Value : True

Syntax: bBreakFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.Line(poslPositions=[[]], crlTargetFace=[], bBreakFace=True)

```

==========================================================

# Geometry.Edge.Spline

## Wrapper Macro

GeoImprintSplineS(...)

## Ribbon-GUI-Location

Geometry > Edge > Spline

## Command Description

Imprint a Spline on a face

## Argument List

**Arg1: veclAprroxiPositions**

Description: two dimensional array of aprroxi positions

Data Type: vector list

Default Value : [[]]

Syntax: veclAprroxiPositions = [[value1, value2, value3], [value1, value2, value3]]

**Arg2: crlTargetFace**

Description: array entities in database model face

Data Type: cursor list

Default Value : []

Syntax: crlTargetFace = [EntityType(id1, id2, id3)]

**Arg3: bBreakFace**

Description: enable or disable feature break face

Data Type: bool

Default Value : True

Syntax: bBreakFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.Spline(veclAprroxiPositions=[[]], crlTargetFace=[], bBreakFace=True)

```

==========================================================

# Geometry.Edge.PlanarLine

## Wrapper Macro

ImprintPlannarLineS(...)

## Ribbon-GUI-Location

Geometry > Edge > PlanarLine

## Command Description

Imprint Planar Line

## Argument List

**Arg1: veclPosition**

Description: two dimensional array of position

Data Type: vector list

Default Value : [[]]

Syntax: veclPosition = [[value1, value2, value3], [value1, value2, value3]]

**Arg2: crlTargetFace**

Description: array entities in database model face

Data Type: cursor list

Default Value : []

Syntax: crlTargetFace = [EntityType(id1, id2, id3)]

**Arg3: crLocalCoord**

Description: entity in database model with type local coordinate

Data Type: cursor

Default Value : None

Syntax: crLocalCoord = EntityType(id)

**Arg4: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg5: bBreakFace**

Description: enable or disable feature break face

Data Type: bool

Default Value : True

Syntax: bBreakFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.PlanarLine(veclPosition=[[]], crlTargetFace=[], crLocalCoord=None, iType=0, bBreakFace=True)

```

==========================================================

# Geometry.Edge.Circle

## Wrapper Macro

ImprintCircleS(...)

## Ribbon-GUI-Location

Geometry > Edge > Circle

## Command Description

Imprint Cirlcle Line S

## Argument List

**Arg1: veclPositions**

Description: two dimensional array of positions

Data Type: vector list

Default Value : [[]]

Syntax: veclPositions = [[value1, value2, value3], [value1, value2, value3]]

**Arg2: crlTargetFace**

Description: array entities in database model face

Data Type: cursor list

Default Value : []

Syntax: crlTargetFace = [EntityType(id1, id2, id3)]

**Arg3: dInRadius**

Description: double value of in radius

Data Type: double

Default Value : 1

Syntax: dInRadius = 1.0

**Arg4: dOutRadius**

Description: double value of out radius

Data Type: double

Default Value : 4

Syntax: dOutRadius = 1.0

**Arg5: iNoOfLayer**

Description: option for no of layer

Data Type: integer

Default Value : 1

Syntax: iNoOfLayer = 1

**Arg6: iNoOfDiv**

Description: option for no of div

Data Type: integer

Default Value : 30

Syntax: iNoOfDiv = 1

**Arg7: bBreakFace**

Description: enable or disable feature break face

Data Type: bool

Default Value : True

Syntax: bBreakFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.Circle(veclPositions=[[]], crlTargetFace=[], dInRadius=1, dOutRadius=4, iNoOfLayer=1, iNoOfDiv=30, bBreakFace=True)

```

==========================================================

# Geometry.Edge.PerpendicularLineOfEdge

## Wrapper Macro

ImprintPerpendicularLine(...)

## Ribbon-GUI-Location

Geometry > Edge > PerpendicularLineOfEdge

## Command Description

Imprint the perpendicular line of edge

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0

Syntax: dOffset = 1.0

**Arg4: bReakFace**

Description: enable or disable feature reak face

Data Type: bool

Default Value : True

Syntax: bReakFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.PerpendicularLineOfEdge(crlNode=[], crlFace=[], dOffset=0, bReakFace=True)

```

==========================================================

# Geometry.Edge.ExtendLine

## Wrapper Macro

ImprintExtendLine(...)

## Ribbon-GUI-Location

Geometry > Edge > ExtendLine

## Command Description

make edge by extend line

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg2: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg3: iEnd**

Description: option for end

Data Type: integer

Default Value : 0

Syntax: iEnd = 1

**Arg4: iNoFittingPoints**

Description: option for no fitting points

Data Type: integer

Default Value : 3

Syntax: iNoFittingPoints = 1

**Arg5: iDiv**

Description: option for div

Data Type: integer

Default Value : 2

Syntax: iDiv = 1

**Arg6: iEnableBreakFace**

Description: option for enable break face

Data Type: integer

Default Value : 1

Syntax: iEnableBreakFace = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.ExtendLine(crlEdge=[], iMethod=0, iEnd=0, iNoFittingPoints=3, iDiv=2, iEnableBreakFace=1)

```

==========================================================

# Geometry.Edge.ElementEdges

## Wrapper Macro

CreateEdgeByElemEdge(...)

## Ribbon-GUI-Location

Geometry > Edge > ElementEdges

## Command Description

Create Edge by element edges

## Argument List

**Arg1: crplElemEdge**

Description: list pair of entities in model with type element edge

Data Type: cursor pair list

Default Value : [[]]

Syntax: crplElemEdge = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg2: bBreakEdge**

Description: enable or disable feature break edge

Data Type: bool

Default Value : True

Syntax: bBreakEdge = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.ElementEdges(crplElemEdge=[[]], bBreakEdge=True)

```

==========================================================

# Geometry.Edge.Angle

## Wrapper Macro

CreateEdgeByElemEdgeAngle(...)

## Ribbon-GUI-Location

Geometry > Edge > Angle

## Command Description

create new adge by convert angle

## Argument List

**Arg1: crpPair**

Description: pair of entities in model with type pair

Data Type: cursor pair

Default Value : []

Syntax: crpPair = CursorPair(EntityType(id), EntityType(id))

**Arg2: dAngle**

Description: double value of angle

Data Type: double

Default Value : 135.0

Syntax: dAngle = 1.0

**Arg3: bCurvature**

Description: enable or disable feature curvature

Data Type: bool

Default Value : False

Syntax: bCurvature = True/False

**Arg4: bBreakFace**

Description: enable or disable feature break face

Data Type: bool

Default Value : True

Syntax: bBreakFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.Angle(crpPair=[], dAngle=135.0, bCurvature=False, bBreakFace=True)

```

==========================================================

# Geometry.Edge.NodeShortestPath

## Wrapper Macro

CreateEdgeBy2NodeShortestPath(...)

## Ribbon-GUI-Location

Geometry > Edge > NodeShortestPath

## Command Description

create edge by 2 nodes shortest path

## Argument List

**Arg1: crFirstNode**

Description: entity in database model with type first node

Data Type: cursor

Default Value : None

Syntax: crFirstNode = EntityType(id)

**Arg2: crSecondNode**

Description: entity in database model with type second node

Data Type: cursor

Default Value : None

Syntax: crSecondNode = EntityType(id)

**Arg3: iEnableBreakFace**

Description: option for enable break face

Data Type: integer

Default Value : 1

Syntax: iEnableBreakFace = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.NodeShortestPath(crFirstNode=None, crSecondNode=None, iEnableBreakFace=1)

```

==========================================================

# Geometry.Edge.OffsetLine

## Wrapper Macro

ImprintOffsetLineS(...)

## Ribbon-GUI-Location

Geometry > Edge > OffsetLine

## Command Description

Imprint geometry edge offset line

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg3: bBreakFace**

Description: enable or disable feature break face

Data Type: bool

Default Value : True

Syntax: bBreakFace = True/False

**Arg4: dOffsetDistance**

Description: double value of offset distance

Data Type: double

Default Value : 0.0

Syntax: dOffsetDistance = 1.0

**Arg5: iNumberLayer**

Description: option for number layer

Data Type: integer

Default Value : 1

Syntax: iNumberLayer = 1

**Arg6: bMerge**

Description: enable or disable feature merge

Data Type: bool

Default Value : True

Syntax: bMerge = True/False

**Arg7: bExtend**

Description: enable or disable feature extend

Data Type: bool

Default Value : True

Syntax: bExtend = True/False

**Arg8: iLayerMethod**

Description: option for layer method

Data Type: integer

Default Value : 0

Syntax: iLayerMethod = 1

**Arg9: dlVlayerOffset**

Description: array double values of vlayer offset

Data Type: double list

Default Value : []

Syntax: dlVlayerOffset = [1.0, 2.0]

**Arg10: bAutoCollapse**

Description: enable or disable feature auto collapse

Data Type: bool

Default Value : False

Syntax: bAutoCollapse = True/False

**Arg11: iRLType**

Description: option for r l type

Data Type: integer

Default Value : 2

Syntax: iRLType = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.OffsetLine(crlFace=[], crlEdge=[], bBreakFace=True, dOffsetDistance=0.0, iNumberLayer=1, bMerge=True, bExtend=True, iLayerMethod=0, dlVlayerOffset=[], bAutoCollapse=False, iRLType=2)

```

==========================================================

# Geometry.Edge.SplineFreeEdges

## Wrapper Macro

CreateEdgeSpline(...)

## Ribbon-GUI-Location

Geometry > Edge > SplineFreeEdges

## Command Description

Create Edge by spline

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: iEnableArc**

Description: option for enable arc

Data Type: integer

Default Value : 0

Syntax: iEnableArc = 1

**Arg3: crPart**

Description: entity in database model with type part

Data Type: cursor

Default Value : None

Syntax: crPart = EntityType(id)

**Arg4: strBarName**

Description: definition string of input bar name

Data Type: string

Default Value : ""

Syntax: strBarName = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.SplineFreeEdges(crlNode=[], iEnableArc=0, crPart=None, strBarName="")

```

==========================================================

# Geometry.Edge.ClosedLine

## Wrapper Macro

ImprintCloseLineS(...)

## Ribbon-GUI-Location

Geometry > Edge > ClosedLine

## Command Description

imprint closed line

## Argument List

**Arg1: veclPositions**

Description: two dimensional array of positions

Data Type: vector list

Default Value : [[]]

Syntax: veclPositions = [[value1, value2, value3], [value1, value2, value3]]

**Arg2: crlTargetFace**

Description: array entities in database model face

Data Type: cursor list

Default Value : []

Syntax: crlTargetFace = [EntityType(id1, id2, id3)]

**Arg3: iEnableBreakFace**

Description: option for enable break face

Data Type: integer

Default Value : 1

Syntax: iEnableBreakFace = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.ClosedLine(veclPositions=[[]], crlTargetFace=[], iEnableBreakFace=1)

```

==========================================================

# Geometry.Edge.PerpendicularCylinderLine

## Wrapper Macro

ImprintPerpendicularCylinderLineS(...)

## Ribbon-GUI-Location

Geometry > Edge > PerpendicularCylinderLine

## Command Description

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg4: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0.0

Syntax: dOffset = 1.0

**Arg5: bOppositeSide**

Description: enable or disable feature opposite side

Data Type: bool

Default Value : False

Syntax: bOppositeSide = True/False

**Arg6: bBreakFace**

Description: enable or disable feature break face

Data Type: bool

Default Value : True

Syntax: bBreakFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.PerpendicularCylinderLine(crlNode=[], crlFace=[], iMethod=0, dOffset=0.0, bOppositeSide=False, bBreakFace=True)

```

==========================================================

# Geometry.Edge.IntersectionLine

## Wrapper Macro

Imprint_Intersection_LineS(...)

## Ribbon-GUI-Location

Geometry > Edge > IntersectionLine

## Command Description

## Argument List

**Arg1: crlFaces**

Description: array entities in model with type faces

Data Type: cursor list

Default Value : []

Syntax: crlFaces = [EntityType(id1, id2, id3)]

**Arg2: bBreakFace**

Description: enable or disable feature break face

Data Type: bool

Default Value : True

Syntax: bBreakFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.IntersectionLine(crlFaces=[], bBreakFace=True)

```

==========================================================

# Geometry.Edge.ProjectLine

## Wrapper Macro

Imprint_Projection_LineS(...)

## Ribbon-GUI-Location

Geometry > Edge > ProjectLine

## Command Description

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg2: crlFaces**

Description: array entities in model with type faces

Data Type: cursor list

Default Value : []

Syntax: crlFaces = [EntityType(id1, id2, id3)]

**Arg3: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg4: bBreakFace**

Description: enable or disable feature break face

Data Type: bool

Default Value : True

Syntax: bBreakFace = True/False

**Arg5: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg6: bCheckGap**

Description: enable or disable feature check gap

Data Type: bool

Default Value : False

Syntax: bCheckGap = True/False

**Arg7: dGap**

Description: double value of gap

Data Type: double

Default Value : 0.0

Syntax: dGap = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.ProjectLine(crlEdge=[], crlFaces=[], crlNode=[], bBreakFace=True, iType=0, bCheckGap=False, dGap=0.0)

```

==========================================================

# Geometry.Edge.PerpendicularLineToEdge

## Wrapper Macro

ImprintPerpendicularLine2(...)

## Ribbon-GUI-Location

Geometry > Edge > PerpendicularLineToEdge

## Command Description

## Argument List

**Arg1: crNode**

Description: entity in database model with type node

Data Type: cursor

Default Value : None

Syntax: crNode = EntityType(id)

**Arg2: crEdge**

Description: entity in database model with type edge

Data Type: cursor

Default Value : None

Syntax: crEdge = EntityType(id)

**Arg3: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg4: bBreakFace**

Description: enable or disable feature break face

Data Type: bool

Default Value : True

Syntax: bBreakFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Edge.PerpendicularLineToEdge(crNode=None, crEdge=None, crlFace=[], bBreakFace=True)

```

==========================================================

# Geometry.ExtractSurfaces.ExtractSurfaces

## Wrapper Macro

MeshEditExtractSurfaces(...)

## Ribbon-GUI-Location

Geometry > ExtractSurfaces > ExtractSurfaces

## Command Description

Command use for Geometry ExtractSurfaces

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dAngle**

Description: double value of angle

Data Type: double

Default Value : 60.0

Syntax: dAngle = 1.0

**Arg3: strName**

Description: definition string of input name

Data Type: string

Default Value : "ExtractFace_1"

Syntax: strName = "string input"

**Arg4: bMergePart**

Description: enable or disable feature merge part

Data Type: bool

Default Value : False

Syntax: bMergePart = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.ExtractSurfaces.ExtractSurfaces(crlFace=[], dAngle=60.0, strName="ExtractFace_1", bMergePart=False)

```

==========================================================

# Geometry.Face.FourEdges

## Wrapper Macro

CreateFaceFromFourEdges(...)

## Ribbon-GUI-Location

Geometry > Face > FourEdges

## Command Description

Create face by four edges

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Face.FourEdges(crlEdge=[])

```

==========================================================

# Geometry.Face.FromMesh

## Wrapper Macro

CreateFaceFromMeshFace(...)

## Ribbon-GUI-Location

Geometry > Face > FromMesh

## Command Description

Create geometry face from mesh face

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Face.FromMesh(crlFace=[])

```

==========================================================

# Geometry.Face.CreateSmoothFace

## Wrapper Macro

CreateSmoothFace(...)

## Ribbon-GUI-Location

Geometry > Face > CreateSmoothFace

## Command Description

Geometry Face CreateSmoothFace

## Argument List

**Arg1: bInterPoration**

Description: enable or disable feature inter poration

Data Type: bool

Default Value : False

Syntax: bInterPoration = True/False

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: iElemGeneration**

Description: option for element generation

Data Type: integer

Default Value : 0

Syntax: iElemGeneration = 1

**Arg4: dGradation**

Description: double value of gradation

Data Type: double

Default Value : 0.0

Syntax: dGradation = 1.0

**Arg5: iEnableFaceSmooth**

Description: option for enable face smooth

Data Type: integer

Default Value : 0

Syntax: iEnableFaceSmooth = 1

**Arg6: crTargetPart**

Description: entity in database model with type target part

Data Type: cursor

Default Value : None

Syntax: crTargetPart = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Face.CreateSmoothFace(bInterPoration=False, crlTarget=[], iElemGeneration=0, dGradation=0.0, iEnableFaceSmooth=0, crTargetPart=None)

```

==========================================================

# Geometry.Face.Edges

## Wrapper Macro

CreateFaceFromEdges(...)

## Ribbon-GUI-Location

Geometry > Face > Edges

## Command Description

Create Face From Edges

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg2: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg3: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg4: bSharedFace**

Description: enable or disable feature shared face

Data Type: bool

Default Value : False

Syntax: bSharedFace = True/False

**Arg5: bSmoothFace**

Description: enable or disable feature smooth face

Data Type: bool

Default Value : False

Syntax: bSmoothFace = True/False

**Arg6: bCreatePart**

Description: enable or disable feature create part

Data Type: bool

Default Value : False

Syntax: bCreatePart = True/False

**Arg7: bImproved**

Description: enable or disable feature improved

Data Type: bool

Default Value : False

Syntax: bImproved = True/False

**Arg8: bBarsOnly**

Description: enable or disable feature bars only

Data Type: bool

Default Value : False

Syntax: bBarsOnly = True/False

**Arg9: bOnlyOnePart**

Description: enable or disable feature only one part

Data Type: bool

Default Value : True

Syntax: bOnlyOnePart = True/False

**Arg10: bUseMidNodes**

Description: enable or disable feature use mid nodes

Data Type: bool

Default Value : False

Syntax: bUseMidNodes = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Face.Edges(crlEdge=[], crlPart=[], crlNode=[], bSharedFace=False, bSmoothFace=False, bCreatePart=False, bImproved=False, bBarsOnly=False, bOnlyOnePart=True, bUseMidNodes=False)

```

==========================================================

# Geometry.Face.Elements

## Wrapper Macro

CreateFaceByElem(...)

## Ribbon-GUI-Location

Geometry > Face > Elements

## Command Description

Create Face By Elements

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: bShareFace**

Description: enable or disable feature share face

Data Type: bool

Default Value : False

Syntax: bShareFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Face.Elements(crlElem=[], bShareFace=False)

```

==========================================================

# Geometry.FindFeature.DelCircChamfer

## Wrapper Macro

DelCircChamfer(...)

## Ribbon-GUI-Location

Geometry > FindFeature > DelCircChamfer

## Command Description

Delete Circ Chamfer

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: dMaxThick**

Description: double value of maximize thick

Data Type: double

Default Value : 0.1

Syntax: dMaxThick = 1.0

**Arg3: dMinThick**

Description: double value of minimize thick

Data Type: double

Default Value : 2

Syntax: dMinThick = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.FindFeature.DelCircChamfer(crlPart=[], dMaxThick=0.1, dMinThick=2)

```

==========================================================

# Geometry.FindFeature.Fillet

## Wrapper Macro

FindFeatureFillet(...)

## Ribbon-GUI-Location

Geometry > FindFeature > Fillet

## Command Description

Find feature in part by typical description

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: dMinAngle**

Description: double value of minimize angle

Data Type: double

Default Value : 1.0

Syntax: dMinAngle = 1.0

**Arg4: dMaxAngle**

Description: double value of maximize angle

Data Type: double

Default Value : 10.0

Syntax: dMaxAngle = 1.0

**Arg5: dMinFaceWidth**

Description: double value of minimize face width

Data Type: double

Default Value : 1.0

Syntax: dMinFaceWidth = 1.0

**Arg6: dMaxFaceWidth**

Description: double value of maximize face width

Data Type: double

Default Value : 10.0

Syntax: dMaxFaceWidth = 1.0

**Arg7: dMinCurveRadius**

Description: double value of minimize curve radius

Data Type: double

Default Value : 0.0

Syntax: dMinCurveRadius = 1.0

**Arg8: dMaxCurveRadius**

Description: double value of maximize curve radius

Data Type: double

Default Value : 171

Syntax: dMaxCurveRadius = 1.0

**Arg9: dScale**

Description: double value of scale

Data Type: double

Default Value : 1.0

Syntax: dScale = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.FindFeature.Fillet(crlPart=[], crlFace=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0)

```

==========================================================

# Geometry.FindFeature.Faces

## Wrapper Macro

Geom_FindFeatures(...)

## Ribbon-GUI-Location

Geometry > FindFeature > Faces

## Command Description

Command use for Geometry FindFeature Faces

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : [],iOption

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg3: bCylinder**

Description: enable or disable feature cylinder

Data Type: bool

Default Value : True

Syntax: bCylinder = True/False

**Arg4: bDisc**

Description: enable or disable feature disc

Data Type: bool

Default Value : False

Syntax: bDisc = True/False

**Arg5: bFourCorners**

Description: enable or disable feature four corners

Data Type: bool

Default Value : True

Syntax: bFourCorners = True/False

**Arg6: dMinThickness**

Description: double value of minimize thickness

Data Type: double

Default Value : 0.1

Syntax: dMinThickness = 1.0

**Arg7: dMaxThickness**

Description: double value of maximize thickness

Data Type: double

Default Value : 2.0

Syntax: dMaxThickness = 1.0

**Arg8: dDiameterMin**

Description: double value of diameter minimize

Data Type: double

Default Value : 1.0

Syntax: dDiameterMin = 1.0

**Arg9: dDiameterMax**

Description: double value of diameter maximize

Data Type: double

Default Value : 2.0

Syntax: dDiameterMax = 1.0

**Arg10: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.FindFeature.Faces(crlPart=[],iOption=0, crlEdge=[], bCylinder=True, bDisc=False, bFourCorners=True, dMinThickness=0.1, dMaxThickness=2.0, dDiameterMin=1.0, dDiameterMax=2.0, crlFace=[])

```

==========================================================

# Geometry.FindFeature.Edges

## Wrapper Macro

Geom_FindFeatures(...)

## Ribbon-GUI-Location

Geometry > FindFeature > Edges

## Command Description

Command use for Geometry FindFeature Edges

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : [],iOption

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg3: bCylinder**

Description: enable or disable feature cylinder

Data Type: bool

Default Value : True

Syntax: bCylinder = True/False

**Arg4: bDisc**

Description: enable or disable feature disc

Data Type: bool

Default Value : False

Syntax: bDisc = True/False

**Arg5: bFourCorners**

Description: enable or disable feature four corners

Data Type: bool

Default Value : True

Syntax: bFourCorners = True/False

**Arg6: dMinThickness**

Description: double value of minimize thickness

Data Type: double

Default Value : 0.1

Syntax: dMinThickness = 1.0

**Arg7: dMaxThickness**

Description: double value of maximize thickness

Data Type: double

Default Value : 2.0

Syntax: dMaxThickness = 1.0

**Arg8: dDiameterMin**

Description: double value of diameter minimize

Data Type: double

Default Value : 1.0

Syntax: dDiameterMin = 1.0

**Arg9: dDiameterMax**

Description: double value of diameter maximize

Data Type: double

Default Value : 2.0

Syntax: dDiameterMax = 1.0

**Arg10: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.FindFeature.Edges(crlPart=[],iOption=0, crlEdge=[], bCylinder=True, bDisc=False, bFourCorners=True, dMinThickness=0.1, dMaxThickness=2.0, dDiameterMin=1.0, dDiameterMax=2.0, crlFace=[])

```

==========================================================

# Geometry.MergeEntities.Faces

## Wrapper Macro

MergeFace_MergeEntities(...)

## Ribbon-GUI-Location

Geometry > MergeEntities > Faces

## Command Description

Merge faces

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: bMergeEdge**

Description: enable or disable feature merge edge

Data Type: bool

Default Value : True

Syntax: bMergeEdge = True/False

**Arg3: bRemoveNonBoundEdge**

Description: enable or disable feature remove non bound edge

Data Type: bool

Default Value : True

Syntax: bRemoveNonBoundEdge = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.MergeEntities.Faces(crlFace=[], bMergeEdge=True, bRemoveNonBoundEdge=True)

```

==========================================================

# Geometry.MergeEntities.TinyFacesMerge

## Wrapper Macro

GeometryMergeEntitiesTinyFacesMerge(...)

## Ribbon-GUI-Location

Geometry > MergeEntities > TinyFacesMerge

## Command Description

merge tiny faces

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: dMinFaceWidth**

Description: double value of minimize face width

Data Type: double

Default Value : 0.0

Syntax: dMinFaceWidth = 1.0

**Arg4: dMaxFaceWidth**

Description: double value of maximize face width

Data Type: double

Default Value : 0.001

Syntax: dMaxFaceWidth = 1.0

**Arg5: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 30

Syntax: dFaceAngle = 1.0

**Arg6: bReferLocalSetting**

Description: enable or disable feature refer local setting

Data Type: bool

Default Value : False

Syntax: bReferLocalSetting = True/False

**Arg7: bConnectFace**

Description: enable or disable feature connect face

Data Type: bool

Default Value : False

Syntax: bConnectFace = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.MergeEntities.TinyFacesMerge(crlPart=[], crlFace=[], dMinFaceWidth=0.0, dMaxFaceWidth=0.001, dFaceAngle=30, bReferLocalSetting=False, bConnectFace=False)

```

==========================================================

# Geometry.MergeEntities.CBarParts

## Wrapper Macro

MergeCBarPart(...)

## Ribbon-GUI-Location

Geometry > MergeEntities > CBarParts

## Command Description

Merge CBar Parts

## Argument List

**Arg1: crlCBarPart**

Description: array entities in model with type c bar part

Data Type: cursor list

Default Value : []

Syntax: crlCBarPart = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.MergeEntities.CBarParts(crlCBarPart=[])

```

==========================================================

# Geometry.MergeEntities.Edges

## Wrapper Macro

bMergeEdge(...)

## Ribbon-GUI-Location

Geometry > MergeEntities > Edges

## Command Description

Merge Edge

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.MergeEntities.Edges(crlEdge=[])

```

==========================================================

# Geometry.MergeEntities.Parts

## Wrapper Macro

MergePart(...)

## Ribbon-GUI-Location

Geometry > MergeEntities > Parts

## Command Description

Merge Part

## Argument List

**Arg1: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 1e-5

Syntax: dTolerance = 1.0

**Arg2: bRemovesharefaceflag**

Description: enable or disable feature removesharefaceflag

Data Type: bool

Default Value : True

Syntax: bRemovesharefaceflag = True/False

**Arg3: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.MergeEntities.Parts(dTolerance=1e-5, bRemovesharefaceflag=True, crlPart=[])

```

==========================================================

# Geometry.MergeEntities.PartFaces

## Wrapper Macro

MergeBodyFaceCr(...)

## Ribbon-GUI-Location

Geometry > MergeEntities > PartFaces

## Command Description

Merge by Part Faces

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: bAngle**

Description: enable or disable feature angle

Data Type: bool

Default Value : True

Syntax: bAngle = True/False

**Arg4: dTolAngle**

Description: double value of tolerance angle

Data Type: double

Default Value : 20

Syntax: dTolAngle = 1.0

**Arg5: bWidth**

Description: enable or disable feature width

Data Type: bool

Default Value : True

Syntax: bWidth = True/False

**Arg6: dTolWidth**

Description: double value of tolerance width

Data Type: double

Default Value : 0.2

Syntax: dTolWidth = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.MergeEntities.PartFaces(crlPart=[], crlFace=[], bAngle=True, dTolAngle=20, bWidth=True, dTolWidth=0.2)

```

==========================================================

# Geometry.Part.Cube

## Wrapper Macro

CreateCube(...)

## Ribbon-GUI-Location

Geometry > Part > Cube

## Command Description

create cube part

## Argument List

**Arg1: dlOrigin**

Description: array double values of origin

Data Type: double list

Default Value : [0

Syntax: dlOrigin = [1.0, 2.0]

**Arg4: dlLength**

Description: array double values of length

Data Type: double list

Default Value : [0

Syntax: dlLength = [1.0, 2.0]

**Arg7: ilNodeCnt**

Description: array int values of node count

Data Type: int list

Default Value : [10

Syntax: ilNodeCnt = [1,2,3,4]

**Arg10: strPartName**

Description: definition string of input part name

Data Type: string

Default Value : "Cube_1"

Syntax: strPartName = "string input"

**Arg11: iColorPart**

Description: option for color part

Data Type: integer

Default Value : 710

Syntax: iColorPart = 1

**Arg12: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Part.Cube(dlOrigin=[0, 0, 0], dlLength=[0.01, 0.01, 0.01], ilNodeCnt=[10, 10, 10], strPartName="Cube_1", iColorPart=7105764, crCoord=None)

```

==========================================================

# Geometry.Part.Wedge

## Wrapper Macro

CreateWedge(...)

## Ribbon-GUI-Location

Geometry > Part > Wedge

## Command Description

Create Wedge Body

## Argument List

**Arg1: vecOrigin**

Description: array values of origin

Data Type: vector

Default Value : [0.0

Syntax: vecOrigin = [value1, value2, value3]

**Arg4: vecLength**

Description: array values of length

Data Type: vector

Default Value : [0.0

Syntax: vecLength = [value1, value2, value3]

**Arg7: vecNodeCount**

Description: array values of node count

Data Type: vector

Default Value : [10

Syntax: vecNodeCount = [value1, value2, value3]

**Arg10: strPartName**

Description: definition string of input part name

Data Type: string

Default Value : "Wedge_1"

Syntax: strPartName = "string input"

**Arg11: iPartColor**

Description: option for part color

Data Type: integer

Default Value : 710

Syntax: iPartColor = 1

**Arg12: crCoordinate**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoordinate = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Part.Wedge(vecOrigin=[0.0, 0.0, 0.0], vecLength=[0.01, 0.01, 0.01], vecNodeCount=[10, 10, 10], strPartName="Wedge_1", iPartColor=7105764, crCoordinate=None)

```

==========================================================

# Geometry.Part.Sphere

## Wrapper Macro

CreateSphere(...)

## Ribbon-GUI-Location

Geometry > Part > Sphere

## Command Description

create Sphere part

## Argument List

**Arg1: dlOrigin**

Description: array double values of origin

Data Type: double list

Default Value : [0

Syntax: dlOrigin = [1.0, 2.0]

**Arg4: dRadius**

Description: double value of radius

Data Type: double

Default Value : 0

Syntax: dRadius = 1.0

**Arg5: iLatitudeNodeCnt**

Description: option for latitude node count

Data Type: integer

Default Value : 20

Syntax: iLatitudeNodeCnt = 1

**Arg6: iLongitudeNodeCnt**

Description: option for longitude node count

Data Type: integer

Default Value : 20

Syntax: iLongitudeNodeCnt = 1

**Arg7: strPartName**

Description: definition string of input part name

Data Type: string

Default Value : "Sphere_1"

Syntax: strPartName = "string input"

**Arg8: iColorPart**

Description: option for color part

Data Type: integer

Default Value : 710

Syntax: iColorPart = 1

**Arg9: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Part.Sphere(dlOrigin=[0, 0, 0], dRadius=0.005, iLatitudeNodeCnt=20, iLongitudeNodeCnt=20, strPartName="Sphere_1", iColorPart=7105764, crCoord=None)

```

==========================================================

# Geometry.Part.Torus

## Wrapper Macro

CreateTorus(...)

## Ribbon-GUI-Location

Geometry > Part > Torus

## Command Description

create Torus part

## Argument List

**Arg1: dlOrigin**

Description: array double values of origin

Data Type: double list

Default Value : [0

Syntax: dlOrigin = [1.0, 2.0]

**Arg4: dInnerRadius**

Description: double value of inner radius

Data Type: double

Default Value : 0

Syntax: dInnerRadius = 1.0

**Arg5: dRingRadius**

Description: double value of ring radius

Data Type: double

Default Value : 0

Syntax: dRingRadius = 1.0

**Arg6: iLatitudeNodeCnt**

Description: option for latitude node count

Data Type: integer

Default Value : 20

Syntax: iLatitudeNodeCnt = 1

**Arg7: iLongitudeNodeCnt**

Description: option for longitude node count

Data Type: integer

Default Value : 20

Syntax: iLongitudeNodeCnt = 1

**Arg8: strPartName**

Description: definition string of input part name

Data Type: string

Default Value : "Torus_1"

Syntax: strPartName = "string input"

**Arg9: iColorPart**

Description: option for color part

Data Type: integer

Default Value : 710

Syntax: iColorPart = 1

**Arg10: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Part.Torus(dlOrigin=[0, 0, 0], dInnerRadius=0.015, dRingRadius=0.02, iLatitudeNodeCnt=20, iLongitudeNodeCnt=20, strPartName="Torus_1", iColorPart=7105764, crCoord=None)

```

==========================================================

# Geometry.Part.Elems

## Wrapper Macro

CreatePartFromElems(...)

## Ribbon-GUI-Location

Geometry > Part > Elems

## Command Description

create part from element

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: strPartName**

Description: definition string of input part name

Data Type: string

Default Value : ""

Syntax: strPartName = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Part.Elems(crlElem=[], strPartName="")

```

==========================================================

# Geometry.Part.Cylinder

## Wrapper Macro

CreateCylinderFrustum(...)

## Ribbon-GUI-Location

Geometry > Part > Cylinder

## Command Description

create cylinder part

## Argument List

**Arg1: dlOrigin**

Description: array double values of origin

Data Type: double list

Default Value : [0,0,0]

Syntax: dlOrigin = [1.0, 2.0]

**Arg2: dTopRadius**

Description: double value of top radius

Data Type: double

Default Value : 0.01

Syntax: dTopRadius = 1.0

**Arg3: dBotRadius**

Description: double value of bot radius

Data Type: double

Default Value : 0.01

Syntax: dBotRadius = 1.0

**Arg4: dHeight**

Description: double value of height

Data Type: double

Default Value : 0.01

Syntax: dHeight = 1.0

**Arg5: iCircleNodeCnt**

Description: option for circle node count

Data Type: integer

Default Value : 36

Syntax: iCircleNodeCnt = 1

**Arg6: iAxisNodeCnt**

Description: option for axis node count

Data Type: integer

Default Value : 10

Syntax: iAxisNodeCnt = 1

**Arg7: strName**

Description: definition string of input name

Data Type: string

Default Value : "Cylinder_1"

Syntax: strName = "string input"

**Arg8: iPartCol**

Description: option for part col

Data Type: integer

Default Value : 7105764

Syntax: iPartCol = 1

**Arg9: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Part.Cylinder(dlOrigin=[0,0,0], dTopRadius=0.01, dBotRadius=0.01, dHeight=0.01, iCircleNodeCnt=36, iAxisNodeCnt=10, strName="Cylinder_1", iPartCol=7105764, crCoord=None)

```

==========================================================

# Geometry.Part.Tube

## Wrapper Macro

CreateCylinderTube(...)

## Ribbon-GUI-Location

Geometry > Part > Tube

## Command Description

create tube part

## Argument List

**Arg1: dlOrigin**

Description: array double values of origin

Data Type: double list

Default Value : [0,0,0]

Syntax: dlOrigin = [1.0, 2.0]

**Arg2: dTopInnerRadius**

Description: double value of top inner radius

Data Type: double

Default Value : 0.001

Syntax: dTopInnerRadius = 1.0

**Arg3: dTopOuterRadius**

Description: double value of top outer radius

Data Type: double

Default Value : 0.01

Syntax: dTopOuterRadius = 1.0

**Arg4: dBotInnerRadius**

Description: double value of bot inner radius

Data Type: double

Default Value : 0.001

Syntax: dBotInnerRadius = 1.0

**Arg5: dBotOuterRadius**

Description: double value of bot outer radius

Data Type: double

Default Value : 0.01

Syntax: dBotOuterRadius = 1.0

**Arg6: dHeight**

Description: double value of height

Data Type: double

Default Value : 0.01

Syntax: dHeight = 1.0

**Arg7: iCircleNodeCnt**

Description: option for circle node count

Data Type: integer

Default Value : 36

Syntax: iCircleNodeCnt = 1

**Arg8: iAxisNodeCnt**

Description: option for axis node count

Data Type: integer

Default Value : 10

Syntax: iAxisNodeCnt = 1

**Arg9: strName**

Description: definition string of input name

Data Type: string

Default Value : "Cylinder_1"

Syntax: strName = "string input"

**Arg10: iPartCol**

Description: option for part col

Data Type: integer

Default Value : 7105764

Syntax: iPartCol = 1

**Arg11: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Part.Tube(dlOrigin=[0,0,0], dTopInnerRadius=0.001, dTopOuterRadius=0.01, dBotInnerRadius=0.001, dBotOuterRadius=0.01, dHeight=0.01, iCircleNodeCnt=36, iAxisNodeCnt=10, strName="Cylinder_1", iPartCol=7105764, crCoord=None)

```

==========================================================

# Geometry.Part.Trapezoid

## Wrapper Macro

CreateTrapezoid(...)

## Ribbon-GUI-Location

Geometry > Part > Trapezoid

## Command Description

Create trapezoid part

## Argument List

**Arg1: dlOrigin**

Description: array double values of origin

Data Type: double list

Default Value : [0.0,0.0,0.0]

Syntax: dlOrigin = [1.0, 2.0]

**Arg2: dlLength**

Description: array double values of length

Data Type: double list

Default Value : [0.01

Syntax: dlLength = [1.0, 2.0]

**Arg5: dTopXLength**

Description: double value of top x length

Data Type: double

Default Value : 7.0

Syntax: dTopXLength = 1.0

**Arg6: dRadius**

Description: double value of radius

Data Type: double

Default Value : 0

Syntax: dRadius = 1.0

**Arg7: ilNodeCnt**

Description: array int values of node count

Data Type: int list

Default Value : [10

Syntax: ilNodeCnt = [1,2,3,4]

**Arg10: strPartName**

Description: definition string of input part name

Data Type: string

Default Value : "Trapezoid_1"

Syntax: strPartName = "string input"

**Arg11: iColorPart**

Description: option for color part

Data Type: integer

Default Value : 710

Syntax: iColorPart = 1

**Arg12: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Part.Trapezoid(dlOrigin=[0.0,0.0,0.0], dlLength=[0.01, 0.01, 0.01], dTopXLength=7.0, dRadius=0, ilNodeCnt=[10, 10, 10], strPartName="Trapezoid_1", iColorPart=7105764, crCoord=None)

```

==========================================================

# Geometry.Part.Cone

## Wrapper Macro

CreateCone(...)

## Ribbon-GUI-Location

Geometry > Part > Cone

## Command Description

Create Cone Body

## Argument List

**Arg1: dlOriginXyz**

Description: array double values of origin xyz

Data Type: double list

Default Value : [0,0,0]

Syntax: dlOriginXyz = [1.0, 2.0]

**Arg2: dBottomRadius**

Description: double value of bottom radius

Data Type: double

Default Value : 0.01

Syntax: dBottomRadius = 1.0

**Arg3: dHeight**

Description: double value of height

Data Type: double

Default Value : 0.02

Syntax: dHeight = 1.0

**Arg4: iCircleNodeCount**

Description: option for circle node count

Data Type: integer

Default Value : 20

Syntax: iCircleNodeCount = 1

**Arg5: iAxisNodeCnt**

Description: option for axis node count

Data Type: integer

Default Value : 20

Syntax: iAxisNodeCnt = 1

**Arg6: strPartName**

Description: definition string of input part name

Data Type: string

Default Value : "Cone_1"

Syntax: strPartName = "string input"

**Arg7: iPartColor**

Description: option for part color

Data Type: integer

Default Value : 7105764

Syntax: iPartColor = 1

**Arg8: crCoordinate**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoordinate = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Part.Cone(dlOriginXyz=[0,0,0], dBottomRadius=0.01, dHeight=0.02, iCircleNodeCount=20, iAxisNodeCnt=20, strPartName="Cone_1", iPartColor=7105764, crCoordinate=None)

```

==========================================================

# Geometry.Transform.Rotation

## Wrapper Macro

RotateBody(...)

## Ribbon-GUI-Location

Geometry > Transform > Rotation

## Command Description

Rotate the selected Part.

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: posCenter**

Description: array double value [x, y, z] in coordinate system of center

Data Type: position

Default Value : [0,0,0]

Syntax: posCenter = [x, y, z]

**Arg3: vecAxis**

Description: array values of axis

Data Type: vector

Default Value : [1,0,0]

Syntax: vecAxis = [value1, value2, value3]

**Arg4: dAngle**

Description: double value of angle

Data Type: double

Default Value : 0

Syntax: dAngle = 1.0

**Arg5: bCreateNewPart**

Description: enable or disable feature create new part

Data Type: bool

Default Value : False

Syntax: bCreateNewPart = True/False

**Arg6: bCopyLBC**

Description: enable or disable feature copy load-boundary-condition

Data Type: bool

Default Value : False

Syntax: bCopyLBC = True/False

**Arg7: bCopyProperty**

Description: enable or disable feature copy property

Data Type: bool

Default Value : False

Syntax: bCopyProperty = True/False

**Arg8: iCopyCount**

Description: option for copy count

Data Type: integer

Default Value : 1

Syntax: iCopyCount = 1

**Arg9: bMergeNode**

Description: enable or disable feature merge node

Data Type: bool

Default Value : False

Syntax: bMergeNode = True/False

**Arg10: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1.0e-5

Syntax: dTol = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Transform.Rotation(crlPart=[], posCenter=[0,0,0], vecAxis=[1,0,0], dAngle=0, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, iCopyCount=1, bMergeNode=False, dTol=1.0e-5)

```

==========================================================

# Geometry.Transform.Scaling

## Wrapper Macro

ScaleBody(...)

## Ribbon-GUI-Location

Geometry > Transform > Scaling

## Command Description

Scale Body

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: dlScaleVector**

Description: array double values of scale vector

Data Type: double list

Default Value : [1.0,1.0,1.0]

Syntax: dlScaleVector = [1.0, 2.0]

**Arg3: dlScaleCentre**

Description: array double values of scale centre

Data Type: double list

Default Value : [0.0,0.0,0.0]

Syntax: dlScaleCentre = [1.0, 2.0]

**Arg4: crCoordinate**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoordinate = EntityType(id)

**Arg5: bCreateNew**

Description: enable or disable feature create new

Data Type: bool

Default Value : False

Syntax: bCreateNew = True/False

**Arg6: bCopyLbc**

Description: enable or disable feature copy lbc

Data Type: bool

Default Value : False

Syntax: bCopyLbc = True/False

**Arg7: bCopyProperty**

Description: enable or disable feature copy property

Data Type: bool

Default Value : False

Syntax: bCopyProperty = True/False

**Arg8: bUsepartcenter**

Description: enable or disable feature usepartcenter

Data Type: bool

Default Value : True

Syntax: bUsepartcenter = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Transform.Scaling(crlPart=[], dlScaleVector=[1.0,1.0,1.0], dlScaleCentre=[0.0,0.0,0.0], crCoordinate=None, bCreateNew=False, bCopyLbc=False, bCopyProperty=False, bUsepartcenter=True)

```

==========================================================

# Geometry.Transform.Mirror

## Wrapper Macro

MirrorBody(...)

## Ribbon-GUI-Location

Geometry > Transform > Mirror

## Command Description

mirror body

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: veclPoint**

Description: two dimensional array of point

Data Type: vector list

Default Value : [[0.0

Syntax: veclPoint = [[value1, value2, value3], [value1, value2, value3]]

**Arg5: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0.0

Syntax: dOffset = 1.0

**Arg6: bCreateNewPart**

Description: enable or disable feature create new part

Data Type: bool

Default Value : True

Syntax: bCreateNewPart = True/False

**Arg7: bCopyLBC**

Description: enable or disable feature copy load-boundary-condition

Data Type: bool

Default Value : False

Syntax: bCopyLBC = True/False

**Arg8: bCopyProperty**

Description: enable or disable feature copy property

Data Type: bool

Default Value : False

Syntax: bCopyProperty = True/False

**Arg9: bRemoveDupFace**

Description: enable or disable feature remove dup face

Data Type: bool

Default Value : True

Syntax: bRemoveDupFace = True/False

**Arg10: bMergeNode**

Description: enable or disable feature merge node

Data Type: bool

Default Value : False

Syntax: bMergeNode = True/False

**Arg11: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 1e-05

Syntax: dTol = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Transform.Mirror(crlPart=[], veclPoint=[[0.0, 0.0, 0.0]], dOffset=0.0, bCreateNewPart=True, bCopyLBC=False, bCopyProperty=False, bRemoveDupFace=True, bMergeNode=False, dTol=1e-05)

```

==========================================================

# Geometry.Transform.Position

## Wrapper Macro

PositionBody(...)

## Ribbon-GUI-Location

Geometry > Transform > Position

## Command Description

transform position

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: veclPoint**

Description: two dimensional array of point

Data Type: vector list

Default Value : [[0.0

Syntax: veclPoint = [[value1, value2, value3], [value1, value2, value3]]

**Arg5: bCreateNewPart**

Description: enable or disable feature create new part

Data Type: bool

Default Value : False

Syntax: bCreateNewPart = True/False

**Arg6: bCopyLBC**

Description: enable or disable feature copy load-boundary-condition

Data Type: bool

Default Value : False

Syntax: bCopyLBC = True/False

**Arg7: bCopyProperty**

Description: enable or disable feature copy property

Data Type: bool

Default Value : False

Syntax: bCopyProperty = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Transform.Position(crlPart=[], veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False)

```

==========================================================

# Geometry.Transform.Translation

## Wrapper Macro

TranslateBody(...)

## Ribbon-GUI-Location

Geometry > Transform > Translation

## Command Description

Translate the selected Part.

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: poslTranslates**

Description: list positions [x, y, z] in coordinate system of translates

Data Type: position list

Default Value : []

Syntax: poslTranslates = [[x, y, z], [x, y, z]]

**Arg3: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg4: bCreateNewPart**

Description: enable or disable feature create new part

Data Type: bool

Default Value : False

Syntax: bCreateNewPart = True/False

**Arg5: bCopyLBC**

Description: enable or disable feature copy load-boundary-condition

Data Type: bool

Default Value : False

Syntax: bCopyLBC = True/False

**Arg6: bCopyProperty**

Description: enable or disable feature copy property

Data Type: bool

Default Value : False

Syntax: bCopyProperty = True/False

**Arg7: iCopyCount**

Description: option for copy count

Data Type: integer

Default Value : 1

Syntax: iCopyCount = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Transform.Translation(crlPart=[], poslTranslates=[], crCoord=None, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, iCopyCount=1)

```

==========================================================

# Geometry.Transform.MatingFace

## Wrapper Macro

TransMatingFace(...)

## Ribbon-GUI-Location

Geometry > Transform > MatingFace

## Command Description

Transform MatingFace

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crSrcFace**

Description: entity in database model with type src face

Data Type: cursor

Default Value : None

Syntax: crSrcFace = EntityType(id)

**Arg3: crDstFace**

Description: entity in database model with type dst face

Data Type: cursor

Default Value : None

Syntax: crDstFace = EntityType(id)

**Arg4: crSrcEdge**

Description: entity in database model with type src edge

Data Type: cursor

Default Value : None

Syntax: crSrcEdge = EntityType(id)

**Arg5: crDstEdge**

Description: entity in database model with type dst edge

Data Type: cursor

Default Value : None

Syntax: crDstEdge = EntityType(id)

**Arg6: crSrcNode**

Description: entity in database model with type src node

Data Type: cursor

Default Value : None

Syntax: crSrcNode = EntityType(id)

**Arg7: crDstNode**

Description: entity in database model with type dst node

Data Type: cursor

Default Value : None

Syntax: crDstNode = EntityType(id)

**Arg8: iFaceOpposite**

Description: option for face opposite

Data Type: integer

Default Value : 0

Syntax: iFaceOpposite = 1

**Arg9: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 0

Syntax: dEdgeAngle = 1.0

**Arg10: iEdgeOpposite**

Description: option for edge opposite

Data Type: integer

Default Value : 0

Syntax: iEdgeOpposite = 1

**Arg11: iAlignMethodType**

Description: option for align method type

Data Type: integer

Default Value : 0

Syntax: iAlignMethodType = 1

**Arg12: iAdjustPointType**

Description: option for adjust point type

Data Type: integer

Default Value : 0

Syntax: iAdjustPointType = 1

**Arg13: iAdjustProjectionType**

Description: option for adjust projection type

Data Type: integer

Default Value : 0

Syntax: iAdjustProjectionType = 1

**Arg14: dlAlignVector**

Description: array double values of align vector

Data Type: double list

Default Value : [0

Syntax: dlAlignVector = [1.0, 2.0]

**Arg17: dlAdjustPoint**

Description: array double values of adjust point

Data Type: double list

Default Value : [0

Syntax: dlAdjustPoint = [1.0, 2.0]

**Arg20: dlAdjustVector**

Description: array double values of adjust vector

Data Type: double list

Default Value : [0

Syntax: dlAdjustVector = [1.0, 2.0]

**Arg23: bCreateNewPart**

Description: enable or disable feature create new part

Data Type: bool

Default Value : False

Syntax: bCreateNewPart = True/False

**Arg24: bCopyLBC**

Description: enable or disable feature copy load-boundary-condition

Data Type: bool

Default Value : False

Syntax: bCopyLBC = True/False

**Arg25: bCopyProperty**

Description: enable or disable feature copy property

Data Type: bool

Default Value : False

Syntax: bCopyProperty = True/False

**Arg26: bIsPreview**

Description: enable or disable feature is preview

Data Type: bool

Default Value : False

Syntax: bIsPreview = True/False

**Arg27: crlCoordSyss**

Description: array entities in model with type coordinate syss

Data Type: cursor list

Default Value : []

Syntax: crlCoordSyss = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Transform.MatingFace(crlPart=[], crSrcFace=None, crDstFace=None, crSrcEdge=None, crDstEdge=None, crSrcNode=None, crDstNode=None, iFaceOpposite=0, dEdgeAngle=0, iEdgeOpposite=0, iAlignMethodType=0, iAdjustPointType=0, iAdjustProjectionType=0, dlAlignVector=[0, 0, 0], dlAdjustPoint=[0, 0, 0], dlAdjustVector=[0, 0, 0], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, bIsPreview=False, crlCoordSyss=[])

```

==========================================================

# Geometry.Transform.CylinderFace

## Wrapper Macro

Transform_CylinderFace(...)

## Ribbon-GUI-Location

Geometry > Transform > CylinderFace

## Command Description

transform position

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: veclPoint**

Description: two dimensional array of point

Data Type: vector list

Default Value : [[0.0

Syntax: veclPoint = [[value1, value2, value3], [value1, value2, value3]]

**Arg5: bCreateNewPart**

Description: enable or disable feature create new part

Data Type: bool

Default Value : False

Syntax: bCreateNewPart = True/False

**Arg6: bCopyLBC**

Description: enable or disable feature copy load-boundary-condition

Data Type: bool

Default Value : False

Syntax: bCopyLBC = True/False

**Arg7: bCopyProperty**

Description: enable or disable feature copy property

Data Type: bool

Default Value : False

Syntax: bCopyProperty = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.Transform.CylinderFace(crlPart=[], veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False)

```

==========================================================

# Geometry.CADTrim

## Wrapper Macro

GeometryCADTrim(...)

## Ribbon-GUI-Location

Geometry > CADTrim

## Command Description

CAD Trim

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg3: dTrimSize**

Description: double value of trim size

Data Type: double

Default Value : 1

Syntax: dTrimSize = 1.0

**Arg4: dTrimAngle**

Description: double value of trim angle

Data Type: double

Default Value : 15

Syntax: dTrimAngle = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.CADTrim(crlFace=[], crlPart=[], dTrimSize=1, dTrimAngle=15)

```

==========================================================

# Geometry.StitchEdge

## Wrapper Macro

StitchEdge(...)

## Ribbon-GUI-Location

Geometry > StitchEdge

## Command Description

Stitch Edges

## Argument List

**Arg1: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 0.3

Syntax: dTolerance = 1.0

**Arg2: bKeepSlave**

Description: enable or disable feature keep slave

Data Type: bool

Default Value : True

Syntax: bKeepSlave = True/False

**Arg3: crlMaster**

Description: array entities in model with type master

Data Type: cursor list

Default Value : []

Syntax: crlMaster = [EntityType(id1, id2, id3)]

**Arg4: crlSlave**

Description: array entities in model with type slave

Data Type: cursor list

Default Value : []

Syntax: crlSlave = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.StitchEdge(dTolerance=0.3, bKeepSlave=True, crlMaster=[], crlSlave=[])

```

==========================================================

# Geometry.LogoRemoval

## Wrapper Macro

LogoRemoval(...)

## Ribbon-GUI-Location

Geometry > LogoRemoval

## Command Description

Create Face From Edges

## Argument List

**Arg1: crlStartFaces**

Description: array entities in model with type start faces

Data Type: cursor list

Default Value : []

Syntax: crlStartFaces = [EntityType(id1, id2, id3)]

**Arg2: crlStopFaces**

Description: array entities in model with type stop faces

Data Type: cursor list

Default Value : []

Syntax: crlStopFaces = [EntityType(id1, id2, id3)]

**Arg3: iLayers**

Description: option for layers

Data Type: integer

Default Value : 5

Syntax: iLayers = 1

**Arg4: bMergeFaces**

Description: enable or disable feature merge faces

Data Type: bool

Default Value : False

Syntax: bMergeFaces = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.LogoRemoval(crlStartFaces=[], crlStopFaces=[], iLayers=5, bMergeFaces=False)

```

==========================================================

# Geometry.ShellAsm

## Wrapper Macro

ShellAsm(...)

## Ribbon-GUI-Location

Geometry > ShellAsm

## Command Description

assemble the separated parts

## Argument List

**Arg1: crlPartK**

Description: array entities in model with type part k

Data Type: cursor list

Default Value : []

Syntax: crlPartK = [EntityType(id1, id2, id3)]

**Arg2: crlFaceK**

Description: array entities in model with type face k

Data Type: cursor list

Default Value : []

Syntax: crlFaceK = [EntityType(id1, id2, id3)]

**Arg3: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 0.2

Syntax: dTol = 1.0

**Arg4: iElemType**

Description: option for element type

Data Type: integer

Default Value : 0

Syntax: iElemType = 1

**Arg5: bSkipTiny**

Description: enable or disable feature skip tiny

Data Type: bool

Default Value : False

Syntax: bSkipTiny = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.ShellAsm(crlPartK=[], crlFaceK=[], dTol=0.2, iElemType=0, bSkipTiny=False)

```

==========================================================

# Geometry.SquareUpFillet

## Wrapper Macro

SquareUpFillet(...)

## Ribbon-GUI-Location

Geometry > SquareUpFillet

## Command Description

Square Up Fillet

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.SquareUpFillet(crlFace=[])

```

==========================================================

# Geometry.MakeFillet

## Wrapper Macro

MakeFillet(...)

## Ribbon-GUI-Location

Geometry > MakeFillet

## Command Description

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg2: dRadius**

Description: double value of radius

Data Type: double

Default Value : 1.0

Syntax: dRadius = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.MakeFillet(crlEdge=[], dRadius=1.0)

```

==========================================================

# Geometry.MakeFacePlanar

## Wrapper Macro

MakeFacePlanar(...)

## Ribbon-GUI-Location

Geometry > MakeFacePlanar

## Command Description

Make planar faces by given plane points

## Argument List

**Arg1: dlPlanePt1**

Description: array double values of plane pt1

Data Type: double list

Default Value : [0.0,0.0,0.0]

Syntax: dlPlanePt1 = [1.0, 2.0]

**Arg2: dlPlanePt2**

Description: array double values of plane pt2

Data Type: double list

Default Value : [0.0,0.0,0.0]

Syntax: dlPlanePt2 = [1.0, 2.0]

**Arg3: dlPlanePt3**

Description: array double values of plane pt3

Data Type: double list

Default Value : [0.0,0.0,0.0]

Syntax: dlPlanePt3 = [1.0, 2.0]

**Arg4: ilFaceIds**

Description: array int values of face ids

Data Type: int list

Default Value : []

Syntax: ilFaceIds = [1,2,3,4]

**Arg5: iMergeFace**

Description: option for merge face

Data Type: integer

Default Value : 0

Syntax: iMergeFace = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.MakeFacePlanar(dlPlanePt1=[0.0,0.0,0.0], dlPlanePt2=[0.0,0.0,0.0], dlPlanePt3=[0.0,0.0,0.0], ilFaceIds=[], iMergeFace=0)

```

==========================================================

# Geometry.FCircleAdjustVertex

## Wrapper Macro

MeshEditAdjustVertex(...)

## Ribbon-GUI-Location

Geometry > FCircleAdjustVertex

## Command Description

adjust vertex in circle

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.FCircleAdjustVertex(crlPart=[])

```

==========================================================

# Geometry.AdjustHalfCylinder

## Wrapper Macro

MeshEditAdjustHalfCylinderCoordinateCr(...)

## Ribbon-GUI-Location

Geometry > AdjustHalfCylinder

## Command Description

Adjust half cylinder

## Argument List

**Arg1: poslPoint**

Description: list positions [x, y, z] in coordinate system of point

Data Type: position list

Default Value : []

Syntax: poslPoint = [[x, y, z], [x, y, z]]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg4: iAxisPlane**

Description: option for axis plane

Data Type: integer

Default Value : 0

Syntax: iAxisPlane = 1

**Arg5: bDivideFace**

Description: enable or disable feature divide face

Data Type: bool

Default Value : True

Syntax: bDivideFace = True/False

**Arg6: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg7: bMergeEdge**

Description: enable or disable feature merge edge

Data Type: bool

Default Value : True

Syntax: bMergeEdge = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.AdjustHalfCylinder(poslPoint=[], crlFace=[], crCoord=None, iAxisPlane=0, bDivideFace=True, crlPart=[], bMergeEdge=True)

```

==========================================================

# Geometry.FCircVertexAdjust

## Wrapper Macro

MeshEditGeomEditDivideCylinderBy90Deg(...)

## Ribbon-GUI-Location

Geometry > FCircVertexAdjust

## Command Description

FCirc Vertex Adjust

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: dMinRadius**

Description: double value of minimize radius

Data Type: double

Default Value : 0.0

Syntax: dMinRadius = 1.0

**Arg3: bFullCylinder**

Description: enable or disable feature full cylinder

Data Type: bool

Default Value : True

Syntax: bFullCylinder = True/False

**Arg4: bCylinderMorethan90**

Description: enable or disable feature cylinder morethan90

Data Type: bool

Default Value : False

Syntax: bCylinderMorethan90 = True/False

**Arg5: bSkipFaceHaveLocalSetting**

Description: enable or disable feature skip face have local setting

Data Type: bool

Default Value : False

Syntax: bSkipFaceHaveLocalSetting = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.FCircVertexAdjust(crlPart=[], dMinRadius=0.0, bFullCylinder=True, bCylinderMorethan90=False, bSkipFaceHaveLocalSetting=False)

```

==========================================================

# Geometry.ExtractSurfaces

## Wrapper Macro

MeshEditExtractSurfaces(...)

## Ribbon-GUI-Location

Geometry > ExtractSurfaces

## Command Description

Extract Reference Surfaces

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dAngle**

Description: double value of angle

Data Type: double

Default Value : 60.0

Syntax: dAngle = 1.0

**Arg3: strName**

Description: definition string of input name

Data Type: string

Default Value : "ExtractFace_1"

Syntax: strName = "string input"

**Arg4: bMergePart**

Description: enable or disable feature merge part

Data Type: bool

Default Value : False

Syntax: bMergePart = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.ExtractSurfaces(crlFace=[], dAngle=60.0, strName="ExtractFace_1", bMergePart=False)

```

==========================================================

# Geometry.RemoveRibBoss

## Wrapper Macro

Remove_Rib_Boss(...)

## Ribbon-GUI-Location

Geometry > RemoveRibBoss

## Command Description

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dGradiation**

Description: double value of gradiation

Data Type: double

Default Value : 1.0

Syntax: dGradiation = 1.0

**Arg3: iContinuity**

Description: option for continuity

Data Type: integer

Default Value : 1

Syntax: iContinuity = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.RemoveRibBoss(crlFace=[], dGradiation=1.0, iContinuity=1)

```

==========================================================

# Geometry.AdvancedShellAssembly

## Wrapper Macro

ShellAssyGeneral(...)

## Ribbon-GUI-Location

Geometry > AdvancedShellAssembly

## Command Description

Test shell assembly

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: iMeshType**

Description: option for mesh type

Data Type: integer

Default Value : 0

Syntax: iMeshType = 1

**Arg4: bSelfIntersection**

Description: enable or disable feature self intersection

Data Type: bool

Default Value : False

Syntax: bSelfIntersection = True/False

**Arg5: iMethod**

Description: option for method

Data Type: integer

Default Value : 3

Syntax: iMethod = 1

**Arg6: dGapTol**

Description: double value of gap tolerance

Data Type: double

Default Value : 2.1

Syntax: dGapTol = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.AdvancedShellAssembly(crlPart=[], crlFace=[], iMeshType=0, bSelfIntersection=False, iMethod=3, dGapTol=2.1)

```

==========================================================

# Geometry.ExtractRefSurface

## Wrapper Macro

MeshEditExtractRefSurfaces(...)

## Ribbon-GUI-Location

Geometry > ExtractRefSurface

## Command Description

Command use for Geometry ExtractRefSurface

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dAngle**

Description: double value of angle

Data Type: double

Default Value : 60.0

Syntax: dAngle = 1.0

**Arg3: strName**

Description: definition string of input name

Data Type: string

Default Value : "ExtractFace_1"

Syntax: strName = "string input"

**Arg4: bMergePart**

Description: enable or disable feature merge part

Data Type: bool

Default Value : False

Syntax: bMergePart = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Geometry.ExtractRefSurface(crlFace=[], dAngle=60.0, strName="ExtractFace_1", bMergePart=False)

```

==========================================================

# Groups.RightClick.PropertyGroup

## Wrapper Macro

CreatePropertyGroup(...)

## Ribbon-GUI-Location

Groups > RightClick > PropertyGroup

## Command Description

create group of properties

## Argument List

**Arg1: strTmp**

Description: definition string of input tmp

Data Type: string

Default Value : ""

Syntax: strTmp = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Groups.RightClick.PropertyGroup(strTmp="")

```

==========================================================

# Groups.RightClick.Rename

## Wrapper Macro

RenameItem(...)

## Ribbon-GUI-Location

Groups > RightClick > Rename

## Command Description

Command use for Groups RightClick Rename

## Argument List

**Arg1: strNewName**

Description: definition string of input new name

Data Type: string

Default Value : ""

Syntax: strNewName = "string input"

**Arg2: crItem**

Description: entity in database model with type item

Data Type: cursor

Default Value : None

Syntax: crItem = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Groups.RightClick.Rename(strNewName="", crItem=None)

```

==========================================================

# Groups.RightClick.DeleteGroup

## Wrapper Macro

DeleteGroup(...)

## Ribbon-GUI-Location

Groups > RightClick > DeleteGroup

## Command Description

Delete Group

## Argument List

**Arg1: crlDelGroup**

Description: array entities in model with type delete group

Data Type: cursor list

Default Value : []

Syntax: crlDelGroup = [EntityType(id1, id2, id3)]

**Arg2: bRemoveAll**

Description: enable or disable feature remove all

Data Type: bool

Default Value : False

Syntax: bRemoveAll = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Groups.RightClick.DeleteGroup(crlDelGroup=[], bRemoveAll=False)

```

==========================================================

# Groups.RightClick.CopyGroup

## Wrapper Macro

CopyGroup(...)

## Ribbon-GUI-Location

Groups > RightClick > CopyGroup

## Command Description

Copy Group

## Argument List

**Arg1: crlSrc**

Description: array entities in model with type src

Data Type: cursor list

Default Value : []

Syntax: crlSrc = [EntityType(id1, id2, id3)]

**Arg2: strlNames**

Description: list definition string of names

Data Type: string list

Default Value : []

Syntax: strlNames = ["str1", "str2", "str3"]

**Arg3: crDest**

Description: entity in database model with type dest

Data Type: cursor

Default Value : None

Syntax: crDest = EntityType(id)

**Arg4: bKeep**

Description: enable or disable feature keep

Data Type: bool

Default Value : 0

Syntax: bKeep = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Groups.RightClick.CopyGroup(crlSrc=[], strlNames=[], crDest=None, bKeep=0)

```

==========================================================

# Groups.RightClick.AddSupGroup

## Wrapper Macro

AddSupGroup(...)

## Ribbon-GUI-Location

Groups > RightClick > AddSupGroup

## Command Description

Add supper group

## Argument List

**Arg1: crSupGroupSelected**

Description: entity in database model with type sup group selected

Data Type: cursor

Default Value : None

Syntax: crSupGroupSelected = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Groups.RightClick.AddSupGroup(crSupGroupSelected=None)

```

==========================================================

# Groups.RightClick.CreateMatGroup

## Wrapper Macro

CreateMaterialGroup(...)

## Ribbon-GUI-Location

Groups > RightClick > CreateMatGroup

## Command Description

Command use for Groups RightClick CreateMatGroup

## Argument List

**Arg1: strTmp**

Description: definition string of input tmp

Data Type: string

Default Value : ""

Syntax: strTmp = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Groups.RightClick.CreateMatGroup(strTmp="")

```

==========================================================

# HexModeling.Sweep.Circular

## Wrapper Macro

HexSweepCircular(...)

## Ribbon-GUI-Location

HexModeling > Sweep > Circular

## Command Description

Command use for HexModeling Sweep Circular

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dAngle**

Description: double value of angle

Data Type: double

Default Value : 360

Syntax: dAngle = 1.0

**Arg3: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 0.0000001

Syntax: dTol = 1.0

**Arg4: iLayer**

Description: option for layer

Data Type: integer

Default Value : 36

Syntax: iLayer = 1

**Arg5: vecAxisPt**

Description: array values of axis pt

Data Type: vector

Default Value : [0.0,0.0,0.0]

Syntax: vecAxisPt = [value1, value2, value3]

**Arg6: vecAxisVect**

Description: array values of axis vect

Data Type: vector

Default Value : [1.0,0.0,0.0]

Syntax: vecAxisVect = [value1, value2, value3]

**Arg7: bInterfaceElem**

Description: enable or disable feature interface element

Data Type: bool

Default Value : False

Syntax: bInterfaceElem = True/False

**Arg8: bExtrusion**

Description: enable or disable feature extrusion

Data Type: bool

Default Value : False

Syntax: bExtrusion = True/False

**Arg9: dTranslationExtrusion**

Description: double value of translation extrusion

Data Type: double

Default Value : 0.0

Syntax: dTranslationExtrusion = 1.0

**Arg10: dBDeleteOriginalParts**

Description: double value of b delete original parts

Data Type: double

Default Value : 0.0

Syntax: dBDeleteOriginalParts = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.Sweep.Circular(crlFace=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0)

```

==========================================================

# HexModeling.Sweep.FaceToFace

## Wrapper Macro

HexSweepFaceToFace(...)

## Ribbon-GUI-Location

HexModeling > Sweep > FaceToFace

## Command Description

Command use for HexModeling Sweep FaceToFace

## Argument List

**Arg1: crSrcFace**

Description: entity in database model with type src face

Data Type: cursor

Default Value : None

Syntax: crSrcFace = EntityType(id)

**Arg2: crDstFace**

Description: entity in database model with type dst face

Data Type: cursor

Default Value : None

Syntax: crDstFace = EntityType(id)

**Arg3: bDeleteOriginalParts**

Description: enable or disable feature delete original parts

Data Type: bool

Default Value : True

Syntax: bDeleteOriginalParts = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.Sweep.FaceToFace(crSrcFace=None, crDstFace=None, bDeleteOriginalParts=True)

```

==========================================================

# HexModeling.Sweep.Layer

## Wrapper Macro

HexSweepLayer(...)

## Ribbon-GUI-Location

HexModeling > Sweep > Layer

## Command Description

Command use for HexModeling Sweep Layer

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dFrontWidth**

Description: double value of front width

Data Type: double

Default Value : 0.0

Syntax: dFrontWidth = 1.0

**Arg3: dBackWidth**

Description: double value of back width

Data Type: double

Default Value : 0.0

Syntax: dBackWidth = 1.0

**Arg4: iFrontLayers**

Description: option for front layers

Data Type: integer

Default Value : 1

Syntax: iFrontLayers = 1

**Arg5: iBackLayers**

Description: option for back layers

Data Type: integer

Default Value : 0

Syntax: iBackLayers = 1

**Arg6: iBaseFaceType**

Description: option for base face type

Data Type: integer

Default Value : 0

Syntax: iBaseFaceType = 1

**Arg7: iSeparate**

Description: option for separate

Data Type: integer

Default Value : 0

Syntax: iSeparate = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.Sweep.Layer(crlFace=[], dFrontWidth=0.0, dBackWidth=0.0, iFrontLayers=1, iBackLayers=0, iBaseFaceType=0, iSeparate=0)

```

==========================================================

# HexModeling.Sweep.Linear

## Wrapper Macro

HexSweepLinear(...)

## Ribbon-GUI-Location

HexModeling > Sweep > Linear

## Command Description

Command use for HexModeling Sweep Linear

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dLength**

Description: double value of length

Data Type: double

Default Value : 10

Syntax: dLength = 1.0

**Arg3: iLayer**

Description: option for layer

Data Type: integer

Default Value : 10

Syntax: iLayer = 1

**Arg4: dlSweepDirection**

Description: array double values of sweep direction

Data Type: double list

Default Value : []

Syntax: dlSweepDirection = [1.0, 2.0]

**Arg5: bInterfaceElemFlag**

Description: enable or disable feature interface element flag

Data Type: bool

Default Value : False

Syntax: bInterfaceElemFlag = True/False

**Arg6: iLinearMethod**

Description: option for linear method

Data Type: integer

Default Value : 0

Syntax: iLinearMethod = 1

**Arg7: bDeleteOriginalParts**

Description: enable or disable feature delete original parts

Data Type: bool

Default Value : False

Syntax: bDeleteOriginalParts = True/False

**Arg8: bDeleteTargetParts**

Description: enable or disable feature delete target parts

Data Type: bool

Default Value : False

Syntax: bDeleteTargetParts = True/False

**Arg9: iMethodBias**

Description: option for method bias

Data Type: integer

Default Value : 0

Syntax: iMethodBias = 1

**Arg10: dFactor**

Description: double value of factor

Data Type: double

Default Value : 2.0

Syntax: dFactor = 1.0

**Arg11: iProgression**

Description: option for progression

Data Type: integer

Default Value : 0

Syntax: iProgression = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.Sweep.Linear(crlFace=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0)

```

==========================================================

# HexModeling.Sweep.Curve

## Wrapper Macro

SweepCloseLoopShape(...)

## Ribbon-GUI-Location

HexModeling > Sweep > Curve

## Command Description

Command use for HexModeling Sweep Curve

## Argument List

**Arg1: crFace**

Description: entity in database model with type face

Data Type: cursor

Default Value : None

Syntax: crFace = EntityType(id)

**Arg2: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg3: crlRefEdge**

Description: array entities in model with type ref edge

Data Type: cursor list

Default Value : []

Syntax: crlRefEdge = [EntityType(id1, id2, id3)]

**Arg4: dMeshSize**

Description: double value of mesh size

Data Type: double

Default Value : 0.1

Syntax: dMeshSize = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.Sweep.Curve(crFace=None, crlEdge=[], crlRefEdge=[], dMeshSize=0.1)

```

==========================================================

# HexModeling.Sweep.FromMidPlane

## Wrapper Macro

Shell2Hex(...)

## Ribbon-GUI-Location

HexModeling > Sweep > FromMidPlane

## Command Description

Command use for HexModeling Sweep FromMidPlane

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: bRef**

Description: enable or disable feature ref

Data Type: bool

Default Value : True

Syntax: bRef = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.Sweep.FromMidPlane(crlPart=[], bRef=True)

```

==========================================================

# HexModeling.SolidElemInterface

## Wrapper Macro

SolidElemInterface(...)

## Ribbon-GUI-Location

HexModeling > SolidElemInterface

## Command Description

make solid element interface

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: bFlip**

Description: enable or disable feature flip

Data Type: bool

Default Value : False

Syntax: bFlip = True/False

**Arg3: crlElms**

Description: array entities in model with type elms

Data Type: cursor list

Default Value : []

Syntax: crlElms = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.SolidElemInterface(crlFace=[], bFlip=False, crlElms=[])

```

==========================================================

# HexModeling.BallHexa

## Wrapper Macro

HexModelingBallHexa(...)

## Ribbon-GUI-Location

HexModeling > BallHexa

## Command Description

hexa modeling ball hexa

## Argument List

**Arg1: crPart**

Description: entity in database model with type part

Data Type: cursor

Default Value : None

Syntax: crPart = EntityType(id)

**Arg2: vecCenter**

Description: array values of center

Data Type: vector

Default Value : [0.0,0.0,0.0]

Syntax: vecCenter = [value1, value2, value3]

**Arg3: dRadius**

Description: double value of radius

Data Type: double

Default Value : 5.0

Syntax: dRadius = 1.0

**Arg4: dMeshSize**

Description: double value of mesh size

Data Type: double

Default Value : 0.5

Syntax: dMeshSize = 1.0

**Arg5: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg6: iLayer**

Description: option for layer

Data Type: integer

Default Value : 3

Syntax: iLayer = 1

**Arg7: bMakeCenterNode**

Description: enable or disable feature make center node

Data Type: bool

Default Value : True

Syntax: bMakeCenterNode = True/False

**Arg8: strPartName**

Description: definition string of input part name

Data Type: string

Default Value : "HexBall_1"

Syntax: strPartName = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.BallHexa(crPart=None, vecCenter=[0.0,0.0,0.0], dRadius=5.0, dMeshSize=0.5, iType=0, iLayer=3, bMakeCenterNode=True, strPartName="HexBall_1")

```

==========================================================

# HexModeling.BoxMesh

## Wrapper Macro

HexBoxMesh(...)

## Ribbon-GUI-Location

HexModeling > BoxMesh

## Command Description

Box hex mesh creator for parts

## Argument List

**Arg1: ilPartIds**

Description: array int values of part ids

Data Type: int list

Default Value : []

Syntax: ilPartIds = [1,2,3,4]

**Arg2: dMeshSize**

Description: double value of mesh size

Data Type: double

Default Value : 0.0

Syntax: dMeshSize = 1.0

**Arg3: strMaterialName**

Description: definition string of input material name

Data Type: string

Default Value : ""

Syntax: strMaterialName = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.BoxMesh(ilPartIds=[], dMeshSize=0.0, strMaterialName="")

```

==========================================================

# HexModeling.AutoSweep

## Wrapper Macro

HexModelAutoSweep(...)

## Ribbon-GUI-Location

HexModeling > AutoSweep

## Command Description

Hex Modeling Auto Sweep

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: dMeshSize**

Description: double value of mesh size

Data Type: double

Default Value : 0.0

Syntax: dMeshSize = 1.0

**Arg3: bLayers**

Description: enable or disable feature layers

Data Type: bool

Default Value : False

Syntax: bLayers = True/False

**Arg4: iLayers**

Description: option for layers

Data Type: integer

Default Value : 2

Syntax: iLayers = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.AutoSweep(crlPart=[], dMeshSize=0.0, bLayers=False, iLayers=2)

```

==========================================================

# HexModeling.Circular

## Wrapper Macro

HexSweepCircular(...)

## Ribbon-GUI-Location

HexModeling > Circular

## Command Description

create Hexa mesh by revolving a surface

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dAngle**

Description: double value of angle

Data Type: double

Default Value : 360

Syntax: dAngle = 1.0

**Arg3: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 0.0000001

Syntax: dTol = 1.0

**Arg4: iLayer**

Description: option for layer

Data Type: integer

Default Value : 36

Syntax: iLayer = 1

**Arg5: vecAxisPt**

Description: array values of axis pt

Data Type: vector

Default Value : [0.0,0.0,0.0]

Syntax: vecAxisPt = [value1, value2, value3]

**Arg6: vecAxisVect**

Description: array values of axis vect

Data Type: vector

Default Value : [1.0,0.0,0.0]

Syntax: vecAxisVect = [value1, value2, value3]

**Arg7: bInterfaceElem**

Description: enable or disable feature interface element

Data Type: bool

Default Value : False

Syntax: bInterfaceElem = True/False

**Arg8: bExtrusion**

Description: enable or disable feature extrusion

Data Type: bool

Default Value : False

Syntax: bExtrusion = True/False

**Arg9: dTranslationExtrusion**

Description: double value of translation extrusion

Data Type: double

Default Value : 0.0

Syntax: dTranslationExtrusion = 1.0

**Arg10: dBDeleteOriginalParts**

Description: double value of b delete original parts

Data Type: double

Default Value : 0.0

Syntax: dBDeleteOriginalParts = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.Circular(crlFace=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0)

```

==========================================================

# HexModeling.FaceToFace

## Wrapper Macro

HexSweepFaceToFace(...)

## Ribbon-GUI-Location

HexModeling > FaceToFace

## Command Description

## Argument List

**Arg1: crSrcFace**

Description: entity in database model with type src face

Data Type: cursor

Default Value : None

Syntax: crSrcFace = EntityType(id)

**Arg2: crDstFace**

Description: entity in database model with type dst face

Data Type: cursor

Default Value : None

Syntax: crDstFace = EntityType(id)

**Arg3: bDeleteOriginalParts**

Description: enable or disable feature delete original parts

Data Type: bool

Default Value : True

Syntax: bDeleteOriginalParts = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.FaceToFace(crSrcFace=None, crDstFace=None, bDeleteOriginalParts=True)

```

==========================================================

# HexModeling.Layer

## Wrapper Macro

HexSweepLayer(...)

## Ribbon-GUI-Location

HexModeling > Layer

## Command Description

sweep by layer

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dFrontWidth**

Description: double value of front width

Data Type: double

Default Value : 0.0

Syntax: dFrontWidth = 1.0

**Arg3: dBackWidth**

Description: double value of back width

Data Type: double

Default Value : 0.0

Syntax: dBackWidth = 1.0

**Arg4: iFrontLayers**

Description: option for front layers

Data Type: integer

Default Value : 1

Syntax: iFrontLayers = 1

**Arg5: iBackLayers**

Description: option for back layers

Data Type: integer

Default Value : 0

Syntax: iBackLayers = 1

**Arg6: iBaseFaceType**

Description: option for base face type

Data Type: integer

Default Value : 0

Syntax: iBaseFaceType = 1

**Arg7: iSeparate**

Description: option for separate

Data Type: integer

Default Value : 0

Syntax: iSeparate = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.Layer(crlFace=[], dFrontWidth=0.0, dBackWidth=0.0, iFrontLayers=1, iBackLayers=0, iBaseFaceType=0, iSeparate=0)

```

==========================================================

# HexModeling.Linear

## Wrapper Macro

HexModelSweepLinear(...)

## Ribbon-GUI-Location

HexModeling > Linear

## Command Description

Linear hex mesh creation

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: dLength**

Description: double value of length

Data Type: double

Default Value : 10

Syntax: dLength = 1.0

**Arg3: iLayer**

Description: option for layer

Data Type: integer

Default Value : 10

Syntax: iLayer = 1

**Arg4: vecSweepDirection**

Description: array values of sweep direction

Data Type: vector

Default Value : []

Syntax: vecSweepDirection = [value1, value2, value3]

**Arg5: bInterfaceElemFlag**

Description: enable or disable feature interface element flag

Data Type: bool

Default Value : False

Syntax: bInterfaceElemFlag = True/False

**Arg6: iLinearMethod**

Description: option for linear method

Data Type: integer

Default Value : 0

Syntax: iLinearMethod = 1

**Arg7: bDeleteOriginalParts**

Description: enable or disable feature delete original parts

Data Type: bool

Default Value : False

Syntax: bDeleteOriginalParts = True/False

**Arg8: bDeleteTargetParts**

Description: enable or disable feature delete target parts

Data Type: bool

Default Value : False

Syntax: bDeleteTargetParts = True/False

**Arg9: iMethodBias**

Description: option for method bias

Data Type: integer

Default Value : 0

Syntax: iMethodBias = 1

**Arg10: dFactor**

Description: double value of factor

Data Type: double

Default Value : 2.0

Syntax: dFactor = 1.0

**Arg11: iProgression**

Description: option for progression

Data Type: integer

Default Value : 0

Syntax: iProgression = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.Linear(crlFace=[], dLength=10, iLayer=10, vecSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0)

```

==========================================================

# HexModeling.FromMidPlane

## Wrapper Macro

Shell2Hex(...)

## Ribbon-GUI-Location

HexModeling > FromMidPlane

## Command Description

HexModeling From MidPlane

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: bRef**

Description: enable or disable feature ref

Data Type: bool

Default Value : True

Syntax: bRef = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.FromMidPlane(crlPart=[], bRef=True)

```

==========================================================

# HexModeling.Curve

## Wrapper Macro

SweepCloseLoopShape(...)

## Ribbon-GUI-Location

HexModeling > Curve

## Command Description

make hex by sweeping curve

## Argument List

**Arg1: crFace**

Description: entity in database model with type face

Data Type: cursor

Default Value : None

Syntax: crFace = EntityType(id)

**Arg2: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg3: crlRefEdge**

Description: array entities in model with type ref edge

Data Type: cursor list

Default Value : []

Syntax: crlRefEdge = [EntityType(id1, id2, id3)]

**Arg4: dMeshSize**

Description: double value of mesh size

Data Type: double

Default Value : 0.1

Syntax: dMeshSize = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

HexModeling.Curve(crFace=None, crlEdge=[], crlRefEdge=[], dMeshSize=0.1)

```

==========================================================

# Home.ImportCAD.Elysium

## Wrapper Macro

ImportElysium(...)

## Ribbon-GUI-Location

Home > ImportCAD > Elysium

## Command Description

import elysium

## Argument List

**Arg1: strlPath**

Description: list definition string of path

Data Type: string list

Default Value : []

Syntax: strlPath = ["str1", "str2", "str3"]

**Arg2: dChordHeightTolerance**

Description: double value of chord height tolerance

Data Type: double

Default Value : 1.0

Syntax: dChordHeightTolerance = 1.0

**Arg3: dAngleToleranceDegree**

Description: double value of angle tolerance degree

Data Type: double

Default Value : 5.0

Syntax: dAngleToleranceDegree = 1.0

**Arg4: dPointCoincidentTolerance**

Description: double value of point coincident tolerance

Data Type: double

Default Value : 0.01

Syntax: dPointCoincidentTolerance = 1.0

**Arg5: iConvertIsolatedCurve**

Description: option for convert isolated curve

Data Type: integer

Default Value : 0

Syntax: iConvertIsolatedCurve = 1

**Arg6: iDekCleanselfintersectingloop**

Description: option for dek cleanselfintersectingloop

Data Type: integer

Default Value : 2

Syntax: iDekCleanselfintersectingloop = 1

**Arg7: iDekVolumetopart**

Description: option for dek volumetopart

Data Type: integer

Default Value : 4

Syntax: iDekVolumetopart = 1

**Arg8: iIgesFixedcurevepreference**

Description: option for iges fixedcurevepreference

Data Type: integer

Default Value : 0

Syntax: iIgesFixedcurevepreference = 1

**Arg9: iIgesAutostitch**

Description: option for iges auto stitch

Data Type: integer

Default Value : 1

Syntax: iIgesAutostitch = 1

**Arg10: dIgesStitchtolerance**

Description: double value of iges stitch tolerance

Data Type: double

Default Value : 0.1

Syntax: dIgesStitchtolerance = 1.0

**Arg11: iCatiaConvertnotshowedelement**

Description: option for catia convert not showed element

Data Type: integer

Default Value : 0

Syntax: iCatiaConvertnotshowedelement = 1

**Arg12: iCatiaConvertnotshowedinstance**

Description: option for catia convert not showed instance

Data Type: integer

Default Value : 0

Syntax: iCatiaConvertnotshowedinstance = 1

**Arg13: iCatiaConvertaxis**

Description: option for catia convertaxis

Data Type: integer

Default Value : 1

Syntax: iCatiaConvertaxis = 1

**Arg14: iStepCreateseam**

Description: option for step createseam

Data Type: integer

Default Value : 1

Syntax: iStepCreateseam = 1

**Arg15: dStepPointtolerance**

Description: double value of step pointtolerance

Data Type: double

Default Value : 0.0

Syntax: dStepPointtolerance = 1.0

**Arg16: iAcisHealacisbeforeversion**

Description: option for acis healacisbeforeversion

Data Type: integer

Default Value : 0

Syntax: iAcisHealacisbeforeversion = 1

**Arg17: iJtConvertgeometrytype**

Description: option for jt convertgeometrytype

Data Type: integer

Default Value : 2

Syntax: iJtConvertgeometrytype = 1

**Arg18: bFaceColor**

Description: enable or disable feature face color

Data Type: bool

Default Value : False

Syntax: bFaceColor = True/False

**Arg19: iJtConvertgeneralpart**

Description: option for jt convertgeneralpart

Data Type: integer

Default Value : 1

Syntax: iJtConvertgeneralpart = 1

**Arg20: iJtConvertaxis**

Description: option for jt convertaxis

Data Type: integer

Default Value : 1

Syntax: iJtConvertaxis = 1

**Arg21: iJtConvertcenterline**

Description: option for jt convertcenterline

Data Type: integer

Default Value : 0

Syntax: iJtConvertcenterline = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportCAD.Elysium(strlPath=[], dChordHeightTolerance=1.0, dAngleToleranceDegree=5.0, dPointCoincidentTolerance=0.01, iConvertIsolatedCurve=0, iDekCleanselfintersectingloop=2, iDekVolumetopart=4, iIgesFixedcurevepreference=0, iIgesAutostitch=1, dIgesStitchtolerance=0.1, iCatiaConvertnotshowedelement=0, iCatiaConvertnotshowedinstance=0, iCatiaConvertaxis=1, iStepCreateseam=1, dStepPointtolerance=0.0, iAcisHealacisbeforeversion=0, iJtConvertgeometrytype=2, bFaceColor=False, iJtConvertgeneralpart=1, iJtConvertaxis=1, iJtConvertcenterline=0)

```

==========================================================

# Home.ImportCAD.Spatial

## Wrapper Macro

ImportSpatial(...)

## Ribbon-GUI-Location

Home > ImportCAD > Spatial

## Command Description

import CAD by Spatial

## Argument List

**Arg1: strlPath**

Description: list definition string of path

Data Type: string list

Default Value : []

Syntax: strlPath = ["str1", "str2", "str3"]

**Arg2: dSurfacePlaneTolerance**

Description: double value of surface plane tolerance

Data Type: double

Default Value : 0.0

Syntax: dSurfacePlaneTolerance = 1.0

**Arg3: dSufacePlaneAngle**

Description: double value of suface plane angle

Data Type: double

Default Value : 20.0

Syntax: dSufacePlaneAngle = 1.0

**Arg4: dMaxFacetWidth**

Description: double value of maximize facet width

Data Type: double

Default Value : 1000.0

Syntax: dMaxFacetWidth = 1.0

**Arg5: bNXMultipart**

Description: enable or disable feature n x multipart

Data Type: bool

Default Value : True

Syntax: bNXMultipart = True/False

**Arg6: bHealing**

Description: enable or disable feature healing

Data Type: bool

Default Value : True

Syntax: bHealing = True/False

**Arg7: bIsNXDirect**

Description: enable or disable feature is n x direct

Data Type: bool

Default Value : False

Syntax: bIsNXDirect = True/False

**Arg8: bSetFaceColor**

Description: enable or disable feature set face color

Data Type: bool

Default Value : False

Syntax: bSetFaceColor = True/False

**Arg9: strCsvFilePath**

Description: definition string of input csv file path

Data Type: string

Default Value : ""

Syntax: strCsvFilePath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportCAD.Spatial(strlPath=[], dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=20.0, dMaxFacetWidth=1000.0, bNXMultipart=True, bHealing=True, bIsNXDirect=False, bSetFaceColor=False, strCsvFilePath="")

```

==========================================================

# Home.ImportCAD.Parasolid

## Wrapper Macro

ImportDirect_Parasolid(...)

## Ribbon-GUI-Location

Home > ImportCAD > Parasolid

## Command Description

Import Parasolid

## Argument List

**Arg1: strlFiles**

Description: list definition string of files

Data Type: string list

Default Value : []

Syntax: strlFiles = ["str1", "str2", "str3"]

**Arg2: dChordHeightTolerance**

Description: double value of chord height tolerance

Data Type: double

Default Value : 0.0

Syntax: dChordHeightTolerance = 1.0

**Arg3: dAngleToleranceDegree**

Description: double value of angle tolerance degree

Data Type: double

Default Value : 0.0

Syntax: dAngleToleranceDegree = 1.0

**Arg4: iConvertIsolatedCurve**

Description: option for convert isolated curve

Data Type: integer

Default Value : 0

Syntax: iConvertIsolatedCurve = 1

**Arg5: dSurfacePlaneTolerance**

Description: double value of surface plane tolerance

Data Type: double

Default Value : 0.0

Syntax: dSurfacePlaneTolerance = 1.0

**Arg6: dSufacePlaneAngle**

Description: double value of suface plane angle

Data Type: double

Default Value : 20.0

Syntax: dSufacePlaneAngle = 1.0

**Arg7: dMaxFacetWidth**

Description: double value of maximize facet width

Data Type: double

Default Value : 0.1

Syntax: dMaxFacetWidth = 1.0

**Arg8: dMinFacetWidth**

Description: double value of minimize facet width

Data Type: double

Default Value : 0.0

Syntax: dMinFacetWidth = 1.0

**Arg9: bICAD**

Description: enable or disable feature i c a d

Data Type: bool

Default Value : False

Syntax: bICAD = True/False

**Arg10: iVRMLColorGroups**

Description: option for v r m l color groups

Data Type: integer

Default Value : 0

Syntax: iVRMLColorGroups = 1

**Arg11: dScale**

Description: double value of scale

Data Type: double

Default Value : 1.0

Syntax: dScale = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportCAD.Parasolid(strlFiles=[], dChordHeightTolerance=0.0, dAngleToleranceDegree=0.0, iConvertIsolatedCurve=0, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=20.0, dMaxFacetWidth=0.1, dMinFacetWidth=0.0, bICAD=False, iVRMLColorGroups=0, dScale=1.0)

```

==========================================================

# Home.ImportCAD.STL

## Wrapper Macro

ImportDirect_STL(...)

## Ribbon-GUI-Location

Home > ImportCAD > STL

## Command Description

Import STL

## Argument List

**Arg1: strlFiles**

Description: list definition string of files

Data Type: string list

Default Value : []

Syntax: strlFiles = ["str1", "str2", "str3"]

**Arg2: dChordHeightTolerance**

Description: double value of chord height tolerance

Data Type: double

Default Value : 0.0

Syntax: dChordHeightTolerance = 1.0

**Arg3: dAngleToleranceDegree**

Description: double value of angle tolerance degree

Data Type: double

Default Value : 0.0

Syntax: dAngleToleranceDegree = 1.0

**Arg4: iConvertIsolatedCurve**

Description: option for convert isolated curve

Data Type: integer

Default Value : 0

Syntax: iConvertIsolatedCurve = 1

**Arg5: dSurfacePlaneTolerance**

Description: double value of surface plane tolerance

Data Type: double

Default Value : 0.0

Syntax: dSurfacePlaneTolerance = 1.0

**Arg6: dSufacePlaneAngle**

Description: double value of suface plane angle

Data Type: double

Default Value : 7.0

Syntax: dSufacePlaneAngle = 1.0

**Arg7: dMaxFacetWidth**

Description: double value of maximize facet width

Data Type: double

Default Value : 0.0

Syntax: dMaxFacetWidth = 1.0

**Arg8: dMinFacetWidth**

Description: double value of minimize facet width

Data Type: double

Default Value : 0.0

Syntax: dMinFacetWidth = 1.0

**Arg9: bICAD**

Description: enable or disable feature i c a d

Data Type: bool

Default Value : False

Syntax: bICAD = True/False

**Arg10: iVRMLColorGroups**

Description: option for v r m l color groups

Data Type: integer

Default Value : -227253959

Syntax: iVRMLColorGroups = 1

**Arg11: dScale**

Description: double value of scale

Data Type: double

Default Value : 0.001

Syntax: dScale = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportCAD.STL(strlFiles=[], dChordHeightTolerance=0.0, dAngleToleranceDegree=0.0, iConvertIsolatedCurve=0, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=7.0, dMaxFacetWidth=0.0, dMinFacetWidth=0.0, bICAD=False, iVRMLColorGroups=-227253959, dScale=0.001)

```

==========================================================

# Home.ImportCAD.VRML

## Wrapper Macro

ImportDirect_VRML(...)

## Ribbon-GUI-Location

Home > ImportCAD > VRML

## Command Description

Import VRML

## Argument List

**Arg1: strlFiles**

Description: list definition string of files

Data Type: string list

Default Value : []

Syntax: strlFiles = ["str1", "str2", "str3"]

**Arg2: dChordHeightTolerance**

Description: double value of chord height tolerance

Data Type: double

Default Value : 0.0

Syntax: dChordHeightTolerance = 1.0

**Arg3: dAngleToleranceDegree**

Description: double value of angle tolerance degree

Data Type: double

Default Value : 0.0

Syntax: dAngleToleranceDegree = 1.0

**Arg4: iConvertIsolatedCurve**

Description: option for convert isolated curve

Data Type: integer

Default Value : 0

Syntax: iConvertIsolatedCurve = 1

**Arg5: dSurfacePlaneTolerance**

Description: double value of surface plane tolerance

Data Type: double

Default Value : 0.0

Syntax: dSurfacePlaneTolerance = 1.0

**Arg6: dSufacePlaneAngle**

Description: double value of suface plane angle

Data Type: double

Default Value : 20.0

Syntax: dSufacePlaneAngle = 1.0

**Arg7: dMaxFacetWidth**

Description: double value of maximize facet width

Data Type: double

Default Value : 0.1

Syntax: dMaxFacetWidth = 1.0

**Arg8: dMinFacetWidth**

Description: double value of minimize facet width

Data Type: double

Default Value : 0.0

Syntax: dMinFacetWidth = 1.0

**Arg9: bICAD**

Description: enable or disable feature i c a d

Data Type: bool

Default Value : False

Syntax: bICAD = True/False

**Arg10: iVRMLColorGroups**

Description: option for v r m l color groups

Data Type: integer

Default Value : 0

Syntax: iVRMLColorGroups = 1

**Arg11: dScale**

Description: double value of scale

Data Type: double

Default Value : 1.0

Syntax: dScale = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportCAD.VRML(strlFiles=[], dChordHeightTolerance=0.0, dAngleToleranceDegree=0.0, iConvertIsolatedCurve=0, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=20.0, dMaxFacetWidth=0.1, dMinFacetWidth=0.0, bICAD=False, iVRMLColorGroups=0, dScale=1.0)

```

==========================================================

# Home.ImportCAD.ProECreoDirect

## Wrapper Macro

ImportCreo(...)

## Ribbon-GUI-Location

Home > ImportCAD > ProECreoDirect

## Command Description

import Creo by Direct

## Argument List

**Arg1: strlPath**

Description: list definition string of path

Data Type: string list

Default Value : []

Syntax: strlPath = ["str1", "str2", "str3"]

**Arg2: dChordHeightTolerance**

Description: double value of chord height tolerance

Data Type: double

Default Value : 0.0

Syntax: dChordHeightTolerance = 1.0

**Arg3: dAngleToleranceDegree**

Description: double value of angle tolerance degree

Data Type: double

Default Value : 20.0

Syntax: dAngleToleranceDegree = 1.0

**Arg4: dStepMaxSize**

Description: double value of step maximize size

Data Type: double

Default Value : 0.1

Syntax: dStepMaxSize = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportCAD.ProECreoDirect(strlPath=[], dChordHeightTolerance=0.0, dAngleToleranceDegree=20.0, dStepMaxSize=0.1)

```

==========================================================

# Home.ImportMesh.ADVCADX

## Wrapper Macro

ImportAdx(...)

## Ribbon-GUI-Location

Home > ImportMesh > ADVCADX

## Command Description

import adx files

## Argument List

**Arg1: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

**Arg2: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 60.0

Syntax: dFaceAngle = 1.0

**Arg3: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportMesh.ADVCADX(strPath="", dFaceAngle=60.0, dEdgeAngle=60.0)

```

==========================================================

# Home.ImportMesh.AnsysDat

## Wrapper Macro

ImportAnsys(...)

## Ribbon-GUI-Location

Home > ImportMesh > AnsysDat

## Command Description

Import Ansys file

## Argument List

**Arg1: strlPath**

Description: list definition string of path

Data Type: string list

Default Value : []

Syntax: strlPath = ["str1", "str2", "str3"]

**Arg2: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 60.0

Syntax: dFaceAngle = 1.0

**Arg3: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportMesh.AnsysDat(strlPath=[], dFaceAngle=60.0, dEdgeAngle=60.0)

```

==========================================================

# Home.ImportMesh.NastranBdf

## Wrapper Macro

ImportBdf(...)

## Ribbon-GUI-Location

Home > ImportMesh > NastranBdf

## Command Description

import Nastran bdf file

## Argument List

**Arg1: strlFilePaths**

Description: list definition string of file paths

Data Type: string list

Default Value : []

Syntax: strlFilePaths = ["str1", "str2", "str3"]

**Arg2: iImportType**

Description: option for import type

Data Type: integer

Default Value : 2

Syntax: iImportType = 1

**Arg3: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 60.0

Syntax: dFaceAngle = 1.0

**Arg4: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

**Arg5: bReadNameComment**

Description: enable or disable feature read name comment

Data Type: bool

Default Value : False

Syntax: bReadNameComment = True/False

**Arg6: iCreateDup1DElemAnswer**

Description: option for create dup1 d element answer

Data Type: integer

Default Value : -1

Syntax: iCreateDup1DElemAnswer = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportMesh.NastranBdf(strlFilePaths=[], iImportType=2, dFaceAngle=60.0, dEdgeAngle=60.0, bReadNameComment=False, iCreateDup1DElemAnswer=-1)

```

==========================================================

# Home.ImportMesh.AbaqusINP

## Wrapper Macro

ImportInp(...)

## Ribbon-GUI-Location

Home > ImportMesh > AbaqusINP

## Command Description

import Abaqus INP file

## Argument List

**Arg1: strlFilePaths**

Description: list definition string of file paths

Data Type: string list

Default Value : []

Syntax: strlFilePaths = ["str1", "str2", "str3"]

**Arg2: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 60.0

Syntax: dFaceAngle = 1.0

**Arg3: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

**Arg4: iImportType**

Description: option for import type

Data Type: integer

Default Value : 1

Syntax: iImportType = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportMesh.AbaqusINP(strlFilePaths=[], dFaceAngle=60.0, dEdgeAngle=60.0, iImportType=1)

```

==========================================================

# Home.ImportMesh.LSDYNA

## Wrapper Macro

ImportLsDyna(...)

## Ribbon-GUI-Location

Home > ImportMesh > LSDYNA

## Command Description

Import Ls-Dyna file

## Argument List

**Arg1: strlPath**

Description: list definition string of path

Data Type: string list

Default Value : []

Syntax: strlPath = ["str1", "str2", "str3"]

**Arg2: dFaceAngle**

Description: double value of face angle

Data Type: double

Default Value : 60.0

Syntax: dFaceAngle = 1.0

**Arg3: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 60.0

Syntax: dEdgeAngle = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportMesh.LSDYNA(strlPath=[], dFaceAngle=60.0, dEdgeAngle=60.0)

```

==========================================================

# Home.ImportMesh.Universal

## Wrapper Macro

ImportUnv(...)

## Ribbon-GUI-Location

Home > ImportMesh > Universal

## Command Description

Import Universal

## Argument List

**Arg1: strPath**

Description: definition string of input path

Data Type: string

Default Value : ""

Syntax: strPath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ImportMesh.Universal(strPath="")

```

==========================================================

# Home.Export

## Wrapper Macro

ExportGeomBDF(...)

## Ribbon-GUI-Location

Home > Export

## Command Description

Export Technostar Goemtroy file

## Argument List

**Arg1: strFileName**

Description: definition string of input file name

Data Type: string

Default Value : ""

Syntax: strFileName = "string input"

**Arg2: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg3: bBigID**

Description: enable or disable feature big ID

Data Type: bool

Default Value : False

Syntax: bBigID = True/False

**Arg4: bUseUnit**

Description: enable or disable feature use unit

Data Type: bool

Default Value : True

Syntax: bUseUnit = True/False

**Arg5: bVert**

Description: enable or disable feature vert

Data Type: bool

Default Value : True

Syntax: bVert = True/False

**Arg6: bEdge**

Description: enable or disable feature edge

Data Type: bool

Default Value : True

Syntax: bEdge = True/False

**Arg7: bFace**

Description: enable or disable feature face

Data Type: bool

Default Value : True

Syntax: bFace = True/False

**Arg8: bSolid**

Description: enable or disable feature solid

Data Type: bool

Default Value : True

Syntax: bSolid = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.Export(strFileName="", crlPart=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True)

```

==========================================================

# Home.ToImage

## Wrapper Macro

Capture_ToImageEx(...)

## Ribbon-GUI-Location

Home > ToImage

## Command Description

Command use for Home ToImage

## Argument List

**Arg1: strImgPath**

Description: definition string of input img path

Data Type: string

Default Value : ""

Syntax: strImgPath = "string input"

**Arg2: bWhiteBG**

Description: enable or disable feature white background

Data Type: bool

Default Value : False

Syntax: bWhiteBG = True/False

**Arg3: bTransparentBG**

Description: enable or disable feature transparent background

Data Type: bool

Default Value : False

Syntax: bTransparentBG = True/False

**Arg4: bFixedSize**

Description: enable or disable feature fixed size

Data Type: bool

Default Value : False

Syntax: bFixedSize = True/False

**Arg5: iExportWidth**

Description: option for export width

Data Type: integer

Default Value : 1200

Syntax: iExportWidth = 1

**Arg6: iExportHeight**

Description: option for export height

Data Type: integer

Default Value : 900

Syntax: iExportHeight = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.ToImage(strImgPath="", bWhiteBG=False, bTransparentBG=False, bFixedSize=False, iExportWidth=1200, iExportHeight=900)

```

==========================================================

# Home.Find

## Wrapper Macro

ViewFindEntities(...)

## Ribbon-GUI-Location

Home > Find

## Command Description

Command use for Home Find

## Argument List

**Arg1: strSearch**

Description: definition string of input search

Data Type: string

Default Value : ""

Syntax: strSearch = "string input"

**Arg2: strSeletedType**

Description: definition string of input seleted type

Data Type: string

Default Value : "Part"

Syntax: strSeletedType = "string input"

**Arg3: bFindMatch**

Description: enable or disable feature find match

Data Type: bool

Default Value : False

Syntax: bFindMatch = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.Find(strSearch="", strSeletedType="Part", bFindMatch=False)

```

==========================================================

# Home.RectangularCapture

## Wrapper Macro

Capture_Rectangular(...)

## Ribbon-GUI-Location

Home > RectangularCapture

## Command Description

Command use for Home RectangularCapture

## Argument List

**Arg1: iLeft**

Description: option for left

Data Type: integer

Default Value : 0

Syntax: iLeft = 1

**Arg2: iTop**

Description: option for top

Data Type: integer

Default Value : 0

Syntax: iTop = 1

**Arg3: iRight**

Description: option for right

Data Type: integer

Default Value : 0

Syntax: iRight = 1

**Arg4: iBottom**

Description: option for bottom

Data Type: integer

Default Value : 0

Syntax: iBottom = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.RectangularCapture(iLeft=0, iTop=0, iRight=0, iBottom=0)

```

==========================================================

# Home.CopyToClipboard

## Wrapper Macro

Capture_CopyToClipboardEx(...)

## Ribbon-GUI-Location

Home > CopyToClipboard

## Command Description

Command use for Home CopyToClipboard

## Argument List

**Arg1: bWhiteBG**

Description: enable or disable feature white background

Data Type: bool

Default Value : False

Syntax: bWhiteBG = True/False

**Arg2: bTransparentBG**

Description: enable or disable feature transparent background

Data Type: bool

Default Value : False

Syntax: bTransparentBG = True/False

**Arg3: bFixedSize**

Description: enable or disable feature fixed size

Data Type: bool

Default Value : False

Syntax: bFixedSize = True/False

**Arg4: iWidth**

Description: option for width

Data Type: integer

Default Value : 1200

Syntax: iWidth = 1

**Arg5: iHeight**

Description: option for height

Data Type: integer

Default Value : 900

Syntax: iHeight = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.CopyToClipboard(bWhiteBG=False, bTransparentBG=False, bFixedSize=False, iWidth=1200, iHeight=900)

```

==========================================================

# Home.FullScreen

## Wrapper Macro

ShowFullScreen(...)

## Ribbon-GUI-Location

Home > FullScreen

## Command Description

Command use for Home FullScreen

## Argument List

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.FullScreen()

```

==========================================================

# Home.Synchronize

## Wrapper Macro

SetSynchronize(...)

## Ribbon-GUI-Location

Home > Synchronize

## Command Description

Command use for Home Synchronize

## Argument List

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

Home.Synchronize()

```

==========================================================

# MainWindow.RightClick.MergeFaces

## Wrapper Macro

bMergeFace(...)

## Ribbon-GUI-Location

MainWindow > RightClick > MergeFaces

## Command Description

Merge Faces

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: bIsMergeEdge**

Description: enable or disable feature is merge edge

Data Type: bool

Default Value : False

Syntax: bIsMergeEdge = True/False

**Arg3: bRemoveNonBoundEdge**

Description: enable or disable feature remove non bound edge

Data Type: bool

Default Value : True

Syntax: bRemoveNonBoundEdge = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MainWindow.RightClick.MergeFaces(crlFace=[], bIsMergeEdge=False, bRemoveNonBoundEdge=True)

```

==========================================================

# MainWindow.RightClick.SelectAllParts

## Wrapper Macro

SelectAllParts(...)

## Ribbon-GUI-Location

MainWindow > RightClick > SelectAllParts

## Command Description

Select all of the parts in the model

## Argument List

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MainWindow.RightClick.SelectAllParts()

```

==========================================================

# MainWindow.RightClick.AssociatedPick

## Wrapper Macro

AssociatedPick(...)

## Ribbon-GUI-Location

MainWindow > RightClick > AssociatedPick

## Command Description

pick associated entity

## Argument List

**Arg1: crlInput**

Description: array entities in model with type input

Data Type: cursor list

Default Value : []

Syntax: crlInput = [EntityType(id1, id2, id3)]

**Arg2: strTarget**

Description: definition string of input target

Data Type: string

Default Value : ""

Syntax: strTarget = "string input"

**Arg3: strConnect**

Description: definition string of input connect

Data Type: string

Default Value : "UNKNOWN"

Syntax: strConnect = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MainWindow.RightClick.AssociatedPick(crlInput=[], strTarget="", strConnect="UNKNOWN")

```

==========================================================

# MainWindow.RightClick.FlipElement

## Wrapper Macro

FlipElement(...)

## Ribbon-GUI-Location

MainWindow > RightClick > FlipElement

## Command Description

flip element

## Argument List

**Arg1: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MainWindow.RightClick.FlipElement(crlTarget=[])

```

==========================================================

# MeshCleanup.Element.SolidElement

## Wrapper Macro

ChangeTopoSolidElem(...)

## Ribbon-GUI-Location

MeshCleanup > Element > SolidElement

## Command Description

Change Topology for Solid Element

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: crPart**

Description: entity in database model with type part

Data Type: cursor

Default Value : None

Syntax: crPart = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Element.SolidElement(crlElem=[], crPart=None)

```

==========================================================

# MeshCleanup.Element.SurfaceElement

## Wrapper Macro

ChangeTopologyElement(...)

## Ribbon-GUI-Location

MeshCleanup > Element > SurfaceElement

## Command Description

Change Topology Element

## Argument List

**Arg1: ilElement**

Description: array int values of element

Data Type: int list

Default Value : []

Syntax: ilElement = [1,2,3,4]

**Arg2: ilFace**

Description: array int values of face

Data Type: int list

Default Value : []

Syntax: ilFace = [1,2,3,4]

**Arg3: ilPart**

Description: array int values of part

Data Type: int list

Default Value : []

Syntax: ilPart = [1,2,3,4]

**Arg4: iCreateNewPart**

Description: option for create new part

Data Type: integer

Default Value : 0

Syntax: iCreateNewPart = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)

```

==========================================================

# MeshCleanup.Face

## Wrapper Macro

ChangeTopoFaceCr(...)

## Ribbon-GUI-Location

MeshCleanup > Face

## Command Description

change topology face

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg3: bCreateNewPart**

Description: enable or disable feature create new part

Data Type: bool

Default Value : False

Syntax: bCreateNewPart = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Face(crlFace=[], crlPart=[], bCreateNewPart=False)

```

==========================================================

# MeshCleanup.CorrectModel

## Wrapper Macro

CorrectModel(...)

## Ribbon-GUI-Location

MeshCleanup > CorrectModel

## Command Description

correct model

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: iEnableBreakEdge**

Description: option for enable break edge

Data Type: integer

Default Value : 0

Syntax: iEnableBreakEdge = 1

**Arg3: dEdgeAngle**

Description: double value of edge angle

Data Type: double

Default Value : 0

Syntax: dEdgeAngle = 1.0

**Arg4: iEnableMergeEdge**

Description: option for enable merge edge

Data Type: integer

Default Value : 0

Syntax: iEnableMergeEdge = 1

**Arg5: dMergeEdgeAngle**

Description: double value of merge edge angle

Data Type: double

Default Value : 0

Syntax: dMergeEdgeAngle = 1.0

**Arg6: iEnableMergePlanarFace**

Description: option for enable merge planar face

Data Type: integer

Default Value : 0

Syntax: iEnableMergePlanarFace = 1

**Arg7: iEnableRemoveExtraVertex**

Description: option for enable remove extra vertex

Data Type: integer

Default Value : 0

Syntax: iEnableRemoveExtraVertex = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.CorrectModel(crlPart=[], iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0)

```

==========================================================

# MeshCleanup.CloseHoles

## Wrapper Macro

FindHoles(...)

## Ribbon-GUI-Location

MeshCleanup > CloseHoles

## Command Description

close holes

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg2: dAreaMin**

Description: double value of area minimize

Data Type: double

Default Value : 0.0

Syntax: dAreaMin = 1.0

**Arg3: dAreaMax**

Description: double value of area maximize

Data Type: double

Default Value : 543210.0

Syntax: dAreaMax = 1.0

**Arg4: bMergeFace**

Description: enable or disable feature merge face

Data Type: bool

Default Value : False

Syntax: bMergeFace = True/False

**Arg5: bMergeEdge**

Description: enable or disable feature merge edge

Data Type: bool

Default Value : False

Syntax: bMergeEdge = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.CloseHoles(crlEdge=[], dAreaMin=0.0, dAreaMax=543210.0, bMergeFace=False, bMergeEdge=False)

```

==========================================================

# MeshCleanup.CloseGap

## Wrapper Macro

CloseGaps(...)

## Ribbon-GUI-Location

MeshCleanup > CloseGap

## Command Description

MeshCleanup Cleanup CloseGap

## Argument List

**Arg1: crlPartCur**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPartCur = [EntityType(id1, id2, id3)]

**Arg2: dDistanceTol**

Description: double value of distance tolerance

Data Type: double

Default Value : 0.01

Syntax: dDistanceTol = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.CloseGap(crlPartCur=[], dDistanceTol=0.01)

```

==========================================================

# MeshCleanup.AutoCheck

## Wrapper Macro

CleanupAuto(...)

## Ribbon-GUI-Location

MeshCleanup > AutoCheck

## Command Description

check meshing quality

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: iElemType**

Description: option for element type

Data Type: integer

Default Value : 0

Syntax: iElemType = 1

**Arg3: blCheckCondition**

Description: list of enable/disable options of check condition

Data Type: bool list

Default Value : []

Syntax: blCheckCondition = [True, False]

**Arg4: blElemQuality**

Description: list of enable/disable options of element quality

Data Type: bool list

Default Value : []

Syntax: blElemQuality = [True, False]

**Arg5: dlLimitValue**

Description: array double values of limit value

Data Type: double list

Default Value : []

Syntax: dlLimitValue = [1.0, 2.0]

**Arg6: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.AutoCheck(crlPart=[], iElemType=0, blCheckCondition=[], blElemQuality=[], dlLimitValue=[], crlElem=[])

```

==========================================================

# MeshCleanup.ManualCheck

## Wrapper Macro

CleanupManual(...)

## Ribbon-GUI-Location

MeshCleanup > ManualCheck

## Command Description

MeshCleanup ManualCheck

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: iElemType**

Description: option for element type

Data Type: integer

Default Value : 0

Syntax: iElemType = 1

**Arg3: iVeQuality**

Description: option for ve quality

Data Type: integer

Default Value : 0

Syntax: iVeQuality = 1

**Arg4: iCheckCondition**

Description: option for check condition

Data Type: integer

Default Value : 0

Syntax: iCheckCondition = 1

**Arg5: dLimitValue**

Description: double value of limit value

Data Type: double

Default Value : 0.0

Syntax: dLimitValue = 1.0

**Arg6: dCFLValue**

Description: double value of c l value

Data Type: double

Default Value : 0.0

Syntax: dCFLValue = 1.0

**Arg7: iNonManifold**

Description: option for non manifold

Data Type: integer

Default Value : 0

Syntax: iNonManifold = 1

**Arg8: iCleanupMode**

Description: option for cleanup mode

Data Type: integer

Default Value : 0

Syntax: iCleanupMode = 1

**Arg9: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.ManualCheck(crlPart=[], iElemType=0, iVeQuality=0, iCheckCondition=0, dLimitValue=0.0, dCFLValue=0.0, iNonManifold=0, iCleanupMode=0, crlElem=[])

```

==========================================================

# MeshCleanup.ChangeTopology.Element.SurfaceElement

## Wrapper Macro

ChangeTopologyElement(...)

## Ribbon-GUI-Location

MeshCleanup > ChangeTopology > Element > SurfaceElement

## Command Description

Command use for MeshCleanup ChangeTopology Element SurfaceElement

## Argument List

**Arg1: ilElement**

Description: array int values of element

Data Type: int list

Default Value : []

Syntax: ilElement = [1,2,3,4]

**Arg2: ilFace**

Description: array int values of face

Data Type: int list

Default Value : []

Syntax: ilFace = [1,2,3,4]

**Arg3: ilPart**

Description: array int values of part

Data Type: int list

Default Value : []

Syntax: ilPart = [1,2,3,4]

**Arg4: iCreateNewPart**

Description: option for create new part

Data Type: integer

Default Value : 0

Syntax: iCreateNewPart = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.ChangeTopology.Element.SurfaceElement(ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0)

```

==========================================================

# MeshCleanup.Cleanup.CloseGap

## Wrapper Macro

CloseGaps(...)

## Ribbon-GUI-Location

MeshCleanup > Cleanup > CloseGap

## Command Description

Command use for MeshCleanup Cleanup CloseGap

## Argument List

**Arg1: crlPartCur**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPartCur = [EntityType(id1, id2, id3)]

**Arg2: dDistanceTol**

Description: double value of distance tolerance

Data Type: double

Default Value : 0.0

Syntax: dDistanceTol = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Cleanup.CloseGap(crlPartCur=[], dDistanceTol=0.0)

```

==========================================================

# MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad

## Wrapper Macro

MC_ManualCleanup_2QuadToQuad(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > MergeElement > TwoQuadsToQuad

## Command Description

Merge two Quad elements into one Quad element

## Argument List

**Arg1: crlElements**

Description: array entities in model with type elements

Data Type: cursor list

Default Value : []

Syntax: crlElements = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad(crlElements=[])

```

==========================================================

# MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad

## Wrapper Macro

MC_ManualCleanup_2QuadToQuad(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > MergeElement > TwoQuadsToQuad

## Command Description

Merge two Quad elements into one Quad element

## Argument List

**Arg1: crlElements**

Description: array entities in model with type elements

Data Type: cursor list

Default Value : []

Syntax: crlElements = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad(crlElements=[])

```

==========================================================

# MeshCleanup.Manual2D.MergeElement.TwoTrisToQuad

## Wrapper Macro

MC_ManualCleanup_2TrisToQuad(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > MergeElement > TwoTrisToQuad

## Command Description

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.MergeElement.TwoTrisToQuad(crlElem=[])

```

==========================================================

# MeshCleanup.Manual2D.SplitElement.QuadTo4Quads

## Wrapper Macro

SplitElement(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > SplitElement > QuadTo4Quads

## Command Description

Split element 2D

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: crDatumNode0**

Description: entity in database model with type datum node0

Data Type: cursor

Default Value : None

Syntax: crDatumNode0 = EntityType(id)

**Arg3: crDatumNode1**

Description: entity in database model with type datum node1

Data Type: cursor

Default Value : None

Syntax: crDatumNode1 = EntityType(id)

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg5: iAutoExecute**

Description: option for auto execute

Data Type: integer

Default Value : 0

Syntax: iAutoExecute = 1

**Arg6: iAutoTransition**

Description: option for auto transition

Data Type: integer

Default Value : 0

Syntax: iAutoTransition = 1

**Arg7: iCADProject**

Description: option for c a d project

Data Type: integer

Default Value : 0

Syntax: iCADProject = 1

**Arg8: iMergeNode**

Description: option for merge node

Data Type: integer

Default Value : 0

Syntax: iMergeNode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.SplitElement.QuadTo4Quads(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)

```

==========================================================

# MeshCleanup.Manual2D.SplitElement.QuadToTrans4Quads

## Wrapper Macro

SplitElement(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > SplitElement > QuadToTrans4Quads

## Command Description

Command use for MeshCleanup Manual2D SplitElement QuadToTrans4Quads

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: crDatumNode0**

Description: entity in database model with type datum node0

Data Type: cursor

Default Value : None

Syntax: crDatumNode0 = EntityType(id)

**Arg3: crDatumNode1**

Description: entity in database model with type datum node1

Data Type: cursor

Default Value : None

Syntax: crDatumNode1 = EntityType(id)

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg5: iAutoExecute**

Description: option for auto execute

Data Type: integer

Default Value : 0

Syntax: iAutoExecute = 1

**Arg6: iAutoTransition**

Description: option for auto transition

Data Type: integer

Default Value : 0

Syntax: iAutoTransition = 1

**Arg7: iCADProject**

Description: option for c a d project

Data Type: integer

Default Value : 0

Syntax: iCADProject = 1

**Arg8: iMergeNode**

Description: option for merge node

Data Type: integer

Default Value : 0

Syntax: iMergeNode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.SplitElement.QuadToTrans4Quads(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)

```

==========================================================

# MeshCleanup.Manual2D.SplitElement.QuadToTrans3Quads

## Wrapper Macro

SplitElement(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > SplitElement > QuadToTrans3Quads

## Command Description

Command use for MeshCleanup Manual2D SplitElement QuadToTrans3Quads

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: crDatumNode0**

Description: entity in database model with type datum node0

Data Type: cursor

Default Value : None

Syntax: crDatumNode0 = EntityType(id)

**Arg3: crDatumNode1**

Description: entity in database model with type datum node1

Data Type: cursor

Default Value : None

Syntax: crDatumNode1 = EntityType(id)

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg5: iAutoExecute**

Description: option for auto execute

Data Type: integer

Default Value : 0

Syntax: iAutoExecute = 1

**Arg6: iAutoTransition**

Description: option for auto transition

Data Type: integer

Default Value : 0

Syntax: iAutoTransition = 1

**Arg7: iCADProject**

Description: option for c a d project

Data Type: integer

Default Value : 0

Syntax: iCADProject = 1

**Arg8: iMergeNode**

Description: option for merge node

Data Type: integer

Default Value : 0

Syntax: iMergeNode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.SplitElement.QuadToTrans3Quads(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)

```

==========================================================

# MeshCleanup.Manual2D.SplitElement.QuadTo2Quads1Tri

## Wrapper Macro

SplitElement(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > SplitElement > QuadTo2Quads1Tri

## Command Description

Command use for MeshCleanup Manual2D SplitElement QuadTo2Quads1Tri

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: crDatumNode0**

Description: entity in database model with type datum node0

Data Type: cursor

Default Value : None

Syntax: crDatumNode0 = EntityType(id)

**Arg3: crDatumNode1**

Description: entity in database model with type datum node1

Data Type: cursor

Default Value : None

Syntax: crDatumNode1 = EntityType(id)

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg5: iAutoExecute**

Description: option for auto execute

Data Type: integer

Default Value : 0

Syntax: iAutoExecute = 1

**Arg6: iAutoTransition**

Description: option for auto transition

Data Type: integer

Default Value : 0

Syntax: iAutoTransition = 1

**Arg7: iCADProject**

Description: option for c a d project

Data Type: integer

Default Value : 0

Syntax: iCADProject = 1

**Arg8: iMergeNode**

Description: option for merge node

Data Type: integer

Default Value : 0

Syntax: iMergeNode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.SplitElement.QuadTo2Quads1Tri(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)

```

==========================================================

# MeshCleanup.Manual2D.SplitElement.QuadTo3Tris

## Wrapper Macro

SplitElement(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > SplitElement > QuadTo3Tris

## Command Description

Command use for MeshCleanup Manual2D SplitElement QuadTo3Tris

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: crDatumNode0**

Description: entity in database model with type datum node0

Data Type: cursor

Default Value : None

Syntax: crDatumNode0 = EntityType(id)

**Arg3: crDatumNode1**

Description: entity in database model with type datum node1

Data Type: cursor

Default Value : None

Syntax: crDatumNode1 = EntityType(id)

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg5: iAutoExecute**

Description: option for auto execute

Data Type: integer

Default Value : 0

Syntax: iAutoExecute = 1

**Arg6: iAutoTransition**

Description: option for auto transition

Data Type: integer

Default Value : 0

Syntax: iAutoTransition = 1

**Arg7: iCADProject**

Description: option for c a d project

Data Type: integer

Default Value : 0

Syntax: iCADProject = 1

**Arg8: iMergeNode**

Description: option for merge node

Data Type: integer

Default Value : 0

Syntax: iMergeNode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.SplitElement.QuadTo3Tris(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)

```

==========================================================

# MeshCleanup.Manual2D.SplitElement.QuadTo2Quads

## Wrapper Macro

SplitElement(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > SplitElement > QuadTo2Quads

## Command Description

Command use for MeshCleanup Manual2D SplitElement QuadTo2Quads

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: crDatumNode0**

Description: entity in database model with type datum node0

Data Type: cursor

Default Value : None

Syntax: crDatumNode0 = EntityType(id)

**Arg3: crDatumNode1**

Description: entity in database model with type datum node1

Data Type: cursor

Default Value : None

Syntax: crDatumNode1 = EntityType(id)

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg5: iAutoExecute**

Description: option for auto execute

Data Type: integer

Default Value : 0

Syntax: iAutoExecute = 1

**Arg6: iAutoTransition**

Description: option for auto transition

Data Type: integer

Default Value : 0

Syntax: iAutoTransition = 1

**Arg7: iCADProject**

Description: option for c a d project

Data Type: integer

Default Value : 0

Syntax: iCADProject = 1

**Arg8: iMergeNode**

Description: option for merge node

Data Type: integer

Default Value : 0

Syntax: iMergeNode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.SplitElement.QuadTo2Quads(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)

```

==========================================================

# MeshCleanup.Manual2D.SplitElement.QuadTo2Tris

## Wrapper Macro

SplitElement(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > SplitElement > QuadTo2Tris

## Command Description

Command use for MeshCleanup Manual2D SplitElement QuadTo2Tris

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: crDatumNode0**

Description: entity in database model with type datum node0

Data Type: cursor

Default Value : None

Syntax: crDatumNode0 = EntityType(id)

**Arg3: crDatumNode1**

Description: entity in database model with type datum node1

Data Type: cursor

Default Value : None

Syntax: crDatumNode1 = EntityType(id)

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg5: iAutoExecute**

Description: option for auto execute

Data Type: integer

Default Value : 0

Syntax: iAutoExecute = 1

**Arg6: iAutoTransition**

Description: option for auto transition

Data Type: integer

Default Value : 0

Syntax: iAutoTransition = 1

**Arg7: iCADProject**

Description: option for c a d project

Data Type: integer

Default Value : 0

Syntax: iCADProject = 1

**Arg8: iMergeNode**

Description: option for merge node

Data Type: integer

Default Value : 0

Syntax: iMergeNode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.SplitElement.QuadTo2Tris(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)

```

==========================================================

# MeshCleanup.Manual2D.SplitElement.QuadToQuadTri

## Wrapper Macro

SplitElement(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > SplitElement > QuadToQuadTri

## Command Description

Command use for MeshCleanup Manual2D SplitElement QuadToQuadTri

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: crDatumNode0**

Description: entity in database model with type datum node0

Data Type: cursor

Default Value : None

Syntax: crDatumNode0 = EntityType(id)

**Arg3: crDatumNode1**

Description: entity in database model with type datum node1

Data Type: cursor

Default Value : None

Syntax: crDatumNode1 = EntityType(id)

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg5: iAutoExecute**

Description: option for auto execute

Data Type: integer

Default Value : 0

Syntax: iAutoExecute = 1

**Arg6: iAutoTransition**

Description: option for auto transition

Data Type: integer

Default Value : 0

Syntax: iAutoTransition = 1

**Arg7: iCADProject**

Description: option for c a d project

Data Type: integer

Default Value : 0

Syntax: iCADProject = 1

**Arg8: iMergeNode**

Description: option for merge node

Data Type: integer

Default Value : 0

Syntax: iMergeNode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.SplitElement.QuadToQuadTri(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)

```

==========================================================

# MeshCleanup.Manual2D.SplitElement.QuadTo4Tris

## Wrapper Macro

SplitElement(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > SplitElement > QuadTo4Tris

## Command Description

Command use for MeshCleanup Manual2D SplitElement QuadTo4Tris

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: crDatumNode0**

Description: entity in database model with type datum node0

Data Type: cursor

Default Value : None

Syntax: crDatumNode0 = EntityType(id)

**Arg3: crDatumNode1**

Description: entity in database model with type datum node1

Data Type: cursor

Default Value : None

Syntax: crDatumNode1 = EntityType(id)

**Arg4: iMethod**

Description: option for method

Data Type: integer

Default Value : 0

Syntax: iMethod = 1

**Arg5: iAutoExecute**

Description: option for auto execute

Data Type: integer

Default Value : 0

Syntax: iAutoExecute = 1

**Arg6: iAutoTransition**

Description: option for auto transition

Data Type: integer

Default Value : 0

Syntax: iAutoTransition = 1

**Arg7: iCADProject**

Description: option for c a d project

Data Type: integer

Default Value : 0

Syntax: iCADProject = 1

**Arg8: iMergeNode**

Description: option for merge node

Data Type: integer

Default Value : 0

Syntax: iMergeNode = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.SplitElement.QuadTo4Tris(crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0)

```

==========================================================

# MeshCleanup.Manual2D.Equivalence

## Wrapper Macro

Equivalence(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > Equivalence

## Command Description

Equivalence Nodes

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: iTypeEquiva**

Description: option for type equiva

Data Type: integer

Default Value : 0

Syntax: iTypeEquiva = 1

**Arg3: dTolerance**

Description: double value of tolerance

Data Type: double

Default Value : 1.0

Syntax: dTolerance = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.Equivalence(crlNode=[], iTypeEquiva=0, dTolerance=1.0)

```

==========================================================

# MeshCleanup.Manual2D.DeleteElement

## Wrapper Macro

DeleteElement(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > DeleteElement

## Command Description

Delete Element

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg2: bKeepShareElem**

Description: enable or disable feature keep share element

Data Type: bool

Default Value : False

Syntax: bKeepShareElem = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.DeleteElement(crlElem=[], bKeepShareElem=False)

```

==========================================================

# MeshCleanup.Manual2D.Split

## Wrapper Macro

SplitElemEdge(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > Split

## Command Description

manual cleanup by split

## Argument List

**Arg1: crplElemEdge**

Description: list pair of entities in model with type element edge

Data Type: cursor pair list

Default Value : [[]]

Syntax: crplElemEdge = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg2: dRatio**

Description: double value of ratio

Data Type: double

Default Value : 0.0

Syntax: dRatio = 1.0

**Arg3: crNodeRef**

Description: entity in database model with type node ref

Data Type: cursor

Default Value : None

Syntax: crNodeRef = EntityType(id)

**Arg4: crProjPart**

Description: entity in database model with type proj part

Data Type: cursor

Default Value : None

Syntax: crProjPart = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.Split(crplElemEdge=[[]], dRatio=0.0, crNodeRef=None, crProjPart=None)

```

==========================================================

# MeshCleanup.Manual2D.Swap

## Wrapper Macro

SwapElemEdge(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > Swap

## Command Description

Swap Element Edge

## Argument List

**Arg1: crplElemEdge**

Description: list pair of entities in model with type element edge

Data Type: cursor pair list

Default Value : []

Syntax: crplElemEdge = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.Swap(crplElemEdge=[])

```

==========================================================

# MeshCleanup.Manual2D.Collapse

## Wrapper Macro

Collapse(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > Collapse

## Command Description

Collapse for Mesh Cleanup

## Argument List

**Arg1: crNodeRef**

Description: entity in database model with type node ref

Data Type: cursor

Default Value : None

Syntax: crNodeRef = EntityType(id)

**Arg2: crNodeEq**

Description: entity in database model with type node eq

Data Type: cursor

Default Value : None

Syntax: crNodeEq = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.Collapse(crNodeRef=None, crNodeEq=None)

```

==========================================================

# MeshCleanup.Manual2D.CreateElement

## Wrapper Macro

CreateElementCr(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > CreateElement

## Command Description

Create element

## Argument List

**Arg1: iElemType**

Description: option for element type

Data Type: integer

Default Value : 0

Syntax: iElemType = 1

**Arg2: crParentEntity**

Description: entity in database model with type parent entity

Data Type: cursor

Default Value : None

Syntax: crParentEntity = EntityType(id)

**Arg3: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.CreateElement(iElemType=0, crParentEntity=None, crlNode=[])

```

==========================================================

# MeshCleanup.Manual2D.RemeshElement

## Wrapper Macro

LocalRemeshTriQuad_MC2D(...)

## Ribbon-GUI-Location

MeshCleanup > Manual2D > RemeshElement

## Command Description

local surface remesh

## Argument List

**Arg1: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg2: surfaceMesh**

Description: data structure of SURFACE_MESH (refer PSJ Command Data Structure Document)

Data Type: SURFACE_MESH

Default Value : SURFACE_MESH()

Syntax: surfaceMesh = SURFACE_MESH(,,,)

**Arg3: bUseSetting**

Description: enable or disable feature use setting

Data Type: bool

Default Value : False

Syntax: bUseSetting = True/False

**Arg4: bGrading**

Description: enable or disable feature grading

Data Type: bool

Default Value : False

Syntax: bGrading = True/False

**Arg5: bFMesher**

Description: enable or disable feature mesher

Data Type: bool

Default Value : False

Syntax: bFMesher = True/False

**Arg6: iOverrideType**

Description: option for override type

Data Type: integer

Default Value : 0

Syntax: iOverrideType = 1

**Arg7: bKeepConnection**

Description: enable or disable feature keep connection

Data Type: bool

Default Value : False

Syntax: bKeepConnection = True/False

**Arg8: bProjCAD**

Description: enable or disable feature proj c a d

Data Type: bool

Default Value : False

Syntax: bProjCAD = True/False

**Arg9: bTinyFaceMerge**

Description: enable or disable feature tiny face merge

Data Type: bool

Default Value : False

Syntax: bTinyFaceMerge = True/False

**Arg10: dMinFaceWidth**

Description: double value of minimize face width

Data Type: double

Default Value : 0

Syntax: dMinFaceWidth = 1.0

**Arg11: dMaxFaceWidth**

Description: double value of maximize face width

Data Type: double

Default Value : 0.001

Syntax: dMaxFaceWidth = 1.0

**Arg12: bIDchcek**

Description: enable or disable feature i dchcek

Data Type: bool

Default Value : False

Syntax: bIDchcek = True/False

**Arg13: bKeepRemeshEdge**

Description: enable or disable feature keep remesh edge

Data Type: bool

Default Value : False

Syntax: bKeepRemeshEdge = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual2D.RemeshElement(crlTarget=[], surfaceMesh=SURFACE_MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False)

```

==========================================================

# MeshCleanup.Manual3D.Collapse.CenterFaceCollapse

## Wrapper Macro

CleanupCenterFaceCollapse(...)

## Ribbon-GUI-Location

MeshCleanup > Manual3D > Collapse > CenterFaceCollapse

## Command Description

## Argument List

**Arg1: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual3D.Collapse.CenterFaceCollapse(crlElem=[])

```

==========================================================

# MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse

## Wrapper Macro

CleanupHalfEdgeCollapse(...)

## Ribbon-GUI-Location

MeshCleanup > Manual3D > Collapse > HalfEdgeCollapse

## Command Description

mash cleanup by manual for half edge collapse

## Argument List

**Arg1: crplElemEdge**

Description: list pair of entities in model with type element edge

Data Type: cursor pair list

Default Value : [[]]

Syntax: crplElemEdge = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse(crplElemEdge=[[]])

```

==========================================================

# MeshCleanup.Manual3D.Collapse.EdgeCollapse

## Wrapper Macro

CleaunpEdgeCollapse(...)

## Ribbon-GUI-Location

MeshCleanup > Manual3D > Collapse > EdgeCollapse

## Command Description

collapse

## Argument List

**Arg1: crplElemEdge**

Description: list pair of entities in model with type element edge

Data Type: cursor pair list

Default Value : []

Syntax: crplElemEdge = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg2: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual3D.Collapse.EdgeCollapse(crplElemEdge=[], crlNode=[])

```

==========================================================

# MeshCleanup.Manual3D.DeleteNode

## Wrapper Macro

CleanupRemoveNode(...)

## Ribbon-GUI-Location

MeshCleanup > Manual3D > DeleteNode

## Command Description

remove node for solid element.

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual3D.DeleteNode(crlNode=[])

```

==========================================================

# MeshCleanup.Manual3D.Swap

## Wrapper Macro

CleanupSwap(...)

## Ribbon-GUI-Location

MeshCleanup > Manual3D > Swap

## Command Description

cleanup element edge by swap

## Argument List

**Arg1: crplElemEdge**

Description: list pair of entities in model with type element edge

Data Type: cursor pair list

Default Value : [[]]

Syntax: crplElemEdge = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual3D.Swap(crplElemEdge=[[]])

```

==========================================================

# MeshCleanup.Manual3D.Equivalence

## Wrapper Macro

CleanupEquivalence(...)

## Ribbon-GUI-Location

MeshCleanup > Manual3D > Equivalence

## Command Description

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: iMergeTowards**

Description: option for merge towards

Data Type: integer

Default Value : 0

Syntax: iMergeTowards = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual3D.Equivalence(crlNode=[], iMergeTowards=0)

```

==========================================================

# MeshCleanup.Manual3D.Split

## Wrapper Macro

CleanupSplit(...)

## Ribbon-GUI-Location

MeshCleanup > Manual3D > Split

## Command Description

Merge two Quad elements into one Quad element

## Argument List

**Arg1: crplElemEdge**

Description: list pair of entities in model with type element edge

Data Type: cursor pair list

Default Value : [[]]

Syntax: crplElemEdge = [CursorPair(EntityType(id), EntityType(id)), CursorPair(EntityType(id), EntityType(id))]

**Arg2: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg3: dRatioDistance**

Description: double value of ratio distance

Data Type: double

Default Value : 0.5

Syntax: dRatioDistance = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual3D.Split(crplElemEdge=[[]], crlNode=[], dRatioDistance=0.5)

```

==========================================================

# MeshCleanup.Manual3D.CreateHex

## Wrapper Macro

CreateElementHEX8(...)

## Ribbon-GUI-Location

MeshCleanup > Manual3D > CreateHex

## Command Description

create hex8 elements

## Argument List

**Arg1: iParentEntityId**

Description: option for parent entity id

Data Type: integer

Default Value : 0

Syntax: iParentEntityId = 1

**Arg2: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg3: iSeprateN**

Description: option for seprate n

Data Type: integer

Default Value : 1

Syntax: iSeprateN = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual3D.CreateHex(iParentEntityId=0, crlElem=[], iSeprateN=1)

```

==========================================================

# MeshCleanup.Manual3D.CreatePenta

## Wrapper Macro

CreateElementPENTA5(...)

## Ribbon-GUI-Location

MeshCleanup > Manual3D > CreatePenta

## Command Description

Create penta5 element

## Argument List

**Arg1: iParentEntityId**

Description: option for parent entity id

Data Type: integer

Default Value : 0

Syntax: iParentEntityId = 1

**Arg2: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual3D.CreatePenta(iParentEntityId=0, crlElem=[])

```

==========================================================

# MeshCleanup.Manual3D.CreateTetra

## Wrapper Macro

CreateElementTET4(...)

## Ribbon-GUI-Location

MeshCleanup > Manual3D > CreateTetra

## Command Description

create element Tet

## Argument List

**Arg1: iParentEntityId**

Description: option for parent entity id

Data Type: integer

Default Value : 0

Syntax: iParentEntityId = 1

**Arg2: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg3: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.Manual3D.CreateTetra(iParentEntityId=0, crlNode=[], crlElem=[])

```

==========================================================

# MeshCleanup.ManualCheck.Tri

## Wrapper Macro

CleanupManual(...)

## Ribbon-GUI-Location

MeshCleanup > ManualCheck > Tri

## Command Description

Command use for MeshCleanup ManualCheck Tri

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: nElemType**

Description: data structure of 0 (refer PSJ Command Data Structure Document)

Data Type: 0

Default Value : 0

Syntax: nElemType = 0(,,,)

**Arg3: veQuality**

Description: data structure of 0 (refer PSJ Command Data Structure Document)

Data Type: 0

Default Value : 0

Syntax: veQuality = 0(,,,)

**Arg4: nCheckCondition**

Description: data structure of 0 (refer PSJ Command Data Structure Document)

Data Type: 0

Default Value : 0

Syntax: nCheckCondition = 0(,,,)

**Arg5: dLimitValue**

Description: double value of limit value

Data Type: double

Default Value : 0.0

Syntax: dLimitValue = 1.0

**Arg6: CFLValue**

Description: data structure of 0.0 (refer PSJ Command Data Structure Document)

Data Type: 0.0

Default Value : 0.0

Syntax: CFLValue = 0.0(,,,)

**Arg7: nNonManifold**

Description: data structure of 0 (refer PSJ Command Data Structure Document)

Data Type: 0

Default Value : 0

Syntax: nNonManifold = 0(,,,)

**Arg8: nCleanupMode**

Description: data structure of 0 (refer PSJ Command Data Structure Document)

Data Type: 0

Default Value : 0

Syntax: nCleanupMode = 0(,,,)

**Arg9: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshCleanup.ManualCheck.Tri(crlPart=[], nElemType=0, veQuality=0, nCheckCondition=0, dLimitValue=0.0, CFLValue=0.0, nNonManifold=0, nCleanupMode=0, crlElem=[])

```

==========================================================

# MeshEdit.CreateElement.Hex

## Wrapper Macro

CreateElementHEX8_ME(...)

## Ribbon-GUI-Location

MeshEdit > CreateElement > Hex

## Command Description

create hex8 elements

## Argument List

**Arg1: iParentEntityId**

Description: option for parent entity id

Data Type: integer

Default Value : 0

Syntax: iParentEntityId = 1

**Arg2: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg3: iSeprateN**

Description: option for seprate n

Data Type: integer

Default Value : 1

Syntax: iSeprateN = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateElement.Hex(iParentEntityId=0, crlElem=[], iSeprateN=1)

```

==========================================================

# MeshEdit.CreateElement.Penta

## Wrapper Macro

MeshEditCreatePenta(...)

## Ribbon-GUI-Location

MeshEdit > CreateElement > Penta

## Command Description

Create penta element

## Argument List

**Arg1: iParentEntityId**

Description: option for parent entity id

Data Type: integer

Default Value : 0

Syntax: iParentEntityId = 1

**Arg2: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateElement.Penta(iParentEntityId=0, crlElem=[])

```

==========================================================

# MeshEdit.CreateElement.Tet

## Wrapper Macro

CreateElementTET4_ME(...)

## Ribbon-GUI-Location

MeshEdit > CreateElement > Tet

## Command Description

create element Tet

## Argument List

**Arg1: iParentEntityId**

Description: option for parent entity id

Data Type: integer

Default Value : 0

Syntax: iParentEntityId = 1

**Arg2: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg3: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateElement.Tet(iParentEntityId=0, crlNode=[], crlElem=[])

```

==========================================================

# MeshEdit.CreateElement.Tri3

## Wrapper Macro

CreateElementTRI3Cr(...)

## Ribbon-GUI-Location

MeshEdit > CreateElement > Tri3

## Command Description

Create element

## Argument List

**Arg1: iElemType**

Description: option for element type

Data Type: integer

Default Value : 0

Syntax: iElemType = 1

**Arg2: crParentEntity**

Description: entity in database model with type parent entity

Data Type: cursor

Default Value : None

Syntax: crParentEntity = EntityType(id)

**Arg3: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateElement.Tri3(iElemType=0, crParentEntity=None, crlNode=[])

```

==========================================================

# MeshEdit.CreateElement.Quad4

## Wrapper Macro

CreateElementQUAD4Cr(...)

## Ribbon-GUI-Location

MeshEdit > CreateElement > Quad4

## Command Description

Create element

## Argument List

**Arg1: iElemType**

Description: option for element type

Data Type: integer

Default Value : 0

Syntax: iElemType = 1

**Arg2: crParentEntity**

Description: entity in database model with type parent entity

Data Type: cursor

Default Value : None

Syntax: crParentEntity = EntityType(id)

**Arg3: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateElement.Quad4(iElemType=0, crParentEntity=None, crlNode=[])

```

==========================================================

# MeshEdit.CreateNode.CircleCenter

## Wrapper Macro

CreateNodeEdgeCenter(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > CircleCenter

## Command Description

create node at center of circle

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg2: iNodeID**

Description: option for node ID

Data Type: integer

Default Value : 0

Syntax: iNodeID = 1

**Arg3: bImprint**

Description: enable or disable feature imprint

Data Type: bool

Default Value : False

Syntax: bImprint = True/False

**Arg4: crFace**

Description: entity in database model with type face

Data Type: cursor

Default Value : None

Syntax: crFace = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.CircleCenter(crlEdge=[], iNodeID=0, bImprint=False, crFace=None)

```

==========================================================

# MeshEdit.CreateNode.Absolute

## Wrapper Macro

CreateNode(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > Absolute

## Command Description

create node by input direct value

## Argument List

**Arg1: veclNodeCoord**

Description: two dimensional array of node coordinate

Data Type: vector list

Default Value : []

Syntax: veclNodeCoord = [[value1, value2, value3], [value1, value2, value3]]

**Arg2: ilNewNodeID**

Description: array int values of new node ID

Data Type: int list

Default Value : []

Syntax: ilNewNodeID = [1,2,3,4]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.Absolute(veclNodeCoord=[], ilNewNodeID=[])

```

==========================================================

# MeshEdit.CreateNode.Import

## Wrapper Macro

CreateNodeImport(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > Import

## Command Description

create node by importing CSV file

## Argument List

**Arg1: strCsvFilePath**

Description: definition string of input csv file path

Data Type: string

Default Value : ""

Syntax: strCsvFilePath = "string input"

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.Import(strCsvFilePath="")

```

==========================================================

# MeshEdit.CreateNode.Point

## Wrapper Macro

MeshEditCreateNodePoint(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > Point

## Command Description

create node point

## Argument List

**Arg1: iNodeID**

Description: option for node ID

Data Type: integer

Default Value : 1

Syntax: iNodeID = 1

**Arg2: posPoint**

Description: array double value [x, y, z] in coordinate system of point

Data Type: position

Default Value : [0,0,0]

Syntax: posPoint = [x, y, z]

**Arg3: bImprint**

Description: enable or disable feature imprint

Data Type: bool

Default Value : True

Syntax: bImprint = True/False

**Arg4: crShape**

Description: entity in database model with type shape

Data Type: cursor

Default Value : None

Syntax: crShape = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.Point(iNodeID=1, posPoint=[0,0,0], bImprint=True, crShape=None)

```

==========================================================

# MeshEdit.CreateNode.Between2Nodes

## Wrapper Macro

MeshEditCreateNodeBetween2Nodes(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > Between2Nodes

## Command Description

create node point

## Argument List

**Arg1: iNodeID**

Description: option for node ID

Data Type: integer

Default Value : 0

Syntax: iNodeID = 1

**Arg2: dX**

Description: double value of x

Data Type: double

Default Value : 0.0

Syntax: dX = 1.0

**Arg3: dY**

Description: double value of y

Data Type: double

Default Value : 0.0

Syntax: dY = 1.0

**Arg4: dZ**

Description: double value of z

Data Type: double

Default Value : 0.0

Syntax: dZ = 1.0

**Arg5: iNumberofNodes**

Description: option for numberof nodes

Data Type: integer

Default Value : 0

Syntax: iNumberofNodes = 1

**Arg6: bImprint**

Description: enable or disable feature imprint

Data Type: bool

Default Value : False

Syntax: bImprint = True/False

**Arg7: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg8: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.Between2Nodes(iNodeID=0, dX=0.0, dY=0.0, dZ=0.0, iNumberofNodes=0, bImprint=False, crlNode=[], crlFace=[])

```

==========================================================

# MeshEdit.CreateNode.Between3Nodes

## Wrapper Macro

MeshEditCreateNodeBetween3Nodes(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > Between3Nodes

## Command Description

create node point

## Argument List

**Arg1: iNodeID**

Description: option for node ID

Data Type: integer

Default Value : 0

Syntax: iNodeID = 1

**Arg2: dX**

Description: double value of x

Data Type: double

Default Value : 0.0

Syntax: dX = 1.0

**Arg3: dY**

Description: double value of y

Data Type: double

Default Value : 0.0

Syntax: dY = 1.0

**Arg4: dZ**

Description: double value of z

Data Type: double

Default Value : 0.0

Syntax: dZ = 1.0

**Arg5: bImprint**

Description: enable or disable feature imprint

Data Type: bool

Default Value : False

Syntax: bImprint = True/False

**Arg6: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg7: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.Between3Nodes(iNodeID=0, dX=0.0, dY=0.0, dZ=0.0, bImprint=False, crlNode=[], crlFace=[])

```

==========================================================

# MeshEdit.CreateNode.ProjectToPlane

## Wrapper Macro

MeshEditCreateNodeProjectNode(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > ProjectToPlane

## Command Description

create node point

## Argument List

**Arg1: dX**

Description: double value of x

Data Type: double

Default Value : 0.0

Syntax: dX = 1.0

**Arg2: dY**

Description: double value of y

Data Type: double

Default Value : 0.0

Syntax: dY = 1.0

**Arg3: dZ**

Description: double value of z

Data Type: double

Default Value : 0.0

Syntax: dZ = 1.0

**Arg4: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg5: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.ProjectToPlane(dX=0.0, dY=0.0, dZ=0.0, crlNode=[], crlFace=[])

```

==========================================================

# MeshEdit.CreateNode.CenterOfCylinder

## Wrapper Macro

MeshEditCreateNodeCylindCenter(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > CenterOfCylinder

## Command Description

Create node of center cylinder

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: iNodeID**

Description: option for node ID

Data Type: integer

Default Value : 1

Syntax: iNodeID = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.CenterOfCylinder(crlFace=[], iNodeID=1)

```

==========================================================

# MeshEdit.CreateNode.CenterOfSphere

## Wrapper Macro

MeshEditCreateNodeSphereCenter(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > CenterOfSphere

## Command Description

Create node of center sphere

## Argument List

**Arg1: crlNodeOrFace**

Description: array entities in model with type node or face

Data Type: cursor list

Default Value : []

Syntax: crlNodeOrFace = [EntityType(id1, id2, id3)]

**Arg2: iNodeID**

Description: option for node ID

Data Type: integer

Default Value : 1

Syntax: iNodeID = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.CenterOfSphere(crlNodeOrFace=[], iNodeID=1)

```

==========================================================

# MeshEdit.CreateNode.Offset

## Wrapper Macro

CreateNodeOffset(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > Offset

## Command Description

MeshEdit CreateNode CreateNodeNodeOffset

## Argument List

**Arg1: vecOffset**

Description: array values of offset

Data Type: vector

Default Value : []

Syntax: vecOffset = [value1, value2, value3]

**Arg2: iRep**

Description: option for rep

Data Type: integer

Default Value : 1

Syntax: iRep = 1

**Arg3: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg4: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.Offset(vecOffset=[], iRep=1, crlNode=[], crCoord=None)

```

==========================================================

# MeshEdit.CreateNode.CenterOfGravity

## Wrapper Macro

MeshEditCreateNodeCenterofGravity(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > CenterOfGravity

## Command Description

create node Center Of Gravity

## Argument List

**Arg1: iCreationType**

Description: option for creation type

Data Type: integer

Default Value : 1

Syntax: iCreationType = 1

**Arg2: iNodeID**

Description: option for node ID

Data Type: integer

Default Value : 0

Syntax: iNodeID = 1

**Arg3: dX**

Description: double value of x

Data Type: double

Default Value : 0.0

Syntax: dX = 1.0

**Arg4: dY**

Description: double value of y

Data Type: double

Default Value : 0.0

Syntax: dY = 1.0

**Arg5: dZ**

Description: double value of z

Data Type: double

Default Value : 0.0

Syntax: dZ = 1.0

**Arg6: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg7: crlBarPart**

Description: array entities in model with type bar part

Data Type: cursor list

Default Value : []

Syntax: crlBarPart = [EntityType(id1, id2, id3)]

**Arg8: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.CenterOfGravity(iCreationType=1, iNodeID=0, dX=0.0, dY=0.0, dZ=0.0, crlPart=[], crlBarPart=[], crlFace=[])

```

==========================================================

# MeshEdit.CreateNode.ProjectToLine

## Wrapper Macro

CreateNodeProjectToLine(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > ProjectToLine

## Command Description

create node by projection to line

## Argument List

**Arg1: crlTa**

Description: array entities in model with type ta

Data Type: cursor list

Default Value : []

Syntax: crlTa = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.ProjectToLine(crlTa=[])

```

==========================================================

# MeshEdit.CreateNode.IntersectionNode

## Wrapper Macro

CreateNodeIntersectionNode(...)

## Ribbon-GUI-Location

MeshEdit > CreateNode > IntersectionNode

## Command Description

create node by intersection node

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg3: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg4: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.CreateNode.IntersectionNode(crlFace=[], crlPart=[], crlEdge=[], crlNode=[])

```

==========================================================

# MeshEdit.MoveNode.Point

## Wrapper Macro

MoveNodePoint(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > Point

## Command Description

Move node(s) to an Face(Edge) Point position

## Argument List

**Arg1: dX**

Description: double value of x

Data Type: double

Default Value : 0.0

Syntax: dX = 1.0

**Arg2: dY**

Description: double value of y

Data Type: double

Default Value : 0.0

Syntax: dY = 1.0

**Arg3: dZ**

Description: double value of z

Data Type: double

Default Value : 0.0

Syntax: dZ = 1.0

**Arg4: ilNodeList**

Description: array int values of node list

Data Type: int list

Default Value : []

Syntax: ilNodeList = [1,2,3,4]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.Point(dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[])

```

==========================================================

# MeshEdit.MoveNode.ProjectToLine

## Wrapper Macro

MoveNodeAlignNodeCr(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > ProjectToLine

## Command Description

move node by project to line

## Argument List

**Arg1: crlRefNodes**

Description: array entities in model with type ref nodes

Data Type: cursor list

Default Value : []

Syntax: crlRefNodes = [EntityType(id1, id2, id3)]

**Arg2: crlObjNodes**

Description: array entities in model with type obj nodes

Data Type: cursor list

Default Value : []

Syntax: crlObjNodes = [EntityType(id1, id2, id3)]

**Arg3: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.ProjectToLine(crlRefNodes=[], crlObjNodes=[], iType=0)

```

==========================================================

# MeshEdit.MoveNode.ProjectToPlaneElem

## Wrapper Macro

MoveNodeNode2PlanElem(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > ProjectToPlaneElem

## Command Description

Move Node by Project to Plane(element)

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.ProjectToPlaneElem(crlNode=[], crlElem=[])

```

==========================================================

# MeshEdit.MoveNode.Equalize

## Wrapper Macro

MeshEditMoveNodeEqualize(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > Equalize

## Command Description

Move node by equalize

## Argument List

**Arg1: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.Equalize(crlEdge=[])

```

==========================================================

# MeshEdit.MoveNode.NormalOffset

## Wrapper Macro

MoveNodeNormalOffset(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > NormalOffset

## Command Description

Move node(s) in Normal Direction of plane

## Argument List

**Arg1: dMagnitude**

Description: double value of magnitude

Data Type: double

Default Value : 0.0

Syntax: dMagnitude = 1.0

**Arg2: ilNodeList**

Description: array int values of node list

Data Type: int list

Default Value : []

Syntax: ilNodeList = [1,2,3,4]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.NormalOffset(dMagnitude=0.0, ilNodeList=[])

```

==========================================================

# MeshEdit.MoveNode.CoincidentNodes

## Wrapper Macro

Coincident_Nodes(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > CoincidentNodes

## Command Description

Coincident Nodes

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: dTol**

Description: double value of tolerance

Data Type: double

Default Value : 0.01

Syntax: dTol = 1.0

**Arg3: bDesOrder**

Description: enable or disable feature des order

Data Type: bool

Default Value : False

Syntax: bDesOrder = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.CoincidentNodes(crlNode=[], dTol=0.01, bDesOrder=False)

```

==========================================================

# MeshEdit.MoveNode.AlongCylinder

## Wrapper Macro

MoveNodeAlongCylinder(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > AlongCylinder

## Command Description

Move node along cylinder surface

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg3: dIrX**

Description: double value of ir x

Data Type: double

Default Value : 0

Syntax: dIrX = 1.0

**Arg4: dIrY**

Description: double value of ir y

Data Type: double

Default Value : 0

Syntax: dIrY = 1.0

**Arg5: dIrZ**

Description: double value of ir z

Data Type: double

Default Value : 0

Syntax: dIrZ = 1.0

**Arg6: dCircleX**

Description: double value of circle x

Data Type: double

Default Value : 0

Syntax: dCircleX = 1.0

**Arg7: dCircleY**

Description: double value of circle y

Data Type: double

Default Value : 0

Syntax: dCircleY = 1.0

**Arg8: dCircleZ**

Description: double value of circle z

Data Type: double

Default Value : 0

Syntax: dCircleZ = 1.0

**Arg9: dRadius**

Description: double value of radius

Data Type: double

Default Value : 0

Syntax: dRadius = 1.0

**Arg10: dHeight**

Description: double value of height

Data Type: double

Default Value : 0

Syntax: dHeight = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.AlongCylinder(crlFace=[], crlNode=[], dIrX=0, dIrY=0, dIrZ=0, dCircleX=0, dCircleY=0, dCircleZ=0, dRadius=0, dHeight=0)

```

==========================================================

# MeshEdit.MoveNode.ProjectToPlane_3Nodes

## Wrapper Macro

MoveNodeNode2PlanNodes(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > ProjectToPlane_3Nodes

## Command Description

Move Nodes from Node to 3 nodes created Plane

## Argument List

**Arg1: ilNodeList**

Description: array int values of node list

Data Type: int list

Default Value : []

Syntax: ilNodeList = [1,2,3,4]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.ProjectToPlane_3Nodes(ilNodeList=[])

```

==========================================================

# MeshEdit.MoveNode.MoveNodeOffset

## Wrapper Macro

MoveNodeOffset(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > MoveNodeOffset

## Command Description

Command use for MeshEdit MoveNode MoveNodeOffset

## Argument List

**Arg1: dDeltaX**

Description: double value of delta x

Data Type: double

Default Value : 0.0

Syntax: dDeltaX = 1.0

**Arg2: dDeltaY**

Description: double value of delta y

Data Type: double

Default Value : 0.0

Syntax: dDeltaY = 1.0

**Arg3: dDeltaZ**

Description: double value of delta z

Data Type: double

Default Value : 0.0

Syntax: dDeltaZ = 1.0

**Arg4: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg5: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.MoveNodeOffset(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crlNode=[], crCoord=None)

```

==========================================================

# MeshEdit.MoveNode.RefineQuality

## Wrapper Macro

MeshEditMoveNodeRefineQuality(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > RefineQuality

## Command Description

MeshEdit RefineQuality

## Argument List

**Arg1: iMetric**

Description: option for metric

Data Type: integer

Default Value : 0

Syntax: iMetric = 1

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg4: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.RefineQuality(iMetric=0, crlFace=[], crlElem=[], crlNode=[])

```

==========================================================

# MeshEdit.MoveNode.StraightenMidnodes

## Wrapper Macro

MoveNodeStraightenMidNodesCr(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > StraightenMidnodes

## Command Description

move node by straighten_mid_nodes

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: crlEdge**

Description: array entities in model with type edge

Data Type: cursor list

Default Value : []

Syntax: crlEdge = [EntityType(id1, id2, id3)]

**Arg4: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.StraightenMidnodes(crlPart=[], crlFace=[], crlEdge=[], crlNode=[])

```

==========================================================

# MeshEdit.MoveNode.Offset

## Wrapper Macro

MeshEditMoveNodeOffset(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > Offset

## Command Description

MeshEdit MoveNode MoveNodeOffset

## Argument List

**Arg1: dDeltaX**

Description: double value of delta x

Data Type: double

Default Value : 0.0

Syntax: dDeltaX = 1.0

**Arg2: dDeltaY**

Description: double value of delta y

Data Type: double

Default Value : 0.0

Syntax: dDeltaY = 1.0

**Arg3: dDeltaZ**

Description: double value of delta z

Data Type: double

Default Value : 0.0

Syntax: dDeltaZ = 1.0

**Arg4: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg5: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.Offset(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crCoord=None, crlNode=[])

```

==========================================================

# MeshEdit.MoveNode.Laplacian

## Wrapper Macro

LaplacianSmooth(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > Laplacian

## Command Description

## Argument List

**Arg1: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg2: iType**

Description: option for type

Data Type: integer

Default Value : 0

Syntax: iType = 1

**Arg3: bWithCADFollow**

Description: enable or disable feature with c a d follow

Data Type: bool

Default Value : False

Syntax: bWithCADFollow = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.Laplacian(crlTarget=[], iType=0, bWithCADFollow=False)

```

==========================================================

# MeshEdit.MoveNode.AlongEdge

## Wrapper Macro

MeshEditMoveNodeOnEdge(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > AlongEdge

## Command Description

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: bMoveX**

Description: enable or disable feature move x

Data Type: bool

Default Value : False

Syntax: bMoveX = True/False

**Arg3: bMoveY**

Description: enable or disable feature move y

Data Type: bool

Default Value : False

Syntax: bMoveY = True/False

**Arg4: bMoveZ**

Description: enable or disable feature move z

Data Type: bool

Default Value : False

Syntax: bMoveZ = True/False

**Arg5: dPosX**

Description: double value of pos x

Data Type: double

Default Value : 0.0

Syntax: dPosX = 1.0

**Arg6: dPosY**

Description: double value of pos y

Data Type: double

Default Value : 0.0

Syntax: dPosY = 1.0

**Arg7: dPosZ**

Description: double value of pos z

Data Type: double

Default Value : 0.0

Syntax: dPosZ = 1.0

**Arg8: iMoveType**

Description: option for move type

Data Type: integer

Default Value : 0

Syntax: iMoveType = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.AlongEdge(crlNode=[], bMoveX=False, bMoveY=False, bMoveZ=False, dPosX=0.0, dPosY=0.0, dPosZ=0.0, iMoveType=0)

```

==========================================================

# MeshEdit.MoveNode.AlongDirection

## Wrapper Macro

NodeMovedByDirection(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > AlongDirection

## Command Description

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: crElem**

Description: entity in database model with type element

Data Type: cursor

Default Value : None

Syntax: crElem = EntityType(id)

**Arg3: crFace**

Description: entity in database model with type face

Data Type: cursor

Default Value : None

Syntax: crFace = EntityType(id)

**Arg4: vecDirection**

Description: array values of direction

Data Type: vector

Default Value : [0,0,0]

Syntax: vecDirection = [value1, value2, value3]

**Arg5: dMagnitude**

Description: double value of magnitude

Data Type: double

Default Value : 0.0

Syntax: dMagnitude = 1.0

**Arg6: bDestination**

Description: enable or disable feature destination

Data Type: bool

Default Value : False

Syntax: bDestination = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.AlongDirection(crlNode=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False)

```

==========================================================

# MeshEdit.MoveNode.CADFollows

## Wrapper Macro

MoveNodeCADFollows(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > CADFollows

## Command Description

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: dMovedPosX**

Description: double value of moved pos x

Data Type: double

Default Value : 0.0

Syntax: dMovedPosX = 1.0

**Arg3: dMovedPosY**

Description: double value of moved pos y

Data Type: double

Default Value : 0.0

Syntax: dMovedPosY = 1.0

**Arg4: dMovedPosZ**

Description: double value of moved pos z

Data Type: double

Default Value : 0.0

Syntax: dMovedPosZ = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.CADFollows(crlNode=[], dMovedPosX=0.0, dMovedPosY=0.0, dMovedPosZ=0.0)

```

==========================================================

# MeshEdit.MoveNode.Scale

## Wrapper Macro

MeshEditMoveNodeScale(...)

## Ribbon-GUI-Location

MeshEdit > MoveNode > Scale

## Command Description

Move node scale

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: crlNodeOrigin**

Description: array entities in model with type node origin

Data Type: cursor list

Default Value : []

Syntax: crlNodeOrigin = [EntityType(id1, id2, id3)]

**Arg3: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg4: posDeltaXYZ**

Description: array double value [x, y, z] in coordinate system of delta x y z

Data Type: position

Default Value : [10.0

Syntax: posDeltaXYZ = [x, y, z]

**Arg1: dDeltaX**

Description: double value of delta x

Data Type: double

Default Value : 0.0

Syntax: dDeltaX = 1.0

**Arg2: dDeltaY**

Description: double value of delta y

Data Type: double

Default Value : 0.0

Syntax: dDeltaY = 1.0

**Arg3: dDeltaZ**

Description: double value of delta z

Data Type: double

Default Value : 0.0

Syntax: dDeltaZ = 1.0

**Arg4: b1stCoord**

Description: data structure of True (refer PSJ Command Data Structure Document)

Data Type: True

Default Value : True

Syntax: b1stCoord = True(,,,)

**Arg5: b2ndCoord**

Description: data structure of True (refer PSJ Command Data Structure Document)

Data Type: True

Default Value : True

Syntax: b2ndCoord = True(,,,)

**Arg6: b3rdCoord**

Description: data structure of True (refer PSJ Command Data Structure Document)

Data Type: True

Default Value : True

Syntax: b3rdCoord = True(,,,)

**Arg7: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg8: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MoveNode.Absolute(dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNode=[], crCoord=None)

```

==========================================================

# MeshEdit.Face

## Wrapper Macro

MeshEditMorphingFaces(...)

## Ribbon-GUI-Location

MeshEdit > Face

## Command Description

Make Mesh deformation

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []Fixed

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: iOffsetType**

Description: option for offset type

Data Type: integer

Default Value : 0

Syntax: iOffsetType = 1

**Arg4: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg5: dlOffset**

Description: array double values of offset

Data Type: double list

Default Value : [1.0

Syntax: dlOffset = [1.0, 2.0]

**Arg8: dOffset**

Description: double value of offset

Data Type: double

Default Value : 0

Syntax: dOffset = 1.0

**Arg9: iDistType**

Description: option for distance type

Data Type: integer

Default Value : 0

Syntax: iDistType = 1

**Arg10: dDistStrong**

Description: double value of distance strong

Data Type: double

Default Value : 10

Syntax: dDistStrong = 1.0

**Arg11: dDistWeak**

Description: double value of distance weak

Data Type: double

Default Value : 20

Syntax: dDistWeak = 1.0

**Arg12: iNodeIdPick**

Description: option for node id pick

Data Type: integer

Default Value : -1

Syntax: iNodeIdPick = 1

**Arg13: dlPickForMacro**

Description: array double values of pick for macro

Data Type: double list

Default Value : []

Syntax: dlPickForMacro = [1.0, 2.0]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.Face(crlFace=[], crlFace=[]Fixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[])

```

==========================================================

# MeshEdit.ElementConvert

## Wrapper Macro

ElementConvert(...)

## Ribbon-GUI-Location

MeshEdit > ElementConvert

## Command Description

Element Conversion

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: iType**

Description: option for type

Data Type: integer

Default Value : 1

Syntax: iType = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.ElementConvert(crlPart=[], iType=1)

```

==========================================================

# MeshEdit.Deform

## Wrapper Macro

GeometryDeform(...)

## Ribbon-GUI-Location

MeshEdit > Deform

## Command Description

geometry deform

## Argument List

**Arg1: crlFacercObverse**

Description: array entities in model with type facerc obverse

Data Type: cursor list

Default Value : []

Syntax: crlFacercObverse = [EntityType(id1, id2, id3)]

**Arg2: crlFaceDstReverse**

Description: array entities in model with type face dst reverse

Data Type: cursor list

Default Value : []

Syntax: crlFaceDstReverse = [EntityType(id1, id2, id3)]

**Arg3: crlFacercReverse**

Description: array entities in model with type facerc reverse

Data Type: cursor list

Default Value : []

Syntax: crlFacercReverse = [EntityType(id1, id2, id3)]

**Arg4: crlFaceDstObverse**

Description: array entities in model with type face dst obverse

Data Type: cursor list

Default Value : []

Syntax: crlFaceDstObverse = [EntityType(id1, id2, id3)]

**Arg5: crlFaceFixed**

Description: array entities in model with type face fixed

Data Type: cursor list

Default Value : []

Syntax: crlFaceFixed = [EntityType(id1, id2, id3)]

**Arg6: dDistEffect**

Description: double value of distance effect

Data Type: double

Default Value : 0.02

Syntax: dDistEffect = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.Deform(crlFacercObverse=[], crlFaceDstReverse=[], crlFacercReverse=[], crlFaceDstObverse=[], crlFaceFixed=[], dDistEffect=0.02)

```

==========================================================

# MeshEdit.MirrorCopy

## Wrapper Macro

MirrorCopy(...)

## Ribbon-GUI-Location

MeshEdit > MirrorCopy

## Command Description

mirror copy of surface mesh

## Argument List

**Arg1: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.MirrorCopy(crlFace=[])

```

==========================================================

# MeshEdit.DeleteNode

## Wrapper Macro

DeleteNode(...)

## Ribbon-GUI-Location

MeshEdit > DeleteNode

## Command Description

Delete floating nodes in db

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: bRemoveVertex**

Description: enable or disable feature remove vertex

Data Type: bool

Default Value : True

Syntax: bRemoveVertex = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.DeleteNode(crlNode=[], bRemoveVertex=True)

```

==========================================================

# MeshEdit.FaceImprint

## Wrapper Macro

MeshEditCMPFaceImprint(...)

## Ribbon-GUI-Location

MeshEdit > FaceImprint

## Command Description

import Nastran bdf file

## Argument List

**Arg1: crlFaces**

Description: array entities in model with type faces

Data Type: cursor list

Default Value : []

Syntax: crlFaces = [EntityType(id1, id2, id3)]

**Arg2: bMeshCopy**

Description: enable or disable feature mesh copy

Data Type: bool

Default Value : False

Syntax: bMeshCopy = True/False

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.FaceImprint(crlFaces=[], bMeshCopy=False)

```

==========================================================

# MeshEdit.AdjustOrientation

## Wrapper Macro

GeomEditAdjustOrientation(...)

## Ribbon-GUI-Location

MeshEdit > AdjustOrientation

## Command Description

Adjust Orientation

## Argument List

**Arg1: crlPart**

Description: array entities in model with type part

Data Type: cursor list

Default Value : []

Syntax: crlPart = [EntityType(id1, id2, id3)]

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.AdjustOrientation(crlPart=[], crlFace=[], crlElem=[])

```

==========================================================

# MeshEdit.OneNode

## Wrapper Macro

MeshEditMorphingOneNode(...)

## Ribbon-GUI-Location

MeshEdit > OneNode

## Command Description

morphing one node

## Argument List

**Arg1: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

**Arg2: crlFaceFixed**

Description: array entities in model with type face fixed

Data Type: cursor list

Default Value : []

Syntax: crlFaceFixed = [EntityType(id1, id2, id3)]

**Arg3: bOffsetvector**

Description: enable or disable feature offsetvector

Data Type: bool

Default Value : False

Syntax: bOffsetvector = True/False

**Arg4: crCoord**

Description: entity in database model with type coordinate

Data Type: cursor

Default Value : None

Syntax: crCoord = EntityType(id)

**Arg5: dlOffset**

Description: array double values of offset

Data Type: double list

Default Value : [0

Syntax: dlOffset = [1.0, 2.0]

**Arg8: dOffset**

Description: double value of offset

Data Type: double

Default Value : 1

Syntax: dOffset = 1.0

**Arg9: iDisttype**

Description: option for disttype

Data Type: integer

Default Value : 0

Syntax: iDisttype = 1

**Arg10: dDiststrong**

Description: double value of diststrong

Data Type: double

Default Value : 1

Syntax: dDiststrong = 1.0

**Arg11: dDistweak**

Description: double value of distweak

Data Type: double

Default Value : 20

Syntax: dDistweak = 1.0

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.OneNode(crlNode=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDisttype=0, dDiststrong=10, dDistweak=20)

```

==========================================================

# MeshEdit.SeparateNodes

## Wrapper Macro

SeparateNode(...)

## Ribbon-GUI-Location

MeshEdit > SeparateNodes

## Command Description

Separate nodes

## Argument List

**Arg1: crlShareNodes**

Description: array entities in model with type share nodes

Data Type: cursor list

Default Value : []

Syntax: crlShareNodes = [EntityType(id1, id2, id3)]

**Arg2: crlTarget**

Description: array entities in database model

Data Type: cursor list

Default Value : []

Syntax: crlTarget = [EntityType(id1, id2, id3)]

**Arg3: iKeepNodeIDsOn**

Description: option for keep node i ds on

Data Type: integer

Default Value : 0

Syntax: iKeepNodeIDsOn = 1

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.SeparateNodes(crlShareNodes=[], crlTarget=[], iKeepNodeIDsOn=0)

```

==========================================================

# MeshEdit.RefineQuality

## Wrapper Macro

MeshEdit_RefineQuality(...)

## Ribbon-GUI-Location

MeshEdit > RefineQuality

## Command Description

Command use for MeshEdit RefineQuality

## Argument List

**Arg1: iMetric**

Description: option for metric

Data Type: integer

Default Value : 0

Syntax: iMetric = 1

**Arg2: crlFace**

Description: array entities in model with type face

Data Type: cursor list

Default Value : []

Syntax: crlFace = [EntityType(id1, id2, id3)]

**Arg3: crlElem**

Description: array entities in model with type element

Data Type: cursor list

Default Value : []

Syntax: crlElem = [EntityType(id1, id2, id3)]

**Arg4: crlNode**

Description: array entities in model with type node

Data Type: cursor list

Default Value : []

Syntax: crlNode = [EntityType(id1, id2, id3)]

## Return Value

Data Type: int

Return Value: 1 successed, 0 failed

## Example Code

```python

MeshEdit.RefineQuality(iMetric=0, crlFace=[], crlElem=[], crlNode=[])

```

==========================================================

# MeshEdit.Import



