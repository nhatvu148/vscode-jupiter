// AUTO-GENERATED — do not edit by hand.
// Merged from the PSJ editor IDEData (.dat) sources + the previously shipped
// callTips. Regenerate when the PSJ docs change.
//
// callTips: 1983 entries (was 1983, +0 new commands).

export interface CallTip {
  prefix: string;
  text: string;
}

export const callTips: Record<string, CallTip> = {
  "FileMenu.AddJTDB": {
    "prefix": "AddJTDB",
    "text": "*Name:* FileMenu.AddJTDB  \n*Desc:* add jtdb into model  \n *Arg1:* strFileName (String)  \n *Arg2:* strMethod (String)  \n *Arg3:* strTargetModel (String)  \n *Arg4:* strOption (String)  \n *Arg5:* iInputNode (Integer)  \n *Arg6:* iInputElem (Integer)  \n *Arg7:* iInputPart (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "FileMenu.Save": {
    "prefix": "Save",
    "text": "*Name:* FileMenu.Save  \n*Desc:* Save file JTDB  \n *Arg1:* strFileName (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "FileMenu.Open": {
    "prefix": "Open",
    "text": "*Name:* FileMenu.Open  \n*Desc:* Load JTDB file  \n *Arg1:* strFileName (String)  \n *Arg2:* bUseTmpTable (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Utility.FindEntities": {
    "prefix": "FindEntities",
    "text": "*Name:* Utility.FindEntities  \n*Desc:* Search entity by ID, Name ...etc  \n *Arg1:* strTarget (String)  \n *Arg2:* strFindType (String)  \n *Arg3:* bFindMatch (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* crEdgeFirst (Cursor)  \n *Arg2:* crEdgeLast (Cursor)  \n *Arg3:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "ACModeling.ACBoundary.FirstMethod": {
    "prefix": "FirstMethod",
    "text": "*Name:* ACModeling.ACBoundary.FirstMethod  \n*Desc:* Unknown Description  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* bIsMergePart (Boolean)  \n *Arg3:* bIsRenumber (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "ACModeling.Create.Convex": {
    "prefix": "Convex",
    "text": "*Name:* ACModeling.Create.Convex  \n*Desc:* Create Convex In Boundary  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* dMeshSize (Double)  \n *Arg3:* dOffset (Double)  \n *Arg4:* dRadius (Double)  \n *Arg5:* iDAxisGround (Integer)  \n *Arg6:* dScale (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "ACModeling.CloseHoleAuto": {
    "prefix": "CloseHoleAuto",
    "text": "*Name:* ACModeling.CloseHoleAuto  \n*Desc:* ACModeling CloseHoleAuto  \n *Arg1:* crlClosedHoleParts (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "ACModeling.Cut": {
    "prefix": "Cut",
    "text": "*Name:* ACModeling.Cut  \n*Desc:* cut for ACModeling  \n *Arg1:* crlPart (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.AbaqusStep.DynamicStep": {
    "prefix": "DynamicStep",
    "text": "*Name:* Analysis.AbaqusStep.DynamicStep  \n*Desc:* Unknown Description  \n *Arg1:* abaqusDynamic (ABAQUS_DYNAMIC)  \n *Arg2:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.AbaqusStep.TransientStep": {
    "prefix": "TransientStep",
    "text": "*Name:* Analysis.AbaqusStep.TransientStep  \n*Desc:*   \n *Arg1:* strName (String)  \n *Arg2:* strDesp (String)  \n *Arg3:* iEnableAutomatic (Integer)  \n *Arg4:* iMaxInc (Integer)  \n *Arg5:* dInitSize (Double)  \n *Arg6:* dMinSize (Double)  \n *Arg7:* dMaxSize (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.AbaqusStep.CoupledTDStep": {
    "prefix": "CoupledTDStep",
    "text": "*Name:* Analysis.AbaqusStep.CoupledTDStep  \n*Desc:* create abaqus step of coupled Temp-Displacement  \n *Arg1:* strName (String)  \n *Arg2:* strDesp (String)  \n *Arg3:* iEnableAutomatic (Integer)  \n *Arg4:* iMaxInc (Integer)  \n *Arg5:* dInitSize (Double)  \n *Arg6:* dMinSize (Double)  \n *Arg7:* dMaxSize (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.AbaqusStep.DynamicExplicitStep": {
    "prefix": "DynamicExplicitStep",
    "text": "*Name:* Analysis.AbaqusStep.DynamicExplicitStep  \n*Desc:* create abaqus step of dynamic explicit  \n *Arg1:* strName (String)  \n *Arg2:* strDesp (String)  \n *Arg3:* iEnableAutomatic (Integer)  \n *Arg4:* iIncrmtEstimator (Integer)  \n *Arg5:* abaqusPair1 (ABAQUS_PAIR1)  \n *Arg6:* dTimeScalfactor (Double)  \n *Arg7:* abaqusPair2 (ABAQUS_PAIR2)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.AbaqusStep.ModalStep": {
    "prefix": "ModalStep",
    "text": "*Name:* Analysis.AbaqusStep.ModalStep  \n*Desc:*   \n *Arg1:* strName (String)  \n *Arg2:* strDesp (String)  \n *Arg3:* iEigenSolver (Integer)  \n *Arg4:* iNFreqRequestbchecked (Integer)  \n *Arg5:* ilNFreqRequestTList (Integer List)  \n *Arg6:* iFreqShiftbchecked (Integer)  \n *Arg7:* ilFreqShiftTList (Integer List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.AbaqusStep.StaticRiskStep": {
    "prefix": "StaticRiskStep",
    "text": "*Name:* Analysis.AbaqusStep.StaticRiskStep  \n*Desc:* Abaqus Static Risk Step  \n *Arg1:* strName (String)  \n *Arg2:* strDesp (String)  \n *Arg3:* iEnableAutomatic (Integer)  \n *Arg4:* iMaxInc (Integer)  \n *Arg5:* dInitSize (Double)  \n *Arg6:* dMinSize (Double)  \n *Arg7:* dMaxSize (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.AbaqusStep.SteadyStateStep": {
    "prefix": "SteadyStateStep",
    "text": "*Name:* Analysis.AbaqusStep.SteadyStateStep  \n*Desc:* Abaqus Steady State Step  \n *Arg1:* strName (String)  \n *Arg2:* strDesp (String)  \n *Arg3:* iEnableAutomatic (Integer)  \n *Arg4:* iMaxInc (Integer)  \n *Arg5:* iNitSize (Integer)  \n *Arg6:* dMinSize (Double)  \n *Arg7:* dMaxSize (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ACTRAN.ExportBdf": {
    "prefix": "ExportBdf",
    "text": "*Name:* Analysis.ACTRAN.ExportBdf  \n*Desc:*   \n *Arg1:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ACTRAN.Run": {
    "prefix": "Run",
    "text": "*Name:* Analysis.ACTRAN.Run  \n*Desc:* Unknown Description  \n *Arg1:* actranAnalysis (ACTRAN_ANALYSIS)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ACTRAN.CreateEdat": {
    "prefix": "CreateEdat",
    "text": "*Name:* Analysis.ACTRAN.CreateEdat  \n*Desc:* Unknown Description  \n *Arg1:* actranAnalysis (ACTRAN_ANALYSIS)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Analysis.Abaqus": {
    "prefix": "Abaqus",
    "text": "*Name:* Analysis.Analysis.Abaqus  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* bRBE2toMPC (Boolean)  \n *Arg3:* bRenameProcess (Boolean)  \n *Arg4:* iCodeType (Integer)  \n *Arg5:* iSurfDefType (Integer)  \n *Arg6:* iUnit (Integer)  \n *Arg7:* iWriteType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Ansys.HeadTransferSteady": {
    "prefix": "HeadTransferSteady",
    "text": "*Name:* Analysis.Ansys.HeadTransferSteady  \n*Desc:* Set parameters  \n *Arg1:* strName (String)  \n *Arg2:* iJobdataAnatype (Integer)  \n *Arg3:* iJobdataSoltype (Integer)  \n *Arg4:* strJobdataJobname (String)  \n *Arg5:* strJobdataJobdescription (String)  \n *Arg6:* bBasicdataBoutputdisplacements (Boolean)  \n *Arg7:* bBasicdataBoutputreactionload (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Ansys.LinearStatic": {
    "prefix": "LinearStatic",
    "text": "*Name:* Analysis.Ansys.LinearStatic  \n*Desc:* Create and export Ansys job for Linear Static Structural  \n *Arg1:* strJobName (String)  \n *Arg2:* iJobdataAnatype (Integer)  \n *Arg3:* iJobdataSoltype (Integer)  \n *Arg4:* strJobdataJobname (String)  \n *Arg5:* strJobdataJobdescription (String)  \n *Arg6:* bBasicdataBoutputdisplacements (Boolean)  \n *Arg7:* bBasicdataBoutputreactionload (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Ansys.NormalModes": {
    "prefix": "NormalModes",
    "text": "*Name:* Analysis.Ansys.NormalModes  \n*Desc:* Create and export Ansys job for Normal Modes Structural  \n *Arg1:* strJobName (String)  \n *Arg2:* iJobdataAnatype (Integer)  \n *Arg3:* iJobdataSoltype (Integer)  \n *Arg4:* strJobdataJobname (String)  \n *Arg5:* strJobdataJobdescription (String)  \n *Arg6:* bBasicdataBoutputdisplacements (Boolean)  \n *Arg7:* bBasicdataBoutputreactionload (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Ansys.Harmonic": {
    "prefix": "Harmonic",
    "text": "*Name:* Analysis.Ansys.Harmonic  \n*Desc:* Create and export Ansys job for Harmonic Structural  \n *Arg1:* strJobName (String)  \n *Arg2:* iJobdataAnatype (Integer)  \n *Arg3:* iJobdataSoltype (Integer)  \n *Arg4:* strJobdataJobname (String)  \n *Arg5:* strJobdataJobdescription (String)  \n *Arg6:* bBasicdataBoutputdisplacements (Boolean)  \n *Arg7:* bBasicdataBoutputreactionload (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Ansys.Steady": {
    "prefix": "Steady",
    "text": "*Name:* Analysis.Ansys.Steady  \n*Desc:* Create and export Ansys job for Steady Heat Transfer  \n *Arg1:* strJobName (String)  \n *Arg2:* iJobdataAnatype (Integer)  \n *Arg3:* iJobdataSoltype (Integer)  \n *Arg4:* strJobdataJobname (String)  \n *Arg5:* strJobdataJobdescription (String)  \n *Arg6:* bBasicdataBoutputdisplacements (Boolean)  \n *Arg7:* bBasicdataBoutputreactionload (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Nastran.ModalTransientResponse": {
    "prefix": "ModalTransientResponse",
    "text": "*Name:* Analysis.Nastran.ModalTransientResponse  \n*Desc:* Export Nastran Modal Transient Response  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* bDummyPropAutoAssign (Boolean)  \n *Arg6:* iDummyPropMaterialID (Integer)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Nastran.LinearBuckling": {
    "prefix": "LinearBuckling",
    "text": "*Name:* Analysis.Nastran.LinearBuckling  \n*Desc:* Export Nastran Linear Buckling  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* bDummyPropAutoAssign (Boolean)  \n *Arg6:* iDummyPropMaterialID (Integer)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Nastran.Transient": {
    "prefix": "Transient",
    "text": "*Name:* Analysis.Nastran.Transient  \n*Desc:* Export Nastran Transient  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* bDummyPropAutoAssign (Boolean)  \n *Arg6:* iDummyPropMaterialID (Integer)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Nastran.SteadyState": {
    "prefix": "SteadyState",
    "text": "*Name:* Analysis.Nastran.SteadyState  \n*Desc:* Export Nastran Steady State  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* bDummyPropAutoAssign (Boolean)  \n *Arg6:* iDummyPropMaterialID (Integer)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Nastran.ModalFrequencyResponse": {
    "prefix": "ModalFrequencyResponse",
    "text": "*Name:* Analysis.Nastran.ModalFrequencyResponse  \n*Desc:* Export Nastran Modal Frequency Response  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* bDummyPropAutoAssign (Boolean)  \n *Arg6:* iDummyPropMaterialID (Integer)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Nastran.LinearStatic": {
    "prefix": "LinearStatic",
    "text": "*Name:* Analysis.Nastran.LinearStatic  \n*Desc:* Export Nastran Linear Static  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* bDummyPropAutoAssign (Boolean)  \n *Arg6:* iDummyPropMaterialID (Integer)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Nastran.NormalModes": {
    "prefix": "NormalModes",
    "text": "*Name:* Analysis.Nastran.NormalModes  \n*Desc:* Export Nastran Normal Modes  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* bDummyPropAutoAssign (Boolean)  \n *Arg6:* iDummyPropMaterialID (Integer)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Permas.Job": {
    "prefix": "Job",
    "text": "*Name:* Analysis.Permas.Job  \n*Desc:* permas output  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* iType (Integer)  \n *Arg4:* crEdit (Cursor)  \n *Arg5:* crlTarget (Cursor List)  \n *Arg6:* bElStress (Boolean)  \n *Arg7:* bElStressMis (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.ExportDynamisBdf": {
    "prefix": "ExportDynamisBdf",
    "text": "*Name:* Analysis.TSSolver.ExportDynamisBdf  \n*Desc:*   \n *Arg1:* strPath (String)  \n *Arg2:* crJob (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.Job": {
    "prefix": "Job",
    "text": "*Name:* Analysis.TSSolver.Job  \n*Desc:* Create TS-Solver Job  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.LinearBucking": {
    "prefix": "LinearBucking",
    "text": "*Name:* Analysis.TSSolver.LinearBucking  \n*Desc:* Export TS-Solver Linear Bucking  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.LinearStatic": {
    "prefix": "LinearStatic",
    "text": "*Name:* Analysis.TSSolver.LinearStatic  \n*Desc:* Export TS-Solver Linear Static  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.NonlinearStatic": {
    "prefix": "NonlinearStatic",
    "text": "*Name:* Analysis.TSSolver.NonlinearStatic  \n*Desc:* Export TS-Solver Nonlinear Static  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.NormalModes": {
    "prefix": "NormalModes",
    "text": "*Name:* Analysis.TSSolver.NormalModes  \n*Desc:* Export TS-Solver Normal Modes  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.NonlinearFrequency": {
    "prefix": "NonlinearFrequency",
    "text": "*Name:* Analysis.TSSolver.NonlinearFrequency  \n*Desc:* Export TS-Solver Nonlinear Frequency  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.ModalTransientResponse": {
    "prefix": "ModalTransientResponse",
    "text": "*Name:* Analysis.TSSolver.ModalTransientResponse  \n*Desc:* Export TS-Solver Modal Transient Response  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.TransientHeatTransfer": {
    "prefix": "TransientHeatTransfer",
    "text": "*Name:* Analysis.TSSolver.TransientHeatTransfer  \n*Desc:* Export TS-Solver Transient Heat Transfer  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.ModalFrequencyResponse": {
    "prefix": "ModalFrequencyResponse",
    "text": "*Name:* Analysis.TSSolver.ModalFrequencyResponse  \n*Desc:* Export TS-Solver Modal Frequency Response  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSolver.SteadyStateHeatTransfer": {
    "prefix": "SteadyStateHeatTransfer",
    "text": "*Name:* Analysis.TSSolver.SteadyStateHeatTransfer  \n*Desc:* Export TS-Solver Steady State Heat Transfer  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSS.TransientHeatTransfer": {
    "prefix": "TransientHeatTransfer",
    "text": "*Name:* Analysis.TSSS.TransientHeatTransfer  \n*Desc:* Export TS-SS Transient Heat Transfer  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* iRadialReturn (Integer)  \n *Arg6:* listNastranNonlinear (NASTRAN_NONLINEAR List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSS.LinearStatic": {
    "prefix": "LinearStatic",
    "text": "*Name:* Analysis.TSSS.LinearStatic  \n*Desc:* Export TS-SS Linear Static  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* iRadialReturn (Integer)  \n *Arg6:* listNastranNonlinear (NASTRAN_NONLINEAR List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSS.NonlinearStatic": {
    "prefix": "NonlinearStatic",
    "text": "*Name:* Analysis.TSSS.NonlinearStatic  \n*Desc:* Export TS-SS Nonlinear Static  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* iRadialReturn (Integer)  \n *Arg6:* listNastranNonlinear (NASTRAN_NONLINEAR List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSS.NormalModes": {
    "prefix": "NormalModes",
    "text": "*Name:* Analysis.TSSS.NormalModes  \n*Desc:* Export TS-SS Normal Modes  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* iRadialReturn (Integer)  \n *Arg6:* listNastranNonlinear (NASTRAN_NONLINEAR List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSS.LinearBuckling": {
    "prefix": "LinearBuckling",
    "text": "*Name:* Analysis.TSSS.LinearBuckling  \n*Desc:* Export TS-SS Linear Buckling  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* iRadialReturn (Integer)  \n *Arg6:* listNastranNonlinear (NASTRAN_NONLINEAR List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSS.ModalFrequencyResponse": {
    "prefix": "ModalFrequencyResponse",
    "text": "*Name:* Analysis.TSSS.ModalFrequencyResponse  \n*Desc:* Export TS-SS Modal Frequency Response  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* iRadialReturn (Integer)  \n *Arg6:* listNastranNonlinear (NASTRAN_NONLINEAR List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.TSSS.SteadyStateHeatTransfer": {
    "prefix": "SteadyStateHeatTransfer",
    "text": "*Name:* Analysis.TSSS.SteadyStateHeatTransfer  \n*Desc:* Export TS-SS Steady State Heat Transfer  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* iRadialReturn (Integer)  \n *Arg6:* listNastranNonlinear (NASTRAN_NONLINEAR List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.Abaqus": {
    "prefix": "Abaqus",
    "text": "*Name:* Analysis.Abaqus  \n*Desc:* abaqus exporting  \n *Arg1:* strName (String)  \n *Arg2:* bRBE2toMPC (Boolean)  \n *Arg3:* bRenameProcess (Boolean)  \n *Arg4:* iCodeType (Integer)  \n *Arg5:* iSurfDefType (Integer)  \n *Arg6:* iUnit (Integer)  \n *Arg7:* iWriteType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ExportAnsys": {
    "prefix": "ExportAnsys",
    "text": "*Name:* Analysis.ExportAnsys  \n*Desc:* Find faces in part by typical description  \n *Arg1:* strName (String)  \n *Arg2:* crAnsysJob (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ExportAbaqus": {
    "prefix": "ExportAbaqus",
    "text": "*Name:* Analysis.ExportAbaqus  \n*Desc:* export inp file  \n *Arg1:* crAbaJob (Cursor)  \n *Arg2:* crlSelectPart (Cursor List)  \n *Arg3:* strInpPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ModifyLbcToStep": {
    "prefix": "ModifyLbcToStep",
    "text": "*Name:* Analysis.ModifyLbcToStep  \n*Desc:* Abaqus analysis output data setting  \n *Arg1:* listAbaqusLbcStepInfo (ABAQUS_LBC_STEP_INFO List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ExportAdx": {
    "prefix": "ExportAdx",
    "text": "*Name:* Analysis.ExportAdx  \n*Desc:* export adx file  \n *Arg1:* crJob (Cursor)  \n *Arg2:* strPath (String)  \n *Arg3:* iNumType (Integer)  \n *Arg4:* iUiWidth (Integer)  \n *Arg5:* iUiPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ExportLsdyna": {
    "prefix": "ExportLsdyna",
    "text": "*Name:* Analysis.ExportLsdyna  \n*Desc:* Analysis LSDYNA ExportLsdyna  \n *Arg1:* strPath (String)  \n *Arg2:* crJob (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.NastranJob": {
    "prefix": "NastranJob",
    "text": "*Name:* Analysis.NastranJob  \n*Desc:* Create nastran Job  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* nastranAnalysis (NASTRAN_ANALYSIS)  \n *Arg5:* bDummyPropAutoAssign (Boolean)  \n *Arg6:* iDummyPropMaterialID (Integer)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.LSDYNAJob": {
    "prefix": "LSDYNAJob",
    "text": "*Name:* Analysis.LSDYNAJob  \n*Desc:* Create analysis LSDYNA job  \n *Arg1:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.Static": {
    "prefix": "Static",
    "text": "*Name:* Analysis.ADVC.MakeProcess.Static  \n*Desc:* create static process  \n *Arg1:* strName (String)  \n *Arg2:* iGeomNonlinear (Integer)  \n *Arg3:* advcStructTimeStep (ADVC_STRUCT_TIME_STEP)  \n *Arg4:* bConvergence (Boolean)  \n *Arg5:* advcConvergence (ADVC_CONVERGENCE)  \n *Arg6:* bContact (Boolean)  \n *Arg7:* advcContactIter (ADVC_CONTACT_ITER)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.Creep": {
    "prefix": "Creep",
    "text": "*Name:* Analysis.ADVC.MakeProcess.Creep  \n*Desc:* create creep process  \n *Arg1:* strName (String)  \n *Arg2:* iGeomNonlinear (Integer)  \n *Arg3:* advcStructTimeStep (ADVC_STRUCT_TIME_STEP)  \n *Arg4:* bConvergence (Boolean)  \n *Arg5:* advcConvergence (ADVC_CONVERGENCE)  \n *Arg6:* bContact (Boolean)  \n *Arg7:* advcContactIter (ADVC_CONTACT_ITER)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.Dynamic": {
    "prefix": "Dynamic",
    "text": "*Name:* Analysis.ADVC.MakeProcess.Dynamic  \n*Desc:* create dynamic process  \n *Arg1:* strName (String)  \n *Arg2:* iGeomNonlinear (Integer)  \n *Arg3:* advcStructTimeStep (ADVC_STRUCT_TIME_STEP)  \n *Arg4:* bConvergence (Boolean)  \n *Arg5:* advcConvergence (ADVC_CONVERGENCE)  \n *Arg6:* bContact (Boolean)  \n *Arg7:* advcContactIter (ADVC_CONTACT_ITER)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.EigenValue": {
    "prefix": "EigenValue",
    "text": "*Name:* Analysis.ADVC.MakeProcess.EigenValue  \n*Desc:* create advc eigen value process  \n *Arg1:* strName (String)  \n *Arg2:* bEigenValue (Boolean)  \n *Arg3:* iNumberOfModes (Integer)  \n *Arg4:* iEigenvecNorm (Integer)  \n *Arg5:* dShift (Double)  \n *Arg6:* dCgcgpiTol (Double)  \n *Arg7:* dCgcgpiEigTol (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.DynamicExplicit": {
    "prefix": "DynamicExplicit",
    "text": "*Name:* Analysis.ADVC.MakeProcess.DynamicExplicit  \n*Desc:* create dynamic explicit process.  \n *Arg1:* strName (String)  \n *Arg2:* iGeomNonlinear (Integer)  \n *Arg3:* advcStructTimeStep (ADVC_STRUCT_TIME_STEP)  \n *Arg4:* bConvergence (Boolean)  \n *Arg5:* advcConvergence (ADVC_CONVERGENCE)  \n *Arg6:* bContact (Boolean)  \n *Arg7:* advcContactIter (ADVC_CONTACT_ITER)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.ModalFreqResp": {
    "prefix": "ModalFreqResp",
    "text": "*Name:* Analysis.ADVC.MakeProcess.ModalFreqResp  \n*Desc:* create modal frequency response process of ADVC  \n *Arg1:* strName (String)  \n *Arg2:* strRefEigenDir (String)  \n *Arg3:* dRefLowFreq (Double)  \n *Arg4:* dRefHighFreq (Double)  \n *Arg5:* crModalDampingRatio (Cursor)  \n *Arg6:* crExcitationFreq (Cursor)  \n *Arg7:* bAutoFreqInterval (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.ResponseSpectrum": {
    "prefix": "ResponseSpectrum",
    "text": "*Name:* Analysis.ADVC.MakeProcess.ResponseSpectrum  \n*Desc:* create advc response spectrum process  \n *Arg1:* strName (String)  \n *Arg2:* strRefEigenDir (String)  \n *Arg3:* dRefLowFreq (Double)  \n *Arg4:* dRefHighFreq (Double)  \n *Arg5:* iPropMethod (Integer)  \n *Arg6:* iSpttype (Integer)  \n *Arg7:* dSptFactor0 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.SteadyState": {
    "prefix": "SteadyState",
    "text": "*Name:* Analysis.ADVC.MakeProcess.SteadyState  \n*Desc:* create advc heat transfer steady state process  \n *Arg1:* strName (String)  \n *Arg2:* iEndType (Integer)  \n *Arg3:* dMaxTime (Double)  \n *Arg4:* iFixedOrAuto (Integer)  \n *Arg5:* dMaxChange (Double)  \n *Arg6:* dInitDt (Double)  \n *Arg7:* iDefineMaxDt (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.Transient": {
    "prefix": "Transient",
    "text": "*Name:* Analysis.ADVC.MakeProcess.Transient  \n*Desc:* create advc heat transfer transient process  \n *Arg1:* strName (String)  \n *Arg2:* iEndType (Integer)  \n *Arg3:* dMaxTime (Double)  \n *Arg4:* dSteadyRate (Double)  \n *Arg5:* iFixedOrAuto (Integer)  \n *Arg6:* dMaxChange (Double)  \n *Arg7:* dInitDt (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.Fatigue": {
    "prefix": "Fatigue",
    "text": "*Name:* Analysis.ADVC.MakeProcess.Fatigue  \n*Desc:* create advc fatigue process  \n *Arg1:* strName (String)  \n *Arg2:* bFatigue (Boolean)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iStressAxis (Integer)  \n *Arg5:* iSafetyType (Integer)  \n *Arg6:* dSearchResolution (Double)  \n *Arg7:* dSafetyMax (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.MakeProcess.RandomResponse": {
    "prefix": "RandomResponse",
    "text": "*Name:* Analysis.ADVC.MakeProcess.RandomResponse  \n*Desc:* create advc random response process  \n *Arg1:* strName (String)  \n *Arg2:* strRefEigenDir (String)  \n *Arg3:* dRefLowFreq (Double)  \n *Arg4:* dRefHighFreq (Double)  \n *Arg5:* crModalDampingRatio (Cursor)  \n *Arg6:* crExcitationFreq (Cursor)  \n *Arg7:* bAutoFreqInterval (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.Structure": {
    "prefix": "Structure",
    "text": "*Name:* Analysis.ADVC.Structure  \n*Desc:* create advc job  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* iEJobType (Integer)  \n *Arg4:* crlProcessSequence (Cursor List)  \n *Arg5:* crlElemLocationGroup (Cursor List)  \n *Arg6:* crlNodeLocationGroup (Cursor List)  \n *Arg7:* bWriteGroup (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Analysis.ADVC.HeatTransfer": {
    "prefix": "HeatTransfer",
    "text": "*Name:* Analysis.ADVC.HeatTransfer  \n*Desc:* create advc job  \n *Arg1:* strName (String)  \n *Arg2:* strDescription (String)  \n *Arg3:* iEJobType (Integer)  \n *Arg4:* crlProcessSequence (Cursor List)  \n *Arg5:* crlElemLocationGroup (Cursor List)  \n *Arg6:* crlNodeLocationGroup (Cursor List)  \n *Arg7:* bWriteGroup (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.SeparateFaces.AllSharedNodes": {
    "prefix": "AllSharedNodes",
    "text": "*Name:* Assemble.SeparateFaces.AllSharedNodes  \n*Desc:* create by all shared nodes  \n *Arg1:*  ()  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.SeparateFaces.Shell": {
    "prefix": "Shell",
    "text": "*Name:* Assemble.SeparateFaces.Shell  \n*Desc:* Separate Faces for Shell  \n *Arg1:* iType (Integer)  \n *Arg2:* crlEntity (Cursor List)  \n *Arg3:* bCreateGroup (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.SeparateFaces.Solid": {
    "prefix": "Solid",
    "text": "*Name:* Assemble.SeparateFaces.Solid  \n*Desc:*   \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* bCreateGroup (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.Boolean": {
    "prefix": "Boolean",
    "text": "*Name:* Assemble.Boolean  \n*Desc:* Make Boolean between Parts  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* iBooleanType (Integer)  \n *Arg3:* dToleranceAlignment (Double)  \n *Arg4:* bLeaveOriginalBodies (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.AssembleFace": {
    "prefix": "AssembleFace",
    "text": "*Name:* Assemble.AssembleFace  \n*Desc:* create assemble face  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* dTolerance (Double)  \n *Arg4:* iFitEdge (Integer)  \n *Arg5:* iMeshSetting (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.FullLayer": {
    "prefix": "FullLayer",
    "text": "*Name:* Assemble.FullLayer  \n*Desc:* assemble full layer  \n *Arg1:* crPart (Cursor)  \n *Arg2:* dLayerWidth (Double)  \n *Arg3:* iLayer (Integer)  \n *Arg4:* bUsePyramid (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.CylinderLayer": {
    "prefix": "CylinderLayer",
    "text": "*Name:* Assemble.CylinderLayer  \n*Desc:* Assemble cylinder layer  \n *Arg1:* crFace (Cursor)  \n *Arg2:* crNode (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.SharedFace": {
    "prefix": "SharedFace",
    "text": "*Name:* Assemble.SharedFace  \n*Desc:* Create assemble shared face  \n *Arg1:*  ()  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.AssembleFaces": {
    "prefix": "AssembleFaces",
    "text": "*Name:* Assemble.AssembleFaces  \n*Desc:* Assemble AssembleFaces  \n *Arg1:* ilPairFaceToMakeShareFace (Integer List)  \n *Arg2:* dTolerance (Double)  \n *Arg3:* iTypeConnectPos (Integer)  \n *Arg4:* bUseSnapInput (Boolean)  \n *Arg5:* dSnapTolerance (Double)  \n *Arg6:* bFitEdge (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.GeneralLayer": {
    "prefix": "GeneralLayer",
    "text": "*Name:* Assemble.GeneralLayer  \n*Desc:*   \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dWidth (Double)  \n *Arg3:* iLayer (Integer)  \n *Arg4:* bSeparatePart (Boolean)  \n *Arg5:* bForceStitchToSide (Boolean)  \n *Arg6:* bSmoothingEdge (Boolean)  \n *Arg7:* bNoImprint (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.AddRib": {
    "prefix": "AddRib",
    "text": "*Name:* Assemble.AddRib  \n*Desc:* create Rib  \n *Arg1:* crPart (Cursor)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* veclPoints (Vector List)  \n *Arg4:* dWidth (Double)  \n *Arg5:* dDepth (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.FindMatingFace": {
    "prefix": "FindMatingFace",
    "text": "*Name:* Assemble.FindMatingFace  \n*Desc:* Find Mating Face For Assemble Faces  \n *Arg1:* crlMasterFaces (Cursor List)  \n *Arg2:* crlSlaveFaces (Cursor List)  \n *Arg3:* crlPart (Cursor List)  \n *Arg4:* dTolerance (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assemble.AddBoss": {
    "prefix": "AddBoss",
    "text": "*Name:* Assemble.AddBoss  \n*Desc:*   \n *Arg1:* crPart (Cursor)  \n *Arg2:* iType (Integer)  \n *Arg3:* bMerge (Boolean)  \n *Arg4:* posOrgCenter (Position)  \n *Arg5:* vecOrgDirection (Vector)  \n *Arg6:* crCoord (Cursor)  \n *Arg7:* iAxis (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assembly.RightClick.AddToReference": {
    "prefix": "AddToReference",
    "text": "*Name:* Assembly.RightClick.AddToReference  \n*Desc:* Add Reference to Body  \n *Arg1:* crSrcPart (Cursor)  \n *Arg2:* crDestPart (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assembly.RightClick.Suppress": {
    "prefix": "Suppress",
    "text": "*Name:* Assembly.RightClick.Suppress  \n*Desc:* Suppress/ Unsuppress part on Tree Assembly  \n *Arg1:* crlPart (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assembly.RightClick.UnSuppress": {
    "prefix": "UnSuppress",
    "text": "*Name:* Assembly.RightClick.UnSuppress  \n*Desc:* Unknown Description  \n *Arg1:* crlPart (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assembly.RightClick.RestoreOriginalPart": {
    "prefix": "RestoreOriginalPart",
    "text": "*Name:* Assembly.RightClick.RestoreOriginalPart  \n*Desc:* Restore body  \n *Arg1:* crlBodies (Cursor List)  \n *Arg2:* bKeepShareFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assembly.RightClick.Rename": {
    "prefix": "Rename",
    "text": "*Name:* Assembly.RightClick.Rename  \n*Desc:* Rename item  \n *Arg1:* strNewName (String)  \n *Arg2:* crItem (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assembly.RightClick.ChangeEntityColor": {
    "prefix": "ChangeEntityColor",
    "text": "*Name:* Assembly.RightClick.ChangeEntityColor  \n*Desc:* Unknown Description  \n *Arg1:* crlEntity (Cursor List)  \n *Arg2:* iColor (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assembly.RightClick.AddSubAssembly": {
    "prefix": "AddSubAssembly",
    "text": "*Name:* Assembly.RightClick.AddSubAssembly  \n*Desc:* Add sub assembly  \n *Arg1:* crInst (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assembly.RightClick.ChangeBodyColor": {
    "prefix": "ChangeBodyColor",
    "text": "*Name:* Assembly.RightClick.ChangeBodyColor  \n*Desc:* Change Body Color  \n *Arg1:* listPartColorPair (PART_COLOR_PAIR List)  \n *Arg2:* bResetFaceColor (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Assembly.RightClick.ChangeMeshLineColor": {
    "prefix": "ChangeMeshLineColor",
    "text": "*Name:* Assembly.RightClick.ChangeMeshLineColor  \n*Desc:* Change Entity color  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* iColor (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.BoundaryTemperature.Constant": {
    "prefix": "Constant",
    "text": "*Name:* BoundaryConditions.BoundaryTemperature.Constant  \n*Desc:* Create boundary temperature  \n *Arg1:* strName (String)  \n *Arg2:* dFTemp (Double)  \n *Arg3:* crTable (Cursor)  \n *Arg4:* crlTarget (Cursor List)  \n *Arg5:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.BoundaryTemperature.SurfaceMapping": {
    "prefix": "SurfaceMapping",
    "text": "*Name:* BoundaryConditions.BoundaryTemperature.SurfaceMapping  \n*Desc:* Create mapping boundary temperature  \n *Arg1:* strName (String)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* iMAPPos (Integer)  \n *Arg4:* iViewCp (Integer)  \n *Arg5:* iCp (Integer)  \n *Arg6:* iSrcType (Integer)  \n *Arg7:* iMappedCpIndexArr0 (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Convection.Constant": {
    "prefix": "Constant",
    "text": "*Name:* BoundaryConditions.Convection.Constant  \n*Desc:* Create lbc of convection  \n *Arg1:* strName (String)  \n *Arg2:* dExtTemp (Double)  \n *Arg3:* crTableTimeTemp (Cursor)  \n *Arg4:* dDcoef (Double)  \n *Arg5:* crTableTimeCoeff (Cursor)  \n *Arg6:* crTableTempCoeff (Cursor)  \n *Arg7:* crlTarget (Cursor List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Convection.SurfaceMapping": {
    "prefix": "SurfaceMapping",
    "text": "*Name:* BoundaryConditions.Convection.SurfaceMapping  \n*Desc:* Create lbc of convection Surface Mapping  \n *Arg1:* strName (String)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* iPos (Integer)  \n *Arg4:* iViewCp (Integer)  \n *Arg5:* iCp (Integer)  \n *Arg6:* iSrcType (Integer)  \n *Arg7:* iMappedCpIndex0 (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.EnforcedLoads.Acceleration": {
    "prefix": "Acceleration",
    "text": "*Name:* BoundaryConditions.EnforcedLoads.Acceleration  \n*Desc:* Set enforced acceleration  \n *Arg1:* strName (String)  \n *Arg2:* iDwDof (Integer)  \n *Arg3:* dFVel1 (Double)  \n *Arg4:* dFVel2 (Double)  \n *Arg5:* dFVel3 (Double)  \n *Arg6:* dFVel4 (Double)  \n *Arg7:* dFVel5 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.EnforcedLoads.Velocity": {
    "prefix": "Velocity",
    "text": "*Name:* BoundaryConditions.EnforcedLoads.Velocity  \n*Desc:* create enforced velocity  \n *Arg1:* strName (String)  \n *Arg2:* iDwDof (Integer)  \n *Arg3:* dFVel0 (Double)  \n *Arg4:* dFVel1 (Double)  \n *Arg5:* dFVel2 (Double)  \n *Arg6:* dFVel3 (Double)  \n *Arg7:* dFVel4 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.EnforcedLoads.Displacement": {
    "prefix": "Displacement",
    "text": "*Name:* BoundaryConditions.EnforcedLoads.Displacement  \n*Desc:* create enforced displacement  \n *Arg1:* strName (String)  \n *Arg2:* iDwDof (Integer)  \n *Arg3:* dFDisp0 (Double)  \n *Arg4:* dFDisp1 (Double)  \n *Arg5:* dFDisp2 (Double)  \n *Arg6:* dFDisp3 (Double)  \n *Arg7:* dFDisp4 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.HeatFlux.SurfaceFlux": {
    "prefix": "SurfaceFlux",
    "text": "*Name:* BoundaryConditions.HeatFlux.SurfaceFlux  \n*Desc:* create surface flux  \n *Arg1:* strName (String)  \n *Arg2:* dFflux (Double)  \n *Arg3:* iDistributionMethod (Integer)  \n *Arg4:* crTable (Cursor)  \n *Arg5:* crlTarget (Cursor List)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.HeatFlux.SurfaceMapping": {
    "prefix": "SurfaceMapping",
    "text": "*Name:* BoundaryConditions.HeatFlux.SurfaceMapping  \n*Desc:* Create mapping heat flux  \n *Arg1:* strName (String)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* iMAPPos (Integer)  \n *Arg4:* iViewCp (Integer)  \n *Arg5:* iCp (Integer)  \n *Arg6:* iSrcType (Integer)  \n *Arg7:* iMappedCpIndexArr0 (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.HeatFlux.ConcentrateFlux": {
    "prefix": "ConcentrateFlux",
    "text": "*Name:* BoundaryConditions.HeatFlux.ConcentrateFlux  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* lbcConcentrateFluxData (LBC_CONCENTRATE_FLUX_DATA)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InitialElementalValue.InitialStress": {
    "prefix": "InitialStress",
    "text": "*Name:* BoundaryConditions.InitialElementalValue.InitialStress  \n*Desc:* create mapping stress  \n *Arg1:* strName (String)  \n *Arg2:* iDimension (Integer)  \n *Arg3:* iElemCs (Integer)  \n *Arg4:* dSXX (Double)  \n *Arg5:* dSYY (Double)  \n *Arg6:* dSXY (Double)  \n *Arg7:* crTable (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InitialTemperature.WholeMapping": {
    "prefix": "WholeMapping",
    "text": "*Name:* BoundaryConditions.InitialTemperature.WholeMapping  \n*Desc:* Create initial temperature whole mapping  \n *Arg1:* strName (String)  \n *Arg2:* iMapSourceType (Integer)  \n *Arg3:* strPath (String)  \n *Arg4:* iMappingMethod (Integer)  \n *Arg5:* iIsubcase (Integer)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InitialTemperature.Constant": {
    "prefix": "Constant",
    "text": "*Name:* BoundaryConditions.InitialTemperature.Constant  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* strFilePathName (String)  \n *Arg3:* bUseDefault (Boolean)  \n *Arg4:* crTable (Cursor)  \n *Arg5:* crlTarget (Cursor List)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InitialTemperature.ADVC": {
    "prefix": "ADVC",
    "text": "*Name:* BoundaryConditions.InitialTemperature.ADVC  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* strFilePathName (String)  \n *Arg3:* bUseDefault (Boolean)  \n *Arg4:* crTable (Cursor)  \n *Arg5:* crlTarget (Cursor List)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InitialTemperature.NastranPunch": {
    "prefix": "NastranPunch",
    "text": "*Name:* BoundaryConditions.InitialTemperature.NastranPunch  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* strFilePathName (String)  \n *Arg3:* bUseDefault (Boolean)  \n *Arg4:* crTable (Cursor)  \n *Arg5:* crlTarget (Cursor List)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.PropertiesCopyTranslate": {
    "prefix": "PropertiesCopyTranslate",
    "text": "*Name:* BoundaryConditions.LBCCopy.PropertiesCopyTranslate  \n*Desc:* Copy property translate  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* posVecTrans (Position)  \n *Arg4:* dMagnitude (Double)  \n *Arg5:* dTrandataDoffset (Double)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.PropertiesCopyRotate": {
    "prefix": "PropertiesCopyRotate",
    "text": "*Name:* BoundaryConditions.LBCCopy.PropertiesCopyRotate  \n*Desc:* Copy property rotate  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* posAxis (Position)  \n *Arg4:* posCenter (Position)  \n *Arg5:* dAngle (Double)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.PropertiesCopyMirror": {
    "prefix": "PropertiesCopyMirror",
    "text": "*Name:* BoundaryConditions.LBCCopy.PropertiesCopyMirror  \n*Desc:* Copy property mirror  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* poslPoints (Position List)  \n *Arg4:* dOffset (Double)  \n *Arg5:* dTol (Double)  \n *Arg6:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.ConnectionCopyTranslate": {
    "prefix": "ConnectionCopyTranslate",
    "text": "*Name:* BoundaryConditions.LBCCopy.ConnectionCopyTranslate  \n*Desc:* Copy connection translate  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* posVecTrans (Position)  \n *Arg4:* dMagnitude (Double)  \n *Arg5:* dTrandataDoffset (Double)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.ConnectionCopyRotate": {
    "prefix": "ConnectionCopyRotate",
    "text": "*Name:* BoundaryConditions.LBCCopy.ConnectionCopyRotate  \n*Desc:* Copy Connection rotate  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* posAxis (Position)  \n *Arg4:* posCenter (Position)  \n *Arg5:* dAngle (Double)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.ConnectionCopyMirror": {
    "prefix": "ConnectionCopyMirror",
    "text": "*Name:* BoundaryConditions.LBCCopy.ConnectionCopyMirror  \n*Desc:* Copy Connection mirror  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* poslPoints (Position List)  \n *Arg4:* dOffset (Double)  \n *Arg5:* dTol (Double)  \n *Arg6:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.GroupCopyTranslate": {
    "prefix": "GroupCopyTranslate",
    "text": "*Name:* BoundaryConditions.LBCCopy.GroupCopyTranslate  \n*Desc:* Copy group translate  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* posVecTrans (Position)  \n *Arg4:* dMagnitude (Double)  \n *Arg5:* dTrandataDoffset (Double)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.GroupCopyRotate": {
    "prefix": "GroupCopyRotate",
    "text": "*Name:* BoundaryConditions.LBCCopy.GroupCopyRotate  \n*Desc:* Copy Group rotate  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* posAxis (Position)  \n *Arg4:* posCenter (Position)  \n *Arg5:* dAngle (Double)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.GroupCopyMirror": {
    "prefix": "GroupCopyMirror",
    "text": "*Name:* BoundaryConditions.LBCCopy.GroupCopyMirror  \n*Desc:* Copy Group mirror  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* poslPoints (Position List)  \n *Arg4:* dOffset (Double)  \n *Arg5:* dTol (Double)  \n *Arg6:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.LBCCopyTranslate": {
    "prefix": "LBCCopyTranslate",
    "text": "*Name:* BoundaryConditions.LBCCopy.LBCCopyTranslate  \n*Desc:* Copy LBC translate  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* posVecTrans (Position)  \n *Arg4:* dMagnitude (Double)  \n *Arg5:* dTrandataDoffset (Double)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.LBCCopyRotate": {
    "prefix": "LBCCopyRotate",
    "text": "*Name:* BoundaryConditions.LBCCopy.LBCCopyRotate  \n*Desc:* Copy LBC rotate  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* posAxis (Position)  \n *Arg4:* posCenter (Position)  \n *Arg5:* dAngle (Double)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopy.LBCCopyMirror": {
    "prefix": "LBCCopyMirror",
    "text": "*Name:* BoundaryConditions.LBCCopy.LBCCopyMirror  \n*Desc:* Copy LBC mirror  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* poslPoints (Position List)  \n *Arg4:* dOffset (Double)  \n *Arg5:* dTol (Double)  \n *Arg6:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Pressure.SurfaceLoads": {
    "prefix": "SurfaceLoads",
    "text": "*Name:* BoundaryConditions.Pressure.SurfaceLoads  \n*Desc:* create distrubited pressure  \n *Arg1:* strName (String)  \n *Arg2:* dlPressure (Double List)  \n *Arg3:* iArrowdir (Integer)  \n *Arg4:* crCoordinate (Cursor)  \n *Arg5:* crlTargetFace (Cursor List)  \n *Arg6:* crEditCur (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Create lbc of 2nodes pressure  \n *Arg1:* strName (String)  \n *Arg2:* crNodeA (Cursor)  \n *Arg3:* dPressureA (Double)  \n *Arg4:* iNodeAUnit (Integer)  \n *Arg5:* crNodeB (Cursor)  \n *Arg6:* dPressureB (Double)  \n *Arg7:* iNodeBUnit (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Pressure.General": {
    "prefix": "General",
    "text": "*Name:* BoundaryConditions.Pressure.General  \n*Desc:* Create general pressure boundary condition  \n *Arg1:* strName (String)  \n *Arg2:* dFpressure (Double)  \n *Arg3:* iIdistribute (Integer)  \n *Arg4:* crTable (Cursor)  \n *Arg5:* dDphase (Double)  \n *Arg6:* dDdelay (Double)  \n *Arg7:* crPhaseTable (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Pressure.Quadratic": {
    "prefix": "Quadratic",
    "text": "*Name:* BoundaryConditions.Pressure.Quadratic  \n*Desc:* Create Pressure quadratic  \n *Arg1:* strName (String)  \n *Arg2:* dA (Double)  \n *Arg3:* dB (Double)  \n *Arg4:* crCoordinate (Cursor)  \n *Arg5:* dAngleRange (Double)  \n *Arg6:* iPressureDirectionMode (Integer)  \n *Arg7:* dlPressureDirection (Double List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Pressure.FunctionLoadToCylinderSine": {
    "prefix": "FunctionLoadToCylinderSine",
    "text": "*Name:* BoundaryConditions.Pressure.FunctionLoadToCylinderSine  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* dA (Double)  \n *Arg3:* crCoordinate (Cursor)  \n *Arg4:* dAngleRange (Double)  \n *Arg5:* bDistributionAxis (Boolean)  \n *Arg6:* iPressureDirectionMode (Integer)  \n *Arg7:* bIsTotalForceAdjustment (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Pressure.Hydrostatic": {
    "prefix": "Hydrostatic",
    "text": "*Name:* BoundaryConditions.Pressure.Hydrostatic  \n*Desc:* Boundary Conditions HPressure  \n *Arg1:* strName (String)  \n *Arg2:* dFHPressure (Double)  \n *Arg3:* dFDensity (Double)  \n *Arg4:* iDensityUnit (Integer)  \n *Arg5:* dFGravity (Double)  \n *Arg6:* iGravityUnit (Integer)  \n *Arg7:* iGravityDir (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Pressure.SurfaceMapping": {
    "prefix": "SurfaceMapping",
    "text": "*Name:* BoundaryConditions.Pressure.SurfaceMapping  \n*Desc:* Create mapping pressure  \n *Arg1:* strName (String)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* iMAPPos (Integer)  \n *Arg4:* iViewCp (Integer)  \n *Arg5:* iCp (Integer)  \n *Arg6:* iSrcType (Integer)  \n *Arg7:* iMappedCpIndexArr (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Submodel.SubmodelForcedFlux": {
    "prefix": "SubmodelForcedFlux",
    "text": "*Name:* BoundaryConditions.Submodel.SubmodelForcedFlux  \n*Desc:* create submodel forced flux  \n *Arg1:* strName (String)  \n *Arg2:* iSolver (Integer)  \n *Arg3:* strFilePathName (String)  \n *Arg4:* iProcessNo (Integer)  \n *Arg5:* iReferType (Integer)  \n *Arg6:* dExtensionRange (Double)  \n *Arg7:* dExtensionTol (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Submodel.ForcedTempertature": {
    "prefix": "ForcedTempertature",
    "text": "*Name:* BoundaryConditions.Submodel.ForcedTempertature  \n*Desc:* create sub model forced temperature  \n *Arg1:* strName (String)  \n *Arg2:* iSolver (Integer)  \n *Arg3:* strFilePathName (String)  \n *Arg4:* iProcessNo (Integer)  \n *Arg5:* iReferType (Integer)  \n *Arg6:* dExtensionRange (Double)  \n *Arg7:* dExtensionTol (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Submodel.ForcedDisplacement": {
    "prefix": "ForcedDisplacement",
    "text": "*Name:* BoundaryConditions.Submodel.ForcedDisplacement  \n*Desc:* Boundary Conditions Lbc Submodel Forced Disp  \n *Arg1:* strName (String)  \n *Arg2:* iSolver (Integer)  \n *Arg3:* strFilePathName (String)  \n *Arg4:* iProcessNo (Integer)  \n *Arg5:* bTranslationX (Boolean)  \n *Arg6:* bTranslationY (Boolean)  \n *Arg7:* bTranslationZ (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.TemperatureLoads.Constant": {
    "prefix": "Constant",
    "text": "*Name:* BoundaryConditions.TemperatureLoads.Constant  \n*Desc:* create temperature load constant  \n *Arg1:* strName (String)  \n *Arg2:* dTemperature (Double)  \n *Arg3:* crTable (Cursor)  \n *Arg4:* crlTarget (Cursor List)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* bUseDefaultTemp (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.TemperatureLoads.ADVCFile": {
    "prefix": "ADVCFile",
    "text": "*Name:* BoundaryConditions.TemperatureLoads.ADVCFile  \n*Desc:* create temperature load by advc file  \n *Arg1:* strName (String)  \n *Arg2:* strFilePathName (String)  \n *Arg3:* crTable (Cursor)  \n *Arg4:* crlTarget (Cursor List)  \n *Arg5:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.TemperatureLoads.NastranPunch": {
    "prefix": "NastranPunch",
    "text": "*Name:* BoundaryConditions.TemperatureLoads.NastranPunch  \n*Desc:* create temperature load of nastran punch  \n *Arg1:* strName (String)  \n *Arg2:* strFilePathName (String)  \n *Arg3:* crTable (Cursor)  \n *Arg4:* crlTarget (Cursor List)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* bUseAsMaterialReferenceTemp (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.TemperatureLoads.WholeMapping": {
    "prefix": "WholeMapping",
    "text": "*Name:* BoundaryConditions.TemperatureLoads.WholeMapping  \n*Desc:* Create mapping pressure  \n *Arg1:* strName (String)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* iMAPPos (Integer)  \n *Arg4:* iViewCp (Integer)  \n *Arg5:* iCp (Integer)  \n *Arg6:* iSrcType (Integer)  \n *Arg7:* iMappedCpIndexArr0 (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.TemperatureLoads.LbcInitialTemperature": {
    "prefix": "LbcInitialTemperature",
    "text": "*Name:* BoundaryConditions.TemperatureLoads.LbcInitialTemperature  \n*Desc:* Boundary Conditions Lbc Initial Temperature  \n *Arg1:* strName (String)  \n *Arg2:* iType (Integer)  \n *Arg3:* dFTemp (Double)  \n *Arg4:* strFilePathName (String)  \n *Arg5:* bUseDefault (Boolean)  \n *Arg6:* crTable (Cursor)  \n *Arg7:* crlTarget (Cursor List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LoadCase": {
    "prefix": "LoadCase",
    "text": "*Name:* BoundaryConditions.LoadCase  \n*Desc:* create load case  \n *Arg1:* strName (String)  \n *Arg2:* dFactor (Double)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* iExportId (Integer)  \n *Arg5:* dlTargetFactor (Double List)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InsideHeatGeneration": {
    "prefix": "InsideHeatGeneration",
    "text": "*Name:* BoundaryConditions.InsideHeatGeneration  \n*Desc:* Create lbc of inside heat generation  \n *Arg1:* strName (String)  \n *Arg2:* dInsideFlux (Double)  \n *Arg3:* crTable (Cursor)  \n *Arg4:* crlTarget (Cursor List)  \n *Arg5:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LBCCopyMisc": {
    "prefix": "LBCCopyMisc",
    "text": "*Name:* BoundaryConditions.LBCCopyMisc  \n*Desc:* Unknown Description  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iMatchMethod (Integer)  \n *Arg3:* dlTransVec (Double List)  \n *Arg4:* dTransMag (Double)  \n *Arg5:* dTransOffset (Double)  \n *Arg6:* dTransTol (Double)  \n *Arg7:* crTranscrCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.LbcContactConvert": {
    "prefix": "LbcContactConvert",
    "text": "*Name:* BoundaryConditions.LbcContactConvert  \n*Desc:* BoundaryConditions LbcContactConvert  \n *Arg1:* iConvertTo (Integer)  \n *Arg2:* iTieConvType (Integer)  \n *Arg3:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.FieldData": {
    "prefix": "FieldData",
    "text": "*Name:* BoundaryConditions.FieldData  \n*Desc:* create field data table  \n *Arg1:* strName (String)  \n *Arg2:* iType (Integer)  \n *Arg3:* ilSheet (Integer List)  \n *Arg4:* crEdit (Cursor)  \n *Arg5:* bAbaqusAmp (Boolean)  \n *Arg6:* iAmpType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.FixedConstraint": {
    "prefix": "FixedConstraint",
    "text": "*Name:* BoundaryConditions.FixedConstraint  \n*Desc:* create FixedConstraint  \n *Arg1:* strName (String)  \n *Arg2:* iDwDof (Integer)  \n *Arg3:* crCurCoord (Cursor)  \n *Arg4:* iType (Integer)  \n *Arg5:* iUsetType (Integer)  \n *Arg6:* crTable (Cursor)  \n *Arg7:* bAbaqusFixed (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.DofSet": {
    "prefix": "DofSet",
    "text": "*Name:* BoundaryConditions.DofSet  \n*Desc:* Lbc Dof Set  \n *Arg1:* strName (String)  \n *Arg2:* iDwDof (Integer)  \n *Arg3:* crCurCoord (Cursor)  \n *Arg4:* crTable (Cursor)  \n *Arg5:* crlTarget (Cursor List)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems": {
    "prefix": "CoordinateSystems",
    "text": "*Name:* BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems  \n*Desc:* create centrifugal force by coordinate system  \n *Arg1:* strName (String)  \n *Arg2:* dFVelocity (Double)  \n *Arg3:* dFAcceleration (Double)  \n *Arg4:* iAxisDirection (Integer)  \n *Arg5:* iVelocityUnit (Integer)  \n *Arg6:* iAccelerationUnit (Integer)  \n *Arg7:* crCurCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions": {
    "prefix": "TwoPositions",
    "text": "*Name:* BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions  \n*Desc:* create centrifugal force  \n *Arg1:* strName (String)  \n *Arg2:* dFBasePoint1 (Double)  \n *Arg3:* dFBasePoint2 (Double)  \n *Arg4:* dFBasePoint3 (Double)  \n *Arg5:* dFTipPoint1 (Double)  \n *Arg6:* dFTipPoint2 (Double)  \n *Arg7:* dFTipPoint3 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.BodyLoads.Gravity": {
    "prefix": "Gravity",
    "text": "*Name:* BoundaryConditions.BodyLoads.Gravity  \n*Desc:* create gravity  \n *Arg1:* strName (String)  \n *Arg2:* dlGravity (Double List)  \n *Arg3:* crCurCoord (Cursor)  \n *Arg4:* crlTarget (Cursor List)  \n *Arg5:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Force.FunctionLoadCylinder.Quadratic": {
    "prefix": "Quadratic",
    "text": "*Name:* BoundaryConditions.Force.FunctionLoadCylinder.Quadratic  \n*Desc:* Create Force (Quadratic) y = a*x^2 + b  \n *Arg1:* strName (String)  \n *Arg2:* dFTotalForce (Double)  \n *Arg3:* dA (Double)  \n *Arg4:* dB (Double)  \n *Arg5:* crCoord (Cursor)  \n *Arg6:* iAngleBase (Integer)  \n *Arg7:* dAngleRange (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Force.FunctionLoadCylinder.Sine": {
    "prefix": "Sine",
    "text": "*Name:* BoundaryConditions.Force.FunctionLoadCylinder.Sine  \n*Desc:* Define the force load on selected entity based on the distribution of the sine function.  \n *Arg1:* strName (String)  \n *Arg2:* dFTotalForce (Double)  \n *Arg3:* dA (Double)  \n *Arg4:* crCoord (Cursor)  \n *Arg5:* iAngleBase (Integer)  \n *Arg6:* dAngleRange (Double)  \n *Arg7:* iEnArrowDir (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Force.FunctionLoadCylinder.Vector": {
    "prefix": "Vector",
    "text": "*Name:* BoundaryConditions.Force.FunctionLoadCylinder.Vector  \n*Desc:* Define the force load on selected entity based on the distribution of the vector function.  \n *Arg1:* strName (String)  \n *Arg2:* dFTotalForce (Double)  \n *Arg3:* dA (Double)  \n *Arg4:* dX (Double)  \n *Arg5:* dY (Double)  \n *Arg6:* crCoord (Cursor)  \n *Arg7:* iEnDirection (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* create nonlinear force NOLIN3  \n *Arg1:* strName (String)  \n *Arg2:* dForceScale (Double)  \n *Arg3:* dMomentScale (Double)  \n *Arg4:* dForcePowerA (Double)  \n *Arg5:* dMomentPowerA (Double)  \n *Arg6:* iForcDir (Integer)  \n *Arg7:* iForceDepends (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* create NOLIN4 nonlinear force  \n *Arg1:* strName (String)  \n *Arg2:* dForceScale (Double)  \n *Arg3:* dMomentScale (Double)  \n *Arg4:* dForcePowerA (Double)  \n *Arg5:* dMomentPowerA (Double)  \n *Arg6:* iForcDir (Integer)  \n *Arg7:* iForceDepends (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Create Nonlinear Force of NOLIN1(Table)  \n *Arg1:* strName (String)  \n *Arg2:* dForceScale (Double)  \n *Arg3:* dMomentScale (Double)  \n *Arg4:* iForcDir (Integer)  \n *Arg5:* iForceDepends (Integer)  \n *Arg6:* iMomentDir (Integer)  \n *Arg7:* iMomentDepends (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Force.General": {
    "prefix": "General",
    "text": "*Name:* BoundaryConditions.Force.General  \n*Desc:* create force general  \n *Arg1:* strName (String)  \n *Arg2:* DFLT_DBL (DFLT_DBL)  \n *Arg3:* DFLT_DBL] (DFLT_DBL])  \n *Arg4:* vecForce (Vector)  \n *Arg5:* DFLT_DBL (DFLT_DBL)  \n *Arg6:* DFLT_DBL] (DFLT_DBL])  \n *Arg7:* vecMoment (Vector)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.Force.ForceNormalDirection": {
    "prefix": "ForceNormalDirection",
    "text": "*Name:* BoundaryConditions.Force.ForceNormalDirection  \n*Desc:* Create Force (normal direction)  \n *Arg1:* strName (String)  \n *Arg2:* DFLT_DBL (DFLT_DBL)  \n *Arg3:* DFLT_DBL] (DFLT_DBL])  \n *Arg4:* vecForce (Vector)  \n *Arg5:* iEnArrowDir (Integer)  \n *Arg6:* iDistributionMethod (Integer)  \n *Arg7:* crCurCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus": {
    "prefix": "Abaqus",
    "text": "*Name:* BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus  \n*Desc:* Create lbc of initial angular velocity for abaqus  \n *Arg1:* strName (String)  \n *Arg2:* dVelocity (Double)  \n *Arg3:* strFirstCoord (String)  \n *Arg4:* strSecondCoord (String)  \n *Arg5:* crlTarget (Cursor List)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General": {
    "prefix": "General",
    "text": "*Name:* BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* stData (ST_DATA)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InitialNodalValue.Displacement": {
    "prefix": "Displacement",
    "text": "*Name:* BoundaryConditions.InitialNodalValue.Displacement  \n*Desc:* Create Initial Dynamic  \n *Arg1:* strName (String)  \n *Arg2:* iType (Integer)  \n *Arg3:* vecInit (Vector)  \n *Arg4:* bSelNode (Boolean)  \n *Arg5:* crNodeSet (Cursor)  \n *Arg6:* crTable (Cursor)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InitialNodalValue.Velocity": {
    "prefix": "Velocity",
    "text": "*Name:* BoundaryConditions.InitialNodalValue.Velocity  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* stData (ST_DATA)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "BoundaryConditions.InitialNodalValue.RotationAngle": {
    "prefix": "RotationAngle",
    "text": "*Name:* BoundaryConditions.InitialNodalValue.RotationAngle  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* stData (ST_DATA)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Pretension.General": {
    "prefix": "General",
    "text": "*Name:* Connections.Pretension.General  \n*Desc:* Pretension general  \n *Arg1:* strName (String)  \n *Arg2:* iDir (Integer)  \n *Arg3:* dValue (Double)  \n *Arg4:* bFixLength (Boolean)  \n *Arg5:* crTable (Cursor)  \n *Arg6:* crCoord (Cursor)  \n *Arg7:* iLocalUnit (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Pretension.Abaqus": {
    "prefix": "Abaqus",
    "text": "*Name:* Connections.Pretension.Abaqus  \n*Desc:* Create Pretension Abaqus  \n *Arg1:* strName (String)  \n *Arg2:* bFixedLenght (Boolean)  \n *Arg3:* crTable (Cursor)  \n *Arg4:* dValue (Double)  \n *Arg5:* iLocalUnit (Integer)  \n *Arg6:* strNormal (String)  \n *Arg7:* dlNodePos (Double List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Pretension.Advc": {
    "prefix": "Advc",
    "text": "*Name:* Connections.Pretension.Advc  \n*Desc:* Create ADVC pretension  \n *Arg1:* strName (String)  \n *Arg2:* bFixedLength (Boolean)  \n *Arg3:* crEnforcedVelocity (Cursor)  \n *Arg4:* dDvalue (Double)  \n *Arg5:* iDirUpdateType (Integer)  \n *Arg6:* dlVnormal (Double List)  \n *Arg7:* dlCtrolNodePos (Double List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MassElements": {
    "prefix": "MassElements",
    "text": "*Name:* Connections.MassElements  \n*Desc:* Connection new mass  \n *Arg1:* strName (String)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* dMass (Double)  \n *Arg4:* iDof (Integer)  \n *Arg5:* bDesigner (Boolean)  \n *Arg6:* crCoordinate (Cursor)  \n *Arg7:* dOffset0 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.BarBeam": {
    "prefix": "BarBeam",
    "text": "*Name:* Connections.BarBeam  \n*Desc:* create Connections Bar or Beam  \n *Arg1:* strName (String)  \n *Arg2:* iEType (Integer)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* crProp (Cursor)  \n *Arg5:* dlOrient (Double List)  \n *Arg6:* crlMasterTarget (Cursor List)  \n *Arg7:* crlSlaveTarget (Cursor List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.GapsDetail": {
    "prefix": "GapsDetail",
    "text": "*Name:* Connections.GapsDetail  \n*Desc:* Unknown Description  \n *Arg1:* crlMaster (Cursor List)  \n *Arg2:* crlSlave (Cursor List)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iOriMode (Integer)  \n *Arg5:* crCoord (Cursor)  \n *Arg6:* strName (String)  \n *Arg7:* dU0 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Plot": {
    "prefix": "Plot",
    "text": "*Name:* Connections.Plot  \n*Desc:* Create 1D plot connection  \n *Arg1:* strName (String)  \n *Arg2:* iPID (Integer)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.CreateConnConm": {
    "prefix": "CreateConnConm",
    "text": "*Name:* Connections.CreateConnConm  \n*Desc:*   \n *Arg1:* strName (String)  \n *Arg2:* iEType (Integer)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iCoordSys (Integer)  \n *Arg5:* iConmId (Integer)  \n *Arg6:* crMatCoord (Cursor)  \n *Arg7:* dMass (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* listRbe3TermConnection (RBE3TERM_CONNECTION List)  \n *Arg5:* iTypeRBE3 (Integer)  \n *Arg6:* strName (String)  \n *Arg7:* crCoordSys (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidWall": {
    "prefix": "RigidWall",
    "text": "*Name:* Connections.RigidWall  \n*Desc:*   \n *Arg1:* strName (String)  \n *Arg2:* iObject (Integer)  \n *Arg3:* iType (Integer)  \n *Arg4:* iMotion (Integer)  \n *Arg5:* iFriction (Integer)  \n *Arg6:* iOrtho (Integer)  \n *Arg7:* iForces (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Connector": {
    "prefix": "Connector",
    "text": "*Name:* Connections.Connector  \n*Desc:* create Connector  \n *Arg1:* strName (String)  \n *Arg2:* iMethod (Integer)  \n *Arg3:* iConnectType (Integer)  \n *Arg4:* iRefNode (Integer)  \n *Arg5:* iElemCs (Integer)  \n *Arg6:* crLocalCS (Cursor)  \n *Arg7:* crlElasticity (Cursor List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.BoltMeshingSplitOnly": {
    "prefix": "BoltMeshingSplitOnly",
    "text": "*Name:* Connections.BoltMeshingSplitOnly  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* iPartcutparamImethod (Integer)  \n *Arg3:* dPartcutparamDoffset (Double)  \n *Arg4:* iPartcutparamBshareface (Integer)  \n *Arg5:* iPartcutparamBseparateface (Integer)  \n *Arg6:* iPartcutparamBsplitonly (Integer)  \n *Arg7:* iPartcutparamBmakesectionface (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.BoltMeshingNotSplitOnly": {
    "prefix": "BoltMeshingNotSplitOnly",
    "text": "*Name:* Connections.BoltMeshingNotSplitOnly  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* iPartcutparamImethod (Integer)  \n *Arg3:* dPartcutparamDoffset (Double)  \n *Arg4:* iPartcutparamBshareface (Integer)  \n *Arg5:* iPartcutparamBseparateface (Integer)  \n *Arg6:* iPartcutparamBsplitonly (Integer)  \n *Arg7:* iPartcutparamBmakesectionface (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.BoltConnections.Edge.TypeC": {
    "prefix": "TypeC",
    "text": "*Name:* Connections.BoltConnections.Edge.TypeC  \n*Desc:* create bolt connections by TypeC edge.  \n *Arg1:* crlEdgeCur1 (Cursor List)  \n *Arg2:* crlEdgeCur2 (Cursor List)  \n *Arg3:* strRbeName (String)  \n *Arg4:* dPlaneTol (Double)  \n *Arg5:* dMaxBoltHeight (Double)  \n *Arg6:* iConnectionType (Integer)  \n *Arg7:* iCoincidentNodes (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.BoltConnections.Edge.TypeB": {
    "prefix": "TypeB",
    "text": "*Name:* Connections.BoltConnections.Edge.TypeB  \n*Desc:*   \n *Arg1:* crlEdgeCur1 (Cursor List)  \n *Arg2:* crlEdgeCur2 (Cursor List)  \n *Arg3:* strRbeName (String)  \n *Arg4:* strBarName (String)  \n *Arg5:* iShaftType (Integer)  \n *Arg6:* crCurBarProperty (Cursor)  \n *Arg7:* dPlaneTol (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.BoltConnections.Edge.TypeD": {
    "prefix": "TypeD",
    "text": "*Name:* Connections.BoltConnections.Edge.TypeD  \n*Desc:* create bolt connection typeD  \n *Arg1:* crlEdgeCur1 (Cursor List)  \n *Arg2:* crlEdgeCur2 (Cursor List)  \n *Arg3:* strMpcName (String)  \n *Arg4:* dConnRadius (Double)  \n *Arg5:* dPlaneTol (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.BoltConnections.Edge.TypeA": {
    "prefix": "TypeA",
    "text": "*Name:* Connections.BoltConnections.Edge.TypeA  \n*Desc:* Create Lbc TypeA Bolt Edge method  \n *Arg1:* crlEdgeCur1 (Cursor List)  \n *Arg2:* crlEdgeCur2 (Cursor List)  \n *Arg3:* strRbeName (String)  \n *Arg4:* strBarName (String)  \n *Arg5:* iShaftType (Integer)  \n *Arg6:* crCurBarProperty (Cursor)  \n *Arg7:* dPlaneTol (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.BoltConnections.Face.TypeC": {
    "prefix": "TypeC",
    "text": "*Name:* Connections.BoltConnections.Face.TypeC  \n*Desc:* Create Lbc TypeC Bolt Face method  \n *Arg1:* crlFaceCur1 (Cursor List)  \n *Arg2:* crlFaceCur2 (Cursor List)  \n *Arg3:* strRbeName (String)  \n *Arg4:* dPlaneTol (Double)  \n *Arg5:* dMaxBoltHeight (Double)  \n *Arg6:* dMaxDiameter (Double)  \n *Arg7:* dMinDiameter (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.BoltConnections.Face.TypeB": {
    "prefix": "TypeB",
    "text": "*Name:* Connections.BoltConnections.Face.TypeB  \n*Desc:* Create Lbc TypeB Bolt Face method  \n *Arg1:* crlFaceCur1 (Cursor List)  \n *Arg2:* crlFaceCur2 (Cursor List)  \n *Arg3:* strRbeName (String)  \n *Arg4:* strBarName (String)  \n *Arg5:* iShaftType (Integer)  \n *Arg6:* crCurBarProperty (Cursor)  \n *Arg7:* dPlaneTol (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.BoltConnections.Face.TypeA": {
    "prefix": "TypeA",
    "text": "*Name:* Connections.BoltConnections.Face.TypeA  \n*Desc:*   \n *Arg1:* crlFaceCur1 (Cursor List)  \n *Arg2:* crlFaceCur2 (Cursor List)  \n *Arg3:* strRbeName (String)  \n *Arg4:* strBarName (String)  \n *Arg5:* iShaftType (Integer)  \n *Arg6:* crCurBarProperty (Cursor)  \n *Arg7:* dPlaneTol (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.Abaqus.ContactTable": {
    "prefix": "ContactTable",
    "text": "*Name:* Connections.Contacts.Abaqus.ContactTable  \n*Desc:* Create LBC contact abaqus manual face  \n *Arg1:* strName (String)  \n *Arg2:* iContactMethod (Integer)  \n *Arg3:* iContactType (Integer)  \n *Arg4:* iAlg (Integer)  \n *Arg5:* dAdjustVal (Double)  \n *Arg6:* dExtensionZone (Double)  \n *Arg7:* dMaxPenetration (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.Abaqus.ManualGroup": {
    "prefix": "ManualGroup",
    "text": "*Name:* Connections.Contacts.Abaqus.ManualGroup  \n*Desc:* Create LBC contact abaqus manual group  \n *Arg1:* strName (String)  \n *Arg2:* iContactMethod (Integer)  \n *Arg3:* iContactType (Integer)  \n *Arg4:* iAlg (Integer)  \n *Arg5:* dAdjustVal (Double)  \n *Arg6:* dExtensionZone (Double)  \n *Arg7:* dMaxPenetration (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.Abaqus.ManualFace": {
    "prefix": "ManualFace",
    "text": "*Name:* Connections.Contacts.Abaqus.ManualFace  \n*Desc:* Create LBC contact abaqus manual face  \n *Arg1:* strName (String)  \n *Arg2:* iContactMethod (Integer)  \n *Arg3:* iContactType (Integer)  \n *Arg4:* iAlg (Integer)  \n *Arg5:* dAdjustVal (Double)  \n *Arg6:* dExtensionZone (Double)  \n *Arg7:* dMaxPenetration (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.Abaqus.ContactGroupByMatrix": {
    "prefix": "ContactGroupByMatrix",
    "text": "*Name:* Connections.Contacts.Abaqus.ContactGroupByMatrix  \n*Desc:* Create LBC contact abaqus group by matrix  \n *Arg1:* strName (String)  \n *Arg2:* iContactMethod (Integer)  \n *Arg3:* iContactType (Integer)  \n *Arg4:* iAlg (Integer)  \n *Arg5:* dAdjustVal (Double)  \n *Arg6:* dExtensionZone (Double)  \n *Arg7:* dMaxPenetration (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.Abaqus.ContactShareFace": {
    "prefix": "ContactShareFace",
    "text": "*Name:* Connections.Contacts.Abaqus.ContactShareFace  \n*Desc:* Create LBC contact abaqus manual group  \n *Arg1:* strName (String)  \n *Arg2:* iContactMethod (Integer)  \n *Arg3:* iContactType (Integer)  \n *Arg4:* iAlg (Integer)  \n *Arg5:* dAdjustVal (Double)  \n *Arg6:* dExtensionZone (Double)  \n *Arg7:* dMaxPenetration (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.ADVC.ContactClearance": {
    "prefix": "ContactClearance",
    "text": "*Name:* Connections.Contacts.ADVC.ContactClearance  \n*Desc:* contact clearance for ADVC contact  \n *Arg1:* strName (String)  \n *Arg2:* dClearanceVal (Double)  \n *Arg3:* iLocalUnit (Integer)  \n *Arg4:* iSolverType (Integer)  \n *Arg5:* crlTarget (Cursor List)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.ADVC.ManualGroup": {
    "prefix": "ManualGroup",
    "text": "*Name:* Connections.Contacts.ADVC.ManualGroup  \n*Desc:* create ADVC contact Manual Group  \n *Arg1:* strName (String)  \n *Arg2:* iContactType (Integer)  \n *Arg3:* iSlidingType (Integer)  \n *Arg4:* iInitialState (Integer)  \n *Arg5:* dInitialStateTol (Double)  \n *Arg6:* dKineticFrictionCoef (Double)  \n *Arg7:* dExponentialCoef (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.ADVC.ManualFace": {
    "prefix": "ManualFace",
    "text": "*Name:* Connections.Contacts.ADVC.ManualFace  \n*Desc:* create ADVC contact by manual face  \n *Arg1:* crlFaceMaster (Cursor List)  \n *Arg2:* crlFaceSlave (Cursor List)  \n *Arg3:* strName (String)  \n *Arg4:* iContactType (Integer)  \n *Arg5:* iSlidingType (Integer)  \n *Arg6:* iInitialState (Integer)  \n *Arg7:* dInitialStateTol (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.ADVC.ContactShareFace": {
    "prefix": "ContactShareFace",
    "text": "*Name:* Connections.Contacts.ADVC.ContactShareFace  \n*Desc:* create ADVC Contact Share Face  \n *Arg1:* crlShareFace (Cursor List)  \n *Arg2:* strName (String)  \n *Arg3:* iContactType (Integer)  \n *Arg4:* iSlidingType (Integer)  \n *Arg5:* iInitialState (Integer)  \n *Arg6:* dInitialStateTol (Double)  \n *Arg7:* dKineticFrictionCoef (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.ADVC.ContactTable": {
    "prefix": "ContactTable",
    "text": "*Name:* Connections.Contacts.ADVC.ContactTable  \n*Desc:* create ADVC Contact Table  \n *Arg1:* strName (String)  \n *Arg2:* iContactType (Integer)  \n *Arg3:* iSlidingType (Integer)  \n *Arg4:* iInitialState (Integer)  \n *Arg5:* dInitialStateTol (Double)  \n *Arg6:* dKineticFrictionCoef (Double)  \n *Arg7:* dExponentialCoef (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.ADVC.ContactGroupByMatrix": {
    "prefix": "ContactGroupByMatrix",
    "text": "*Name:* Connections.Contacts.ADVC.ContactGroupByMatrix  \n*Desc:* create ADVC contact Group By Matrix  \n *Arg1:* strName (String)  \n *Arg2:* iContactType (Integer)  \n *Arg3:* iSlidingType (Integer)  \n *Arg4:* iInitialState (Integer)  \n *Arg5:* dInitialStateTol (Double)  \n *Arg6:* dKineticFrictionCoef (Double)  \n *Arg7:* dExponentialCoef (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.Ansys.ManualGroup": {
    "prefix": "ManualGroup",
    "text": "*Name:* Connections.Contacts.Ansys.ManualGroup  \n*Desc:* create contact ansys Manual Group  \n *Arg1:* strName (String)  \n *Arg2:* iMethod (Integer)  \n *Arg3:* iType (Integer)  \n *Arg4:* iContactAlgorithm (Integer)  \n *Arg5:* ansysContact (ANSYS_CONTACT)  \n *Arg6:* crplTarget (Cursor Pair List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.Ansys.ManualFace": {
    "prefix": "ManualFace",
    "text": "*Name:* Connections.Contacts.Ansys.ManualFace  \n*Desc:* create contacts of Ansys Manual Face  \n *Arg1:* crlFaceMaster (Cursor List)  \n *Arg2:* crlFaceSlave (Cursor List)  \n *Arg3:* strName (String)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iType (Integer)  \n *Arg6:* iContactAlgorithm (Integer)  \n *Arg7:* ansysContact (ANSYS_CONTACT)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.Ansys.ContactGroupByMatrix": {
    "prefix": "ContactGroupByMatrix",
    "text": "*Name:* Connections.Contacts.Ansys.ContactGroupByMatrix  \n*Desc:* create contact ansys Group By Matrix  \n *Arg1:* strName (String)  \n *Arg2:* iMethod (Integer)  \n *Arg3:* iType (Integer)  \n *Arg4:* iContactAlgorithm (Integer)  \n *Arg5:* ansysContact (ANSYS_CONTACT)  \n *Arg6:* crplTarget (Cursor Pair List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.Ansys.ContactShareFace": {
    "prefix": "ContactShareFace",
    "text": "*Name:* Connections.Contacts.Ansys.ContactShareFace  \n*Desc:* create contact ansys Share Face  \n *Arg1:* crlShareFace (Cursor List)  \n *Arg2:* strName (String)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iType (Integer)  \n *Arg5:* iContactAlgorithm (Integer)  \n *Arg6:* ansysContact (ANSYS_CONTACT)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.Ansys.ContactTable": {
    "prefix": "ContactTable",
    "text": "*Name:* Connections.Contacts.Ansys.ContactTable  \n*Desc:* create contact ansys Contact Table  \n *Arg1:* strName (String)  \n *Arg2:* iMethod (Integer)  \n *Arg3:* iType (Integer)  \n *Arg4:* iContactAlgorithm (Integer)  \n *Arg5:* ansysContact (ANSYS_CONTACT)  \n *Arg6:* crplTarget (Cursor Pair List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.MSCNastran.ManualGroup": {
    "prefix": "ManualGroup",
    "text": "*Name:* Connections.Contacts.MSCNastran.ManualGroup  \n*Desc:* create contacts of MSC Nastran  \n *Arg1:* strName (String)  \n *Arg2:* nastranContact (NASTRAN_CONTACT)  \n *Arg3:* crplTarget (Cursor Pair List)  \n *Arg4:* crEdit (Cursor)  \n *Arg5:* iColor (Integer)  \n *Arg6:* iMethod (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.MSCNastran.ContactGroupByMatrix": {
    "prefix": "ContactGroupByMatrix",
    "text": "*Name:* Connections.Contacts.MSCNastran.ContactGroupByMatrix  \n*Desc:* create contacts of MSC Nastran Contact Group By Matrix  \n *Arg1:* strName (String)  \n *Arg2:* nastranContact (NASTRAN_CONTACT)  \n *Arg3:* crplTarget (Cursor Pair List)  \n *Arg4:* crEdit (Cursor)  \n *Arg5:* iColor (Integer)  \n *Arg6:* iMethod (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.MSCNastran.ManualFace": {
    "prefix": "ManualFace",
    "text": "*Name:* Connections.Contacts.MSCNastran.ManualFace  \n*Desc:* create contacts of MSC Nastran Manual Face  \n *Arg1:* crlFaceMaster (Cursor List)  \n *Arg2:* crlFaceSlave (Cursor List)  \n *Arg3:* strName (String)  \n *Arg4:* nastranContact (NASTRAN_CONTACT)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* iColor (Integer)  \n *Arg7:* iMethod (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.MSCNastran.ContactShareFace": {
    "prefix": "ContactShareFace",
    "text": "*Name:* Connections.Contacts.MSCNastran.ContactShareFace  \n*Desc:* create contacts of MSC Nastran Contact Share Face  \n *Arg1:* crlShareFace (Cursor List)  \n *Arg2:* strName (String)  \n *Arg3:* nastranContact (NASTRAN_CONTACT)  \n *Arg4:* crEdit (Cursor)  \n *Arg5:* iColor (Integer)  \n *Arg6:* iMethod (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.MSCNastran.ContactTable": {
    "prefix": "ContactTable",
    "text": "*Name:* Connections.Contacts.MSCNastran.ContactTable  \n*Desc:* create contacts of MSC Nastran Contact Table  \n *Arg1:* strName (String)  \n *Arg2:* nastranContact (NASTRAN_CONTACT)  \n *Arg3:* crplTarget (Cursor Pair List)  \n *Arg4:* crEdit (Cursor)  \n *Arg5:* iColor (Integer)  \n *Arg6:* iMethod (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.NXNastran.ManualFace": {
    "prefix": "ManualFace",
    "text": "*Name:* Connections.Contacts.NXNastran.ManualFace  \n*Desc:* Create Contact NXNastran Manual Face  \n *Arg1:* crlFaceMaster (Cursor List)  \n *Arg2:* crlFaceSlave (Cursor List)  \n *Arg3:* strName (String)  \n *Arg4:* iContactType (Integer)  \n *Arg5:* iContactAlg (Integer)  \n *Arg6:* dNorPenFactor (Double)  \n *Arg7:* dTanPenFactor (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.NXNastran.ContactShareFace": {
    "prefix": "ContactShareFace",
    "text": "*Name:* Connections.Contacts.NXNastran.ContactShareFace  \n*Desc:* Create Contact NXNastran Contact Share Face  \n *Arg1:* crlShareFace (Cursor List)  \n *Arg2:* strName (String)  \n *Arg3:* iContactType (Integer)  \n *Arg4:* iContactAlg (Integer)  \n *Arg5:* dNorPenFactor (Double)  \n *Arg6:* dTanPenFactor (Double)  \n *Arg7:* dForceConTol (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.NXNastran.ContactTable": {
    "prefix": "ContactTable",
    "text": "*Name:* Connections.Contacts.NXNastran.ContactTable  \n*Desc:* Create Contact NXNastran Contact Table  \n *Arg1:* strName (String)  \n *Arg2:* iType (Integer)  \n *Arg3:* iAlg (Integer)  \n *Arg4:* dNorPenFactor (Double)  \n *Arg5:* dTanPenFactor (Double)  \n *Arg6:* dForceConTol (Double)  \n *Arg7:* dMaxForceIter (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.NXNastran.ManualGroup": {
    "prefix": "ManualGroup",
    "text": "*Name:* Connections.Contacts.NXNastran.ManualGroup  \n*Desc:* Create Contact NXNastran Manual Group  \n *Arg1:* crFaceMaster (Cursor)  \n *Arg2:* crFaceSlave (Cursor)  \n *Arg3:* strName (String)  \n *Arg4:* iContactType (Integer)  \n *Arg5:* iContactAlg (Integer)  \n *Arg6:* dNorPenFactor (Double)  \n *Arg7:* dTanPenFactor (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.NXNastran.ContactGroupByMatrix": {
    "prefix": "ContactGroupByMatrix",
    "text": "*Name:* Connections.Contacts.NXNastran.ContactGroupByMatrix  \n*Desc:* Create Contact NXNastran Contact Group By Matrix  \n *Arg1:* crFaceMaster (Cursor)  \n *Arg2:* crFaceSlave (Cursor)  \n *Arg3:* strName (String)  \n *Arg4:* iContactType (Integer)  \n *Arg5:* iContactAlg (Integer)  \n *Arg6:* dNorPenFactor (Double)  \n *Arg7:* dTanPenFactor (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.TSSolver.ManualFace": {
    "prefix": "ManualFace",
    "text": "*Name:* Connections.Contacts.TSSolver.ManualFace  \n*Desc:* Create TSSolver Contact  \n *Arg1:* strName (String)  \n *Arg2:* nastranContact (NASTRAN_CONTACT)  \n *Arg3:* crplTarget (Cursor Pair List)  \n *Arg4:* crEdit (Cursor)  \n *Arg5:* iColor (Integer)  \n *Arg6:* iMethod (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.TSSolver.Auto": {
    "prefix": "Auto",
    "text": "*Name:* Connections.Contacts.TSSolver.Auto  \n*Desc:* find contact  \n *Arg1:* strlNames (String List)  \n *Arg2:* crllMasterFaceTargets (Cursor List List)  \n *Arg3:* crllSlaveFaceTargets (Cursor List List)  \n *Arg4:* crlContactTypes (Cursor List)  \n *Arg5:* dlInterferenceClosures (Double List)  \n *Arg6:* dlFrictionCoefficients (Double List)  \n *Arg7:* blInitialAdjustments (Boolean List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.TSSolver.ManualGroup": {
    "prefix": "ManualGroup",
    "text": "*Name:* Connections.Contacts.TSSolver.ManualGroup  \n*Desc:* Create TSSolver Contact  \n *Arg1:* strName (String)  \n *Arg2:* tssolverContact (TSSOLVER_CONTACT)  \n *Arg3:* crplTarget (Cursor Pair List)  \n *Arg4:* crEdit (Cursor)  \n *Arg5:* iColor (Integer)  \n *Arg6:* iMethod (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.TSSS.ManualFace": {
    "prefix": "ManualFace",
    "text": "*Name:* Connections.Contacts.TSSS.ManualFace  \n*Desc:* Create Contact TSSS Manual Face  \n *Arg1:* crlFaceMaster (Cursor List)  \n *Arg2:* crlFaceSlave (Cursor List)  \n *Arg3:* strName (String)  \n *Arg4:* nastranContact (NASTRAN_CONTACT)  \n *Arg5:* crEdit (Cursor)  \n *Arg6:* iColor (Integer)  \n *Arg7:* iMethod (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.TSSS.ManualGroup": {
    "prefix": "ManualGroup",
    "text": "*Name:* Connections.Contacts.TSSS.ManualGroup  \n*Desc:* Create Contact TSSS Manual FaceGroup  \n *Arg1:* strName (String)  \n *Arg2:* tssolverContact (TSSOLVER_CONTACT)  \n *Arg3:* crplTarget (Cursor Pair List)  \n *Arg4:* crEdit (Cursor)  \n *Arg5:* iColor (Integer)  \n *Arg6:* iMethod (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.TSSS.ContactTable": {
    "prefix": "ContactTable",
    "text": "*Name:* Connections.Contacts.TSSS.ContactTable  \n*Desc:* Create Contact TSSS Manual FaceGroup  \n *Arg1:* strName (String)  \n *Arg2:* nastranContact (NASTRAN_CONTACT)  \n *Arg3:* crplTarget (Cursor Pair List)  \n *Arg4:* crEdit (Cursor)  \n *Arg5:* iColor (Integer)  \n *Arg6:* iMethod (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.CheckPattern": {
    "prefix": "CheckPattern",
    "text": "*Name:* Connections.Contacts.CheckPattern  \n*Desc:* check contact Pattern  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* bShowMismatch (Boolean)  \n *Arg3:* bShowMatch (Boolean)  \n *Arg4:* dTol (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.NXNastranGeneral": {
    "prefix": "NXNastranGeneral",
    "text": "*Name:* Connections.Contacts.NXNastranGeneral  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* iPiType (Integer)  \n *Arg3:* iPiAlg (Integer)  \n *Arg4:* dPdNorPenFactor (Double)  \n *Arg5:* dPdTanPenFactor (Double)  \n *Arg6:* dPdForceConTol (Double)  \n *Arg7:* dPdMaxForceIter (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Contacts.ExportCheckReport": {
    "prefix": "ExportCheckReport",
    "text": "*Name:* Connections.Contacts.ExportCheckReport  \n*Desc:* Unknown Description  \n *Arg1:* strFullPath (String)  \n *Arg2:* dZoomFactor (Double)  \n *Arg3:* iFitBy (Integer)  \n *Arg4:* iListBy (Integer)  \n *Arg5:* iListOrder (Integer)  \n *Arg6:* iFormat (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Gaps.TwoNodes": {
    "prefix": "TwoNodes",
    "text": "*Name:* Connections.Gaps.TwoNodes  \n*Desc:* create gap connection  \n *Arg1:* crlMaster (Cursor List)  \n *Arg2:* crlSlave (Cursor List)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iOriMode (Integer)  \n *Arg5:* crCoord (Cursor)  \n *Arg6:* strName (String)  \n *Arg7:* dU0 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Gaps.TwoEdges": {
    "prefix": "TwoEdges",
    "text": "*Name:* Connections.Gaps.TwoEdges  \n*Desc:* create gap connection  \n *Arg1:* crlMaster (Cursor List)  \n *Arg2:* crlSlave (Cursor List)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iOriMode (Integer)  \n *Arg5:* crCoord (Cursor)  \n *Arg6:* strName (String)  \n *Arg7:* dU0 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.Gaps.TwoFaces": {
    "prefix": "TwoFaces",
    "text": "*Name:* Connections.Gaps.TwoFaces  \n*Desc:* create gap connection  \n *Arg1:* crlMaster (Cursor List)  \n *Arg2:* crlSlave (Cursor List)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iOriMode (Integer)  \n *Arg5:* crCoord (Cursor)  \n *Arg6:* strName (String)  \n *Arg7:* dU0 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.Equation.MultiNodes": {
    "prefix": "MultiNodes",
    "text": "*Name:* Connections.MPC.Equation.MultiNodes  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.Equation.TwoFace": {
    "prefix": "TwoFace",
    "text": "*Name:* Connections.MPC.Equation.TwoFace  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.Equation.SemiAuto": {
    "prefix": "SemiAuto",
    "text": "*Name:* Connections.MPC.Equation.SemiAuto  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.General.NodeToNode": {
    "prefix": "NodeToNode",
    "text": "*Name:* Connections.MPC.General.NodeToNode  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.General.NodeToEdges": {
    "prefix": "NodeToEdges",
    "text": "*Name:* Connections.MPC.General.NodeToEdges  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.General.NodeToFaces": {
    "prefix": "NodeToFaces",
    "text": "*Name:* Connections.MPC.General.NodeToFaces  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.General.TwoEdges": {
    "prefix": "TwoEdges",
    "text": "*Name:* Connections.MPC.General.TwoEdges  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.General.FacesToFaces": {
    "prefix": "FacesToFaces",
    "text": "*Name:* Connections.MPC.General.FacesToFaces  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.General.NodesToNodes": {
    "prefix": "NodesToNodes",
    "text": "*Name:* Connections.MPC.General.NodesToNodes  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.General.TwoFaces": {
    "prefix": "TwoFaces",
    "text": "*Name:* Connections.MPC.General.TwoFaces  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.General.NodeToAny": {
    "prefix": "NodeToAny",
    "text": "*Name:* Connections.MPC.General.NodeToAny  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.MPC.General.NodesWithTolerance": {
    "prefix": "NodesWithTolerance",
    "text": "*Name:* Connections.MPC.General.NodesWithTolerance  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crlMaster (Cursor List)  \n *Arg3:* crlSlave (Cursor List)  \n *Arg4:* listMpcConnection (MPC_CONNECTION List)  \n *Arg5:* dSearchTol (Double)  \n *Arg6:* dValue (Double)  \n *Arg7:* iMPCType (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBar.OneToOne": {
    "prefix": "OneToOne",
    "text": "*Name:* Connections.RigidElements.RBar.OneToOne  \n*Desc:* create RBar  \n *Arg1:* strName (String)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iUlDOFs (Integer)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBar.OneToMany": {
    "prefix": "OneToMany",
    "text": "*Name:* Connections.RigidElements.RBar.OneToMany  \n*Desc:* create RBar  \n *Arg1:* strName (String)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iUlDOFs (Integer)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBar.OneToOneNodesWithTolerance": {
    "prefix": "OneToOneNodesWithTolerance",
    "text": "*Name:* Connections.RigidElements.RBar.OneToOneNodesWithTolerance  \n*Desc:* create RBar  \n *Arg1:* strName (String)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iUlDOFs (Integer)  \n *Arg6:* dTol (Double)  \n *Arg7:* crCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBE2.OneToMany": {
    "prefix": "OneToMany",
    "text": "*Name:* Connections.RigidElements.RBE2.OneToMany  \n*Desc:* create RBE2  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* iEType (Integer)  \n *Arg5:* strName (String)  \n *Arg6:* crCoordSys (Cursor)  \n *Arg7:* dTolerance (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBE2.OneToOne": {
    "prefix": "OneToOne",
    "text": "*Name:* Connections.RigidElements.RBE2.OneToOne  \n*Desc:* create RBE2  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* iEType (Integer)  \n *Arg5:* strName (String)  \n *Arg6:* crCoordSys (Cursor)  \n *Arg7:* dTolerance (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBE2.OneToOneNodesWithTolerance": {
    "prefix": "OneToOneNodesWithTolerance",
    "text": "*Name:* Connections.RigidElements.RBE2.OneToOneNodesWithTolerance  \n*Desc:* create RBE2  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* iEType (Integer)  \n *Arg5:* strName (String)  \n *Arg6:* crCoordSys (Cursor)  \n *Arg7:* dTolerance (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBE2.ToCenter": {
    "prefix": "ToCenter",
    "text": "*Name:* Connections.RigidElements.RBE2.ToCenter  \n*Desc:* create RBE2  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* iEType (Integer)  \n *Arg5:* strName (String)  \n *Arg6:* crCoordSys (Cursor)  \n *Arg7:* dTolerance (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBE2.ToCircleCenter": {
    "prefix": "ToCircleCenter",
    "text": "*Name:* Connections.RigidElements.RBE2.ToCircleCenter  \n*Desc:* create RBE2  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* iEType (Integer)  \n *Arg5:* strName (String)  \n *Arg6:* crCoordSys (Cursor)  \n *Arg7:* dTolerance (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBE3.OneToMany": {
    "prefix": "OneToMany",
    "text": "*Name:* Connections.RigidElements.RBE3.OneToMany  \n*Desc:* Create RBE3  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* listRbe3TermConnection (RBE3TERM_CONNECTION List)  \n *Arg5:* iTypeRBE3 (Integer)  \n *Arg6:* strName (String)  \n *Arg7:* crCoordSys (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBE3.OneToOne": {
    "prefix": "OneToOne",
    "text": "*Name:* Connections.RigidElements.RBE3.OneToOne  \n*Desc:* Create RBE3  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* listRbe3TermConnection (RBE3TERM_CONNECTION List)  \n *Arg5:* iTypeRBE3 (Integer)  \n *Arg6:* strName (String)  \n *Arg7:* crCoordSys (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBE3.ToCenter": {
    "prefix": "ToCenter",
    "text": "*Name:* Connections.RigidElements.RBE3.ToCenter  \n*Desc:* Create RBE3  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* listRbe3TermConnection (RBE3TERM_CONNECTION List)  \n *Arg5:* iTypeRBE3 (Integer)  \n *Arg6:* strName (String)  \n *Arg7:* crCoordSys (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBE3.ToCircleCenter": {
    "prefix": "ToCircleCenter",
    "text": "*Name:* Connections.RigidElements.RBE3.ToCircleCenter  \n*Desc:* Create RBE3  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* listRbe3TermConnection (RBE3TERM_CONNECTION List)  \n *Arg5:* iTypeRBE3 (Integer)  \n *Arg6:* strName (String)  \n *Arg7:* crCoordSys (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.RigidElements.RBarGeneral": {
    "prefix": "RBarGeneral",
    "text": "*Name:* Connections.RigidElements.RBarGeneral  \n*Desc:* Unknown Description  \n *Arg1:* rbarConnection (RBAR_CONNECTION)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* iUlDOFs (Integer)  \n *Arg5:* dTol (Double)  \n *Arg6:* crCoord (Cursor)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* iEType (Integer)  \n *Arg5:* strName (String)  \n *Arg6:* crCoordSys (Cursor)  \n *Arg7:* dTolerance (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlMasterTarget (Cursor List)  \n *Arg3:* crlSlaveTarget (Cursor List)  \n *Arg4:* listRbe3TermConnection (RBE3TERM_CONNECTION List)  \n *Arg5:* iTypeRBE3 (Integer)  \n *Arg6:* strName (String)  \n *Arg7:* crCoordSys (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Create Damper Connection  \n *Arg1:* iMethod (Integer)  \n *Arg2:* strName (String)  \n *Arg3:* crlMasterTarget (Cursor List)  \n *Arg4:* crlSlaveTarget (Cursor List)  \n *Arg5:* crCoordSys (Cursor)  \n *Arg6:* iGround (Integer)  \n *Arg7:* dTolerance (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.SpringsDampers.BushGeneral": {
    "prefix": "BushGeneral",
    "text": "*Name:* Connections.SpringsDampers.BushGeneral  \n*Desc:* Unknown Description  \n *Arg1:* iMethod (Integer)  \n *Arg2:* strName (String)  \n *Arg3:* crlMaster (Cursor List)  \n *Arg4:* crlSlave (Cursor List)  \n *Arg5:* crCoord (Cursor)  \n *Arg6:* dTol (Double)  \n *Arg7:* iGround (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.SpringsDampers.Bush.TwoNodes": {
    "prefix": "TwoNodes",
    "text": "*Name:* Connections.SpringsDampers.Bush.TwoNodes  \n*Desc:* Create bush connection  \n *Arg1:* iMethod (Integer)  \n *Arg2:* strName (String)  \n *Arg3:* crlMaster (Cursor List)  \n *Arg4:* crlSlave (Cursor List)  \n *Arg5:* crCoord (Cursor)  \n *Arg6:* dTol (Double)  \n *Arg7:* iGround (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.SpringsDampers.Bush.AnyEntities": {
    "prefix": "AnyEntities",
    "text": "*Name:* Connections.SpringsDampers.Bush.AnyEntities  \n*Desc:* Create bush connection  \n *Arg1:* iMethod (Integer)  \n *Arg2:* strName (String)  \n *Arg3:* crlMaster (Cursor List)  \n *Arg4:* crlSlave (Cursor List)  \n *Arg5:* crCoord (Cursor)  \n *Arg6:* dTol (Double)  \n *Arg7:* iGround (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.SpringsDampers.Bush.OnetoOne": {
    "prefix": "OnetoOne",
    "text": "*Name:* Connections.SpringsDampers.Bush.OnetoOne  \n*Desc:* Create bush connection  \n *Arg1:* iMethod (Integer)  \n *Arg2:* strName (String)  \n *Arg3:* crlMaster (Cursor List)  \n *Arg4:* crlSlave (Cursor List)  \n *Arg5:* crCoord (Cursor)  \n *Arg6:* dTol (Double)  \n *Arg7:* iGround (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.SpringsDampers.Spring.GroundedSpring": {
    "prefix": "GroundedSpring",
    "text": "*Name:* Connections.SpringsDampers.Spring.GroundedSpring  \n*Desc:* Grounded Spring connection  \n *Arg1:* iMethod (Integer)  \n *Arg2:* strName (String)  \n *Arg3:* crlMasterTarget (Cursor List)  \n *Arg4:* crlSlaveTarget (Cursor List)  \n *Arg5:* crCoordSys (Cursor)  \n *Arg6:* iSpringType (Integer)  \n *Arg7:* iGround (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.SpringsDampers.Spring.Nodeswithtolerance.sameDoFs": {
    "prefix": "sameDoFs",
    "text": "*Name:* Connections.SpringsDampers.Spring.Nodeswithtolerance.sameDoFs  \n*Desc:* Spring connection Nodes with tolerance same DOFs  \n *Arg1:* iMethod (Integer)  \n *Arg2:* strName (String)  \n *Arg3:* crlMasterTarget (Cursor List)  \n *Arg4:* crlSlaveTarget (Cursor List)  \n *Arg5:* crCoordSys (Cursor)  \n *Arg6:* iSpringType (Integer)  \n *Arg7:* iGround (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.SpringsDampers.Spring.Nodeswithtolerance.differentDoFs": {
    "prefix": "differentDoFs",
    "text": "*Name:* Connections.SpringsDampers.Spring.Nodeswithtolerance.differentDoFs  \n*Desc:* Spring connection Nodes with tolerance different DOFs  \n *Arg1:* iMethod (Integer)  \n *Arg2:* strName (String)  \n *Arg3:* crlMasterTarget (Cursor List)  \n *Arg4:* crlSlaveTarget (Cursor List)  \n *Arg5:* crCoordSys (Cursor)  \n *Arg6:* iSpringType (Integer)  \n *Arg7:* iGround (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.SpringsDampers.Spring.OneToOne.sameDoFs": {
    "prefix": "sameDoFs",
    "text": "*Name:* Connections.SpringsDampers.Spring.OneToOne.sameDoFs  \n*Desc:* Spring connection One to One same DOFs  \n *Arg1:* iMethod (Integer)  \n *Arg2:* strName (String)  \n *Arg3:* crlMasterTarget (Cursor List)  \n *Arg4:* crlSlaveTarget (Cursor List)  \n *Arg5:* crCoordSys (Cursor)  \n *Arg6:* iSpringType (Integer)  \n *Arg7:* iGround (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Connections.SpringsDampers.Spring.OneToOne.differentDoFs": {
    "prefix": "differentDoFs",
    "text": "*Name:* Connections.SpringsDampers.Spring.OneToOne.differentDoFs  \n*Desc:* Spring connection One to One different DOFs  \n *Arg1:* iMethod (Integer)  \n *Arg2:* strName (String)  \n *Arg3:* crlMasterTarget (Cursor List)  \n *Arg4:* crlSlaveTarget (Cursor List)  \n *Arg5:* crCoordSys (Cursor)  \n *Arg6:* iSpringType (Integer)  \n *Arg7:* iGround (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Designer.LBC.TemperatureLoad": {
    "prefix": "TemperatureLoad",
    "text": "*Name:* Designer.LBC.TemperatureLoad  \n*Desc:* create temperature load Desiner  \n *Arg1:* strName (String)  \n *Arg2:* iDnType (Integer)  \n *Arg3:* dFTemp (Double)  \n *Arg4:* strDstrFilePathName (String)  \n *Arg5:* crDcrTable (Cursor)  \n *Arg6:* crlTarget (Cursor List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Designer.Load.Moment": {
    "prefix": "Moment",
    "text": "*Name:* Designer.Load.Moment  \n*Desc:* Create moment  \n *Arg1:* strName (String)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* dlVecMomentXYZ (Double List)  \n *Arg4:* crCoord (Cursor)  \n *Arg5:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Designer.ContactMerge": {
    "prefix": "ContactMerge",
    "text": "*Name:* Designer.ContactMerge  \n*Desc:* Build contact for designer  \n *Arg1:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Designer.Material": {
    "prefix": "Material",
    "text": "*Name:* Designer.Material  \n*Desc:* Unknown Description  \n *Arg1:* strMatName (String)  \n *Arg2:* strPropName (String)  \n *Arg3:* dThickness (Double)  \n *Arg4:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "EngReliability.SubModelBC": {
    "prefix": "SubModelBC",
    "text": "*Name:* EngReliability.SubModelBC  \n*Desc:* create mapping forced displacement  \n *Arg1:* strName (String)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* iPos (Integer)  \n *Arg4:* iViewCp (Integer)  \n *Arg5:* iCp (Integer)  \n *Arg6:* iSrcType (Integer)  \n *Arg7:* iMappedCpIndexArr0 (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:*   \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crlPart (Cursor List)  \n *Arg3:* dLayerWidth (Double)  \n *Arg4:* iLayerNumber (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Bar.TwoNodes": {
    "prefix": "TwoNodes",
    "text": "*Name:* Geometry.Bar.TwoNodes  \n*Desc:* Create Bar Body  \n *Arg1:* strPartName (String)  \n *Arg2:* iMeshCount (Integer)  \n *Arg3:* crStartNode (Cursor)  \n *Arg4:* crEndNode (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Bar.Arc": {
    "prefix": "Arc",
    "text": "*Name:* Geometry.Bar.Arc  \n*Desc:* Create Edge by spline  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* crPart (Cursor)  \n *Arg3:* strBarName (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Bar.Spline": {
    "prefix": "Spline",
    "text": "*Name:* Geometry.Bar.Spline  \n*Desc:* Create Edge by spline  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* crPart (Cursor)  \n *Arg3:* strBarName (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.BodyCut.XXYYOnOnePoint": {
    "prefix": "XXYYOnOnePoint",
    "text": "*Name:* Geometry.BodyCut.XXYYOnOnePoint  \n*Desc:* Cut body by one point  \n *Arg1:* crPart (Cursor)  \n *Arg2:* posCutPos (Position)  \n *Arg3:* iType (Integer)  \n *Arg4:* dOffset (Double)  \n *Arg5:* bSplit (Boolean)  \n *Arg6:* bSectionFace (Boolean)  \n *Arg7:* bShateFace (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.BodyCut.BySurface": {
    "prefix": "BySurface",
    "text": "*Name:* Geometry.BodyCut.BySurface  \n*Desc:* Cut body by surface  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crCutter (Cursor)  \n *Arg3:* bSplitOnly (Boolean)  \n *Arg4:* bMakeSectionFace (Boolean)  \n *Arg5:* bShareFace (Boolean)  \n *Arg6:* bSeparateFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Body Cut by 3 Points  \n *Arg1:* crPart (Cursor)  \n *Arg2:* poslPosition (Position List)  \n *Arg3:* dOffset (Double)  \n *Arg4:* bSplitonly (Boolean)  \n *Arg5:* bMakesectionface (Boolean)  \n *Arg6:* bShareface (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.BreakEntity.StlPart": {
    "prefix": "StlPart",
    "text": "*Name:* Geometry.BreakEntity.StlPart  \n*Desc:* break STL part  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* iMinNoOfFaces (Integer)  \n *Arg3:* iMethod (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.BreakEntity.Face": {
    "prefix": "Face",
    "text": "*Name:* Geometry.BreakEntity.Face  \n*Desc:* break entity for face  \n *Arg1:* crlFace (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.BreakEntity.Edge": {
    "prefix": "Edge",
    "text": "*Name:* Geometry.BreakEntity.Edge  \n*Desc:* Break selected edge  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* crlEdge (Cursor List)  \n *Arg4:* crlNode (Cursor List)  \n *Arg5:* bAutoByAngle (Boolean)  \n *Arg6:* dEdgeAngle (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.BreakEntity.Part": {
    "prefix": "Part",
    "text": "*Name:* Geometry.BreakEntity.Part  \n*Desc:* Separate Part  \n *Arg1:* crlPart (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.DeleteEntity.Part": {
    "prefix": "Part",
    "text": "*Name:* Geometry.DeleteEntity.Part  \n*Desc:* Delete Part  \n *Arg1:* crlPart (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.DeleteEntity.Edge": {
    "prefix": "Edge",
    "text": "*Name:* Geometry.DeleteEntity.Edge  \n*Desc:* Delete Edge  \n *Arg1:* crlEdge (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.DeleteEntity.Vertex": {
    "prefix": "Vertex",
    "text": "*Name:* Geometry.DeleteEntity.Vertex  \n*Desc:* delete vertex  \n *Arg1:* crlVertex (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.DeleteEntity.Face": {
    "prefix": "Face",
    "text": "*Name:* Geometry.DeleteEntity.Face  \n*Desc:* Delete Face  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* bKeepSolid (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.Line": {
    "prefix": "Line",
    "text": "*Name:* Geometry.Edge.Line  \n*Desc:* Imprint line 2 point  \n *Arg1:* poslPositions (Position List)  \n *Arg2:* crlTargetFace (Cursor List)  \n *Arg3:* bBreakFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.Spline": {
    "prefix": "Spline",
    "text": "*Name:* Geometry.Edge.Spline  \n*Desc:* Imprint a Spline on a face  \n *Arg1:* veclAprroxiPositions (Vector List)  \n *Arg2:* crlTargetFace (Cursor List)  \n *Arg3:* bBreakFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.PlanarLine": {
    "prefix": "PlanarLine",
    "text": "*Name:* Geometry.Edge.PlanarLine  \n*Desc:* Imprint Planar Line  \n *Arg1:* veclPosition (Vector List)  \n *Arg2:* crlTargetFace (Cursor List)  \n *Arg3:* crLocalCoord (Cursor)  \n *Arg4:* iType (Integer)  \n *Arg5:* bBreakFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.Circle": {
    "prefix": "Circle",
    "text": "*Name:* Geometry.Edge.Circle  \n*Desc:* Imprint Cirlcle Line S  \n *Arg1:* veclPositions (Vector List)  \n *Arg2:* crlTargetFace (Cursor List)  \n *Arg3:* dInRadius (Double)  \n *Arg4:* dOutRadius (Double)  \n *Arg5:* iNoOfLayer (Integer)  \n *Arg6:* iNoOfDiv (Integer)  \n *Arg7:* bBreakFace (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.PerpendicularLineOfEdge": {
    "prefix": "PerpendicularLineOfEdge",
    "text": "*Name:* Geometry.Edge.PerpendicularLineOfEdge  \n*Desc:* Imprint the perpendicular line of edge  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* dOffset (Double)  \n *Arg4:* bReakFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.ExtendLine": {
    "prefix": "ExtendLine",
    "text": "*Name:* Geometry.Edge.ExtendLine  \n*Desc:* make edge by extend line  \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* iMethod (Integer)  \n *Arg3:* iEnd (Integer)  \n *Arg4:* iNoFittingPoints (Integer)  \n *Arg5:* iDiv (Integer)  \n *Arg6:* iEnableBreakFace (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.ElementEdges": {
    "prefix": "ElementEdges",
    "text": "*Name:* Geometry.Edge.ElementEdges  \n*Desc:* Create Edge by element edges  \n *Arg1:* crplElemEdge (Cursor Pair List)  \n *Arg2:* bBreakEdge (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.Angle": {
    "prefix": "Angle",
    "text": "*Name:* Geometry.Edge.Angle  \n*Desc:* create new adge by convert angle  \n *Arg1:* crpPair (Cursor Pair)  \n *Arg2:* dAngle (Double)  \n *Arg3:* bCurvature (Boolean)  \n *Arg4:* bBreakFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.NodeShortestPath": {
    "prefix": "NodeShortestPath",
    "text": "*Name:* Geometry.Edge.NodeShortestPath  \n*Desc:* create edge by 2 nodes shortest path  \n *Arg1:* crFirstNode (Cursor)  \n *Arg2:* crSecondNode (Cursor)  \n *Arg3:* iEnableBreakFace (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.OffsetLine": {
    "prefix": "OffsetLine",
    "text": "*Name:* Geometry.Edge.OffsetLine  \n*Desc:* Imprint geometry edge offset line  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crlEdge (Cursor List)  \n *Arg3:* bBreakFace (Boolean)  \n *Arg4:* dOffsetDistance (Double)  \n *Arg5:* iNumberLayer (Integer)  \n *Arg6:* bMerge (Boolean)  \n *Arg7:* bExtend (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.SplineFreeEdges": {
    "prefix": "SplineFreeEdges",
    "text": "*Name:* Geometry.Edge.SplineFreeEdges  \n*Desc:* Create Edge by spline  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* iEnableArc (Integer)  \n *Arg3:* crPart (Cursor)  \n *Arg4:* strBarName (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.ClosedLine": {
    "prefix": "ClosedLine",
    "text": "*Name:* Geometry.Edge.ClosedLine  \n*Desc:* imprint closed line  \n *Arg1:* veclPositions (Vector List)  \n *Arg2:* crlTargetFace (Cursor List)  \n *Arg3:* iEnableBreakFace (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.PerpendicularCylinderLine": {
    "prefix": "PerpendicularCylinderLine",
    "text": "*Name:* Geometry.Edge.PerpendicularCylinderLine  \n*Desc:*   \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* dOffset (Double)  \n *Arg5:* bOppositeSide (Boolean)  \n *Arg6:* bBreakFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.IntersectionLine": {
    "prefix": "IntersectionLine",
    "text": "*Name:* Geometry.Edge.IntersectionLine  \n*Desc:*   \n *Arg1:* crlFaces (Cursor List)  \n *Arg2:* bBreakFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.ProjectLine": {
    "prefix": "ProjectLine",
    "text": "*Name:* Geometry.Edge.ProjectLine  \n*Desc:*   \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* crlFaces (Cursor List)  \n *Arg3:* crlNode (Cursor List)  \n *Arg4:* bBreakFace (Boolean)  \n *Arg5:* iType (Integer)  \n *Arg6:* bCheckGap (Boolean)  \n *Arg7:* dGap (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Edge.PerpendicularLineToEdge": {
    "prefix": "PerpendicularLineToEdge",
    "text": "*Name:* Geometry.Edge.PerpendicularLineToEdge  \n*Desc:*   \n *Arg1:* crNode (Cursor)  \n *Arg2:* crEdge (Cursor)  \n *Arg3:* crlFace (Cursor List)  \n *Arg4:* bBreakFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.ExtractSurfaces.ExtractRefSurface": {
    "prefix": "ExtractRefSurface",
    "text": "*Name:* Geometry.ExtractSurfaces.ExtractRefSurface  \n*Desc:* Unknown Description  \n *Arg1:* listFace (FACE List)  \n *Arg2:* dAngle (Double)  \n *Arg3:* strName (String)  \n *Arg4:* isMergePart (IS_MERGE_PART)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.ExtractSurfaces.ExtractSurfaces": {
    "prefix": "ExtractSurfaces",
    "text": "*Name:* Geometry.ExtractSurfaces.ExtractSurfaces  \n*Desc:* Unknown Description  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dAngle (Double)  \n *Arg3:* strName (String)  \n *Arg4:* bMergePart (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Face.FourEdges": {
    "prefix": "FourEdges",
    "text": "*Name:* Geometry.Face.FourEdges  \n*Desc:* Create face by four edges  \n *Arg1:* crlEdge (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Face.FromMesh": {
    "prefix": "FromMesh",
    "text": "*Name:* Geometry.Face.FromMesh  \n*Desc:* Create geometry face from mesh face  \n *Arg1:* crlFace (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Face.CreateSmoothFace": {
    "prefix": "CreateSmoothFace",
    "text": "*Name:* Geometry.Face.CreateSmoothFace  \n*Desc:* Geometry Face CreateSmoothFace  \n *Arg1:* bInterPoration (Boolean)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* iElemGeneration (Integer)  \n *Arg4:* dGradation (Double)  \n *Arg5:* iEnableFaceSmooth (Integer)  \n *Arg6:* crTargetPart (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Face.Edges": {
    "prefix": "Edges",
    "text": "*Name:* Geometry.Face.Edges  \n*Desc:* Create Face From Edges  \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* crlPart (Cursor List)  \n *Arg3:* crlNode (Cursor List)  \n *Arg4:* bSharedFace (Boolean)  \n *Arg5:* bSmoothFace (Boolean)  \n *Arg6:* bCreatePart (Boolean)  \n *Arg7:* bImproved (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Face.Elements": {
    "prefix": "Elements",
    "text": "*Name:* Geometry.Face.Elements  \n*Desc:* Create Face By Elements  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* bShareFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.FindFeature.DelCircChamfer": {
    "prefix": "DelCircChamfer",
    "text": "*Name:* Geometry.FindFeature.DelCircChamfer  \n*Desc:* Delete Circ Chamfer  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* dMaxThick (Double)  \n *Arg3:* dMinThick (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.FindFeature.Fillet": {
    "prefix": "Fillet",
    "text": "*Name:* Geometry.FindFeature.Fillet  \n*Desc:* Find feature in part by typical description  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* dMinAngle (Double)  \n *Arg4:* dMaxAngle (Double)  \n *Arg5:* dMinFaceWidth (Double)  \n *Arg6:* dMaxFaceWidth (Double)  \n *Arg7:* dMinCurveRadius (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.FindFeature.Faces": {
    "prefix": "Faces",
    "text": "*Name:* Geometry.FindFeature.Faces  \n*Desc:* Unknown Description  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlEdge (Cursor List)  \n *Arg3:* bCylinder (Boolean)  \n *Arg4:* bDisc (Boolean)  \n *Arg5:* bFourCorners (Boolean)  \n *Arg6:* dMinThickness (Double)  \n *Arg7:* dMaxThickness (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.FindFeature.Edges": {
    "prefix": "Edges",
    "text": "*Name:* Geometry.FindFeature.Edges  \n*Desc:* Unknown Description  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlEdge (Cursor List)  \n *Arg3:* bCylinder (Boolean)  \n *Arg4:* bDisc (Boolean)  \n *Arg5:* bFourCorners (Boolean)  \n *Arg6:* dMinThickness (Double)  \n *Arg7:* dMaxThickness (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.MergeEntities.Faces": {
    "prefix": "Faces",
    "text": "*Name:* Geometry.MergeEntities.Faces  \n*Desc:* Merge faces  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* bMergeEdge (Boolean)  \n *Arg3:* bRemoveNonBoundEdge (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.MergeEntities.TinyFacesMerge": {
    "prefix": "TinyFacesMerge",
    "text": "*Name:* Geometry.MergeEntities.TinyFacesMerge  \n*Desc:* merge tiny faces  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* dMinFaceWidth (Double)  \n *Arg4:* dMaxFaceWidth (Double)  \n *Arg5:* dFaceAngle (Double)  \n *Arg6:* bReferLocalSetting (Boolean)  \n *Arg7:* bConnectFace (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.MergeEntities.CBarParts": {
    "prefix": "CBarParts",
    "text": "*Name:* Geometry.MergeEntities.CBarParts  \n*Desc:* Merge CBar Parts  \n *Arg1:* crlCBarPart (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.MergeEntities.Edges": {
    "prefix": "Edges",
    "text": "*Name:* Geometry.MergeEntities.Edges  \n*Desc:* Merge Edge  \n *Arg1:* crlEdge (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.MergeEntities.Parts": {
    "prefix": "Parts",
    "text": "*Name:* Geometry.MergeEntities.Parts  \n*Desc:* Merge Part  \n *Arg1:* dTolerance (Double)  \n *Arg2:* bRemovesharefaceflag (Boolean)  \n *Arg3:* crlPart (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.MergeEntities.PartFaces": {
    "prefix": "PartFaces",
    "text": "*Name:* Geometry.MergeEntities.PartFaces  \n*Desc:* Merge by Part Faces  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* bAngle (Boolean)  \n *Arg4:* dTolAngle (Double)  \n *Arg5:* bWidth (Boolean)  \n *Arg6:* dTolWidth (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Part.Cube": {
    "prefix": "Cube",
    "text": "*Name:* Geometry.Part.Cube  \n*Desc:* create cube part  \n *Arg1:* 0 (0)  \n *Arg2:* 0] (0])  \n *Arg3:* dlOrigin (Double List)  \n *Arg4:* 0.01 (0.01)  \n *Arg5:* 0.01] (0.01])  \n *Arg6:* dlLength (Double List)  \n *Arg7:* 10 (10)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Part.Wedge": {
    "prefix": "Wedge",
    "text": "*Name:* Geometry.Part.Wedge  \n*Desc:* Create Wedge Body  \n *Arg1:* 0.0 (0.0)  \n *Arg2:* 0.0] (0.0])  \n *Arg3:* vecOrigin (Vector)  \n *Arg4:* 0.01 (0.01)  \n *Arg5:* 0.01] (0.01])  \n *Arg6:* vecLength (Vector)  \n *Arg7:* 10 (10)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Part.Sphere": {
    "prefix": "Sphere",
    "text": "*Name:* Geometry.Part.Sphere  \n*Desc:* create Sphere part  \n *Arg1:* 0 (0)  \n *Arg2:* 0] (0])  \n *Arg3:* dlOrigin (Double List)  \n *Arg4:* dRadius (Double)  \n *Arg5:* iLatitudeNodeCnt (Integer)  \n *Arg6:* iLongitudeNodeCnt (Integer)  \n *Arg7:* strPartName (String)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Part.Torus": {
    "prefix": "Torus",
    "text": "*Name:* Geometry.Part.Torus  \n*Desc:* create Torus part  \n *Arg1:* 0 (0)  \n *Arg2:* 0] (0])  \n *Arg3:* dlOrigin (Double List)  \n *Arg4:* dInnerRadius (Double)  \n *Arg5:* dRingRadius (Double)  \n *Arg6:* iLatitudeNodeCnt (Integer)  \n *Arg7:* iLongitudeNodeCnt (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Part.Elems": {
    "prefix": "Elems",
    "text": "*Name:* Geometry.Part.Elems  \n*Desc:* create part from element  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* strPartName (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Part.Cylinder": {
    "prefix": "Cylinder",
    "text": "*Name:* Geometry.Part.Cylinder  \n*Desc:* create cylinder part  \n *Arg1:* dlOrigin (Double List)  \n *Arg2:* dTopRadius (Double)  \n *Arg3:* dBotRadius (Double)  \n *Arg4:* dHeight (Double)  \n *Arg5:* iCircleNodeCnt (Integer)  \n *Arg6:* iAxisNodeCnt (Integer)  \n *Arg7:* strName (String)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Part.Tube": {
    "prefix": "Tube",
    "text": "*Name:* Geometry.Part.Tube  \n*Desc:* create tube part  \n *Arg1:* dlOrigin (Double List)  \n *Arg2:* dTopInnerRadius (Double)  \n *Arg3:* dTopOuterRadius (Double)  \n *Arg4:* dBotInnerRadius (Double)  \n *Arg5:* dBotOuterRadius (Double)  \n *Arg6:* dHeight (Double)  \n *Arg7:* iCircleNodeCnt (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Part.Trapezoid": {
    "prefix": "Trapezoid",
    "text": "*Name:* Geometry.Part.Trapezoid  \n*Desc:* Create trapezoid part  \n *Arg1:* dlOrigin (Double List)  \n *Arg2:* 0.01 (0.01)  \n *Arg3:* 0.01] (0.01])  \n *Arg4:* dlLength (Double List)  \n *Arg5:* dTopXLength (Double)  \n *Arg6:* dRadius (Double)  \n *Arg7:* 10 (10)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Part.Cone": {
    "prefix": "Cone",
    "text": "*Name:* Geometry.Part.Cone  \n*Desc:* Create Cone Body  \n *Arg1:* dlOriginXyz (Double List)  \n *Arg2:* dBottomRadius (Double)  \n *Arg3:* dHeight (Double)  \n *Arg4:* iCircleNodeCount (Integer)  \n *Arg5:* iAxisNodeCnt (Integer)  \n *Arg6:* strPartName (String)  \n *Arg7:* iPartColor (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.ShowAdjacent.Faces": {
    "prefix": "Faces",
    "text": "*Name:* Geometry.ShowAdjacent.Faces  \n*Desc:* Unknown Description  \n *Arg1:* dAngle (Double)  \n *Arg2:* iIncludeStopFace (Integer)  \n *Arg3:* iLayer (Integer)  \n *Arg4:* bIsPreview (Boolean)  \n *Arg5:* crlStartFace (Cursor List)  \n *Arg6:* crlStopFace (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.ShowAdjacent.Elements": {
    "prefix": "Elements",
    "text": "*Name:* Geometry.ShowAdjacent.Elements  \n*Desc:* Unknown Description  \n *Arg1:* dAngle (Double)  \n *Arg2:* iIncludeStopFace (Integer)  \n *Arg3:* iLayer (Integer)  \n *Arg4:* bIsPreview (Boolean)  \n *Arg5:* crlStartElem (Cursor List)  \n *Arg6:* crlStopElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Transform.Rotation": {
    "prefix": "Rotation",
    "text": "*Name:* Geometry.Transform.Rotation  \n*Desc:* Rotate the selected Part.  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* posCenter (Position)  \n *Arg3:* vecAxis (Vector)  \n *Arg4:* dAngle (Double)  \n *Arg5:* bCreateNewPart (Boolean)  \n *Arg6:* bCopyLBC (Boolean)  \n *Arg7:* bCopyProperty (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Transform.Scaling": {
    "prefix": "Scaling",
    "text": "*Name:* Geometry.Transform.Scaling  \n*Desc:* Scale Body  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* dlScaleVector (Double List)  \n *Arg3:* dlScaleCentre (Double List)  \n *Arg4:* crCoordinate (Cursor)  \n *Arg5:* bCreateNew (Boolean)  \n *Arg6:* bCopyLbc (Boolean)  \n *Arg7:* bCopyProperty (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Transform.Mirror": {
    "prefix": "Mirror",
    "text": "*Name:* Geometry.Transform.Mirror  \n*Desc:* mirror body  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* 0.0 (0.0)  \n *Arg3:* 0.0]] (0.0]])  \n *Arg4:* veclPoint (Vector List)  \n *Arg5:* dOffset (Double)  \n *Arg6:* bCreateNewPart (Boolean)  \n *Arg7:* bCopyLBC (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Transform.Position": {
    "prefix": "Position",
    "text": "*Name:* Geometry.Transform.Position  \n*Desc:* transform position  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* 0.0 (0.0)  \n *Arg3:* 0.0]] (0.0]])  \n *Arg4:* veclPoint (Vector List)  \n *Arg5:* bCreateNewPart (Boolean)  \n *Arg6:* bCopyLBC (Boolean)  \n *Arg7:* bCopyProperty (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Transform.Translation": {
    "prefix": "Translation",
    "text": "*Name:* Geometry.Transform.Translation  \n*Desc:* Translate the selected Part.  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* poslTranslates (Position List)  \n *Arg3:* crCoord (Cursor)  \n *Arg4:* bCreateNewPart (Boolean)  \n *Arg5:* bCopyLBC (Boolean)  \n *Arg6:* bCopyProperty (Boolean)  \n *Arg7:* iCopyCount (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Transform.MatingFace": {
    "prefix": "MatingFace",
    "text": "*Name:* Geometry.Transform.MatingFace  \n*Desc:* Transform MatingFace  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crSrcFace (Cursor)  \n *Arg3:* crDstFace (Cursor)  \n *Arg4:* crSrcEdge (Cursor)  \n *Arg5:* crDstEdge (Cursor)  \n *Arg6:* crSrcNode (Cursor)  \n *Arg7:* crDstNode (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.Transform.CylinderFace": {
    "prefix": "CylinderFace",
    "text": "*Name:* Geometry.Transform.CylinderFace  \n*Desc:* transform position  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* 0.0 (0.0)  \n *Arg3:* 0.0]] (0.0]])  \n *Arg4:* veclPoint (Vector List)  \n *Arg5:* bCreateNewPart (Boolean)  \n *Arg6:* bCopyLBC (Boolean)  \n *Arg7:* bCopyProperty (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.CADTrim": {
    "prefix": "CADTrim",
    "text": "*Name:* Geometry.CADTrim  \n*Desc:* CAD Trim  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crlPart (Cursor List)  \n *Arg3:* dTrimSize (Double)  \n *Arg4:* dTrimAngle (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.StitchEdge": {
    "prefix": "StitchEdge",
    "text": "*Name:* Geometry.StitchEdge  \n*Desc:* Stitch Edges  \n *Arg1:* dTolerance (Double)  \n *Arg2:* bKeepSlave (Boolean)  \n *Arg3:* crlMaster (Cursor List)  \n *Arg4:* crlSlave (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.LogoRemoval": {
    "prefix": "LogoRemoval",
    "text": "*Name:* Geometry.LogoRemoval  \n*Desc:* Create Face From Edges  \n *Arg1:* crlStartFaces (Cursor List)  \n *Arg2:* crlStopFaces (Cursor List)  \n *Arg3:* iLayers (Integer)  \n *Arg4:* bMergeFaces (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.ShellAsm": {
    "prefix": "ShellAsm",
    "text": "*Name:* Geometry.ShellAsm  \n*Desc:* assemble the separated parts  \n *Arg1:* crlPartK (Cursor List)  \n *Arg2:* crlFaceK (Cursor List)  \n *Arg3:* dTol (Double)  \n *Arg4:* iElemType (Integer)  \n *Arg5:* bSkipTiny (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.SquareUpFillet": {
    "prefix": "SquareUpFillet",
    "text": "*Name:* Geometry.SquareUpFillet  \n*Desc:* Square Up Fillet  \n *Arg1:* crlFace (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.MakeFillet": {
    "prefix": "MakeFillet",
    "text": "*Name:* Geometry.MakeFillet  \n*Desc:*   \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* dRadius (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.MakeFacePlanar": {
    "prefix": "MakeFacePlanar",
    "text": "*Name:* Geometry.MakeFacePlanar  \n*Desc:* Make planar faces by given plane points  \n *Arg1:* dlPlanePt1 (Double List)  \n *Arg2:* dlPlanePt2 (Double List)  \n *Arg3:* dlPlanePt3 (Double List)  \n *Arg4:* ilFaceIds (Integer List)  \n *Arg5:* iMergeFace (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.FCircleAdjustVertex": {
    "prefix": "FCircleAdjustVertex",
    "text": "*Name:* Geometry.FCircleAdjustVertex  \n*Desc:* adjust vertex in circle  \n *Arg1:* crlPart (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.AdjustHalfCylinder": {
    "prefix": "AdjustHalfCylinder",
    "text": "*Name:* Geometry.AdjustHalfCylinder  \n*Desc:* Adjust half cylinder  \n *Arg1:* poslPoint (Position List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* crCoord (Cursor)  \n *Arg4:* iAxisPlane (Integer)  \n *Arg5:* bDivideFace (Boolean)  \n *Arg6:* crlPart (Cursor List)  \n *Arg7:* bMergeEdge (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.FCircVertexAdjust": {
    "prefix": "FCircVertexAdjust",
    "text": "*Name:* Geometry.FCircVertexAdjust  \n*Desc:* FCirc Vertex Adjust  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* dMinRadius (Double)  \n *Arg3:* bFullCylinder (Boolean)  \n *Arg4:* bCylinderMorethan90 (Boolean)  \n *Arg5:* bSkipFaceHaveLocalSetting (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.ExtractSurfaces": {
    "prefix": "ExtractSurfaces",
    "text": "*Name:* Geometry.ExtractSurfaces  \n*Desc:* Extract Reference Surfaces  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dAngle (Double)  \n *Arg3:* strName (String)  \n *Arg4:* bMergePart (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.RemoveRibBoss": {
    "prefix": "RemoveRibBoss",
    "text": "*Name:* Geometry.RemoveRibBoss  \n*Desc:*   \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dGradiation (Double)  \n *Arg3:* iContinuity (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.AdvancedShellAssembly": {
    "prefix": "AdvancedShellAssembly",
    "text": "*Name:* Geometry.AdvancedShellAssembly  \n*Desc:* Test shell assembly  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* iMeshType (Integer)  \n *Arg4:* bSelfIntersection (Boolean)  \n *Arg5:* iMethod (Integer)  \n *Arg6:* dGapTol (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Geometry.ExtractRefSurface": {
    "prefix": "ExtractRefSurface",
    "text": "*Name:* Geometry.ExtractRefSurface  \n*Desc:* Unknown Description  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dAngle (Double)  \n *Arg3:* strName (String)  \n *Arg4:* bMergePart (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Groups.RightClick.PropertyGroup": {
    "prefix": "PropertyGroup",
    "text": "*Name:* Groups.RightClick.PropertyGroup  \n*Desc:* create group of properties  \n *Arg1:* strTmp (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Groups.RightClick.Rename": {
    "prefix": "Rename",
    "text": "*Name:* Groups.RightClick.Rename  \n*Desc:* Unknown Description  \n *Arg1:* strNewName (String)  \n *Arg2:* crItem (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Groups.RightClick.DeleteGroup": {
    "prefix": "DeleteGroup",
    "text": "*Name:* Groups.RightClick.DeleteGroup  \n*Desc:* Delete Group  \n *Arg1:* crlDelGroup (Cursor List)  \n *Arg2:* bRemoveAll (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Groups.RightClick.CopyGroup": {
    "prefix": "CopyGroup",
    "text": "*Name:* Groups.RightClick.CopyGroup  \n*Desc:* Copy Group  \n *Arg1:* crlSrc (Cursor List)  \n *Arg2:* strlNames (String List)  \n *Arg3:* crDest (Cursor)  \n *Arg4:* bKeep (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Groups.RightClick.AddSupGroup": {
    "prefix": "AddSupGroup",
    "text": "*Name:* Groups.RightClick.AddSupGroup  \n*Desc:* Add supper group  \n *Arg1:* crSupGroupSelected (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Groups.RightClick.CreateMatGroup": {
    "prefix": "CreateMatGroup",
    "text": "*Name:* Groups.RightClick.CreateMatGroup  \n*Desc:* Unknown Description  \n *Arg1:* strTmp (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.Sweep.Circular": {
    "prefix": "Circular",
    "text": "*Name:* HexModeling.Sweep.Circular  \n*Desc:* Unknown Description  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dAngle (Double)  \n *Arg3:* dTol (Double)  \n *Arg4:* iLayer (Integer)  \n *Arg5:* vecAxisPt (Vector)  \n *Arg6:* vecAxisVect (Vector)  \n *Arg7:* bInterfaceElem (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.Sweep.FaceToFace": {
    "prefix": "FaceToFace",
    "text": "*Name:* HexModeling.Sweep.FaceToFace  \n*Desc:* Unknown Description  \n *Arg1:* crSrcFace (Cursor)  \n *Arg2:* crDstFace (Cursor)  \n *Arg3:* bDeleteOriginalParts (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.Sweep.Layer": {
    "prefix": "Layer",
    "text": "*Name:* HexModeling.Sweep.Layer  \n*Desc:* Unknown Description  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dFrontWidth (Double)  \n *Arg3:* dBackWidth (Double)  \n *Arg4:* iFrontLayers (Integer)  \n *Arg5:* iBackLayers (Integer)  \n *Arg6:* iBaseFaceType (Integer)  \n *Arg7:* iSeparate (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.Sweep.Linear": {
    "prefix": "Linear",
    "text": "*Name:* HexModeling.Sweep.Linear  \n*Desc:* Unknown Description  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dLength (Double)  \n *Arg3:* iLayer (Integer)  \n *Arg4:* dlSweepDirection (Double List)  \n *Arg5:* bInterfaceElemFlag (Boolean)  \n *Arg6:* iLinearMethod (Integer)  \n *Arg7:* bDeleteOriginalParts (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.Sweep.Curve": {
    "prefix": "Curve",
    "text": "*Name:* HexModeling.Sweep.Curve  \n*Desc:* Unknown Description  \n *Arg1:* crFace (Cursor)  \n *Arg2:* crlEdge (Cursor List)  \n *Arg3:* crlRefEdge (Cursor List)  \n *Arg4:* dMeshSize (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.Sweep.FromMidPlane": {
    "prefix": "FromMidPlane",
    "text": "*Name:* HexModeling.Sweep.FromMidPlane  \n*Desc:* Unknown Description  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* bRef (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.SolidElemInterface": {
    "prefix": "SolidElemInterface",
    "text": "*Name:* HexModeling.SolidElemInterface  \n*Desc:* make solid elem interface  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* bFlip (Boolean)  \n *Arg3:* crlElms (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.BallHexa": {
    "prefix": "BallHexa",
    "text": "*Name:* HexModeling.BallHexa  \n*Desc:* hexa modeling ball hexa  \n *Arg1:* crPart (Cursor)  \n *Arg2:* vecCenter (Vector)  \n *Arg3:* dRadius (Double)  \n *Arg4:* dMeshSize (Double)  \n *Arg5:* iType (Integer)  \n *Arg6:* iLayer (Integer)  \n *Arg7:* bMakeCenterNode (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.BoxMesh": {
    "prefix": "BoxMesh",
    "text": "*Name:* HexModeling.BoxMesh  \n*Desc:* Box hex mesh creator for parts  \n *Arg1:* ilPartIds (Integer List)  \n *Arg2:* dMeshSize (Double)  \n *Arg3:* strMaterialName (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.AutoSweep": {
    "prefix": "AutoSweep",
    "text": "*Name:* HexModeling.AutoSweep  \n*Desc:* Hex Modeling Auto Sweep  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* dMeshSize (Double)  \n *Arg3:* bLayers (Boolean)  \n *Arg4:* iLayers (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.Circular": {
    "prefix": "Circular",
    "text": "*Name:* HexModeling.Circular  \n*Desc:* create Hexa mesh by revolving a surface  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dAngle (Double)  \n *Arg3:* dTol (Double)  \n *Arg4:* iLayer (Integer)  \n *Arg5:* vecAxisPt (Vector)  \n *Arg6:* vecAxisVect (Vector)  \n *Arg7:* bInterfaceElem (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.FaceToFace": {
    "prefix": "FaceToFace",
    "text": "*Name:* HexModeling.FaceToFace  \n*Desc:*   \n *Arg1:* crSrcFace (Cursor)  \n *Arg2:* crDstFace (Cursor)  \n *Arg3:* bDeleteOriginalParts (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.Layer": {
    "prefix": "Layer",
    "text": "*Name:* HexModeling.Layer  \n*Desc:* sweep by layer  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dFrontWidth (Double)  \n *Arg3:* dBackWidth (Double)  \n *Arg4:* iFrontLayers (Integer)  \n *Arg5:* iBackLayers (Integer)  \n *Arg6:* iBaseFaceType (Integer)  \n *Arg7:* iSeparate (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.Linear": {
    "prefix": "Linear",
    "text": "*Name:* HexModeling.Linear  \n*Desc:* Linear hex mesh creation  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* dLength (Double)  \n *Arg3:* iLayer (Integer)  \n *Arg4:* vecSweepDirection (Vector)  \n *Arg5:* bInterfaceElemFlag (Boolean)  \n *Arg6:* iLinearMethod (Integer)  \n *Arg7:* bDeleteOriginalParts (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.FromMidPlane": {
    "prefix": "FromMidPlane",
    "text": "*Name:* HexModeling.FromMidPlane  \n*Desc:* HexModeling From MidPlane  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* bRef (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "HexModeling.Curve": {
    "prefix": "Curve",
    "text": "*Name:* HexModeling.Curve  \n*Desc:* make hex by sweeping curve  \n *Arg1:* crFace (Cursor)  \n *Arg2:* crlEdge (Cursor List)  \n *Arg3:* crlRefEdge (Cursor List)  \n *Arg4:* dMeshSize (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportCAD.Elysium": {
    "prefix": "Elysium",
    "text": "*Name:* Home.ImportCAD.Elysium  \n*Desc:* import elysium  \n *Arg1:* strlPath (String List)  \n *Arg2:* dChordHeightTolerance (Double)  \n *Arg3:* dAngleToleranceDegree (Double)  \n *Arg4:* dPointCoincidentTolerance (Double)  \n *Arg5:* iConvertIsolatedCurve (Integer)  \n *Arg6:* iDekCleanselfintersectingloop (Integer)  \n *Arg7:* iDekVolumetopart (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportCAD.Spatial": {
    "prefix": "Spatial",
    "text": "*Name:* Home.ImportCAD.Spatial  \n*Desc:* import CAD by Spatial  \n *Arg1:* strlPath (String List)  \n *Arg2:* dSurfacePlaneTolerance (Double)  \n *Arg3:* dSufacePlaneAngle (Double)  \n *Arg4:* dMaxFacetWidth (Double)  \n *Arg5:* bNXMultipart (Boolean)  \n *Arg6:* bHealing (Boolean)  \n *Arg7:* bIsNXDirect (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportCAD.Parasolid": {
    "prefix": "Parasolid",
    "text": "*Name:* Home.ImportCAD.Parasolid  \n*Desc:* Import Parasolid  \n *Arg1:* strlFiles (String List)  \n *Arg2:* dChordHeightTolerance (Double)  \n *Arg3:* dAngleToleranceDegree (Double)  \n *Arg4:* iConvertIsolatedCurve (Integer)  \n *Arg5:* dSurfacePlaneTolerance (Double)  \n *Arg6:* dSufacePlaneAngle (Double)  \n *Arg7:* dMaxFacetWidth (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportCAD.STL": {
    "prefix": "STL",
    "text": "*Name:* Home.ImportCAD.STL  \n*Desc:* Import STL  \n *Arg1:* strlFiles (String List)  \n *Arg2:* dChordHeightTolerance (Double)  \n *Arg3:* dAngleToleranceDegree (Double)  \n *Arg4:* iConvertIsolatedCurve (Integer)  \n *Arg5:* dSurfacePlaneTolerance (Double)  \n *Arg6:* dSufacePlaneAngle (Double)  \n *Arg7:* dMaxFacetWidth (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportCAD.VRML": {
    "prefix": "VRML",
    "text": "*Name:* Home.ImportCAD.VRML  \n*Desc:* Import VRML  \n *Arg1:* strlFiles (String List)  \n *Arg2:* dChordHeightTolerance (Double)  \n *Arg3:* dAngleToleranceDegree (Double)  \n *Arg4:* iConvertIsolatedCurve (Integer)  \n *Arg5:* dSurfacePlaneTolerance (Double)  \n *Arg6:* dSufacePlaneAngle (Double)  \n *Arg7:* dMaxFacetWidth (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportCAD.ProECreoDirect": {
    "prefix": "ProECreoDirect",
    "text": "*Name:* Home.ImportCAD.ProECreoDirect  \n*Desc:* import Creo by Direct  \n *Arg1:* strlPath (String List)  \n *Arg2:* dChordHeightTolerance (Double)  \n *Arg3:* dAngleToleranceDegree (Double)  \n *Arg4:* dStepMaxSize (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportCAD.TechnoStarGeometry": {
    "prefix": "TechnoStarGeometry",
    "text": "*Name:* Home.ImportCAD.TechnoStarGeometry  \n*Desc:* Import Geometry bdf file  \n *Arg1:* strlPath (String List)  \n *Arg2:* bUseUnit (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportMesh.ADVCADX": {
    "prefix": "ADVCADX",
    "text": "*Name:* Home.ImportMesh.ADVCADX  \n*Desc:* import adx files  \n *Arg1:* strPath (String)  \n *Arg2:* dFaceAngle (Double)  \n *Arg3:* dEdgeAngle (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportMesh.AnsysDat": {
    "prefix": "AnsysDat",
    "text": "*Name:* Home.ImportMesh.AnsysDat  \n*Desc:* Import Ansys file  \n *Arg1:* strlPath (String List)  \n *Arg2:* dFaceAngle (Double)  \n *Arg3:* dEdgeAngle (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportMesh.NastranBdf": {
    "prefix": "NastranBdf",
    "text": "*Name:* Home.ImportMesh.NastranBdf  \n*Desc:* import Nastran bdf file  \n *Arg1:* strlFilePaths (String List)  \n *Arg2:* iImportType (Integer)  \n *Arg3:* dFaceAngle (Double)  \n *Arg4:* dEdgeAngle (Double)  \n *Arg5:* bReadNameComment (Boolean)  \n *Arg6:* iCreateDup1DElemAnswer (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportMesh.AbaqusINP": {
    "prefix": "AbaqusINP",
    "text": "*Name:* Home.ImportMesh.AbaqusINP  \n*Desc:* import Abaqus INP file  \n *Arg1:* strlFilePaths (String List)  \n *Arg2:* dFaceAngle (Double)  \n *Arg3:* dEdgeAngle (Double)  \n *Arg4:* iImportType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportMesh.LSDYNA": {
    "prefix": "LSDYNA",
    "text": "*Name:* Home.ImportMesh.LSDYNA  \n*Desc:* Import Ls-Dyna file  \n *Arg1:* strlPath (String List)  \n *Arg2:* dFaceAngle (Double)  \n *Arg3:* dEdgeAngle (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportMesh.Universal": {
    "prefix": "Universal",
    "text": "*Name:* Home.ImportMesh.Universal  \n*Desc:* Import Universal  \n *Arg1:* strPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ImportMesh.TSVPre": {
    "prefix": "TSVPre",
    "text": "*Name:* Home.ImportMesh.TSVPre  \n*Desc:* Convert a old TSV-Pre/Designer file into one or more jtdb files.  \n *Arg1:* strImportPath (String)  \n *Arg2:* strExportPath (String)  \n *Arg3:* ilModelIndex (Integer List)  \n *Arg4:* iMerge (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ExportSTL": {
    "prefix": "ExportSTL",
    "text": "*Name:* Home.ExportSTL  \n*Desc:* export stl  \n *Arg1:* strFile (String)  \n *Arg2:* crlPart (Cursor List)  \n *Arg3:* dScale (Double)  \n *Arg4:* bFilterIndex (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ExportGeometryBDF": {
    "prefix": "ExportGeometryBDF",
    "text": "*Name:* Home.ExportGeometryBDF  \n*Desc:* Unknown Description  \n *Arg1:* strFileName (String)  \n *Arg2:* crlPart (Cursor List)  \n *Arg3:* bBigID (Boolean)  \n *Arg4:* bUseUnit (Boolean)  \n *Arg5:* bVert (Boolean)  \n *Arg6:* bEdge (Boolean)  \n *Arg7:* bFace (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.ToImage": {
    "prefix": "ToImage",
    "text": "*Name:* Home.ToImage  \n*Desc:* Unknown Description  \n *Arg1:* strImgPath (String)  \n *Arg2:* bWhiteBG (Boolean)  \n *Arg3:* bTransparentBG (Boolean)  \n *Arg4:* bFixedSize (Boolean)  \n *Arg5:* iExportWidth (Integer)  \n *Arg6:* iExportHeight (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.Find": {
    "prefix": "Find",
    "text": "*Name:* Home.Find  \n*Desc:* Unknown Description  \n *Arg1:* strSearch (String)  \n *Arg2:* strSeletedType (String)  \n *Arg3:* bFindMatch (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.RectangularCapture": {
    "prefix": "RectangularCapture",
    "text": "*Name:* Home.RectangularCapture  \n*Desc:* Unknown Description  \n *Arg1:* iLeft (Integer)  \n *Arg2:* iTop (Integer)  \n *Arg3:* iRight (Integer)  \n *Arg4:* iBottom (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.CopyToClipboard": {
    "prefix": "CopyToClipboard",
    "text": "*Name:* Home.CopyToClipboard  \n*Desc:* Unknown Description  \n *Arg1:* bWhiteBG (Boolean)  \n *Arg2:* bTransparentBG (Boolean)  \n *Arg3:* bFixedSize (Boolean)  \n *Arg4:* iWidth (Integer)  \n *Arg5:* iHeight (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.FullScreen": {
    "prefix": "FullScreen",
    "text": "*Name:* Home.FullScreen  \n*Desc:* Unknown Description  \n *Arg1:*  ()  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Home.Synchronize": {
    "prefix": "Synchronize",
    "text": "*Name:* Home.Synchronize  \n*Desc:* Unknown Description  \n *Arg1:*  ()  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MainWindow.RightClick.MergeFaces": {
    "prefix": "MergeFaces",
    "text": "*Name:* MainWindow.RightClick.MergeFaces  \n*Desc:* Merge Faces  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* bIsMergeEdge (Boolean)  \n *Arg3:* bRemoveNonBoundEdge (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MainWindow.RightClick.SelectAllParts": {
    "prefix": "SelectAllParts",
    "text": "*Name:* MainWindow.RightClick.SelectAllParts  \n*Desc:* Select all of the parts in the model  \n *Arg1:*  ()  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MainWindow.RightClick.AssociatedPick": {
    "prefix": "AssociatedPick",
    "text": "*Name:* MainWindow.RightClick.AssociatedPick  \n*Desc:* pick associated entity  \n *Arg1:* crlInput (Cursor List)  \n *Arg2:* strTarget (String)  \n *Arg3:* strConnect (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MainWindow.RightClick.FlipElement": {
    "prefix": "FlipElement",
    "text": "*Name:* MainWindow.RightClick.FlipElement  \n*Desc:* flip element  \n *Arg1:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Element.SolidElement": {
    "prefix": "SolidElement",
    "text": "*Name:* MeshCleanup.Element.SolidElement  \n*Desc:* Change Topology for Solid Element  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* crPart (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Element.SurfaceElement": {
    "prefix": "SurfaceElement",
    "text": "*Name:* MeshCleanup.Element.SurfaceElement  \n*Desc:* Change Topology Element  \n *Arg1:* ilElement (Integer List)  \n *Arg2:* ilFace (Integer List)  \n *Arg3:* ilPart (Integer List)  \n *Arg4:* iCreateNewPart (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Face": {
    "prefix": "Face",
    "text": "*Name:* MeshCleanup.Face  \n*Desc:* change topology face  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crlPart (Cursor List)  \n *Arg3:* bCreateNewPart (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.CorrectModel": {
    "prefix": "CorrectModel",
    "text": "*Name:* MeshCleanup.CorrectModel  \n*Desc:* correct model  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* iEnableBreakEdge (Integer)  \n *Arg3:* dEdgeAngle (Double)  \n *Arg4:* iEnableMergeEdge (Integer)  \n *Arg5:* dMergeEdgeAngle (Double)  \n *Arg6:* iEnableMergePlanarFace (Integer)  \n *Arg7:* iEnableRemoveExtraVertex (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.CloseHoles": {
    "prefix": "CloseHoles",
    "text": "*Name:* MeshCleanup.CloseHoles  \n*Desc:* close holes  \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* dAreaMin (Double)  \n *Arg3:* dAreaMax (Double)  \n *Arg4:* bMergeFace (Boolean)  \n *Arg5:* bMergeEdge (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.CloseGap": {
    "prefix": "CloseGap",
    "text": "*Name:* MeshCleanup.CloseGap  \n*Desc:* MeshCleanup Cleanup CloseGap  \n *Arg1:* crlPartCur (Cursor List)  \n *Arg2:* dDistanceTol (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.AutoCheck": {
    "prefix": "AutoCheck",
    "text": "*Name:* MeshCleanup.AutoCheck  \n*Desc:* check meshing quality  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* iElemType (Integer)  \n *Arg3:* blCheckCondition (Boolean List)  \n *Arg4:* blElemQuality (Boolean List)  \n *Arg5:* dlLimitValue (Double List)  \n *Arg6:* crlElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.ManualCheck": {
    "prefix": "ManualCheck",
    "text": "*Name:* MeshCleanup.ManualCheck  \n*Desc:* MeshCleanup ManualCheck  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* iElemType (Integer)  \n *Arg3:* iVeQuality (Integer)  \n *Arg4:* iCheckCondition (Integer)  \n *Arg5:* dLimitValue (Double)  \n *Arg6:* dCFLValue (Double)  \n *Arg7:* iNonManifold (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.ChangeTopology.Element.SurfaceElement": {
    "prefix": "SurfaceElement",
    "text": "*Name:* MeshCleanup.ChangeTopology.Element.SurfaceElement  \n*Desc:* Unknown Description  \n *Arg1:* ilElement (Integer List)  \n *Arg2:* ilFace (Integer List)  \n *Arg3:* ilPart (Integer List)  \n *Arg4:* iCreateNewPart (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Cleanup.CloseGap": {
    "prefix": "CloseGap",
    "text": "*Name:* MeshCleanup.Cleanup.CloseGap  \n*Desc:* Unknown Description  \n *Arg1:* crlPartCur (Cursor List)  \n *Arg2:* dDistanceTol (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad": {
    "prefix": "TwoQuadsToQuad",
    "text": "*Name:* MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad  \n*Desc:* Merge two Quad elements into one Quad element  \n *Arg1:* crlElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual2D.MergeElement.TwoTrisToQuad": {
    "prefix": "TwoTrisToQuad",
    "text": "*Name:* MeshCleanup.Manual2D.MergeElement.TwoTrisToQuad  \n*Desc:*   \n *Arg1:* crlElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Split element 2D  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* crDatumNode0 (Cursor)  \n *Arg3:* crDatumNode1 (Cursor)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iAutoExecute (Integer)  \n *Arg6:* iAutoTransition (Integer)  \n *Arg7:* iCADProject (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* crDatumNode0 (Cursor)  \n *Arg3:* crDatumNode1 (Cursor)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iAutoExecute (Integer)  \n *Arg6:* iAutoTransition (Integer)  \n *Arg7:* iCADProject (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* crDatumNode0 (Cursor)  \n *Arg3:* crDatumNode1 (Cursor)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iAutoExecute (Integer)  \n *Arg6:* iAutoTransition (Integer)  \n *Arg7:* iCADProject (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* crDatumNode0 (Cursor)  \n *Arg3:* crDatumNode1 (Cursor)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iAutoExecute (Integer)  \n *Arg6:* iAutoTransition (Integer)  \n *Arg7:* iCADProject (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* crDatumNode0 (Cursor)  \n *Arg3:* crDatumNode1 (Cursor)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iAutoExecute (Integer)  \n *Arg6:* iAutoTransition (Integer)  \n *Arg7:* iCADProject (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* crDatumNode0 (Cursor)  \n *Arg3:* crDatumNode1 (Cursor)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iAutoExecute (Integer)  \n *Arg6:* iAutoTransition (Integer)  \n *Arg7:* iCADProject (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* crDatumNode0 (Cursor)  \n *Arg3:* crDatumNode1 (Cursor)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iAutoExecute (Integer)  \n *Arg6:* iAutoTransition (Integer)  \n *Arg7:* iCADProject (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual2D.SplitElement.QuadToQuadTri": {
    "prefix": "QuadToQuadTri",
    "text": "*Name:* MeshCleanup.Manual2D.SplitElement.QuadToQuadTri  \n*Desc:* Unknown Description  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* crDatumNode0 (Cursor)  \n *Arg3:* crDatumNode1 (Cursor)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iAutoExecute (Integer)  \n *Arg6:* iAutoTransition (Integer)  \n *Arg7:* iCADProject (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Unknown Description  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* crDatumNode0 (Cursor)  \n *Arg3:* crDatumNode1 (Cursor)  \n *Arg4:* iMethod (Integer)  \n *Arg5:* iAutoExecute (Integer)  \n *Arg6:* iAutoTransition (Integer)  \n *Arg7:* iCADProject (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual2D.Equivalence": {
    "prefix": "Equivalence",
    "text": "*Name:* MeshCleanup.Manual2D.Equivalence  \n*Desc:* Equivalence Nodes  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* iTypeEquiva (Integer)  \n *Arg3:* dTolerance (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual2D.DeleteElement": {
    "prefix": "DeleteElement",
    "text": "*Name:* MeshCleanup.Manual2D.DeleteElement  \n*Desc:* Delete Element  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* bKeepShareElem (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual2D.Split": {
    "prefix": "Split",
    "text": "*Name:* MeshCleanup.Manual2D.Split  \n*Desc:* manual cleanup by split  \n *Arg1:* crplElemEdge (Cursor Pair List)  \n *Arg2:* dRatio (Double)  \n *Arg3:* crNodeRef (Cursor)  \n *Arg4:* crProjectPart (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual2D.Swap": {
    "prefix": "Swap",
    "text": "*Name:* MeshCleanup.Manual2D.Swap  \n*Desc:* Swap Element Edge  \n *Arg1:* crplElemEdge (Cursor Pair List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual2D.Collapse": {
    "prefix": "Collapse",
    "text": "*Name:* MeshCleanup.Manual2D.Collapse  \n*Desc:* Collapse for Mesh Cleanup  \n *Arg1:* crNodeRef (Cursor)  \n *Arg2:* crNodeEq (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual2D.CreateElement": {
    "prefix": "CreateElement",
    "text": "*Name:* MeshCleanup.Manual2D.CreateElement  \n*Desc:* Create element  \n *Arg1:* iElemType (Integer)  \n *Arg2:* crParentEntity (Cursor)  \n *Arg3:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual2D.RemeshElement": {
    "prefix": "RemeshElement",
    "text": "*Name:* MeshCleanup.Manual2D.RemeshElement  \n*Desc:* local surface remesh  \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* surfaceMesh (SURFACE_MESH)  \n *Arg3:* bUseSetting (Boolean)  \n *Arg4:* bGrading (Boolean)  \n *Arg5:* bFMesher (Boolean)  \n *Arg6:* iOverrideType (Integer)  \n *Arg7:* bKeepConnection (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual3D.Collapse.CenterFaceCollapse": {
    "prefix": "CenterFaceCollapse",
    "text": "*Name:* MeshCleanup.Manual3D.Collapse.CenterFaceCollapse  \n*Desc:*   \n *Arg1:* crlElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse": {
    "prefix": "HalfEdgeCollapse",
    "text": "*Name:* MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse  \n*Desc:* mash cleanup by manual for half edge collapse  \n *Arg1:* crplElemEdge (Cursor Pair List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual3D.Collapse.EdgeCollapse": {
    "prefix": "EdgeCollapse",
    "text": "*Name:* MeshCleanup.Manual3D.Collapse.EdgeCollapse  \n*Desc:* collapse  \n *Arg1:* crplElemEdge (Cursor Pair List)  \n *Arg2:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual3D.DeleteNode": {
    "prefix": "DeleteNode",
    "text": "*Name:* MeshCleanup.Manual3D.DeleteNode  \n*Desc:* remove node for solid element.  \n *Arg1:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual3D.Swap": {
    "prefix": "Swap",
    "text": "*Name:* MeshCleanup.Manual3D.Swap  \n*Desc:* cleanup element edge by swap  \n *Arg1:* crplElemEdge (Cursor Pair List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual3D.Equivalence": {
    "prefix": "Equivalence",
    "text": "*Name:* MeshCleanup.Manual3D.Equivalence  \n*Desc:*   \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* iMergeTowards (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual3D.Split": {
    "prefix": "Split",
    "text": "*Name:* MeshCleanup.Manual3D.Split  \n*Desc:* Merge two Quad elements into one Quad element  \n *Arg1:* crplElemEdge (Cursor Pair List)  \n *Arg2:* crlNode (Cursor List)  \n *Arg3:* dRatioDistance (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual3D.CreateHex": {
    "prefix": "CreateHex",
    "text": "*Name:* MeshCleanup.Manual3D.CreateHex  \n*Desc:* create hex8 elements  \n *Arg1:* iParentEntityId (Integer)  \n *Arg2:* crlElem (Cursor List)  \n *Arg3:* iSeprateN (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual3D.CreatePenta": {
    "prefix": "CreatePenta",
    "text": "*Name:* MeshCleanup.Manual3D.CreatePenta  \n*Desc:* Create penta5 element  \n *Arg1:* iParentEntityId (Integer)  \n *Arg2:* crlElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.Manual3D.CreateTetra": {
    "prefix": "CreateTetra",
    "text": "*Name:* MeshCleanup.Manual3D.CreateTetra  \n*Desc:* create element Tet  \n *Arg1:* iParentEntityId (Integer)  \n *Arg2:* crlNode (Cursor List)  \n *Arg3:* crlElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshCleanup.ManualCheck.Tri": {
    "prefix": "Tri",
    "text": "*Name:* MeshCleanup.ManualCheck.Tri  \n*Desc:* Unknown Description  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* nElemType (N_ELEM_TYPE)  \n *Arg3:* veQuality (VE_QUALITY)  \n *Arg4:* nCheckCondition (N_CHECK_CONDITION)  \n *Arg5:* dLimitValue (Double)  \n *Arg6:* CFLValue (CFLVALUE)  \n *Arg7:* nNonManifold (N_NON_MANIFOLD)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateElement.Hex": {
    "prefix": "Hex",
    "text": "*Name:* MeshEdit.CreateElement.Hex  \n*Desc:* create hex8 elements  \n *Arg1:* iParentEntityId (Integer)  \n *Arg2:* crlElem (Cursor List)  \n *Arg3:* iSeprateN (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateElement.Penta": {
    "prefix": "Penta",
    "text": "*Name:* MeshEdit.CreateElement.Penta  \n*Desc:* Create penta element  \n *Arg1:* iParentEntityId (Integer)  \n *Arg2:* crlElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateElement.Tet": {
    "prefix": "Tet",
    "text": "*Name:* MeshEdit.CreateElement.Tet  \n*Desc:* create element Tet  \n *Arg1:* iParentEntityId (Integer)  \n *Arg2:* crlNode (Cursor List)  \n *Arg3:* crlElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Create element  \n *Arg1:* iElemType (Integer)  \n *Arg2:* crParentEntity (Cursor)  \n *Arg3:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Create element  \n *Arg1:* iElemType (Integer)  \n *Arg2:* crParentEntity (Cursor)  \n *Arg3:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.CircleCenter": {
    "prefix": "CircleCenter",
    "text": "*Name:* MeshEdit.CreateNode.CircleCenter  \n*Desc:* create node at center of circle  \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* iNodeID (Integer)  \n *Arg3:* bImprint (Boolean)  \n *Arg4:* crFace (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.Absolute": {
    "prefix": "Absolute",
    "text": "*Name:* MeshEdit.CreateNode.Absolute  \n*Desc:* create node by input direct value  \n *Arg1:* veclNodeCoord (Vector List)  \n *Arg2:* ilNewNodeID (Integer List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.Import": {
    "prefix": "Import",
    "text": "*Name:* MeshEdit.CreateNode.Import  \n*Desc:* create node by importing CSV file  \n *Arg1:* strCsvFilePath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.Point": {
    "prefix": "Point",
    "text": "*Name:* MeshEdit.CreateNode.Point  \n*Desc:* create node point  \n *Arg1:* iNodeID (Integer)  \n *Arg2:* posPoint (Position)  \n *Arg3:* bImprint (Boolean)  \n *Arg4:* crShape (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* create node point  \n *Arg1:* iNodeID (Integer)  \n *Arg2:* dX (Double)  \n *Arg3:* dY (Double)  \n *Arg4:* dZ (Double)  \n *Arg5:* iNumberofNodes (Integer)  \n *Arg6:* bImprint (Boolean)  \n *Arg7:* crlNode (Cursor List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* create node point  \n *Arg1:* iNodeID (Integer)  \n *Arg2:* dX (Double)  \n *Arg3:* dY (Double)  \n *Arg4:* dZ (Double)  \n *Arg5:* bImprint (Boolean)  \n *Arg6:* crlNode (Cursor List)  \n *Arg7:* crlFace (Cursor List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.ProjectToPlane": {
    "prefix": "ProjectToPlane",
    "text": "*Name:* MeshEdit.CreateNode.ProjectToPlane  \n*Desc:* create node point  \n *Arg1:* dX (Double)  \n *Arg2:* dY (Double)  \n *Arg3:* dZ (Double)  \n *Arg4:* crlNode (Cursor List)  \n *Arg5:* crlFace (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.CenterOfCylinder": {
    "prefix": "CenterOfCylinder",
    "text": "*Name:* MeshEdit.CreateNode.CenterOfCylinder  \n*Desc:* Create node of center cylinder  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* iNodeID (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.CenterOfSphere": {
    "prefix": "CenterOfSphere",
    "text": "*Name:* MeshEdit.CreateNode.CenterOfSphere  \n*Desc:* Create node of center sphere  \n *Arg1:* crlNodeOrFace (Cursor List)  \n *Arg2:* iNodeID (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.Offset": {
    "prefix": "Offset",
    "text": "*Name:* MeshEdit.CreateNode.Offset  \n*Desc:* MeshEdit CreateNode CreateNodeNodeOffset  \n *Arg1:* vecOffset (Vector)  \n *Arg2:* iRep (Integer)  \n *Arg3:* crlNode (Cursor List)  \n *Arg4:* crCoord (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.CenterOfGravity": {
    "prefix": "CenterOfGravity",
    "text": "*Name:* MeshEdit.CreateNode.CenterOfGravity  \n*Desc:* create node Center Of Gravity  \n *Arg1:* iCreationType (Integer)  \n *Arg2:* iNodeID (Integer)  \n *Arg3:* dX (Double)  \n *Arg4:* dY (Double)  \n *Arg5:* dZ (Double)  \n *Arg6:* crlPart (Cursor List)  \n *Arg7:* crlBarPart (Cursor List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.ProjectToLine": {
    "prefix": "ProjectToLine",
    "text": "*Name:* MeshEdit.CreateNode.ProjectToLine  \n*Desc:* create node by projection to line  \n *Arg1:* crlTa (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.CreateNode.IntersectionNode": {
    "prefix": "IntersectionNode",
    "text": "*Name:* MeshEdit.CreateNode.IntersectionNode  \n*Desc:* create node by intersection node  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crlPart (Cursor List)  \n *Arg3:* crlEdge (Cursor List)  \n *Arg4:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.Point": {
    "prefix": "Point",
    "text": "*Name:* MeshEdit.MoveNode.Point  \n*Desc:* Move node(s) to an Face(Edge) Point position  \n *Arg1:* dX (Double)  \n *Arg2:* dY (Double)  \n *Arg3:* dZ (Double)  \n *Arg4:* ilNodeList (Integer List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.ProjectToLine": {
    "prefix": "ProjectToLine",
    "text": "*Name:* MeshEdit.MoveNode.ProjectToLine  \n*Desc:* move node by project to line  \n *Arg1:* crlRefNodes (Cursor List)  \n *Arg2:* crlObjNodes (Cursor List)  \n *Arg3:* iType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.ProjectToPlaneElem": {
    "prefix": "ProjectToPlaneElem",
    "text": "*Name:* MeshEdit.MoveNode.ProjectToPlaneElem  \n*Desc:* Move Node by Project to Plane(Elem)  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* crlElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.Equalize": {
    "prefix": "Equalize",
    "text": "*Name:* MeshEdit.MoveNode.Equalize  \n*Desc:* Move node by equalize  \n *Arg1:* crlEdge (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.NormalOffset": {
    "prefix": "NormalOffset",
    "text": "*Name:* MeshEdit.MoveNode.NormalOffset  \n*Desc:* Move node(s) in Normal Direction of plane  \n *Arg1:* dMagnitude (Double)  \n *Arg2:* ilNodeList (Integer List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.CoincidentNodes": {
    "prefix": "CoincidentNodes",
    "text": "*Name:* MeshEdit.MoveNode.CoincidentNodes  \n*Desc:* Coincident Nodes  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* dTol (Double)  \n *Arg3:* bDesOrder (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.AlongCylinder": {
    "prefix": "AlongCylinder",
    "text": "*Name:* MeshEdit.MoveNode.AlongCylinder  \n*Desc:* Move node along cylinder surface  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crlNode (Cursor List)  \n *Arg3:* dIrX (Double)  \n *Arg4:* dIrY (Double)  \n *Arg5:* dIrZ (Double)  \n *Arg6:* dCircleX (Double)  \n *Arg7:* dCircleY (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Move Nodes from Node to 3 nodes created Plane  \n *Arg1:* ilNodeList (Integer List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.MoveNodeOffset": {
    "prefix": "MoveNodeOffset",
    "text": "*Name:* MeshEdit.MoveNode.MoveNodeOffset  \n*Desc:* Unknown Description  \n *Arg1:* dDeltaX (Double)  \n *Arg2:* dDeltaY (Double)  \n *Arg3:* dDeltaZ (Double)  \n *Arg4:* crlNode (Cursor List)  \n *Arg5:* crCoord (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.RefineQuality": {
    "prefix": "RefineQuality",
    "text": "*Name:* MeshEdit.MoveNode.RefineQuality  \n*Desc:* MeshEdit RefineQuality  \n *Arg1:* iMetric (Integer)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* crlElem (Cursor List)  \n *Arg4:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.StraightenMidnodes": {
    "prefix": "StraightenMidnodes",
    "text": "*Name:* MeshEdit.MoveNode.StraightenMidnodes  \n*Desc:* move node by straighten_mid_nodes  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* crlEdge (Cursor List)  \n *Arg4:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.Offset": {
    "prefix": "Offset",
    "text": "*Name:* MeshEdit.MoveNode.Offset  \n*Desc:* MeshEdit MoveNode MoveNodeOffset  \n *Arg1:* dDeltaX (Double)  \n *Arg2:* dDeltaY (Double)  \n *Arg3:* dDeltaZ (Double)  \n *Arg4:* crCoord (Cursor)  \n *Arg5:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.Laplacian": {
    "prefix": "Laplacian",
    "text": "*Name:* MeshEdit.MoveNode.Laplacian  \n*Desc:*   \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* iType (Integer)  \n *Arg3:* bWithCADFollow (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.AlongEdge": {
    "prefix": "AlongEdge",
    "text": "*Name:* MeshEdit.MoveNode.AlongEdge  \n*Desc:*   \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* bMoveX (Boolean)  \n *Arg3:* bMoveY (Boolean)  \n *Arg4:* bMoveZ (Boolean)  \n *Arg5:* dPosX (Double)  \n *Arg6:* dPosY (Double)  \n *Arg7:* dPosZ (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.AlongDirection": {
    "prefix": "AlongDirection",
    "text": "*Name:* MeshEdit.MoveNode.AlongDirection  \n*Desc:*   \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* crElem (Cursor)  \n *Arg3:* crFace (Cursor)  \n *Arg4:* vecDirection (Vector)  \n *Arg5:* dMagnitude (Double)  \n *Arg6:* bDestination (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.CADFollows": {
    "prefix": "CADFollows",
    "text": "*Name:* MeshEdit.MoveNode.CADFollows  \n*Desc:*   \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* dMovedPosX (Double)  \n *Arg3:* dMovedPosY (Double)  \n *Arg4:* dMovedPosZ (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.Scale": {
    "prefix": "Scale",
    "text": "*Name:* MeshEdit.MoveNode.Scale  \n*Desc:* Move node scale  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* crlNodeOrigin (Cursor List)  \n *Arg3:* crCoord (Cursor)  \n *Arg4:* 10.0 (10.0)  \n *Arg5:* 10.0] (10.0])  \n *Arg6:* posDeltaXYZ (Position)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MoveNode.Absolute": {
    "prefix": "Absolute",
    "text": "*Name:* MeshEdit.MoveNode.Absolute  \n*Desc:* move node absolute  \n *Arg1:* dDeltaX (Double)  \n *Arg2:* dDeltaY (Double)  \n *Arg3:* dDeltaZ (Double)  \n *Arg4:* b1stCoord (B1ST_COORD)  \n *Arg5:* b2ndCoord (B2ND_COORD)  \n *Arg6:* b3rdCoord (B3RD_COORD)  \n *Arg7:* crlNode (Cursor List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.Face": {
    "prefix": "Face",
    "text": "*Name:* MeshEdit.Face  \n*Desc:* Make Mesh deformation  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crlFaceFixed (Cursor List)  \n *Arg3:* iOffsetType (Integer)  \n *Arg4:* crCoord (Cursor)  \n *Arg5:* 0.0 (0.0)  \n *Arg6:* 0.0] (0.0])  \n *Arg7:* dlOffset (Double List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.ElementConvert": {
    "prefix": "ElementConvert",
    "text": "*Name:* MeshEdit.ElementConvert  \n*Desc:* Element Conversion  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* iType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.Deform": {
    "prefix": "Deform",
    "text": "*Name:* MeshEdit.Deform  \n*Desc:* geometry deform  \n *Arg1:* crlFaceSrcObverse (Cursor List)  \n *Arg2:* crlFaceDstReverse (Cursor List)  \n *Arg3:* crlFaceSrcReverse (Cursor List)  \n *Arg4:* crlFaceDstObverse (Cursor List)  \n *Arg5:* crlFaceFixed (Cursor List)  \n *Arg6:* dDistEffect (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MirrorCopy": {
    "prefix": "MirrorCopy",
    "text": "*Name:* MeshEdit.MirrorCopy  \n*Desc:* mirror copy of surface mesh  \n *Arg1:* crlFace (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.DeleteNode": {
    "prefix": "DeleteNode",
    "text": "*Name:* MeshEdit.DeleteNode  \n*Desc:* Delete floating nodes in db  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* bRemoveVertex (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.FaceImprint": {
    "prefix": "FaceImprint",
    "text": "*Name:* MeshEdit.FaceImprint  \n*Desc:* import Nastran bdf file  \n *Arg1:* crlFaces (Cursor List)  \n *Arg2:* bMeshCopy (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.AdjustOrientation": {
    "prefix": "AdjustOrientation",
    "text": "*Name:* MeshEdit.AdjustOrientation  \n*Desc:* Adjust Orientation  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* crlElem (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.OneNode": {
    "prefix": "OneNode",
    "text": "*Name:* MeshEdit.OneNode  \n*Desc:* morphing one node  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* crlFaceFixed (Cursor List)  \n *Arg3:* bOffsetvector (Boolean)  \n *Arg4:* crCoord (Cursor)  \n *Arg5:* 1 (1)  \n *Arg6:* 0] (0])  \n *Arg7:* dlOffset (Double List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.SeparateNodes": {
    "prefix": "SeparateNodes",
    "text": "*Name:* MeshEdit.SeparateNodes  \n*Desc:* Separate nodes  \n *Arg1:* crlShareNodes (Cursor List)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* iKeepNodeIDsOn (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.RefineQuality": {
    "prefix": "RefineQuality",
    "text": "*Name:* MeshEdit.RefineQuality  \n*Desc:* Unknown Description  \n *Arg1:* iMetric (Integer)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* crlElem (Cursor List)  \n *Arg4:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.Import": {
    "prefix": "Import",
    "text": "*Name:* MeshEdit.Import  \n*Desc:* Move nodes deform  \n *Arg1:* iSolverType (Integer)  \n *Arg2:* strFilePath (String)  \n *Arg3:* iStep (Integer)  \n *Arg4:* dScale (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.RemoveSolidMesh": {
    "prefix": "RemoveSolidMesh",
    "text": "*Name:* MeshEdit.RemoveSolidMesh  \n*Desc:* Remove Solid Mesh  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* bConvFirst (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MergeNodes": {
    "prefix": "MergeNodes",
    "text": "*Name:* MeshEdit.MergeNodes  \n*Desc:* Merge nodes  \n *Arg1:* dTolerance (Double)  \n *Arg2:* iKeepType (Integer)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* bGroup (Boolean)  \n *Arg5:* bEquivalence (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.MeshCopy": {
    "prefix": "MeshCopy",
    "text": "*Name:* MeshEdit.MeshCopy  \n*Desc:* Mesh Copy Pattern  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.RibThickness": {
    "prefix": "RibThickness",
    "text": "*Name:* MeshEdit.RibThickness  \n*Desc:* Mesh Edit Morphing Rib Thickness  \n *Arg1:* crlFaceMove (Cursor List)  \n *Arg2:* crlFaceFixed (Cursor List)  \n *Arg3:* dMove (Double)  \n *Arg4:* dDistStrong (Double)  \n *Arg5:* dDistWeak (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.ChangePattern": {
    "prefix": "ChangePattern",
    "text": "*Name:* MeshEdit.ChangePattern  \n*Desc:* Element ChangePattern  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* iPatternType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.SurfaceMesh": {
    "prefix": "SurfaceMesh",
    "text": "*Name:* MeshEdit.SurfaceMesh  \n*Desc:* Element Conversion  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* iType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.SolidMesh": {
    "prefix": "SolidMesh",
    "text": "*Name:* MeshEdit.SolidMesh  \n*Desc:* Element Conversion  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* iType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MeshEdit.DividePartByRegion": {
    "prefix": "DividePartByRegion",
    "text": "*Name:* MeshEdit.DividePartByRegion  \n*Desc:* Divide Part By Region  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlBoundaryParts (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.CADProjection.Part": {
    "prefix": "Part",
    "text": "*Name:* Meshing.CADProjection.Part  \n*Desc:* CadProject for Part  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crCadPart (Cursor)  \n *Arg3:* crMeshedPart (Cursor)  \n *Arg4:* bForceProject (Boolean)  \n *Arg5:* bProjectCornerNodes (Boolean)  \n *Arg6:* bProjectMidNodes (Boolean)  \n *Arg7:* bIDcheck (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.CADProjection.Face": {
    "prefix": "Face",
    "text": "*Name:* Meshing.CADProjection.Face  \n*Desc:* CadProject for Face  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crCadPart (Cursor)  \n *Arg3:* crlMeshedFace (Cursor List)  \n *Arg4:* bForceProject (Boolean)  \n *Arg5:* bProjectCornerNodes (Boolean)  \n *Arg6:* bProjectMidNodes (Boolean)  \n *Arg7:* bIDcheck (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.CADProjection.FaceToFace": {
    "prefix": "FaceToFace",
    "text": "*Name:* Meshing.CADProjection.FaceToFace  \n*Desc:* CadProject for Fact to Face  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlCadFace (Cursor List)  \n *Arg3:* crlMeshedFace (Cursor List)  \n *Arg4:* bForceProject (Boolean)  \n *Arg5:* bProjectCornerNodes (Boolean)  \n *Arg6:* bProjectMidNodes (Boolean)  \n *Arg7:* bIDcheck (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.CADProjection.NodeToFace": {
    "prefix": "NodeToFace",
    "text": "*Name:* Meshing.CADProjection.NodeToFace  \n*Desc:* CadProject for Node to Face  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crlCadFace (Cursor List)  \n *Arg3:* crlMeshedNode (Cursor List)  \n *Arg4:* iDirection (Integer)  \n *Arg5:* iImproveQuality (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.CADProjection.NodeToEdge": {
    "prefix": "NodeToEdge",
    "text": "*Name:* Meshing.CADProjection.NodeToEdge  \n*Desc:* CadProject for Node to Edge  \n *Arg1:* iMethod (Integer)  \n *Arg2:* crCadEdge (Cursor)  \n *Arg3:* crlMeshedNode (Cursor List)  \n *Arg4:* iDirection (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalMeshing.FilletMapping": {
    "prefix": "FilletMapping",
    "text": "*Name:* Meshing.LocalMeshing.FilletMapping  \n*Desc:*   \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* iIsoDiv (Integer)  \n *Arg3:* dIsoSize (Double)  \n *Arg4:* dIsoError (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalMeshing.SelectFillet": {
    "prefix": "SelectFillet",
    "text": "*Name:* Meshing.LocalMeshing.SelectFillet  \n*Desc:* Unknown Description  \n *Arg1:* crlItems (Cursor List)  \n *Arg2:* dSelectWidthMin (Double)  \n *Arg3:* dSelectWidthMax (Double)  \n *Arg4:* dSelectRMin (Double)  \n *Arg5:* dSelectRMax (Double)  \n *Arg6:* dAngleMin (Double)  \n *Arg7:* dAngleMax (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalSetting.SearchTargetFaces": {
    "prefix": "SearchTargetFaces",
    "text": "*Name:* Meshing.LocalSetting.SearchTargetFaces  \n*Desc:* Search Target Faces for Local mesh setting  \n *Arg1:* iPartType (Integer)  \n *Arg2:* 0 (0)  \n *Arg3:* 0] (0])  \n *Arg4:* dlOrigin (Double List)  \n *Arg5:* 0.1 (0.1)  \n *Arg6:* 0.1] (0.1])  \n *Arg7:* dlLength (Double List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.Templates.TemplateCopy": {
    "prefix": "TemplateCopy",
    "text": "*Name:* Meshing.Templates.TemplateCopy  \n*Desc:* Template Copy local setting  \n *Arg1:* crlReferent (Cursor List)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iCopySub (Integer)  \n *Arg5:* dTolerance (Double)  \n *Arg6:* strSource (String)  \n *Arg7:* strTarget (String)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.BarMeshing": {
    "prefix": "BarMeshing",
    "text": "*Name:* Meshing.BarMeshing  \n*Desc:* meshing 1D edge/bar  \n *Arg1:* crlCadEdge (Cursor List)  \n *Arg2:* crlBarEdge (Cursor List)  \n *Arg3:* crlBarPart (Cursor List)  \n *Arg4:* dDocMeshSize (Double)  \n *Arg5:* iDocNumofElem (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.GridMesh": {
    "prefix": "GridMesh",
    "text": "*Name:* Meshing.GridMesh  \n*Desc:* Grid meshing  \n *Arg1:* listGridMesh (GRID_MESH List)  \n *Arg2:* bLocalsetting (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.SolidMeshing": {
    "prefix": "SolidMeshing",
    "text": "*Name:* Meshing.SolidMeshing  \n*Desc:* Solid Meshing  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* bTet10 (Boolean)  \n *Arg3:* dGradingFactor (Double)  \n *Arg4:* bGravCenter (Boolean)  \n *Arg5:* dStretchLimit (Double)  \n *Arg6:* iSpeedVsQual (Integer)  \n *Arg7:* iSpeedVsMem (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.SurfaceMeshing": {
    "prefix": "SurfaceMeshing",
    "text": "*Name:* Meshing.SurfaceMeshing  \n*Desc:* Surface Meshing  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* surfaceMesh (SURFACE_MESH)  \n *Arg3:* bUseSetting (Boolean)  \n *Arg4:* bFMesher (Boolean)  \n *Arg5:* iThreadNum (Integer)  \n *Arg6:* bRefData (Boolean)  \n *Arg7:* bMeshColor (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.SetAttib": {
    "prefix": "SetAttib",
    "text": "*Name:* Meshing.SetAttib  \n*Desc:* set attribute  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* surfaceMesh (SURFACE_MESH)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalRemesh.Solid": {
    "prefix": "Solid",
    "text": "*Name:* Meshing.LocalRemesh.Solid  \n*Desc:*   \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* dlCenter (Double List)  \n *Arg3:* dRadius (Double)  \n *Arg4:* dGradFactor (Double)  \n *Arg5:* dStrechLimit (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalRemesh.Surfase": {
    "prefix": "Surfase",
    "text": "*Name:* Meshing.LocalRemesh.Surfase  \n*Desc:* local surface remesh  \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* surfaceMesh (SURFACE_MESH)  \n *Arg3:* bUseSetting (Boolean)  \n *Arg4:* bGrading (Boolean)  \n *Arg5:* bFMesher (Boolean)  \n *Arg6:* iOverrideType (Integer)  \n *Arg7:* bKeepConnection (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalSettings.Edge": {
    "prefix": "Edge",
    "text": "*Name:* Meshing.LocalSettings.Edge  \n*Desc:* LocalSettings.Edge  \n *Arg1:* strName (String)  \n *Arg2:* localMesh (LOCAL_MESH)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* ilHardPointId (Integer List)  \n *Arg5:* veclHardPointXYZ (Vector List)  \n *Arg6:* crlHardPointTarget (Cursor List)  \n *Arg7:* crEditTarget (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalSettings.Face": {
    "prefix": "Face",
    "text": "*Name:* Meshing.LocalSettings.Face  \n*Desc:* LocalSettings.Face  \n *Arg1:* strName (String)  \n *Arg2:* localMesh (LOCAL_MESH)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* ilHardPointId (Integer List)  \n *Arg5:* veclHardPointXYZ (Vector List)  \n *Arg6:* crlHardPointTarget (Cursor List)  \n *Arg7:* crEditTarget (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalSettings.FaceElement": {
    "prefix": "FaceElement",
    "text": "*Name:* Meshing.LocalSettings.FaceElement  \n*Desc:* LocalSettings.FaceElement  \n *Arg1:* strName (String)  \n *Arg2:* localMesh (LOCAL_MESH)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* ilHardPointId (Integer List)  \n *Arg5:* veclHardPointXYZ (Vector List)  \n *Arg6:* crlHardPointTarget (Cursor List)  \n *Arg7:* crEditTarget (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalSettings.Model": {
    "prefix": "Model",
    "text": "*Name:* Meshing.LocalSettings.Model  \n*Desc:* LocalSettings.Model  \n *Arg1:* strName (String)  \n *Arg2:* localMesh (LOCAL_MESH)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* ilHardPointId (Integer List)  \n *Arg5:* veclHardPointXYZ (Vector List)  \n *Arg6:* crlHardPointTarget (Cursor List)  \n *Arg7:* crEditTarget (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalSettings.Part": {
    "prefix": "Part",
    "text": "*Name:* Meshing.LocalSettings.Part  \n*Desc:* LocalSettings.Part  \n *Arg1:* strName (String)  \n *Arg2:* localMesh (LOCAL_MESH)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* ilHardPointId (Integer List)  \n *Arg5:* veclHardPointXYZ (Vector List)  \n *Arg6:* crlHardPointTarget (Cursor List)  \n *Arg7:* crEditTarget (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Meshing.LocalSettings.Points": {
    "prefix": "Points",
    "text": "*Name:* Meshing.LocalSettings.Points  \n*Desc:* LocalSettings.Points  \n *Arg1:* strName (String)  \n *Arg2:* localMesh (LOCAL_MESH)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* ilHardPointId (Integer List)  \n *Arg5:* veclHardPointXYZ (Vector List)  \n *Arg6:* crlHardPointTarget (Cursor List)  \n *Arg7:* crEditTarget (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlane.AdjustThickness": {
    "prefix": "AdjustThickness",
    "text": "*Name:* MidPlane.AdjustThickness  \n*Desc:* Adjust thickness of midplane  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* dRatio (Double)  \n *Arg3:* bAdjustFaceThick (Boolean)  \n *Arg4:* bAdjustPropThick (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlane.FaceCross": {
    "prefix": "FaceCross",
    "text": "*Name:* MidPlane.FaceCross  \n*Desc:* Face Cross  \n *Arg1:* crlBodies (Cursor List)  \n *Arg2:* crlFaces (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlane.CreateThickProps": {
    "prefix": "CreateThickProps",
    "text": "*Name:* MidPlane.CreateThickProps  \n*Desc:* create thick properties for mid-plane  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* dThickDiff (Double)  \n *Arg3:* dMaxThick (Double)  \n *Arg4:* dMinThick (Double)  \n *Arg5:* crMatMembrane (Cursor)  \n *Arg6:* crMatBend (Cursor)  \n *Arg7:* crMatShear (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlane.FindMidPlane": {
    "prefix": "FindMidPlane",
    "text": "*Name:* MidPlane.FindMidPlane  \n*Desc:* Unknown Description  \n *Arg1:*  ()  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.Edge.Nodes": {
    "prefix": "Nodes",
    "text": "*Name:* MidPlaneEdit.Edge.Nodes  \n*Desc:* Edit mid-plane with edge nodes  \n *Arg1:* crlNode (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.ExtendFace.CylinderFace": {
    "prefix": "CylinderFace",
    "text": "*Name:* MidPlaneEdit.ExtendFace.CylinderFace  \n*Desc:* project an edge to face to get a new edge  \n *Arg1:* crlExtFace (Cursor List)  \n *Arg2:* crRefFace (Cursor)  \n *Arg3:* crEdge (Cursor)  \n *Arg4:* iExtendType (Integer)  \n *Arg5:* iFaceType (Integer)  \n *Arg6:* iMethod (Integer)  \n *Arg7:* dParaAngleOffset (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.ExtendFace.PlanarFace": {
    "prefix": "PlanarFace",
    "text": "*Name:* MidPlaneEdit.ExtendFace.PlanarFace  \n*Desc:* Extend Face  \n *Arg1:* bIType (Boolean)  \n *Arg2:* crExtFace (Cursor)  \n *Arg3:* crRefFace (Cursor)  \n *Arg4:* crEdge (Cursor)  \n *Arg5:* iFaceType (Integer)  \n *Arg6:* iExtendType (Integer)  \n *Arg7:* iMethod (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.Face.FaceExtendtoFace": {
    "prefix": "FaceExtendtoFace",
    "text": "*Name:* MidPlaneEdit.Face.FaceExtendtoFace  \n*Desc:* add face by face extend to face  \n *Arg1:* crlExtFaces (Cursor List)  \n *Arg2:* crlRefFaces (Cursor List)  \n *Arg3:* bMergeFace (Boolean)  \n *Arg4:* bMergeEdge (Boolean)  \n *Arg5:* dMergeEdgeAngle (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.Face.FaceExtendToIntersection": {
    "prefix": "FaceExtendToIntersection",
    "text": "*Name:* MidPlaneEdit.Face.FaceExtendToIntersection  \n*Desc:* Face Extend To Intersection  \n *Arg1:* crEdge0 (Cursor)  \n *Arg2:* crEdge1 (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.Face.EdgesToEdges": {
    "prefix": "EdgesToEdges",
    "text": "*Name:* MidPlaneEdit.Face.EdgesToEdges  \n*Desc:* add face by edges  \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* bImprint (Boolean)  \n *Arg3:* bMultiEdges (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.Manual.vecOffset": {
    "prefix": "vecOffset",
    "text": "*Name:* MidPlaneEdit.Manual.vecOffset  \n*Desc:* Unknown Description  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crPart (Cursor)  \n *Arg3:* dOffset (Double)  \n *Arg4:* bCyl (Boolean)  \n *Arg5:* strNewPartName (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.Manual.MidByPair": {
    "prefix": "MidByPair",
    "text": "*Name:* MidPlaneEdit.Manual.MidByPair  \n*Desc:* Midplane Manual MidByPair  \n *Arg1:* crlBaseFaces (Cursor List)  \n *Arg2:* crlPairFaces (Cursor List)  \n *Arg3:* crlRefFaces (Cursor List)  \n *Arg4:* crPart (Cursor)  \n *Arg5:* bMergeFaces (Boolean)  \n *Arg6:* bExtendFaces (Boolean)  \n *Arg7:* bHideFaces (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace": {
    "prefix": "ProjectEdgeToFace",
    "text": "*Name:* MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace  \n*Desc:* project an edge to face to get a new edge  \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* bExtendEdge (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.AddItems.Edge.FaceTwoFace": {
    "prefix": "FaceTwoFace",
    "text": "*Name:* MidPlaneEdit.AddItems.Edge.FaceTwoFace  \n*Desc:* Exent face to face  \n *Arg1:* crRefFace (Cursor)  \n *Arg2:* crExtFace (Cursor)  \n *Arg3:* iExtendType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.AddItems.Face.EFExtendFreeEdge": {
    "prefix": "EFExtendFreeEdge",
    "text": "*Name:* MidPlaneEdit.AddItems.Face.EFExtendFreeEdge  \n*Desc:* Create new face by extend free edge to a destination face  \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* bMergeFace (Boolean)  \n *Arg4:* bMergeEdge (Boolean)  \n *Arg5:* bUseNeighDir (Boolean)  \n *Arg6:* dMergeEdgeAngle (Double)  \n *Arg7:* bMultiEF (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MidPlaneEdit.AddItems.Face.EFProject": {
    "prefix": "EFProject",
    "text": "*Name:* MidPlaneEdit.AddItems.Face.EFProject  \n*Desc:* Creat new face by project edge to destination face  \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* bMergeFace (Boolean)  \n *Arg4:* bMergeEdge (Boolean)  \n *Arg5:* dMergeEdgeAngle (Double)  \n *Arg6:* bMultiEF (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MMCCarACTools.ACModelCreationTools.MeshedFace": {
    "prefix": "MeshedFace",
    "text": "*Name:* MMCCarACTools.ACModelCreationTools.MeshedFace  \n*Desc:*   \n *Arg1:* crlItem1 (Cursor List)  \n *Arg2:* crlItem2 (Cursor List)  \n *Arg3:* crlItem3 (Cursor List)  \n *Arg4:* crlPart (Cursor List)  \n *Arg5:* iType (Integer)  \n *Arg6:* dMeshSise (Double)  \n *Arg7:* bMergeTol (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MMCCarACTools.ClearanceElement.Connect": {
    "prefix": "Connect",
    "text": "*Name:* MMCCarACTools.ClearanceElement.Connect  \n*Desc:* MMCCarACTools ClearanceElement Connect  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crlElem (Cursor List)  \n *Arg3:* iConnectionMethod (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MMCCarACTools.ClearanceElement.Edit": {
    "prefix": "Edit",
    "text": "*Name:* MMCCarACTools.ClearanceElement.Edit  \n*Desc:* Edit clearance elment  \n *Arg1:* dDx (Double)  \n *Arg2:* dDy (Double)  \n *Arg3:* dDz (Double)  \n *Arg4:* dLx (Double)  \n *Arg5:* dLy (Double)  \n *Arg6:* dLz (Double)  \n *Arg7:* crlTarget (Cursor List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MufflerHA.CreateEdge.PerpendicularLineToEdge": {
    "prefix": "PerpendicularLineToEdge",
    "text": "*Name:* MufflerHA.CreateEdge.PerpendicularLineToEdge  \n*Desc:* Unknown Description  \n *Arg1:* crNode (Cursor)  \n *Arg2:* crEdge (Cursor)  \n *Arg3:* crlFace (Cursor List)  \n *Arg4:* bBreakFace (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MufflerHA.CreateEdgeClassic.ProjectLine": {
    "prefix": "ProjectLine",
    "text": "*Name:* MufflerHA.CreateEdgeClassic.ProjectLine  \n*Desc:* create edge  \n *Arg1:* ilAiedgeidForMacro (Integer List)  \n *Arg2:* ilAifaceidForMacro (Integer List)  \n *Arg3:* bDivideFace (Boolean)  \n *Arg4:* crlAiparttargetForMarco (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MufflerHA.CopyMeshCount": {
    "prefix": "CopyMeshCount",
    "text": "*Name:* MufflerHA.CopyMeshCount  \n*Desc:*   \n *Arg1:* crlMasterEdge (Cursor List)  \n *Arg2:* crlSlaveEdge (Cursor List)  \n *Arg3:* strBaseName (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MufflerT.SpecialModeling.Rod.Rod": {
    "prefix": "Rod",
    "text": "*Name:* MufflerT.SpecialModeling.Rod.Rod  \n*Desc:* create rod  \n *Arg1:* crlNode (Cursor List)  \n *Arg2:* dRadius (Double)  \n *Arg3:* iType (Integer)  \n *Arg4:* dMeshSize (Double)  \n *Arg5:* dStartDist (Double)  \n *Arg6:* dWeldDist (Double)  \n *Arg7:* iDivNumber (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MuxWeld.CreateWeld.Auto": {
    "prefix": "Auto",
    "text": "*Name:* MuxWeld.CreateWeld.Auto  \n*Desc:* Auto create weld  \n *Arg1:* iIconnectattributeMethod (Integer)  \n *Arg2:* strStrconnectattributeName (String)  \n *Arg3:* crlMasterTarget (Cursor List)  \n *Arg4:* crlSlaveTarget (Cursor List)  \n *Arg5:* iIconnectattributeCoordsys (Integer)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MuxWeld.CreateWeld.CreateBeadWeld": {
    "prefix": "CreateBeadWeld",
    "text": "*Name:* MuxWeld.CreateWeld.CreateBeadWeld  \n*Desc:* Unknown Description  \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* crlPrjtedEdge (Cursor List)  \n *Arg3:* crlPart (Cursor List)  \n *Arg4:* dTol (Double)  \n *Arg5:* dRatio (Double)  \n *Arg6:* crRefElem (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MuxWeld.DefineSequence.Single": {
    "prefix": "Single",
    "text": "*Name:* MuxWeld.DefineSequence.Single  \n*Desc:* Define Sequence  \n *Arg1:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "MuxWeld.MeshingPass": {
    "prefix": "MeshingPass",
    "text": "*Name:* MuxWeld.MeshingPass  \n*Desc:* sweep cross section to create welding  \n *Arg1:* crPart (Cursor)  \n *Arg2:* crlEdge (Cursor List)  \n *Arg3:* dMeshSize (Double)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* create Property 3D Weld Bead  \n *Arg1:* strName (String)  \n *Arg2:* crMaterial (Cursor)  \n *Arg3:* crlTarget (Cursor List)  \n *Arg4:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "NSModeling.NSModeling_Close_Hole": {
    "prefix": "NSModeling_Close_Hole",
    "text": "*Name:* NSModeling.NSModeling_Close_Hole  \n*Desc:* NSModeling NSModeling_Close_Hole  \n *Arg1:* iType (Integer)  \n *Arg2:* dMaxLength (Double)  \n *Arg3:* bMergeFaces (Boolean)  \n *Arg4:* bSetCenterPoint (Boolean)  \n *Arg5:* crlNode (Cursor List)  \n *Arg6:* crlPart (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "OasisAWizard.LocalMeshing.FilletMapMeshing": {
    "prefix": "FilletMapMeshing",
    "text": "*Name:* OasisAWizard.LocalMeshing.FilletMapMeshing  \n*Desc:*   \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* dMinLength (Double)  \n *Arg4:* dMaxLength (Double)  \n *Arg5:* dMinRadius (Double)  \n *Arg6:* dMaxRadius (Double)  \n *Arg7:* bConvex (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* import Nastran op2 mesh  \n *Arg1:* strlFilePaths (String List)  \n *Arg2:* iImportType (Integer)  \n *Arg3:* dFaceAngle (Double)  \n *Arg4:* dEdgeAngle (Double)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* import Nastran op2 post job  \n *Arg1:* strName (String)  \n *Arg2:* strlPaths (String List)  \n *Arg3:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Post.ImportResults.ImportTsdbMesh": {
    "prefix": "ImportTsdbMesh",
    "text": "*Name:* Post.ImportResults.ImportTsdbMesh  \n*Desc:* import tsdb mesh  \n *Arg1:* strTsdbFilePath (String)  \n *Arg2:* strBtxFilePath (String)  \n *Arg3:* iImportType (Integer)  \n *Arg4:* dFaceAngle (Double)  \n *Arg5:* dEdgeAngle (Double)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* import Nastran HDF5Mesh file  \n *Arg1:* strlFilePaths (String List)  \n *Arg2:* iImportType (Integer)  \n *Arg3:* dFaceAngle (Double)  \n *Arg4:* dEdgeAngle (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Post.ImportResults.ADVC": {
    "prefix": "ADVC",
    "text": "*Name:* Post.ImportResults.ADVC  \n*Desc:* Unknown Description  \n *Arg1:* strlPath (String List)  \n *Arg2:* iImportType (Integer)  \n *Arg3:* dFaceAngle (Double)  \n *Arg4:* dEdgeAngle (Double)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Post ImportResults ADVC2PostJob  \n *Arg1:* strName (String)  \n *Arg2:* strlResultFolderPaths (String List)  \n *Arg3:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Import Nastran HDF5PostJob file  \n *Arg1:* strName (String)  \n *Arg2:* strlPaths (String List)  \n *Arg3:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.ElemRelatedInfo.Shell": {
    "prefix": "Shell",
    "text": "*Name:* Properties.ElemRelatedInfo.Shell  \n*Desc:* Set Shell Parameter  \n *Arg1:* listErishellThetaProp (ERISHELL_THETA_PROP List)  \n *Arg2:* listErishellCsProp (ERISHELL_CS_PROP List)  \n *Arg3:* listErishellZoffsProp (ERISHELL_ZOFFS_PROP List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.ElemRelatedInfo.Conn": {
    "prefix": "Conn",
    "text": "*Name:* Properties.ElemRelatedInfo.Conn  \n*Desc:* Set Shell Parameter  \n *Arg1:* listEricontEndProp (ERICONT_END_PROP List)  \n *Arg2:* listEricontOriVecProp (ERICONT_ORI_VEC_PROP List)  \n *Arg3:* listCidProp (CID_PROP List)  \n *Arg4:* listEricontDamperLocProp (ERICONT_DAMPER_LOC_PROP List)  \n *Arg5:* listOcidProp (OCID_PROP List)  \n *Arg6:* listDamperOffsetVecs (DAMPER_OFFSET_VECS List)  \n *Arg7:* listEricontNodeidProp (ERICONT_NODEID_PROP List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.ElemRelatedInfo.Rod": {
    "prefix": "Rod",
    "text": "*Name:* Properties.ElemRelatedInfo.Rod  \n*Desc:* Set Rod Parameter  \n *Arg1:* listEricontEndProp (ERICONT_END_PROP List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.ElemRelatedInfo.Beam": {
    "prefix": "Beam",
    "text": "*Name:* Properties.ElemRelatedInfo.Beam  \n*Desc:* Set Beam Parameter  \n *Arg1:* listEribeamEndProp (ERIBEAM_END_PROP List)  \n *Arg2:* listEribeamOriVecProp (ERIBEAM_ORI_VEC_PROP List)  \n *Arg3:* listEribeamOriNodeidProp (ERIBEAM_ORI_NODEID_PROP List)  \n *Arg4:* listEribeamOffsetVecA (ERIBEAM_OFFSET_VEC_A List)  \n *Arg5:* listEribeamOffsetVecB (ERIBEAM_OFFSET_VEC_B List)  \n *Arg6:* listEribeamPinAProp (ERIBEAM_PIN_APROP List)  \n *Arg7:* listEribeamPinBProp (ERIBEAM_PIN_BPROP List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.ElemRelatedInfo.Bar": {
    "prefix": "Bar",
    "text": "*Name:* Properties.ElemRelatedInfo.Bar  \n*Desc:* Set Bar Parameter  \n *Arg1:* listEribeamEndProp (ERIBEAM_END_PROP List)  \n *Arg2:* listEribeamOriVecProp (ERIBEAM_ORI_VEC_PROP List)  \n *Arg3:* listEribeamOriNodeidProp (ERIBEAM_ORI_NODEID_PROP List)  \n *Arg4:* listEribeamOffsetVecA (ERIBEAM_OFFSET_VEC_A List)  \n *Arg5:* listEribeamOffsetVecB (ERIBEAM_OFFSET_VEC_B List)  \n *Arg6:* listEribeamPinAProp (ERIBEAM_PIN_APROP List)  \n *Arg7:* listEribeamPinBProp (ERIBEAM_PIN_BPROP List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.ElemRelatedInfo.Gap": {
    "prefix": "Gap",
    "text": "*Name:* Properties.ElemRelatedInfo.Gap  \n*Desc:* Set Shell Parameter  \n *Arg1:* listEricontEndProp (ERICONT_END_PROP List)  \n *Arg2:* listEricontOriVecProp (ERICONT_ORI_VEC_PROP List)  \n *Arg3:* listCidProp (CID_PROP List)  \n *Arg4:* listEricontDamperLocProp (ERICONT_DAMPER_LOC_PROP List)  \n *Arg5:* listOcidProp (OCID_PROP List)  \n *Arg6:* listDamperOffsetVecs (DAMPER_OFFSET_VECS List)  \n *Arg7:* listEricontNodeidProp (ERICONT_NODEID_PROP List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.ElemRelatedInfo.Bush": {
    "prefix": "Bush",
    "text": "*Name:* Properties.ElemRelatedInfo.Bush  \n*Desc:* Set Shell Parameter  \n *Arg1:* listEricontEndProp (ERICONT_END_PROP List)  \n *Arg2:* listEricontOriVecProp (ERICONT_ORI_VEC_PROP List)  \n *Arg3:* listCidProp (CID_PROP List)  \n *Arg4:* listEricontDamperLocProp (ERICONT_DAMPER_LOC_PROP List)  \n *Arg5:* listOcidProp (OCID_PROP List)  \n *Arg6:* listDamperOffsetVecs (DAMPER_OFFSET_VECS List)  \n *Arg7:* listEricontNodeidProp (ERICONT_NODEID_PROP List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Material.Add": {
    "prefix": "Add",
    "text": "*Name:* Properties.Material.Add  \n*Desc:* Unknown Description  \n *Arg1:* strMaterialName (String)  \n *Arg2:* listMaterialProperty (MATERIAL_PROPERTY List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Material.Modify": {
    "prefix": "Modify",
    "text": "*Name:* Properties.Material.Modify  \n*Desc:* Unknown Description  \n *Arg1:* strMaterialID (String)  \n *Arg2:* listMaterialProperty (MATERIAL_PROPERTY List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Material.Delete": {
    "prefix": "Delete",
    "text": "*Name:* Properties.Material.Delete  \n*Desc:* Unknown Description  \n *Arg1:* strMaterialID (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Section.Import": {
    "prefix": "Import",
    "text": "*Name:* Properties.Section.Import  \n*Desc:* import 1D Section  \n *Arg1:* strImportPath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Section.ModifyGeneral": {
    "prefix": "ModifyGeneral",
    "text": "*Name:* Properties.Section.ModifyGeneral  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crSection (Cursor)  \n *Arg3:* iSecType (Integer)  \n *Arg4:* iGeneralType (Integer)  \n *Arg5:* dA (Double)  \n *Arg6:* dB (Double)  \n *Arg7:* dH (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Section.ModifyLibrary": {
    "prefix": "ModifyLibrary",
    "text": "*Name:* Properties.Section.ModifyLibrary  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crSection (Cursor)  \n *Arg3:* iType (Integer)  \n *Arg4:* iLibType (Integer)  \n *Arg5:* dDimSize0 (Double)  \n *Arg6:* dDimSize1 (Double)  \n *Arg7:* dDimSize2 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Section.ModifySketcher": {
    "prefix": "ModifySketcher",
    "text": "*Name:* Properties.Section.ModifySketcher  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* crSection (Cursor)  \n *Arg3:* iType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Section.Export": {
    "prefix": "Export",
    "text": "*Name:* Properties.Section.Export  \n*Desc:* export 1D section to xml file  \n *Arg1:* strExportSavePath (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Section.Delete": {
    "prefix": "Delete",
    "text": "*Name:* Properties.Section.Delete  \n*Desc:* Properties Section Delete  \n *Arg1:* crlSection (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Section.AddGeneral": {
    "prefix": "AddGeneral",
    "text": "*Name:* Properties.Section.AddGeneral  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* iSecType (Integer)  \n *Arg3:* iSecGenType (Integer)  \n *Arg4:* dDsecGensizeA (Double)  \n *Arg5:* dDsecGensizeB (Double)  \n *Arg6:* dDsecGensizeH (Double)  \n *Arg7:* dDsecGensizeT1 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Section.AddLibrary": {
    "prefix": "AddLibrary",
    "text": "*Name:* Properties.Section.AddLibrary  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* iSecType (Integer)  \n *Arg3:* iLibType (Integer)  \n *Arg4:* dDim1 (Double)  \n *Arg5:* dDim2 (Double)  \n *Arg6:* dDim3 (Double)  \n *Arg7:* dDim4 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Section.AddSketcher": {
    "prefix": "AddSketcher",
    "text": "*Name:* Properties.Section.AddSketcher  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* iSecType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Cohesive": {
    "prefix": "Cohesive",
    "text": "*Name:* Properties.Cohesive  \n*Desc:* create property 3d cohesive  \n *Arg1:* strName (String)  \n *Arg2:* crMaterial (Cursor)  \n *Arg3:* iResponse (Integer)  \n *Arg4:* bSpecifyThick (Boolean)  \n *Arg5:* dInitialThick (Double)  \n *Arg6:* crlTarget (Cursor List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Gasket": {
    "prefix": "Gasket",
    "text": "*Name:* Properties.Gasket  \n*Desc:* create property 3d gasket  \n *Arg1:* strName (String)  \n *Arg2:* crMaterial (Cursor)  \n *Arg3:* dThickX (Double)  \n *Arg4:* dThickY (Double)  \n *Arg5:* dThickZ (Double)  \n *Arg6:* crlTarget (Cursor List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Shell": {
    "prefix": "Shell",
    "text": "*Name:* Properties.Shell  \n*Desc:* create shell property  \n *Arg1:* strName (String)  \n *Arg2:* iPID (Integer)  \n *Arg3:* crMatMembrane (Cursor)  \n *Arg4:* crMatBend (Cursor)  \n *Arg5:* crMatShear (Cursor)  \n *Arg6:* crMatCoupl (Cursor)  \n *Arg7:* dMatOrient1 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.PropertyTable": {
    "prefix": "PropertyTable",
    "text": "*Name:* Properties.PropertyTable  \n*Desc:* renumber property/material ID  \n *Arg1:* listRenumberProp (RENUMBER_PROP List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Beam": {
    "prefix": "Beam",
    "text": "*Name:* Properties.Beam  \n*Desc:* add property of 1D beam  \n *Arg1:* strNewName (String)  \n *Arg2:* iPId (Integer)  \n *Arg3:* crSection (Cursor)  \n *Arg4:* iShapeDataType (Integer)  \n *Arg5:* crMat (Cursor)  \n *Arg6:* dArea (Double)  \n *Arg7:* dlVecOrient (Double List)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Rod": {
    "prefix": "Rod",
    "text": "*Name:* Properties.Rod  \n*Desc:* create 1D rod property  \n *Arg1:* strName (String)  \n *Arg2:* iId (Integer)  \n *Arg3:* crSection (Cursor)  \n *Arg4:* crMat (Cursor)  \n *Arg5:* dArea (Double)  \n *Arg6:* dTorConst (Double)  \n *Arg7:* dTorStressCoeff (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:*   \n *Arg1:* strName (String)  \n *Arg2:* iId (Integer)  \n *Arg3:* crSection (Cursor)  \n *Arg4:* crMat (Cursor)  \n *Arg5:* vecOrient (Vector)  \n *Arg6:* crlTarget (Cursor List)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Solid": {
    "prefix": "Solid",
    "text": "*Name:* Properties.Solid  \n*Desc:* create property solid  \n *Arg1:* strName (String)  \n *Arg2:* iPID (Integer)  \n *Arg3:* crMaterial (Cursor)  \n *Arg4:* iCordM (Integer)  \n *Arg5:* iIN (Integer)  \n *Arg6:* iOutLoc (Integer)  \n *Arg7:* iISOP (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* Create 1D Property Sketcher Section  \n *Arg1:* strName (String)  \n *Arg2:* iSecType (Integer)  \n *Arg3:* iSecGentype (Integer)  \n *Arg4:* dSecGensizeA (Double)  \n *Arg5:* dSecGensizeB (Double)  \n *Arg6:* dSecGensizeH (Double)  \n *Arg7:* dSecGensizeT1 (Double)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.Composite": {
    "prefix": "Composite",
    "text": "*Name:* Properties.Composite  \n*Desc:* Create 2D Composite Material Shell Property  \n *Arg1:* strName (String)  \n *Arg2:* iDFT (Integer)  \n *Arg3:* dGE (Double)  \n *Arg4:* iDLAM (Integer)  \n *Arg5:* crMat (Cursor)  \n *Arg6:* dNSM (Double)  \n *Arg7:* iDPID (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.BAR": {
    "prefix": "BAR",
    "text": "*Name:* Properties.BAR  \n*Desc:* create 1D bar property  \n *Arg1:* strName (String)  \n *Arg2:* iId (Integer)  \n *Arg3:* crSection (Cursor)  \n *Arg4:* iShapeDataType (Integer)  \n *Arg5:* crDatacrMat (Cursor)  \n *Arg6:* dDatadArea (Double)  \n *Arg7:* 0 (0)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.ThicknessDistribution": {
    "prefix": "ThicknessDistribution",
    "text": "*Name:* Properties.ThicknessDistribution  \n*Desc:* Properties view Thickness Distribution  \n *Arg1:* dMax (Double)  \n *Arg2:* dMin (Double)  \n *Arg3:* iByEach (Integer)  \n *Arg4:* dlThicknessValueSet (Double List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Properties.RigidBody": {
    "prefix": "RigidBody",
    "text": "*Name:* Properties.RigidBody  \n*Desc:* assign properties rigid body  \n *Arg1:* strName (String)  \n *Arg2:* iId (Integer)  \n *Arg3:* iRefNodeId (Integer)  \n *Arg4:* crlTarget (Cursor List)  \n *Arg5:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "SNOnePush.DropTest.CalcTimestep": {
    "prefix": "CalcTimestep",
    "text": "*Name:* SNOnePush.DropTest.CalcTimestep  \n*Desc:* Used to calculate time step for drop test function  \n *Arg1:* dRelevantElemRate (Double)  \n *Arg2:* dChangeMassRage (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "SNOnePush.DropTest.UpdateFloor": {
    "prefix": "UpdateFloor",
    "text": "*Name:* SNOnePush.DropTest.UpdateFloor  \n*Desc:* Assemble cylinder layer  \n *Arg1:* strName (String)  \n *Arg2:* iDir (Integer)  \n *Arg3:* dRopHeight (Double)  \n *Arg4:* dSolutionTime (Double)  \n *Arg5:* iNumberOutput (Integer)  \n *Arg6:* dContactFriction (Double)  \n *Arg7:* iRotAxis (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "SNOnePush.DropTest.DropRotation": {
    "prefix": "DropRotation",
    "text": "*Name:* SNOnePush.DropTest.DropRotation  \n*Desc:* Assemble cylinder layer  \n *Arg1:* strName (String)  \n *Arg2:* iDir (Integer)  \n *Arg3:* dRopHeight (Double)  \n *Arg4:* dSolutionTime (Double)  \n *Arg5:* iNumberOutput (Integer)  \n *Arg6:* dContactFriction (Double)  \n *Arg7:* iRotAxis (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "SNOnePush.CADImport": {
    "prefix": "CADImport",
    "text": "*Name:* SNOnePush.CADImport  \n*Desc:* import CAD model  \n *Arg1:* dDsurfaceplaneTolerance (Double)  \n *Arg2:* dDsurfaceplaneAngle (Double)  \n *Arg3:* dMaxFacetWidth (Double)  \n *Arg4:* bBnxMultipart (Boolean)  \n *Arg5:* dChordHeightTolerance (Double)  \n *Arg6:* dAngleToleranceDegree (Double)  \n *Arg7:* iConvertIsolatedCurve (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "SNOnePush.DropTestSNOnePush": {
    "prefix": "DropTestSNOnePush",
    "text": "*Name:* SNOnePush.DropTestSNOnePush  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* iDir (Integer)  \n *Arg3:* dRopHeight (Double)  \n *Arg4:* dSolutionTime (Double)  \n *Arg5:* iNumOutput (Integer)  \n *Arg6:* dContactFriction (Double)  \n *Arg7:* iRotAxis (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "SNOnePush.AutoSweepClosedLoopShaped": {
    "prefix": "AutoSweepClosedLoopShaped",
    "text": "*Name:* SNOnePush.AutoSweepClosedLoopShaped  \n*Desc:* Make hexa for closed loop shaped  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* dMeshSize (Double)  \n *Arg3:* dLengthSize (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "StiffCalc.Force": {
    "prefix": "Force",
    "text": "*Name:* StiffCalc.Force  \n*Desc:* create NormalUnityForce  \n *Arg1:* strName (String)  \n *Arg2:* poslForce (Position List)  \n *Arg3:* poslMoment (Position List)  \n *Arg4:* iEnArrowDir (Integer)  \n *Arg5:* iDistributionMethod (Integer)  \n *Arg6:* crCurCoord (Cursor)  \n *Arg7:* crTable (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "SZOnepushReliability.Assembly.CreateWeld": {
    "prefix": "CreateWeld",
    "text": "*Name:* SZOnepushReliability.Assembly.CreateWeld  \n*Desc:* Create welding  \n *Arg1:* crlWelds (Cursor List)  \n *Arg2:* dMeshSize (Double)  \n *Arg3:* iRrate (Integer)  \n *Arg4:* dFilletRadius (Double)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "SZOnepushReliability.Assembly.ContactSurface": {
    "prefix": "ContactSurface",
    "text": "*Name:* SZOnepushReliability.Assembly.ContactSurface  \n*Desc:* Contact surface  \n *Arg1:* crlSrcFace (Cursor List)  \n *Arg2:* crlTarPart (Cursor List)  \n *Arg3:* dTolerance (Double)  \n *Arg4:* iLayer (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "SZOnepushReliability.MeshEdit.FilletMapping": {
    "prefix": "FilletMapping",
    "text": "*Name:* SZOnepushReliability.MeshEdit.FilletMapping  \n*Desc:* Fillet mapping  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* dMinRadius (Double)  \n *Arg4:* dMaxRadius (Double)  \n *Arg5:* dMinAngle (Double)  \n *Arg6:* dMaxAngle (Double)  \n *Arg7:* bConvex (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "SZOnepushReliability.AlignMidNode": {
    "prefix": "AlignMidNode",
    "text": "*Name:* SZOnepushReliability.AlignMidNode  \n*Desc:* align mid-nodes  \n *Arg1:* crlSource (Cursor List)  \n *Arg2:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Test.Connection.RRod": {
    "prefix": "RRod",
    "text": "*Name:* Test.Connection.RRod  \n*Desc:* create RRod  \n *Arg1:* rbarConnection (RBAR_CONNECTION)  \n *Arg2:* iUlDOFs (Integer)  \n *Arg3:* dTol (Double)  \n *Arg4:* crlMasterTarget (Cursor List)  \n *Arg5:* crlSlaveTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Test.Muffler.ProjectLineForWeld": {
    "prefix": "ProjectLineForWeld",
    "text": "*Name:* Test.Muffler.ProjectLineForWeld  \n*Desc:* Projec line for weld  \n *Arg1:* crlEdge (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Test.ZGeometryTest.IntersectionCheck": {
    "prefix": "IntersectionCheck",
    "text": "*Name:* Test.ZGeometryTest.IntersectionCheck  \n*Desc:* Intersection check  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* crlElem (Cursor List)  \n *Arg4:* iType (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Test.ZGeometryTest.ShellAssy": {
    "prefix": "ShellAssy",
    "text": "*Name:* Test.ZGeometryTest.ShellAssy  \n*Desc:* Unknown Description  \n *Arg1:* taPart (TA_PART)  \n *Arg2:* crlFace (Cursor List)  \n *Arg3:* _iMeshType (_I_MESH_TYPE)  \n *Arg4:* _bSelfIntersection (_B_SELF_INTERSECTION)  \n *Arg5:* _iMethod (_I_METHOD)  \n *Arg6:* _dGapTol (_D_GAP_TOL)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Test.FindFacesInPart": {
    "prefix": "FindFacesInPart",
    "text": "*Name:* Test.FindFacesInPart  \n*Desc:* Find faces in part by typical description  \n *Arg1:* crPart (Cursor)  \n *Arg2:* strIdentical (String)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Test.CreateElementForWelding": {
    "prefix": "CreateElementForWelding",
    "text": "*Name:* Test.CreateElementForWelding  \n*Desc:* Create weld elements  \n *Arg1:* crlSrcElems (Cursor List)  \n *Arg2:* crlDstElems (Cursor List)  \n *Arg3:* crlSideElems (Cursor List)  \n *Arg4:* crlPart (Cursor List)  \n *Arg5:* crMaterial (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Toolbar.Undo": {
    "prefix": "Undo",
    "text": "*Name:* Toolbar.Undo  \n*Desc:* Undo  \n *Arg1:* iCntUndo (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Toolbar.Redo": {
    "prefix": "Redo",
    "text": "*Name:* Toolbar.Redo  \n*Desc:* Redo  \n *Arg1:* iCntRedo (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.BySelection.SelectionOrder": {
    "prefix": "SelectionOrder",
    "text": "*Name:* Tools.BySelection.SelectionOrder  \n*Desc:* Renumber by selection order  \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* iType (Integer)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iStartID (Integer)  \n *Arg5:* iIncrementStep (Integer)  \n *Arg6:* bAscending (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.BySelection.Position": {
    "prefix": "Position",
    "text": "*Name:* Tools.BySelection.Position  \n*Desc:* Renumber by position  \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* iType (Integer)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iStartID (Integer)  \n *Arg5:* iIncrementStep (Integer)  \n *Arg6:* bAscending1 (Boolean)  \n *Arg7:* bAscending2 (Boolean)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.BySelection.OriginalID": {
    "prefix": "OriginalID",
    "text": "*Name:* Tools.BySelection.OriginalID  \n*Desc:* Renumber by original ID  \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* iType (Integer)  \n *Arg3:* iMethod (Integer)  \n *Arg4:* iStartID (Integer)  \n *Arg5:* iIncrementStep (Integer)  \n *Arg6:* bAscending (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Coordinates.CylinderFace": {
    "prefix": "CylinderFace",
    "text": "*Name:* Tools.Coordinates.CylinderFace  \n*Desc:* create Coordinate by Cylinder Face  \n *Arg1:* strName (String)  \n *Arg2:* iCoordType (Integer)  \n *Arg3:* crFace (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Coordinates.ThreeNode": {
    "prefix": "ThreeNode",
    "text": "*Name:* Tools.Coordinates.ThreeNode  \n*Desc:* create Coordinate by Cylinder Face  \n *Arg1:* strName (String)  \n *Arg2:* iCoordType (Integer)  \n *Arg3:* iOrder (Integer)  \n *Arg4:* crlNode (Cursor List)  \n *Arg5:* veclPoints (Vector List)  \n *Arg6:* crRefCoord (Cursor)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Coordinates.Align": {
    "prefix": "Align",
    "text": "*Name:* Tools.Coordinates.Align  \n*Desc:* create Coordinate by Align  \n *Arg1:* strName (String)  \n *Arg2:* iCoordType (Integer)  \n *Arg3:* iCoordAxis (Integer)  \n *Arg4:* bCreateNew (Boolean)  \n *Arg5:* crlNode (Cursor List)  \n *Arg6:* crEdge (Cursor)  \n *Arg7:* crEdit (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Coordinates.vecOffset": {
    "prefix": "vecOffset",
    "text": "*Name:* Tools.Coordinates.vecOffset  \n*Desc:* Unknown Description  \n *Arg1:* strName (String)  \n *Arg2:* iCoordType (Integer)  \n *Arg3:* vTranslate (V_TRANSLATE)  \n *Arg4:* bCreateNew (Boolean)  \n *Arg5:* crRefCoord (Cursor)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Coordinates.Rotate": {
    "prefix": "Rotate",
    "text": "*Name:* Tools.Coordinates.Rotate  \n*Desc:* create Coordinate by Rotate  \n *Arg1:* strName (String)  \n *Arg2:* iCoordType (Integer)  \n *Arg3:* vecRotate (Vector)  \n *Arg4:* bCreateNew (Boolean)  \n *Arg5:* crRefCoord (Cursor)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Coordinates.AttachCircle": {
    "prefix": "AttachCircle",
    "text": "*Name:* Tools.Coordinates.AttachCircle  \n*Desc:* create Coordinate by AttachCircle  \n *Arg1:* strName (String)  \n *Arg2:* iCoordType (Integer)  \n *Arg3:* crEdge (Cursor)  \n *Arg4:* bCreateNew (Boolean)  \n *Arg5:* crRefCoord (Cursor)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Coordinates.AttachNode": {
    "prefix": "AttachNode",
    "text": "*Name:* Tools.Coordinates.AttachNode  \n*Desc:* create Coordinate by AttachNode  \n *Arg1:* strName (String)  \n *Arg2:* iCoordType (Integer)  \n *Arg3:* crNode (Cursor)  \n *Arg4:* bCreateNew (Boolean)  \n *Arg5:* crRefCoord (Cursor)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Coordinates.Face": {
    "prefix": "Face",
    "text": "*Name:* Tools.Coordinates.Face  \n*Desc:* create Coordinate by Face  \n *Arg1:* strName (String)  \n *Arg2:* iCoordType (Integer)  \n *Arg3:* iOrder (Integer)  \n *Arg4:* veclPoint (Vector List)  \n *Arg5:* crlNode (Cursor List)  \n *Arg6:* crItem (Cursor)  \n *Arg7:* crRefCoord (Cursor)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Coordinates.Offset": {
    "prefix": "Offset",
    "text": "*Name:* Tools.Coordinates.Offset  \n*Desc:* create Coordinate by Offset  \n *Arg1:* strName (String)  \n *Arg2:* iCoordType (Integer)  \n *Arg3:* vecTranslate (Vector)  \n *Arg4:* bCreateNew (Boolean)  \n *Arg5:* crRefCoord (Cursor)  \n *Arg6:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Group.DeleteGroupEntity": {
    "prefix": "DeleteGroupEntity",
    "text": "*Name:* Tools.Group.DeleteGroupEntity  \n*Desc:* Delete Entity in Group  \n *Arg1:* crlDelGroup (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Group.CreateGroup": {
    "prefix": "CreateGroup",
    "text": "*Name:* Tools.Group.CreateGroup  \n*Desc:* Unknown Description  \n *Arg1:* strGroupName (String)  \n *Arg2:* crlTarget (Cursor List)  \n *Arg3:* crEdit (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.TotalLoad.LBC": {
    "prefix": "LBC",
    "text": "*Name:* Tools.TotalLoad.LBC  \n*Desc:*   \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* crCoordinate (Cursor)  \n *Arg3:* strOutput (String)  \n *Arg4:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.TotalLoad.Model": {
    "prefix": "Model",
    "text": "*Name:* Tools.TotalLoad.Model  \n*Desc:*   \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* crCoordinate (Cursor)  \n *Arg3:* strOutput (String)  \n *Arg4:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.TotalLoad.Node": {
    "prefix": "Node",
    "text": "*Name:* Tools.TotalLoad.Node  \n*Desc:*   \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* crCoordinate (Cursor)  \n *Arg3:* strOutput (String)  \n *Arg4:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.TotalLoad.Part": {
    "prefix": "Part",
    "text": "*Name:* Tools.TotalLoad.Part  \n*Desc:*   \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* crCoordinate (Cursor)  \n *Arg3:* strOutput (String)  \n *Arg4:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.TotalLoad.Face": {
    "prefix": "Face",
    "text": "*Name:* Tools.TotalLoad.Face  \n*Desc:*   \n *Arg1:* crlTarget (Cursor List)  \n *Arg2:* crCoordinate (Cursor)  \n *Arg3:* strOutput (String)  \n *Arg4:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.NodeCS": {
    "prefix": "NodeCS",
    "text": "*Name:* Tools.NodeCS  \n*Desc:* create Node CS  \n *Arg1:* crlInst (Cursor List)  \n *Arg2:* crCoordSystem (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.NodeCSGroup": {
    "prefix": "NodeCSGroup",
    "text": "*Name:* Tools.NodeCSGroup  \n*Desc:* Unknown Description  \n *Arg1:*  ()  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.DisplacementCS": {
    "prefix": "DisplacementCS",
    "text": "*Name:* Tools.DisplacementCS  \n*Desc:* displace coordinate  \n *Arg1:* crlInst (Cursor List)  \n *Arg2:* crCoordSystem (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Connections": {
    "prefix": "Connections",
    "text": "*Name:* Tools.Connections  \n*Desc:* renumber connection  \n *Arg1:* listConnectRenumberTool (CONNECT_RENUMBER_TOOL List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.GroupByDCS": {
    "prefix": "GroupByDCS",
    "text": "*Name:* Tools.GroupByDCS  \n*Desc:* Unknown Description  \n *Arg1:*  ()  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Renumber": {
    "prefix": "Renumber",
    "text": "*Name:* Tools.Renumber  \n*Desc:* Set renumber data  \n *Arg1:* listRenumberItem (RENUMBER_ITEM List)  \n *Arg2:* bAssignProp (Boolean)  \n *Arg3:* bSurfCornerFirst (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.RenumberByConnection": {
    "prefix": "RenumberByConnection",
    "text": "*Name:* Tools.RenumberByConnection  \n*Desc:* Renumber by selection  \n *Arg1:* connectRenumberTool (CONNECT_RENUMBER_TOOL)  \n *Arg2:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.RenumberByFile": {
    "prefix": "RenumberByFile",
    "text": "*Name:* Tools.RenumberByFile  \n*Desc:* Renumber By File  \n *Arg1:* strCSVPath (String)  \n *Arg2:* iConfilctStrategy (Integer)  \n *Arg3:* bNeedToUpdateCount (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.ModelInfo": {
    "prefix": "ModelInfo",
    "text": "*Name:* Tools.ModelInfo  \n*Desc:* export model info file  \n *Arg1:* strPath (String)  \n *Arg2:* strPathName (String)  \n *Arg3:* listMeshPartInfoTool (MESH_PART_INFO_TOOL List)  \n *Arg4:* bPropertyAssignedPart (Boolean)  \n *Arg5:* bPropertyAssignedSummary (Boolean)  \n *Arg6:* iModelNode (Integer)  \n *Arg7:* iNmodelnodeWithprop (Integer)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Section": {
    "prefix": "Section",
    "text": "*Name:* Tools.Section  \n*Desc:* Unknown Description  \n *Arg1:* bSection (Boolean)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.ElementCS": {
    "prefix": "ElementCS",
    "text": "*Name:* Tools.ElementCS  \n*Desc:* create element coordinate system  \n *Arg1:* iMethod (Integer)  \n *Arg2:* iDispType (Integer)  \n *Arg3:* bDispXDir (Boolean)  \n *Arg4:* bDispCoord (Boolean)  \n *Arg5:* dDispScale (Double)  \n *Arg6:* crlTarget (Cursor List)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Angle.TwoNodesAxis": {
    "prefix": "TwoNodesAxis",
    "text": "*Name:* Tools.Measure.Angle.TwoNodesAxis  \n*Desc:* Measure the angle created by 2 nodes and Axis.  \n *Arg1:* crNode1 (Cursor)  \n *Arg2:* crNode2 (Cursor)  \n *Arg3:* dlAxis (Double List)  \n *Arg4:* strTarget (String)  \n *Arg5:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Angle.ThreeNodes": {
    "prefix": "ThreeNodes",
    "text": "*Name:* Tools.Measure.Angle.ThreeNodes  \n*Desc:*   \n *Arg1:* crNode1 (Cursor)  \n *Arg2:* crNode2 (Cursor)  \n *Arg3:* crNode3 (Cursor)  \n *Arg4:* strTarget (String)  \n *Arg5:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Angle.ProjectedNode": {
    "prefix": "ProjectedNode",
    "text": "*Name:* Tools.Measure.Angle.ProjectedNode  \n*Desc:* measure angle on projected node  \n *Arg1:* crNode (Cursor)  \n *Arg2:* strTarget (String)  \n *Arg3:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Angle.TwoElemEdges": {
    "prefix": "TwoElemEdges",
    "text": "*Name:* Tools.Measure.Angle.TwoElemEdges  \n*Desc:*   \n *Arg1:* crpElemEdge1 (Cursor Pair)  \n *Arg2:* crpElemEdge2 (Cursor Pair)  \n *Arg3:* strTarget (String)  \n *Arg4:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Angle.TwoAxis": {
    "prefix": "TwoAxis",
    "text": "*Name:* Tools.Measure.Angle.TwoAxis  \n*Desc:* Measure the angle created by 2 Axis.  \n *Arg1:* 0 (0)  \n *Arg2:* 0] (0])  \n *Arg3:* dlXyz1 (Double List)  \n *Arg4:* 0 (0)  \n *Arg5:* 0] (0])  \n *Arg6:* dlXyz2 (Double List)  \n *Arg7:* strTarget (String)  \n ... please read PSJ Command document for other args ...  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Angle.TwoEdges": {
    "prefix": "TwoEdges",
    "text": "*Name:* Tools.Measure.Angle.TwoEdges  \n*Desc:* Measure the angle created by 2 edges.  \n *Arg1:* crEdge1 (Cursor)  \n *Arg2:* crEdge2 (Cursor)  \n *Arg3:* strTarget (String)  \n *Arg4:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Area.Element": {
    "prefix": "Element",
    "text": "*Name:* Tools.Measure.Area.Element  \n*Desc:* Measure Distance By FaceNode  \n *Arg1:* crlElem (Cursor List)  \n *Arg2:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Area.Face": {
    "prefix": "Face",
    "text": "*Name:* Tools.Measure.Area.Face  \n*Desc:* Measure Distance By FaceNode  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Area.Part": {
    "prefix": "Part",
    "text": "*Name:* Tools.Measure.Area.Part  \n*Desc:* Measure Distance By FaceNode  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Distance.TwoEdges": {
    "prefix": "TwoEdges",
    "text": "*Name:* Tools.Measure.Distance.TwoEdges  \n*Desc:* measure the distance of two edges  \n *Arg1:* crEdge1 (Cursor)  \n *Arg2:* crEdge2 (Cursor)  \n *Arg3:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Distance.TwoNodes": {
    "prefix": "TwoNodes",
    "text": "*Name:* Tools.Measure.Distance.TwoNodes  \n*Desc:* Measure Distance Two Nodes  \n *Arg1:* crNode1 (Cursor)  \n *Arg2:* crNode2 (Cursor)  \n *Arg3:* strTarget (String)  \n *Arg4:* iPrecision (Integer)  \n *Arg5:* crCoordinateSystem (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Distance.FaceNode": {
    "prefix": "FaceNode",
    "text": "*Name:* Tools.Measure.Distance.FaceNode  \n*Desc:* Measure Distance By FaceNode  \n *Arg1:* crlFace (Cursor List)  \n *Arg2:* crlNode (Cursor List)  \n *Arg3:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Distance.Edge": {
    "prefix": "Edge",
    "text": "*Name:* Tools.Measure.Distance.Edge  \n*Desc:* Measure Edge Length  \n *Arg1:* crEdge (Cursor)  \n *Arg2:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Distance.TwoPoints": {
    "prefix": "TwoPoints",
    "text": "*Name:* Tools.Measure.Distance.TwoPoints  \n*Desc:* measure distance 2 points  \n *Arg1:* posPoint1 (Position)  \n *Arg2:* posPoint2 (Position)  \n *Arg3:* strTarget (String)  \n *Arg4:* iPrecision (Integer)  \n *Arg5:* crCoordinateSystem (Cursor)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Distance.EdgeNode": {
    "prefix": "EdgeNode",
    "text": "*Name:* Tools.Measure.Distance.EdgeNode  \n*Desc:* Measure Distance From Node to Edge  \n *Arg1:* crEdge (Cursor)  \n *Arg2:* crNode (Cursor)  \n *Arg3:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Distance.LineNode": {
    "prefix": "LineNode",
    "text": "*Name:* Tools.Measure.Distance.LineNode  \n*Desc:* Measures the distance of a perpendicular line from a node toward the line defined by the two nodes.  \n *Arg1:* crlTargetNode (Cursor List)  \n *Arg2:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Distance.PlaneElemToNode": {
    "prefix": "PlaneElemToNode",
    "text": "*Name:* Tools.Measure.Distance.PlaneElemToNode  \n*Desc:* Measure Distance between Node and plane (created by element).  \n *Arg1:* crNode (Cursor)  \n *Arg2:* crElem (Cursor)  \n *Arg3:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n *Desc:* measure the distance from node to plane(defined by 3 nodes)  \n *Arg1:* crNode1 (Cursor)  \n *Arg2:* crNode2 (Cursor)  \n *Arg3:* crNode3 (Cursor)  \n *Arg4:* crNode (Cursor)  \n *Arg5:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Mass.Property": {
    "prefix": "Property",
    "text": "*Name:* Tools.Measure.Mass.Property  \n*Desc:* measure mass using applied property  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlCondition (Cursor List)  \n *Arg3:* strTarget (String)  \n *Arg4:* bGravityCenter (Boolean)  \n *Arg5:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Mass.Material": {
    "prefix": "Material",
    "text": "*Name:* Tools.Measure.Mass.Material  \n*Desc:* measure mass by material  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* crlCondition (Cursor List)  \n *Arg3:* strDensity (String)  \n *Arg4:* strTarget (String)  \n *Arg5:* bGravityCenter (Boolean)  \n *Arg6:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Radius.Edge": {
    "prefix": "Edge",
    "text": "*Name:* Tools.Measure.Radius.Edge  \n*Desc:* Measure edge minimum radius  \n *Arg1:* crEdge (Cursor)  \n *Arg2:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Radius.ThreeNodes": {
    "prefix": "ThreeNodes",
    "text": "*Name:* Tools.Measure.Radius.ThreeNodes  \n*Desc:* Measure Radius MeasureRadiusBy3Nodes  \n *Arg1:* crNode13 (Cursor)  \n *Arg2:* crNode23 (Cursor)  \n *Arg3:* crNode33 (Cursor)  \n *Arg4:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "Tools.Measure.Volume": {
    "prefix": "Volume",
    "text": "*Name:* Tools.Measure.Volume  \n*Desc:* measure volume of parts  \n *Arg1:* crlPart (Cursor List)  \n *Arg2:* iPrecision (Integer)  \n *Return:* 1 if successed, or 0 if failed  \n "
  },
  "JPT.RemoveEntitiesByID": {
    "prefix": "RemoveEntitiesByID",
    "text": "*Function:* JPT.RemoveEntitiesByID  \n*Description:* remove entities from model by id  \n *Input1:* DItem type (JPT.EntityType)  \n *Input2:* id of entity (int)  \n *Return:* None  \n *Example:*   \n listbody = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, \"Cube\", JPT.BoolType.FALSE_VAL)  \n idbody = listbody[0].id  \n JPT.RemoveEntitiesByID(JPT.EntityType.BODY, idbody)  \n "
  },
  "JPT.RemoveEntitiesByName": {
    "prefix": "RemoveEntitiesByName",
    "text": "*Function:* JPT.RemoveEntitiesByName  \n*Description:* remove entities from model by name  \n *Input1:* DTable type (JPT.DTableType)  \n *Input2:* name of entity (string)  \n *Input3:* match with name option (1,0 or JPT.BoolType)  \n *Return:* None  \n *Example:* JPT.RemoveEntitiesByName(JPT.DTableType.DTABLE_BODY, \"Cube_1\", 1)  \n "
  },
  "JPT.RemoveAllLoadsBCs": {
    "prefix": "RemoveAllLoadsBCs",
    "text": "*Function:* JPT.RemoveAllLoadsBCs  \n*Description:* Remove all Loads and Boundary Condition in model  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveAllLoadsBCs ()  \n "
  },
  "JPT.RemoveAllContacts": {
    "prefix": "RemoveAllContacts",
    "text": "*Function:* JPT.RemoveAllContacts  \n*Description:* Remove all of Contact in models  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveAllContacts()  \n "
  },
  "JPT.RemoveAllConnections": {
    "prefix": "RemoveAllConnections",
    "text": "*Function:* JPT.RemoveAllConnections  \n*Description:* Remove all of Connection in models  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveAllConnections()  \n "
  },
  "JPT.RemoveAllLoadCases": {
    "prefix": "RemoveAllLoadCases",
    "text": "*Function:* JPT.RemoveAllLoadCases  \n*Description:* Remove all load cases in models  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveAllLoadCases()  \n "
  },
  "JPT.RemoveAllMaterials": {
    "prefix": "RemoveAllMaterials",
    "text": "*Function:* JPT.RemoveAllMaterials  \n*Description:* Remove all of Material in User Data Base  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveAllMaterials()  \n "
  },
  "JPT.RemoveWSProperties": {
    "prefix": "RemoveWSProperties",
    "text": "*Function:* JPT.RemoveWSProperties  \n*Description:* Remove all properties in models  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveWSProperties()  \n "
  },
  "JPT.RemoveAllCoordinates": {
    "prefix": "RemoveAllCoordinates",
    "text": "*Function:* JPT.RemoveAllCoordinates  \n*Description:* Remove all of created coordinates  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveAllCoordinates()  \n "
  },
  "JPT.RemoveAllMeshSettings": {
    "prefix": "RemoveAllMeshSettings",
    "text": "*Function:* JPT.RemoveAllMeshSettings  \n*Description:* Remove all local mesh settings  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveAllMeshSettings()  \n "
  },
  "JPT.RemoveAllFieldTables": {
    "prefix": "RemoveAllFieldTables",
    "text": "*Function:* JPT.RemoveAllFieldTables  \n*Description:* Remove all of Field Data table in models  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveAllFieldTables()  \n "
  },
  "JPT.RemoveAllAbaqusStep": {
    "prefix": "RemoveAllAbaqusStep",
    "text": "*Function:* JPT.RemoveAllAbaqusStep  \n*Description:* Remove all of Abaqus steps in Analysis  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveAllAbaqusStep()  \n "
  },
  "JPT.RemoveAllSolverjob": {
    "prefix": "RemoveAllSolverjob",
    "text": "*Function:* JPT.RemoveAllSolverjob  \n*Description:* Remove all analysis Jobs  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.RemoveAllSolverjob()  \n "
  },
  "JPT.RemoveAllByTableType": {
    "prefix": "RemoveAllByTableType",
    "text": "*Function:* JPT.RemoveAllByTableType  \n*Description:* remove all entities in models by table type   \n *Input1:* DTable type (JPT.DTableType)  \n *Return:* None  \n *Example:* JPT.RemoveAllByTableType(JPT.DTableType.DTABLE_BODY)  \n "
  },
  "JPT.CreateSubAssembly": {
    "prefix": "CreateSubAssembly",
    "text": "*Function:* JPT.CreateSubAssembly  \n*Description:* Create a sub node under parent on assembly tree with name  \n *Input1:* name of sub node (string)  \n *Input2:* parent object (DItem class)  \n *Return:* new sub node object (DItem class)  \n *Example:* JPT.CreateSubAssembly(\"LocalSetting_1\", parentObject)  \n "
  },
  "JPT.DeleteSubAssembly": {
    "prefix": "DeleteSubAssembly",
    "text": "*Function:* JPT.DeleteSubAssembly  \n*Description:* Delete a sub node from assembly tree  \n *Input1:* sub node object (DItem class)  \n *Return:* None  \n *Example:* JPT.DeleteSubAssembly(dentityObject)  \n "
  },
  "JPT.FindSubAssemblyByName": {
    "prefix": "FindSubAssemblyByName",
    "text": "*Function:* JPT.FindSubAssemblyByName  \n*Description:* Find a sub node from assembly tree by name  \n *Input1:* name of sub node (string)  \n *Return:* list DItem object matched with input name (DItemVector)  \n *Example:* JPT.FindSubAssemblyByName(\"LocalSetting_1\")  \n "
  },
  "JPT.FindSubAssemblyByID": {
    "prefix": "FindSubAssemblyByID",
    "text": "*Function:* JPT.FindSubAssemblyByID  \n*Description:* Find a sub node from assembly tree by id  \n *Input1:* id of entity sub node (int)   \n *Return:* sub node object matched with input id (DItem)   \n *Example:* JPT.FindSubAssemblyByID(1)  \n "
  },
  "JPT.DeleteSubAssemblyRecursively": {
    "prefix": "DeleteSubAssemblyRecursively",
    "text": "*Function:* JPT.DeleteSubAssemblyRecursively  \n*Description:* Delete a sub node and all childs from assembly tree  \n *Input1:* sub node object (DItem class)  \n *Return:* None  \n *Example:* JPT.DeleteSubAssemblyRecursively(dentityObject)  \n "
  },
  "JPT.GetAllPartsInSubAssembly": {
    "prefix": "GetAllPartsInSubAssembly",
    "text": "*Function:* JPT.GetAllPartsInSubAssembly  \n*Description:* get all parts in a sub node from assembly tree  \n *Input1:* sub node object (DItem class)  \n *Return:* list of DItem object matched with input name (DItemVector)  \n *Example:* JPT.GetAllPartsInSubAssembly(DItem)   \n "
  },
  "JPT.CastToDItem": {
    "prefix": "CastToDItem",
    "text": "*Function:* JPT.CastToDItem  \n*Description:* cast a child object to entity object  \n *Input1:* any kind of objects (Body, Face, Elem, Edge, Group, Node,...)  \n *Return:* entity object (DItem class)  \n *Example:*   \n listDbodyObject = JPT.GetAllParts()   \n bodyObject = listDbodyObject[0]  \n entityObject = JPT.CastToDItem(dbodyObject)  \n "
  },
  "JPT.CastDItemToDBody": {
    "prefix": "CastDItemToDBody",
    "text": "*Function:* JPT.CastDItemToDBody  \n*Description:* cast a DItem object to Body object  \n *Input1:* DItem object (DItem class)  \n *Return:* Body object (Body class)  \n *Example:*   \n listEntityObject = JPT.GetAllByType(JPT.EntityType.BODY)  \n entityObject = listEntityObject[0]  \n bodyObject = JPT.CastDItemToDBody(dentityObject)  \n "
  },
  "JPT.CastDItemToDFace": {
    "prefix": "CastDItemToDFace",
    "text": "*Function:* JPT.CastDItemToDFace  \n*Description:* cast a DItem object to Face object  \n *Input1:* DItem object (DItem class)  \n *Return:* Face object (Face class)  \n *Example:*   \n listEntityObject = JPT.GetAllByType(JPT.EntityType.FACE)  \n entityObject = listEntityObject[0]  \n faceObject = JPT.CastDItemToDFace(dentityObject)  \n "
  },
  "JPT.CastDItemToDElem": {
    "prefix": "CastDItemToDElem",
    "text": "*Function:* JPT.CastDItemToDElem  \n*Description:* cast a DItem object to Elem object  \n *Input1:* DItem object (DItem class)  \n *Return:* Elem object (Elem class)  \n *Example:*   \n listEntityObject = JPT.GetAllByType(JPT.EntityType.ELEM)  \n entityObject = listEntityObject[0]  \n elemObject = JPT.CastDItemToDElem(dentityObject)  \n "
  },
  "JPT.CastDItemToDEdge": {
    "prefix": "CastDItemToDEdge",
    "text": "*Function:* JPT.CastDItemToDEdge  \n*Description:* cast a DItem object to Edge object  \n *Input1:* DItem object (DItem class)  \n *Return:* Edge object (Edge class)  \n *Example:*   \n listEntityObject = JPT.GetAllByType(JPT.EntityType.EDGE)  \n entityObject = listEntityObject[0]  \n edgeObject = JPT.CastDItemToDEdge(dentityObject)  \n "
  },
  "JPT.CastDItemToDGroup": {
    "prefix": "CastDItemToDGroup",
    "text": "*Function:* JPT.CastDItemToDGroup  \n*Description:* cast a DItem object to Group object  \n *Input1:* DItem object (DItem class)  \n *Return:* Group object (Group class)  \n *Example:*   \n listEntityObject = JPT.GetAllByType(JPT.EntityType.GROUP)  \n entityObject = listEntityObject[0]  \n groupObject = JPT.CastDItemToDGroup(dentityObject)  \n "
  },
  "JPT.CastDItemToDNode": {
    "prefix": "CastDItemToDNode",
    "text": "*Function:* JPT.CastDItemToDNode  \n*Description:* cast a DItem object to Node object  \n *Input1:* DItem object (DItem class)  \n *Return:* Node object (Node class)  \n *Example:*   \n listEntityObject = JPT.GetAllByType(JPT.EntityType.NODE)  \n entityObject = listEntityObject[0]  \n nodeObject = JPT.CastDItemToDNode(dentityObject)  \n "
  },
  "JPT.CastDItemToDCoord": {
    "prefix": "CastDItemToDCoord",
    "text": "*Function:* JPT.CastDItemToDCoord  \n*Description:* cast a DItem object to Coordinate object  \n *Input1:* DItem object (DItem class)  \n *Return:* Coordinate object (DCoord class)  \n *Example:*   \n listEntityObject = JPT.GetAllByType(JPT.EntityType.COORD)  \n entityObject = listEntityObject[0]  \n coordObject = JPT.CastDItemToDCoord(dentityObject)  \n "
  },
  "JPT.CastDItemToDConnect": {
    "prefix": "CastDItemToDConnect",
    "text": "*Function:* JPT.CastDItemToDConnect  \n*Description:* cast a DItem object to Connection object  \n *Input1:* DItem object (DItem class)  \n *Return:* DConnect object (DConnect class)  \n *Example:*   \n listEntityObject = JPT.GetAllByType(JPT.EntityType.CONNECT_MPC)  \n entityObject = listEntityObject[0]  \n connectObject= JPT.CastDItemToDConnect(dentityObject)  \n "
  },
  "JPT.CastDItemToDLoadBC": {
    "prefix": "CastDItemToDLoadBC",
    "text": "*Function:* JPT.CastDItemToDLoadBC  \n*Description:* cast a DItem object to LBC object  \n *Input1:* DItem object (DItem class)  \n *Return:* LBC object (DLoadBC class)  \n *Example:*   \n listEntityObject = JPT.GetAllByType(JPT.EntityType.LBC_FORCE)  \n entityObject = listEntityObject[0]  \n lbcObject = JPT.CastDItemToDLoadBC(dentityObject)  \n "
  },
  "JPT.DItemToMacroTCursorPair": {
    "prefix": "DItemToMacroTCursorPair",
    "text": "*Function:* JPT.DItemToMacroTCursorPair  \n*Description:* convert pair of DItem object to cursor pair macro string    \n *Input1:* DItem object 1 (DItem class)  \n *Input2:* DItem object 2 (DItem class)  \n *Return:* cursor pair macro string (string)  \n *Example:*   \n listNodeObject = JPT.GetAllNodes()  \n entityObject1 = JPT.CastToDItem(listNodeObject[0])  \n entityObject2 = JPT.CastToDItem(listNodeObject[1])  \n *strElemEdge = JPT.DItemToMacroTCursorPair(dentityObject1, dentityObject2) // 10:1-10:*2  \n "
  },
  "JPT.ListDoubleToMacroVector": {
    "prefix": "ListDoubleToMacroVector",
    "text": "*Function:* JPT.ListDoubleToMacroVector  \n*Description:* convert list of double value to vector3d macro string    \n *Input1:* value1 (double)   \n *Input2:* value2 (double)   \n *Input2:* value3 (double)   \n *Return:* vector3d macro string (string)   \n *Example:*   \n JPT.ListDoubleToMacroVector(1.0, 1.0, 1.0) // [1.0,1.0,1.0]  \n JPT.ListDoubleToMacroVector(1, 2, 3) // [1,2,3]  \n "
  },
  "JPT.DTVector3dToMacroVector": {
    "prefix": "DTVector3dToMacroVector",
    "text": "*Function:* JPT.DTVector3dToMacroVector  \n*Description:* convert Vector3d object to vector3d macro string   \n *Input1:* Vector3d object (DTVector3d class)  \n *Return:* vector3d macro string (string)   \n *Example:*   \n listNodeObject = JPT.GetAllNodes()  \n posNode1 = listNodeObject[0].pos  \n JPT.DTVector3dToMacroVector(posNode1)  \n "
  },
  "JPT.DItemToMacroTCursor": {
    "prefix": "DItemToMacroTCursor",
    "text": "*Function:* JPT.DItemToMacroTCursor  \n*Description:* convert a DItem object to cursor macro string   \n *Input1:* DItem object (DItem class)  \n *Return:* cursor macro string (string)  \n *Example:*   \n listnode1 = JPT.GetEntitiesByID(JPT.EntityType.NODE, 435)  \n listnode2 = JPT.GetEntitiesByID(JPT.EntityType.NODE, 434)  \n *node1 = JPT.DItemToMacroTCursor(listnode1[0]) // 10:*1  \n *node2 = JPT.DItemToMacroTCursor(listnode2[0]) // 10:*2  \n JPT.Exec('Collapse({0}, {1})'.format(node1, node2))  \n "
  },
  "JPT.DItemListToMacroListTCursor": {
    "prefix": "DItemListToMacroListTCursor",
    "text": "*Function:* JPT.DItemListToMacroListTCursor  \n*Description:* convert list of DItem objects to cursor list macro string   \n *Input1:* list of DItem objects (DItemVector)   \n *Return:* cursor list macro string (string)    \n *Example:*   \n listface1 = JPT.GetAllFaces()  \n *JPT.DItemListToMacroListTCursor(listface1) // [10:1, 10:*1, ...]  \n "
  },
  "JPT.DItemToMacroListTCursor": {
    "prefix": "DItemToMacroListTCursor",
    "text": "*Function:* JPT.DItemToMacroListTCursor  \n*Description:* convert a DItem object to cursor list macro string   \n *Input1:* DItem objects (DItem class)  \n *Return:* cursor list macro string (string)    \n *Example:*   \n listnode = JPT.GetEntitiesByID(JPT.EntityType.NODE, 434)  \n *node = JPT.DItemToMacroTCursor(listnode[0]) // 10:*1  \n *JPT.DItemToMacroListTCursor(node) [10:*1]  \n "
  },
  "JPT.MacroResultParser": {
    "prefix": "MacroResultParser",
    "text": "*Function:* JPT.MacroResultParser  \n*Description:* parse returned string from macro to list of string  \n *Input1:* returned string from macro (string)    \n *Input2:* list of string pattern (string, cursor, cursor_pair, list_number  \n list_cursor_pair, list_cursor, list_list_cursor, list_string, vector3d, number)   \n *Return:* list of result (list string)    \n *Example:*   \n *result = JPT.Exec('MC_Mesh_Quality_Manual_Check_Tri([3:*1], 0, 0, 0.1)')  \n *# result = 1, [6:100, 6:*101]  \n listString = JPT.MacroResultParser(result, [\"number\", \"list_cursor\"])   \n "
  },
  "JPT.MacroListTCursorToListDItem": {
    "prefix": "MacroListTCursorToListDItem",
    "text": "*Function:* JPT.MacroListTCursorToListDItem  \n*Description:* convert a macro cursor list string to list of DItem objects  \n *Input1:* macro cursor list string (string)  \n *Return:* list of DItem objects (DItemVector)  \n *Example: listEntityObject = JPT.MacroListTCursorToListDItem('[10:1, 10:*1, ...]')  \n "
  },
  "JPT.MacroTCursorToDItem": {
    "prefix": "MacroTCursorToDItem",
    "text": "*Function:* JPT.MacroTCursorToDItem  \n*Description:* convert a macro cursor string to DItem object  \n *Input1:* macro cursor string (string)  \n *Return:* DItem object (DItem class)  \n *Example: dentityObject = JPT.MacroTCursorToDItem('3:*1')  \n "
  },
  "JPT.ConvertRGBToJPTColor": {
    "prefix": "ConvertRGBToJPTColor",
    "text": "*Function:* JPT.ConvertRGBToJPTColor  \n*Description:* convert a RGB (red,green,blue) value to JPT color number  \n *Input1:* RGB (red,green,blue)  \n *Return:* JPT color number (int)  \n *Example:*   \n newcolor = JPT.ConvertRGBToJPTColor(255,0,0) # red color  \n listbody = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, \"Cube_1\", 1)  \n JPT.CastDItemToDBody(listbody[0]).color = newcolor  \n "
  },
  "JPT.CopyToClipBoard": {
    "prefix": "CopyToClipBoard",
    "text": "*Function:* JPT.CopyToClipBoard  \n*Description:* put a text to clipboard buffer   \n *Input1:* text input (string)  \n *Return:* None  \n *Example:* JPT.CopyToClipBoard(text)  \n "
  },
  "JPT.CheckLicense": {
    "prefix": "CheckLicense",
    "text": "*Function:* JPT.CheckLicense  \n*Description:* Check feature license whether active or not  \n *Input1:* License name(string)  \n *        Jupiter feature license:* Home > Preference > License  \n *Return:* True / False  \n *Example:* JPT.CheckLicense(\"JPT_BASE\")  \n "
  },
  "JPT.IsDefaultDouble": {
    "prefix": "IsDefaultDouble",
    "text": "*Function:* JPT.IsDefaultDouble  \n*Description:* check a double value is Default value or not   \n *Input1:* value (double)   \n *Return:* True / False  \n *Example:* JPT.IsDefaultDouble(value)  \n "
  },
  "JPT.IsDefaultInt": {
    "prefix": "IsDefaultInt",
    "text": "*Function:* JPT.IsDefaultInt  \n*Description:* check a int value is Default value or not   \n *Input1:* value (int)   \n *Return:* True / False  \n *Example:* JPT.IsDefaultInt(value)  \n "
  },
  "JPT.ConvertFromDocUnit": {
    "prefix": "ConvertFromDocUnit",
    "text": "*Function:* JPT.ConvertFromDocUnit  \n*Description:* Convert value from JPT user setup unit to SI unit system  \n *Input1:* Conversion source value (double)  \n *Input2:* Unit system conversion type (JPT.UnitType)  \n *Return:* Converted Value (double)  \n *Example:* JPT.ConvertFromDocUnit(1, JPT.UnitType.Unit_Length)  \n "
  },
  "JPT.ConvertValueToDocUnit": {
    "prefix": "ConvertValueToDocUnit",
    "text": "*Function:* JPT.ConvertValueToDocUnit  \n*Description:* Convert value from SI unit system to JPT user setup unit  \n *Input1:* Conversion source value (double)  \n *Input2:* Unit system conversion type (JPT.UnitType)  \n *Return:* Converted value (double)  \n *Example:* JPT.ConvertValueToDocUnit(1, JPT.UnitType.Unit_Length)  \n "
  },
  "JPT.ConvertFromMacroUnit": {
    "prefix": "ConvertFromMacroUnit",
    "text": "*Function:* JPT.ConvertFromMacroUnit  \n*Description:* Convert unit system from user input unit to macro SI unit  \n *Input1:* Conversion source value (double)  \n *Input2:* Unit system conversion type (JPT.UnitType)  \n *Input3:* Unit abbreviation (string)  \n *Return:* Converted value (double)  \n *Example:* JPT.ConvertFromMacroUnit(1, JPT.UnitType.Unit_Length, 'mm')  \n "
  },
  "JPT.ConvertValueToMacroUnit": {
    "prefix": "ConvertValueToMacroUnit",
    "text": "*Function:* JPT.ConvertValueToMacroUnit  \n*Description:* Convert unit system from macro SI unit to user input unit  \n *Input1:* Conversion source value (double)  \n *Input2:* Unit system conversion type (JPT.UnitType)  \n *Input3:* Unit abbreviation (string)  \n *Return:* Converted value(double)  \n *Example:* convToMacr = JPT.ConvertValueToMacroUnit(1, JPT.UnitType.Unit_Length, 'mm')  \n "
  },
  "JPT.GetJPTTempPath": {
    "prefix": "GetJPTTempPath",
    "text": "*Function:* JPT.GetJPTTempPath  \n*Description:* Get temp document path  \n *Input1:* None  \n *Return:* Temp Document Path(string)  \n *Example:* JPT.GetJPTTempPath()  \n "
  },
  "JPT.GetProgramPath": {
    "prefix": "GetProgramPath",
    "text": "*Function:* JPT.GetProgramPath  \n*Description:* Get application installation directory  \n *Input1:* None  \n *Return:* Program Path(string)  \n *Example:* JPT.GetProgramPath()  \n "
  },
  "JPT.GetCurrentDocumentPath": {
    "prefix": "GetCurrentDocumentPath",
    "text": "*Function:* JPT.GetCurrentDocumentPath  \n*Description:* Get current document path  \n *Input1:* None  \n *Return:* Current Document Path(string)  \n *Example:* JPT.GetCurrentDocumentPath()  \n "
  },
  "JPT.QuitApplication": {
    "prefix": "QuitApplication",
    "text": "*Function:* JPT.QuitApplication  \n*Description:* quit jupiter  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.QuitApplication()  \n "
  },
  "JPT.GetAppPathInfo": {
    "prefix": "GetAppPathInfo",
    "text": "*Function:* JPT.GetAppPathInfo  \n*Description:* get a JPT path string (Program, Temp, Appdata, Document)  \n *Input1:* Path type (JPT.PathType)  \n *Return:* path (string)  \n *Example:* JPT.GetAppPathInfo()  \n "
  },
  "JPT.GetSelectedNodes": {
    "prefix": "GetSelectedNodes",
    "text": "*Function:* JPT.GetSelectedNodes  \n*Description:* Get selected node information  \n *Input1:* None  \n *Return:* list of DNode objects contain selected node information (NodeVector)  \n *Example:* JPT.GetSelectedNodes()  \n "
  },
  "JPT.GetSelectedElems": {
    "prefix": "GetSelectedElems",
    "text": "*Function:* JPT.GetSelectedElems  \n*Description:* Get selected element information  \n *Input1:* None  \n *Return:* list of DElem objects contain selected element information (ElemVector)  \n *Example:* JPT.GetSelectedElems()  \n "
  },
  "JPT.GetSelectedFaces": {
    "prefix": "GetSelectedFaces",
    "text": "*Function:* JPT.GetSelectedFaces  \n*Description:* Get selected face information  \n *Input1:* None  \n *Return:* list of DFace objects contain selected face information (FaceVector)  \n *Example:* JPT.GetSelectedFaces()  \n "
  },
  "JPT.GetSelectedEdges": {
    "prefix": "GetSelectedEdges",
    "text": "*Function:* JPT.GetSelectedEdges  \n*Description:* Get all of selected edge information  \n *Input1:* None  \n *Return:* list of DEdge objects contain selected edge information (EdgeVector)  \n *Example:* JPT.GetSelectedEdges()  \n "
  },
  "JPT.GetSelectedParts": {
    "prefix": "GetSelectedParts",
    "text": "*Function:* JPT.GetSelectedParts  \n*Description:* Get selected part information  \n *Input1:* None  \n *Return:* list of DBody objects contain selected part information (BodyVector)  \n *Example:* JPT.GetSelectedParts()  \n "
  },
  "JPT.GetSelectedGroups": {
    "prefix": "GetSelectedGroups",
    "text": "*Function:* JPT.GetSelectedGroups  \n*Description:* Get selected group information   \n *Input1:* None  \n *Return:* list of DGroup objects contain selected group information (GroupVector)  \n *Example:* JPT.GetSelectedGroups()  \n "
  },
  "JPT.GetAllParts": {
    "prefix": "GetAllParts",
    "text": "*Function:* JPT.GetAllParts  \n*Description:* Get information of all parts  \n *Input1:* None  \n *Return:* list of DBody objects contain part information (BodyVector)  \n *Example:* JPT.GetAllParts()  \n "
  },
  "JPT.GetAllFaces": {
    "prefix": "GetAllFaces",
    "text": "*Function:* JPT.GetAllFaces  \n*Description:* Get information of faces  \n *Input1:* None  \n *Return:* list of DFace objects contain face information (FaceVector)  \n *Example:* JPT.GetAllFaces()  \n "
  },
  "JPT.GetAllEdges": {
    "prefix": "GetAllEdges",
    "text": "*Function:* JPT.GetAllEdges  \n*Description:* Get information of edges  \n *Input1:* None  \n *Return:* list of DEdge objects contain edge information (EdgeVector)  \n *Example:* JPT.GetAllEdges()  \n "
  },
  "JPT.GetAllElems": {
    "prefix": "GetAllElems",
    "text": "*Function:* JPT.GetAllElems  \n*Description:* Get information of elements  \n *Input1:* None  \n *Return:* list of DNode objects contain element information (NodeVector)  \n *Example:* JPT.GetAllElems()  \n "
  },
  "JPT.GetAllNodes": {
    "prefix": "GetAllNodes",
    "text": "*Function:* JPT.GetAllNodes  \n*Description:* Get information of all nodes  \n *Input1:* None  \n *Return:* list of DNode objects contain node information (NodeVector)  \n *Example:* JPT.GetAllNodes()  \n "
  },
  "JPT.GetAllGroups": {
    "prefix": "GetAllGroups",
    "text": "*Function:* JPT.GetAllGroups  \n*Description:* Get all entities' information inside groups  \n *Input1:* None  \n *Return:* list of DGroup objects contain group information (GroupVector)  \n *Example:* JPT.GetAllGroups()  \n "
  },
  "JPT.GetAllByTableTypeID": {
    "prefix": "GetAllByTableTypeID",
    "text": "*Function:* JPT.GetAllByTableTypeID  \n*Description:* Get the information about indicated entity by type ID  \n *Input1:* DTable type ID input(JPT.DTableType)  \n *Return:* Type ID(DItem)   \n *Example:* JPT.GetAllByTableTypeID(3)  \n "
  },
  "JPT.GetAllByType": {
    "prefix": "GetAllByType",
    "text": "*Function:* JPT.GetAllByType  \n*Description:* Get entities information by inputting their DItem type  \n *Input1:* DItem type input (JPT.EntityType)  \n *Return:* DItem information (DItem)   \n *Example:* JPT.GetAllByType(JPT.EntityType.INST)  \n "
  },
  "JPT.GetCountByType": {
    "prefix": "GetCountByType",
    "text": "*Function:* JPT.GetCountByType  \n*Description:* Get count of entities by type  \n *Input1: DItem Type:* BODY, VERTEX, EDGE, FACE, SOLID, ELEM,...(JPT.EntityType)  \n *Return:* Number of entities(int)  \n *Example:* JPT.GetCountByType(JPT.EntityType.BODY)  \n "
  },
  "JPT.GetAllSelected": {
    "prefix": "GetAllSelected",
    "text": "*Function:* JPT.GetAllSelected  \n*Description:* Get entity information from the selected entity (Connections, Contacts, Parts, ...)  \n *Input1:* None  \n *Return:* list of DItem objects contain selected entity information (DItem)   \n *Example:* JPT.GetAllSelected()  \n "
  },
  "JPT.GetLastCreatedCursor": {
    "prefix": "GetLastCreatedCursor",
    "text": "*Function:* JPT.GetLastCreatedCursor  \n*Description:* Get the latest id of created entity  \n *Input1:* None  \n *Return:* Last created Object(DItem)   \n *Example:* JPT.GetLastCreatedCursor()  \n "
  },
  "JPT.GetCenterOfEntities": {
    "prefix": "GetCenterOfEntities",
    "text": "*Function:* JPT.GetCenterOfEntities  \n*Description:* Get center coordinate of selected entities  \n *Input1:* list of DItem object (DItemVector)  \n *Return:* Coordinate[x,y,z] of selected entities(double)  \n *Example:* JPT.GetCenterOfEntities(entity)  \n "
  },
  "JPT.GetSharedFaces": {
    "prefix": "GetSharedFaces",
    "text": "*Function:* JPT.GetSharedFaces  \n*Description:* Get shared face information  \n *Input1:* list of DItem object (DItemVector)  \n *Return:* Shared face information (typeID, id, key)(DItem)   \n *Example:* JPT.GetSharedFaces(shareFace)  \n "
  },
  "JPT.GetSharedElements": {
    "prefix": "GetSharedElements",
    "text": "*Function:* JPT.GetSharedElements  \n*Description:* Get shared element information  \n *Input1:* ist of DItem object (DItemVector)  \n *Return:* Shared element information (type, typeID, id, info, key, masters, slave, targets, children, parent)(DItem)   \n *Example:* JPT.GetSharedElements(bodies)  \n "
  },
  "JPT.GetSharedNodes": {
    "prefix": "GetSharedNodes",
    "text": "*Function:* JPT.GetSharedNodes  \n*Description:* Get shared node information  \n *Input1:* ist of DItem object (DItemVector)  \n *Return:* Shared node information (typeID, id, key)(DItem)   \n *Example:* JPT.GetSharedNodes(shareNodes)  \n "
  },
  "JPT.GetAllLoadsBCs": {
    "prefix": "GetAllLoadsBCs",
    "text": "*Function:* JPT.GetAllLoadsBCs  \n*Description:* Get information of all loads and BCs  \n *Input1:* None  \n *Return:* Load information (type, type ID, id, key, name, info, targets, isValid, masters, slaves, parent, children)(DItem)   \n *Example:* JPT.GetAllLoadsBCs()  \n "
  },
  "JPT.GetSelectedNodesCr": {
    "prefix": "GetSelectedNodesCr",
    "text": "*Function:* JPT.GetSelectedNodesCr  \n*Description:* get selected node as string output  \n *Input1:* None  \n *Return:* selected node (string)  \n *Example:* JPT.GetSelectedNodesCr()  \n "
  },
  "JPT.GetSelectedElemsCr": {
    "prefix": "GetSelectedElemsCr",
    "text": "*Function:* JPT.GetSelectedElemsCr  \n*Description:* get selected element as string output  \n *Input1:* None  \n *Return:* selected element (string)  \n *Example:* JPT.GetSelectedElemsCr()  \n "
  },
  "JPT.GetSelectedFacesCr": {
    "prefix": "GetSelectedFacesCr",
    "text": "*Function:* JPT.GetSelectedFacesCr  \n*Description:* get selected face as string output  \n *Input1:* None  \n *Return:* selected face (string)  \n *Example:* JPT.GetSelectedFacesCr()  \n "
  },
  "JPT.GetSelectedEdgesCr": {
    "prefix": "GetSelectedEdgesCr",
    "text": "*Function:* JPT.GetSelectedEdgesCr  \n*Description:* get selected edge as string output  \n *Input1:* None  \n *Return:* selected edge (string)  \n *Example:* JPT.GetSelectedEdgesCr()  \n "
  },
  "JPT.GetSelectedPartsCr": {
    "prefix": "GetSelectedPartsCr",
    "text": "*Function:* JPT.GetSelectedPartsCr  \n*Description:* get selected part as string output  \n *Input1:* None  \n *Return:* selected part (string)  \n *Example:* JPT.GetSelectedPartsCr()  \n "
  },
  "JPT.GetSelectedGroupsCr": {
    "prefix": "GetSelectedGroupsCr",
    "text": "*Function:* JPT.GetSelectedGroupsCr  \n*Description:* get selected group as string output  \n *Input1:* None  \n *Return:* selected group (string)  \n *Example:* JPT.GetSelectedGroupsCr()  \n "
  },
  "JPT.GetUndoCount": {
    "prefix": "GetUndoCount",
    "text": "*Function:* JPT.GetUndoCount  \n*Description:* Get number of undo action which is capable of running  \n *Input1:* None  \n *Return:* Number of undo action(int)  \n *Example:* JPT.GetUndoCount()  \n "
  },
  "JPT.ClearUndo": {
    "prefix": "ClearUndo",
    "text": "*Function:* JPT.ClearUndo  \n*Description:* Clear Undo list  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.ClearUndo()  \n "
  },
  "JPT.GetRedoCount": {
    "prefix": "GetRedoCount",
    "text": "*Function:* JPT.GetRedoCount  \n*Description:* Get number of redo action which is capable of running  \n *Input1:* None  \n *Return:* Number of redo action(int)  \n *Example:* JPT.GetRedoCount()  \n "
  },
  "JPT.ClearRedo": {
    "prefix": "ClearRedo",
    "text": "*Function:* JPT.ClearRedo  \n*Description:* Clear Redo list  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.ClearRedo()  \n "
  },
  "JPT.GetOpnList": {
    "prefix": "GetOpnList",
    "text": "*Function:* JPT.GetOpnList  \n*Description:* Get list of Launch Operation  \n *Input1:* None  \n *Return:* List of Launch Operation(string)  \n *Example:* JPT.GetOpnList()  \n "
  },
  "JPT.GetMacroLog": {
    "prefix": "GetMacroLog",
    "text": "*Function:* JPT.GetMacroLog  \n*Description:* Get all of the macro in Macro Window  \n *Input1:* None  \n *Return:* List of previous Macro in Macro Window (list string)  \n *Example:* JPT.GetMacroLog()  \n "
  },
  "JPT.GetPythonAPILog": {
    "prefix": "GetPythonAPILog",
    "text": "*Function:* JPT.GetPythonAPILog  \n*Description:* Get log string from python API window  \n *Input1:* None  \n *Return:* List of messages from python API window (list string)  \n *Example:* JPT.GetPythonAPILog()  \n "
  },
  "JPT.ShowHideEntitiesByID": {
    "prefix": "ShowHideEntitiesByID",
    "text": "*Function:* JPT.ShowHideEntitiesByID  \n*Description:* show or hide an entity by id in view  \n *Input1:* DTable type (JPT.DTableType)  \n *Input2:* entity id (int)  \n *Input3:* show/hide option (1,0 or JPT.BoolType)  \n *Return:* None  \n *Example:*   \n // hide a part  \n JPT.ShowHideEntitiesByID(JPT.DTableType.DTABLE_BODY, 1, JPT.BoolType.TRUE_VAL)  \n // show a part  \n JPT.ShowHideEntitiesByID(JPT.DTableType.DTABLE_BODY, 1, JPT.BoolType.FALSE_VAL)  \n "
  },
  "JPT.ShowHideAllParts": {
    "prefix": "ShowHideAllParts",
    "text": "*Function:* JPT.ShowHideAllParts  \n*Description:* show or hide all parts in view  \n *Input1:* show/hide option (1,0 or JPT.BoolType)  \n *Return:* None  \n *Example:*   \n // show all parts  \n JPT.ShowHideAllParts(JPT.BoolType.TRUE_VAL)  \n // hide all parts  \n JPT.ShowHideAllParts(JPT.BoolType.FALSE_VAL)  \n "
  },
  "JPT.InverseHideBodies": {
    "prefix": "InverseHideBodies",
    "text": "*Function:* JPT.InverseHideBodies  \n*Description:* inverse hide parts in view  \n *Input1:* id of part (int)  \n *Return:* None  \n *Example:*   \n listbody = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, \"Cube1\", 1)  \n idbody = listbody[0].id  \n JPT.InverseHideBodies(idbody)  \n "
  },
  "JPT.ViewFitToModel": {
    "prefix": "ViewFitToModel",
    "text": "*Function:* JPT.ViewFitToModel  \n*Description:* fit models to current view  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.ViewFitToModel()  \n "
  },
  "JPT.Exec": {
    "prefix": "Exec",
    "text": "*Function:* JPT.Exec  \n*Description:* Run Jupiter macro  \n *Input1:* Macro command (string)  \n *Return:* Refer each macro command(string)  \n *Example: JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], \"Cube_1\", 7105764, 0:*0) ')  \n "
  },
  "JPT.GetMaxIDEntity": {
    "prefix": "GetMaxIDEntity",
    "text": "*Function:* JPT.GetMaxIDEntity  \n*Description:* get max id entity from DItem type  \n *Input1:* DItem type (JPT.EntityType)  \n *Return:* max id entity (int)   \n *Example:* JPT.GetMaxIDEntity(JPT.EntityType.BODY)  \n "
  },
  "JPT.GetMinIDEntity": {
    "prefix": "GetMinIDEntity",
    "text": "*Function:* JPT.GetMinIDEntity  \n*Description:* get min id entity from DItem type  \n *Input1:* DItem type (JPT.EntityType)  \n *Return:* min id entity (int)   \n *Example:* JPT.GetMinIDEntity(JPT.EntityType.BODY)  \n "
  },
  "JPT.GetEntitiesByName": {
    "prefix": "GetEntitiesByName",
    "text": "*Function:* JPT.GetEntitiesByName  \n*Description:* get list of object entity by name  \n *Input1:* DTableType type (JPT.DTableType)  \n *Input2:* name of entity (string)  \n *Input3:* match with name option (1,0 or JPT.BoolType)  \n *Return:* list of object entity (DItemVector)  \n *Example:* listbody = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, \"Cube1\", 1)  \n "
  },
  "JPT.GetEntitiesByID": {
    "prefix": "GetEntitiesByID",
    "text": "*Function:* JPT.GetEntitiesByID  \n*Description:* get list of object entity by id  \n *Input1:* DItem type (JPT.EntityType)  \n *Input2:* id entity (int)   \n *Return:* list of object entity (DItemVector)  \n *Example:* listbody = JPT.GetEntitiesByID(JPT.EntityType.BODY, 1)  \n "
  },
  "JPT.GetEntitiesByPosition": {
    "prefix": "GetEntitiesByPosition",
    "text": "*Function:* JPT.GetEntitiesByPosition  \n*Description:* get list of entity object by position  \n *Input1:* AssociateType type (JPT.AssociateType)  \n *Input2:* x (double)    \n *Input3:* y (double)   \n *Input4:* z (double)   \n *Return:* list of DItem object (DItemVector)  \n *Example:* JPT.GetEntitiesByPosition(JPT.AssociateType.AS_BODY, 1, 2, 3)  \n "
  },
  "JPT.GetEntitiesByAssociation": {
    "prefix": "GetEntitiesByAssociation",
    "text": "*Function:* JPT.GetEntitiesByAssociation  \n*Description:* get list of entity object by association  \n *Input1:* DItem type of parent entity (JPT.EntityType)  \n *Input2:* AssociateType type (JPT.AssociateType)  \n *Input3:* id entity (int)   \n *Return:* list of DItem object (DItemVector)  \n *Example:* JPT.GetEntitiesByAssociation(JPT.EntityType.BODY, JPT.AssociateType.AS_FACE, 1)  \n "
  },
  "JPT.GetEntitiesByAdjacent": {
    "prefix": "GetEntitiesByAdjacent",
    "text": "*Function:* JPT.GetEntitiesByAdjacent  \n*Description:* get list of entity object by adjacency  \n *Input1:* only DItem Face/Element type (JPT.EntityType)  \n *Input2:* id entity (int)    \n *Input3:* stop angle (int)  \n *Return:* list of DItem object (DItemVector)  \n *Example:* JPT.GetEntitiesByAdjacent(JPT.EntityType.FACE, 1, 30)  \n "
  },
  "JPT.MsgOut": {
    "prefix": "MsgOut",
    "text": "*Function:* JPT.MsgOut  \n*Description:* print out message to Python API window (~ print())  \n *Input1:* message (string)  \n *Return:* None  \n *Example:* JPT.MsgOut(\"this is test message\")  \n "
  },
  "JPT.PrintAppPathInfo": {
    "prefix": "PrintAppPathInfo",
    "text": "*Function:* JPT.PrintAppPathInfo  \n*Description:* print all JPT path information (Program, Temp, Appdata, Document)  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.PrintAppPathInfo()  \n "
  },
  "JPT.PrintPSJUtilityManual": {
    "prefix": "PrintPSJUtilityManual",
    "text": "*Function:* JPT.PrintPSJUtilityManual  \n*Description:* Print PSJ Utility Manual Information  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.PrintPSJUtilityManual()  \n "
  },
  "JPT.Debugger": {
    "prefix": "Debugger",
    "text": "*Function:* JPT.Debugger  \n*Description:* console debugger for PSJ   \n *Input1:* any type, any argument number  \n *Return:* None  \n *Example:*   \n // debug enum type  \n JPT.Debugger(JPT.EntityType.values)   \n // debug python standard type  \n JPT.Debugger(1, \"abcd\", list, tuble, dict, ....)  \n // debug Jupiter data type  \n JPT.Debugger(JPT.GetAllNodes()[0].id)  \n JPT.Debugger(JPT.GetAllNodes()[0])  \n JPT.Debugger(JPT.GetAllNodes())  \n "
  },
  "JPT.GetElemsByKind": {
    "prefix": "GetElemsByKind",
    "text": "*Function:* JPT.GetElemsByKind  \n*Description:* get list of element object by kind  \n *Input1:* element kind (JPT.ElemKind)  \n *Return:* list of Elem object (ElemVector)  \n *Example:* listElemObject = JPT.GetElemsByKind(JPT.ElemKind.ELEMKIND_2D)  \n "
  },
  "JPT.GetRandomJPTColor": {
    "prefix": "GetRandomJPTColor",
    "text": "*Function:* JPT.GetRandomJPTColor  \n*Description:* get a random color   \n *Input1:* None  \n *Return:* random color number (int)  \n *Example:* color = JPT.GetRandomJPTColor()  \n "
  },
  "JPT.ConvertJPTColorToRGB": {
    "prefix": "ConvertJPTColorToRGB",
    "text": "*Function:* JPT.ConvertJPTColorToRGB  \n*Description:* convert JPT color to string RGB (red, green, blue)  \n *Input1:* JPT color (int)  \n *Return:* string RGB (string)  \n *Example:* stringRGB = JPT.ConvertJPTColorToRGB(255)  \n "
  },
  "JPT.ClearLog": {
    "prefix": "ClearLog",
    "text": "*Function:* JPT.ClearLog  \n*Description:* clear all log on Python API Window  \n *Input1:* None  \n *Return:* None  \n *Example:* JPT.ClearLog()  \n *Description:* return size of list  \n *Input1:* None  \n *Return:* None  \n *Example:* objectVector.sizeVec()  \n *Description:* clear all element in list, size reset to zero  \n *Input1:* None  \n *Return:* None  \n *Example:* objectVector.clearVec()  \n *Description:* append an entity to current list  \n *Input1:* entity object  \n *Return:* Node  \n *Example:* objectVector.addObj(entityObject)  \n *Description:* insert another list entity to current list  \n *Input1:* list of object  \n *Return:* None  \n *Example:* objectVector1.extendVec(objectVector2)  \n *Description:* delete a entity in list by index  \n *Input1:* None  \n *Return:* None  \n *Example:* objectVector.deleteObj(1)  \n *Description:* check if entityObject is exist in current list  \n *Input1:* None  \n *Return:* TRUE if existed/FALSE if not  \n *Example:* objectVector.isContainObj(entityObject)  \n "
  },
  "JPT.SetSelectMethod": {
    "prefix": "SetSelectMethod",
    "text": "*Function:* JPT.SetSelectMethod  \n*Description:* set select method on view   \n *Input1:* select method type (JPT.SelectMethodType)  \n *Return:* None  \n *Example:* JPT.SetSelector(JPT.SelectMethodType.SELMTD_BODY)  \n "
  },
  "JPT.MacroTCursorPairToDItemPair": {
    "prefix": "MacroTCursorPairToDItemPair",
    "text": "*Function:* JPT.MacroTCursorPairToDItemPair  \n*Description:* convert a macro cursor pair string to DItemPair objects  \n *Input1:* macro cursor pair string (string)  \n *Return:* DItemPair objects (DItemPair)  \n *Example: listEntityObject = JPT.MacroTCursorPairToDItemPair('10:210-10:*202')  \n "
  },
  "JPT.MessageBoxPSJ": {
    "prefix": "MessageBoxPSJ",
    "text": "*Function:* JPT.MessageBoxPSJ  \n*Description:* display a message box  \n *Input1:* message (string)  \n *Input2:* message type (JPT.MsgBoxType)  \n *Return: anwser :* YES, NO, OK, CANCEL (string)  \n *Example:* anwser = JPT.MessageBoxPSJ(\"this is test message, JPT.MsgBoxType.MB_INFORMATION_OKCANCEL)  \n "
  },
  "JPT.GetProgramVersion": {
    "prefix": "GetProgramVersion",
    "text": "*Function:* JPT.GetProgramVersion  \n*Description:* get jupiter version   \n *Input:* None  \n *Return:* VersionInfo object (VersionInfo)  \n *Example:* versionInfo = JPT.GetProgramVersion()  \n print(versionInfo.major)  \n print(versionInfo.minor)  \n print(versionInfo.sub)  \n print(versionInfo.build)  \n "
  },
  "JPT.GetMaterialFromProperty": {
    "prefix": "GetMaterialFromProperty",
    "text": "*Function:* JPT.GetMaterialFromProperty  \n*Description:* get material from property ID  \n *Input:* property ID (init)  \n *Return:* DItem object (DItem)  \n *Example:* material = JPT.GetMaterialFromProperty(1)  \n "
  },
  "JPT.GetAllCoordinates": {
    "prefix": "GetAllCoordinates",
    "text": "*Function:* JPT.GetAllCoordinates  \n*Description:* get jupiter version   \n *Input:* None  \n *Return:* list of DCoord object (CoordVector)  \n *Example:* coordinate = JPT.GetAllCoordinates()  \n "
  },
  "JPT.GetAllConnections": {
    "prefix": "GetAllConnections",
    "text": "*Function:* JPT.GetAllConnections  \n*Description:* get jupiter version   \n *Input:* None  \n *Return:* list of DConnect object (ConnectVector)  \n *Example:* connection = JPT.GetAllConnections()  \n "
  },
  "JPT.GetAllLoadBoundaryConditions": {
    "prefix": "GetAllLoadBoundaryConditions",
    "text": "*Function:* JPT.GetAllLoadBoundaryConditions  \n*Description:* get jupiter version   \n *Input:* None  \n *Return:* list of DLoadBC object (LoadBCVector)  \n *Example:* lbcs = JPT.GetAllLoadBoundaryConditions()  \n "
  },
  "JPT.GetThicknessOfEntity": {
    "prefix": "GetThicknessOfEntity",
    "text": "*Function:* JPT.GetThicknessOfEntity  \n*Description:* get thickness of body or face or element   \n *Input1:* only DItem Body/Face/Element type (JPT.EntityType)  \n *Input2:* id entity (int)    \n *Return:* double thickness of entity  \n *Example:* dThickness = JPT.GetThicknessOfEntity(JPT.EntityType.FACE, 1)  \n "
  },
  "Analysis.AbaqusStep.DynamicCoupledTDExplicitStep": {
    "prefix": "DynamicCoupledTDExplicitStep",
    "text": "**Analysis.AbaqusStep.DynamicCoupledTDExplicitStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "Analysis.AbaqusStep.StaticStep": {
    "prefix": "StaticStep",
    "text": "**Analysis.AbaqusStep.StaticStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "Analysis.ADVC.MakeProcess.RDNLK": {
    "prefix": "RDNLK",
    "text": "**Analysis.ADVC.MakeProcess.RDNLK**  \nPSJ command. See the reference for arguments and usage."
  },
  "Analysis.Ansys.HeatTransferSteady": {
    "prefix": "HeatTransferSteady",
    "text": "**Analysis.Ansys.HeatTransferSteady**  \nPSJ command. See the reference for arguments and usage."
  },
  "Analysis.Nastran.ModalComplexEigenvalue": {
    "prefix": "ModalComplexEigenvalue",
    "text": "**Analysis.Nastran.ModalComplexEigenvalue**  \nPSJ command. See the reference for arguments and usage."
  },
  "Analysis.TSSS.ElectromagneticFrequencyResponse": {
    "prefix": "ElectromagneticFrequencyResponse",
    "text": "**Analysis.TSSS.ElectromagneticFrequencyResponse**  \nPSJ command. See the reference for arguments and usage."
  },
  "Analysis.Akselos_inp": {
    "prefix": "Akselos_inp",
    "text": "**Analysis.Akselos_inp**  \nPSJ command. See the reference for arguments and usage."
  },
  "Analysis.NastranImplicitNonlinear": {
    "prefix": "NastranImplicitNonlinear",
    "text": "**Analysis.NastranImplicitNonlinear**  \nPSJ command. See the reference for arguments and usage."
  },
  "Assemble.BooleanEx": {
    "prefix": "BooleanEx",
    "text": "**Assemble.BooleanEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "Assemble.AssembleFaceEx": {
    "prefix": "AssembleFaceEx",
    "text": "**Assemble.AssembleFaceEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "Assemble.FindMatingFaceEx": {
    "prefix": "FindMatingFaceEx",
    "text": "**Assemble.FindMatingFaceEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "Assemble.AddRibPart": {
    "prefix": "AddRibPart",
    "text": "**Assemble.AddRibPart**  \nPSJ command. See the reference for arguments and usage."
  },
  "Assemble.ConvertToSharedFaces": {
    "prefix": "ConvertToSharedFaces",
    "text": "**Assemble.ConvertToSharedFaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "BoundaryConditions.BodyLoads.AccelerationLoadACCEL": {
    "prefix": "AccelerationLoadACCEL",
    "text": "**BoundaryConditions.BodyLoads.AccelerationLoadACCEL**  \nPSJ command. See the reference for arguments and usage."
  },
  "BoundaryConditions.BodyLoads.AccelerationLoadACCEL1": {
    "prefix": "AccelerationLoadACCEL1",
    "text": "**BoundaryConditions.BodyLoads.AccelerationLoadACCEL1**  \nPSJ command. See the reference for arguments and usage."
  },
  "BoundaryConditions.Force.NonlinearForce.NOLIN3": {
    "prefix": "NOLIN3",
    "text": "**BoundaryConditions.Force.NonlinearForce.NOLIN3**  \nPSJ command. See the reference for arguments and usage."
  },
  "BoundaryConditions.Force.NonlinearForce.NOLIN4": {
    "prefix": "NOLIN4",
    "text": "**BoundaryConditions.Force.NonlinearForce.NOLIN4**  \nPSJ command. See the reference for arguments and usage."
  },
  "BoundaryConditions.Force.NonlinearForce.NOLIN1": {
    "prefix": "NOLIN1",
    "text": "**BoundaryConditions.Force.NonlinearForce.NOLIN1**  \nPSJ command. See the reference for arguments and usage."
  },
  "BoundaryConditions.Force.NormalDirection": {
    "prefix": "NormalDirection",
    "text": "**BoundaryConditions.Force.NormalDirection**  \nPSJ command. See the reference for arguments and usage."
  },
  "BoundaryConditions.Pressure.By2Nodes": {
    "prefix": "By2Nodes",
    "text": "**BoundaryConditions.Pressure.By2Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "BoundaryConditions.Coil": {
    "prefix": "Coil",
    "text": "**BoundaryConditions.Coil**  \nPSJ command. See the reference for arguments and usage."
  },
  "BoundaryConditions.ExternalCurrentDensity": {
    "prefix": "ExternalCurrentDensity",
    "text": "**BoundaryConditions.ExternalCurrentDensity**  \nPSJ command. See the reference for arguments and usage."
  },
  "C01_CarACTools.ACModelCreationTools.MeshedFace": {
    "prefix": "MeshedFace",
    "text": "**C01_CarACTools.ACModelCreationTools.MeshedFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "C01_CarACTools.ClearanceElement.Connect": {
    "prefix": "Connect",
    "text": "**C01_CarACTools.ClearanceElement.Connect**  \nPSJ command. See the reference for arguments and usage."
  },
  "C01_CarACTools.ClearanceElement.Edit": {
    "prefix": "Edit",
    "text": "**C01_CarACTools.ClearanceElement.Edit**  \nPSJ command. See the reference for arguments and usage."
  },
  "C01_CarACTools.Repair.CloseHoleEx": {
    "prefix": "CloseHoleEx",
    "text": "**C01_CarACTools.Repair.CloseHoleEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "C01_CarACTools.Repair.FindHoleEx": {
    "prefix": "FindHoleEx",
    "text": "**C01_CarACTools.Repair.FindHoleEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "CabinACTools.Repair.FindHoleEx": {
    "prefix": "FindHoleEx",
    "text": "**CabinACTools.Repair.FindHoleEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "CabinACTools.Repair.CloseHoleEx": {
    "prefix": "CloseHoleEx",
    "text": "**CabinACTools.Repair.CloseHoleEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.AcousticAnalysis.TransmissionLoss.PCHResult": {
    "prefix": "PCHResult",
    "text": "**Calculation.AcousticAnalysis.TransmissionLoss.PCHResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.AcousticAnalysis.TransmissionLoss.TransmissionLossCondition": {
    "prefix": "TransmissionLossCondition",
    "text": "**Calculation.AcousticAnalysis.TransmissionLoss.TransmissionLossCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.AcousticAnalysis.PanelContribution": {
    "prefix": "PanelContribution",
    "text": "**Calculation.AcousticAnalysis.PanelContribution**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.AcousticAnalysis.PanelContributionCreateGraph": {
    "prefix": "PanelContributionCreateGraph",
    "text": "**Calculation.AcousticAnalysis.PanelContributionCreateGraph**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.AcousticAnalysis.ActranPltImport": {
    "prefix": "ActranPltImport",
    "text": "**Calculation.AcousticAnalysis.ActranPltImport**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.AcousticAnalysis.AcousticIntensity": {
    "prefix": "AcousticIntensity",
    "text": "**Calculation.AcousticAnalysis.AcousticIntensity**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.AcousticAnalysis.ACCombinedAnimation": {
    "prefix": "ACCombinedAnimation",
    "text": "**Calculation.AcousticAnalysis.ACCombinedAnimation**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FFTAnalysis.SetCondition": {
    "prefix": "SetCondition",
    "text": "**Calculation.FFTAnalysis.SetCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FFTAnalysis.XYPlot": {
    "prefix": "XYPlot",
    "text": "**Calculation.FFTAnalysis.XYPlot**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FFTAnalysis.CirclePlot": {
    "prefix": "CirclePlot",
    "text": "**Calculation.FFTAnalysis.CirclePlot**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FFTAnalysis.SectionGraph": {
    "prefix": "SectionGraph",
    "text": "**Calculation.FFTAnalysis.SectionGraph**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FFTAnalysis.CircleGraph": {
    "prefix": "CircleGraph",
    "text": "**Calculation.FFTAnalysis.CircleGraph**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FFTAnalysis.CopyCondition": {
    "prefix": "CopyCondition",
    "text": "**Calculation.FFTAnalysis.CopyCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqResp.MPFMCFCalculation.TotalMPC": {
    "prefix": "TotalMPC",
    "text": "**Calculation.FreqResp.MPFMCFCalculation.TotalMPC**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqResp.MPFMCFCalculation.AtFrequency": {
    "prefix": "AtFrequency",
    "text": "**Calculation.FreqResp.MPFMCFCalculation.AtFrequency**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqResp.MPFMCFCalculation.SaveMPCResultToCSV": {
    "prefix": "SaveMPCResultToCSV",
    "text": "**Calculation.FreqResp.MPFMCFCalculation.SaveMPCResultToCSV**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqResp.LoadCondition": {
    "prefix": "LoadCondition",
    "text": "**Calculation.FreqResp.LoadCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqResp.SaveAnalysis": {
    "prefix": "SaveAnalysis",
    "text": "**Calculation.FreqResp.SaveAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqResp.OpenAnalysis": {
    "prefix": "OpenAnalysis",
    "text": "**Calculation.FreqResp.OpenAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqResp.LoadCaseCondition": {
    "prefix": "LoadCaseCondition",
    "text": "**Calculation.FreqResp.LoadCaseCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqResp.ResponseCondition": {
    "prefix": "ResponseCondition",
    "text": "**Calculation.FreqResp.ResponseCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqResp.ResponseConditionNewResult": {
    "prefix": "ResponseConditionNewResult",
    "text": "**Calculation.FreqResp.ResponseConditionNewResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqResp.LoadCase": {
    "prefix": "LoadCase",
    "text": "**Calculation.FreqResp.LoadCase**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqRespSolver.LoadCondition": {
    "prefix": "LoadCondition",
    "text": "**Calculation.FreqRespSolver.LoadCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FreqRespSolver.ResponseCondition": {
    "prefix": "ResponseCondition",
    "text": "**Calculation.FreqRespSolver.ResponseCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.Gururi.Sweep": {
    "prefix": "Sweep",
    "text": "**Calculation.Gururi.Sweep**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.Gururi.Response": {
    "prefix": "Response",
    "text": "**Calculation.Gururi.Response**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.Gururi.LoadCondition": {
    "prefix": "LoadCondition",
    "text": "**Calculation.Gururi.LoadCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.Gururi.LoadCase": {
    "prefix": "LoadCase",
    "text": "**Calculation.Gururi.LoadCase**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.StrainGauge.AxisWithAngle": {
    "prefix": "AxisWithAngle",
    "text": "**Calculation.StrainGauge.AxisWithAngle**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.StrainGauge.DirectionCosine": {
    "prefix": "DirectionCosine",
    "text": "**Calculation.StrainGauge.DirectionCosine**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.StrainGauge.ExistingResult": {
    "prefix": "ExistingResult",
    "text": "**Calculation.StrainGauge.ExistingResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.StrainGauge.MaxMinPrincipal": {
    "prefix": "MaxMinPrincipal",
    "text": "**Calculation.StrainGauge.MaxMinPrincipal**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.StrainGauge.TangentProjection": {
    "prefix": "TangentProjection",
    "text": "**Calculation.StrainGauge.TangentProjection**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.StrainGauge.TwoPoints": {
    "prefix": "TwoPoints",
    "text": "**Calculation.StrainGauge.TwoPoints**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.StrainGauge.NodePoint": {
    "prefix": "NodePoint",
    "text": "**Calculation.StrainGauge.NodePoint**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.Subcase.convertSubCaseIDtoNativeStr": {
    "prefix": "convertSubCaseIDtoNativeStr",
    "text": "**Calculation.Subcase.convertSubCaseIDtoNativeStr**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.Subcase.ShowSafety": {
    "prefix": "ShowSafety",
    "text": "**Calculation.Subcase.ShowSafety**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.Subcase.PeakHold": {
    "prefix": "PeakHold",
    "text": "**Calculation.Subcase.PeakHold**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.Subcase.RelativeOffset": {
    "prefix": "RelativeOffset",
    "text": "**Calculation.Subcase.RelativeOffset**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.Subcase.Fatigue": {
    "prefix": "Fatigue",
    "text": "**Calculation.Subcase.Fatigue**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.SurfaceDistance.DistanceCalculate": {
    "prefix": "DistanceCalculate",
    "text": "**Calculation.SurfaceDistance.DistanceCalculate**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.TransResp.MPFMCFCalculation.TotalMPC": {
    "prefix": "TotalMPC",
    "text": "**Calculation.TransResp.MPFMCFCalculation.TotalMPC**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.TransResp.MPFMCFCalculation.AtTime": {
    "prefix": "AtTime",
    "text": "**Calculation.TransResp.MPFMCFCalculation.AtTime**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.TransResp.MPFMCFCalculation.SaveMPCResultToCSV": {
    "prefix": "SaveMPCResultToCSV",
    "text": "**Calculation.TransResp.MPFMCFCalculation.SaveMPCResultToCSV**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.TransResp.SaveAnalysis": {
    "prefix": "SaveAnalysis",
    "text": "**Calculation.TransResp.SaveAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.TransResp.OpenAnalysis": {
    "prefix": "OpenAnalysis",
    "text": "**Calculation.TransResp.OpenAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.TransResp.LoadCondition": {
    "prefix": "LoadCondition",
    "text": "**Calculation.TransResp.LoadCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.TransResp.LoadCaseCondition": {
    "prefix": "LoadCaseCondition",
    "text": "**Calculation.TransResp.LoadCaseCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.TransResp.ResponseCondition": {
    "prefix": "ResponseCondition",
    "text": "**Calculation.TransResp.ResponseCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.TransResp.ResponseConditionNewResult": {
    "prefix": "ResponseConditionNewResult",
    "text": "**Calculation.TransResp.ResponseConditionNewResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.TransRespSolver.LoadCondition": {
    "prefix": "LoadCondition",
    "text": "**Calculation.TransRespSolver.LoadCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.RotateMapping": {
    "prefix": "RotateMapping",
    "text": "**Calculation.RotateMapping**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.RotateMappingExportUnv": {
    "prefix": "RotateMappingExportUnv",
    "text": "**Calculation.RotateMappingExportUnv**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.UserResult": {
    "prefix": "UserResult",
    "text": "**Calculation.UserResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.PeakSearch": {
    "prefix": "PeakSearch",
    "text": "**Calculation.PeakSearch**  \nPSJ command. See the reference for arguments and usage."
  },
  "Calculation.FatigueMaterial": {
    "prefix": "FatigueMaterial",
    "text": "**Calculation.FatigueMaterial**  \nPSJ command. See the reference for arguments and usage."
  },
  "Chart.CreateGraph": {
    "prefix": "CreateGraph",
    "text": "**Chart.CreateGraph**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Contacts.Abaqus.ContactTable_Abaqus": {
    "prefix": "ContactTable_Abaqus",
    "text": "**Connections.Contacts.Abaqus.ContactTable_Abaqus**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Contacts.ADVC.ContactTable_Advc": {
    "prefix": "ContactTable_Advc",
    "text": "**Connections.Contacts.ADVC.ContactTable_Advc**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Contacts.MSCNastran.ManualGroupBCTABL1": {
    "prefix": "ManualGroupBCTABL1",
    "text": "**Connections.Contacts.MSCNastran.ManualGroupBCTABL1**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Contacts.MSCNastran.ManualFaceBCTABL1": {
    "prefix": "ManualFaceBCTABL1",
    "text": "**Connections.Contacts.MSCNastran.ManualFaceBCTABL1**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Contacts.MSCNastran.ContactShareFaceBCTABL1": {
    "prefix": "ContactShareFaceBCTABL1",
    "text": "**Connections.Contacts.MSCNastran.ContactShareFaceBCTABL1**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Contacts.MSCNastran.ContactBodyParamBCBDPRP": {
    "prefix": "ContactBodyParamBCBDPRP",
    "text": "**Connections.Contacts.MSCNastran.ContactBodyParamBCBDPRP**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Contacts.MSCNastran.PhysicalContactParamBCBDPRP": {
    "prefix": "PhysicalContactParamBCBDPRP",
    "text": "**Connections.Contacts.MSCNastran.PhysicalContactParamBCBDPRP**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Contacts.SunShine.ManualFace": {
    "prefix": "ManualFace",
    "text": "**Connections.Contacts.SunShine.ManualFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Contacts.TSSS.ContactTable_TSSS": {
    "prefix": "ContactTable_TSSS",
    "text": "**Connections.Contacts.TSSS.ContactTable_TSSS**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Contacts.AutoConvertContact": {
    "prefix": "AutoConvertContact",
    "text": "**Connections.Contacts.AutoConvertContact**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.MPC.Equation.MultipleNodes": {
    "prefix": "MultipleNodes",
    "text": "**Connections.MPC.Equation.MultipleNodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.MPC.Equation.TwoFaces": {
    "prefix": "TwoFaces",
    "text": "**Connections.MPC.Equation.TwoFaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.MPC.General.TwoNodes": {
    "prefix": "TwoNodes",
    "text": "**Connections.MPC.General.TwoNodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Pretension.SunShine": {
    "prefix": "SunShine",
    "text": "**Connections.Pretension.SunShine**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.Pretension.MscNastran": {
    "prefix": "MscNastran",
    "text": "**Connections.Pretension.MscNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.RigidElements.RBE2General": {
    "prefix": "RBE2General",
    "text": "**Connections.RigidElements.RBE2General**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.RigidElements.RBE3General": {
    "prefix": "RBE3General",
    "text": "**Connections.RigidElements.RBE3General**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.SpringsDampers.Damper.AnyEntities11DoFS": {
    "prefix": "AnyEntities11DoFS",
    "text": "**Connections.SpringsDampers.Damper.AnyEntities11DoFS**  \nPSJ command. See the reference for arguments and usage."
  },
  "Connections.RBE3": {
    "prefix": "RBE3",
    "text": "**Connections.RBE3**  \nPSJ command. See the reference for arguments and usage."
  },
  "Exchange.ReplaceSolidMesh": {
    "prefix": "ReplaceSolidMesh",
    "text": "**Exchange.ReplaceSolidMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "Exchange.ClayWork": {
    "prefix": "ClayWork",
    "text": "**Exchange.ClayWork**  \nPSJ command. See the reference for arguments and usage."
  },
  "Exchange.AssembleSolidMesh": {
    "prefix": "AssembleSolidMesh",
    "text": "**Exchange.AssembleSolidMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "ExManifoldModeling.SZ.WeldLine2": {
    "prefix": "WeldLine2",
    "text": "**ExManifoldModeling.SZ.WeldLine2**  \nPSJ command. See the reference for arguments and usage."
  },
  "FileMenu.LoadJTDB": {
    "prefix": "LoadJTDB",
    "text": "**FileMenu.LoadJTDB**  \nPSJ command. See the reference for arguments and usage."
  },
  "FileMenu.SaveJTDB": {
    "prefix": "SaveJTDB",
    "text": "**FileMenu.SaveJTDB**  \nPSJ command. See the reference for arguments and usage."
  },
  "FileMenu.SaveJTH5": {
    "prefix": "SaveJTH5",
    "text": "**FileMenu.SaveJTH5**  \nPSJ command. See the reference for arguments and usage."
  },
  "FileMenu.LoadJTH5": {
    "prefix": "LoadJTH5",
    "text": "**FileMenu.LoadJTH5**  \nPSJ command. See the reference for arguments and usage."
  },
  "FileMenu.SavePOH5": {
    "prefix": "SavePOH5",
    "text": "**FileMenu.SavePOH5**  \nPSJ command. See the reference for arguments and usage."
  },
  "FileMenu.LoadPOH5": {
    "prefix": "LoadPOH5",
    "text": "**FileMenu.LoadPOH5**  \nPSJ command. See the reference for arguments and usage."
  },
  "FOWT.Analysis.AnalysisStaic": {
    "prefix": "AnalysisStaic",
    "text": "**FOWT.Analysis.AnalysisStaic**  \nPSJ command. See the reference for arguments and usage."
  },
  "FOWT.Analysis.AnalysisDynamic": {
    "prefix": "AnalysisDynamic",
    "text": "**FOWT.Analysis.AnalysisDynamic**  \nPSJ command. See the reference for arguments and usage."
  },
  "FOWT.MooringForce": {
    "prefix": "MooringForce",
    "text": "**FOWT.MooringForce**  \nPSJ command. See the reference for arguments and usage."
  },
  "FOWT.ExternalPressure": {
    "prefix": "ExternalPressure",
    "text": "**FOWT.ExternalPressure**  \nPSJ command. See the reference for arguments and usage."
  },
  "FOWT.InertialForce": {
    "prefix": "InertialForce",
    "text": "**FOWT.InertialForce**  \nPSJ command. See the reference for arguments and usage."
  },
  "FOWT.Acceleration": {
    "prefix": "Acceleration",
    "text": "**FOWT.Acceleration**  \nPSJ command. See the reference for arguments and usage."
  },
  "FOWT.MappingAcceleration": {
    "prefix": "MappingAcceleration",
    "text": "**FOWT.MappingAcceleration**  \nPSJ command. See the reference for arguments and usage."
  },
  "FOWT.LoadsTransmittedFromRNA": {
    "prefix": "LoadsTransmittedFromRNA",
    "text": "**FOWT.LoadsTransmittedFromRNA**  \nPSJ command. See the reference for arguments and usage."
  },
  "FOWT.WindLoad": {
    "prefix": "WindLoad",
    "text": "**FOWT.WindLoad**  \nPSJ command. See the reference for arguments and usage."
  },
  "FOWT.MooringForce_RNA": {
    "prefix": "MooringForce_RNA",
    "text": "**FOWT.MooringForce_RNA**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.BodyCut.By3Points": {
    "prefix": "By3Points",
    "text": "**Geometry.BodyCut.By3Points**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.Edge.LineInBetween": {
    "prefix": "LineInBetween",
    "text": "**Geometry.Edge.LineInBetween**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.FindFeature.Edge": {
    "prefix": "Edge",
    "text": "**Geometry.FindFeature.Edge**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.FindFeature.Face": {
    "prefix": "Face",
    "text": "**Geometry.FindFeature.Face**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.MergeEntities.MergeTinyFaces": {
    "prefix": "MergeTinyFaces",
    "text": "**Geometry.MergeEntities.MergeTinyFaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.Part.Frustum": {
    "prefix": "Frustum",
    "text": "**Geometry.Part.Frustum**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.Transform.ThreePoints": {
    "prefix": "ThreePoints",
    "text": "**Geometry.Transform.ThreePoints**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.Transform.AxisAlignment": {
    "prefix": "AxisAlignment",
    "text": "**Geometry.Transform.AxisAlignment**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.Transform.PlaneAlignment": {
    "prefix": "PlaneAlignment",
    "text": "**Geometry.Transform.PlaneAlignment**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.Transform.BestFit": {
    "prefix": "BestFit",
    "text": "**Geometry.Transform.BestFit**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.CreateROnBar": {
    "prefix": "CreateROnBar",
    "text": "**Geometry.CreateROnBar**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.ExtractRefSurfaces": {
    "prefix": "ExtractRefSurfaces",
    "text": "**Geometry.ExtractRefSurfaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.ShipFormMorphing": {
    "prefix": "ShipFormMorphing",
    "text": "**Geometry.ShipFormMorphing**  \nPSJ command. See the reference for arguments and usage."
  },
  "Geometry.MakeFaceSmoothFunc": {
    "prefix": "MakeFaceSmoothFunc",
    "text": "**Geometry.MakeFaceSmoothFunc**  \nPSJ command. See the reference for arguments and usage."
  },
  "Groups.RightClick.AddSubGroup": {
    "prefix": "AddSubGroup",
    "text": "**Groups.RightClick.AddSubGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.ImportCAD.GeomBDF": {
    "prefix": "GeomBDF",
    "text": "**Home.ImportCAD.GeomBDF**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.ImportMesh.Ansys": {
    "prefix": "Ansys",
    "text": "**Home.ImportMesh.Ansys**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.ImportMesh.Abaqus": {
    "prefix": "Abaqus",
    "text": "**Home.ImportMesh.Abaqus**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.ImportMesh.LsDyna": {
    "prefix": "LsDyna",
    "text": "**Home.ImportMesh.LsDyna**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.ImportMesh.Marc": {
    "prefix": "Marc",
    "text": "**Home.ImportMesh.Marc**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Preferences.SaveLoad.CalculateTrescaStress": {
    "prefix": "CalculateTrescaStress",
    "text": "**Home.Preferences.SaveLoad.CalculateTrescaStress**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Preferences.Export": {
    "prefix": "Export",
    "text": "**Home.Preferences.Export**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Preferences.Import": {
    "prefix": "Import",
    "text": "**Home.Preferences.Import**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.RectangularCapture.Clipboard": {
    "prefix": "Clipboard",
    "text": "**Home.RectangularCapture.Clipboard**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.RectangularCapture.Single": {
    "prefix": "Single",
    "text": "**Home.RectangularCapture.Single**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.RectangularCapture.Multiple": {
    "prefix": "Multiple",
    "text": "**Home.RectangularCapture.Multiple**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.ViewControl.ResetCenter": {
    "prefix": "ResetCenter",
    "text": "**Home.Windows.ViewControl.ResetCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.ViewControl.SetCenter": {
    "prefix": "SetCenter",
    "text": "**Home.Windows.ViewControl.SetCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.ViewControl.Rotate": {
    "prefix": "Rotate",
    "text": "**Home.Windows.ViewControl.Rotate**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.ViewControl.PanUp": {
    "prefix": "PanUp",
    "text": "**Home.Windows.ViewControl.PanUp**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.ViewControl.PanDown": {
    "prefix": "PanDown",
    "text": "**Home.Windows.ViewControl.PanDown**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.ViewControl.PanRight": {
    "prefix": "PanRight",
    "text": "**Home.Windows.ViewControl.PanRight**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.ViewControl.PanLeft": {
    "prefix": "PanLeft",
    "text": "**Home.Windows.ViewControl.PanLeft**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.ViewControl.ZoomIn": {
    "prefix": "ZoomIn",
    "text": "**Home.Windows.ViewControl.ZoomIn**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.ViewControl.ZoomOut": {
    "prefix": "ZoomOut",
    "text": "**Home.Windows.ViewControl.ZoomOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.ViewControl.FitToModel": {
    "prefix": "FitToModel",
    "text": "**Home.Windows.ViewControl.FitToModel**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.TileBox": {
    "prefix": "TileBox",
    "text": "**Home.Windows.TileBox**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.TileVertical": {
    "prefix": "TileVertical",
    "text": "**Home.Windows.TileVertical**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.TileHorizontal": {
    "prefix": "TileHorizontal",
    "text": "**Home.Windows.TileHorizontal**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.Windows.FrameCancel": {
    "prefix": "FrameCancel",
    "text": "**Home.Windows.FrameCancel**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.ExportGeometrySurface": {
    "prefix": "ExportGeometrySurface",
    "text": "**Home.ExportGeometrySurface**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.EXPORT_UNIVERSAL": {
    "prefix": "EXPORT_UNIVERSAL",
    "text": "**Home.EXPORT_UNIVERSAL**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.ToPPTX": {
    "prefix": "ToPPTX",
    "text": "**Home.ToPPTX**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.ExportPV": {
    "prefix": "ExportPV",
    "text": "**Home.ExportPV**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.ToPPTX_3DModel": {
    "prefix": "ToPPTX_3DModel",
    "text": "**Home.ToPPTX_3DModel**  \nPSJ command. See the reference for arguments and usage."
  },
  "Home.ExportGLB": {
    "prefix": "ExportGLB",
    "text": "**Home.ExportGLB**  \nPSJ command. See the reference for arguments and usage."
  },
  "LabPreRelease.CopyMeshPattern": {
    "prefix": "CopyMeshPattern",
    "text": "**LabPreRelease.CopyMeshPattern**  \nPSJ command. See the reference for arguments and usage."
  },
  "macro_mesh_cleanup.from_list": {
    "prefix": "from_list",
    "text": "**macro_mesh_cleanup.from_list**  \nPSJ command. See the reference for arguments and usage."
  },
  "macro_mesh_cleanup.from_str": {
    "prefix": "from_str",
    "text": "**macro_mesh_cleanup.from_str**  \nPSJ command. See the reference for arguments and usage."
  },
  "macro_mesh_cleanup.__str__": {
    "prefix": "__str__",
    "text": "**macro_mesh_cleanup.__str__**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.SetPartAppearance": {
    "prefix": "SetPartAppearance",
    "text": "**MainWindow.RightClick.SetPartAppearance**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.InverseHide": {
    "prefix": "InverseHide",
    "text": "**MainWindow.RightClick.InverseHide**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.ShowAll": {
    "prefix": "ShowAll",
    "text": "**MainWindow.RightClick.ShowAll**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.ShowAllHiddenFaces": {
    "prefix": "ShowAllHiddenFaces",
    "text": "**MainWindow.RightClick.ShowAllHiddenFaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.ShowSettings": {
    "prefix": "ShowSettings",
    "text": "**MainWindow.RightClick.ShowSettings**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.ShowHideFlip": {
    "prefix": "ShowHideFlip",
    "text": "**MainWindow.RightClick.ShowHideFlip**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.ShowHideAllToolbar": {
    "prefix": "ShowHideAllToolbar",
    "text": "**MainWindow.RightClick.ShowHideAllToolbar**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick._change_select_type": {
    "prefix": "_change_select_type",
    "text": "**MainWindow.RightClick._change_select_type**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.SelectAll": {
    "prefix": "SelectAll",
    "text": "**MainWindow.RightClick.SelectAll**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.SelectDisplayed": {
    "prefix": "SelectDisplayed",
    "text": "**MainWindow.RightClick.SelectDisplayed**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.SelectReverse": {
    "prefix": "SelectReverse",
    "text": "**MainWindow.RightClick.SelectReverse**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.SelectByWindow": {
    "prefix": "SelectByWindow",
    "text": "**MainWindow.RightClick.SelectByWindow**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.SelectByFace": {
    "prefix": "SelectByFace",
    "text": "**MainWindow.RightClick.SelectByFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.SelectByAttached": {
    "prefix": "SelectByAttached",
    "text": "**MainWindow.RightClick.SelectByAttached**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.ShowHideEntity": {
    "prefix": "ShowHideEntity",
    "text": "**MainWindow.RightClick.ShowHideEntity**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.InverseHideAll": {
    "prefix": "InverseHideAll",
    "text": "**MainWindow.RightClick.InverseHideAll**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.RightClick.SelectSurfaceColor": {
    "prefix": "SelectSurfaceColor",
    "text": "**MainWindow.RightClick.SelectSurfaceColor**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.ViewPoint.Add": {
    "prefix": "Add",
    "text": "**MainWindow.ViewPoint.Add**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.ViewPoint.Rename": {
    "prefix": "Rename",
    "text": "**MainWindow.ViewPoint.Rename**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.ViewPoint.Delete": {
    "prefix": "Delete",
    "text": "**MainWindow.ViewPoint.Delete**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.ViewPoint.Import": {
    "prefix": "Import",
    "text": "**MainWindow.ViewPoint.Import**  \nPSJ command. See the reference for arguments and usage."
  },
  "MainWindow.ViewPoint.Export": {
    "prefix": "Export",
    "text": "**MainWindow.ViewPoint.Export**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.AutoCheck._split_results": {
    "prefix": "_split_results",
    "text": "**MeshCleanup.AutoCheck._split_results**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Cleanup.Manual": {
    "prefix": "Manual",
    "text": "**MeshCleanup.Cleanup.Manual**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Cleanup.Auto": {
    "prefix": "Auto",
    "text": "**MeshCleanup.Cleanup.Auto**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual2D.SplitElement.QuadTo4Quads": {
    "prefix": "QuadTo4Quads",
    "text": "**MeshCleanup.Manual2D.SplitElement.QuadTo4Quads**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual2D.SplitElement.QuadToTrans4Quads": {
    "prefix": "QuadToTrans4Quads",
    "text": "**MeshCleanup.Manual2D.SplitElement.QuadToTrans4Quads**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual2D.SplitElement.QuadToTrans3Quads": {
    "prefix": "QuadToTrans3Quads",
    "text": "**MeshCleanup.Manual2D.SplitElement.QuadToTrans3Quads**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual2D.SplitElement.QuadTo2Quads1Tri": {
    "prefix": "QuadTo2Quads1Tri",
    "text": "**MeshCleanup.Manual2D.SplitElement.QuadTo2Quads1Tri**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual2D.SplitElement.QuadTo3Tris": {
    "prefix": "QuadTo3Tris",
    "text": "**MeshCleanup.Manual2D.SplitElement.QuadTo3Tris**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual2D.SplitElement.QuadTo2Quads": {
    "prefix": "QuadTo2Quads",
    "text": "**MeshCleanup.Manual2D.SplitElement.QuadTo2Quads**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual2D.SplitElement.QuadTo2Tris": {
    "prefix": "QuadTo2Tris",
    "text": "**MeshCleanup.Manual2D.SplitElement.QuadTo2Tris**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual2D.SplitElement.QuadTo4Tris": {
    "prefix": "QuadTo4Tris",
    "text": "**MeshCleanup.Manual2D.SplitElement.QuadTo4Tris**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual2D.SplitElement.TriTo4Tris": {
    "prefix": "TriTo4Tris",
    "text": "**MeshCleanup.Manual2D.SplitElement.TriTo4Tris**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual2D.HalfEdgeCollapse": {
    "prefix": "HalfEdgeCollapse",
    "text": "**MeshCleanup.Manual2D.HalfEdgeCollapse**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.Manual3D.Collapse.CenterElementCollapse": {
    "prefix": "CenterElementCollapse",
    "text": "**MeshCleanup.Manual3D.Collapse.CenterElementCollapse**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.ManualCheck._split_results": {
    "prefix": "_split_results",
    "text": "**MeshCleanup.ManualCheck._split_results**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.ManualCheck.Quad": {
    "prefix": "Quad",
    "text": "**MeshCleanup.ManualCheck.Quad**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.ManualCheck.Tet": {
    "prefix": "Tet",
    "text": "**MeshCleanup.ManualCheck.Tet**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.ManualCheck.Hex": {
    "prefix": "Hex",
    "text": "**MeshCleanup.ManualCheck.Hex**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshCleanup.FindHoles": {
    "prefix": "FindHoles",
    "text": "**MeshCleanup.FindHoles**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshEdit.CreateElement.Tri3": {
    "prefix": "Tri3",
    "text": "**MeshEdit.CreateElement.Tri3**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshEdit.CreateElement.Quad4": {
    "prefix": "Quad4",
    "text": "**MeshEdit.CreateElement.Quad4**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshEdit.CreateNode.Node": {
    "prefix": "Node",
    "text": "**MeshEdit.CreateNode.Node**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshEdit.CreateNode.Between3Nodes": {
    "prefix": "Between3Nodes",
    "text": "**MeshEdit.CreateNode.Between3Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshEdit.MoveNode.ProjectToPlane_3Nodes": {
    "prefix": "ProjectToPlane_3Nodes",
    "text": "**MeshEdit.MoveNode.ProjectToPlane_3Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "MeshEdit.QuadMeshCleanupCustom": {
    "prefix": "QuadMeshCleanupCustom",
    "text": "**MeshEdit.QuadMeshCleanupCustom**  \nPSJ command. See the reference for arguments and usage."
  },
  "Meshing.LocalRemesh.Surface": {
    "prefix": "Surface",
    "text": "**Meshing.LocalRemesh.Surface**  \nPSJ command. See the reference for arguments and usage."
  },
  "Meshing.LocalSettings.BoltEdge": {
    "prefix": "BoltEdge",
    "text": "**Meshing.LocalSettings.BoltEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "Meshing.LocalSettings.SaveMeshSetting": {
    "prefix": "SaveMeshSetting",
    "text": "**Meshing.LocalSettings.SaveMeshSetting**  \nPSJ command. See the reference for arguments and usage."
  },
  "Meshing.LocalSettings.LoadMeshSetting": {
    "prefix": "LoadMeshSetting",
    "text": "**Meshing.LocalSettings.LoadMeshSetting**  \nPSJ command. See the reference for arguments and usage."
  },
  "Meshing.SetMeshAttribute": {
    "prefix": "SetMeshAttribute",
    "text": "**Meshing.SetMeshAttribute**  \nPSJ command. See the reference for arguments and usage."
  },
  "Meshing.AdjustCircleVertex": {
    "prefix": "AdjustCircleVertex",
    "text": "**Meshing.AdjustCircleVertex**  \nPSJ command. See the reference for arguments and usage."
  },
  "Meshing.FullQuadRemesh": {
    "prefix": "FullQuadRemesh",
    "text": "**Meshing.FullQuadRemesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "Meshing.AutoFullQuadRemeshForPart": {
    "prefix": "AutoFullQuadRemeshForPart",
    "text": "**Meshing.AutoFullQuadRemeshForPart**  \nPSJ command. See the reference for arguments and usage."
  },
  "MidPlane.PressShell": {
    "prefix": "PressShell",
    "text": "**MidPlane.PressShell**  \nPSJ command. See the reference for arguments and usage."
  },
  "MidPlane.PressShellV2": {
    "prefix": "PressShellV2",
    "text": "**MidPlane.PressShellV2**  \nPSJ command. See the reference for arguments and usage."
  },
  "MuxWeld.Prop3DWeldBead": {
    "prefix": "Prop3DWeldBead",
    "text": "**MuxWeld.Prop3DWeldBead**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ACModelingOut.CreateConvex": {
    "prefix": "CreateConvex",
    "text": "**OutPython.ACModelingOut.CreateConvex**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ACModelingOut.ACModelingCloseHoleAuto": {
    "prefix": "ACModelingCloseHoleAuto",
    "text": "**OutPython.ACModelingOut.ACModelingCloseHoleAuto**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ACModelingOut.ACModellingCut": {
    "prefix": "ACModellingCut",
    "text": "**OutPython.ACModelingOut.ACModellingCut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ACModelingOut.ACBoundaryMethod1": {
    "prefix": "ACBoundaryMethod1",
    "text": "**OutPython.ACModelingOut.ACBoundaryMethod1**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.CreateAbaqusJob": {
    "prefix": "CreateAbaqusJob",
    "text": "**OutPython.AnalysisOut.CreateAbaqusJob**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcCreepProcess": {
    "prefix": "AdvcCreepProcess",
    "text": "**OutPython.AnalysisOut.AdvcCreepProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.ExportAnsys": {
    "prefix": "ExportAnsys",
    "text": "**OutPython.AnalysisOut.ExportAnsys**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcModalFreqRespProcess": {
    "prefix": "AdvcModalFreqRespProcess",
    "text": "**OutPython.AnalysisOut.AdvcModalFreqRespProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.ExportActranBdf": {
    "prefix": "ExportActranBdf",
    "text": "**OutPython.AnalysisOut.ExportActranBdf**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.ExportDynamisBdf": {
    "prefix": "ExportDynamisBdf",
    "text": "**OutPython.AnalysisOut.ExportDynamisBdf**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.PermasJobOut": {
    "prefix": "PermasJobOut",
    "text": "**OutPython.AnalysisOut.PermasJobOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcEigenProcess": {
    "prefix": "AdvcEigenProcess",
    "text": "**OutPython.AnalysisOut.AdvcEigenProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.ExportAbaqusInp": {
    "prefix": "ExportAbaqusInp",
    "text": "**OutPython.AnalysisOut.ExportAbaqusInp**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcDynamicProcess": {
    "prefix": "AdvcDynamicProcess",
    "text": "**OutPython.AnalysisOut.AdvcDynamicProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcSpectrumProcess": {
    "prefix": "AdvcSpectrumProcess",
    "text": "**OutPython.AnalysisOut.AdvcSpectrumProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcSSHProcess": {
    "prefix": "AdvcSSHProcess",
    "text": "**OutPython.AnalysisOut.AdvcSSHProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AbaModifyLbcToStep": {
    "prefix": "AbaModifyLbcToStep",
    "text": "**OutPython.AnalysisOut.AbaModifyLbcToStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcDynamicExplicitProcess": {
    "prefix": "AdvcDynamicExplicitProcess",
    "text": "**OutPython.AnalysisOut.AdvcDynamicExplicitProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.ExportAdx": {
    "prefix": "ExportAdx",
    "text": "**OutPython.AnalysisOut.ExportAdx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.LsdynaJob": {
    "prefix": "LsdynaJob",
    "text": "**OutPython.AnalysisOut.LsdynaJob**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.ExportLsdyna": {
    "prefix": "ExportLsdyna",
    "text": "**OutPython.AnalysisOut.ExportLsdyna**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcStaticProcess": {
    "prefix": "AdvcStaticProcess",
    "text": "**OutPython.AnalysisOut.AdvcStaticProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AbaqusSteadyStateStep": {
    "prefix": "AbaqusSteadyStateStep",
    "text": "**OutPython.AnalysisOut.AbaqusSteadyStateStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.CreateAnsysJob": {
    "prefix": "CreateAnsysJob",
    "text": "**OutPython.AnalysisOut.CreateAnsysJob**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AbaqusStaticRiskStep": {
    "prefix": "AbaqusStaticRiskStep",
    "text": "**OutPython.AnalysisOut.AbaqusStaticRiskStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.NastranJobOut": {
    "prefix": "NastranJobOut",
    "text": "**OutPython.AnalysisOut.NastranJobOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Nastran_ImplicitNonlinear": {
    "prefix": "Nastran_ImplicitNonlinear",
    "text": "**OutPython.AnalysisOut.Nastran_ImplicitNonlinear**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AbaqusDynamicStep": {
    "prefix": "AbaqusDynamicStep",
    "text": "**OutPython.AnalysisOut.AbaqusDynamicStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.DynamisJobOut": {
    "prefix": "DynamisJobOut",
    "text": "**OutPython.AnalysisOut.DynamisJobOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AnalysisActranJob": {
    "prefix": "AnalysisActranJob",
    "text": "**OutPython.AnalysisOut.AnalysisActranJob**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AbaqusTransientStep": {
    "prefix": "AbaqusTransientStep",
    "text": "**OutPython.AnalysisOut.AbaqusTransientStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcJob": {
    "prefix": "AdvcJob",
    "text": "**OutPython.AnalysisOut.AdvcJob**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AbaqusDynamicCoupledTDExplicitStep": {
    "prefix": "AbaqusDynamicCoupledTDExplicitStep",
    "text": "**OutPython.AnalysisOut.AbaqusDynamicCoupledTDExplicitStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AbaqusCoupledTDStep": {
    "prefix": "AbaqusCoupledTDStep",
    "text": "**OutPython.AnalysisOut.AbaqusCoupledTDStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AbaqusDynamicExplicitStep": {
    "prefix": "AbaqusDynamicExplicitStep",
    "text": "**OutPython.AnalysisOut.AbaqusDynamicExplicitStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AbaqusModalStep": {
    "prefix": "AbaqusModalStep",
    "text": "**OutPython.AnalysisOut.AbaqusModalStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSolver_LinearBuckling": {
    "prefix": "TSSolver_LinearBuckling",
    "text": "**OutPython.AnalysisOut.TSSolver_LinearBuckling**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AnalysisActranRun": {
    "prefix": "AnalysisActranRun",
    "text": "**OutPython.AnalysisOut.AnalysisActranRun**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Nastran_ModalTransientResponse": {
    "prefix": "Nastran_ModalTransientResponse",
    "text": "**OutPython.AnalysisOut.Nastran_ModalTransientResponse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Nastran_LinearBuckling": {
    "prefix": "Nastran_LinearBuckling",
    "text": "**OutPython.AnalysisOut.Nastran_LinearBuckling**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Nastran_Transient": {
    "prefix": "Nastran_Transient",
    "text": "**OutPython.AnalysisOut.Nastran_Transient**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSS_TransientHeatTransfer": {
    "prefix": "TSSS_TransientHeatTransfer",
    "text": "**OutPython.AnalysisOut.TSSS_TransientHeatTransfer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSolverLinearStatic": {
    "prefix": "TSSolverLinearStatic",
    "text": "**OutPython.AnalysisOut.TSSolverLinearStatic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSolverNonlinearStatic": {
    "prefix": "TSSolverNonlinearStatic",
    "text": "**OutPython.AnalysisOut.TSSolverNonlinearStatic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSolverNormalModes": {
    "prefix": "TSSolverNormalModes",
    "text": "**OutPython.AnalysisOut.TSSolverNormalModes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSolverNonlinearFrequency": {
    "prefix": "TSSolverNonlinearFrequency",
    "text": "**OutPython.AnalysisOut.TSSolverNonlinearFrequency**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSolverModalTransientResponse": {
    "prefix": "TSSolverModalTransientResponse",
    "text": "**OutPython.AnalysisOut.TSSolverModalTransientResponse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Nastran_SteadyState": {
    "prefix": "Nastran_SteadyState",
    "text": "**OutPython.AnalysisOut.Nastran_SteadyState**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Nastran_ModalFrequencyResponse": {
    "prefix": "Nastran_ModalFrequencyResponse",
    "text": "**OutPython.AnalysisOut.Nastran_ModalFrequencyResponse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Nastran_ModalComplexEigenvalue": {
    "prefix": "Nastran_ModalComplexEigenvalue",
    "text": "**OutPython.AnalysisOut.Nastran_ModalComplexEigenvalue**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSolverTransientHeatTransfer": {
    "prefix": "TSSolverTransientHeatTransfer",
    "text": "**OutPython.AnalysisOut.TSSolverTransientHeatTransfer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSS_LinearStatic": {
    "prefix": "TSSS_LinearStatic",
    "text": "**OutPython.AnalysisOut.TSSS_LinearStatic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSS_NonlinearStatic": {
    "prefix": "TSSS_NonlinearStatic",
    "text": "**OutPython.AnalysisOut.TSSS_NonlinearStatic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSS_NormalModes": {
    "prefix": "TSSS_NormalModes",
    "text": "**OutPython.AnalysisOut.TSSS_NormalModes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSS_LinearBuckling": {
    "prefix": "TSSS_LinearBuckling",
    "text": "**OutPython.AnalysisOut.TSSS_LinearBuckling**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSS_ModalFrequencyResponse": {
    "prefix": "TSSS_ModalFrequencyResponse",
    "text": "**OutPython.AnalysisOut.TSSS_ModalFrequencyResponse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSS_SteadyStateHeatTransfer": {
    "prefix": "TSSS_SteadyStateHeatTransfer",
    "text": "**OutPython.AnalysisOut.TSSS_SteadyStateHeatTransfer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Ansys_LinearStaticStructural": {
    "prefix": "Ansys_LinearStaticStructural",
    "text": "**OutPython.AnalysisOut.Ansys_LinearStaticStructural**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Ansys_NormalModesStructural": {
    "prefix": "Ansys_NormalModesStructural",
    "text": "**OutPython.AnalysisOut.Ansys_NormalModesStructural**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Ansys_HarmonicStructural": {
    "prefix": "Ansys_HarmonicStructural",
    "text": "**OutPython.AnalysisOut.Ansys_HarmonicStructural**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Ansys_SteadyHeatTransfer": {
    "prefix": "Ansys_SteadyHeatTransfer",
    "text": "**OutPython.AnalysisOut.Ansys_SteadyHeatTransfer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Nastran_LinearStatic": {
    "prefix": "Nastran_LinearStatic",
    "text": "**OutPython.AnalysisOut.Nastran_LinearStatic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.Nastran_NormalModes": {
    "prefix": "Nastran_NormalModes",
    "text": "**OutPython.AnalysisOut.Nastran_NormalModes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSolver_ModalFrequencyResponse": {
    "prefix": "TSSolver_ModalFrequencyResponse",
    "text": "**OutPython.AnalysisOut.TSSolver_ModalFrequencyResponse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSolver_SteadyStateHeatTransfer": {
    "prefix": "TSSolver_SteadyStateHeatTransfer",
    "text": "**OutPython.AnalysisOut.TSSolver_SteadyStateHeatTransfer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.ADVC_Structure": {
    "prefix": "ADVC_Structure",
    "text": "**OutPython.AnalysisOut.ADVC_Structure**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.ADVC_HeatTransfer": {
    "prefix": "ADVC_HeatTransfer",
    "text": "**OutPython.AnalysisOut.ADVC_HeatTransfer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcTHProcess": {
    "prefix": "AdvcTHProcess",
    "text": "**OutPython.AnalysisOut.AdvcTHProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcFatigueProcess": {
    "prefix": "AdvcFatigueProcess",
    "text": "**OutPython.AnalysisOut.AdvcFatigueProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcRandomProcess": {
    "prefix": "AdvcRandomProcess",
    "text": "**OutPython.AnalysisOut.AdvcRandomProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AbaqusStaticStep": {
    "prefix": "AbaqusStaticStep",
    "text": "**OutPython.AnalysisOut.AbaqusStaticStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.AdvcRDNLKProcess": {
    "prefix": "AdvcRDNLKProcess",
    "text": "**OutPython.AnalysisOut.AdvcRDNLKProcess**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.TSSS_ElectromagneticFrequencyResponse": {
    "prefix": "TSSS_ElectromagneticFrequencyResponse",
    "text": "**OutPython.AnalysisOut.TSSS_ElectromagneticFrequencyResponse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AnalysisOut.ExportAbaqusInpForSony": {
    "prefix": "ExportAbaqusInpForSony",
    "text": "**OutPython.AnalysisOut.ExportAbaqusInpForSony**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.AssembleBoolean2": {
    "prefix": "AssembleBoolean2",
    "text": "**OutPython.AssembleOut.AssembleBoolean2**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.ASMAssembleFace": {
    "prefix": "ASMAssembleFace",
    "text": "**OutPython.AssembleOut.ASMAssembleFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.AssembleFullLayer": {
    "prefix": "AssembleFullLayer",
    "text": "**OutPython.AssembleOut.AssembleFullLayer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.CylinderLayer": {
    "prefix": "CylinderLayer",
    "text": "**OutPython.AssembleOut.CylinderLayer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.ASMSeparateAll2": {
    "prefix": "ASMSeparateAll2",
    "text": "**OutPython.AssembleOut.ASMSeparateAll2**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.Assemble_Faces": {
    "prefix": "Assemble_Faces",
    "text": "**OutPython.AssembleOut.Assemble_Faces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.AssembleGeneralLayer": {
    "prefix": "AssembleGeneralLayer",
    "text": "**OutPython.AssembleOut.AssembleGeneralLayer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.AddRib": {
    "prefix": "AddRib",
    "text": "**OutPython.AssembleOut.AddRib**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.Assemble_Faces_MatingStep": {
    "prefix": "Assemble_Faces_MatingStep",
    "text": "**OutPython.AssembleOut.Assemble_Faces_MatingStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.AssembleAddBoss": {
    "prefix": "AssembleAddBoss",
    "text": "**OutPython.AssembleOut.AssembleAddBoss**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.ASMSeparateShellCr": {
    "prefix": "ASMSeparateShellCr",
    "text": "**OutPython.AssembleOut.ASMSeparateShellCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.ASMSeparateSolidCr": {
    "prefix": "ASMSeparateSolidCr",
    "text": "**OutPython.AssembleOut.ASMSeparateSolidCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.BooleanEx": {
    "prefix": "BooleanEx",
    "text": "**OutPython.AssembleOut.BooleanEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.AssembleFaceEx": {
    "prefix": "AssembleFaceEx",
    "text": "**OutPython.AssembleOut.AssembleFaceEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.AssembleFaceMatingStep": {
    "prefix": "AssembleFaceMatingStep",
    "text": "**OutPython.AssembleOut.AssembleFaceMatingStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.AddRibPart": {
    "prefix": "AddRibPart",
    "text": "**OutPython.AssembleOut.AddRibPart**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.SharedFaces": {
    "prefix": "SharedFaces",
    "text": "**OutPython.AssembleOut.SharedFaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssembleOut.ConvertToSharedFaces": {
    "prefix": "ConvertToSharedFaces",
    "text": "**OutPython.AssembleOut.ConvertToSharedFaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssemblyOut.RenameParts": {
    "prefix": "RenameParts",
    "text": "**OutPython.AssemblyOut.RenameParts**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssemblyOut.ChangeEntityColor": {
    "prefix": "ChangeEntityColor",
    "text": "**OutPython.AssemblyOut.ChangeEntityColor**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssemblyOut.AddReference": {
    "prefix": "AddReference",
    "text": "**OutPython.AssemblyOut.AddReference**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssemblyOut.Suppress": {
    "prefix": "Suppress",
    "text": "**OutPython.AssemblyOut.Suppress**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssemblyOut.RenameItem": {
    "prefix": "RenameItem",
    "text": "**OutPython.AssemblyOut.RenameItem**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssemblyOut.RestoreBody": {
    "prefix": "RestoreBody",
    "text": "**OutPython.AssemblyOut.RestoreBody**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssemblyOut.AddSubAssembly": {
    "prefix": "AddSubAssembly",
    "text": "**OutPython.AssemblyOut.AddSubAssembly**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssemblyOut.ChangeBodyColor": {
    "prefix": "ChangeBodyColor",
    "text": "**OutPython.AssemblyOut.ChangeBodyColor**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssemblyOut.ChangeFaceMeshLineColor": {
    "prefix": "ChangeFaceMeshLineColor",
    "text": "**OutPython.AssemblyOut.ChangeFaceMeshLineColor**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.AssemblyOut.TransferDocumentData": {
    "prefix": "TransferDocumentData",
    "text": "**OutPython.AssemblyOut.TransferDocumentData**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.Gravity": {
    "prefix": "Gravity",
    "text": "**OutPython.BoundaryConditionsOut.Gravity**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.EnforcedDisplacement": {
    "prefix": "EnforcedDisplacement",
    "text": "**OutPython.BoundaryConditionsOut.EnforcedDisplacement**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.ForceGeneral": {
    "prefix": "ForceGeneral",
    "text": "**OutPython.BoundaryConditionsOut.ForceGeneral**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LbcNolin3Exp": {
    "prefix": "LbcNolin3Exp",
    "text": "**OutPython.BoundaryConditionsOut.LbcNolin3Exp**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.BoundaryTemperature": {
    "prefix": "BoundaryTemperature",
    "text": "**OutPython.BoundaryConditionsOut.BoundaryTemperature**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.TemperatureLoadGeneral": {
    "prefix": "TemperatureLoadGeneral",
    "text": "**OutPython.BoundaryConditionsOut.TemperatureLoadGeneral**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.SubmodelForcedFlux": {
    "prefix": "SubmodelForcedFlux",
    "text": "**OutPython.BoundaryConditionsOut.SubmodelForcedFlux**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.SurfaceLoads": {
    "prefix": "SurfaceLoads",
    "text": "**OutPython.BoundaryConditionsOut.SurfaceLoads**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.TemperatureLoadADVCFile": {
    "prefix": "TemperatureLoadADVCFile",
    "text": "**OutPython.BoundaryConditionsOut.TemperatureLoadADVCFile**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.InitialDynamic": {
    "prefix": "InitialDynamic",
    "text": "**OutPython.BoundaryConditionsOut.InitialDynamic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LbcNolin4Exp": {
    "prefix": "LbcNolin4Exp",
    "text": "**OutPython.BoundaryConditionsOut.LbcNolin4Exp**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LoadCaseOut": {
    "prefix": "LoadCaseOut",
    "text": "**OutPython.BoundaryConditionsOut.LoadCaseOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.EnforcedAcceleration": {
    "prefix": "EnforcedAcceleration",
    "text": "**OutPython.BoundaryConditionsOut.EnforcedAcceleration**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.ForceSine": {
    "prefix": "ForceSine",
    "text": "**OutPython.BoundaryConditionsOut.ForceSine**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.SurfaceFlux": {
    "prefix": "SurfaceFlux",
    "text": "**OutPython.BoundaryConditionsOut.SurfaceFlux**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.TemperatureLoadNastran": {
    "prefix": "TemperatureLoadNastran",
    "text": "**OutPython.BoundaryConditionsOut.TemperatureLoadNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.CentrifugalForceCoordinateSystem": {
    "prefix": "CentrifugalForceCoordinateSystem",
    "text": "**OutPython.BoundaryConditionsOut.CentrifugalForceCoordinateSystem**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.CentrifugalForce2Positions": {
    "prefix": "CentrifugalForce2Positions",
    "text": "**OutPython.BoundaryConditionsOut.CentrifugalForce2Positions**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.Convection": {
    "prefix": "Convection",
    "text": "**OutPython.BoundaryConditionsOut.Convection**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.InitialAngularVelAbaqus": {
    "prefix": "InitialAngularVelAbaqus",
    "text": "**OutPython.BoundaryConditionsOut.InitialAngularVelAbaqus**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.InsideHeatGeneration": {
    "prefix": "InsideHeatGeneration",
    "text": "**OutPython.BoundaryConditionsOut.InsideHeatGeneration**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LbcNolin1Table": {
    "prefix": "LbcNolin1Table",
    "text": "**OutPython.BoundaryConditionsOut.LbcNolin1Table**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.Pressure2Nodes": {
    "prefix": "Pressure2Nodes",
    "text": "**OutPython.BoundaryConditionsOut.Pressure2Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.PressureGeneral": {
    "prefix": "PressureGeneral",
    "text": "**OutPython.BoundaryConditionsOut.PressureGeneral**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.MappingTemperatureLoad": {
    "prefix": "MappingTemperatureLoad",
    "text": "**OutPython.BoundaryConditionsOut.MappingTemperatureLoad**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.CmdLbcCopy": {
    "prefix": "CmdLbcCopy",
    "text": "**OutPython.BoundaryConditionsOut.CmdLbcCopy**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.MappingForcedTemperature": {
    "prefix": "MappingForcedTemperature",
    "text": "**OutPython.BoundaryConditionsOut.MappingForcedTemperature**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.MappingHeatFlux": {
    "prefix": "MappingHeatFlux",
    "text": "**OutPython.BoundaryConditionsOut.MappingHeatFlux**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.PressureQuadratic": {
    "prefix": "PressureQuadratic",
    "text": "**OutPython.BoundaryConditionsOut.PressureQuadratic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.EnforcedVelocity": {
    "prefix": "EnforcedVelocity",
    "text": "**OutPython.BoundaryConditionsOut.EnforcedVelocity**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.ForceNormalDirection": {
    "prefix": "ForceNormalDirection",
    "text": "**OutPython.BoundaryConditionsOut.ForceNormalDirection**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.SubmodelForcedTemp": {
    "prefix": "SubmodelForcedTemp",
    "text": "**OutPython.BoundaryConditionsOut.SubmodelForcedTemp**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LbcContactConvertTo": {
    "prefix": "LbcContactConvertTo",
    "text": "**OutPython.BoundaryConditionsOut.LbcContactConvertTo**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.WholeMappingTemperatureLoad": {
    "prefix": "WholeMappingTemperatureLoad",
    "text": "**OutPython.BoundaryConditionsOut.WholeMappingTemperatureLoad**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.PressureHydrostatic": {
    "prefix": "PressureHydrostatic",
    "text": "**OutPython.BoundaryConditionsOut.PressureHydrostatic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.InitialTemperature": {
    "prefix": "InitialTemperature",
    "text": "**OutPython.BoundaryConditionsOut.InitialTemperature**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.SubmodelForcedDisp": {
    "prefix": "SubmodelForcedDisp",
    "text": "**OutPython.BoundaryConditionsOut.SubmodelForcedDisp**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.ForceQuadratic": {
    "prefix": "ForceQuadratic",
    "text": "**OutPython.BoundaryConditionsOut.ForceQuadratic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.InitialStressGeneral": {
    "prefix": "InitialStressGeneral",
    "text": "**OutPython.BoundaryConditionsOut.InitialStressGeneral**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.PressureSine": {
    "prefix": "PressureSine",
    "text": "**OutPython.BoundaryConditionsOut.PressureSine**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.MappingPressure": {
    "prefix": "MappingPressure",
    "text": "**OutPython.BoundaryConditionsOut.MappingPressure**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.FieldDataOut": {
    "prefix": "FieldDataOut",
    "text": "**OutPython.BoundaryConditionsOut.FieldDataOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.FixedConstraint": {
    "prefix": "FixedConstraint",
    "text": "**OutPython.BoundaryConditionsOut.FixedConstraint**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.ForceVector": {
    "prefix": "ForceVector",
    "text": "**OutPython.BoundaryConditionsOut.ForceVector**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.DofSet": {
    "prefix": "DofSet",
    "text": "**OutPython.BoundaryConditionsOut.DofSet**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.PropertiesCopyTranslate": {
    "prefix": "PropertiesCopyTranslate",
    "text": "**OutPython.BoundaryConditionsOut.PropertiesCopyTranslate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.PropertiesCopyRotate": {
    "prefix": "PropertiesCopyRotate",
    "text": "**OutPython.BoundaryConditionsOut.PropertiesCopyRotate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.PropertiesCopyMirror": {
    "prefix": "PropertiesCopyMirror",
    "text": "**OutPython.BoundaryConditionsOut.PropertiesCopyMirror**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.ConnectionCopyTranslate": {
    "prefix": "ConnectionCopyTranslate",
    "text": "**OutPython.BoundaryConditionsOut.ConnectionCopyTranslate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.ConnectionCopyRotate": {
    "prefix": "ConnectionCopyRotate",
    "text": "**OutPython.BoundaryConditionsOut.ConnectionCopyRotate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.ConnectionCopyMirror": {
    "prefix": "ConnectionCopyMirror",
    "text": "**OutPython.BoundaryConditionsOut.ConnectionCopyMirror**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.GroupCopyTranslate": {
    "prefix": "GroupCopyTranslate",
    "text": "**OutPython.BoundaryConditionsOut.GroupCopyTranslate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.GroupCopyRotate": {
    "prefix": "GroupCopyRotate",
    "text": "**OutPython.BoundaryConditionsOut.GroupCopyRotate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.GroupCopyMirror": {
    "prefix": "GroupCopyMirror",
    "text": "**OutPython.BoundaryConditionsOut.GroupCopyMirror**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LBCCopyTranslate": {
    "prefix": "LBCCopyTranslate",
    "text": "**OutPython.BoundaryConditionsOut.LBCCopyTranslate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LBCCopyRotate": {
    "prefix": "LBCCopyRotate",
    "text": "**OutPython.BoundaryConditionsOut.LBCCopyRotate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LBCCopyMirror": {
    "prefix": "LBCCopyMirror",
    "text": "**OutPython.BoundaryConditionsOut.LBCCopyMirror**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.MappingConvection": {
    "prefix": "MappingConvection",
    "text": "**OutPython.BoundaryConditionsOut.MappingConvection**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.ConcentrateFlux": {
    "prefix": "ConcentrateFlux",
    "text": "**OutPython.BoundaryConditionsOut.ConcentrateFlux**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.WholeMappingInitTemperature": {
    "prefix": "WholeMappingInitTemperature",
    "text": "**OutPython.BoundaryConditionsOut.WholeMappingInitTemperature**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.FieldDataEx": {
    "prefix": "FieldDataEx",
    "text": "**OutPython.BoundaryConditionsOut.FieldDataEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LbcAccelerationLoadACCEL": {
    "prefix": "LbcAccelerationLoadACCEL",
    "text": "**OutPython.BoundaryConditionsOut.LbcAccelerationLoadACCEL**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LbcAccelerationLoadACCEL1": {
    "prefix": "LbcAccelerationLoadACCEL1",
    "text": "**OutPython.BoundaryConditionsOut.LbcAccelerationLoadACCEL1**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.VirtualFluidMass": {
    "prefix": "VirtualFluidMass",
    "text": "**OutPython.BoundaryConditionsOut.VirtualFluidMass**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LbcThermalAttributes": {
    "prefix": "LbcThermalAttributes",
    "text": "**OutPython.BoundaryConditionsOut.LbcThermalAttributes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.FieldDataLsDyna": {
    "prefix": "FieldDataLsDyna",
    "text": "**OutPython.BoundaryConditionsOut.FieldDataLsDyna**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LbcCoil": {
    "prefix": "LbcCoil",
    "text": "**OutPython.BoundaryConditionsOut.LbcCoil**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.BoundaryConditionsOut.LbcExternalCurrentDensity": {
    "prefix": "LbcExternalCurrentDensity",
    "text": "**OutPython.BoundaryConditionsOut.LbcExternalCurrentDensity**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.C01_CarACToolsOut.MMC_CONNECTION_CLEARANCE_ELEMENT": {
    "prefix": "MMC_CONNECTION_CLEARANCE_ELEMENT",
    "text": "**OutPython.C01_CarACToolsOut.MMC_CONNECTION_CLEARANCE_ELEMENT**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.C01_CarACToolsOut.MMC_EDIT_CLEARANCE_ELEMENT": {
    "prefix": "MMC_EDIT_CLEARANCE_ELEMENT",
    "text": "**OutPython.C01_CarACToolsOut.MMC_EDIT_CLEARANCE_ELEMENT**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.C01_CarACToolsOut.MMCMeshedFace": {
    "prefix": "MMCMeshedFace",
    "text": "**OutPython.C01_CarACToolsOut.MMCMeshedFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.C01_CarACToolsOut.RepairFindHoleEx": {
    "prefix": "RepairFindHoleEx",
    "text": "**OutPython.C01_CarACToolsOut.RepairFindHoleEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CabinACToolsOut.RepairCloseHoleEx": {
    "prefix": "RepairCloseHoleEx",
    "text": "**OutPython.CabinACToolsOut.RepairCloseHoleEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CabinACToolsOut.RepairFindHoleEx": {
    "prefix": "RepairFindHoleEx",
    "text": "**OutPython.CabinACToolsOut.RepairFindHoleEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.SurfaceDistanceDistanceCalculate": {
    "prefix": "SurfaceDistanceDistanceCalculate",
    "text": "**OutPython.CalculationOut.SurfaceDistanceDistanceCalculate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostRotateMapping": {
    "prefix": "PostRotateMapping",
    "text": "**OutPython.CalculationOut.PostRotateMapping**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostRotateMappingExportUnv": {
    "prefix": "PostRotateMappingExportUnv",
    "text": "**OutPython.CalculationOut.PostRotateMappingExportUnv**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_GURURI_ANALYSIS_SWEEP": {
    "prefix": "DYNAMIC_GURURI_ANALYSIS_SWEEP",
    "text": "**OutPython.CalculationOut.DYNAMIC_GURURI_ANALYSIS_SWEEP**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_GURURI_ANALYSIS_RESPONSE": {
    "prefix": "DYNAMIC_GURURI_ANALYSIS_RESPONSE",
    "text": "**OutPython.CalculationOut.DYNAMIC_GURURI_ANALYSIS_RESPONSE**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_LOAD": {
    "prefix": "DYNAMIC_FREQ_ANALYSIS_LOAD",
    "text": "**OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_LOAD**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_LOADCASE": {
    "prefix": "DYNAMIC_FREQ_ANALYSIS_LOADCASE",
    "text": "**OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_LOADCASE**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostFFTConditionOut": {
    "prefix": "PostFFTConditionOut",
    "text": "**OutPython.CalculationOut.PostFFTConditionOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdFFTXYPlot": {
    "prefix": "CmdFFTXYPlot",
    "text": "**OutPython.CalculationOut.CmdFFTXYPlot**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdFFTCirclePlot": {
    "prefix": "CmdFFTCirclePlot",
    "text": "**OutPython.CalculationOut.CmdFFTCirclePlot**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdFFTSectionGraph": {
    "prefix": "CmdFFTSectionGraph",
    "text": "**OutPython.CalculationOut.CmdFFTSectionGraph**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdFFTCircleGraph": {
    "prefix": "CmdFFTCircleGraph",
    "text": "**OutPython.CalculationOut.CmdFFTCircleGraph**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.AcousticTLCondition": {
    "prefix": "AcousticTLCondition",
    "text": "**OutPython.CalculationOut.AcousticTLCondition**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.AcousticTLPCHResult": {
    "prefix": "AcousticTLPCHResult",
    "text": "**OutPython.CalculationOut.AcousticTLPCHResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostAcousticPanelContributionCreateGraph": {
    "prefix": "PostAcousticPanelContributionCreateGraph",
    "text": "**OutPython.CalculationOut.PostAcousticPanelContributionCreateGraph**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostToolAcousticPanelContribution": {
    "prefix": "PostToolAcousticPanelContribution",
    "text": "**OutPython.CalculationOut.PostToolAcousticPanelContribution**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostImportActranPlt": {
    "prefix": "PostImportActranPlt",
    "text": "**OutPython.CalculationOut.PostImportActranPlt**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.AcousticIntensity": {
    "prefix": "AcousticIntensity",
    "text": "**OutPython.CalculationOut.AcousticIntensity**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.ACCombinedAnimation": {
    "prefix": "ACCombinedAnimation",
    "text": "**OutPython.CalculationOut.ACCombinedAnimation**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostCreateUserResult": {
    "prefix": "PostCreateUserResult",
    "text": "**OutPython.CalculationOut.PostCreateUserResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdSaveOpenTsdv": {
    "prefix": "CmdSaveOpenTsdv",
    "text": "**OutPython.CalculationOut.CmdSaveOpenTsdv**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_TRANS_ANALYSIS_LOAD": {
    "prefix": "DYNAMIC_TRANS_ANALYSIS_LOAD",
    "text": "**OutPython.CalculationOut.DYNAMIC_TRANS_ANALYSIS_LOAD**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_TRANS_ANALYSIS_LOADCASE": {
    "prefix": "DYNAMIC_TRANS_ANALYSIS_LOADCASE",
    "text": "**OutPython.CalculationOut.DYNAMIC_TRANS_ANALYSIS_LOADCASE**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_TRANS_ANALYSIS_RESPONSE": {
    "prefix": "DYNAMIC_TRANS_ANALYSIS_RESPONSE",
    "text": "**OutPython.CalculationOut.DYNAMIC_TRANS_ANALYSIS_RESPONSE**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_TRANS_ANALYSIS_RESPONSE_NewResult": {
    "prefix": "DYNAMIC_TRANS_ANALYSIS_RESPONSE_NewResult",
    "text": "**OutPython.CalculationOut.DYNAMIC_TRANS_ANALYSIS_RESPONSE_NewResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostToolsSubcaseSafetyFactor": {
    "prefix": "PostToolsSubcaseSafetyFactor",
    "text": "**OutPython.CalculationOut.PostToolsSubcaseSafetyFactor**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostToolsSubcasePeakHoldEx": {
    "prefix": "PostToolsSubcasePeakHoldEx",
    "text": "**OutPython.CalculationOut.PostToolsSubcasePeakHoldEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostToolsSubcaseRelativeOffset": {
    "prefix": "PostToolsSubcaseRelativeOffset",
    "text": "**OutPython.CalculationOut.PostToolsSubcaseRelativeOffset**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdAddStrainGaugeAxisAngle": {
    "prefix": "CmdAddStrainGaugeAxisAngle",
    "text": "**OutPython.CalculationOut.CmdAddStrainGaugeAxisAngle**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdAddStrainGaugeDirCos": {
    "prefix": "CmdAddStrainGaugeDirCos",
    "text": "**OutPython.CalculationOut.CmdAddStrainGaugeDirCos**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdAddStrainGaugeExistingResult": {
    "prefix": "CmdAddStrainGaugeExistingResult",
    "text": "**OutPython.CalculationOut.CmdAddStrainGaugeExistingResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdAddStrainGaugeMaxPrincipal": {
    "prefix": "CmdAddStrainGaugeMaxPrincipal",
    "text": "**OutPython.CalculationOut.CmdAddStrainGaugeMaxPrincipal**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdAddStrainGaugeMinPrincipal": {
    "prefix": "CmdAddStrainGaugeMinPrincipal",
    "text": "**OutPython.CalculationOut.CmdAddStrainGaugeMinPrincipal**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdAddStrainGaugeTangentProject": {
    "prefix": "CmdAddStrainGaugeTangentProject",
    "text": "**OutPython.CalculationOut.CmdAddStrainGaugeTangentProject**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdAddStrainGauge2Nodes": {
    "prefix": "CmdAddStrainGauge2Nodes",
    "text": "**OutPython.CalculationOut.CmdAddStrainGauge2Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdAddStrainGaugeNodePoint": {
    "prefix": "CmdAddStrainGaugeNodePoint",
    "text": "**OutPython.CalculationOut.CmdAddStrainGaugeNodePoint**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_RESPONSE": {
    "prefix": "DYNAMIC_FREQ_ANALYSIS_RESPONSE",
    "text": "**OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_RESPONSE**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_RESPONSE_NewResult": {
    "prefix": "DYNAMIC_FREQ_ANALYSIS_RESPONSE_NewResult",
    "text": "**OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_RESPONSE_NewResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_LOAD_SOLVER": {
    "prefix": "DYNAMIC_FREQ_ANALYSIS_LOAD_SOLVER",
    "text": "**OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_LOAD_SOLVER**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_RESPONSE_SOLVER": {
    "prefix": "DYNAMIC_FREQ_ANALYSIS_RESPONSE_SOLVER",
    "text": "**OutPython.CalculationOut.DYNAMIC_FREQ_ANALYSIS_RESPONSE_SOLVER**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostToolsSubcaseFatigueEx": {
    "prefix": "PostToolsSubcaseFatigueEx",
    "text": "**OutPython.CalculationOut.PostToolsSubcaseFatigueEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.DYNAMIC_TRANS_ANALYSIS_LOAD_SOLVER": {
    "prefix": "DYNAMIC_TRANS_ANALYSIS_LOAD_SOLVER",
    "text": "**OutPython.CalculationOut.DYNAMIC_TRANS_ANALYSIS_LOAD_SOLVER**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.TotalMPC": {
    "prefix": "TotalMPC",
    "text": "**OutPython.CalculationOut.TotalMPC**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CalculateMPCAtTime": {
    "prefix": "CalculateMPCAtTime",
    "text": "**OutPython.CalculationOut.CalculateMPCAtTime**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CalculateMPCAtFrequency": {
    "prefix": "CalculateMPCAtFrequency",
    "text": "**OutPython.CalculationOut.CalculateMPCAtFrequency**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.SaveMPCResultToCSV": {
    "prefix": "SaveMPCResultToCSV",
    "text": "**OutPython.CalculationOut.SaveMPCResultToCSV**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.CmdPostPeakSearch": {
    "prefix": "CmdPostPeakSearch",
    "text": "**OutPython.CalculationOut.CmdPostPeakSearch**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.CalculationOut.PostFFTConditionCopy": {
    "prefix": "PostFFTConditionCopy",
    "text": "**OutPython.CalculationOut.PostFFTConditionCopy**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ChartOut.PostCreateGraph": {
    "prefix": "PostCreateGraph",
    "text": "**OutPython.ChartOut.PostCreateGraph**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Rbe2": {
    "prefix": "Rbe2",
    "text": "**OutPython.ConnectionsOut.Rbe2**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_C_Face": {
    "prefix": "Lbc_Bolt_Modeling_Type_C_Face",
    "text": "**OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_C_Face**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.CreateGeneralContact": {
    "prefix": "CreateGeneralContact",
    "text": "**OutPython.ConnectionsOut.CreateGeneralContact**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Damper": {
    "prefix": "Damper",
    "text": "**OutPython.ConnectionsOut.Damper**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ConnectionNewMass": {
    "prefix": "ConnectionNewMass",
    "text": "**OutPython.ConnectionsOut.ConnectionNewMass**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.CheckPattern": {
    "prefix": "CheckPattern",
    "text": "**OutPython.ConnectionsOut.CheckPattern**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ConnectionBarBeam": {
    "prefix": "ConnectionBarBeam",
    "text": "**OutPython.ConnectionsOut.ConnectionBarBeam**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Pretension": {
    "prefix": "Pretension",
    "text": "**OutPython.ConnectionsOut.Pretension**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.PretensionAbaqus": {
    "prefix": "PretensionAbaqus",
    "text": "**OutPython.ConnectionsOut.PretensionAbaqus**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.PretensionSunShine": {
    "prefix": "PretensionSunShine",
    "text": "**OutPython.ConnectionsOut.PretensionSunShine**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_C_Edge": {
    "prefix": "Lbc_Bolt_Modeling_Type_C_Edge",
    "text": "**OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_C_Edge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_B_Face": {
    "prefix": "Lbc_Bolt_Modeling_Type_B_Face",
    "text": "**OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_B_Face**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactClearance": {
    "prefix": "ContactClearance",
    "text": "**OutPython.ConnectionsOut.ContactClearance**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_A_Face": {
    "prefix": "Lbc_Bolt_Modeling_Type_A_Face",
    "text": "**OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_A_Face**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_B_Edge": {
    "prefix": "Lbc_Bolt_Modeling_Type_B_Edge",
    "text": "**OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_B_Edge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ConnectGapOut": {
    "prefix": "ConnectGapOut",
    "text": "**OutPython.ConnectionsOut.ConnectGapOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Property1DPlotOut": {
    "prefix": "Property1DPlotOut",
    "text": "**OutPython.ConnectionsOut.Property1DPlotOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactADVCOut": {
    "prefix": "ContactADVCOut",
    "text": "**OutPython.ConnectionsOut.ContactADVCOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactTSSolver": {
    "prefix": "ContactTSSolver",
    "text": "**OutPython.ConnectionsOut.ContactTSSolver**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBar": {
    "prefix": "RBar",
    "text": "**OutPython.ConnectionsOut.RBar**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactMSCNastranOut": {
    "prefix": "ContactMSCNastranOut",
    "text": "**OutPython.ConnectionsOut.ContactMSCNastranOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.FindContact": {
    "prefix": "FindContact",
    "text": "**OutPython.ConnectionsOut.FindContact**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Bush": {
    "prefix": "Bush",
    "text": "**OutPython.ConnectionsOut.Bush**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcPretensionAdvc": {
    "prefix": "LbcPretensionAdvc",
    "text": "**OutPython.ConnectionsOut.LbcPretensionAdvc**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcPreTensionMSCNastran": {
    "prefix": "LbcPreTensionMSCNastran",
    "text": "**OutPython.ConnectionsOut.LbcPreTensionMSCNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactAnsysOut": {
    "prefix": "ContactAnsysOut",
    "text": "**OutPython.ConnectionsOut.ContactAnsysOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.CreateConnConm": {
    "prefix": "CreateConnConm",
    "text": "**OutPython.ConnectionsOut.CreateConnConm**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_D": {
    "prefix": "Lbc_Bolt_Modeling_Type_D",
    "text": "**OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_D**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Rbe3": {
    "prefix": "Rbe3",
    "text": "**OutPython.ConnectionsOut.Rbe3**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactAbaqus_ManualGroup": {
    "prefix": "ContactAbaqus_ManualGroup",
    "text": "**OutPython.ConnectionsOut.ContactAbaqus_ManualGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactAbaqus_ManualFace": {
    "prefix": "ContactAbaqus_ManualFace",
    "text": "**OutPython.ConnectionsOut.ContactAbaqus_ManualFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactAbaqus_GroupByMatrix": {
    "prefix": "ContactAbaqus_GroupByMatrix",
    "text": "**OutPython.ConnectionsOut.ContactAbaqus_GroupByMatrix**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactAbaqus_ShareFace": {
    "prefix": "ContactAbaqus_ShareFace",
    "text": "**OutPython.ConnectionsOut.ContactAbaqus_ShareFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LBCRigdWall": {
    "prefix": "LBCRigdWall",
    "text": "**OutPython.ConnectionsOut.LBCRigdWall**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactNXNastranOut": {
    "prefix": "ContactNXNastranOut",
    "text": "**OutPython.ConnectionsOut.ContactNXNastranOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.SpringOneToOneUniformDOFs": {
    "prefix": "SpringOneToOneUniformDOFs",
    "text": "**OutPython.ConnectionsOut.SpringOneToOneUniformDOFs**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.SpringOneToOneDOFs": {
    "prefix": "SpringOneToOneDOFs",
    "text": "**OutPython.ConnectionsOut.SpringOneToOneDOFs**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.SpringNodesUniformDOFs": {
    "prefix": "SpringNodesUniformDOFs",
    "text": "**OutPython.ConnectionsOut.SpringNodesUniformDOFs**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.SpringNodesDOFs": {
    "prefix": "SpringNodesDOFs",
    "text": "**OutPython.ConnectionsOut.SpringNodesDOFs**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.SpringGrounded": {
    "prefix": "SpringGrounded",
    "text": "**OutPython.ConnectionsOut.SpringGrounded**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ConnBush_OnetoOne": {
    "prefix": "ConnBush_OnetoOne",
    "text": "**OutPython.ConnectionsOut.ConnBush_OnetoOne**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ConnBush_2Nodes": {
    "prefix": "ConnBush_2Nodes",
    "text": "**OutPython.ConnectionsOut.ConnBush_2Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ConnBush_AnyEntity": {
    "prefix": "ConnBush_AnyEntity",
    "text": "**OutPython.ConnectionsOut.ConnBush_AnyEntity**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ConnectGap_2Nodes": {
    "prefix": "ConnectGap_2Nodes",
    "text": "**OutPython.ConnectionsOut.ConnectGap_2Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ConnectGap_2Edges": {
    "prefix": "ConnectGap_2Edges",
    "text": "**OutPython.ConnectionsOut.ConnectGap_2Edges**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ConnectGap_2Faces": {
    "prefix": "ConnectGap_2Faces",
    "text": "**OutPython.ConnectionsOut.ConnectGap_2Faces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Connector": {
    "prefix": "Connector",
    "text": "**OutPython.ConnectionsOut.Connector**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Mpc": {
    "prefix": "Mpc",
    "text": "**OutPython.ConnectionsOut.Mpc**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.MpcEquation2Faces": {
    "prefix": "MpcEquation2Faces",
    "text": "**OutPython.ConnectionsOut.MpcEquation2Faces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.MpcGeneralNodeToFaces": {
    "prefix": "MpcGeneralNodeToFaces",
    "text": "**OutPython.ConnectionsOut.MpcGeneralNodeToFaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.MpcGeneralNodeToEdges": {
    "prefix": "MpcGeneralNodeToEdges",
    "text": "**OutPython.ConnectionsOut.MpcGeneralNodeToEdges**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.MpcGeneral2Nodes": {
    "prefix": "MpcGeneral2Nodes",
    "text": "**OutPython.ConnectionsOut.MpcGeneral2Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.MpcGeneralTwoEdges": {
    "prefix": "MpcGeneralTwoEdges",
    "text": "**OutPython.ConnectionsOut.MpcGeneralTwoEdges**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.MpcGeneralTwoFaces": {
    "prefix": "MpcGeneralTwoFaces",
    "text": "**OutPython.ConnectionsOut.MpcGeneralTwoFaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.MpcGeneralNodeToAny": {
    "prefix": "MpcGeneralNodeToAny",
    "text": "**OutPython.ConnectionsOut.MpcGeneralNodeToAny**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.MpcEquationMultipleNodes": {
    "prefix": "MpcEquationMultipleNodes",
    "text": "**OutPython.ConnectionsOut.MpcEquationMultipleNodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactManualFaceNXNastran": {
    "prefix": "LbcContactManualFaceNXNastran",
    "text": "**OutPython.ConnectionsOut.LbcContactManualFaceNXNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactShareFaceNxNastran": {
    "prefix": "LbcContactShareFaceNxNastran",
    "text": "**OutPython.ConnectionsOut.LbcContactShareFaceNxNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactTableNXNastran": {
    "prefix": "LbcContactTableNXNastran",
    "text": "**OutPython.ConnectionsOut.LbcContactTableNXNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactByGroupMatrixMSCNastran": {
    "prefix": "LbcContactByGroupMatrixMSCNastran",
    "text": "**OutPython.ConnectionsOut.LbcContactByGroupMatrixMSCNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactManualFaceMSCNastran": {
    "prefix": "LbcContactManualFaceMSCNastran",
    "text": "**OutPython.ConnectionsOut.LbcContactManualFaceMSCNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactTableMSCNastran": {
    "prefix": "LbcContactTableMSCNastran",
    "text": "**OutPython.ConnectionsOut.LbcContactTableMSCNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactManualGroupNXNastran": {
    "prefix": "LbcContactManualGroupNXNastran",
    "text": "**OutPython.ConnectionsOut.LbcContactManualGroupNXNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactContactGroupByMatrixNXNastran": {
    "prefix": "LbcContactContactGroupByMatrixNXNastran",
    "text": "**OutPython.ConnectionsOut.LbcContactContactGroupByMatrixNXNastran**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactManualFaceADVC": {
    "prefix": "ContactManualFaceADVC",
    "text": "**OutPython.ConnectionsOut.ContactManualFaceADVC**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactManualFaceTSSS": {
    "prefix": "ContactManualFaceTSSS",
    "text": "**OutPython.ConnectionsOut.ContactManualFaceTSSS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactTableAdvc": {
    "prefix": "LbcContactTableAdvc",
    "text": "**OutPython.ConnectionsOut.LbcContactTableAdvc**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactManualFaceAnsys": {
    "prefix": "LbcContactManualFaceAnsys",
    "text": "**OutPython.ConnectionsOut.LbcContactManualFaceAnsys**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactByGroupMatrixANSYS": {
    "prefix": "LbcContactByGroupMatrixANSYS",
    "text": "**OutPython.ConnectionsOut.LbcContactByGroupMatrixANSYS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactTableANSYS": {
    "prefix": "LbcContactTableANSYS",
    "text": "**OutPython.ConnectionsOut.LbcContactTableANSYS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactTSSolver_ManualGroup": {
    "prefix": "LbcContactTSSolver_ManualGroup",
    "text": "**OutPython.ConnectionsOut.LbcContactTSSolver_ManualGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactTSSSOut": {
    "prefix": "ContactTSSSOut",
    "text": "**OutPython.ConnectionsOut.ContactTSSSOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactTSSS_ContactTable": {
    "prefix": "ContactTSSS_ContactTable",
    "text": "**OutPython.ConnectionsOut.ContactTSSS_ContactTable**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactAdvc_ContactGroupByMatrix": {
    "prefix": "LbcContactAdvc_ContactGroupByMatrix",
    "text": "**OutPython.ConnectionsOut.LbcContactAdvc_ContactGroupByMatrix**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.CreateContactReport": {
    "prefix": "CreateContactReport",
    "text": "**OutPython.ConnectionsOut.CreateContactReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.BoltMeshing2_SplitOnly": {
    "prefix": "BoltMeshing2_SplitOnly",
    "text": "**OutPython.ConnectionsOut.BoltMeshing2_SplitOnly**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.BoltMeshing2_NotSplitOnly": {
    "prefix": "BoltMeshing2_NotSplitOnly",
    "text": "**OutPython.ConnectionsOut.BoltMeshing2_NotSplitOnly**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_A_Edge": {
    "prefix": "Lbc_Bolt_Modeling_Type_A_Edge",
    "text": "**OutPython.ConnectionsOut.Lbc_Bolt_Modeling_Type_A_Edge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactTableAbaqus": {
    "prefix": "ContactTableAbaqus",
    "text": "**OutPython.ConnectionsOut.ContactTableAbaqus**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactTable_Abaqus": {
    "prefix": "ContactTable_Abaqus",
    "text": "**OutPython.ConnectionsOut.ContactTable_Abaqus**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBE2OneToMany": {
    "prefix": "RBE2OneToMany",
    "text": "**OutPython.ConnectionsOut.RBE2OneToMany**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBE2OneToOne": {
    "prefix": "RBE2OneToOne",
    "text": "**OutPython.ConnectionsOut.RBE2OneToOne**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBE2OneToOneNodesWithTolerance": {
    "prefix": "RBE2OneToOneNodesWithTolerance",
    "text": "**OutPython.ConnectionsOut.RBE2OneToOneNodesWithTolerance**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBE2ToCenter": {
    "prefix": "RBE2ToCenter",
    "text": "**OutPython.ConnectionsOut.RBE2ToCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBE2ToCircleCenter": {
    "prefix": "RBE2ToCircleCenter",
    "text": "**OutPython.ConnectionsOut.RBE2ToCircleCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBE3OneToMany": {
    "prefix": "RBE3OneToMany",
    "text": "**OutPython.ConnectionsOut.RBE3OneToMany**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBE3OneToOne": {
    "prefix": "RBE3OneToOne",
    "text": "**OutPython.ConnectionsOut.RBE3OneToOne**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBE3ToCenter": {
    "prefix": "RBE3ToCenter",
    "text": "**OutPython.ConnectionsOut.RBE3ToCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBE3ToCircleCenter": {
    "prefix": "RBE3ToCircleCenter",
    "text": "**OutPython.ConnectionsOut.RBE3ToCircleCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBarOneToOne": {
    "prefix": "RBarOneToOne",
    "text": "**OutPython.ConnectionsOut.RBarOneToOne**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBarOneToMany": {
    "prefix": "RBarOneToMany",
    "text": "**OutPython.ConnectionsOut.RBarOneToMany**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.RBarOneToOneNodesWithTolerance": {
    "prefix": "RBarOneToOneNodesWithTolerance",
    "text": "**OutPython.ConnectionsOut.RBarOneToOneNodesWithTolerance**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactShareFaceMSCNastranCr": {
    "prefix": "LbcContactShareFaceMSCNastranCr",
    "text": "**OutPython.ConnectionsOut.LbcContactShareFaceMSCNastranCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactShareFaceAdvcCr": {
    "prefix": "LbcContactShareFaceAdvcCr",
    "text": "**OutPython.ConnectionsOut.LbcContactShareFaceAdvcCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.LbcContactShareFaceANSYSCr": {
    "prefix": "LbcContactShareFaceANSYSCr",
    "text": "**OutPython.ConnectionsOut.LbcContactShareFaceANSYSCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.AutoConvertContact": {
    "prefix": "AutoConvertContact",
    "text": "**OutPython.ConnectionsOut.AutoConvertContact**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.FindContactPairs": {
    "prefix": "FindContactPairs",
    "text": "**OutPython.ConnectionsOut.FindContactPairs**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.FindContactPairs_TSSS": {
    "prefix": "FindContactPairs_TSSS",
    "text": "**OutPython.ConnectionsOut.FindContactPairs_TSSS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactTable_TSSS": {
    "prefix": "ContactTable_TSSS",
    "text": "**OutPython.ConnectionsOut.ContactTable_TSSS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactTable_Advc": {
    "prefix": "ContactTable_Advc",
    "text": "**OutPython.ConnectionsOut.ContactTable_Advc**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ConnectionsOut.ContactManualGroupForLsDyna": {
    "prefix": "ContactManualGroupForLsDyna",
    "text": "**OutPython.ConnectionsOut.ContactManualGroupForLsDyna**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.DesignerOut.MergeContact": {
    "prefix": "MergeContact",
    "text": "**OutPython.DesignerOut.MergeContact**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.DesignerOut.Moment": {
    "prefix": "Moment",
    "text": "**OutPython.DesignerOut.Moment**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.DesignerOut.DoBoxMesh": {
    "prefix": "DoBoxMesh",
    "text": "**OutPython.DesignerOut.DoBoxMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.DesignerOut.TemperatureLoad": {
    "prefix": "TemperatureLoad",
    "text": "**OutPython.DesignerOut.TemperatureLoad**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.DesignerOut.Material2DForDesigner": {
    "prefix": "Material2DForDesigner",
    "text": "**OutPython.DesignerOut.Material2DForDesigner**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.EngReliabilityOut.MappingForcedDisplacement": {
    "prefix": "MappingForcedDisplacement",
    "text": "**OutPython.EngReliabilityOut.MappingForcedDisplacement**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ExchangeOut.MeshEditReplaceSolidMesh": {
    "prefix": "MeshEditReplaceSolidMesh",
    "text": "**OutPython.ExchangeOut.MeshEditReplaceSolidMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ExManifoldModelingOut.SZWeldLine2": {
    "prefix": "SZWeldLine2",
    "text": "**OutPython.ExManifoldModelingOut.SZWeldLine2**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FileMenuOut.AddJTDB": {
    "prefix": "AddJTDB",
    "text": "**OutPython.FileMenuOut.AddJTDB**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FileMenuOut.SaveJTDB": {
    "prefix": "SaveJTDB",
    "text": "**OutPython.FileMenuOut.SaveJTDB**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FileMenuOut.LoadJTDB": {
    "prefix": "LoadJTDB",
    "text": "**OutPython.FileMenuOut.LoadJTDB**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FileMenuOut.LoadDB": {
    "prefix": "LoadDB",
    "text": "**OutPython.FileMenuOut.LoadDB**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FileMenuOut.SaveDB": {
    "prefix": "SaveDB",
    "text": "**OutPython.FileMenuOut.SaveDB**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FileMenuOut.SaveJTH5": {
    "prefix": "SaveJTH5",
    "text": "**OutPython.FileMenuOut.SaveJTH5**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FileMenuOut.LoadJTH5": {
    "prefix": "LoadJTH5",
    "text": "**OutPython.FileMenuOut.LoadJTH5**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FileMenuOut.SavePOH5": {
    "prefix": "SavePOH5",
    "text": "**OutPython.FileMenuOut.SavePOH5**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FileMenuOut.LoadPOH5": {
    "prefix": "LoadPOH5",
    "text": "**OutPython.FileMenuOut.LoadPOH5**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FOWTOut.FOWT_MOORING_FORCE": {
    "prefix": "FOWT_MOORING_FORCE",
    "text": "**OutPython.FOWTOut.FOWT_MOORING_FORCE**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FOWTOut.FOWT_MOORING_FORCE_AND_RNA": {
    "prefix": "FOWT_MOORING_FORCE_AND_RNA",
    "text": "**OutPython.FOWTOut.FOWT_MOORING_FORCE_AND_RNA**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FOWTOut.FOWT_EXTERNAL_PRESSURE": {
    "prefix": "FOWT_EXTERNAL_PRESSURE",
    "text": "**OutPython.FOWTOut.FOWT_EXTERNAL_PRESSURE**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FOWTOut.FOWT_INERTIAL_FORCE": {
    "prefix": "FOWT_INERTIAL_FORCE",
    "text": "**OutPython.FOWTOut.FOWT_INERTIAL_FORCE**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FOWTOut.FOWT_ACCELERATION": {
    "prefix": "FOWT_ACCELERATION",
    "text": "**OutPython.FOWTOut.FOWT_ACCELERATION**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FOWTOut.FOWT_MAPPING_ACCELERATION": {
    "prefix": "FOWT_MAPPING_ACCELERATION",
    "text": "**OutPython.FOWTOut.FOWT_MAPPING_ACCELERATION**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FOWTOut.FOWT_LOADS_TRANSMITTED_FROM_RNA": {
    "prefix": "FOWT_LOADS_TRANSMITTED_FROM_RNA",
    "text": "**OutPython.FOWTOut.FOWT_LOADS_TRANSMITTED_FROM_RNA**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FOWTOut.FOWT_WIND_LOAD": {
    "prefix": "FOWT_WIND_LOAD",
    "text": "**OutPython.FOWTOut.FOWT_WIND_LOAD**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FOWTOut.FOWT_ANALYSIS_STATIC": {
    "prefix": "FOWT_ANALYSIS_STATIC",
    "text": "**OutPython.FOWTOut.FOWT_ANALYSIS_STATIC**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.FOWTOut.FOWT_ANALYSIS_DYNAMIC": {
    "prefix": "FOWT_ANALYSIS_DYNAMIC",
    "text": "**OutPython.FOWTOut.FOWT_ANALYSIS_DYNAMIC**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateCube": {
    "prefix": "CreateCube",
    "text": "**OutPython.GeometryOut.CreateCube**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ImprintLineS": {
    "prefix": "ImprintLineS",
    "text": "**OutPython.GeometryOut.ImprintLineS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.RotateBody": {
    "prefix": "RotateBody",
    "text": "**OutPython.GeometryOut.RotateBody**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.GeometryCADTrim": {
    "prefix": "GeometryCADTrim",
    "text": "**OutPython.GeometryOut.GeometryCADTrim**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ScaleBody": {
    "prefix": "ScaleBody",
    "text": "**OutPython.GeometryOut.ScaleBody**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateWedge": {
    "prefix": "CreateWedge",
    "text": "**OutPython.GeometryOut.CreateWedge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateBar": {
    "prefix": "CreateBar",
    "text": "**OutPython.GeometryOut.CreateBar**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.DeletePart": {
    "prefix": "DeletePart",
    "text": "**OutPython.GeometryOut.DeletePart**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.GeoImprintSplineS": {
    "prefix": "GeoImprintSplineS",
    "text": "**OutPython.GeometryOut.GeoImprintSplineS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ImprintPlannarLineS": {
    "prefix": "ImprintPlannarLineS",
    "text": "**OutPython.GeometryOut.ImprintPlannarLineS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CutBodyByPlane": {
    "prefix": "CutBodyByPlane",
    "text": "**OutPython.GeometryOut.CutBodyByPlane**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ImprintCircleS": {
    "prefix": "ImprintCircleS",
    "text": "**OutPython.GeometryOut.ImprintCircleS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateFaceByElem": {
    "prefix": "CreateFaceByElem",
    "text": "**OutPython.GeometryOut.CreateFaceByElem**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ImprintPerpendicularLine": {
    "prefix": "ImprintPerpendicularLine",
    "text": "**OutPython.GeometryOut.ImprintPerpendicularLine**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.BodyCutBySurfaceS": {
    "prefix": "BodyCutBySurfaceS",
    "text": "**OutPython.GeometryOut.BodyCutBySurfaceS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.StitchEdge": {
    "prefix": "StitchEdge",
    "text": "**OutPython.GeometryOut.StitchEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateSphere": {
    "prefix": "CreateSphere",
    "text": "**OutPython.GeometryOut.CreateSphere**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateTorus": {
    "prefix": "CreateTorus",
    "text": "**OutPython.GeometryOut.CreateTorus**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MirrorBody": {
    "prefix": "MirrorBody",
    "text": "**OutPython.GeometryOut.MirrorBody**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.PositionBody": {
    "prefix": "PositionBody",
    "text": "**OutPython.GeometryOut.PositionBody**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MergeFace_MergeEntities": {
    "prefix": "MergeFace_MergeEntities",
    "text": "**OutPython.GeometryOut.MergeFace_MergeEntities**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ImprintExtendLine": {
    "prefix": "ImprintExtendLine",
    "text": "**OutPython.GeometryOut.ImprintExtendLine**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreatePartFromElems": {
    "prefix": "CreatePartFromElems",
    "text": "**OutPython.GeometryOut.CreatePartFromElems**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MeshEditExtractRefSurfaces": {
    "prefix": "MeshEditExtractRefSurfaces",
    "text": "**OutPython.GeometryOut.MeshEditExtractRefSurfaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.LogoRemoval": {
    "prefix": "LogoRemoval",
    "text": "**OutPython.GeometryOut.LogoRemoval**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.GeometryMergeEntitiesTinyFacesMerge": {
    "prefix": "GeometryMergeEntitiesTinyFacesMerge",
    "text": "**OutPython.GeometryOut.GeometryMergeEntitiesTinyFacesMerge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.FindFeatureFillet": {
    "prefix": "FindFeatureFillet",
    "text": "**OutPython.GeometryOut.FindFeatureFillet**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.TranslateBody": {
    "prefix": "TranslateBody",
    "text": "**OutPython.GeometryOut.TranslateBody**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.SeparateSTLPart": {
    "prefix": "SeparateSTLPart",
    "text": "**OutPython.GeometryOut.SeparateSTLPart**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.BreakFace": {
    "prefix": "BreakFace",
    "text": "**OutPython.GeometryOut.BreakFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateEdgeByElemEdge": {
    "prefix": "CreateEdgeByElemEdge",
    "text": "**OutPython.GeometryOut.CreateEdgeByElemEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateEdgeByElemEdgeAngle": {
    "prefix": "CreateEdgeByElemEdgeAngle",
    "text": "**OutPython.GeometryOut.CreateEdgeByElemEdgeAngle**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ShellAsm": {
    "prefix": "ShellAsm",
    "text": "**OutPython.GeometryOut.ShellAsm**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateEdgeBy2NodeShortestPath": {
    "prefix": "CreateEdgeBy2NodeShortestPath",
    "text": "**OutPython.GeometryOut.CreateEdgeBy2NodeShortestPath**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ImprintPerpendicularLine2": {
    "prefix": "ImprintPerpendicularLine2",
    "text": "**OutPython.GeometryOut.ImprintPerpendicularLine2**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.BodyCutBy3PointsS": {
    "prefix": "BodyCutBy3PointsS",
    "text": "**OutPython.GeometryOut.BodyCutBy3PointsS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateFaceFromFourEdges": {
    "prefix": "CreateFaceFromFourEdges",
    "text": "**OutPython.GeometryOut.CreateFaceFromFourEdges**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateTrapezoid": {
    "prefix": "CreateTrapezoid",
    "text": "**OutPython.GeometryOut.CreateTrapezoid**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ImprintCloseLineS": {
    "prefix": "ImprintCloseLineS",
    "text": "**OutPython.GeometryOut.ImprintCloseLineS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.SquareUpFillet": {
    "prefix": "SquareUpFillet",
    "text": "**OutPython.GeometryOut.SquareUpFillet**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateFaceFromMeshFace": {
    "prefix": "CreateFaceFromMeshFace",
    "text": "**OutPython.GeometryOut.CreateFaceFromMeshFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ImprintOffsetLineS": {
    "prefix": "ImprintOffsetLineS",
    "text": "**OutPython.GeometryOut.ImprintOffsetLineS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateFaceFromEdges": {
    "prefix": "CreateFaceFromEdges",
    "text": "**OutPython.GeometryOut.CreateFaceFromEdges**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MakeFillet": {
    "prefix": "MakeFillet",
    "text": "**OutPython.GeometryOut.MakeFillet**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.Create_R_On_Bar": {
    "prefix": "Create_R_On_Bar",
    "text": "**OutPython.GeometryOut.Create_R_On_Bar**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateCone": {
    "prefix": "CreateCone",
    "text": "**OutPython.GeometryOut.CreateCone**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateCylinderFrustum": {
    "prefix": "CreateCylinderFrustum",
    "text": "**OutPython.GeometryOut.CreateCylinderFrustum**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.DelCircChamfer": {
    "prefix": "DelCircChamfer",
    "text": "**OutPython.GeometryOut.DelCircChamfer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MeshEditExtractSurfaces": {
    "prefix": "MeshEditExtractSurfaces",
    "text": "**OutPython.GeometryOut.MeshEditExtractSurfaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ShellAssyGeneral": {
    "prefix": "ShellAssyGeneral",
    "text": "**OutPython.GeometryOut.ShellAssyGeneral**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.Imprint_Intersection_LineS": {
    "prefix": "Imprint_Intersection_LineS",
    "text": "**OutPython.GeometryOut.Imprint_Intersection_LineS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.Imprint_Projection_LineS": {
    "prefix": "Imprint_Projection_LineS",
    "text": "**OutPython.GeometryOut.Imprint_Projection_LineS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MakeFacePlanar": {
    "prefix": "MakeFacePlanar",
    "text": "**OutPython.GeometryOut.MakeFacePlanar**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MergeEdge": {
    "prefix": "MergeEdge",
    "text": "**OutPython.GeometryOut.MergeEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MergePart": {
    "prefix": "MergePart",
    "text": "**OutPython.GeometryOut.MergePart**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateSmoothFace": {
    "prefix": "CreateSmoothFace",
    "text": "**OutPython.GeometryOut.CreateSmoothFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.SeparatePart": {
    "prefix": "SeparatePart",
    "text": "**OutPython.GeometryOut.SeparatePart**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.TransMatingFace": {
    "prefix": "TransMatingFace",
    "text": "**OutPython.GeometryOut.TransMatingFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateEdgeSpline": {
    "prefix": "CreateEdgeSpline",
    "text": "**OutPython.GeometryOut.CreateEdgeSpline**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateBarArc": {
    "prefix": "CreateBarArc",
    "text": "**OutPython.GeometryOut.CreateBarArc**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateBarSpline": {
    "prefix": "CreateBarSpline",
    "text": "**OutPython.GeometryOut.CreateBarSpline**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ImprintPerpendicularCylinderLineS": {
    "prefix": "ImprintPerpendicularCylinderLineS",
    "text": "**OutPython.GeometryOut.ImprintPerpendicularCylinderLineS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.Remove_Rib_Boss": {
    "prefix": "Remove_Rib_Boss",
    "text": "**OutPython.GeometryOut.Remove_Rib_Boss**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.Transform_CylinderFace": {
    "prefix": "Transform_CylinderFace",
    "text": "**OutPython.GeometryOut.Transform_CylinderFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.Geom_ShowAdjacent_Elements": {
    "prefix": "Geom_ShowAdjacent_Elements",
    "text": "**OutPython.GeometryOut.Geom_ShowAdjacent_Elements**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.Geom_ShowAdjacent": {
    "prefix": "Geom_ShowAdjacent",
    "text": "**OutPython.GeometryOut.Geom_ShowAdjacent**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.Geom_FindFeatures": {
    "prefix": "Geom_FindFeatures",
    "text": "**OutPython.GeometryOut.Geom_FindFeatures**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.DeletePartCr": {
    "prefix": "DeletePartCr",
    "text": "**OutPython.GeometryOut.DeletePartCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.DeleteVertexCr": {
    "prefix": "DeleteVertexCr",
    "text": "**OutPython.GeometryOut.DeleteVertexCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.DeleteFaceCr": {
    "prefix": "DeleteFaceCr",
    "text": "**OutPython.GeometryOut.DeleteFaceCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.DeleteEdgeCr": {
    "prefix": "DeleteEdgeCr",
    "text": "**OutPython.GeometryOut.DeleteEdgeCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.BreakEdgeCr": {
    "prefix": "BreakEdgeCr",
    "text": "**OutPython.GeometryOut.BreakEdgeCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MeshEditAdjustHalfCylinderCoordinateCr": {
    "prefix": "MeshEditAdjustHalfCylinderCoordinateCr",
    "text": "**OutPython.GeometryOut.MeshEditAdjustHalfCylinderCoordinateCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MergeBodyFaceCr": {
    "prefix": "MergeBodyFaceCr",
    "text": "**OutPython.GeometryOut.MergeBodyFaceCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MergeCBarPart": {
    "prefix": "MergeCBarPart",
    "text": "**OutPython.GeometryOut.MergeCBarPart**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.GeometryMergeEntitiesTinyFacesMerge_K": {
    "prefix": "GeometryMergeEntitiesTinyFacesMerge_K",
    "text": "**OutPython.GeometryOut.GeometryMergeEntitiesTinyFacesMerge_K**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ImprintMiddleLine": {
    "prefix": "ImprintMiddleLine",
    "text": "**OutPython.GeometryOut.ImprintMiddleLine**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.AdjustCircleVertex": {
    "prefix": "AdjustCircleVertex",
    "text": "**OutPython.GeometryOut.AdjustCircleVertex**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.GeometryFindFeatureEdge": {
    "prefix": "GeometryFindFeatureEdge",
    "text": "**OutPython.GeometryOut.GeometryFindFeatureEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.GeometryFindFeatureFace": {
    "prefix": "GeometryFindFeatureFace",
    "text": "**OutPython.GeometryOut.GeometryFindFeatureFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateTube": {
    "prefix": "CreateTube",
    "text": "**OutPython.GeometryOut.CreateTube**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.CreateCylinderPart": {
    "prefix": "CreateCylinderPart",
    "text": "**OutPython.GeometryOut.CreateCylinderPart**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.Transform3Points": {
    "prefix": "Transform3Points",
    "text": "**OutPython.GeometryOut.Transform3Points**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.ShipHull": {
    "prefix": "ShipHull",
    "text": "**OutPython.GeometryOut.ShipHull**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.MakeFaceSmoothFunc": {
    "prefix": "MakeFaceSmoothFunc",
    "text": "**OutPython.GeometryOut.MakeFaceSmoothFunc**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.TransformAxisAlignment": {
    "prefix": "TransformAxisAlignment",
    "text": "**OutPython.GeometryOut.TransformAxisAlignment**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.TransformPlaneAlignment": {
    "prefix": "TransformPlaneAlignment",
    "text": "**OutPython.GeometryOut.TransformPlaneAlignment**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.NewTinyFacesMerge": {
    "prefix": "NewTinyFacesMerge",
    "text": "**OutPython.GeometryOut.NewTinyFacesMerge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GeometryOut.BestFitFunc": {
    "prefix": "BestFitFunc",
    "text": "**OutPython.GeometryOut.BestFitFunc**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GroupsOut.CreateMaterialGroup": {
    "prefix": "CreateMaterialGroup",
    "text": "**OutPython.GroupsOut.CreateMaterialGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GroupsOut.CreatePropertyGroup": {
    "prefix": "CreatePropertyGroup",
    "text": "**OutPython.GroupsOut.CreatePropertyGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GroupsOut.DeleteGroup": {
    "prefix": "DeleteGroup",
    "text": "**OutPython.GroupsOut.DeleteGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GroupsOut.CopyGroup": {
    "prefix": "CopyGroup",
    "text": "**OutPython.GroupsOut.CopyGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GroupsOut.AddSupGroupEx": {
    "prefix": "AddSupGroupEx",
    "text": "**OutPython.GroupsOut.AddSupGroupEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.GroupsOut.AddSupGroup": {
    "prefix": "AddSupGroup",
    "text": "**OutPython.GroupsOut.AddSupGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.HexBoxMesh": {
    "prefix": "HexBoxMesh",
    "text": "**OutPython.HexModelingOut.HexBoxMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.HexModelingBallHexa": {
    "prefix": "HexModelingBallHexa",
    "text": "**OutPython.HexModelingOut.HexModelingBallHexa**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.HexSweepLayer": {
    "prefix": "HexSweepLayer",
    "text": "**OutPython.HexModelingOut.HexSweepLayer**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.SolidElemInterface": {
    "prefix": "SolidElemInterface",
    "text": "**OutPython.HexModelingOut.SolidElemInterface**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.SweepCloseLoopShape": {
    "prefix": "SweepCloseLoopShape",
    "text": "**OutPython.HexModelingOut.SweepCloseLoopShape**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.Shell2Hex": {
    "prefix": "Shell2Hex",
    "text": "**OutPython.HexModelingOut.Shell2Hex**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.HexSweepCircular": {
    "prefix": "HexSweepCircular",
    "text": "**OutPython.HexModelingOut.HexSweepCircular**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.HexSweepFaceToFace": {
    "prefix": "HexSweepFaceToFace",
    "text": "**OutPython.HexModelingOut.HexSweepFaceToFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.HexSweepCurve": {
    "prefix": "HexSweepCurve",
    "text": "**OutPython.HexModelingOut.HexSweepCurve**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.HexModelSweepLinear": {
    "prefix": "HexModelSweepLinear",
    "text": "**OutPython.HexModelingOut.HexModelSweepLinear**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HexModelingOut.HexModelAutoSweep": {
    "prefix": "HexModelAutoSweep",
    "text": "**OutPython.HexModelingOut.HexModelAutoSweep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportSpatial": {
    "prefix": "ImportSpatial",
    "text": "**OutPython.HomeOut.ImportSpatial**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportInp": {
    "prefix": "ImportInp",
    "text": "**OutPython.HomeOut.ImportInp**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportGeomBDF": {
    "prefix": "ImportGeomBDF",
    "text": "**OutPython.HomeOut.ImportGeomBDF**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportCreo": {
    "prefix": "ImportCreo",
    "text": "**OutPython.HomeOut.ImportCreo**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportLsDyna": {
    "prefix": "ImportLsDyna",
    "text": "**OutPython.HomeOut.ImportLsDyna**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportElysium": {
    "prefix": "ImportElysium",
    "text": "**OutPython.HomeOut.ImportElysium**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportUnv": {
    "prefix": "ImportUnv",
    "text": "**OutPython.HomeOut.ImportUnv**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ExportSTL": {
    "prefix": "ExportSTL",
    "text": "**OutPython.HomeOut.ExportSTL**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ExportGeomBDF": {
    "prefix": "ExportGeomBDF",
    "text": "**OutPython.HomeOut.ExportGeomBDF**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ExportTSG": {
    "prefix": "ExportTSG",
    "text": "**OutPython.HomeOut.ExportTSG**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.PostExportGeom": {
    "prefix": "PostExportGeom",
    "text": "**OutPython.HomeOut.PostExportGeom**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportAnsys": {
    "prefix": "ImportAnsys",
    "text": "**OutPython.HomeOut.ImportAnsys**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportVDB": {
    "prefix": "ImportVDB",
    "text": "**OutPython.HomeOut.ImportVDB**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportDirect_Parasolid": {
    "prefix": "ImportDirect_Parasolid",
    "text": "**OutPython.HomeOut.ImportDirect_Parasolid**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportDirect_STL": {
    "prefix": "ImportDirect_STL",
    "text": "**OutPython.HomeOut.ImportDirect_STL**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportDirect_VRML": {
    "prefix": "ImportDirect_VRML",
    "text": "**OutPython.HomeOut.ImportDirect_VRML**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.Capture_ToImageEx": {
    "prefix": "Capture_ToImageEx",
    "text": "**OutPython.HomeOut.Capture_ToImageEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewFindEntities": {
    "prefix": "ViewFindEntities",
    "text": "**OutPython.HomeOut.ViewFindEntities**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.Capture_Rectangular": {
    "prefix": "Capture_Rectangular",
    "text": "**OutPython.HomeOut.Capture_Rectangular**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.Capture_CopyToClipboardEx": {
    "prefix": "Capture_CopyToClipboardEx",
    "text": "**OutPython.HomeOut.Capture_CopyToClipboardEx**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ShowFullScreen": {
    "prefix": "ShowFullScreen",
    "text": "**OutPython.HomeOut.ShowFullScreen**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.SetSynchronize": {
    "prefix": "SetSynchronize",
    "text": "**OutPython.HomeOut.SetSynchronize**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.Export_Post_Viewer_File": {
    "prefix": "Export_Post_Viewer_File",
    "text": "**OutPython.HomeOut.Export_Post_Viewer_File**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.EXPORT_UNIVERSAL": {
    "prefix": "EXPORT_UNIVERSAL",
    "text": "**OutPython.HomeOut.EXPORT_UNIVERSAL**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportTSG": {
    "prefix": "ImportTSG",
    "text": "**OutPython.HomeOut.ImportTSG**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewControl_ResetCenter": {
    "prefix": "ViewControl_ResetCenter",
    "text": "**OutPython.HomeOut.ViewControl_ResetCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewControl_SetCenter": {
    "prefix": "ViewControl_SetCenter",
    "text": "**OutPython.HomeOut.ViewControl_SetCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewControl_Rotate": {
    "prefix": "ViewControl_Rotate",
    "text": "**OutPython.HomeOut.ViewControl_Rotate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewControl_Pan_Up": {
    "prefix": "ViewControl_Pan_Up",
    "text": "**OutPython.HomeOut.ViewControl_Pan_Up**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewControl_Pan_Down": {
    "prefix": "ViewControl_Pan_Down",
    "text": "**OutPython.HomeOut.ViewControl_Pan_Down**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewControl_Pan_Left": {
    "prefix": "ViewControl_Pan_Left",
    "text": "**OutPython.HomeOut.ViewControl_Pan_Left**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewControl_Pan_Right": {
    "prefix": "ViewControl_Pan_Right",
    "text": "**OutPython.HomeOut.ViewControl_Pan_Right**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewControl_Zoom_In": {
    "prefix": "ViewControl_Zoom_In",
    "text": "**OutPython.HomeOut.ViewControl_Zoom_In**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewControl_Zoom_Out": {
    "prefix": "ViewControl_Zoom_Out",
    "text": "**OutPython.HomeOut.ViewControl_Zoom_Out**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewControl_FitToModel": {
    "prefix": "ViewControl_FitToModel",
    "text": "**OutPython.HomeOut.ViewControl_FitToModel**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.PostExportToTxt": {
    "prefix": "PostExportToTxt",
    "text": "**OutPython.HomeOut.PostExportToTxt**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.Capture_ToPPT": {
    "prefix": "Capture_ToPPT",
    "text": "**OutPython.HomeOut.Capture_ToPPT**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ViewMakeUserFrame": {
    "prefix": "ViewMakeUserFrame",
    "text": "**OutPython.HomeOut.ViewMakeUserFrame**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportUniversalMesh": {
    "prefix": "ImportUniversalMesh",
    "text": "**OutPython.HomeOut.ImportUniversalMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportMarcMesh": {
    "prefix": "ImportMarcMesh",
    "text": "**OutPython.HomeOut.ImportMarcMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.TileHorizontal": {
    "prefix": "TileHorizontal",
    "text": "**OutPython.HomeOut.TileHorizontal**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessCancel": {
    "prefix": "FrameLessCancel",
    "text": "**OutPython.HomeOut.FrameLessCancel**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessHorizontalMode1": {
    "prefix": "FrameLessHorizontalMode1",
    "text": "**OutPython.HomeOut.FrameLessHorizontalMode1**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessHorizontalMode2": {
    "prefix": "FrameLessHorizontalMode2",
    "text": "**OutPython.HomeOut.FrameLessHorizontalMode2**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessHorizontalMode3": {
    "prefix": "FrameLessHorizontalMode3",
    "text": "**OutPython.HomeOut.FrameLessHorizontalMode3**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessHorizontalMode4": {
    "prefix": "FrameLessHorizontalMode4",
    "text": "**OutPython.HomeOut.FrameLessHorizontalMode4**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessHorizontalMode5": {
    "prefix": "FrameLessHorizontalMode5",
    "text": "**OutPython.HomeOut.FrameLessHorizontalMode5**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessHorizontalMode6": {
    "prefix": "FrameLessHorizontalMode6",
    "text": "**OutPython.HomeOut.FrameLessHorizontalMode6**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessHorizontalMode7": {
    "prefix": "FrameLessHorizontalMode7",
    "text": "**OutPython.HomeOut.FrameLessHorizontalMode7**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.TileVertical": {
    "prefix": "TileVertical",
    "text": "**OutPython.HomeOut.TileVertical**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessVerticalMode1": {
    "prefix": "FrameLessVerticalMode1",
    "text": "**OutPython.HomeOut.FrameLessVerticalMode1**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessVerticalMode2": {
    "prefix": "FrameLessVerticalMode2",
    "text": "**OutPython.HomeOut.FrameLessVerticalMode2**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessVerticalMode3": {
    "prefix": "FrameLessVerticalMode3",
    "text": "**OutPython.HomeOut.FrameLessVerticalMode3**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessVerticalMode4": {
    "prefix": "FrameLessVerticalMode4",
    "text": "**OutPython.HomeOut.FrameLessVerticalMode4**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessVerticalMode5": {
    "prefix": "FrameLessVerticalMode5",
    "text": "**OutPython.HomeOut.FrameLessVerticalMode5**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessVerticalMode6": {
    "prefix": "FrameLessVerticalMode6",
    "text": "**OutPython.HomeOut.FrameLessVerticalMode6**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessVerticalMode7": {
    "prefix": "FrameLessVerticalMode7",
    "text": "**OutPython.HomeOut.FrameLessVerticalMode7**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessBoxMode1": {
    "prefix": "FrameLessBoxMode1",
    "text": "**OutPython.HomeOut.FrameLessBoxMode1**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.FrameLessBoxMode2": {
    "prefix": "FrameLessBoxMode2",
    "text": "**OutPython.HomeOut.FrameLessBoxMode2**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ExportPreferenceSettings": {
    "prefix": "ExportPreferenceSettings",
    "text": "**OutPython.HomeOut.ExportPreferenceSettings**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ImportPreferenceSettings": {
    "prefix": "ImportPreferenceSettings",
    "text": "**OutPython.HomeOut.ImportPreferenceSettings**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.SetCalculateTrescaStress": {
    "prefix": "SetCalculateTrescaStress",
    "text": "**OutPython.HomeOut.SetCalculateTrescaStress**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.Capture_3DModel_ToPPT": {
    "prefix": "Capture_3DModel_ToPPT",
    "text": "**OutPython.HomeOut.Capture_3DModel_ToPPT**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.HomeOut.ExportGLB_Direct": {
    "prefix": "ExportGLB_Direct",
    "text": "**OutPython.HomeOut.ExportGLB_Direct**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.LabPreReleaseOut.CopyMeshPattern": {
    "prefix": "CopyMeshPattern",
    "text": "**OutPython.LabPreReleaseOut.CopyMeshPattern**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.bMergeFace": {
    "prefix": "bMergeFace",
    "text": "**OutPython.MainWindowOut.bMergeFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.FlipElement": {
    "prefix": "FlipElement",
    "text": "**OutPython.MainWindowOut.FlipElement**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.AssociatedPick": {
    "prefix": "AssociatedPick",
    "text": "**OutPython.MainWindowOut.AssociatedPick**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.SetPartAppearance": {
    "prefix": "SetPartAppearance",
    "text": "**OutPython.MainWindowOut.SetPartAppearance**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewInverseHide": {
    "prefix": "ViewInverseHide",
    "text": "**OutPython.MainWindowOut.ViewInverseHide**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewSelectAllParts": {
    "prefix": "ViewSelectAllParts",
    "text": "**OutPython.MainWindowOut.ViewSelectAllParts**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewShowAll": {
    "prefix": "ViewShowAll",
    "text": "**OutPython.MainWindowOut.ViewShowAll**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewShowAllHiddenFaces": {
    "prefix": "ViewShowAllHiddenFaces",
    "text": "**OutPython.MainWindowOut.ViewShowAllHiddenFaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ShowSettings": {
    "prefix": "ShowSettings",
    "text": "**OutPython.MainWindowOut.ShowSettings**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ShowHideFlip": {
    "prefix": "ShowHideFlip",
    "text": "**OutPython.MainWindowOut.ShowHideFlip**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ShowHideAllToolbar": {
    "prefix": "ShowHideAllToolbar",
    "text": "**OutPython.MainWindowOut.ShowHideAllToolbar**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewSelectAll": {
    "prefix": "ViewSelectAll",
    "text": "**OutPython.MainWindowOut.ViewSelectAll**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewSelectByFace": {
    "prefix": "ViewSelectByFace",
    "text": "**OutPython.MainWindowOut.ViewSelectByFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewSelectDisplayed": {
    "prefix": "ViewSelectDisplayed",
    "text": "**OutPython.MainWindowOut.ViewSelectDisplayed**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewSelectByWindow": {
    "prefix": "ViewSelectByWindow",
    "text": "**OutPython.MainWindowOut.ViewSelectByWindow**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewSelectReverse": {
    "prefix": "ViewSelectReverse",
    "text": "**OutPython.MainWindowOut.ViewSelectReverse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewSelectByAttached": {
    "prefix": "ViewSelectByAttached",
    "text": "**OutPython.MainWindowOut.ViewSelectByAttached**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.Show_Entity": {
    "prefix": "Show_Entity",
    "text": "**OutPython.MainWindowOut.Show_Entity**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.ViewInverseHideAll": {
    "prefix": "ViewInverseHideAll",
    "text": "**OutPython.MainWindowOut.ViewInverseHideAll**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MainWindowOut.SelectSurfaceColor": {
    "prefix": "SelectSurfaceColor",
    "text": "**OutPython.MainWindowOut.SelectSurfaceColor**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.MC_ManualCleanup_2QuadToQuad": {
    "prefix": "MC_ManualCleanup_2QuadToQuad",
    "text": "**OutPython.MeshCleanupOut.MC_ManualCleanup_2QuadToQuad**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.Equivalence": {
    "prefix": "Equivalence",
    "text": "**OutPython.MeshCleanupOut.Equivalence**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.DeleteElement": {
    "prefix": "DeleteElement",
    "text": "**OutPython.MeshCleanupOut.DeleteElement**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CreateElementHEX8": {
    "prefix": "CreateElementHEX8",
    "text": "**OutPython.MeshCleanupOut.CreateElementHEX8**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.SplitElemEdge": {
    "prefix": "SplitElemEdge",
    "text": "**OutPython.MeshCleanupOut.SplitElemEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleanupSwap": {
    "prefix": "CleanupSwap",
    "text": "**OutPython.MeshCleanupOut.CleanupSwap**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.ChangeTopoSolidElem": {
    "prefix": "ChangeTopoSolidElem",
    "text": "**OutPython.MeshCleanupOut.ChangeTopoSolidElem**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleaunpEdgeCollapse": {
    "prefix": "CleaunpEdgeCollapse",
    "text": "**OutPython.MeshCleanupOut.CleaunpEdgeCollapse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.SplitElement": {
    "prefix": "SplitElement",
    "text": "**OutPython.MeshCleanupOut.SplitElement**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CorrectModel": {
    "prefix": "CorrectModel",
    "text": "**OutPython.MeshCleanupOut.CorrectModel**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleanupHalfEdgeCollapse": {
    "prefix": "CleanupHalfEdgeCollapse",
    "text": "**OutPython.MeshCleanupOut.CleanupHalfEdgeCollapse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.SwapElemEdge": {
    "prefix": "SwapElemEdge",
    "text": "**OutPython.MeshCleanupOut.SwapElemEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.HalfEdgeCollapse": {
    "prefix": "HalfEdgeCollapse",
    "text": "**OutPython.MeshCleanupOut.HalfEdgeCollapse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleanupManual": {
    "prefix": "CleanupManual",
    "text": "**OutPython.MeshCleanupOut.CleanupManual**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.ChangeTopologyElement": {
    "prefix": "ChangeTopologyElement",
    "text": "**OutPython.MeshCleanupOut.ChangeTopologyElement**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.Collapse": {
    "prefix": "Collapse",
    "text": "**OutPython.MeshCleanupOut.Collapse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleanupAuto": {
    "prefix": "CleanupAuto",
    "text": "**OutPython.MeshCleanupOut.CleanupAuto**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CreateElement": {
    "prefix": "CreateElement",
    "text": "**OutPython.MeshCleanupOut.CreateElement**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CreateElementPENTA5": {
    "prefix": "CreateElementPENTA5",
    "text": "**OutPython.MeshCleanupOut.CreateElementPENTA5**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleanupRemoveNode": {
    "prefix": "CleanupRemoveNode",
    "text": "**OutPython.MeshCleanupOut.CleanupRemoveNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CloseGaps": {
    "prefix": "CloseGaps",
    "text": "**OutPython.MeshCleanupOut.CloseGaps**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleanupCenterFaceCollapse": {
    "prefix": "CleanupCenterFaceCollapse",
    "text": "**OutPython.MeshCleanupOut.CleanupCenterFaceCollapse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleanupCenterCollapse": {
    "prefix": "CleanupCenterCollapse",
    "text": "**OutPython.MeshCleanupOut.CleanupCenterCollapse**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CloseHoles": {
    "prefix": "CloseHoles",
    "text": "**OutPython.MeshCleanupOut.CloseHoles**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CreateElementTET4": {
    "prefix": "CreateElementTET4",
    "text": "**OutPython.MeshCleanupOut.CreateElementTET4**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.FindHoles": {
    "prefix": "FindHoles",
    "text": "**OutPython.MeshCleanupOut.FindHoles**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.MC_ManualCleanup_2TrisToQuad": {
    "prefix": "MC_ManualCleanup_2TrisToQuad",
    "text": "**OutPython.MeshCleanupOut.MC_ManualCleanup_2TrisToQuad**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleanupEquivalence": {
    "prefix": "CleanupEquivalence",
    "text": "**OutPython.MeshCleanupOut.CleanupEquivalence**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleanupSplit": {
    "prefix": "CleanupSplit",
    "text": "**OutPython.MeshCleanupOut.CleanupSplit**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.LocalRemeshTriQuad_MC2D": {
    "prefix": "LocalRemeshTriQuad_MC2D",
    "text": "**OutPython.MeshCleanupOut.LocalRemeshTriQuad_MC2D**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CreateElementCr": {
    "prefix": "CreateElementCr",
    "text": "**OutPython.MeshCleanupOut.CreateElementCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.ChangeTopoFaceCr": {
    "prefix": "ChangeTopoFaceCr",
    "text": "**OutPython.MeshCleanupOut.ChangeTopoFaceCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.MC_Mesh_Quality_Manual_Check_Tri": {
    "prefix": "MC_Mesh_Quality_Manual_Check_Tri",
    "text": "**OutPython.MeshCleanupOut.MC_Mesh_Quality_Manual_Check_Tri**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.MC_Mesh_Quality_Manual_Check_Quad": {
    "prefix": "MC_Mesh_Quality_Manual_Check_Quad",
    "text": "**OutPython.MeshCleanupOut.MC_Mesh_Quality_Manual_Check_Quad**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.MC_Mesh_Quality_Manual_Check_Hex": {
    "prefix": "MC_Mesh_Quality_Manual_Check_Hex",
    "text": "**OutPython.MeshCleanupOut.MC_Mesh_Quality_Manual_Check_Hex**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshCleanupOut.CleaningVolumeMesh": {
    "prefix": "CleaningVolumeMesh",
    "text": "**OutPython.MeshCleanupOut.CleaningVolumeMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditMorphingFaces": {
    "prefix": "MeshEditMorphingFaces",
    "text": "**OutPython.MeshEditOut.MeshEditMorphingFaces**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodePoint": {
    "prefix": "MoveNodePoint",
    "text": "**OutPython.MeshEditOut.MoveNodePoint**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.CreateNodeEdgeCenter": {
    "prefix": "CreateNodeEdgeCenter",
    "text": "**OutPython.MeshEditOut.CreateNodeEdgeCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditCreateNodeCylindCenter": {
    "prefix": "MeshEditCreateNodeCylindCenter",
    "text": "**OutPython.MeshEditOut.MeshEditCreateNodeCylindCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditCreateNodeSphereCenter": {
    "prefix": "MeshEditCreateNodeSphereCenter",
    "text": "**OutPython.MeshEditOut.MeshEditCreateNodeSphereCenter**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.ElementConvert": {
    "prefix": "ElementConvert",
    "text": "**OutPython.MeshEditOut.ElementConvert**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodeAlignNode": {
    "prefix": "MoveNodeAlignNode",
    "text": "**OutPython.MeshEditOut.MoveNodeAlignNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.GeometryDeform": {
    "prefix": "GeometryDeform",
    "text": "**OutPython.MeshEditOut.GeometryDeform**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MirrorCopy": {
    "prefix": "MirrorCopy",
    "text": "**OutPython.MeshEditOut.MirrorCopy**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.CreateNode": {
    "prefix": "CreateNode",
    "text": "**OutPython.MeshEditOut.CreateNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.DeleteNode": {
    "prefix": "DeleteNode",
    "text": "**OutPython.MeshEditOut.DeleteNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditCMPFaceImprint": {
    "prefix": "MeshEditCMPFaceImprint",
    "text": "**OutPython.MeshEditOut.MeshEditCMPFaceImprint**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.CreateNodeImport": {
    "prefix": "CreateNodeImport",
    "text": "**OutPython.MeshEditOut.CreateNodeImport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditMoveNodeEqualize": {
    "prefix": "MeshEditMoveNodeEqualize",
    "text": "**OutPython.MeshEditOut.MeshEditMoveNodeEqualize**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodeNormalOffset": {
    "prefix": "MoveNodeNormalOffset",
    "text": "**OutPython.MeshEditOut.MoveNodeNormalOffset**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.GeomEditAdjustOrientation": {
    "prefix": "GeomEditAdjustOrientation",
    "text": "**OutPython.MeshEditOut.GeomEditAdjustOrientation**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditMorphingOneNode": {
    "prefix": "MeshEditMorphingOneNode",
    "text": "**OutPython.MeshEditOut.MeshEditMorphingOneNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditCreateNodePoint": {
    "prefix": "MeshEditCreateNodePoint",
    "text": "**OutPython.MeshEditOut.MeshEditCreateNodePoint**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditCreateNodeAtNode": {
    "prefix": "MeshEditCreateNodeAtNode",
    "text": "**OutPython.MeshEditOut.MeshEditCreateNodeAtNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.Coincident_Nodes": {
    "prefix": "Coincident_Nodes",
    "text": "**OutPython.MeshEditOut.Coincident_Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditCreateNodeBetween2Nodes": {
    "prefix": "MeshEditCreateNodeBetween2Nodes",
    "text": "**OutPython.MeshEditOut.MeshEditCreateNodeBetween2Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditCreateNodeBetween3Nodes": {
    "prefix": "MeshEditCreateNodeBetween3Nodes",
    "text": "**OutPython.MeshEditOut.MeshEditCreateNodeBetween3Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditCreateNodeProjectNode": {
    "prefix": "MeshEditCreateNodeProjectNode",
    "text": "**OutPython.MeshEditOut.MeshEditCreateNodeProjectNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.SeparateNode": {
    "prefix": "SeparateNode",
    "text": "**OutPython.MeshEditOut.SeparateNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodeAlongCylinder": {
    "prefix": "MoveNodeAlongCylinder",
    "text": "**OutPython.MeshEditOut.MoveNodeAlongCylinder**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MergeNode": {
    "prefix": "MergeNode",
    "text": "**OutPython.MeshEditOut.MergeNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodeNode2PlanNodes": {
    "prefix": "MoveNodeNode2PlanNodes",
    "text": "**OutPython.MeshEditOut.MoveNodeNode2PlanNodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodeDeform": {
    "prefix": "MoveNodeDeform",
    "text": "**OutPython.MeshEditOut.MoveNodeDeform**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.RemoveSolidMesh": {
    "prefix": "RemoveSolidMesh",
    "text": "**OutPython.MeshEditOut.RemoveSolidMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.CreateNodeOffset": {
    "prefix": "CreateNodeOffset",
    "text": "**OutPython.MeshEditOut.CreateNodeOffset**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshCopy": {
    "prefix": "MeshCopy",
    "text": "**OutPython.MeshEditOut.MeshCopy**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditMorphingRibThickness": {
    "prefix": "MeshEditMorphingRibThickness",
    "text": "**OutPython.MeshEditOut.MeshEditMorphingRibThickness**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditMoveNodeScale": {
    "prefix": "MeshEditMoveNodeScale",
    "text": "**OutPython.MeshEditOut.MeshEditMoveNodeScale**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.LaplacianSmooth": {
    "prefix": "LaplacianSmooth",
    "text": "**OutPython.MeshEditOut.LaplacianSmooth**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditMoveNodeOnEdge": {
    "prefix": "MeshEditMoveNodeOnEdge",
    "text": "**OutPython.MeshEditOut.MeshEditMoveNodeOnEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditCreateNodeCenterofGravity": {
    "prefix": "MeshEditCreateNodeCenterofGravity",
    "text": "**OutPython.MeshEditOut.MeshEditCreateNodeCenterofGravity**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodeCADFollows": {
    "prefix": "MoveNodeCADFollows",
    "text": "**OutPython.MeshEditOut.MoveNodeCADFollows**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.NodeMovedByDirection": {
    "prefix": "NodeMovedByDirection",
    "text": "**OutPython.MeshEditOut.NodeMovedByDirection**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditCreatePenta": {
    "prefix": "MeshEditCreatePenta",
    "text": "**OutPython.MeshEditOut.MeshEditCreatePenta**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.CreateElementHEX8_ME": {
    "prefix": "CreateElementHEX8_ME",
    "text": "**OutPython.MeshEditOut.CreateElementHEX8_ME**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.ElementConv_Surface": {
    "prefix": "ElementConv_Surface",
    "text": "**OutPython.MeshEditOut.ElementConv_Surface**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.ElementConv_Solid": {
    "prefix": "ElementConv_Solid",
    "text": "**OutPython.MeshEditOut.ElementConv_Solid**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.CreateElementTET4_ME": {
    "prefix": "CreateElementTET4_ME",
    "text": "**OutPython.MeshEditOut.CreateElementTET4_ME**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.CreateNodeProjectToLine": {
    "prefix": "CreateNodeProjectToLine",
    "text": "**OutPython.MeshEditOut.CreateNodeProjectToLine**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.CreateNodeIntersectionNode": {
    "prefix": "CreateNodeIntersectionNode",
    "text": "**OutPython.MeshEditOut.CreateNodeIntersectionNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodeAbsoluteCr": {
    "prefix": "MoveNodeAbsoluteCr",
    "text": "**OutPython.MeshEditOut.MoveNodeAbsoluteCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodeStraightenMidNodesCr": {
    "prefix": "MoveNodeStraightenMidNodesCr",
    "text": "**OutPython.MeshEditOut.MoveNodeStraightenMidNodesCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.GeomEditChangePatternCr": {
    "prefix": "GeomEditChangePatternCr",
    "text": "**OutPython.MeshEditOut.GeomEditChangePatternCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.CreateElementTRI3Cr": {
    "prefix": "CreateElementTRI3Cr",
    "text": "**OutPython.MeshEditOut.CreateElementTRI3Cr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.CreateElementQUAD4Cr": {
    "prefix": "CreateElementQUAD4Cr",
    "text": "**OutPython.MeshEditOut.CreateElementQUAD4Cr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.DividePartByRegion": {
    "prefix": "DividePartByRegion",
    "text": "**OutPython.MeshEditOut.DividePartByRegion**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditMoveNodeRefineQuality": {
    "prefix": "MeshEditMoveNodeRefineQuality",
    "text": "**OutPython.MeshEditOut.MeshEditMoveNodeRefineQuality**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MeshEditMoveNodeOffset": {
    "prefix": "MeshEditMoveNodeOffset",
    "text": "**OutPython.MeshEditOut.MeshEditMoveNodeOffset**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodeAlignNodeCr": {
    "prefix": "MoveNodeAlignNodeCr",
    "text": "**OutPython.MeshEditOut.MoveNodeAlignNodeCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.MoveNodeNode2PlanElemCr": {
    "prefix": "MoveNodeNode2PlanElemCr",
    "text": "**OutPython.MeshEditOut.MoveNodeNode2PlanElemCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshEditOut.QuadMeshCleanupCustom": {
    "prefix": "QuadMeshCleanupCustom",
    "text": "**OutPython.MeshEditOut.QuadMeshCleanupCustom**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.BeamMeshing": {
    "prefix": "BeamMeshing",
    "text": "**OutPython.MeshingOut.BeamMeshing**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.TemplateCopy": {
    "prefix": "TemplateCopy",
    "text": "**OutPython.MeshingOut.TemplateCopy**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.SearchTargetFacesInModel": {
    "prefix": "SearchTargetFacesInModel",
    "text": "**OutPython.MeshingOut.SearchTargetFacesInModel**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.FilletMapMeshing": {
    "prefix": "FilletMapMeshing",
    "text": "**OutPython.MeshingOut.FilletMapMeshing**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CadProject_Part": {
    "prefix": "CadProject_Part",
    "text": "**OutPython.MeshingOut.CadProject_Part**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CadProject_Face": {
    "prefix": "CadProject_Face",
    "text": "**OutPython.MeshingOut.CadProject_Face**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CadProject_FaceToFace": {
    "prefix": "CadProject_FaceToFace",
    "text": "**OutPython.MeshingOut.CadProject_FaceToFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CadProject_NodeToFace": {
    "prefix": "CadProject_NodeToFace",
    "text": "**OutPython.MeshingOut.CadProject_NodeToFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CadProject_NodeToEdge": {
    "prefix": "CadProject_NodeToEdge",
    "text": "**OutPython.MeshingOut.CadProject_NodeToEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.LocalRemeshSolid": {
    "prefix": "LocalRemeshSolid",
    "text": "**OutPython.MeshingOut.LocalRemeshSolid**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.SurfaceMeshing2D": {
    "prefix": "SurfaceMeshing2D",
    "text": "**OutPython.MeshingOut.SurfaceMeshing2D**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.MeshEditAdjustVertex": {
    "prefix": "MeshEditAdjustVertex",
    "text": "**OutPython.MeshingOut.MeshEditAdjustVertex**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.SetMeshAttrib": {
    "prefix": "SetMeshAttrib",
    "text": "**OutPython.MeshingOut.SetMeshAttrib**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.LocalRemeshTriQuad": {
    "prefix": "LocalRemeshTriQuad",
    "text": "**OutPython.MeshingOut.LocalRemeshTriQuad**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.FilletFaceSearch": {
    "prefix": "FilletFaceSearch",
    "text": "**OutPython.MeshingOut.FilletFaceSearch**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CreateLocalSetting_Edge": {
    "prefix": "CreateLocalSetting_Edge",
    "text": "**OutPython.MeshingOut.CreateLocalSetting_Edge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CreateLocalSetting_Face": {
    "prefix": "CreateLocalSetting_Face",
    "text": "**OutPython.MeshingOut.CreateLocalSetting_Face**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CreateLocalSetting_FaceElement": {
    "prefix": "CreateLocalSetting_FaceElement",
    "text": "**OutPython.MeshingOut.CreateLocalSetting_FaceElement**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CreateLocalSetting_Model": {
    "prefix": "CreateLocalSetting_Model",
    "text": "**OutPython.MeshingOut.CreateLocalSetting_Model**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CreateLocalSetting_Part": {
    "prefix": "CreateLocalSetting_Part",
    "text": "**OutPython.MeshingOut.CreateLocalSetting_Part**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.CreateLocalSetting_Points": {
    "prefix": "CreateLocalSetting_Points",
    "text": "**OutPython.MeshingOut.CreateLocalSetting_Points**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.MeshingLocalMeshingGridMeshNew": {
    "prefix": "MeshingLocalMeshingGridMeshNew",
    "text": "**OutPython.MeshingOut.MeshingLocalMeshingGridMeshNew**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.FullQuadRemesh": {
    "prefix": "FullQuadRemesh",
    "text": "**OutPython.MeshingOut.FullQuadRemesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.AutoFullQuadRemeshForPart": {
    "prefix": "AutoFullQuadRemeshForPart",
    "text": "**OutPython.MeshingOut.AutoFullQuadRemeshForPart**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.LOCALSETTING_FOR_BOLT_HOLE": {
    "prefix": "LOCALSETTING_FOR_BOLT_HOLE",
    "text": "**OutPython.MeshingOut.LOCALSETTING_FOR_BOLT_HOLE**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.ExportMeshSetting": {
    "prefix": "ExportMeshSetting",
    "text": "**OutPython.MeshingOut.ExportMeshSetting**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MeshingOut.ImportMeshSetting": {
    "prefix": "ImportMeshSetting",
    "text": "**OutPython.MeshingOut.ImportMeshSetting**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.GeometryAddItemsEdgeProjectEdgetoFace": {
    "prefix": "GeometryAddItemsEdgeProjectEdgetoFace",
    "text": "**OutPython.MidPlaneEditOut.GeometryAddItemsEdgeProjectEdgetoFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.GeometryAddItemsEdgeExtendCylinderFace": {
    "prefix": "GeometryAddItemsEdgeExtendCylinderFace",
    "text": "**OutPython.MidPlaneEditOut.GeometryAddItemsEdgeExtendCylinderFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.ExtendFaceCylinderFace": {
    "prefix": "ExtendFaceCylinderFace",
    "text": "**OutPython.MidPlaneEditOut.ExtendFaceCylinderFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.GeometryAddItemFaceByEFExtend": {
    "prefix": "GeometryAddItemFaceByEFExtend",
    "text": "**OutPython.MidPlaneEditOut.GeometryAddItemFaceByEFExtend**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.GeometryAddItemFaceByEFProject": {
    "prefix": "GeometryAddItemFaceByEFProject",
    "text": "**OutPython.MidPlaneEditOut.GeometryAddItemFaceByEFProject**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.GeometryAddItemFaceByFaceExtend": {
    "prefix": "GeometryAddItemFaceByFaceExtend",
    "text": "**OutPython.MidPlaneEditOut.GeometryAddItemFaceByFaceExtend**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.MidplaneManualOffset": {
    "prefix": "MidplaneManualOffset",
    "text": "**OutPython.MidPlaneEditOut.MidplaneManualOffset**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.GeometryAddItemFaceByPlaneExtendIntersection": {
    "prefix": "GeometryAddItemFaceByPlaneExtendIntersection",
    "text": "**OutPython.MidPlaneEditOut.GeometryAddItemFaceByPlaneExtendIntersection**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.MidplaneManualMidByPair": {
    "prefix": "MidplaneManualMidByPair",
    "text": "**OutPython.MidPlaneEditOut.MidplaneManualMidByPair**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.MidplaneExtendPlane": {
    "prefix": "MidplaneExtendPlane",
    "text": "**OutPython.MidPlaneEditOut.MidplaneExtendPlane**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.GeometryAddItemFaceByEdges": {
    "prefix": "GeometryAddItemFaceByEdges",
    "text": "**OutPython.MidPlaneEditOut.GeometryAddItemFaceByEdges**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.MidplaneEditAddEdgeNodes": {
    "prefix": "MidplaneEditAddEdgeNodes",
    "text": "**OutPython.MidPlaneEditOut.MidplaneEditAddEdgeNodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneEditOut.GeometryAddItemsEdgeProjectEdgetoFaceCr": {
    "prefix": "GeometryAddItemsEdgeProjectEdgetoFaceCr",
    "text": "**OutPython.MidPlaneEditOut.GeometryAddItemsEdgeProjectEdgetoFaceCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneOut.MidPlaneAdjustThickness": {
    "prefix": "MidPlaneAdjustThickness",
    "text": "**OutPython.MidPlaneOut.MidPlaneAdjustThickness**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneOut.MidPlaneFaceCross": {
    "prefix": "MidPlaneFaceCross",
    "text": "**OutPython.MidPlaneOut.MidPlaneFaceCross**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneOut.FindMidPlane": {
    "prefix": "FindMidPlane",
    "text": "**OutPython.MidPlaneOut.FindMidPlane**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneOut.MidPlaneCreateThickProps": {
    "prefix": "MidPlaneCreateThickProps",
    "text": "**OutPython.MidPlaneOut.MidPlaneCreateThickProps**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneOut.PressShell": {
    "prefix": "PressShell",
    "text": "**OutPython.MidPlaneOut.PressShell**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MidPlaneOut.PressShellV2": {
    "prefix": "PressShellV2",
    "text": "**OutPython.MidPlaneOut.PressShellV2**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MufflerHAOut.LocalSettingEdgeNodeCountAuto": {
    "prefix": "LocalSettingEdgeNodeCountAuto",
    "text": "**OutPython.MufflerHAOut.LocalSettingEdgeNodeCountAuto**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MufflerHAOut.Imprint_ProjectionLine": {
    "prefix": "Imprint_ProjectionLine",
    "text": "**OutPython.MufflerHAOut.Imprint_ProjectionLine**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MufflerTOut.CreateRod": {
    "prefix": "CreateRod",
    "text": "**OutPython.MufflerTOut.CreateRod**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MufflerTOut.ThermalShockAnalysis": {
    "prefix": "ThermalShockAnalysis",
    "text": "**OutPython.MufflerTOut.ThermalShockAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MuxWeldOut.CreateBeadWeld": {
    "prefix": "CreateBeadWeld",
    "text": "**OutPython.MuxWeldOut.CreateBeadWeld**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MuxWeldOut.Prop3DWeldBead": {
    "prefix": "Prop3DWeldBead",
    "text": "**OutPython.MuxWeldOut.Prop3DWeldBead**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MuxWeldOut.ConnectionWeld": {
    "prefix": "ConnectionWeld",
    "text": "**OutPython.MuxWeldOut.ConnectionWeld**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MuxWeldOut.DefineWeldOrder": {
    "prefix": "DefineWeldOrder",
    "text": "**OutPython.MuxWeldOut.DefineWeldOrder**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.MuxWeldOut.WeldHexSweepBodyCr": {
    "prefix": "WeldHexSweepBodyCr",
    "text": "**OutPython.MuxWeldOut.WeldHexSweepBodyCr**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.NSModelingOut.NSModeling_Close_Hole": {
    "prefix": "NSModeling_Close_Hole",
    "text": "**OutPython.NSModelingOut.NSModeling_Close_Hole**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdShowHideMaxMin": {
    "prefix": "CmdShowHideMaxMin",
    "text": "**OutPython.PostOut.CmdShowHideMaxMin**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.ImportOp2Mesh": {
    "prefix": "ImportOp2Mesh",
    "text": "**OutPython.PostOut.ImportOp2Mesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.NastranOp2PostJob": {
    "prefix": "NastranOp2PostJob",
    "text": "**OutPython.PostOut.NastranOp2PostJob**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.ImportHDF5Mesh": {
    "prefix": "ImportHDF5Mesh",
    "text": "**OutPython.PostOut.ImportHDF5Mesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.ImportADVCMesh": {
    "prefix": "ImportADVCMesh",
    "text": "**OutPython.PostOut.ImportADVCMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.ADVC2PostJobOut": {
    "prefix": "ADVC2PostJobOut",
    "text": "**OutPython.PostOut.ADVC2PostJobOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.NastranHDF5PostJobOut": {
    "prefix": "NastranHDF5PostJobOut",
    "text": "**OutPython.PostOut.NastranHDF5PostJobOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdPostPeakSearchForNode": {
    "prefix": "CmdPostPeakSearchForNode",
    "text": "**OutPython.PostOut.CmdPostPeakSearchForNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdResetPostContour": {
    "prefix": "CmdResetPostContour",
    "text": "**OutPython.PostOut.CmdResetPostContour**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdResetPostDeformation": {
    "prefix": "CmdResetPostDeformation",
    "text": "**OutPython.PostOut.CmdResetPostDeformation**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.ShowContour": {
    "prefix": "ShowContour",
    "text": "**OutPython.PostOut.ShowContour**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CreateTemplate": {
    "prefix": "CreateTemplate",
    "text": "**OutPython.PostOut.CreateTemplate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdPostAreaMaxMin": {
    "prefix": "CmdPostAreaMaxMin",
    "text": "**OutPython.PostOut.CmdPostAreaMaxMin**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdEnableMiddleNodes": {
    "prefix": "CmdEnableMiddleNodes",
    "text": "**OutPython.PostOut.CmdEnableMiddleNodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdDistancePlot": {
    "prefix": "CmdDistancePlot",
    "text": "**OutPython.PostOut.CmdDistancePlot**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdMaxMinPlot": {
    "prefix": "CmdMaxMinPlot",
    "text": "**OutPython.PostOut.CmdMaxMinPlot**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdMarkupNode": {
    "prefix": "CmdMarkupNode",
    "text": "**OutPython.PostOut.CmdMarkupNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdMarkupElement": {
    "prefix": "CmdMarkupElement",
    "text": "**OutPython.PostOut.CmdMarkupElement**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdMarkupFacePoint": {
    "prefix": "CmdMarkupFacePoint",
    "text": "**OutPython.PostOut.CmdMarkupFacePoint**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.DisplayPartialContour": {
    "prefix": "DisplayPartialContour",
    "text": "**OutPython.PostOut.DisplayPartialContour**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdPostMaxMinSettings": {
    "prefix": "CmdPostMaxMinSettings",
    "text": "**OutPython.PostOut.CmdPostMaxMinSettings**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdPostTransparencySettings": {
    "prefix": "CmdPostTransparencySettings",
    "text": "**OutPython.PostOut.CmdPostTransparencySettings**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CopyTemplate": {
    "prefix": "CopyTemplate",
    "text": "**OutPython.PostOut.CopyTemplate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.DeleteTemplate": {
    "prefix": "DeleteTemplate",
    "text": "**OutPython.PostOut.DeleteTemplate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.UpdateTemplate": {
    "prefix": "UpdateTemplate",
    "text": "**OutPython.PostOut.UpdateTemplate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.ImportTemplate": {
    "prefix": "ImportTemplate",
    "text": "**OutPython.PostOut.ImportTemplate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.ExportTemplate": {
    "prefix": "ExportTemplate",
    "text": "**OutPython.PostOut.ExportTemplate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.LoadTemplate": {
    "prefix": "LoadTemplate",
    "text": "**OutPython.PostOut.LoadTemplate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteResultTitle": {
    "prefix": "SetNoteResultTitle",
    "text": "**OutPython.PostOut.SetNoteResultTitle**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteResultData": {
    "prefix": "SetNoteResultData",
    "text": "**OutPython.PostOut.SetNoteResultData**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteColorBackground": {
    "prefix": "SetNoteColorBackground",
    "text": "**OutPython.PostOut.SetNoteColorBackground**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteColorText": {
    "prefix": "SetNoteColorText",
    "text": "**OutPython.PostOut.SetNoteColorText**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteColorLine": {
    "prefix": "SetNoteColorLine",
    "text": "**OutPython.PostOut.SetNoteColorLine**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteNumericDisplay": {
    "prefix": "SetNoteNumericDisplay",
    "text": "**OutPython.PostOut.SetNoteNumericDisplay**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteElementType": {
    "prefix": "SetNoteElementType",
    "text": "**OutPython.PostOut.SetNoteElementType**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteElementMatID": {
    "prefix": "SetNoteElementMatID",
    "text": "**OutPython.PostOut.SetNoteElementMatID**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteElementPropID": {
    "prefix": "SetNoteElementPropID",
    "text": "**OutPython.PostOut.SetNoteElementPropID**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteElementNodeID": {
    "prefix": "SetNoteElementNodeID",
    "text": "**OutPython.PostOut.SetNoteElementNodeID**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteResultDisp": {
    "prefix": "SetNoteResultDisp",
    "text": "**OutPython.PostOut.SetNoteResultDisp**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteResultNumber": {
    "prefix": "SetNoteResultNumber",
    "text": "**OutPython.PostOut.SetNoteResultNumber**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteResultPos": {
    "prefix": "SetNoteResultPos",
    "text": "**OutPython.PostOut.SetNoteResultPos**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteResultUnit": {
    "prefix": "SetNoteResultUnit",
    "text": "**OutPython.PostOut.SetNoteResultUnit**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteResultSubID": {
    "prefix": "SetNoteResultSubID",
    "text": "**OutPython.PostOut.SetNoteResultSubID**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetNoteResultPrnVector": {
    "prefix": "SetNoteResultPrnVector",
    "text": "**OutPython.PostOut.SetNoteResultPrnVector**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdMarkupSearchNodeFromPoint": {
    "prefix": "CmdMarkupSearchNodeFromPoint",
    "text": "**OutPython.PostOut.CmdMarkupSearchNodeFromPoint**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdMarkupSearchElementFromPoint": {
    "prefix": "CmdMarkupSearchElementFromPoint",
    "text": "**OutPython.PostOut.CmdMarkupSearchElementFromPoint**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdMarkupSearchNodesFromMultiPoints": {
    "prefix": "CmdMarkupSearchNodesFromMultiPoints",
    "text": "**OutPython.PostOut.CmdMarkupSearchNodesFromMultiPoints**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdMarkupSearchElementsFromMultiPoints": {
    "prefix": "CmdMarkupSearchElementsFromMultiPoints",
    "text": "**OutPython.PostOut.CmdMarkupSearchElementsFromMultiPoints**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdMarkupSearchPoint": {
    "prefix": "CmdMarkupSearchPoint",
    "text": "**OutPython.PostOut.CmdMarkupSearchPoint**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdMarkupSearchMultiPoints": {
    "prefix": "CmdMarkupSearchMultiPoints",
    "text": "**OutPython.PostOut.CmdMarkupSearchMultiPoints**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CreatePostFatigueMaterial": {
    "prefix": "CreatePostFatigueMaterial",
    "text": "**OutPython.PostOut.CreatePostFatigueMaterial**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.EnableOptimizationRenderMode": {
    "prefix": "EnableOptimizationRenderMode",
    "text": "**OutPython.PostOut.EnableOptimizationRenderMode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.SetHidingElementFactor": {
    "prefix": "SetHidingElementFactor",
    "text": "**OutPython.PostOut.SetHidingElementFactor**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdOptimizeShapeSmoothFunc": {
    "prefix": "CmdOptimizeShapeSmoothFunc",
    "text": "**OutPython.PostOut.CmdOptimizeShapeSmoothFunc**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.CmdOptimizeOuterShellExport": {
    "prefix": "CmdOptimizeOuterShellExport",
    "text": "**OutPython.PostOut.CmdOptimizeOuterShellExport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PostOut.PostToolFatigueResult": {
    "prefix": "PostToolFatigueResult",
    "text": "**OutPython.PostOut.PostToolFatigueResult**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property2DShellOut": {
    "prefix": "Property2DShellOut",
    "text": "**OutPython.PropertiesOut.Property2DShellOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.CreateMaterial": {
    "prefix": "CreateMaterial",
    "text": "**OutPython.PropertiesOut.CreateMaterial**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Prop3DCohesive": {
    "prefix": "Prop3DCohesive",
    "text": "**OutPython.PropertiesOut.Prop3DCohesive**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Prop3DGasket": {
    "prefix": "Prop3DGasket",
    "text": "**OutPython.PropertiesOut.Prop3DGasket**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DSectionImport": {
    "prefix": "Property1DSectionImport",
    "text": "**OutPython.PropertiesOut.Property1DSectionImport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.RenumberPropertyTable": {
    "prefix": "RenumberPropertyTable",
    "text": "**OutPython.PropertiesOut.RenumberPropertyTable**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DRodOut": {
    "prefix": "Property1DRodOut",
    "text": "**OutPython.PropertiesOut.Property1DRodOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DSectionExport": {
    "prefix": "Property1DSectionExport",
    "text": "**OutPython.PropertiesOut.Property1DSectionExport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DSectionDelMulti": {
    "prefix": "Property1DSectionDelMulti",
    "text": "**OutPython.PropertiesOut.Property1DSectionDelMulti**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DBeamSimple": {
    "prefix": "Property1DBeamSimple",
    "text": "**OutPython.PropertiesOut.Property1DBeamSimple**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DSectionModify_General": {
    "prefix": "Property1DSectionModify_General",
    "text": "**OutPython.PropertiesOut.Property1DSectionModify_General**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DSectionModify_Library": {
    "prefix": "Property1DSectionModify_Library",
    "text": "**OutPython.PropertiesOut.Property1DSectionModify_Library**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DSectionModify_Sketcher": {
    "prefix": "Property1DSectionModify_Sketcher",
    "text": "**OutPython.PropertiesOut.Property1DSectionModify_Sketcher**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DBarOut": {
    "prefix": "Property1DBarOut",
    "text": "**OutPython.PropertiesOut.Property1DBarOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.ElemRelatedInfo_Conn": {
    "prefix": "ElemRelatedInfo_Conn",
    "text": "**OutPython.PropertiesOut.ElemRelatedInfo_Conn**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property3DSolidOut": {
    "prefix": "Property3DSolidOut",
    "text": "**OutPython.PropertiesOut.Property3DSolidOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DSection": {
    "prefix": "Property1DSection",
    "text": "**OutPython.PropertiesOut.Property1DSection**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DBeamOut": {
    "prefix": "Property1DBeamOut",
    "text": "**OutPython.PropertiesOut.Property1DBeamOut**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Create2DCompositeMaterialShellProperty": {
    "prefix": "Create2DCompositeMaterialShellProperty",
    "text": "**OutPython.PropertiesOut.Create2DCompositeMaterialShellProperty**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DSectionAdd_Sketcher": {
    "prefix": "Property1DSectionAdd_Sketcher",
    "text": "**OutPython.PropertiesOut.Property1DSectionAdd_Sketcher**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DSectionAdd_Library": {
    "prefix": "Property1DSectionAdd_Library",
    "text": "**OutPython.PropertiesOut.Property1DSectionAdd_Library**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DSectionAdd_General": {
    "prefix": "Property1DSectionAdd_General",
    "text": "**OutPython.PropertiesOut.Property1DSectionAdd_General**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.ElemRelatedInfo_Rod": {
    "prefix": "ElemRelatedInfo_Rod",
    "text": "**OutPython.PropertiesOut.ElemRelatedInfo_Rod**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.ElemRelatedInfo_Beam": {
    "prefix": "ElemRelatedInfo_Beam",
    "text": "**OutPython.PropertiesOut.ElemRelatedInfo_Beam**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.ElemRelatedInfo_Bar": {
    "prefix": "ElemRelatedInfo_Bar",
    "text": "**OutPython.PropertiesOut.ElemRelatedInfo_Bar**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.ElemRelatedInfo_Shell": {
    "prefix": "ElemRelatedInfo_Shell",
    "text": "**OutPython.PropertiesOut.ElemRelatedInfo_Shell**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.ElemRelatedInfo_Gap": {
    "prefix": "ElemRelatedInfo_Gap",
    "text": "**OutPython.PropertiesOut.ElemRelatedInfo_Gap**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.ElemRelatedInfo_Bush": {
    "prefix": "ElemRelatedInfo_Bush",
    "text": "**OutPython.PropertiesOut.ElemRelatedInfo_Bush**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.ThicknessDistribution": {
    "prefix": "ThicknessDistribution",
    "text": "**OutPython.PropertiesOut.ThicknessDistribution**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property2DRigidBody": {
    "prefix": "Property2DRigidBody",
    "text": "**OutPython.PropertiesOut.Property2DRigidBody**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.Property1DBeamN": {
    "prefix": "Property1DBeamN",
    "text": "**OutPython.PropertiesOut.Property1DBeamN**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PropertiesOut.ImportFromMLIB": {
    "prefix": "ImportFromMLIB",
    "text": "**OutPython.PropertiesOut.ImportFromMLIB**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.SuzukiAutoReportCommonSetting": {
    "prefix": "SuzukiAutoReportCommonSetting",
    "text": "**OutPython.PTAutoReportOut.SuzukiAutoReportCommonSetting**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.RightMountSlidingOpeningAnalysisReport": {
    "prefix": "RightMountSlidingOpeningAnalysisReport",
    "text": "**OutPython.PTAutoReportOut.RightMountSlidingOpeningAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.PowerPlantFrameVibrationAnalysisReport": {
    "prefix": "PowerPlantFrameVibrationAnalysisReport",
    "text": "**OutPython.PTAutoReportOut.PowerPlantFrameVibrationAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.BafflePlateFatigueReport": {
    "prefix": "BafflePlateFatigueReport",
    "text": "**OutPython.PTAutoReportOut.BafflePlateFatigueReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.PistonSidewallAnalysisReport": {
    "prefix": "PistonSidewallAnalysisReport",
    "text": "**OutPython.PTAutoReportOut.PistonSidewallAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.SuzukiAutoReportPulleyBoltBendingStress": {
    "prefix": "SuzukiAutoReportPulleyBoltBendingStress",
    "text": "**OutPython.PTAutoReportOut.SuzukiAutoReportPulleyBoltBendingStress**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.SuzukiAutoReportPulleyBoltLoosening": {
    "prefix": "SuzukiAutoReportPulleyBoltLoosening",
    "text": "**OutPython.PTAutoReportOut.SuzukiAutoReportPulleyBoltLoosening**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.WaterPipeEigenAnalysisReport": {
    "prefix": "WaterPipeEigenAnalysisReport",
    "text": "**OutPython.PTAutoReportOut.WaterPipeEigenAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.SuzukiAutoReportStressAnalysisForCrank": {
    "prefix": "SuzukiAutoReportStressAnalysisForCrank",
    "text": "**OutPython.PTAutoReportOut.SuzukiAutoReportStressAnalysisForCrank**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.CrankshaftDynamicRigidityAnalysis": {
    "prefix": "CrankshaftDynamicRigidityAnalysis",
    "text": "**OutPython.PTAutoReportOut.CrankshaftDynamicRigidityAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.CrankshaftRigidityAnalysis": {
    "prefix": "CrankshaftRigidityAnalysis",
    "text": "**OutPython.PTAutoReportOut.CrankshaftRigidityAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.CrankshaftHighCycleFatigue": {
    "prefix": "CrankshaftHighCycleFatigue",
    "text": "**OutPython.PTAutoReportOut.CrankshaftHighCycleFatigue**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.GasketSealabilityReport": {
    "prefix": "GasketSealabilityReport",
    "text": "**OutPython.PTAutoReportOut.GasketSealabilityReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.LeftMountSlidingOpeningAnalysisReport": {
    "prefix": "LeftMountSlidingOpeningAnalysisReport",
    "text": "**OutPython.PTAutoReportOut.LeftMountSlidingOpeningAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.OilPumpCaseSealabilityReport": {
    "prefix": "OilPumpCaseSealabilityReport",
    "text": "**OutPython.PTAutoReportOut.OilPumpCaseSealabilityReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.ChainTensionerStrengthReport": {
    "prefix": "ChainTensionerStrengthReport",
    "text": "**OutPython.PTAutoReportOut.ChainTensionerStrengthReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.ChainGuideStrengthReport": {
    "prefix": "ChainGuideStrengthReport",
    "text": "**OutPython.PTAutoReportOut.ChainGuideStrengthReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.PowerPlantAlternatorACCompressorVibrationReport": {
    "prefix": "PowerPlantAlternatorACCompressorVibrationReport",
    "text": "**OutPython.PTAutoReportOut.PowerPlantAlternatorACCompressorVibrationReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.MufflerFrequencyResponseAnalysis": {
    "prefix": "MufflerFrequencyResponseAnalysis",
    "text": "**OutPython.PTAutoReportOut.MufflerFrequencyResponseAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.StaticStiffnessForMountBRKTReport": {
    "prefix": "StaticStiffnessForMountBRKTReport",
    "text": "**OutPython.PTAutoReportOut.StaticStiffnessForMountBRKTReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.VibrationForStrainerBaffleReport": {
    "prefix": "VibrationForStrainerBaffleReport",
    "text": "**OutPython.PTAutoReportOut.VibrationForStrainerBaffleReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.InitStressOfInclinedBoltsReport": {
    "prefix": "InitStressOfInclinedBoltsReport",
    "text": "**OutPython.PTAutoReportOut.InitStressOfInclinedBoltsReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.ACOutletHoseBlockagePredictionReport": {
    "prefix": "ACOutletHoseBlockagePredictionReport",
    "text": "**OutPython.PTAutoReportOut.ACOutletHoseBlockagePredictionReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.AirCleanerSurfaceStiffnessAnalysisReport": {
    "prefix": "AirCleanerSurfaceStiffnessAnalysisReport",
    "text": "**OutPython.PTAutoReportOut.AirCleanerSurfaceStiffnessAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.PowerPlantExhaustSystemVibrationAnalysisReport": {
    "prefix": "PowerPlantExhaustSystemVibrationAnalysisReport",
    "text": "**OutPython.PTAutoReportOut.PowerPlantExhaustSystemVibrationAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.SurfaceStiffnessAnalysisOfEnginePartsReport": {
    "prefix": "SurfaceStiffnessAnalysisOfEnginePartsReport",
    "text": "**OutPython.PTAutoReportOut.SurfaceStiffnessAnalysisOfEnginePartsReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.MufHangerStrengthAndEigenValueReport": {
    "prefix": "MufHangerStrengthAndEigenValueReport",
    "text": "**OutPython.PTAutoReportOut.MufHangerStrengthAndEigenValueReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.PistonSkirtRigidityReport": {
    "prefix": "PistonSkirtRigidityReport",
    "text": "**OutPython.PTAutoReportOut.PistonSkirtRigidityReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.PistonHighTempHighCycleFatigueReport": {
    "prefix": "PistonHighTempHighCycleFatigueReport",
    "text": "**OutPython.PTAutoReportOut.PistonHighTempHighCycleFatigueReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.StaticStiffnessForVehicleMountBRKTReport": {
    "prefix": "StaticStiffnessForVehicleMountBRKTReport",
    "text": "**OutPython.PTAutoReportOut.StaticStiffnessForVehicleMountBRKTReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.FuelPipeStrengthVibrationAnalysisReport": {
    "prefix": "FuelPipeStrengthVibrationAnalysisReport",
    "text": "**OutPython.PTAutoReportOut.FuelPipeStrengthVibrationAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.CamshaftHighCycleFatigueReport": {
    "prefix": "CamshaftHighCycleFatigueReport",
    "text": "**OutPython.PTAutoReportOut.CamshaftHighCycleFatigueReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.DeliveryPipeStrengthVibrationAnalysisReport": {
    "prefix": "DeliveryPipeStrengthVibrationAnalysisReport",
    "text": "**OutPython.PTAutoReportOut.DeliveryPipeStrengthVibrationAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.PTAutoReportOut.MountBracketFrequencyResponseAnalysisReport": {
    "prefix": "MountBracketFrequencyResponseAnalysisReport",
    "text": "**OutPython.PTAutoReportOut.MountBracketFrequencyResponseAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ReportOut.CmdWriteCSVForGeneralReportLinearStatic": {
    "prefix": "CmdWriteCSVForGeneralReportLinearStatic",
    "text": "**OutPython.ReportOut.CmdWriteCSVForGeneralReportLinearStatic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ReportOut.CmdGeneralReportLinearStatic": {
    "prefix": "CmdGeneralReportLinearStatic",
    "text": "**OutPython.ReportOut.CmdGeneralReportLinearStatic**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ReportOut.ResultOutputList": {
    "prefix": "ResultOutputList",
    "text": "**OutPython.ReportOut.ResultOutputList**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ReportOut.CmdWriteCSVForGeneralReportModal": {
    "prefix": "CmdWriteCSVForGeneralReportModal",
    "text": "**OutPython.ReportOut.CmdWriteCSVForGeneralReportModal**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ReportOut.CmdGeneralReportModal": {
    "prefix": "CmdGeneralReportModal",
    "text": "**OutPython.ReportOut.CmdGeneralReportModal**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ReportOut.CmdPostPPTMultiShots": {
    "prefix": "CmdPostPPTMultiShots",
    "text": "**OutPython.ReportOut.CmdPostPPTMultiShots**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ReportTOut.ReportToolOverall": {
    "prefix": "ReportToolOverall",
    "text": "**OutPython.ReportTOut.ReportToolOverall**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ResultsOut.PostTreeItemRename": {
    "prefix": "PostTreeItemRename",
    "text": "**OutPython.ResultsOut.PostTreeItemRename**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ResultsOut.PostTreeItemDeleted": {
    "prefix": "PostTreeItemDeleted",
    "text": "**OutPython.ResultsOut.PostTreeItemDeleted**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.SNOnePushOut.SonyOnePushCadImport": {
    "prefix": "SonyOnePushCadImport",
    "text": "**OutPython.SNOnePushOut.SonyOnePushCadImport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.SNOnePushOut.AutoSweepClosedLoopShaped": {
    "prefix": "AutoSweepClosedLoopShaped",
    "text": "**OutPython.SNOnePushOut.AutoSweepClosedLoopShaped**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.SNOnePushOut.CalcTimeStep": {
    "prefix": "CalcTimeStep",
    "text": "**OutPython.SNOnePushOut.CalcTimeStep**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.SNOnePushOut.DropTest": {
    "prefix": "DropTest",
    "text": "**OutPython.SNOnePushOut.DropTest**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.SNOnePushOut.UpdateFloor": {
    "prefix": "UpdateFloor",
    "text": "**OutPython.SNOnePushOut.UpdateFloor**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.SNOnePushOut.DropRotation": {
    "prefix": "DropRotation",
    "text": "**OutPython.SNOnePushOut.DropRotation**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.StiffCalcOut.PermasForce": {
    "prefix": "PermasForce",
    "text": "**OutPython.StiffCalcOut.PermasForce**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.SZOnepushReliabilityOut.SORCreateWeld": {
    "prefix": "SORCreateWeld",
    "text": "**OutPython.SZOnepushReliabilityOut.SORCreateWeld**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.SZOnepushReliabilityOut.SORAlignMidNode": {
    "prefix": "SORAlignMidNode",
    "text": "**OutPython.SZOnepushReliabilityOut.SORAlignMidNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.SZOnepushReliabilityOut.SORFilletMapping": {
    "prefix": "SORFilletMapping",
    "text": "**OutPython.SZOnepushReliabilityOut.SORFilletMapping**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.SZOnepushReliabilityOut.SOR_CopyContactSurface": {
    "prefix": "SOR_CopyContactSurface",
    "text": "**OutPython.SZOnepushReliabilityOut.SOR_CopyContactSurface**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.TestOut.ConnRRod": {
    "prefix": "ConnRRod",
    "text": "**OutPython.TestOut.ConnRRod**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.TestOut.FindFacesInPart": {
    "prefix": "FindFacesInPart",
    "text": "**OutPython.TestOut.FindFacesInPart**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.TestOut.CreateElementForWelding": {
    "prefix": "CreateElementForWelding",
    "text": "**OutPython.TestOut.CreateElementForWelding**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.TestOut.IntersectionCheckZGeom": {
    "prefix": "IntersectionCheckZGeom",
    "text": "**OutPython.TestOut.IntersectionCheckZGeom**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.TestOut.WeldingEdgeHGA": {
    "prefix": "WeldingEdgeHGA",
    "text": "**OutPython.TestOut.WeldingEdgeHGA**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.TestOut.ReplaceSolidMesh": {
    "prefix": "ReplaceSolidMesh",
    "text": "**OutPython.TestOut.ReplaceSolidMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolbarOut.Undo": {
    "prefix": "Undo",
    "text": "**OutPython.ToolbarOut.Undo**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolbarOut.Redo": {
    "prefix": "Redo",
    "text": "**OutPython.ToolbarOut.Redo**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolOut.CreateContact": {
    "prefix": "CreateContact",
    "text": "**OutPython.ToolOut.CreateContact**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolOut.Imprint_ClosedLine": {
    "prefix": "Imprint_ClosedLine",
    "text": "**OutPython.ToolOut.Imprint_ClosedLine**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolOut.Prop0DMass": {
    "prefix": "Prop0DMass",
    "text": "**OutPython.ToolOut.Prop0DMass**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateGroup": {
    "prefix": "CreateGroup",
    "text": "**OutPython.ToolsOut.CreateGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.DeleteGroupEntity": {
    "prefix": "DeleteGroupEntity",
    "text": "**OutPython.ToolsOut.DeleteGroupEntity**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistance_Edge": {
    "prefix": "MeasureDistance_Edge",
    "text": "**OutPython.ToolsOut.MeasureDistance_Edge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistance_EdgeNode": {
    "prefix": "MeasureDistance_EdgeNode",
    "text": "**OutPython.ToolsOut.MeasureDistance_EdgeNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistance_2Points": {
    "prefix": "MeasureDistance_2Points",
    "text": "**OutPython.ToolsOut.MeasureDistance_2Points**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureVolumeParts": {
    "prefix": "MeasureVolumeParts",
    "text": "**OutPython.ToolsOut.MeasureVolumeParts**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistanceByLine2Nodes_Node": {
    "prefix": "MeasureDistanceByLine2Nodes_Node",
    "text": "**OutPython.ToolsOut.MeasureDistanceByLine2Nodes_Node**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureAngleByProjected_Node": {
    "prefix": "MeasureAngleByProjected_Node",
    "text": "**OutPython.ToolsOut.MeasureAngleByProjected_Node**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistance_2Edges": {
    "prefix": "MeasureDistance_2Edges",
    "text": "**OutPython.ToolsOut.MeasureDistance_2Edges**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureAngleBy2Nodes_Axis": {
    "prefix": "MeasureAngleBy2Nodes_Axis",
    "text": "**OutPython.ToolsOut.MeasureAngleBy2Nodes_Axis**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateNCSGroup": {
    "prefix": "CreateNCSGroup",
    "text": "**OutPython.ToolsOut.CreateNCSGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.AddNodeCS": {
    "prefix": "AddNodeCS",
    "text": "**OutPython.ToolsOut.AddNodeCS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistanceByPlaneElem_Node": {
    "prefix": "MeasureDistanceByPlaneElem_Node",
    "text": "**OutPython.ToolsOut.MeasureDistanceByPlaneElem_Node**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.RenumberSpecify": {
    "prefix": "RenumberSpecify",
    "text": "**OutPython.ToolsOut.RenumberSpecify**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.ModifyElemDir": {
    "prefix": "ModifyElemDir",
    "text": "**OutPython.ToolsOut.ModifyElemDir**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistance_2Nodes": {
    "prefix": "MeasureDistance_2Nodes",
    "text": "**OutPython.ToolsOut.MeasureDistance_2Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateCoordinateCylinderFace": {
    "prefix": "CreateCoordinateCylinderFace",
    "text": "**OutPython.ToolsOut.CreateCoordinateCylinderFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateCoordinateThreeNode": {
    "prefix": "CreateCoordinateThreeNode",
    "text": "**OutPython.ToolsOut.CreateCoordinateThreeNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateCoordinateAlign": {
    "prefix": "CreateCoordinateAlign",
    "text": "**OutPython.ToolsOut.CreateCoordinateAlign**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateCoordinateOffset": {
    "prefix": "CreateCoordinateOffset",
    "text": "**OutPython.ToolsOut.CreateCoordinateOffset**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateCoordinateRotate": {
    "prefix": "CreateCoordinateRotate",
    "text": "**OutPython.ToolsOut.CreateCoordinateRotate**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateCoordinateAttachCircle": {
    "prefix": "CreateCoordinateAttachCircle",
    "text": "**OutPython.ToolsOut.CreateCoordinateAttachCircle**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateCoordinateAttachNode": {
    "prefix": "CreateCoordinateAttachNode",
    "text": "**OutPython.ToolsOut.CreateCoordinateAttachNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateCoordinateFace": {
    "prefix": "CreateCoordinateFace",
    "text": "**OutPython.ToolsOut.CreateCoordinateFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.ImportCS": {
    "prefix": "ImportCS",
    "text": "**OutPython.ToolsOut.ImportCS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.ExportCS": {
    "prefix": "ExportCS",
    "text": "**OutPython.ToolsOut.ExportCS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureRadiusBy3Nodes": {
    "prefix": "MeasureRadiusBy3Nodes",
    "text": "**OutPython.ToolsOut.MeasureRadiusBy3Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistanceByNode2Face": {
    "prefix": "MeasureDistanceByNode2Face",
    "text": "**OutPython.ToolsOut.MeasureDistanceByNode2Face**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.AddDispCS": {
    "prefix": "AddDispCS",
    "text": "**OutPython.ToolsOut.AddDispCS**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureAngleBy2Axis": {
    "prefix": "MeasureAngleBy2Axis",
    "text": "**OutPython.ToolsOut.MeasureAngleBy2Axis**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistanceBy2Edges": {
    "prefix": "MeasureDistanceBy2Edges",
    "text": "**OutPython.ToolsOut.MeasureDistanceBy2Edges**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.RenumberE": {
    "prefix": "RenumberE",
    "text": "**OutPython.ToolsOut.RenumberE**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.RenumberSpecify_byPosition": {
    "prefix": "RenumberSpecify_byPosition",
    "text": "**OutPython.ToolsOut.RenumberSpecify_byPosition**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CreateDispCSGroup": {
    "prefix": "CreateDispCSGroup",
    "text": "**OutPython.ToolsOut.CreateDispCSGroup**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.RenumberByConnection": {
    "prefix": "RenumberByConnection",
    "text": "**OutPython.ToolsOut.RenumberByConnection**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.RenumberByFile": {
    "prefix": "RenumberByFile",
    "text": "**OutPython.ToolsOut.RenumberByFile**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureAngleBy3Nodes": {
    "prefix": "MeasureAngleBy3Nodes",
    "text": "**OutPython.ToolsOut.MeasureAngleBy3Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureAngleBy2ElemEdges": {
    "prefix": "MeasureAngleBy2ElemEdges",
    "text": "**OutPython.ToolsOut.MeasureAngleBy2ElemEdges**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureTotalLoad_ForLBC": {
    "prefix": "MeasureTotalLoad_ForLBC",
    "text": "**OutPython.ToolsOut.MeasureTotalLoad_ForLBC**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureTotalLoad_ForModel": {
    "prefix": "MeasureTotalLoad_ForModel",
    "text": "**OutPython.ToolsOut.MeasureTotalLoad_ForModel**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureTotalLoad_ForNode": {
    "prefix": "MeasureTotalLoad_ForNode",
    "text": "**OutPython.ToolsOut.MeasureTotalLoad_ForNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureTotalLoad_ForPart": {
    "prefix": "MeasureTotalLoad_ForPart",
    "text": "**OutPython.ToolsOut.MeasureTotalLoad_ForPart**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureTotalLoad_ForFace": {
    "prefix": "MeasureTotalLoad_ForFace",
    "text": "**OutPython.ToolsOut.MeasureTotalLoad_ForFace**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.ModelInfoCreateReport": {
    "prefix": "ModelInfoCreateReport",
    "text": "**OutPython.ToolsOut.ModelInfoCreateReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureRadiusByEdge": {
    "prefix": "MeasureRadiusByEdge",
    "text": "**OutPython.ToolsOut.MeasureRadiusByEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureAngleBy2Edges": {
    "prefix": "MeasureAngleBy2Edges",
    "text": "**OutPython.ToolsOut.MeasureAngleBy2Edges**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.ViewSection": {
    "prefix": "ViewSection",
    "text": "**OutPython.ToolsOut.ViewSection**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureMassByProperty": {
    "prefix": "MeasureMassByProperty",
    "text": "**OutPython.ToolsOut.MeasureMassByProperty**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureMassByMaterial": {
    "prefix": "MeasureMassByMaterial",
    "text": "**OutPython.ToolsOut.MeasureMassByMaterial**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.RenumberSpecify_OriginalID": {
    "prefix": "RenumberSpecify_OriginalID",
    "text": "**OutPython.ToolsOut.RenumberSpecify_OriginalID**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistanceBy2Nodes": {
    "prefix": "MeasureDistanceBy2Nodes",
    "text": "**OutPython.ToolsOut.MeasureDistanceBy2Nodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistanceBy2Points": {
    "prefix": "MeasureDistanceBy2Points",
    "text": "**OutPython.ToolsOut.MeasureDistanceBy2Points**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistanceByEdge": {
    "prefix": "MeasureDistanceByEdge",
    "text": "**OutPython.ToolsOut.MeasureDistanceByEdge**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistanceByEdge_Node": {
    "prefix": "MeasureDistanceByEdge_Node",
    "text": "**OutPython.ToolsOut.MeasureDistanceByEdge_Node**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureDistanceByPlane3Nodes_Node": {
    "prefix": "MeasureDistanceByPlane3Nodes_Node",
    "text": "**OutPython.ToolsOut.MeasureDistanceByPlane3Nodes_Node**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.measure_area_part": {
    "prefix": "measure_area_part",
    "text": "**OutPython.ToolsOut.measure_area_part**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.measure_area_face": {
    "prefix": "measure_area_face",
    "text": "**OutPython.ToolsOut.measure_area_face**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.measure_area_elem": {
    "prefix": "measure_area_elem",
    "text": "**OutPython.ToolsOut.measure_area_elem**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.MeasureForce": {
    "prefix": "MeasureForce",
    "text": "**OutPython.ToolsOut.MeasureForce**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.ToPre": {
    "prefix": "ToPre",
    "text": "**OutPython.ToolsOut.ToPre**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.ToPost": {
    "prefix": "ToPost",
    "text": "**OutPython.ToolsOut.ToPost**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.CmdPostProperty": {
    "prefix": "CmdPostProperty",
    "text": "**OutPython.ToolsOut.CmdPostProperty**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.ContourCopy": {
    "prefix": "ContourCopy",
    "text": "**OutPython.ToolsOut.ContourCopy**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.ToolsOut.HideContourDraftAngle": {
    "prefix": "HideContourDraftAngle",
    "text": "**OutPython.ToolsOut.HideContourDraftAngle**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.UtilityOut.FindEntities": {
    "prefix": "FindEntities",
    "text": "**OutPython.UtilityOut.FindEntities**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.WatchDataOut.CmdDataPaneDeleteAll": {
    "prefix": "CmdDataPaneDeleteAll",
    "text": "**OutPython.WatchDataOut.CmdDataPaneDeleteAll**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.WatchSelectedOut.WatchSelectedDataSaveToFile": {
    "prefix": "WatchSelectedDataSaveToFile",
    "text": "**OutPython.WatchSelectedOut.WatchSelectedDataSaveToFile**  \nPSJ command. See the reference for arguments and usage."
  },
  "OutPython.WebGLOut.PostResultLogger": {
    "prefix": "PostResultLogger",
    "text": "**OutPython.WebGLOut.PostResultLogger**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Calculation.PeakSearch": {
    "prefix": "PeakSearch",
    "text": "**Post.Calculation.PeakSearch**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Calculation.FatigueMaterial": {
    "prefix": "FatigueMaterial",
    "text": "**Post.Calculation.FatigueMaterial**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ExportResults.PostViewerFile": {
    "prefix": "PostViewerFile",
    "text": "**Post.ExportResults.PostViewerFile**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ImportResults.ImportOp2Mesh": {
    "prefix": "ImportOp2Mesh",
    "text": "**Post.ImportResults.ImportOp2Mesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ImportResults.NastranOp2PostJob": {
    "prefix": "NastranOp2PostJob",
    "text": "**Post.ImportResults.NastranOp2PostJob**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ImportResults.HDF5Mesh": {
    "prefix": "HDF5Mesh",
    "text": "**Post.ImportResults.HDF5Mesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ImportResults.ADVC2PostJob": {
    "prefix": "ADVC2PostJob",
    "text": "**Post.ImportResults.ADVC2PostJob**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ImportResults.NastranHDF5": {
    "prefix": "NastranHDF5",
    "text": "**Post.ImportResults.NastranHDF5**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Note.Node": {
    "prefix": "Node",
    "text": "**Post.Note.Node**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Note.NodeSearchFromPoints": {
    "prefix": "NodeSearchFromPoints",
    "text": "**Post.Note.NodeSearchFromPoints**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Note.Element": {
    "prefix": "Element",
    "text": "**Post.Note.Element**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Note.ElementSearchFromPoints": {
    "prefix": "ElementSearchFromPoints",
    "text": "**Post.Note.ElementSearchFromPoints**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Note.Position": {
    "prefix": "Position",
    "text": "**Post.Note.Position**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Note.SearchPositions": {
    "prefix": "SearchPositions",
    "text": "**Post.Note.SearchPositions**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Plot.MaxMinPlot": {
    "prefix": "MaxMinPlot",
    "text": "**Post.Plot.MaxMinPlot**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ResultSettings.Animation": {
    "prefix": "Animation",
    "text": "**Post.ResultSettings.Animation**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ResultSettings.Circle": {
    "prefix": "Circle",
    "text": "**Post.ResultSettings.Circle**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ResultSettings.Contour": {
    "prefix": "Contour",
    "text": "**Post.ResultSettings.Contour**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ResultSettings.Deformation": {
    "prefix": "Deformation",
    "text": "**Post.ResultSettings.Deformation**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ResultSettings.Diagram": {
    "prefix": "Diagram",
    "text": "**Post.ResultSettings.Diagram**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ResultSettings.MaxMin": {
    "prefix": "MaxMin",
    "text": "**Post.ResultSettings.MaxMin**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ResultSettings.Opacity": {
    "prefix": "Opacity",
    "text": "**Post.ResultSettings.Opacity**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ResultSettings.FFT3DDisplay": {
    "prefix": "FFT3DDisplay",
    "text": "**Post.ResultSettings.FFT3DDisplay**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ResultSettings.Title": {
    "prefix": "Title",
    "text": "**Post.ResultSettings.Title**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ResultSettings.Vector": {
    "prefix": "Vector",
    "text": "**Post.ResultSettings.Vector**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ColorBackground": {
    "prefix": "ColorBackground",
    "text": "**Post.SetNote.ColorBackground**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ColorText": {
    "prefix": "ColorText",
    "text": "**Post.SetNote.ColorText**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ColorLine": {
    "prefix": "ColorLine",
    "text": "**Post.SetNote.ColorLine**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.NumericDisplay": {
    "prefix": "NumericDisplay",
    "text": "**Post.SetNote.NumericDisplay**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ElementType": {
    "prefix": "ElementType",
    "text": "**Post.SetNote.ElementType**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ElementMatID": {
    "prefix": "ElementMatID",
    "text": "**Post.SetNote.ElementMatID**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ElementPropID": {
    "prefix": "ElementPropID",
    "text": "**Post.SetNote.ElementPropID**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ElementNodeID": {
    "prefix": "ElementNodeID",
    "text": "**Post.SetNote.ElementNodeID**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ResultDisp": {
    "prefix": "ResultDisp",
    "text": "**Post.SetNote.ResultDisp**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ResultNumber": {
    "prefix": "ResultNumber",
    "text": "**Post.SetNote.ResultNumber**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ResultPos": {
    "prefix": "ResultPos",
    "text": "**Post.SetNote.ResultPos**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ResultTitle": {
    "prefix": "ResultTitle",
    "text": "**Post.SetNote.ResultTitle**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ResultData": {
    "prefix": "ResultData",
    "text": "**Post.SetNote.ResultData**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ResultUnit": {
    "prefix": "ResultUnit",
    "text": "**Post.SetNote.ResultUnit**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.SetNote.ResultSubID": {
    "prefix": "ResultSubID",
    "text": "**Post.SetNote.ResultSubID**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Template.Create": {
    "prefix": "Create",
    "text": "**Post.Template.Create**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Template.Copy": {
    "prefix": "Copy",
    "text": "**Post.Template.Copy**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Template.Delete": {
    "prefix": "Delete",
    "text": "**Post.Template.Delete**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Template.Update": {
    "prefix": "Update",
    "text": "**Post.Template.Update**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Template.Import": {
    "prefix": "Import",
    "text": "**Post.Template.Import**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Template.Export": {
    "prefix": "Export",
    "text": "**Post.Template.Export**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.Template.Load": {
    "prefix": "Load",
    "text": "**Post.Template.Load**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ShowMaxMin": {
    "prefix": "ShowMaxMin",
    "text": "**Post.ShowMaxMin**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.ShowContour": {
    "prefix": "ShowContour",
    "text": "**Post.ShowContour**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.UnloadContour": {
    "prefix": "UnloadContour",
    "text": "**Post.UnloadContour**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.UnloadDeformation": {
    "prefix": "UnloadDeformation",
    "text": "**Post.UnloadDeformation**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.DisplayContour": {
    "prefix": "DisplayContour",
    "text": "**Post.DisplayContour**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.AreaMaxMin": {
    "prefix": "AreaMaxMin",
    "text": "**Post.AreaMaxMin**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.EnableMiddleNodes": {
    "prefix": "EnableMiddleNodes",
    "text": "**Post.EnableMiddleNodes**  \nPSJ command. See the reference for arguments and usage."
  },
  "Post.PartialContour": {
    "prefix": "PartialContour",
    "text": "**Post.PartialContour**  \nPSJ command. See the reference for arguments and usage."
  },
  "Properties.Material.ImportFromMLIB": {
    "prefix": "ImportFromMLIB",
    "text": "**Properties.Material.ImportFromMLIB**  \nPSJ command. See the reference for arguments and usage."
  },
  "Properties.Property1DBeamSimple": {
    "prefix": "Property1DBeamSimple",
    "text": "**Properties.Property1DBeamSimple**  \nPSJ command. See the reference for arguments and usage."
  },
  "Properties.Section1D": {
    "prefix": "Section1D",
    "text": "**Properties.Section1D**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.WebViewerCommonSetting": {
    "prefix": "WebViewerCommonSetting",
    "text": "**PTAutoReport.WebViewerCommonSetting**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.RightMountSlidingOpeningAnalysisReport": {
    "prefix": "RightMountSlidingOpeningAnalysisReport",
    "text": "**PTAutoReport.RightMountSlidingOpeningAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.PowerPlantFrameVibrationAnalysisReport": {
    "prefix": "PowerPlantFrameVibrationAnalysisReport",
    "text": "**PTAutoReport.PowerPlantFrameVibrationAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.BafflePlateFatigueReport": {
    "prefix": "BafflePlateFatigueReport",
    "text": "**PTAutoReport.BafflePlateFatigueReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.PistonSidewallAnalysisReport": {
    "prefix": "PistonSidewallAnalysisReport",
    "text": "**PTAutoReport.PistonSidewallAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.SuzukiAutoReportPulleyBoltBendingStress": {
    "prefix": "SuzukiAutoReportPulleyBoltBendingStress",
    "text": "**PTAutoReport.SuzukiAutoReportPulleyBoltBendingStress**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.SuzukiAutoReportPulleyBoltLoosening": {
    "prefix": "SuzukiAutoReportPulleyBoltLoosening",
    "text": "**PTAutoReport.SuzukiAutoReportPulleyBoltLoosening**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.SuzukiAutoReportStressAnalysisForCrank": {
    "prefix": "SuzukiAutoReportStressAnalysisForCrank",
    "text": "**PTAutoReport.SuzukiAutoReportStressAnalysisForCrank**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.CrankshaftDynamicRigidityAnalysis": {
    "prefix": "CrankshaftDynamicRigidityAnalysis",
    "text": "**PTAutoReport.CrankshaftDynamicRigidityAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.CrankshaftRigidityAnalysis": {
    "prefix": "CrankshaftRigidityAnalysis",
    "text": "**PTAutoReport.CrankshaftRigidityAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.CrankshaftHighCycleFatigue": {
    "prefix": "CrankshaftHighCycleFatigue",
    "text": "**PTAutoReport.CrankshaftHighCycleFatigue**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.WaterPipeEigenAnalysisReport": {
    "prefix": "WaterPipeEigenAnalysisReport",
    "text": "**PTAutoReport.WaterPipeEigenAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.GasketSealabilityReport": {
    "prefix": "GasketSealabilityReport",
    "text": "**PTAutoReport.GasketSealabilityReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.LeftMountSlidingOpeningAnalysisReport": {
    "prefix": "LeftMountSlidingOpeningAnalysisReport",
    "text": "**PTAutoReport.LeftMountSlidingOpeningAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.OilPumpCaseSealabilityReport": {
    "prefix": "OilPumpCaseSealabilityReport",
    "text": "**PTAutoReport.OilPumpCaseSealabilityReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.ChainTensionerStrengthReport": {
    "prefix": "ChainTensionerStrengthReport",
    "text": "**PTAutoReport.ChainTensionerStrengthReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.ChainGuideStrengthReport": {
    "prefix": "ChainGuideStrengthReport",
    "text": "**PTAutoReport.ChainGuideStrengthReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.PowerPlantAlternatorACCompressorVibrationAnalysisReport": {
    "prefix": "PowerPlantAlternatorACCompressorVibrationAnalysisReport",
    "text": "**PTAutoReport.PowerPlantAlternatorACCompressorVibrationAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.MufflerFrequencyResponseAnalysis": {
    "prefix": "MufflerFrequencyResponseAnalysis",
    "text": "**PTAutoReport.MufflerFrequencyResponseAnalysis**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.StaticStiffnessForMountBRKTReport": {
    "prefix": "StaticStiffnessForMountBRKTReport",
    "text": "**PTAutoReport.StaticStiffnessForMountBRKTReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.VibrationForStrainerBaffleReport": {
    "prefix": "VibrationForStrainerBaffleReport",
    "text": "**PTAutoReport.VibrationForStrainerBaffleReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.InitStressOfInclinedBoltsReport": {
    "prefix": "InitStressOfInclinedBoltsReport",
    "text": "**PTAutoReport.InitStressOfInclinedBoltsReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.ACOutletHoseBlockagePredictionReport": {
    "prefix": "ACOutletHoseBlockagePredictionReport",
    "text": "**PTAutoReport.ACOutletHoseBlockagePredictionReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.AirCleanerSurfaceStiffnessAnalysisReport": {
    "prefix": "AirCleanerSurfaceStiffnessAnalysisReport",
    "text": "**PTAutoReport.AirCleanerSurfaceStiffnessAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.PowerPlantExhaustSystemVibrationAnalysisReport": {
    "prefix": "PowerPlantExhaustSystemVibrationAnalysisReport",
    "text": "**PTAutoReport.PowerPlantExhaustSystemVibrationAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.SurfaceStiffnessAnalysisOfEnginePartsReport": {
    "prefix": "SurfaceStiffnessAnalysisOfEnginePartsReport",
    "text": "**PTAutoReport.SurfaceStiffnessAnalysisOfEnginePartsReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.MufHangerStrengthAndEigenValueReport": {
    "prefix": "MufHangerStrengthAndEigenValueReport",
    "text": "**PTAutoReport.MufHangerStrengthAndEigenValueReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.PistonSkirtRigidityReport": {
    "prefix": "PistonSkirtRigidityReport",
    "text": "**PTAutoReport.PistonSkirtRigidityReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.PistonHighTempHighCycleFatigueReport": {
    "prefix": "PistonHighTempHighCycleFatigueReport",
    "text": "**PTAutoReport.PistonHighTempHighCycleFatigueReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.StaticStiffnessForVehicleMountBRKTReport": {
    "prefix": "StaticStiffnessForVehicleMountBRKTReport",
    "text": "**PTAutoReport.StaticStiffnessForVehicleMountBRKTReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.FuelPipeStrengthVibrationAnalysisReport": {
    "prefix": "FuelPipeStrengthVibrationAnalysisReport",
    "text": "**PTAutoReport.FuelPipeStrengthVibrationAnalysisReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "PTAutoReport.CamshaftHighCycleFatigueReport": {
    "prefix": "CamshaftHighCycleFatigueReport",
    "text": "**PTAutoReport.CamshaftHighCycleFatigueReport**  \nPSJ command. See the reference for arguments and usage."
  },
  "ReportT.ReportToolOverall": {
    "prefix": "ReportToolOverall",
    "text": "**ReportT.ReportToolOverall**  \nPSJ command. See the reference for arguments and usage."
  },
  "Results.RightClick.Rename": {
    "prefix": "Rename",
    "text": "**Results.RightClick.Rename**  \nPSJ command. See the reference for arguments and usage."
  },
  "Results.RightClick.Delete": {
    "prefix": "Delete",
    "text": "**Results.RightClick.Delete**  \nPSJ command. See the reference for arguments and usage."
  },
  "Test.ReplaceSolidMesh": {
    "prefix": "ReplaceSolidMesh",
    "text": "**Test.ReplaceSolidMesh**  \nPSJ command. See the reference for arguments and usage."
  },
  "Tools.Coordinates.ImportCoordinate": {
    "prefix": "ImportCoordinate",
    "text": "**Tools.Coordinates.ImportCoordinate**  \nPSJ command. See the reference for arguments and usage."
  },
  "Tools.Coordinates.ExportCoordinate": {
    "prefix": "ExportCoordinate",
    "text": "**Tools.Coordinates.ExportCoordinate**  \nPSJ command. See the reference for arguments and usage."
  },
  "Tools.Measure.Distance.Plane3NodesToNode": {
    "prefix": "Plane3NodesToNode",
    "text": "**Tools.Measure.Distance.Plane3NodesToNode**  \nPSJ command. See the reference for arguments and usage."
  },
  "Tools.Measure.Force": {
    "prefix": "Force",
    "text": "**Tools.Measure.Force**  \nPSJ command. See the reference for arguments and usage."
  },
  "Tools.ToPre": {
    "prefix": "ToPre",
    "text": "**Tools.ToPre**  \nPSJ command. See the reference for arguments and usage."
  },
  "Tools.ToPost": {
    "prefix": "ToPost",
    "text": "**Tools.ToPost**  \nPSJ command. See the reference for arguments and usage."
  },
  "Tools.Property": {
    "prefix": "Property",
    "text": "**Tools.Property**  \nPSJ command. See the reference for arguments and usage."
  },
  "Tools.ContourCopy": {
    "prefix": "ContourCopy",
    "text": "**Tools.ContourCopy**  \nPSJ command. See the reference for arguments and usage."
  },
  "Tools.DraftAngleHideContour": {
    "prefix": "DraftAngleHideContour",
    "text": "**Tools.DraftAngleHideContour**  \nPSJ command. See the reference for arguments and usage."
  },
  "Utility.MeasureDistanceBy2Edges": {
    "prefix": "MeasureDistanceBy2Edges",
    "text": "**Utility.MeasureDistanceBy2Edges**  \nPSJ command. See the reference for arguments and usage."
  },
  "WatchData.Toolbar.DeleteAll": {
    "prefix": "DeleteAll",
    "text": "**WatchData.Toolbar.DeleteAll**  \nPSJ command. See the reference for arguments and usage."
  },
  "WatchSelected.Save": {
    "prefix": "Save",
    "text": "**WatchSelected.Save**  \nPSJ command. See the reference for arguments and usage."
  },
  "WebGL.ExportVTFxFile": {
    "prefix": "ExportVTFxFile",
    "text": "**WebGL.ExportVTFxFile**  \nPSJ command. See the reference for arguments and usage."
  },
  "WebGL.LogPostResultToFile": {
    "prefix": "LogPostResultToFile",
    "text": "**WebGL.LogPostResultToFile**  \nPSJ command. See the reference for arguments and usage."
  }
};

export type KeywordGroup = "python" | "psjUtility" | "psjGui" | "psjCommand";

export const keywordGroups: Record<KeywordGroup, string[]> = {
  "python": [
    "False",
    "None",
    "True",
    "__init__",
    "__main__",
    "abort",
    "and",
    "append",
    "argv",
    "array",
    "as",
    "assert",
    "async",
    "await",
    "bool",
    "break",
    "chdir",
    "class",
    "clear",
    "close",
    "continue",
    "copyfile",
    "count",
    "curdir",
    "date",
    "datetime",
    "def",
    "del",
    "elif",
    "else",
    "except",
    "exec",
    "extend",
    "finally",
    "find",
    "float",
    "for",
    "format",
    "from",
    "getcwd",
    "global",
    "groupby",
    "if",
    "import",
    "in",
    "insert",
    "int",
    "is",
    "itertools",
    "join",
    "lambda",
    "len",
    "lstrip",
    "math",
    "matplotlib",
    "mkdir",
    "move",
    "not",
    "numba",
    "numpy",
    "open",
    "or",
    "os",
    "pandas",
    "pass",
    "pipe",
    "pprint",
    "pptx",
    "print",
    "raise",
    "random",
    "range",
    "re",
    "remove",
    "rename",
    "replace",
    "return",
    "rmdir",
    "rstrip",
    "seek",
    "shutil",
    "sklearn",
    "sleep",
    "sort",
    "split",
    "statistics",
    "str",
    "strftime",
    "strip",
    "sys",
    "system",
    "tell",
    "today",
    "try",
    "values",
    "version",
    "while",
    "win32com",
    "with",
    "write",
    "yield"
  ],
  "psjUtility": [
    "ABAQSTEPS",
    "ABAQSTEPS_STRUCT",
    "ABAQSTEPS_STRUCT_COUPLEDTD",
    "ABAQSTEPS_STRUCT_DYNAMIC",
    "ABAQSTEPS_STRUCT_DYNAMIC_COUPLEDTD",
    "ABAQSTEPS_STRUCT_DYNAMIC_EXPLICIT",
    "ABAQSTEPS_STRUCT_FREQUENCY",
    "ABAQSTEPS_STRUCT_STATIC",
    "ABAQSTEPS_STRUCT_STATICRISK",
    "ABAQSTEPS_THERMAL",
    "ABAQSTEPS_THERMAL_SS",
    "ABAQSTEPS_THERMAL_TRANSIENT",
    "ABAQUSJOB",
    "ACTRANJOB",
    "ADVC2_POSTJOB",
    "ADVCJOB",
    "ADVCPROCESS",
    "ADVCPROCESS_CREEP",
    "ADVCPROCESS_DYNAMIC",
    "ADVCPROCESS_DYNAMIC_EXPLICIT",
    "ADVCPROCESS_EIGEN",
    "ADVCPROCESS_FATIGUE",
    "ADVCPROCESS_MODAL_FREQ_RESP",
    "ADVCPROCESS_RAND_RESP",
    "ADVCPROCESS_RESP_SPEC",
    "ADVCPROCESS_SSH",
    "ADVCPROCESS_STATIC",
    "ADVCPROCESS_TH",
    "ANSYSJOB",
    "APPDATA_PATH",
    "AS_BODY",
    "AS_CONNECTION",
    "AS_CONTACT",
    "AS_EDGE",
    "AS_ELEM",
    "AS_ELEM1D",
    "AS_FACE",
    "AS_GROUP",
    "AS_MASS",
    "AS_NODE",
    "AS_SOLIDELEM",
    "ATTRIBUTE_FXWELD",
    "ATTRIBUTE_PS_BLENDSURFACE",
    "Add1DElementSelector",
    "AddBarBodySelector",
    "AddBodySelector",
    "AddConditionSelector",
    "AddCoordinateSelector",
    "AddEdgePointSelector",
    "AddEdgeSelector",
    "AddElementEdgeSelector",
    "AddElementSelector",
    "AddFacePointSelector",
    "AddFaceSelector",
    "AddGroupSelector",
    "AddNodeSelector",
    "AddPyObserver",
    "AddSolidElementSelector",
    "AddVertexSelector",
    "Apply",
    "AssociateType",
    "BARBODY",
    "BEAM_PROP_ATTR",
    "BEAM_PROP_ATTR2",
    "BODY",
    "BODYLINK",
    "BeginDatabaseTransaction",
    "BodyVector",
    "BoolType",
    "CONNECTION_ELEMENT",
    "CONNECT_BUSH",
    "CONNECT_CONM",
    "CONNECT_CONNECTOR",
    "CONNECT_DAMPER",
    "CONNECT_GAP",
    "CONNECT_MOMENT",
    "CONNECT_MPC",
    "CONNECT_PROD",
    "CONNECT_RBAR",
    "CONNECT_RBE2",
    "CONNECT_RBE3",
    "CONNECT_SPRING",
    "CONNECT_WELD",
    "CONN_PROP_ATTR",
    "CONTACT",
    "CONTACT_ABAQUS",
    "CONTACT_ADVC",
    "CONTACT_ANSYS",
    "CONTACT_MSCNASTRAN",
    "CONTACT_NXNASTRAN",
    "CONTACT_TSSS",
    "COORD",
    "CUSTOM_ATTR_DOUBLE",
    "CUSTOM_ATTR_STRING",
    "CUSTOM_ATTR_VECTOR",
    "Cancel",
    "CastDItemToDBody",
    "CastDItemToDConnect",
    "CastDItemToDCoord",
    "CastDItemToDEdge",
    "CastDItemToDElem",
    "CastDItemToDFace",
    "CastDItemToDGroup",
    "CastDItemToDLoadBC",
    "CastDItemToDNode",
    "CastToDItem",
    "CheckLicense",
    "ClearAllSelection",
    "ClearLog",
    "ClearPreview",
    "ClearPyObserver",
    "ClearRedo",
    "ClearUndo",
    "CloseDocument",
    "CollapseAssemblyTree",
    "ConnectVector",
    "ConvertFromDocUnit",
    "ConvertFromMacroUnit",
    "ConvertJPTColorToRGB",
    "ConvertRGBToJPTColor",
    "ConvertValueToDocUnit",
    "ConvertValueToMacroUnit",
    "CoordVector",
    "CopyToClipBoard",
    "Create",
    "CreateNewDocument",
    "CreateSubAssembly",
    "DATABASE_PATH",
    "DBody",
    "DCS",
    "DConnect",
    "DCoord",
    "DEdge",
    "DElem",
    "DFace",
    "DGroup",
    "DItem",
    "DItemListToMacroListTCursor",
    "DItemPair",
    "DItemPairVector",
    "DItemToMacroListTCursor",
    "DItemToMacroTCursor",
    "DItemToMacroTCursorPair",
    "DItemType",
    "DItemVector",
    "DLoadBC",
    "DNode",
    "DOC_PATH",
    "DPostElem",
    "DPostNode",
    "DSolverJob",
    "DTABLE_ABAQSTEPS",
    "DTABLE_ABAQUSJOB",
    "DTABLE_ACTRANJOB",
    "DTABLE_ADVCJOB",
    "DTABLE_ADVCPROCESS",
    "DTABLE_ANSYSJOB",
    "DTABLE_BODY",
    "DTABLE_CONNECTION",
    "DTABLE_CONTACT",
    "DTABLE_COORDINATE",
    "DTABLE_CUSTOM_ATTRIBUTE",
    "DTABLE_DYNAMISJOB",
    "DTABLE_ELEM",
    "DTABLE_ELEMEDGE_GROUP",
    "DTABLE_FIELD_DATA",
    "DTABLE_GROUP",
    "DTABLE_LBC_DOFSET",
    "DTABLE_LBC_END",
    "DTABLE_LBC_START",
    "DTABLE_LOADCASE",
    "DTABLE_LOCAL_SETTING",
    "DTABLE_LSDYNAJOB",
    "DTABLE_MATERIAL",
    "DTABLE_NASTRANJOB",
    "DTABLE_NODE",
    "DTABLE_POSTJOB",
    "DTABLE_PROPERTY",
    "DTABLE_SECTION",
    "DTABLE_SHAPE",
    "DTABLE_SUP_GROUP",
    "DTABLE_UNKNOWN",
    "DTABLE_USER_RESULT",
    "DTVector3dToMacroVector",
    "DTableType",
    "DYANAMISJOB",
    "DeSelectArrayCursor",
    "Debugger",
    "DeleteSubAssembly",
    "DeleteSubAssemblyRecursively",
    "Destroy",
    "DisableMessageBox",
    "DisableOutputMessage",
    "DisableScreenAnimation",
    "DocInit",
    "DocNone",
    "DocPost",
    "DocPre",
    "Document",
    "DocumentType",
    "DocumentVector",
    "DoubleVector",
    "EDGE",
    "ELEM",
    "ELEMEDGE_GROUP",
    "ELEMKIND_0D",
    "ELEMKIND_1D",
    "ELEMKIND_2D",
    "ELEMKIND_3D",
    "ELEMKIND_SP",
    "ELEMKIND_UNKNOWN",
    "ELEMTYPE_HEX18",
    "ELEMTYPE_HEX20",
    "ELEMTYPE_HEX8",
    "ELEMTYPE_LINE2",
    "ELEMTYPE_LINE3",
    "ELEMTYPE_MASS",
    "ELEMTYPE_PLOT",
    "ELEMTYPE_POINT",
    "ELEMTYPE_PRISM12",
    "ELEMTYPE_PRISM15",
    "ELEMTYPE_PRISM6",
    "ELEMTYPE_PYRAMID13",
    "ELEMTYPE_PYRAMID5",
    "ELEMTYPE_QUAD4",
    "ELEMTYPE_QUAD6",
    "ELEMTYPE_QUAD8",
    "ELEMTYPE_QUAD9",
    "ELEMTYPE_RBE",
    "ELEMTYPE_TET10",
    "ELEMTYPE_TET4",
    "ELEMTYPE_TRI3",
    "ELEMTYPE_TRI6",
    "ELEMTYPE_UNKNOWN",
    "ELEMTYPE_VIRTUAL",
    "END",
    "ENTITY_ATTR_CAD_INFO",
    "EdgeVector",
    "ElemKind",
    "ElemType",
    "ElemVector",
    "EnableLicenseFeature",
    "EnableMessageBox",
    "EnableOutputMessage",
    "EnableScreenAnimation",
    "EndDatabaseTransaction",
    "EntityType",
    "Exec",
    "ExpandAssemblyTree",
    "FACE",
    "FALSE_VAL",
    "FEM_FIELD_SCALAR",
    "FEM_FIELD_TENSOR",
    "FEM_FIELD_VECTOR",
    "FILE_PATH",
    "FRONTISTRJOB",
    "FaceVector",
    "FindSubAssemblyByID",
    "FindSubAssemblyByName",
    "GROUP",
    "GetActiveDocument",
    "GetActivePostJob",
    "GetAllByTableTypeID",
    "GetAllByTypeID",
    "GetAllConnections",
    "GetAllCoordinates",
    "GetAllEdges",
    "GetAllElems",
    "GetAllFaces",
    "GetAllGroups",
    "GetAllLoadBoundaryConditions",
    "GetAllLoadsBCs",
    "GetAllNodes",
    "GetAllParts",
    "GetAllPartsInSubAssembly",
    "GetAllSelected",
    "GetAllSolverJobs",
    "GetAppPathInfo",
    "GetAssemblyEntityData",
    "GetAssemblyItems",
    "GetAvailableResultOption",
    "GetCenterOfEntities",
    "GetContactType",
    "GetCountByType",
    "GetCurrentDocumentPath",
    "GetDefaultResultOption",
    "GetDocumentByID",
    "GetDocumentList",
    "GetElemsByKind",
    "GetElemsByType",
    "GetEntitiesByAdjacent",
    "GetEntitiesByAssociation",
    "GetEntitiesByID",
    "GetEntitiesByName",
    "GetEntitiesByPosition",
    "GetGroupFromSubGroup",
    "GetJPTTempPath",
    "GetLastCreatedCursor",
    "GetMacroLog",
    "GetMaterialFromProperty",
    "GetMaxIDEntity",
    "GetMaxResultCoord",
    "GetMaxResultId",
    "GetMaxResultValue",
    "GetMinIDEntity",
    "GetMinResultCoord",
    "GetMinResultId",
    "GetMinResultValue",
    "GetOpnList",
    "GetPostElemFromPosition",
    "GetProgramPath",
    "GetProgramVersion",
    "GetPythonAPILog",
    "GetRandomJPTColor",
    "GetRedoCount",
    "GetResultComponentNames",
    "GetResultIncrements",
    "GetResultLocations",
    "GetResultNames",
    "GetResultSetName",
    "GetResultSteps",
    "GetResultTimeStepInfo",
    "GetResultUseIncrement",
    "GetSelectedEdges",
    "GetSelectedEdgesCr",
    "GetSelectedElemEdges",
    "GetSelectedElems",
    "GetSelectedElemsCr",
    "GetSelectedFaces",
    "GetSelectedFacesCr",
    "GetSelectedGroups",
    "GetSelectedGroupsCr",
    "GetSelectedNodes",
    "GetSelectedNodesCr",
    "GetSelectedParts",
    "GetSelectedPartsCr",
    "GetSharedElements",
    "GetSharedFaces",
    "GetSharedNodes",
    "GetSuppressedParts",
    "GetThicknessOfEntity",
    "GetTimeStepInfoName",
    "GetUndoCount",
    "GroupVector",
    "Hide",
    "HidePreview",
    "IDE_DATA_PATH",
    "INST",
    "IntPair",
    "IntPairVector",
    "IntVector",
    "InverseHideBodies",
    "IsDefaultDouble",
    "IsDefaultInt",
    "JPT",
    "JPT_ACMODEL",
    "JPT_ANABQ",
    "JPT_ANACT",
    "JPT_ANADV",
    "JPT_ANDMS",
    "JPT_ANFIS",
    "JPT_ANLSD",
    "JPT_ANMAR",
    "JPT_ANNAS",
    "JPT_ANOPT",
    "JPT_ANPMS",
    "JPT_ANSYS",
    "JPT_ANTSS",
    "JPT_ANUNIV",
    "JPT_ASSY",
    "JPT_BASE",
    "JPT_CAACS_EL",
    "JPT_CAACS_SP",
    "JPT_CAIDI",
    "JPT_CAIGS_EL",
    "JPT_CAIGS_SP",
    "JPT_CAJT_EL",
    "JPT_CANXD_SP",
    "JPT_CAPAR",
    "JPT_CAPAR_SP",
    "JPT_CAPRO",
    "JPT_CAPRO_SP",
    "JPT_CASTP_EL",
    "JPT_CASTP_SP",
    "JPT_CATIA_EL",
    "JPT_CATIA_SP",
    "JPT_CZASW",
    "JPT_CZCAMMC",
    "JPT_CZDJM",
    "JPT_CZDLAJ",
    "JPT_CZDMMMC",
    "JPT_CZFXW",
    "JPT_CZGGR",
    "JPT_CZHCIK",
    "JPT_CZHGA",
    "JPT_CZJBF",
    "JPT_CZMEM",
    "JPT_CZMFH",
    "JPT_CZMFHA",
    "JPT_CZMFM",
    "JPT_CZMFS",
    "JPT_CZMFT",
    "JPT_CZNPD",
    "JPT_CZOASAW",
    "JPT_CZSOP",
    "JPT_CZSSTRNFT",
    "JPT_CZSZM",
    "JPT_CZTOPOSHL",
    "JPT_CZWMHZ",
    "JPT_CZYME",
    "JPT_DESIGNER",
    "JPT_DESIGNER_LIMITED",
    "JPT_DYNAMIS",
    "JPT_HOME",
    "JPT_MIDP",
    "JPT_NMRI",
    "JPT_PARASOLID",
    "JPT_PSTUNI",
    "JPT_SPACM",
    "JPT_SPANA",
    "JPT_SPANAF",
    "JPT_SPANAR",
    "JPT_SPANAS",
    "JPT_SPAPIPR",
    "JPT_SPBKL",
    "JPT_SPCARRIER",
    "JPT_SPCAT",
    "JPT_SPCNW",
    "JPT_SPCRACK",
    "JPT_SPDLSA",
    "JPT_SPDLSAPR",
    "JPT_SPENGNWA",
    "JPT_SPGRRM",
    "JPT_SPMFG",
    "JPT_SPMIDPSHIP",
    "JPT_SPMSPOT",
    "JPT_SPMWELD",
    "JPT_SPNM3DL",
    "JPT_SPNMRIC",
    "JPT_SPNMRIW",
    "JPT_SPNMWL",
    "JPT_SPOAS",
    "JPT_SPOAS2",
    "JPT_SPOPF",
    "JPT_SPOPM",
    "JPT_SPPMS",
    "JPT_SPPRR",
    "JPT_SPSCREW",
    "JPT_SPSMF",
    "JPT_SPSMFS",
    "JPT_SPTSM",
    "JPT_SPWEB",
    "JPT_SPWLD",
    "JPT_SUZUKI",
    "JPT_TEST",
    "JPT_UNLIM",
    "LBC_CONCENTRATE_FLUX",
    "LBC_CONSTRAINT",
    "LBC_CONTACT_CLEARANCE",
    "LBC_CS_CENTRIFUGAL_FORCE",
    "LBC_DOFSET",
    "LBC_DYNAMIC_INITIAL_CONDITION",
    "LBC_ENFORCED_ACCELERATION",
    "LBC_ENFORCED_DISP",
    "LBC_ENFORCED_VELOCITY",
    "LBC_FORCE",
    "LBC_FORCE_ND",
    "LBC_FORCE_QUADRATIC",
    "LBC_FORCE_SINE",
    "LBC_FORCE_VECTOR",
    "LBC_GRAVITY",
    "LBC_G_PRESSURE",
    "LBC_H_PRESSURE",
    "LBC_INITSTRESS_GENERAL",
    "LBC_INITSTRESS_MAPPING",
    "LBC_INIT_ANGULAR_VEL_ABAQUS",
    "LBC_INSIDE_HEAT_GENERATION",
    "LBC_MAPPING_FORCE",
    "LBC_MAPPING_FORCEDDISPLACEMENT",
    "LBC_MAPPING_FORCED_TEMP",
    "LBC_MAPPING_HEATFLUX",
    "LBC_MAPPING_PRESSURE",
    "LBC_MAPPING_TEMP_BOUNDARY",
    "LBC_MAPPING_TEMP_INIT",
    "LBC_MAPPING_TEMP_LOAD",
    "LBC_MAPPING_TEMP_MARINE_ENGINE",
    "LBC_MAPPING_THERMAL_CONVECTION",
    "LBC_NOLIN1",
    "LBC_NOLIN3",
    "LBC_NOLIN4",
    "LBC_PRESSURE_QUADRATIC",
    "LBC_PRESSURE_SINE",
    "LBC_PRETENSION",
    "LBC_PRETENSION_ABAQUS",
    "LBC_PRETENSION_NXN",
    "LBC_RIGIDWALL",
    "LBC_SUBMODEL_FORCED_DISP",
    "LBC_SUBMODEL_FORCED_FLUX",
    "LBC_SUBMODEL_FORCED_TEMP",
    "LBC_SURFACE_FLUX",
    "LBC_SURFACE_LOADS",
    "LBC_TEMP_BOUNDARY",
    "LBC_TEMP_INI",
    "LBC_TEMP_LOAD",
    "LBC_TEMP_LOAD_ADVC_FILE",
    "LBC_TEMP_LOAD_ADVC_RESULT_REFERENCE",
    "LBC_TEMP_LOAD_GENERAL",
    "LBC_TEMP_LOAD_NASTRAN",
    "LBC_THERMAL_CONVECTION",
    "LBC_T_CENTRIFUGAL_FORCE",
    "LBC_T_PRESSURE",
    "LBC_WELD",
    "LOADCASE",
    "LOCAL_SETTING",
    "LSDYNAJOB",
    "ListDoubleToMacroVector",
    "LoadBCVector",
    "MARCJOB",
    "MATERIAL",
    "MATERIAL_LIB_FILE_PATH",
    "MATERIAL_USER_FILE_PATH",
    "MB_INFORMATION_OK",
    "MB_INFORMATION_OKCANCEL",
    "MB_INFORMATION_YESNO",
    "MB_INFORMATION_YESNOCANCEL",
    "MB_OPTION_CANCEL",
    "MB_OPTION_NO",
    "MB_OPTION_OK",
    "MB_OPTION_YES",
    "MB_WARNING_OK",
    "MB_WARNING_OKCANCEL",
    "MB_WARNING_YESNO",
    "MB_WARNING_YESNOCANCEL",
    "MacroListTCursorPairToListDItemPair",
    "MacroListTCursorToListDItem",
    "MacroResultParser",
    "MacroTCursorPairToDItemPair",
    "MacroTCursorToDItem",
    "MessageBoxPSJ",
    "MsgBoxOptionType",
    "MsgBoxType",
    "MsgOut",
    "NASTRANJOB",
    "NASTRAN_POSTJOB",
    "NCS",
    "NODE",
    "NodeVector",
    "Notify",
    "OPTISHAPE_TS_JOB",
    "PERMASJOB",
    "POST_AMT_COMPLEX",
    "POST_AMT_PLOT",
    "POST_AMT_SCALAR",
    "POST_AMT_SCALAR_TENSOR",
    "POST_AMT_SCALAR_TENSOR_2D",
    "POST_AMT_TENSOR",
    "POST_AMT_TENSOR_2D",
    "POST_AMT_UNKNOWN",
    "POST_AMT_VECTOR_DIR",
    "POST_AMT_VECTOR_TEN",
    "POST_ANALYSIS_BUCKLING",
    "POST_ANALYSIS_COMPLEX_MODAL",
    "POST_ANALYSIS_FREQUENCY",
    "POST_ANALYSIS_HEAT_TRANSFER",
    "POST_ANALYSIS_LINEAR_STATIC",
    "POST_ANALYSIS_MODAL",
    "POST_ANALYSIS_NONLINEAR",
    "POST_ANALYSIS_STEADYT_HEAT_CONDUCTION",
    "POST_ANALYSIS_TRANSIENT",
    "POST_ANALYSIS_UNKNOWN",
    "POST_ANALYSIS_USER_DEFINED",
    "POST_CNV_ALL",
    "POST_CNV_AVG",
    "POST_CNV_AVG_MATERIAL",
    "POST_CNV_COMP_AVG",
    "POST_CNV_MAX",
    "POST_CNV_MAX_MIN",
    "POST_CNV_MIN",
    "POST_CNV_UNKNOWN",
    "POST_COMPLEX_AMP",
    "POST_COMPLEX_AMP_AND_PHASE",
    "POST_COMPLEX_IMG",
    "POST_COMPLEX_PHASE",
    "POST_COMPLEX_PHASE_ANGLE",
    "POST_COMPLEX_REAL",
    "POST_COMPLEX_UNKNOWN",
    "POST_CONT_ALL",
    "POST_CONT_BLK",
    "POST_CONT_MAT",
    "POST_CONT_PROP",
    "POST_CONT_UNKNOWN",
    "POST_COORD_ANALYSIS",
    "POST_COORD_ELEMENT",
    "POST_COORD_GLOBAL",
    "POST_COORD_UNKNOWN",
    "POST_COORD_USER",
    "POST_LOAD1D_ALL",
    "POST_LOAD1D_EXTREME",
    "POST_LOAD1D_MAX",
    "POST_LOAD1D_MIN",
    "POST_LOAD1D_NG",
    "POST_LOAD1D_PT_1",
    "POST_LOAD1D_PT_2",
    "POST_LOAD1D_PT_3",
    "POST_LOAD1D_PT_4",
    "POST_LOAD1D_UNKNOWN",
    "POST_LOAD2D_BOTH",
    "POST_LOAD2D_BOTTOM",
    "POST_LOAD2D_EXTREME",
    "POST_LOAD2D_MAX",
    "POST_LOAD2D_MIN",
    "POST_LOAD2D_TOP",
    "POST_LOAD2D_UNKNOWN",
    "POST_LOC_ON_ELEMENT",
    "POST_LOC_ON_ELEMENT_NODE",
    "POST_LOC_ON_INTEGRATION_POINT",
    "POST_LOC_ON_NODE",
    "POST_LOC_UNKNOWN",
    "PROGRAM_PATH",
    "PROJECT",
    "PROPERTY_0D_MASS",
    "PROPERTY_1D_BAR",
    "PROPERTY_1D_BEAM",
    "PROPERTY_1D_PLOT",
    "PROPERTY_1D_ROD",
    "PROPERTY_2D_COMPOSITE_SHELL",
    "PROPERTY_2D_SHELL",
    "PROPERTY_3D_COHESIVE",
    "PROPERTY_3D_GASKET",
    "PROPERTY_3D_SOLID",
    "PROPERTY_3D_WELDBEAD",
    "PY_DOCUMENT_SWITCHED",
    "PY_MACRO_ADDED",
    "PathType",
    "PostAnalysisType",
    "PostDataOp",
    "PostResultDataAmt",
    "PostResultDataCnv",
    "PostResultDataComplex",
    "PostResultDataCont",
    "PostResultDataCoord",
    "PostResultDataLoad1D",
    "PostResultDataLoad2D",
    "PostResultDataLoc",
    "PostResultKey",
    "PostTimeStepInfo",
    "PreviewBCForceGeneral",
    "PreviewBCForceNormal",
    "PreviewBCPressureGeneral",
    "PreviewMirror",
    "PreviewRotate",
    "PreviewScaling",
    "PreviewTranslation",
    "PrintAppPathInfo",
    "PrintPSJUtilityManual",
    "PushDlgButton",
    "PyNotificationType",
    "QuitApplication",
    "REF_BODY",
    "REF_BODYLINK",
    "REF_EDGE",
    "REF_ELEM",
    "REF_FACE",
    "REF_NODE",
    "REF_SHAPELINK",
    "REF_SOLID",
    "REF_VERTEX",
    "RemoveAllAbaqusStep",
    "RemoveAllByTableType",
    "RemoveAllConnections",
    "RemoveAllContacts",
    "RemoveAllCoordinates",
    "RemoveAllFieldTables",
    "RemoveAllLoadCases",
    "RemoveAllLoadsBCs",
    "RemoveAllMaterials",
    "RemoveAllMeshSettings",
    "RemoveAllSolverjob",
    "RemoveEntitiesByID",
    "RemoveEntitiesByName",
    "RemovePyObserver",
    "RemoveWSProperties",
    "SECTION_GENERAL",
    "SECTION_LIBRARY",
    "SECTION_SKETCHER",
    "SELMTD_BAR_BODY",
    "SELMTD_BODY",
    "SELMTD_CONDITION",
    "SELMTD_CONDITION_CONNECTOR",
    "SELMTD_CONDITION_CONSTRAIN",
    "SELMTD_CONDITION_ENFORCE",
    "SELMTD_CONDITION_FORCE",
    "SELMTD_CONDITION_MASS",
    "SELMTD_CONDITION_MPC",
    "SELMTD_CONDITION_PRESSURE",
    "SELMTD_CONDITION_RBAR",
    "SELMTD_CONDITION_RBE2",
    "SELMTD_CONDITION_RBE3",
    "SELMTD_CONDITION_SPRING",
    "SELMTD_CONDITION_TEMP",
    "SELMTD_COORDINATE",
    "SELMTD_EDGE",
    "SELMTD_EDGE_POINT",
    "SELMTD_ELEM",
    "SELMTD_ELEM1D",
    "SELMTD_ELEM_EDGE",
    "SELMTD_FACE",
    "SELMTD_FACE_POINT",
    "SELMTD_GROUP",
    "SELMTD_NODE",
    "SELMTD_NONE",
    "SELMTD_PROPERTY",
    "SELMTD_SHELL_QUAD4",
    "SELMTD_SHELL_QUAD8",
    "SELMTD_SHELL_TRI3",
    "SELMTD_SHELL_TRI6",
    "SELMTD_SOLIDELEM",
    "SELMTD_SOLID_HEX20",
    "SELMTD_SOLID_HEX8",
    "SELMTD_SOLID_PEN15",
    "SELMTD_SOLID_PENT6",
    "SELMTD_SOLID_PYR13",
    "SELMTD_SOLID_PYRD5",
    "SELMTD_SOLID_TET10",
    "SELMTD_SOLID_TET4",
    "SELMTD_VERTEX",
    "SELMTD_VIEW_ITEM",
    "SHAPELINK",
    "SHELL_PROP_ATTR",
    "SOLID",
    "SUNSHINE_PATH",
    "SUP_GROUP",
    "SelectArrayCursor",
    "SelectDlgComboBox",
    "SelectMethodType",
    "SelectionByID",
    "SelectionByType",
    "SelectionListDlg",
    "SetActiveDocument",
    "SetDlgText",
    "SetSelectMethod",
    "Show",
    "ShowHideAllParts",
    "ShowHideEntitiesByID",
    "ShowPreview",
    "StartSunShine",
    "StringVector",
    "TEMP_PATH",
    "TRUE_VAL",
    "TVector3d",
    "UNKNOWN",
    "USER_PROP",
    "UnitType",
    "Unit_Acceleration",
    "Unit_Angle",
    "Unit_Area",
    "Unit_AreaMomentInertia",
    "Unit_ConvectionCoef",
    "Unit_DampingCoef",
    "Unit_Density",
    "Unit_ElectricalResistivity",
    "Unit_Energy",
    "Unit_Force",
    "Unit_Frequency",
    "Unit_HeatFlux",
    "Unit_HeatGeneration",
    "Unit_Length",
    "Unit_LinearDensity",
    "Unit_LinearMassMomentIntertia",
    "Unit_Mass",
    "Unit_Modulus",
    "Unit_Moment",
    "Unit_MomentInertia",
    "Unit_Power",
    "Unit_Pressure",
    "Unit_RotateAcc",
    "Unit_RotateDampingCoef",
    "Unit_RotateStiff",
    "Unit_RotateVelo",
    "Unit_SpecificHeat",
    "Unit_Stiffness",
    "Unit_Strain",
    "Unit_StrainEnergy",
    "Unit_Stress",
    "Unit_SurfaceDensity",
    "Unit_Temperature",
    "Unit_ThermalConductivity",
    "Unit_ThermalEnergy",
    "Unit_ThermalExCoef",
    "Unit_Time",
    "Unit_TorsionalConst",
    "Unit_Velocity",
    "Unit_Volume",
    "Unit_VolumeEnergyDensity",
    "Unit_WarpCoef",
    "UpdateCheckboxAssembly",
    "UpdateCheckboxWatchSelected",
    "UpdateSelectors",
    "VERTEX",
    "VersionInfo",
    "ViewFitToModel",
    "WELDORDER",
    "addObj",
    "area",
    "build",
    "children",
    "clearVec",
    "color",
    "colorMesh",
    "connectCoord",
    "connectElem",
    "connectMethod",
    "connectNode",
    "connections",
    "contacts",
    "convertXmlFileToDict",
    "convertXmlStringToDict",
    "coordPoints",
    "coordType",
    "deleteObj",
    "docID",
    "docName",
    "docPath",
    "docType",
    "dwg",
    "edges",
    "elems",
    "extendVec",
    "faces",
    "firstDItem",
    "gravityCenter",
    "id",
    "info",
    "isContainObj",
    "isFloating",
    "isValid",
    "jobDescription",
    "jobSteps",
    "jpt",
    "key",
    "kind",
    "lbcAnalysisType",
    "lbcCoord",
    "loadAndBCs",
    "localMeshSettings",
    "major",
    "mass",
    "masters",
    "materials",
    "minor",
    "momentInertia",
    "name",
    "nodes",
    "parent",
    "pos",
    "properties",
    "references",
    "secondDItem",
    "sizeVec",
    "slaves",
    "sub",
    "tableID",
    "targets",
    "transparency",
    "type",
    "typeID",
    "vertex",
    "volume",
    "x",
    "y",
    "z"
  ],
  "psjGui": [
    "JDGCreator",
    "add_1delement_selector",
    "add_2delement_selector",
    "add_3delement_selector",
    "add_barpart_selector",
    "add_browser",
    "add_button",
    "add_checkbox",
    "add_combobox",
    "add_combobox_option",
    "add_condition_selector",
    "add_coordinate_selector",
    "add_edge_selector",
    "add_elementedge_selector",
    "add_face_selector",
    "add_group_selector",
    "add_groupbox",
    "add_hlayout",
    "add_imagectrl",
    "add_label",
    "add_layout",
    "add_listbox",
    "add_listbox_option",
    "add_node_selector",
    "add_pageitem",
    "add_pagesctrl",
    "add_pagesctrl_page",
    "add_part_selector",
    "add_radiobutton",
    "add_richeditbox",
    "add_separator",
    "add_slider",
    "add_space",
    "add_spin",
    "add_table",
    "add_table_right_menu",
    "add_tabwnd",
    "add_tabwnd_page",
    "add_textbox",
    "add_vertex_selector",
    "add_vlayout",
    "disable_item",
    "dlg",
    "do_modal",
    "enable_item",
    "generate_window",
    "get_cell_value",
    "get_combobox_option",
    "get_combobox_sel",
    "get_item_text",
    "get_len_combobox",
    "get_len_listbox",
    "get_listbox_option",
    "get_listbox_sel",
    "get_margin",
    "get_option_text",
    "get_orientation",
    "get_selected_entities",
    "get_selector_name",
    "get_selector_type",
    "get_table_column_width",
    "get_table_sel_cell",
    "get_tabwnd_current_page",
    "get_total_column",
    "get_total_row",
    "hide_layout",
    "insert_combobox_option",
    "insert_combobox_options",
    "insert_listbox_option",
    "insert_listbox_options",
    "isbutton_checked",
    "iscollapsed",
    "isoption_checked",
    "on_active_tab_page",
    "on_command",
    "on_selected",
    "on_table_right_menu",
    "on_table_sel_changed",
    "pyjdg",
    "set_cell_value",
    "set_checkbox_state",
    "set_column_setting",
    "set_combobox_sel",
    "set_combobox_state",
    "set_groupbox_checked",
    "set_groupbox_collapsed",
    "set_groupbox_orientation",
    "set_icon_file",
    "set_image_file",
    "set_item_text",
    "set_listbox_sel",
    "set_margin",
    "set_option_state",
    "set_option_text",
    "set_orientation",
    "set_pagesctrl_current_page",
    "set_popup_menu",
    "set_radiobutton_state",
    "set_slider_bothtics",
    "set_slider_show_border",
    "set_slider_show_tics",
    "set_slider_vertical",
    "set_table_cell_fill_color",
    "set_table_cell_text_color",
    "set_table_column_width",
    "set_tabwnd_current_page",
    "show_layout",
    "show_tooltip"
  ],
  "psjCommand": []
};
