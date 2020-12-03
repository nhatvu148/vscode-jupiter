class ACModeling_ACBoundary:
    def FirstMethod(self, crlPart, bIsMergePart, bIsRenumber):
        message = "ACModeling.ACBoundary.FirstMethod({},{},{})".format(crlPart, bIsMergePart, bIsRenumber)
        return JPT_RUN_LINE(message)

class ACModeling_Create:
    def Convex(self, crlPart=[], dMeshSize=0.005, dOffset=0.02, dRadius=0.02, iDAxisGround=0, dScale=0.001):
        message = "ACModeling.Create.Convex({},{},{},{},{},{})".format(crlPart, dMeshSize, dOffset, dRadius, iDAxisGround, dScale)
        return JPT_RUN_LINE(message)

class ADVC_MakeProcess:
    def Static(self, strName, iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), dStabilizationFactor=0.0, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[]):
        message = "Analysis.ADVC.MakeProcess.Static('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def Creep(self, strName, iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), dStabilizationFactor=DFLT_DBL, bThetaDefined=False, dTheta=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[]):
        message = "Analysis.ADVC.MakeProcess.Creep('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, bThetaDefined, dTheta, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def Dynamic(self, strName, iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), bDynamic=False, advcDynamic=ADVC_DYNAMIC(), crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[]):
        message = "Analysis.ADVC.MakeProcess.Dynamic('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, bDynamic, advcDynamic, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def EigenValue(self, strName, bEigenValue=False, iNumberOfModes=0, iEigenvecNorm=10, dShift=DFLT_DBL, dCgcgpiTol=DFLT_DBL, dCgcgpiEigTol=DFLT_DBL, iCgcgpiLoopMax=DFLT_INT, dCgcgpiInnerTol=DFLT_DBL, iCgcgpiBlockSize=DFLT_INT, iCgcgpiExtraMode=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[]):
        message = "Analysis.ADVC.MakeProcess.EigenValue('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, bEigenValue, iNumberOfModes, iEigenvecNorm, dShift, dCgcgpiTol, dCgcgpiEigTol, iCgcgpiLoopMax, dCgcgpiInnerTol, iCgcgpiBlockSize, iCgcgpiExtraMode, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def DynamicExplicit(self, strName, iGeomNonlinear=0, advcStructTimeStep=ADVC_STRUCT_TIME_STEP(), bConvergence=False, advcConvergence=ADVC_CONVERGENCE(), bContact=False, advcContactIter=ADVC_CONTACT_ITER(), bAutoIncrement=False, advcAutoIncrement=ADVC_AUTO_INCREMENT(), iLogMessageInterval=DFLT_INT, iLinearApproximation=-1, dBulkViscosityCoef1=DFLT_DBL, dBulkViscosityCoef2=DFLT_DBL, dMassScalingdt=DFLT_DBL, dDtScaleFactor=DFLT_DBL, dPenaltyScaleFactor=DFLT_DBL, iContactSearchInterval=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[]):
        message = "Analysis.ADVC.MakeProcess.DynamicExplicit('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, iLogMessageInterval, iLinearApproximation, dBulkViscosityCoef1, dBulkViscosityCoef2, dMassScalingdt, dDtScaleFactor, dPenaltyScaleFactor, iContactSearchInterval, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def ModalFreqResp(self, strName, strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT_DBL, dMinFreq=DFLT_DBL, iNumFreqPoint=DFLT_INT, dBiasParam=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[]):
        message = "Analysis.ADVC.MakeProcess.ModalFreqResp('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def ResponseSpectrum(self, strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, iPropMethod=0, iSpttype=0, dSptFactor0=DFLT_DBL, crSpt0=None, dSptFactor1=DFLT_DBL, crSpt1=None, dSptFactor2=DFLT_DBL, crSpt2=None, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=0, strRefPath="", listAdvcRefStressResult=[]):
        message = "Analysis.ADVC.MakeProcess.ResponseSpectrum('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, iPropMethod, iSpttype, dSptFactor0, crSpt0, dSptFactor1, crSpt1, dSptFactor2, crSpt2, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def SteadyState(self, strName="", iEndType=1, dMaxTime=1, iFixedOrAuto=0, dMaxChange=DFLT_DBL, dInitDt=DFLT_DBL, iDefineMaxDt=0, dMaxDt=DFLT_DBL, iDefineMinDt=0, dMinDt=DFLT_DBL, dFixedDt=DFLT_DBL, iOutputLast=-1, iOutputInterval=DFLT_INT, iRestartLast=-1, iRestartInterval=DFLT_INT, dOutputTimeInterval=DFLT_DBL, dRestartTimeInterval=DFLT_DBL, iOutputInit=-1, iListOutputInterval=DFLT_INT, bConvergence=False, dCgTol=DFLT_DBL, dCgNrTol=DFLT_DBL, dCgDispTol=DFLT_DBL, dCgNrDispTol=DFLT_DBL, dCgDispLimitTol=DFLT_DBL, dCgTotalDispLimitTol=DFLT_DBL, dNewtonTol=DFLT_DBL, dNewtonDispTol=DFLT_DBL, dNewtonDispLimitTol=DFLT_DBL, dNewtonTotalDispLimitTol=DFLT_DBL, iCgloopMax=DFLT_INT, iNewtonMax=DFLT_INT, dHtNlLoopTol=DFLT_DBL, iHtNlLoopMax=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[]):
        message = "Analysis.ADVC.MakeProcess.SteadyState('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iEndType, dMaxTime, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList)
        return JPT_RUN_LINE(message)

    def Transient(self, strName="", iEndType=1, dMaxTime=1, dSteadyRate=0.0, iFixedOrAuto=0, dMaxChange=DFLT_DBL, dInitDt=DFLT_DBL, iDefineMaxDt=0, dMaxDt=DFLT_DBL, iDefineMinDt=0, dMinDt=DFLT_DBL, dFixedDt=DFLT_DBL, iOutputLast=-1, iOutputInterval=DFLT_INT, iRestartLast=-1, iRestartInterval=DFLT_INT, dOutputTimeInterval=DFLT_DBL, dRestartTimeInterval=DFLT_DBL, iOutputInit=-1, iListOutputInterval=DFLT_INT, bConvergence=False, dCgTol=DFLT_DBL, dCgNrTol=DFLT_DBL, dCgDispTol=DFLT_DBL, dCgNrDispTol=DFLT_DBL, dCgDispLimitTol=DFLT_DBL, dCgTotalDispLimitTol=DFLT_DBL, dNewtonTol=DFLT_DBL, dNewtonDispTol=DFLT_DBL, dNewtonDispLimitTol=DFLT_DBL, dNewtonTotalDispLimitTol=DFLT_DBL, iCgloopMax=DFLT_INT, iNewtonMax=DFLT_INT, dHtNlLoopTol=DFLT_DBL, iHtNlLoopMax=DFLT_INT, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[]):
        message = "Analysis.ADVC.MakeProcess.Transient('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iEndType, dMaxTime, dSteadyRate, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList)
        return JPT_RUN_LINE(message)

    def Fatigue(self, strName="", bFatigue=False, iMethod=0, iStressAxis=0, iSafetyType=0, dSearchResolution=DFLT_DBL, dSafetyMax=DFLT_DBL, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[]):
        message = "Analysis.ADVC.MakeProcess.Fatigue('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, bFatigue, iMethod, iStressAxis, iSafetyType, dSearchResolution, dSafetyMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def RandomResponse(self, strName="", strRefEigenDir="", dRefLowFreq=DFLT_DBL, dRefHighFreq=DFLT_DBL, crModalDampingRatio=None, crExcitationFreq=None, bAutoFreqInterval=False, dMaxFreq=DFLT_DBL, dMinFreq=DFLT_DBL, iNumFreqPoint=DFLT_INT, dBiasParam=DFLT_DBL, iPropMethod=0, iPSDtype=-1, iPSDdir=0, crPSDLoad=None, dPSDFactor=DFLT_DBL, dGravityAccel=DFLT_DBL, iOutputEigenFreqStep=-1, crEdit=None, listLoadNode=[], listLoadCaseNode=[], listLoadNodeContact=[], ilOutputParamList=[], iRefType=-1, strRefPath="", listAdvcRefStressResult=[]):
        message = "Analysis.ADVC.MakeProcess.RandomResponse('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, iPropMethod, iPSDtype, iPSDdir, crPSDLoad, dPSDFactor, dGravityAccel, iOutputEigenFreqStep, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class Analysis_AbaqusStep:
    def DynamicStep(self, abaqusDynamic=ABAQUS_DYNAMIC(), crEdit=None):
        message = "Analysis.AbaqusStep.DynamicStep({},{})".format(abaqusDynamic, crEdit)
        return JPT_RUN_LINE(message)

    def TransientStep(self, strName="", strDesp="", iEnableAutomatic=0, iMaxInc=0, dInitSize=DFLT_DBL, dMinSize=DFLT_DBL, dMaxSize=DFLT_DBL, dMaxAllowTChange=DFLT_DBL, iEndsteptBchecked=0, dlEndsteptTlist=[], dMaxAllowEmissivityChange=DFLT_DBL, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=0, dAdjustFactor=DFLT_DBL, iMaxContactIter=0, iEnableNlgeom=0, dTimePeriod=DFLT_DBL, iConvertDscntIter=0, iRamp=0, iExtrapolateMethod=0, listAbaqusOutputRequest=[], crEdit=None):
        message = "Analysis.AbaqusStep.TransientStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iEnableAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, dMaxAllowTChange, iEndsteptBchecked, dlEndsteptTlist, dMaxAllowEmissivityChange, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, dAdjustFactor, iMaxContactIter, iEnableNlgeom, dTimePeriod, iConvertDscntIter, iRamp, iExtrapolateMethod, listAbaqusOutputRequest, crEdit)
        return JPT_RUN_LINE(message)

    def CoupledTDStep(self, strName, strDesp="", iEnableAutomatic=0, iMaxInc=100, dInitSize=1.0, dMinSize=1.0e-5, dMaxSize=1.0, abaqusPair1=ABAQUS_PAIR(), abaqusPair2=ABAQUS_PAIR(), iCSVIntegration=0, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=8, dAdjustFactor=1.0, iMaxContactIter=30, iType=0, iEnableUseAdaptive=1, dDampingfactor=0.0002, dMaxRationofStrainEnergy=0.05, iEnableNlgeom=0, dTimePeriod=1.0, iTransient=1, iConvertDscntIter=0, iRamp=1, iExtrapolateMethod=0, iEnableIncludeCSV=0, listAbaqusOutputRequest=[], crEdit=None):
        message = "Analysis.AbaqusStep.CoupledTDStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iEnableAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, abaqusPair1, abaqusPair2, iCSVIntegration, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, dAdjustFactor, iMaxContactIter, iType, iEnableUseAdaptive, dDampingfactor, dMaxRationofStrainEnergy, iEnableNlgeom, dTimePeriod, iTransient, iConvertDscntIter, iRamp, iExtrapolateMethod, iEnableIncludeCSV, listAbaqusOutputRequest, crEdit)
        return JPT_RUN_LINE(message)

    def DynamicExplicitStep(self, strName, strDesp="", iEnableAutomatic=1, iIncrmtEstimator=0, abaqusPair1=ABAQUS_PAIR(), dTimeScalfactor=1.0, abaqusPair2=ABAQUS_PAIR(), iEnableNlgeom=1, dTimePeriod=1.0, iEnableIncludeHeatEffect=0, dLinearBlkVisco=0.06, dQuadrBlkVisco=1.2, listAbaqusOutputRequest=[], crEdit=None):
        message = "Analysis.AbaqusStep.DynamicExplicitStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iEnableAutomatic, iIncrmtEstimator, abaqusPair1, dTimeScalfactor, abaqusPair2, iEnableNlgeom, dTimePeriod, iEnableIncludeHeatEffect, dLinearBlkVisco, dQuadrBlkVisco, listAbaqusOutputRequest, crEdit)
        return JPT_RUN_LINE(message)

    def ModalStep(self, strName, strDesp="", iEigenSolver=0, iNFreqRequestbchecked=0, ilNFreqRequestTList=[], iFreqShiftbchecked=0, ilFreqShiftTList=[], iFreqRangebchecked=0, ilFreqRangeTList=[], iIncldAcoustic=0, iBlockSizebchecked=0, ilBlockSizeTList=[], iMaxBlkNumofLanczosStepbchecked=0, ilMaxBlkNumofLanczosStepTList=[], iEnableUseSIM=0, iEnableIncludeResMods=0, iNEigenRequest=2147483647, iMaxItersUsed=30, iVectorsUsed=2147483647, iMethod=0, iMatrixStorage=0, iNormalizeEigenBy=1, iEvalPropFreqbchecked=0, ilEvalPropFreqTList=[], abaqusOutputRequest=[], crEdit=None):
        message = "Analysis.AbaqusStep.ModalStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iEigenSolver, iNFreqRequestbchecked, ilNFreqRequestTList, iFreqShiftbchecked, ilFreqShiftTList, iFreqRangebchecked, ilFreqRangeTList, iIncldAcoustic, iBlockSizebchecked, ilBlockSizeTList, iMaxBlkNumofLanczosStepbchecked, ilMaxBlkNumofLanczosStepTList, iEnableUseSIM, iEnableIncludeResMods, iNEigenRequest, iMaxItersUsed, iVectorsUsed, iMethod, iMatrixStorage, iNormalizeEigenBy, iEvalPropFreqbchecked, ilEvalPropFreqTList, abaqusOutputRequest, crEdit)
        return JPT_RUN_LINE(message)

    def StaticRiskStep(self, strName, strDesp="", iEnableAutomatic=0, iMaxInc=100, dInitSize=1.0, dMinSize=1.0e-5, dMaxSize=1.0, iMethod=0, iMatrixStorage=0, dMaxLdPropFactor=0.0, iEnableMaxLdPropFactor=0, iEnableMaxDisp=0, dMaxDisp=DFLT_DBL, iEnableMaxDispDof=DFLT_INT, strNdRgn="", iEnableNlgeom=0, iEnableIncludeHeatEffect=0, iConvertDscntIter=0, dTotalArcLength=1.0, iExtrapolateMethod=0, iEnableAcceptByMaxIters=0, iEnableLongTerm=0, iEnablePerturbation=0, iFullplasticregionBchecked=0, strlFullplasticregionTlist=[], iOutput=0, crEdit=None):
        message = "Analysis.AbaqusStep.StaticRiskStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},'{}',{},{})".format(strName, strDesp, iEnableAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, iMethod, iMatrixStorage, dMaxLdPropFactor, iEnableMaxLdPropFactor, iEnableMaxDisp, dMaxDisp, iEnableMaxDispDof, strNdRgn, iEnableNlgeom, iEnableIncludeHeatEffect, iConvertDscntIter, dTotalArcLength, iExtrapolateMethod, iEnableAcceptByMaxIters, iEnableLongTerm, iEnablePerturbation, iFullplasticregionBchecked, strlFullplasticregionTlist, iOutput, crEdit)
        return JPT_RUN_LINE(message)

    def SteadyStateStep(self, strName, strDesp="", iEnableAutomatic=0, iMaxInc=100, iNitSize=1, dMinSize=1.0e-5, dMaxSize=1.0, dMaxAllowTChange=DFLT_DBL, iEndStepbchecked=0, dlEndStepTList=[], dMaxAllowEmissivityChange=0.1, iMethod=0, iMatrixStorage=0, iSolutionTech=0, iAllowedIters=8, iAdjustFactor=1, iMaxContactIter=30, iEnableNlgeom=0, dTimePeriod=1.0, iConvertDscntIter=0, iRamp=0, iExtrapolateMethod=0, iOutput=0, crEdit=None):
        message = "Analysis.AbaqusStep.SteadyStateStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iEnableAutomatic, iMaxInc, iNitSize, dMinSize, dMaxSize, dMaxAllowTChange, iEndStepbchecked, dlEndStepTList, dMaxAllowEmissivityChange, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, iAdjustFactor, iMaxContactIter, iEnableNlgeom, dTimePeriod, iConvertDscntIter, iRamp, iExtrapolateMethod, iOutput, crEdit)
        return JPT_RUN_LINE(message)

class Analysis_ACTRAN:
    def ExportBdf(self, strPath=""):
        message = "Analysis.ACTRAN.ExportBdf('{}')".format(strPath)
        return JPT_RUN_LINE(message)

    def Run(self, actranAnalysis=ACTRAN_ANALYSIS(), crlTarget=[], crEdit=None):
        message = "Analysis.ACTRAN.Run({},{},{})".format(actranAnalysis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def CreateEdat(self, actranAnalysis=ACTRAN_ANALYSIS(), crlTarget=[], crEdit=None):
        message = "Analysis.ACTRAN.CreateEdat({},{},{})".format(actranAnalysis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Analysis_Analysis:
    def Abaqus(self, strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat):
        message = "Analysis.Analysis.Abaqus('{}',{},{},{},{},{},{},'{}',{},{},'{}',{},{},{},{},{},{})".format(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat)
        return JPT_RUN_LINE(message)

class Analysis_Ansys:
    def HeadTransferSteady(self, strName, iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None):
        message = "Analysis.Ansys.HeadTransferSteady('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit)
        return JPT_RUN_LINE(message)

    def LinearStatic(self, strJobName, iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None, strFileName="", crAnsysJob=None):
        message = "Analysis.Ansys.LinearStatic('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

    def NormalModes(self, strJobName, iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None, strFileName="", crAnsysJob=None):
        message = "Analysis.Ansys.NormalModes('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

    def Harmonic(self, strJobName, iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None, strFileName="", crAnsysJob=None):
        message = "Analysis.Ansys.Harmonic('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

    def Steady(self, strJobName, iJobdataAnatype=0, iJobdataSoltype=0, strJobdataJobname="Job1", strJobdataJobdescription="", bBasicdataBoutputdisplacements=False, bBasicdataBoutputreactionload=False, bBasicdataBoutputstrain=False, bBasicdataBoutputstress=False, iBasicdataIanalysisopt=0, bBasicdataBcalPressEffects=False, dBasicdataFunitem=0.0, dBasicdataFreftemp=0.0, dBasicdataFendloadtime=0.0, iBasicdataItimestep=0, iBasicdataIstepchosen=0, iBasicdataIsubstepnum=0, iBasicdataImaxsubstep=0, iBasicdataIminstepnum=0, dBasicdataFtimestepsize=0.0, dBasicdataFmintimestep=0.0, dBasicdataFmaxtimestep=0.0, iBasicdataIwritereslutfre=1, iBasicdataIn=1, bRunAPDL=False, bWriteResultDB=False, dFEndFreq=DFLT_DBL, dFStartFreq=DFLT_DBL, iFulltransdataIsolutionoption=0, dFulltransdataFpropchange=0.05, iFulltransdataIpointnum=64, dFulltransdataFmintemp=0.0, dFulltransdataFmaxtemp=0.0, iFulltransdataIequationsolv=0, dFulltransdataFtollevel=0.0, dFulltransdataFmultiplier=0.0, bFulltransdataBsignleprecision=False, bFulltransdataBmemorysave=False, dFulltransdataFtempdiff=1.1, dHarmonicdataFstartfreq=0.0, dHarmonicdataFendfreq=1.0, iHarmonicdataNsubsteps=0, dHarmonicdataFalphad=0.0, dHarmonicdataFbetad=0.0, dHarmonicdataFdmprat=0.0, bHarmonicdataBoutputdisplacements=False, bHarmonicdataBoutputstrain=False, bHarmonicdataBoutputstress=False, iLCId=0, iModeShape=0, iModaldataImodemethod=0, iModaldataIextractnum=1, bModaldataBexpandshape=True, iModaldataIexpandnum=0, bModaldataBuseapprox=False, bModaldataBinclprsseff=False, bModaldataBmemorysave=False, bModaldataBrsvec=False, bModaldataBoutputdisplacements=False, bModaldataBoutputstrain=False, bModaldataBoutputstress=False, iReduceddataIprintnum=0, bSsdataBmemorysave=False, bSsdataBoutputheatflux=False, bSsdataBoutputtemperature=False, bSsdataBpivotscheck=True, bSsdataBsignleprecision=False, dSsdataFmultiplier=0.0, dSsdataFtempdiff=0.0, dSsdataFtollevel=0.0, iSsdataIadaptivedes=0, iSsdataIequationsolv=0, iSsdataInpoption=0, strAnsysVersion="", strCommandLineOption="", bOutputSOLVE=False, iSubspacedataIrigidmode=0, iSubspacedataIworksize=8, iSubspacedataInpadnum=4, iSubspacedataIblocknum=5, iSubspacedataImaxiteratcnt=0, iSubspacedataIminnshift=0, iSubspacedataIseqcheck=0, bTransientdataBtraneffect=True, iTransientdataIloadingtype=0, dTransientdataFmassmatrixmult=0.0, dTransientdataFstiffmatrixmult=0.0, bTransientdataBmidstep=False, dTransientdataFtolerancebisection=0.0, dTransientdataFtolerancetimestep=0.0, iTransientdataItimeinteralgor=0, iTransientdataItimeinter=0, dTransientdataFgamma=0.005, dTransientdataFalpha=0.25250625, dTransientdataFdelta=0.505, dTransientdataFalphaf=0.005, dTransientdataFalpham=0.0, bTransientdataBoutputtemperature=False, bTransientdataBoutputheatflux=False, crEdit=None, strFileName="", crAnsysJob=None):
        message = "Analysis.Ansys.Steady('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

class Analysis_Nastran:
    def ModalTransientResponse(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.Nastran.ModalTransientResponse('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def LinearBuckling(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.Nastran.LinearBuckling('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def Transient(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.Nastran.Transient('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def SteadyState(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.Nastran.SteadyState('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def ModalFrequencyResponse(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.Nastran.ModalFrequencyResponse('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def LinearStatic(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.Nastran.LinearStatic('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def NormalModes(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.Nastran.NormalModes('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis_Permas:
    def Job(self, strName, strDescription, iType, crEdit, crlTarget, bElStress, bElStressMis, bElStrain, bNodeStess, bGZip, bIdeas, bNLResult, iNLStepType, dEquiStart, dEquiStep, dEquiEnd, strNLStepList, bTimeStep, iTimeStepKind, dTimeStart, dTimeStep, dTimeEnd, iLCId):
        message = "Analysis.Permas.Job('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{})".format(strName, strDescription, iType, crEdit, crlTarget, bElStress, bElStressMis, bElStrain, bNodeStess, bGZip, bIdeas, bNLResult, iNLStepType, dEquiStart, dEquiStep, dEquiEnd, strNLStepList, bTimeStep, iTimeStepKind, dTimeStart, dTimeStep, dTimeEnd, iLCId)
        return JPT_RUN_LINE(message)

class Analysis_TSSolver:
    def ExportDynamisBdf(self, strPath, crJob):
        message = "Analysis.TSSolver.ExportDynamisBdf('{}',{})".format(strPath, crJob)
        return JPT_RUN_LINE(message)

    def Job(self, strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None):
        message = "Analysis.TSSolver.Job('{}','{}',{},'{}',{})".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit)
        return JPT_RUN_LINE(message)

    def LinearBucking(self, strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath=""):
        message = "Analysis.TSSolver.LinearBucking('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def LinearStatic(self, strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath=""):
        message = "Analysis.TSSolver.LinearStatic('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def NonlinearStatic(self, strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath=""):
        message = "Analysis.TSSolver.NonlinearStatic('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def NormalModes(self, strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath=""):
        message = "Analysis.TSSolver.NormalModes('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def NonlinearFrequency(self, strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath=""):
        message = "Analysis.TSSolver.NonlinearFrequency('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def ModalTransientResponse(self, strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath=""):
        message = "Analysis.TSSolver.ModalTransientResponse('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def TransientHeatTransfer(self, strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath=""):
        message = "Analysis.TSSolver.TransientHeatTransfer('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def ModalFrequencyResponse(self, strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath=""):
        message = "Analysis.TSSolver.ModalFrequencyResponse('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def SteadyStateHeatTransfer(self, strName="", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), crEdit=None, strPath=""):
        message = "Analysis.TSSolver.SteadyStateHeatTransfer('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class Analysis_TSSS:
    def TransientHeatTransfer(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.TSSS.TransientHeatTransfer('{}','{}',{},'{}',{},'{}',{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNastranNonlinear, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def LinearStatic(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0, iNitTempType=0):
        message = "Analysis.TSSS.LinearStatic('{}','{}',{},'{}',{},'{}',{},'{}',{},{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNastranNonlinear, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer, iNitTempType)
        return JPT_RUN_LINE(message)

    def NonlinearStatic(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.TSSS.NonlinearStatic('{}','{}',{},'{}',{},'{}',{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNastranNonlinear, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def NormalModes(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.TSSS.NormalModes('{}','{}',{},'{}',{},'{}',{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNastranNonlinear, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def LinearBuckling(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.TSSS.LinearBuckling('{}','{}',{},'{}',{},'{}',{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNastranNonlinear, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def ModalFrequencyResponse(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.TSSS.ModalFrequencyResponse('{}','{}',{},'{}',{},'{}',{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNastranNonlinear, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def SteadyStateHeatTransfer(self, strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), iRadialReturn=0, listNastranNonlinear=[], crEdit=None, strPath="", iModelCheckAnswer=0, iDeleteSlaveNodesAnswer=0):
        message = "Analysis.TSSS.SteadyStateHeatTransfer('{}','{}',{},'{}',{},'{}',{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNastranNonlinear, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis_ADVC:
    MakeProcess = ADVC_MakeProcess()

    def Structure(self, strName="", strDescription="", iEJobType=0, crlProcessSequence=[], crlElemLocationGroup=[], crlNodeLocationGroup=[], bWriteGroup=False, crEdit=None, bResultReference=False, iSeparateFile=0, bExportRelatedAllLBCs=False, bUseEntityName=False, bMatrixSloverParam=False, iPreconditionType=0, iMatrixStructure=0, crlTarget=[], iLoadType=1, bSameOutputOnAllProcess=True, bDeleteFloatingNode=True, bBC=True, bCheckBCDuplicate=False, bAutoAssignDummyProp=False, crDummyPropMaterial=None, bReferenceRestartData=False, strReferenceRestartDataPath="", iReferenceRestartDataProcessNum=DFLT_INT, iReferenceRestartDataStepNum=DFLT_INT, iReferenceRestartDataCoordType=0, iReferenceRestartDataUpdateContactSearch=1, listLoadNodeContact=[], iHeatConvection=1, iCreateProcessForBoltFixedLength=0, strPath="", iNumType=0, iUiWidth=10, iUiPrecision=1):
        message = "Analysis.ADVC.Structure('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, strDescription, iEJobType, crlProcessSequence, crlElemLocationGroup, crlNodeLocationGroup, bWriteGroup, crEdit, bResultReference, iSeparateFile, bExportRelatedAllLBCs, bUseEntityName, bMatrixSloverParam, iPreconditionType, iMatrixStructure, crlTarget, iLoadType, bSameOutputOnAllProcess, bDeleteFloatingNode, bBC, bCheckBCDuplicate, bAutoAssignDummyProp, crDummyPropMaterial, bReferenceRestartData, strReferenceRestartDataPath, iReferenceRestartDataProcessNum, iReferenceRestartDataStepNum, iReferenceRestartDataCoordType, iReferenceRestartDataUpdateContactSearch, listLoadNodeContact, iHeatConvection, iCreateProcessForBoltFixedLength, strPath, iNumType, iUiWidth, iUiPrecision)
        return JPT_RUN_LINE(message)

    def HeatTransfer(self, strName="", strDescription="", iEJobType=0, crlProcessSequence=[], crlElemLocationGroup=[], crlNodeLocationGroup=[], bWriteGroup=False, crEdit=None, bResultReference=False, iSeparateFile=0, bExportRelatedAllLBCs=False, bUseEntityName=False, bMatrixSloverParam=False, iPreconditionType=0, iMatrixStructure=0, crlTarget=[], iLoadType=1, bSameOutputOnAllProcess=True, bDeleteFloatingNode=True, bBC=True, bCheckBCDuplicate=False, bAutoAssignDummyProp=False, crDummyPropMaterial=None, bReferenceRestartData=False, strReferenceRestartDataPath="", iReferenceRestartDataProcessNum=DFLT_INT, iReferenceRestartDataStepNum=DFLT_INT, iReferenceRestartDataCoordType=0, iReferenceRestartDataUpdateContactSearch=1, listLoadNodeContact=[], iHeatConvection=1, strPath="", iNumType=0, iUiWidth=10, iUiPrecision=1):
        message = "Analysis.ADVC.HeatTransfer('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},'{}',{},{},{})".format(strName, strDescription, iEJobType, crlProcessSequence, crlElemLocationGroup, crlNodeLocationGroup, bWriteGroup, crEdit, bResultReference, iSeparateFile, bExportRelatedAllLBCs, bUseEntityName, bMatrixSloverParam, iPreconditionType, iMatrixStructure, crlTarget, iLoadType, bSameOutputOnAllProcess, bDeleteFloatingNode, bBC, bCheckBCDuplicate, bAutoAssignDummyProp, crDummyPropMaterial, bReferenceRestartData, strReferenceRestartDataPath, iReferenceRestartDataProcessNum, iReferenceRestartDataStepNum, iReferenceRestartDataCoordType, iReferenceRestartDataUpdateContactSearch, listLoadNodeContact, iHeatConvection, strPath, iNumType, iUiWidth, iUiPrecision)
        return JPT_RUN_LINE(message)

class Assemble_SeparateFaces:
    def AllSharedNodes(self, ):
        message = "Assemble.SeparateFaces.AllSharedNodes({})".format('')
        return JPT_RUN_LINE(message)

    def Shell(self, iType=0, crlEntity=[], bCreateGroup=False):
        message = "Assemble.SeparateFaces.Shell({},{},{})".format(iType, crlEntity, bCreateGroup)
        return JPT_RUN_LINE(message)

    def Solid(self, crlPart=[], crlFace=[], bCreateGroup=False):
        message = "Assemble.SeparateFaces.Solid({},{},{})".format(crlPart, crlFace, bCreateGroup)
        return JPT_RUN_LINE(message)

class Assembly_RightClick:
    def AddToReference(self, crSrcPart, crDestPart):
        message = "Assembly.RightClick.AddToReference({},{})".format(crSrcPart, crDestPart)
        return JPT_RUN_LINE(message)

    def Suppress(self, crlPart=[]):
        message = "Assembly.RightClick.Suppress({})".format(crlPart)
        return JPT_RUN_LINE(message)

    def UnSuppress(self, crlPart=[]):
        message = "Assembly.RightClick.UnSuppress({})".format(crlPart)
        return JPT_RUN_LINE(message)

    def RestoreOriginalPart(self, crlBodies=[], bKeepShareFace=False):
        message = "Assembly.RightClick.RestoreOriginalPart({},{})".format(crlBodies, bKeepShareFace)
        return JPT_RUN_LINE(message)

    def Rename(self, strNewName="New name", crItem=None):
        message = "Assembly.RightClick.Rename('{}',{})".format(strNewName, crItem)
        return JPT_RUN_LINE(message)

    def ChangeEntityColor(self, crlEntity, iColor=0):
        message = "Assembly.RightClick.ChangeEntityColor({},{})".format(crlEntity, iColor)
        return JPT_RUN_LINE(message)

    def AddSubAssembly(self, crInst=None):
        message = "Assembly.RightClick.AddSubAssembly({})".format(crInst)
        return JPT_RUN_LINE(message)

    def ChangeBodyColor(self, listPartColorPair=[], bResetFaceColor=False):
        message = "Assembly.RightClick.ChangeBodyColor({},{})".format(listPartColorPair, bResetFaceColor)
        return JPT_RUN_LINE(message)

    def ChangeMeshLineColor(self, crlFace, iColor=0):
        message = "Assembly.RightClick.ChangeMeshLineColor({},{})".format(crlFace, iColor)
        return JPT_RUN_LINE(message)

class BodyLoads_CentrifugalForce:
    def CoordinateSystems(self, strName="CentrifugalForce1", dFVelocity=DFLT_DBL, dFAcceleration=DFLT_DBL, iAxisDirection=0, iVelocityUnit=0, iAccelerationUnit=0, crCurCoord=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems('{}',{},{},{},{},{},{},{},{})".format(strName, dFVelocity, dFAcceleration, iAxisDirection, iVelocityUnit, iAccelerationUnit, crCurCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def TwoPositions(self, strName="CentrifugalForce1", dFBasePoint1=0.0, dFBasePoint2=0.0, dFBasePoint3=0.0, dFTipPoint1=0.0, dFTipPoint2=0.0, dFTipPoint3=0.0, dFVelocity=0.0, dFAcceleration=0.0, iVelocityUnit=0, iAccelerationUnit=0, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dFBasePoint1, dFBasePoint2, dFBasePoint3, dFTipPoint1, dFTipPoint2, dFTipPoint3, dFVelocity, dFAcceleration, iVelocityUnit, iAccelerationUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Force_FunctionLoadCylinder:
    def Quadratic(self, strName="ForceQuadratic1", dFTotalForce=0.0, dA=0.0, dB=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.Quadratic('{}',{},{},{},{},{},{},{},{},{})".format(strName, dFTotalForce, dA, dB, crCoord, iAngleBase, dAngleRange, iEnArrowDir, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Sine(self, strName="ForceSine1", dFTotalForce=0.0, dA=0.0, crCoord=None, iAngleBase=0, dAngleRange=0.0, iEnArrowDir=0, bDistributeInAxis=False, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.Sine('{}',{},{},{},{},{},{},'{}',{},{})".format(strName, dFTotalForce, dA, crCoord, iAngleBase, dAngleRange, iEnArrowDir, bDistributeInAxis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Vector(self, strName="ForceVector1", dFTotalForce=DFLT_DBL, dA=DFLT_DBL, dX=DFLT_DBL, dY=DFLT_DBL, crCoord=None, iEnDirection=0, dAngleRange=0.0, iArrowDir=0, bDistributeInAxis=False, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.Vector('{}',{},{},{},{},{},{},{},{},'{}',{},{})".format(strName, dFTotalForce, dA, dX, dY, crCoord, iEnDirection, dAngleRange, iArrowDir, bDistributeInAxis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Force_NonlinearForce:
    def NOLIN3(self, strName, dForceScale=0.0, dMomentScale=0.0, dForcePowerA=0.0, dMomentPowerA=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCurCoord=None, crlMasterTarget=[], crlSlaveTarget=[], crEdit=None):
        message = "BoundaryConditions.Force.NonlinearForce.NOLIN3('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

    def NOLIN4(self, strName, dForceScale=0.0, dMomentScale=0.0, dForcePowerA=0.0, dMomentPowerA=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCurCoord=None, crlMasterTarget=[], crlSlaveTarget=[], crEdit=None):
        message = "BoundaryConditions.Force.NonlinearForce.NOLIN4('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

    def NOLIN1(self, strName="NonlinearForce1_1", dForceScale=0.0, dMomentScale=0.0, iForcDir=0, iForceDepends=0, iMomentDir=0, iMomentDepends=0, crCoord=None, crForceTable=None, crMomentTable=None, crlMaster=[], crlSlave=[], crEdit=None):
        message = "BoundaryConditions.Force.NonlinearForce.NOLIN1('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCoord, crForceTable, crMomentTable, crlMaster, crlSlave, crEdit)
        return JPT_RUN_LINE(message)

class InitialNodalValue_InitialAngularVelocity:
    def Abaqus(self, strName="InitialAngularVelocityAbaqus1", dVelocity=DFLT_DBL, strFirstCoord="", strSecondCoord="", crlTarget=[], crEdit=None):
        message = "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus('{}',{},'{}','{}',{},{})".format(strName, dVelocity, strFirstCoord, strSecondCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def General(self, strName="InitialAngularVelocity1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None):
        message = "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General('{}',{},{},{})".format(strName, stData, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_BoundaryTemperature:
    def Constant(self, strName="BoundaryTemperature_1", dFTemp=0.0, crTable=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.BoundaryTemperature.Constant('{}',{},{},{},{})".format(strName, dFTemp, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def SurfaceMapping(self, strName="MappingTemperature", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0, iMappedCpIndexArr1=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strPath="", crEdit=None, iMappingMethod=0, iSubmodeLBCMappingType=3, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="all"):
        message = "BoundaryConditions.BoundaryTemperature.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, iMappedCpIndexArr1, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strPath, crEdit, iMappingMethod, iSubmodeLBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
        return JPT_RUN_LINE(message)

class BoundaryConditions_Convection:
    def Constant(self, strName="Convection_1", dExtTemp=DFLT_DBL, crTableTimeTemp=None, dDcoef=DFLT_DBL, crTableTimeCoeff=None, crTableTempCoeff=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Convection.Constant('{}',{},{},{},{},{},{},{})".format(strName, dExtTemp, crTableTimeTemp, dDcoef, crTableTimeCoeff, crTableTempCoeff, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def SurfaceMapping(self, strName="MappingConvection1", crlTarget=[], iPos=0, iViewCp=0, iCp=0, iSrcType=0, iMappedCpIndex0=0, iMappedCpIndex1=0, dRScale=1.0, posOffset=[0,0,0], posAxis=[0,0,0], dTScale=1.0, dSearchRange=1.0, iHTCUnit=0, iTempUnit=0, strPath="", crEdit=None):
        message = "BoundaryConditions.Convection.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, crlTarget, iPos, iViewCp, iCp, iSrcType, iMappedCpIndex0, iMappedCpIndex1, dRScale, posOffset, posAxis, dTScale, dSearchRange, iHTCUnit, iTempUnit, strPath, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_EnforcedLoads:
    def Acceleration(self, strName="EnforcedAcceleration1", iDwDof=0, dFVel1=DFLT_DBL, dFVel2=DFLT_DBL, dFVel3=DFLT_DBL, dFVel4=DFLT_DBL, dFVel5=DFLT_DBL, dFVel6=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, bExport=False, crMEExport1=None, crMEExport2=None, crMEExport3=None, crMEExport4=None, crMEExport5=None, crMEExport6=None, iAcUnit=0, iRotUnit=0, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.EnforcedLoads.Acceleration('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDwDof, dFVel1, dFVel2, dFVel3, dFVel4, dFVel5, dFVel6, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, bExport, crMEExport1, crMEExport2, crMEExport3, crMEExport4, crMEExport5, crMEExport6, iAcUnit, iRotUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Velocity(self, strName="EnforcedVelocity1", iDwDof=0, dFVel0=DFLT_DBL, dFVel1=DFLT_DBL, dFVel2=DFLT_DBL, dFVel3=DFLT_DBL, dFVel4=DFLT_DBL, dFVel5=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, iVelUnit=0, iRotUnit=0, bExport=False, crExportData0=None, crExportData1=None, crExportData2=None, crExportData3=None, crExportData4=None, crExportData5=None, crlTarget=[], crEdit=None, bADVCStatic=False):
        message = "BoundaryConditions.EnforcedLoads.Velocity('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDwDof, dFVel0, dFVel1, dFVel2, dFVel3, dFVel4, dFVel5, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, iVelUnit, iRotUnit, bExport, crExportData0, crExportData1, crExportData2, crExportData3, crExportData4, crExportData5, crlTarget, crEdit, bADVCStatic)
        return JPT_RUN_LINE(message)

    def Displacement(self, strName="", iDwDof=0, dFDisp0=DFLT_DBL, dFDisp1=DFLT_DBL, dFDisp2=DFLT_DBL, dFDisp3=DFLT_DBL, dFDisp4=DFLT_DBL, dFDisp5=DFLT_DBL, crCurCoord=None, iEnArrowDir=0, crTable=None, crNodeSet=None, dFPhase=DFLT_DBL, dFDelay=DFLT_DBL, crPhaseTable=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.EnforcedLoads.Displacement('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDwDof, dFDisp0, dFDisp1, dFDisp2, dFDisp3, dFDisp4, dFDisp5, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_HeatFlux:
    def SurfaceFlux(self, strName, dFflux, iDistributionMethod, crTable, crlTarget, crEdit=None):
        message = "BoundaryConditions.HeatFlux.SurfaceFlux('{}',{},'{}',{},{},{})".format(strName, dFflux, iDistributionMethod, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def SurfaceMapping(self, strName="MappingHeatFlux", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strStrpath="", crEdit=None, iMappingMethod=0, iSubmodeLBCMappingType=4, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet="all"):
        message = "BoundaryConditions.HeatFlux.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strStrpath, crEdit, iMappingMethod, iSubmodeLBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
        return JPT_RUN_LINE(message)

    def ConcentrateFlux(self, strName = "ConcentrateHeatFlux1", lbcConcentrateFluxData=LBC_CONCENTRATE_FLUX_DATA(), crlTarget=[], crEdit=None):
        message = "BoundaryConditions.HeatFlux.ConcentrateFlux('{}',{},{},{})".format(strName , lbcConcentrateFluxData, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_InitialElementalValue:
    def InitialStress(self, strName="InitialStress1", iDimension=2, iElemCs=0, dSXX=DFLT_DBL, dSYY=DFLT_DBL, dSXY=DFLT_DBL, crTable=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.InitialElementalValue.InitialStress('{}',{},{},{},{},{},{},{},{})".format(strName, iDimension, iElemCs, dSXX, dSYY, dSXY, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_InitialTemperature:
    def WholeMapping(self, strName="TemperatureInitsWholeMapping1", iMapSourceType=0, strPath="", iMappingMethod=0, iIsubcase=0, crEdit=None):
        message = "BoundaryConditions.InitialTemperature.WholeMapping('{}',{},'{}',{},{},{})".format(strName, iMapSourceType, strPath, iMappingMethod, iIsubcase, crEdit)
        return JPT_RUN_LINE(message)

    def Constant(self, strName="InitialTemperature1",dFTemp=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.InitialTemperature.Constant('{}',{},'{}',{},{},{},{})".format(strName,dFTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ADVC(self, strName="InitialTemperature1",dTemperatureValue=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.InitialTemperature.ADVC('{}',{},'{}',{},{},{},{})".format(strName,dTemperatureValue, strFilePathName, bUseDefault, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def NastranPunch(self, strName="InitialTemperature1",dTemperatureValue=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.InitialTemperature.NastranPunch('{}',{},'{}',{},{},{},{})".format(strName,dTemperatureValue, strFilePathName, bUseDefault, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_LBCCopy:
    def PropertiesCopyTranslate(self, iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.PropertiesCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def PropertiesCopyRotate(self, iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.PropertiesCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def PropertiesCopyMirror(self, iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.PropertiesCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

    def ConnectionCopyTranslate(self, iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.ConnectionCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def ConnectionCopyRotate(self, iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.ConnectionCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def ConnectionCopyMirror(self, iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.ConnectionCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

    def GroupCopyTranslate(self, iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.GroupCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def GroupCopyRotate(self, iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.GroupCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def GroupCopyMirror(self, iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.GroupCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

    def LBCCopyTranslate(self, iMethod=0, iMatchMethod=0, posVecTrans=[0,0,0], dMagnitude=1, dTrandataDoffset=0.0, dTol=1, crCoord=None, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.LBCCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def LBCCopyRotate(self, iMethod=1, iMatchMethod=0, posAxis=[0,0,0], posCenter=[0,0,0], dAngle=0.0, dTol=1, crCoord=None, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.LBCCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def LBCCopyMirror(self, iMethod=2, iMatchMethod=0, poslPoints=[], dOffset=0, dTol=1, crlTarget=[]):
        message = "BoundaryConditions.LBCCopy.LBCCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions_Pressure:
    def SurfaceLoads(self, strName="SurfaceLoads1", dlPressure=[0,0,0], iArrowdir=0, crCoordinate=None, crlTargetFace=[], crEditCur=None):
        message = "BoundaryConditions.Pressure.SurfaceLoads('{}',{},{},{},{},{})".format(strName, dlPressure, iArrowdir, crCoordinate, crlTargetFace, crEditCur)
        return JPT_RUN_LINE(message)

    def By2Nodes(self, strName="PressureLinear1", crNodeA=None, dPressureA=0.0, iNodeAUnit=0, crNodeB=None, dPressureB=0.0, iNodeBUnit=0, iDirection=0, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Pressure.By2Nodes('{}',{},{},{},{},{},{},{},{},{})".format(strName, crNodeA, dPressureA, iNodeAUnit, crNodeB, dPressureB, iNodeBUnit, iDirection, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def General(self, strName="Pressure1", dFpressure=0.0, iIdistribute=0, crTable=None, dDphase=0.0, dDdelay=0.0, crPhaseTable=None, strFormularValue="", crCoord=None, dlDirection=[DFLT_DBL,DFLT_DBL,DFLT_DBL], strFormularDirX="", strFormularDirY="", strFormularDirZ="", iArrowDir=1, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Pressure.General('{}',{},'{}',{},{},{},{},'{}',{},{},'{}','{}','{}',{},{},{})".format(strName, dFpressure, iIdistribute, crTable, dDphase, dDdelay, crPhaseTable, strFormularValue, crCoord, dlDirection, strFormularDirX, strFormularDirY, strFormularDirZ, iArrowDir, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Quadratic(self, strName="PressureQuadratic1", dA=0.0, dB=0.0, crCoordinate=None, dAngleRange=0.0, iPressureDirectionMode=0, dlPressureDirection=[0.0,0.0,0.0], crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Pressure.Quadratic('{}',{},{},{},{},{},{},{},{})".format(strName, dA, dB, crCoordinate, dAngleRange, iPressureDirectionMode, dlPressureDirection, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def FunctionLoadToCylinderSine(self, strName="PressureSine1", dA=0.0, crCoordinate=None, dAngleRange=0.0, bDistributionAxis=False, iPressureDirectionMode=0, bIsTotalForceAdjustment=False, dTotalForce=0.0, vecPressureDirection=[0.0,0.0,0.0], crCoordinateSystemForDirection=None, bIsCornerNodesDistribution=False, strFormulaForA="", crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Pressure.FunctionLoadToCylinderSine('{}',{},{},{},'{}',{},{},{},{},{},'{}','{}',{},{})".format(strName, dA, crCoordinate, dAngleRange, bDistributionAxis, iPressureDirectionMode, bIsTotalForceAdjustment, dTotalForce, vecPressureDirection, crCoordinateSystemForDirection, bIsCornerNodesDistribution, strFormulaForA, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Hydrostatic(self, strName="PressureHydrostatic1", dFHPressure=0.0, dFDensity=0.0, iDensityUnit=0, dFGravity=0.0, iGravityUnit=0, iGravityDir=0, dFWaterSuface=0.0, iSufaceUnit=0, iDistributionMethod=0, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Pressure.Hydrostatic('{}',{},{},{},{},{},{},{},{},'{}',{},{})".format(strName, dFHPressure, dFDensity, iDensityUnit, dFGravity, iGravityUnit, iGravityDir, dFWaterSuface, iSufaceUnit, iDistributionMethod, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def SurfaceMapping(self, strName="MappingPressure", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr=0, dScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, iUnit=0, strPath="", crEdit=None):
        message = "BoundaryConditions.Pressure.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strPath, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_Submodel:
    def SubmodelForcedFlux(self, strName, iSolver=0, strFilePathName="/home/", iProcessNo=0, iReferType=-1, dExtensionRange=DFLT_DBL, dExtensionTol=DFLT_DBL, dExtensionLimitTol=DFLT_DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT_INT, iNumBucketMaxY=DFLT_INT, iNumBucketMaxZ=DFLT_INT, iPrevBc=-1, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Submodel.SubmodelForcedFlux('{}',{},'{}',{},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(strName, iSolver, strFilePathName, iProcessNo, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ForcedTempertature(self, strName="SubmodelForcedTemperature1", iSolver=0, strFilePathName="/home/", iProcessNo=0, iReferType=0, dExtensionRange=DFLT_DBL, dExtensionTol=DFLT_DBL, dExtensionLimitTol=DFLT_DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT_INT, iNumBucketMaxY=DFLT_INT, iNumBucketMaxZ=DFLT_INT, iPrevBc=-1, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Submodel.ForcedTempertature('{}',{},'{}',{},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(strName, iSolver, strFilePathName, iProcessNo, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ForcedDisplacement(self, strName="SubmodelForcedDisplacement1", iSolver=0, strFilePathName="/home/", iProcessNo=0, bTranslationX=True, bTranslationY=True, bTranslationZ=True, iReferType=-1, dExtensionRange=DFLT_DBL, dExtensionTol=DFLT_DBL, dExtensionLimitTol=DFLT_DBL, strGlobalElementSet="", iUseBucket=-1, iNumBucketMaxX=DFLT_INT, iNumBucketMaxY=DFLT_INT, iNumBucketMaxZ=DFLT_INT, iPrevBc=-1, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Submodel.ForcedDisplacement('{}',{},'{}',{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(strName, iSolver, strFilePathName, iProcessNo, bTranslationX, bTranslationY, bTranslationZ, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_TemperatureLoads:
    def Constant(self, strName, dTemperature=0.0, crTable=None, crlTarget=[], crEdit=None, bUseDefaultTemp=False):
        message = "BoundaryConditions.TemperatureLoads.Constant('{}',{},{},{},{},{})".format(strName, dTemperature, crTable, crlTarget, crEdit, bUseDefaultTemp)
        return JPT_RUN_LINE(message)

    def ADVCFile(self, strName="TemperatureLoadsADVC1", strFilePathName="", crTable=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.TemperatureLoads.ADVCFile('{}','{}',{},{},{})".format(strName, strFilePathName, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def NastranPunch(self, strName="TemperatureLoadsPunch1", strFilePathName="", crTable=None, crlTarget=[], crEdit=None, bUseAsMaterialReferenceTemp=False):
        message = "BoundaryConditions.TemperatureLoads.NastranPunch('{}','{}',{},{},{},{})".format(strName, strFilePathName, crTable, crlTarget, crEdit, bUseAsMaterialReferenceTemp)
        return JPT_RUN_LINE(message)

    def WholeMapping(self, strName="TemperatureLoadsWholeMapping", crlTarget=[], iMAPPos=0, iViewCp=0, iCp=1, iSrcType=0, iMappedCpIndexArr0=0, iMappedCpIndexArr1=0, iDScaleFactor=1, posOffset=[0,0,0], posRotate=[0,0,0], dCorScale=1, dSearchRange=0, strPath="", crEdit=None, iMappingMethod=0, iSubmodelBCMappingType=2, iMappingFromStepNo=0, bSetADVCFile=False, strADVCResultFile="", bSetDetATol=False, dDetATol=DFLT_DBL, bSetElementSet=False, strElementSet=""):
        message = "BoundaryConditions.TemperatureLoads.WholeMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, iMappedCpIndexArr1, iDScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
        return JPT_RUN_LINE(message)

    def LbcInitialTemperature(self, strName="InitialTemperature1", iType=0, dFTemp=0.0, strFilePathName="", bUseDefault=False, crTable=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.TemperatureLoads.LbcInitialTemperature('{}',{},{},'{}',{},{},{},{})".format(strName, iType, dFTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_BodyLoads:
    CentrifugalForce = BodyLoads_CentrifugalForce()

    def Gravity(self, strName, dlGravity, crCurCoord=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.BodyLoads.Gravity('{}',{},{},{},{})".format(strName, dlGravity, crCurCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_Force:
    FunctionLoadCylinder = Force_FunctionLoadCylinder()

    NonlinearForce = Force_NonlinearForce()

    def General(self, strName, vecForce=[DFLT_DBL, DFLT_DBL, DFLT_DBL], vecMoment=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iEnArrowDir=0, iDistributionMethod=0, crCurCoord=None, crTable=None, crNodeSet=None, dFPhase=0.0, dFDelay=0.0, crPhaseTable=None, strFormula1="", strFormula2="", strFormula3="", strFormula4="", strFormula5="", strFormula6="", crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Force.General('{}',{},{},{},'{}',{},{},{},{},{},{},'{}','{}','{}','{}','{}','{}',{},{})".format(strName, vecForce, vecMoment, iEnArrowDir, iDistributionMethod, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, strFormula6, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ForceNormalDirection(self, strName, vecForce=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iEnArrowDir=0, iDistributionMethod=0, crCurCoord=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.Force.ForceNormalDirection('{}',{},{},'{}',{},{},{})".format(strName, vecForce, iEnArrowDir, iDistributionMethod, crCurCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions_InitialNodalValue:
    InitialAngularVelocity = InitialNodalValue_InitialAngularVelocity()

    def Displacement(self, strName="InitialDisplacement1", iType=0, vecInit=[DFLT_DBL,DFLT_DBL,DFLT_DBL], bSelNode=False, crNodeSet=None, crTable=None, crCoord=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.InitialNodalValue.Displacement('{}',{},{},{},{},{},{},{},{})".format(strName, iType, vecInit, bSelNode, crNodeSet, crTable, crCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Velocity(self, strName="InitialRotationAngle1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None):
        message = "BoundaryConditions.InitialNodalValue.Velocity('{}',{},{},{})".format(strName, stData, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def RotationAngle(self, strName="InitialVelocity1", stData=LBC_DYNAMIC_INITIAL_CONDITION_DATA(), crlTarget=[], crEdit=None):
        message = "BoundaryConditions.InitialNodalValue.RotationAngle('{}',{},{},{})".format(strName, stData, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoltConnections_Edge:
    def TypeC(self, crlEdgeCur1, crlEdgeCur2, strRbeName="RBE", dPlaneTol=20.0, dMaxBoltHeight=100.0, iConnectionType=0, iCoincidentNodes=1, dTolerance=0.0, iGround=0, dStiffnessX=0.0, dStiffnessY=0.0, dStiffnessZ=0.0, iLocalStiffUnit=0, dRotateStiffX=0.0, dRotateStiffY=0.0, dRotateStiffZ=0.0, iLocalRotateStiffUnit=0, dDampCoef=0.0, dStressCoef=0.0, crCurCoord=None, iTopRbeType=0, dTopPitch=10, dTopRemoveDepth=0.0, iBotRbeType=0, dBotPitch=10, dBotRemoveDepth=0.0):
        message = "Connections.BoltConnections.Edge.TypeC({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1, crlEdgeCur2, strRbeName, dPlaneTol, dMaxBoltHeight, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth)
        return JPT_RUN_LINE(message)

    def TypeB(self, crlEdgeCur1, crlEdgeCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, dRBE2=0.0, dBotDtDia=0.0, dPitch=10.0, iBotRbeConnType=0, bIfCreate2ADVCStaticProcessForBoltFixLength=False):
        message = "Connections.BoltConnections.Edge.TypeB({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1, crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, bIfCreate2ADVCStaticProcessForBoltFixLength)
        return JPT_RUN_LINE(message)

    def TypeD(self, crlEdgeCur1, crlEdgeCur2, strMpcName="MPC", dConnRadius=0.0, dPlaneTol=20.0):
        message = "Connections.BoltConnections.Edge.TypeD({},{},'{}',{},{})".format(crlEdgeCur1, crlEdgeCur2, strMpcName, dConnRadius, dPlaneTol)
        return JPT_RUN_LINE(message)

    def TypeA(self, crlEdgeCur1, crlEdgeCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, iBotSlot=0, dRBE2=0.0, bIsCreate2ADVCStaticProcessForFixLength=False):
        message = "Connections.BoltConnections.Edge.TypeA({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1, crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, bIsCreate2ADVCStaticProcessForFixLength)
        return JPT_RUN_LINE(message)

class BoltConnections_Face:
    def TypeC(self, crlFaceCur1, crlFaceCur2, strRbeName="RBE", dPlaneTol=20, dMaxBoltHeight=100, dMaxDiameter=0, dMinDiameter=0, iConnectionType=0, iCoincidentNodes=1, dTolerance=0.0, iGround=0, dStiffnessX=0.0, dStiffnessY=0.0, dStiffnessZ=0.0, iLocalStiffUnit=0, dRotateStiffX=0.0, dRotateStiffY=0.0, dRotateStiffZ=0.0, iLocalRotateStiffUnit=0, dDampCoef=0.0, dStressCoef=0.0, crCurCoord=None, iTopRbeType=0, dTopPitch=10, dTopRemoveDepth=0.0, iBotRbeType=0, dBotPitch=10, dBotRemoveDepth=0.0):
        message = "Connections.BoltConnections.Face.TypeC({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1, crlFaceCur2, strRbeName, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth)
        return JPT_RUN_LINE(message)

    def TypeB(self, crlFaceCur1, crlFaceCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, dMaxDiameter=0.0, dMinDiameter=0.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, dRBE2=0.0, dBotDtDia=0.0, dPitch=10.0, iBotRbeConnType=0, dScale1=1.10, bIsCreate2ADVCStaticProcessForFixLength=False):
        message = "Connections.BoltConnections.Face.TypeB({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1, crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, dScale1, bIsCreate2ADVCStaticProcessForFixLength)
        return JPT_RUN_LINE(message)

    def TypeA(self, crlFaceCur1, crlFaceCur2, strRbeName="RBE", strBarName="", iShaftType=0, crCurBarProperty=None, dPlaneTol=20.0, dMaxBoltHeight=100.0, dMaxDiameter=0.0, dMinDiameter=0.0, bPretensionLoad=False, iSolverType=0, dForceValue=0.0, iPreTenDof=0, crCurCoord=None, iBoltFixLength=0, iTopSlot=0, dRBE1=0.0, iBotSlot=0, dRBE2=0.0, dScale1=1.10, bIfCreate2ADVCStaticProcessForBoltFixLength=False):
        message = "Connections.BoltConnections.Face.TypeA({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1, crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, dScale1, bIfCreate2ADVCStaticProcessForBoltFixLength)
        return JPT_RUN_LINE(message)

class Contacts_Abaqus:
    def ContactTable(self, strName="", iContactMethod=0, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0):
        message = "Connections.Contacts.Abaqus.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iFormula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName="", iContactMethod=1, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0):
        message = "Connections.Contacts.Abaqus.ManualGroup('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iFormula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ManualFace(self, strName="", iContactMethod=0, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0):
        message = "Connections.Contacts.Abaqus.ManualFace('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iFormula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName="", iContactMethod=1, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0):
        message = "Connections.Contacts.Abaqus.ContactGroupByMatrix('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iFormula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, strName="", iContactMethod=3, iContactType=0, iAlg=0, dAdjustVal=0.0, dExtensionZone=0.0, dMaxPenetration=0.0, iSmallSliding=0, dSmooth=0.0, iFrictionType=0, dFrictionCoef1=0.0, dFrictionCoef2=0.0, dShearLimit=0.0, dSlipTol=0.0, dStaticFrictionCoef=0.0, dKineticFrictionCoef=0.0, dDecayCoef=0.0, iAdjust=0, dPositonTol=0.0, iFormula=0, iTie=0, iPOCType=0, iAllowSeparation=0, dSlope=0.0, tshPOCTsheet=[], iClearanceType=0, iClearanceTypeId=0, bTemperatureDependency=False, iDependencies=0, tshCDTsheet=[], iPrsTypeId=0, bPrsTemperatureDependency=False, iPrsDependencies=0, tshPrsDTsheet=[], crplTarget=[], crEdit=None, iColor=0):
        message = "Connections.Contacts.Abaqus.ContactShareFace('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iFormula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Contacts_ADVC:
    def ContactClearance(self, strName, dClearanceVal, iLocalUnit, iSolverType, crlTarget, crEdit=None):
        message = "Connections.Contacts.ADVC.ContactClearance('{}',{},{},{},{},{})".format(strName, dClearanceVal, iLocalUnit, iSolverType, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName="ContactADVC", iContactType=0, iSlidingType=0, iInitialState=0, dInitialStateTol=DFLT_DBL, dKineticFrictionCoef=DFLT_DBL, dExponentialCoef=DFLT_DBL, iBehavior=0, dClearance=DFLT_DBL, iAdjust2Clearance=0, dInterference=DFLT_DBL, iAdjust2Interference=0, iAutoShrink=0, iAdvAdjust=0, dAdjustValue=DFLT_DBL, dFrictionCoef=DFLT_DBL, dMaxShear=DFLT_DBL, dElasticSlip=DFLT_DBL, dSlipTolerance=DFLT_DBL, dSearchWidth=DFLT_DBL, dSearchGap=DFLT_DBL, dSearchDepth=DFLT_DBL, dCritialPenetration=DFLT_DBL, iEstimationImpactTime=0, iFormula=0, iConstraintType=0, iDataType=0, iTypeId=0, bTemperatureDependency=False, iNumDependencies=0, tshTableClearance=[], bStabilized=0, iStabilizeType=0, dResidualFactor=DFLT_DBL, dEffectiveDist=DFLT_DBL, dCN=DFLT_DBL, dCT=DFLT_DBL, crlClearance=[], crplTarget=[], crEdit=None, dSearchAngle=DFLT_DBL, iConstraintTypeExplicit=0, dPenaltyFact=DFLT_DBL, dPenaltyFactExplicit=DFLT_DBL, iColor=16711680, iAlg=0, iMethod=0):
        message = "Connections.Contacts.ADVC.ManualGroup('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ManualFace(self, crlFaceMaster=[], crlFaceSlave=[], strName="ContactADVC", iContactType=0, iSlidingType=0, iInitialState=0, dInitialStateTol=DFLT_DBL, dKineticFrictionCoef=DFLT_DBL, dExponentialCoef=DFLT_DBL, iBehavior=0, dClearance=DFLT_DBL, iAdjust2Clearance=0, dInterference=DFLT_DBL, iAdjust2Interference=0, iAutoShrink=0, iAdvAdjust=0, dAdjustValue=DFLT_DBL, dFrictionCoef=DFLT_DBL, dMaxShear=DFLT_DBL, dElasticSlip=DFLT_DBL, dSlipTolerance=DFLT_DBL, dSearchWidth=DFLT_DBL, dSearchGap=DFLT_DBL, dSearchDepth=DFLT_DBL, dCritialPenetration=DFLT_DBL, iEstimationImpactTime=0, iFormula=0, iConstraintType=0, iDataType=0, iTypeId=0, bTemperatureDependency=False, iNumDependencies=0, tshTableClearance=[], bStabilized=0, iStabilizeType=0, dResidualFactor=DFLT_DBL, dEffectiveDist=DFLT_DBL, dCN=DFLT_DBL, dCT=DFLT_DBL, crlClearance=[], crEdit=None, dSearchAngle=DFLT_DBL, iConstraintTypeExplicit=0, dPenaltyFact=DFLT_DBL, dPenaltyFactExplicit=DFLT_DBL, iColor=16711680, iAlg=0, iMethod=0):
        message = "Connections.Contacts.ADVC.ManualFace({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace=[], strName="ContactADVC", iContactType=0, iSlidingType=0, iInitialState=0, dInitialStateTol=DFLT_DBL, dKineticFrictionCoef=DFLT_DBL, dExponentialCoef=DFLT_DBL, iBehavior=0, dClearance=DFLT_DBL, iAdjust2Clearance=0, dInterference=DFLT_DBL, iAdjust2Interference=0, iAutoShrink=0, iAdvAdjust=0, dAdjustValue=DFLT_DBL, dFrictionCoef=DFLT_DBL, dMaxShear=DFLT_DBL, dElasticSlip=DFLT_DBL, dSlipTolerance=DFLT_DBL, dSearchWidth=DFLT_DBL, dSearchGap=DFLT_DBL, dSearchDepth=DFLT_DBL, dCritialPenetration=DFLT_DBL, iEstimationImpactTime=0, iFormula=0, iConstraintType=0, iDataType=0, iTypeId=0, bTemperatureDependency=False, iNumDependencies=0, tshTableClearance=[], bStabilized=0, iStabilizeType=0, dResidualFactor=DFLT_DBL, dEffectiveDist=DFLT_DBL, dCN=DFLT_DBL, dCT=DFLT_DBL, crlClearance=[], crEdit=None, dSearchAngle=DFLT_DBL, iConstraintTypeExplicit=0, dPenaltyFact=DFLT_DBL, dPenaltyFactExplicit=DFLT_DBL, iColor=16711680, iAlg=0, iMethod=3):
        message = "Connections.Contacts.ADVC.ContactShareFace({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(crlShareFace, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName="ContactADVC", iContactType=0, iSlidingType=0, iInitialState=0, dInitialStateTol=DFLT_DBL, dKineticFrictionCoef=DFLT_DBL, dExponentialCoef=DFLT_DBL, iBehavior=0, dClearance=DFLT_DBL, iAdjust2Clearance=0, dInterference=DFLT_DBL, iAdjust2Interference=0, iAutoShrink=0, iAdvAdjust=0, dAdjustValue=DFLT_DBL, dFrictionCoef=DFLT_DBL, dMaxShear=DFLT_DBL, dElasticSlip=DFLT_DBL, dSlipTolerance=DFLT_DBL, dSearchWidth=DFLT_DBL, dSearchGap=DFLT_DBL, dSearchDepth=DFLT_DBL, dCritialPenetration=DFLT_DBL, iEstimationImpactTime=0, iFormula=0, iConstraintType=0, iDataType=0, iTypeId=0, bTemperatureDependency=False, iNumDependencies=0, tshTableClearance=[], bStabilized=0, iStabilizeType=0, dResidualFactor=DFLT_DBL, dEffectiveDist=DFLT_DBL, dCN=DFLT_DBL, dCT=DFLT_DBL, crlClearance=[], crplTarget=[], crEdit=None, dSearchAngle=DFLT_DBL, iConstraintTypeExplicit=0, dPenaltyFact=DFLT_DBL, dPenaltyFactExplicit=DFLT_DBL, iColor=16711680, iAlg=0, iMethod=0):
        message = "Connections.Contacts.ADVC.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName="ContactADVC", iContactType=0, iSlidingType=0, iInitialState=0, dInitialStateTol=DFLT_DBL, dKineticFrictionCoef=DFLT_DBL, dExponentialCoef=DFLT_DBL, iBehavior=0, dClearance=DFLT_DBL, iAdjust2Clearance=0, dInterference=DFLT_DBL, iAdjust2Interference=0, iAutoShrink=0, iAdvAdjust=0, dAdjustValue=DFLT_DBL, dFrictionCoef=DFLT_DBL, dMaxShear=DFLT_DBL, dElasticSlip=DFLT_DBL, dSlipTolerance=DFLT_DBL, dSearchWidth=DFLT_DBL, dSearchGap=DFLT_DBL, dSearchDepth=DFLT_DBL, dCritialPenetration=DFLT_DBL, iEstimationImpactTime=0, iFormula=0, iConstraintType=0, iDataType=0, iTypeId=0, bTemperatureDependency=False, iNumDependencies=0, tshTableClearance=[], bStabilized=0, iStabilizeType=0, dResidualFactor=DFLT_DBL, dEffectiveDist=DFLT_DBL, dCN=DFLT_DBL, dCT=DFLT_DBL, crlClearance=[], crplTarget=[], crEdit=None, dSearchAngle=DFLT_DBL, iConstraintTypeExplicit=0, dPenaltyFact=DFLT_DBL, dPenaltyFactExplicit=DFLT_DBL, iColor=16711680, iAlg=0, iMethod=0):
        message = "Connections.Contacts.ADVC.ContactGroupByMatrix('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

class Contacts_Ansys:
    def ManualGroup(self, strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680):
        message = "Connections.Contacts.Ansys.ManualGroup('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ManualFace(self, crlFaceMaster=[], crlFaceSlave=[], strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crEdit=None, iColor=16711680):
        message = "Connections.Contacts.Ansys.ManualFace({},{},'{}',{},{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680):
        message = "Connections.Contacts.Ansys.ContactGroupByMatrix('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace=[], strName="ContactAnsys_1", iMethod=3, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crEdit=None, iColor=16711680):
        message = "Connections.Contacts.Ansys.ContactShareFace({},'{}',{},{},{},{},{},{})".format(crlShareFace, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName="ContactAnsys_1", iMethod=1, iType=0, iContactAlgorithm=0, ansysContact=ANSYS_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680):
        message = "Connections.Contacts.Ansys.ContactTable('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Contacts_MSCNastran:
    def ManualGroup(self, strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1):
        message = "Connections.Contacts.MSCNastran.ManualGroup('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1):
        message = "Connections.Contacts.MSCNastran.ContactGroupByMatrix('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ManualFace(self, crlFaceMaster=[], crlFaceSlave=[], strName="ContactMSCNastran", nastranContact=NASTRAN_CONTACT(), crEdit=None, iColor=65280, iMethod=0):
        message = "Connections.Contacts.MSCNastran.ManualFace({},{},'{}','{}',{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace=[], strName="", nastranContact=NASTRAN_CONTACT(), crEdit=None, iColor=65280, iMethod=3):
        message = "Connections.Contacts.MSCNastran.ContactShareFace({},'{}','{}',{},{},{})".format(crlShareFace, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName="", nastranContact=NASTRAN_CONTACT(), crplTarget=[], crEdit=None, iColor=65280, iMethod=1):
        message = "Connections.Contacts.MSCNastran.ContactTable('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Contacts_NXNastran:
    def ManualFace(self, crlFaceMaster=[], crlFaceSlave=[], strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=0, crEdit=None):
        message = "Connections.Contacts.NXNastran.ManualFace({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace=[], strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=3, crEdit=None):
        message = "Connections.Contacts.NXNastran.ContactShareFace({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlShareFace, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName="", iType=0, iAlg=0, dNorPenFactor=0, dTanPenFactor=0, dForceConTol=0, dMaxForceIter=0, dMaxStaIter=0, dChangeNum=0, dMinContactPer=0, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=0, dMinSearDist=0, dMaxSearDist=0, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, crplTargetPair=[], crEdit=None, iColor=0, iMethod=1):
        message = "Connections.Contacts.NXNastran.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iType, iAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, crplTargetPair, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, crFaceMaster=None, crFaceSlave=None, strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=0, crEdit=None):
        message = "Connections.Contacts.NXNastran.ManualGroup({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crFaceMaster, crFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, crFaceMaster=None, crFaceSlave=None, strName="ContactNXNastran_1", iContactType=0, iContactAlg=0, dNorPenFactor=10, dTanPenFactor=1, dForceConTol=0.01, dMaxForceIter=10, dMaxStaIter=20, dChangeNum=0.02, dMinContactPer=100, iShellThickness=0, iContactStatus=0, iInitGapPenetra=0, iRegionRefine=0, iEvaluPts=1, dMinSearDist=0, dMaxSearDist=0.01, dFricCoef=0, dSearchDist=0, dPenatlyFactor=0, iShellOffset=0, iColor=0, iMethod=0, crEdit=None):
        message = "Connections.Contacts.NXNastran.ContactGroupByMatrix({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crFaceMaster, crFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

class Contacts_TSSolver:
    def ManualFace(self, strName="ContactTSSolver_1", nastranContact=TSSOLVER_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680, iMethod=0):
        message = "Connections.Contacts.TSSolver.ManualFace('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def Auto(self, strlNames, crllMasterFaceTargets, crllSlaveFaceTargets, crlContactTypes=[1], dlInterferenceClosures=[1.0], dlFrictionCoefficients=[DFLT_DBL], blInitialAdjustments=[False], crlColors=[65280], crlEdit=[], crlMasterGroup=[], crlSlaveGroup=[]):
        message = "Connections.Contacts.TSSolver.Auto('{}',{},{},{},{},{},{},{},{},{},{})".format(strlNames, crllMasterFaceTargets, crllSlaveFaceTargets, crlContactTypes, dlInterferenceClosures, dlFrictionCoefficients, blInitialAdjustments, crlColors, crlEdit, crlMasterGroup, crlSlaveGroup)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName="ContactTSSolver_1", tssolverContact=TSSOLVER_CONTACT(), crplTarget=[], crEdit=None, iColor=16711680, iMethod=0):
        message = "Connections.Contacts.TSSolver.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Contacts_TSSS:
    def ManualFace(self, crlFaceMaster=[], crlFaceSlave=[], strName="ContactTS_SS_1", nastranContact=SUNSHINE_CONTACT(), crEdit=None, iColor=0, iMethod=0):
        message = "Connections.Contacts.TSSS.ManualFace({},{},'{}','{}',{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName="ContactTS_SS_1", tssolverContact=SUNSHINE_CONTACT(), crplTarget=[], crEdit=None, iColor=0, iMethod=1):
        message = "Connections.Contacts.TSSS.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName="ContactTS_SS_1", nastranContact=SUNSHINE_CONTACT(), crplTarget=[], crEdit=None, iColor=0, iMethod=1):
        message = "Connections.Contacts.TSSS.ContactTable('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class MPC_Equation:
    def MultiNodes(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.Equation.MultiNodes('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def TwoFace(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.Equation.TwoFace('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def SemiAuto(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.Equation.SemiAuto('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class MPC_General:
    def NodeToNode(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.General.NodeToNode('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodeToEdges(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.General.NodeToEdges('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodeToFaces(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.General.NodeToFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def TwoEdges(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.General.TwoEdges('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def FacesToFaces(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.General.FacesToFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodesToNodes(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.General.NodesToNodes('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def TwoFaces(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.General.TwoFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodeToAny(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.General.NodeToAny('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodesWithTolerance(self, strName="MPC_1", crlMaster=[], crlSlave=[], listMpcConnection=[], dSearchTol=0.0, dValue=0.0, iMPCType=0, iSearchType=1, iCoordSys=0, bUpdateDispCS=True, crEdit=None):
        message = "Connections.MPC.General.NodesWithTolerance('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class RigidElements_RBar:
    def OneToOne(self, strName="RBAR_1", crlMasterTarget=[], crlSlaveTarget=[], iMethod=17, iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None):
        message = "Connections.RigidElements.RBar.OneToOne('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

    def OneToMany(self, strName="RBAR_1", crlMasterTarget=[], crlSlaveTarget=[], iMethod=16, iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None):
        message = "Connections.RigidElements.RBar.OneToMany('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

    def OneToOneNodesWithTolerance(self, strName="RBAR_1", crlMasterTarget=[], crlSlaveTarget=[], iMethod=21, iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None):
        message = "Connections.RigidElements.RBar.OneToOneNodesWithTolerance('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

class RigidElements_RBE2:
    def OneToMany(self, iMethod=16, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0):
        message = "Connections.RigidElements.RBE2.OneToMany({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iEnableUpdateDispCS, iEnableCornerOnly, iEnableCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def OneToOne(self, iMethod=17, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0):
        message = "Connections.RigidElements.RBE2.OneToOne({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iEnableUpdateDispCS, iEnableCornerOnly, iEnableCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def OneToOneNodesWithTolerance(self, iMethod=21, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0):
        message = "Connections.RigidElements.RBE2.OneToOneNodesWithTolerance({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iEnableUpdateDispCS, iEnableCornerOnly, iEnableCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def ToCenter(self, iMethod=18, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0):
        message = "Connections.RigidElements.RBE2.ToCenter({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iEnableUpdateDispCS, iEnableCornerOnly, iEnableCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def ToCircleCenter(self, iMethod=19, crlMasterTarget=[], crlSlaveTarget=[], iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iEnableCheckDulplicate=1, iDuplicateMode=0):
        message = "Connections.RigidElements.RBE2.ToCircleCenter({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iEnableUpdateDispCS, iEnableCornerOnly, iEnableCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

class RigidElements_RBE3:
    def OneToMany(self, iMethod=16, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False):
        message = "Connections.RigidElements.RBE3.OneToMany({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRbe3TermConnection, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iEnableUpdateDispCS, iEnableCornerOnly)
        return JPT_RUN_LINE(message)

    def OneToOne(self, iMethod=17, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False):
        message = "Connections.RigidElements.RBE3.OneToOne({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRbe3TermConnection, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iEnableUpdateDispCS, iEnableCornerOnly)
        return JPT_RUN_LINE(message)

    def ToCenter(self, iMethod=18, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False):
        message = "Connections.RigidElements.RBE3.ToCenter({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRbe3TermConnection, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iEnableUpdateDispCS, iEnableCornerOnly)
        return JPT_RUN_LINE(message)

    def ToCircleCenter(self, iMethod=19, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=True, iEnableCornerOnly=False):
        message = "Connections.RigidElements.RBE3.ToCircleCenter({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRbe3TermConnection, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iEnableUpdateDispCS, iEnableCornerOnly)
        return JPT_RUN_LINE(message)

class Spring_Nodeswithtolerance:
    def sameDoFs(self, iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None):
        message = "Connections.SpringsDampers.Spring.Nodeswithtolerance.sameDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def differentDoFs(self, iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None):
        message = "Connections.SpringsDampers.Spring.Nodeswithtolerance.differentDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class Spring_OneToOne:
    def sameDoFs(self, iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None):
        message = "Connections.SpringsDampers.Spring.OneToOne.sameDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def differentDoFs(self, iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None):
        message = "Connections.SpringsDampers.Spring.OneToOne.differentDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class SpringsDampers_Damper:
    def AnyEntities11DoFS(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys=None, iGround=0, dTolerance=0.0, vecTDamper=[0, 0, 0], vecRDamper=[0, 0, 0], crEdit=None, bUpdateDispCS=True):
        message = "Connections.SpringsDampers.Damper.AnyEntities11DoFS({},'{}',{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iGround, dTolerance, vecTDamper, vecRDamper, crEdit, bUpdateDispCS)
        return JPT_RUN_LINE(message)

class SpringsDampers_Bush:
    def TwoNodes(self, iMethod=1, strName="BUSH_1", crlMaster=[], crlSlave=[], crCoord=None, dTol=DFLT_DBL, iGround=0, iOriMode=0, iEqual=1, poslVector=[], dlStiffness=[], dlDampCoef=[], dlDampConst=[], dRotStrain=DFLT_DBL, dTransStrain=DFLT_DBL, dRotStress=DFLT_DBL, dTransStress=DFLT_DBL, crEditObj=None):
        message = "Connections.SpringsDampers.Bush.TwoNodes({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

    def AnyEntities(self, iMethod=16, strName="BUSH_1", crlMaster=[], crlSlave=[], crCoord=None, dTol=DFLT_DBL, iGround=0, iOriMode=0, iEqual=1, poslVector=[], dlStiffness=[], dlDampCoef=[], dlDampConst=[], dRotStrain=DFLT_DBL, dTransStrain=DFLT_DBL, dRotStress=DFLT_DBL, dTransStress=DFLT_DBL, crEditObj=None):
        message = "Connections.SpringsDampers.Bush.AnyEntities({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

    def OnetoOne(self, iMethod=21, strName="BUSH_1", crlMaster=[], crlSlave=[], crCoord=None, dTol=DFLT_DBL, iGround=0, iOriMode=0, iEqual=1, poslVector=[], dlStiffness=[], dlDampCoef=[], dlDampConst=[], dRotStrain=DFLT_DBL, dTransStrain=DFLT_DBL, dRotStress=DFLT_DBL, dTransStress=DFLT_DBL, crEditObj=None):
        message = "Connections.SpringsDampers.Bush.OnetoOne({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

class SpringsDampers_Spring:
    def GroundedSpring(self, iMethod=0, strName="SPRING", crlMasterTarget=[], crlSlaveTarget=[], crCoordSys=None, iSpringType=0, iGround=0, dTolerance=0.0, iDirection=0, iDistributeMode=0, iDof1=0, iDof2=0, dDampCoef=DFLT_DBL, dStressCoef=DFLT_DBL, posTStiffness=[0,0,0], posRStiffness=[0,0,0], bUpdateDispCS=True, crEdit=None):
        message = "Connections.SpringsDampers.Spring.GroundedSpring({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    Nodeswithtolerance = Spring_Nodeswithtolerance()

    OneToOne = Spring_OneToOne()

class Connections_Pretension:
    def General(self, strName="BoltLoad001", iDir=0, dValue=DFLT_DBL, bFixLength=False, crTable=None, crCoord=None, iLocalUnit=0, crlTarget=[], crEdit=None, bCreate2ADVCStatic=False):
        message = "Connections.Pretension.General('{}',{},{},{},{},{},{},{},{},{})".format(strName, iDir, dValue, bFixLength, crTable, crCoord, iLocalUnit, crlTarget, crEdit, bCreate2ADVCStatic)
        return JPT_RUN_LINE(message)

    def Abaqus(self, strName="PreTensionAbaqus1", bFixedLenght=False, crTable=None, dValue=DFLT_DBL, iLocalUnit=0, strNormal="", dlNodePos=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crEdit=None, crlTarget=[]):
        message = "Connections.Pretension.Abaqus('{}',{},{},{},{},'{}',{},{},{})".format(strName, bFixedLenght, crTable, dValue, iLocalUnit, strNormal, dlNodePos, crEdit, crlTarget)
        return JPT_RUN_LINE(message)

    def Advc(self, strName="PreTensionAdvc1", bFixedLength=False, crEnforcedVelocity=None, dDvalue=0.0, iDirUpdateType=0, dlVnormal=[0,0,0], dlCtrolNodePos=[0,0,0], iRefNodeId=0, crEdit=None, crlTarget=[]):
        message = "Connections.Pretension.Advc('{}',{},{},{},{},{},{},{},{},{})".format(strName, bFixedLength, crEnforcedVelocity, dDvalue, iDirUpdateType, dlVnormal, dlCtrolNodePos, iRefNodeId, crEdit, crlTarget)
        return JPT_RUN_LINE(message)

class Connections_BoltConnections:
    Edge = BoltConnections_Edge()

    Face = BoltConnections_Face()

class Connections_Contacts:
    Abaqus = Contacts_Abaqus()

    ADVC = Contacts_ADVC()

    Ansys = Contacts_Ansys()

    MSCNastran = Contacts_MSCNastran()

    NXNastran = Contacts_NXNastran()

    TSSolver = Contacts_TSSolver()

    TSSS = Contacts_TSSS()

    def CheckPattern(self, crlPart=[], bShowMismatch=False, bShowMatch=True, dTol=0.01):
        message = "Connections.Contacts.CheckPattern({},{},{},{})".format(crlPart, bShowMismatch, bShowMatch, dTol)
        return JPT_RUN_LINE(message)

    def NXNastranGeneral(self, strName="", iPiType=0, iPiAlg=0, dPdNorPenFactor=0, dPdTanPenFactor=0, dPdForceConTol=0, dPdMaxForceIter=0, dPdMaxStaIter=0, dPdChangeNum=0, dPdMinContactPer=0, iPiShellThickness=0, iPiContactStatus=0, iPiInitGapPenetra=0, iPiRegionRefine=0, iPiEvaluPts=0, dPdMinSearDist=0, dPdMaxSearDist=0, dPdFricCoef=0, dPdSearchDist=0, dPdPenatlyFactor=0, iPiShellOffset=0, crlTarget=[], crEdit=None, iColor=0, iMethod=0):
        message = "Connections.Contacts.NXNastranGeneral('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPiType, iPiAlg, dPdNorPenFactor, dPdTanPenFactor, dPdForceConTol, dPdMaxForceIter, dPdMaxStaIter, dPdChangeNum, dPdMinContactPer, iPiShellThickness, iPiContactStatus, iPiInitGapPenetra, iPiRegionRefine, iPiEvaluPts, dPdMinSearDist, dPdMaxSearDist, dPdFricCoef, dPdSearchDist, dPdPenatlyFactor, iPiShellOffset, crlTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ExportCheckReport(self, strFullPath, dZoomFactor=1.2, iFitBy=0, iListBy=0, iListOrder=0, iFormat=0):
        message = "Connections.Contacts.ExportCheckReport('{}',{},{},{},{},{})".format(strFullPath, dZoomFactor, iFitBy, iListBy, iListOrder, iFormat)
        return JPT_RUN_LINE(message)

class Connections_Gaps:
    def TwoNodes(self, crlMaster=[], crlSlave=[], iMethod=1, iOriMode=0, crCoord=None, strName="", dU0=DFLT_DBL, dF0=DFLT_DBL, dKa=DFLT_DBL, dKb=DFLT_DBL, dKt=DFLT_DBL, dMar=DFLT_DBL, dMu1=DFLT_DBL, dMu2=DFLT_DBL, dlOriVec=[], dTmax=DFLT_DBL, dTol=DFLT_DBL, dTrmin=DFLT_DBL, crEditCur=None):
        message = "Connections.Gaps.TwoNodes({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

    def TwoEdges(self, crlMaster=[], crlSlave=[], iMethod=2, iOriMode=0, crCoord=None, strName="", dU0=DFLT_DBL, dF0=DFLT_DBL, dKa=DFLT_DBL, dKb=DFLT_DBL, dKt=DFLT_DBL, dMar=DFLT_DBL, dMu1=DFLT_DBL, dMu2=DFLT_DBL, dlOriVec=[], dTmax=DFLT_DBL, dTol=DFLT_DBL, dTrmin=DFLT_DBL, crEditCur=None):
        message = "Connections.Gaps.TwoEdges({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

    def TwoFaces(self, crlMaster=[], crlSlave=[], iMethod=3, iOriMode=0, crCoord=None, strName="", dU0=DFLT_DBL, dF0=DFLT_DBL, dKa=DFLT_DBL, dKb=DFLT_DBL, dKt=DFLT_DBL, dMar=DFLT_DBL, dMu1=DFLT_DBL, dMu2=DFLT_DBL, dlOriVec=[], dTmax=DFLT_DBL, dTol=DFLT_DBL, dTrmin=DFLT_DBL, crEditCur=None):
        message = "Connections.Gaps.TwoFaces({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

class Connections_MPC:
    Equation = MPC_Equation()

    General = MPC_General()

class Connections_RigidElements:
    RBar = RigidElements_RBar()

    RBE2 = RigidElements_RBE2()

    RBE3 = RigidElements_RBE3()

    def RBarGeneral(self, rbarConnection=RBAR_CONNECTION(), crlMasterTarget=[], crlSlaveTarget=[], iUlDOFs=0, dTol=DFLT_DBL, crCoord=None, crEdit=None):
        message = "Connections.RigidElements.RBarGeneral({},{},{},{},{},{},{})".format(rbarConnection, crlMasterTarget, crlSlaveTarget, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

    def RBE2General(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType=2, strName="RBE2_1", crCoordSys=None, dTolerance=0.0, iUlDOFs=63, dlVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, iEnableUpdateDispCS=1, iEnableCornerOnly=0, iDuplicateMode=-1):
        message = "Connections.RigidElements.RBE2General({},{},{},{},'{}',{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iEnableUpdateDispCS, iEnableCornerOnly, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def RBE3General(self, iMethod=0, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, posVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, bUpdateDispCS=True, bCornerOnly=False):
        message = "Connections.RigidElements.RBE3General({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRbe3TermConnection, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly)
        return JPT_RUN_LINE(message)

class Connections_SpringsDampers:
    Damper = SpringsDampers_Damper()

    def BushGeneral(self, iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj):
        message = "Connections.SpringsDampers.BushGeneral({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

    Bush = SpringsDampers_Bush()

    Spring = SpringsDampers_Spring()

class Designer_LBC:
    def TemperatureLoad(self, strName="", iDnType=0, dFTemp=0, strDstrFilePathName="", crDcrTable=None, crlTarget=[], crEdit=None, bDbUseAsMaterialReferenceTemp=False):
        message = "Designer.LBC.TemperatureLoad('{}',{},{},'{}',{},{},{},{})".format(strName, iDnType, dFTemp, strDstrFilePathName, crDcrTable, crlTarget, crEdit, bDbUseAsMaterialReferenceTemp)
        return JPT_RUN_LINE(message)

class Designer_Load:
    def Moment(self, strName="", crlFace=[], dlVecMomentXYZ=[0.0,0.0,0.0], crCoord=None, crEdit=None):
        message = "Designer.Load.Moment('{}',{},{},{},{})".format(strName, crlFace, dlVecMomentXYZ, crCoord, crEdit)
        return JPT_RUN_LINE(message)

class ExManifoldModeling_SZ:
    def WeldLine2(self, crlFace, crlPart, dLayerWidth, iLayerNumber):
        message = "ExManifoldModeling.SZ.WeldLine2({},{},{},{})".format(crlFace, crlPart, dLayerWidth, iLayerNumber)
        return JPT_RUN_LINE(message)

class Geometry_Bar:
    def TwoNodes(self, strPartName="Bar_1", iMeshCount=5, crStartNode=None, crEndNode=None):
        message = "Geometry.Bar.TwoNodes('{}',{},{},{})".format(strPartName, iMeshCount, crStartNode, crEndNode)
        return JPT_RUN_LINE(message)

    def Arc(self, crlNode, crPart=None, strBarName=""):
        message = "Geometry.Bar.Arc({},{},'{}')".format(crlNode, crPart, strBarName)
        return JPT_RUN_LINE(message)

    def Spline(self, crlNode, crPart=None, strBarName=""):
        message = "Geometry.Bar.Spline({},{},'{}')".format(crlNode, crPart, strBarName)
        return JPT_RUN_LINE(message)

class Geometry_BodyCut:
    def XXYYOnOnePoint(self, crPart, posCutPos=[0,0,0], iType=0, dOffset=0.0, bSplit=False, bSectionFace=True, bShateFace=False, crLocalCoor=None):
        message = "Geometry.BodyCut.XXYYOnOnePoint({},{},{},{},{},{},{},{})".format(crPart, posCutPos, iType, dOffset, bSplit, bSectionFace, bShateFace, crLocalCoor)
        return JPT_RUN_LINE(message)

    def BySurface(self, crlPart, crCutter, bSplitOnly=False, bMakeSectionFace=True, bShareFace=False, bSeparateFace=False):
        message = "Geometry.BodyCut.BySurface({},{},{},{},{},{})".format(crlPart, crCutter, bSplitOnly, bMakeSectionFace, bShareFace, bSeparateFace)
        return JPT_RUN_LINE(message)

    def By3Points(self, crPart=None, poslPosition=[], dOffset=0.0, bSplitonly=False, bMakesectionface=True, bShareface=False):
        message = "Geometry.BodyCut.By3Points({},{},{},{},{},{})".format(crPart, poslPosition, dOffset, bSplitonly, bMakesectionface, bShareface)
        return JPT_RUN_LINE(message)

class Geometry_BreakEntity:
    def StlPart(self, crlPart=[], iMinNoOfFaces=0, iMethod=0):
        message = "Geometry.BreakEntity.StlPart({},{},{})".format(crlPart, iMinNoOfFaces, iMethod)
        return JPT_RUN_LINE(message)

    def Face(self, crlFace):
        message = "Geometry.BreakEntity.Face({})".format(crlFace)
        return JPT_RUN_LINE(message)

    def Edge(self, crlPart=[], crlFace=[], crlEdge=[], crlNode=[], bAutoByAngle=False, dEdgeAngle=60.0):
        message = "Geometry.BreakEntity.Edge({},{},{},{},{},{})".format(crlPart, crlFace, crlEdge, crlNode, bAutoByAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def Part(self, crlPart=[]):
        message = "Geometry.BreakEntity.Part({})".format(crlPart)
        return JPT_RUN_LINE(message)

class Geometry_DeleteEntity:
    def Part(self, crlPart):
        message = "Geometry.DeleteEntity.Part({})".format(crlPart)
        return JPT_RUN_LINE(message)

    def Edge(self, crlEdge=[]):
        message = "Geometry.DeleteEntity.Edge({})".format(crlEdge)
        return JPT_RUN_LINE(message)

    def Vertex(self, crlVertex=[]):
        message = "Geometry.DeleteEntity.Vertex({})".format(crlVertex)
        return JPT_RUN_LINE(message)

    def Face(self, crlFace=[], bKeepSolid=True):
        message = "Geometry.DeleteEntity.Face({},{})".format(crlFace, bKeepSolid)
        return JPT_RUN_LINE(message)

class Geometry_Edge:
    def Line(self, poslPositions, crlTargetFace, bBreakFace=True):
        message = "Geometry.Edge.Line({},{},{})".format(poslPositions, crlTargetFace, bBreakFace)
        return JPT_RUN_LINE(message)

    def Spline(self, veclAprroxiPositions, crlTargetFace, bBreakFace=True):
        message = "Geometry.Edge.Spline({},{},{})".format(veclAprroxiPositions, crlTargetFace, bBreakFace)
        return JPT_RUN_LINE(message)

    def PlanarLine(self, veclPosition, crlTargetFace, crLocalCoord=None, iType=0, bBreakFace=True):
        message = "Geometry.Edge.PlanarLine({},{},{},{},{})".format(veclPosition, crlTargetFace, crLocalCoord, iType, bBreakFace)
        return JPT_RUN_LINE(message)

    def Circle(self, veclPositions, crlTargetFace, dInRadius=1, dOutRadius=4, iNoOfLayer=1, iNoOfDiv=30, bBreakFace=True):
        message = "Geometry.Edge.Circle({},{},{},{},{},{},{})".format(veclPositions, crlTargetFace, dInRadius, dOutRadius, iNoOfLayer, iNoOfDiv, bBreakFace)
        return JPT_RUN_LINE(message)

    def PerpendicularLineOfEdge(self, crlNode, crlFace, dOffset=0, bReakFace=True):
        message = "Geometry.Edge.PerpendicularLineOfEdge({},{},{},{})".format(crlNode, crlFace, dOffset, bReakFace)
        return JPT_RUN_LINE(message)

    def ExtendLine(self, crlEdge, iMethod=0, iEnd=0, iNoFittingPoints=3, iDiv=2, iEnableBreakFace=1):
        message = "Geometry.Edge.ExtendLine({},{},{},{},{},{})".format(crlEdge, iMethod, iEnd, iNoFittingPoints, iDiv, iEnableBreakFace)
        return JPT_RUN_LINE(message)

    def ElementEdges(self, crplElemEdge, bBreakEdge=True):
        message = "Geometry.Edge.ElementEdges({},{})".format(crplElemEdge, bBreakEdge)
        return JPT_RUN_LINE(message)

    def Angle(self, crpPair, dAngle=135.0, bCurvature=False, bBreakFace=True):
        message = "Geometry.Edge.Angle({},{},{},{})".format(crpPair, dAngle, bCurvature, bBreakFace)
        return JPT_RUN_LINE(message)

    def NodeShortestPath(self, crFirstNode, crSecondNode, iEnableBreakFace=1):
        message = "Geometry.Edge.NodeShortestPath({},{},{})".format(crFirstNode, crSecondNode, iEnableBreakFace)
        return JPT_RUN_LINE(message)

    def OffsetLine(self, crlFace=[], crlEdge=[], bBreakFace=True, dOffsetDistance=0.0, iNumberLayer=1, bMerge=True, bExtend=True, iLayerMethod=0, dlVlayerOffset=[], bAutoCollapse=False, iRLType=2):
        message = "Geometry.Edge.OffsetLine({},{},{},{},{},{},{},{},{},{},{})".format(crlFace, crlEdge, bBreakFace, dOffsetDistance, iNumberLayer, bMerge, bExtend, iLayerMethod, dlVlayerOffset, bAutoCollapse, iRLType)
        return JPT_RUN_LINE(message)

    def SplineFreeEdges(self, crlNode, iEnableArc=0, crPart=None, strBarName=""):
        message = "Geometry.Edge.SplineFreeEdges({},{},{},'{}')".format(crlNode, iEnableArc, crPart, strBarName)
        return JPT_RUN_LINE(message)

    def ClosedLine(self, veclPositions, crlTargetFace, iEnableBreakFace=1):
        message = "Geometry.Edge.ClosedLine({},{},{})".format(veclPositions, crlTargetFace, iEnableBreakFace)
        return JPT_RUN_LINE(message)

    def PerpendicularCylinderLine(self, crlNode=[], crlFace=[], iMethod=0, dOffset=0.0, bOppositeSide=False, bBreakFace=True):
        message = "Geometry.Edge.PerpendicularCylinderLine({},{},{},{},{},{})".format(crlNode, crlFace, iMethod, dOffset, bOppositeSide, bBreakFace)
        return JPT_RUN_LINE(message)

    def IntersectionLine(self, crlFaces=[], bBreakFace=True):
        message = "Geometry.Edge.IntersectionLine({},{})".format(crlFaces, bBreakFace)
        return JPT_RUN_LINE(message)

    def ProjectLine(self, crlEdge=[], crlFaces=[], crlNode=[], bBreakFace=True, iType=0, bCheckGap=False, dGap=0.0):
        message = "Geometry.Edge.ProjectLine({},{},{},{},{},{},{})".format(crlEdge, crlFaces, crlNode, bBreakFace, iType, bCheckGap, dGap)
        return JPT_RUN_LINE(message)

    def PerpendicularLineToEdge(self, crNode=None, crEdge=None, crlFace=[], bBreakFace=True):
        message = "Geometry.Edge.PerpendicularLineToEdge({},{},{},{})".format(crNode, crEdge, crlFace, bBreakFace)
        return JPT_RUN_LINE(message)

class Geometry_ExtractSurfaces:
    def ExtractRefSurface(self, listFace, dAngle=60.0, strName="ExtractFace_1", isMergePart=False):
        message = "Geometry.ExtractSurfaces.ExtractRefSurface({},{},'{}',{})".format(listFace, dAngle, strName, isMergePart)
        return JPT_RUN_LINE(message)

    def ExtractSurfaces(self, crlFace, dAngle=60.0, strName="ExtractFace_1", bMergePart=False):
        message = "Geometry.ExtractSurfaces.ExtractSurfaces({},{},'{}',{})".format(crlFace, dAngle, strName, bMergePart)
        return JPT_RUN_LINE(message)

class Geometry_Face:
    def FourEdges(self, crlEdge):
        message = "Geometry.Face.FourEdges({})".format(crlEdge)
        return JPT_RUN_LINE(message)

    def FromMesh(self, crlFace):
        message = "Geometry.Face.FromMesh({})".format(crlFace)
        return JPT_RUN_LINE(message)

    def CreateSmoothFace(self, bInterPoration, crlTarget, iElemGeneration, dGradation, iEnableFaceSmooth, crTargetPart):
        message = "Geometry.Face.CreateSmoothFace({},{},{},{},{},{})".format(bInterPoration, crlTarget, iElemGeneration, dGradation, iEnableFaceSmooth, crTargetPart)
        return JPT_RUN_LINE(message)

    def Edges(self, crlEdge, crlPart=[], crlNode=[], bSharedFace=False, bSmoothFace=False, bCreatePart=False, bImproved=False, bBarsOnly=False, bOnlyOnePart=True, bUseMidNodes=False):
        message = "Geometry.Face.Edges({},{},{},{},{},{},{},{},{},{})".format(crlEdge, crlPart, crlNode, bSharedFace, bSmoothFace, bCreatePart, bImproved, bBarsOnly, bOnlyOnePart, bUseMidNodes)
        return JPT_RUN_LINE(message)

    def Elements(self, crlElem, bShareFace=False):
        message = "Geometry.Face.Elements({},{})".format(crlElem, bShareFace)
        return JPT_RUN_LINE(message)

class Geometry_FindFeature:
    def DelCircChamfer(self, crlPart, dMaxThick=0.1, dMinThick=2):
        message = "Geometry.FindFeature.DelCircChamfer({},{},{})".format(crlPart, dMaxThick, dMinThick)
        return JPT_RUN_LINE(message)

    def Fillet(self, crlPart=[], crlFace=[], dMinAngle=1.0, dMaxAngle=10.0, dMinFaceWidth=1.0, dMaxFaceWidth=10.0, dMinCurveRadius=0.0, dMaxCurveRadius=171, dScale=1.0):
        message = "Geometry.FindFeature.Fillet({},{},{},{},{},{},{},{},{})".format(crlPart, crlFace, dMinAngle, dMaxAngle, dMinFaceWidth, dMaxFaceWidth, dMinCurveRadius, dMaxCurveRadius, dScale)
        return JPT_RUN_LINE(message)

    def Faces(self, crlPart=[],iOption=0, crlEdge=[], bCylinder=True, bDisc=False, bFourCorners=True, dMinThickness=0.1, dMaxThickness=2.0, dDiameterMin=1.0, dDiameterMax=2.0, crlFace=[]):
        message = "Geometry.FindFeature.Faces({},{},{},{},{},{},{},{},{},{},{})".format(crlPart,iOption, crlEdge, bCylinder, bDisc, bFourCorners, dMinThickness, dMaxThickness, dDiameterMin, dDiameterMax, crlFace)
        return JPT_RUN_LINE(message)

    def Edges(self, crlPart=[],iOption=0, crlEdge=[], bCylinder=True, bDisc=False, bFourCorners=True, dMinThickness=0.1, dMaxThickness=2.0, dDiameterMin=1.0, dDiameterMax=2.0, crlFace=[]):
        message = "Geometry.FindFeature.Edges({},{},{},{},{},{},{},{},{},{},{})".format(crlPart,iOption, crlEdge, bCylinder, bDisc, bFourCorners, dMinThickness, dMaxThickness, dDiameterMin, dDiameterMax, crlFace)
        return JPT_RUN_LINE(message)

class Geometry_MergeEntities:
    def Faces(self, crlFace=[], bMergeEdge=True, bRemoveNonBoundEdge=True):
        message = "Geometry.MergeEntities.Faces({},{},{})".format(crlFace, bMergeEdge, bRemoveNonBoundEdge)
        return JPT_RUN_LINE(message)

    def TinyFacesMerge(self, crlPart=[], crlFace=[], dMinFaceWidth=0.0, dMaxFaceWidth=0.001, dFaceAngle=30, bReferLocalSetting=False, bConnectFace=False):
        message = "Geometry.MergeEntities.TinyFacesMerge({},{},{},{},{},{},{})".format(crlPart, crlFace, dMinFaceWidth, dMaxFaceWidth, dFaceAngle, bReferLocalSetting, bConnectFace)
        return JPT_RUN_LINE(message)

    def CBarParts(self, crlCBarPart=[]):
        message = "Geometry.MergeEntities.CBarParts({})".format(crlCBarPart)
        return JPT_RUN_LINE(message)

    def Edges(self, crlEdge=[]):
        message = "Geometry.MergeEntities.Edges({})".format(crlEdge)
        return JPT_RUN_LINE(message)

    def Parts(self, dTolerance=1e-5, bRemovesharefaceflag=True, crlPart=[]):
        message = "Geometry.MergeEntities.Parts({},{},{})".format(dTolerance, bRemovesharefaceflag, crlPart)
        return JPT_RUN_LINE(message)

    def PartFaces(self, crlPart=[], crlFace=[], bAngle=True, dTolAngle=20, bWidth=True, dTolWidth=0.2):
        message = "Geometry.MergeEntities.PartFaces({},{},{},{},{},{})".format(crlPart, crlFace, bAngle, dTolAngle, bWidth, dTolWidth)
        return JPT_RUN_LINE(message)

class Geometry_Part:
    def Cube(self, dlOrigin=[0, 0, 0], dlLength=[0.01, 0.01, 0.01], ilNodeCnt=[10, 10, 10], strPartName="Cube_1", iColorPart=7105764, crCoord=None):
        message = "Geometry.Part.Cube({},{},{},'{}',{},{})".format(dlOrigin, dlLength, ilNodeCnt, strPartName, iColorPart, crCoord)
        return JPT_RUN_LINE(message)

    def Wedge(self, vecOrigin=[0.0, 0.0, 0.0], vecLength=[0.01, 0.01, 0.01], vecNodeCount=[10, 10, 10], strPartName="Wedge_1", iPartColor=7105764, crCoordinate=None):
        message = "Geometry.Part.Wedge({},{},{},'{}',{},{})".format(vecOrigin, vecLength, vecNodeCount, strPartName, iPartColor, crCoordinate)
        return JPT_RUN_LINE(message)

    def Sphere(self, dlOrigin=[0, 0, 0], dRadius=0.005, iLatitudeNodeCnt=20, iLongitudeNodeCnt=20, strPartName="Sphere_1", iColorPart=7105764, crCoord=None):
        message = "Geometry.Part.Sphere({},{},{},{},'{}',{},{})".format(dlOrigin, dRadius, iLatitudeNodeCnt, iLongitudeNodeCnt, strPartName, iColorPart, crCoord)
        return JPT_RUN_LINE(message)

    def Torus(self, dlOrigin=[0, 0, 0], dInnerRadius=0.015, dRingRadius=0.02, iLatitudeNodeCnt=20, iLongitudeNodeCnt=20, strPartName="Torus_1", iColorPart=7105764, crCoord=None):
        message = "Geometry.Part.Torus({},{},{},{},{},'{}',{},{})".format(dlOrigin, dInnerRadius, dRingRadius, iLatitudeNodeCnt, iLongitudeNodeCnt, strPartName, iColorPart, crCoord)
        return JPT_RUN_LINE(message)

    def Elems(self, crlElem, strPartName):
        message = "Geometry.Part.Elems({},'{}')".format(crlElem, strPartName)
        return JPT_RUN_LINE(message)

    def Cylinder(self, dlOrigin=[0,0,0], dTopRadius=0.01, dBotRadius=0.01, dHeight=0.01, iCircleNodeCnt=36, iAxisNodeCnt=10, strName="Cylinder_1", iPartCol=7105764, crCoord=None):
        message = "Geometry.Part.Cylinder({},{},{},{},{},{},'{}',{},{})".format(dlOrigin, dTopRadius, dBotRadius, dHeight, iCircleNodeCnt, iAxisNodeCnt, strName, iPartCol, crCoord)
        return JPT_RUN_LINE(message)

    def Tube(self, dlOrigin=[0,0,0], dTopInnerRadius=0.001, dTopOuterRadius=0.01, dBotInnerRadius=0.001, dBotOuterRadius=0.01, dHeight=0.01, iCircleNodeCnt=36, iAxisNodeCnt=10, strName="Cylinder_1", iPartCol=7105764, crCoord=None):
        message = "Geometry.Part.Tube({},{},{},{},{},{},{},{},'{}',{},{})".format(dlOrigin, dTopInnerRadius, dTopOuterRadius, dBotInnerRadius, dBotOuterRadius, dHeight, iCircleNodeCnt, iAxisNodeCnt, strName, iPartCol, crCoord)
        return JPT_RUN_LINE(message)

    def Trapezoid(self, dlOrigin=[0.0,0.0,0.0], dlLength=[0.01, 0.01, 0.01], dTopXLength=7.0, dRadius=0, ilNodeCnt=[10, 10, 10], strPartName="Trapezoid_1", iColorPart=7105764, crCoord=None):
        message = "Geometry.Part.Trapezoid({},{},{},{},{},'{}',{},{})".format(dlOrigin, dlLength, dTopXLength, dRadius, ilNodeCnt, strPartName, iColorPart, crCoord)
        return JPT_RUN_LINE(message)

    def Cone(self, dlOriginXyz=[0,0,0], dBottomRadius=0.01, dHeight=0.02, iCircleNodeCount=20, iAxisNodeCnt=20, strPartName="Cone_1", iPartColor=7105764, crCoordinate=None):
        message = "Geometry.Part.Cone({},{},{},{},{},'{}',{},{})".format(dlOriginXyz, dBottomRadius, dHeight, iCircleNodeCount, iAxisNodeCnt, strPartName, iPartColor, crCoordinate)
        return JPT_RUN_LINE(message)

class Geometry_ShowAdjacent:
    def Faces(self, Angle=0.0, IncludeStopFace=0, Layer=1,IsPreview=0, taStartFaceCr=[] ,taStopFaceCr=[]):
        message = "Geometry.ShowAdjacent.Faces({},{},{},{},{},{})".format(Angle, IncludeStopFace, Layer,IsPreview, taStartFaceCr,taStopFaceCr)
        return JPT_RUN_LINE(message)

    def Elements(self, Angle=0.0, IncludeStopElem=0, Layer=1,IsPreview=0, taStartElemCr=[] ,taStopElemCr=[]):
        message = "Geometry.ShowAdjacent.Elements({},{},{},{},{},{})".format(Angle, IncludeStopElem, Layer,IsPreview, taStartElemCr,taStopElemCr)
        return JPT_RUN_LINE(message)

class Geometry_Transform:
    def Rotation(self, crlPart=[], posCenter=[0,0,0], vecAxis=[1,0,0], dAngle=0, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, iCopyCount=1, bMergeNode=False, dTol=1.0e-5):
        message = "Geometry.Transform.Rotation({},{},{},{},{},{},{},{},{},{})".format(crlPart, posCenter, vecAxis, dAngle, bCreateNewPart, bCopyLBC, bCopyProperty, iCopyCount, bMergeNode, dTol)
        return JPT_RUN_LINE(message)

    def Scaling(self, crlPart, dlScaleVector=[1.0,1.0,1.0], dlScaleCentre=[0.0,0.0,0.0], crCoordinate=None, bCreateNew=False, bCopyLbc=False, bCopyProperty=False, bUsepartcenter=True):
        message = "Geometry.Transform.Scaling({},{},{},{},{},{},{},{})".format(crlPart, dlScaleVector, dlScaleCentre, crCoordinate, bCreateNew, bCopyLbc, bCopyProperty, bUsepartcenter)
        return JPT_RUN_LINE(message)

    def Mirror(self, crlPart, veclPoint=[[0.0, 0.0, 0.0]], dOffset=0.0, bCreateNewPart=True, bCopyLBC=False, bCopyProperty=False, bRemoveDupFace=True, bMergeNode=False, dTol=1e-05):
        message = "Geometry.Transform.Mirror({},{},{},{},{},{},{},{},{})".format(crlPart, veclPoint, dOffset, bCreateNewPart, bCopyLBC, bCopyProperty, bRemoveDupFace, bMergeNode, dTol)
        return JPT_RUN_LINE(message)

    def Position(self, crlPart, veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False):
        message = "Geometry.Transform.Position({},{},{},{},{})".format(crlPart, veclPoint, bCreateNewPart, bCopyLBC, bCopyProperty)
        return JPT_RUN_LINE(message)

    def Translation(self, crlPart=[], poslTranslates=[], crCoord=None, bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, iCopyCount=1):
        message = "Geometry.Transform.Translation({},{},{},{},{},{},{})".format(crlPart, poslTranslates, crCoord, bCreateNewPart, bCopyLBC, bCopyProperty, iCopyCount)
        return JPT_RUN_LINE(message)

    def MatingFace(self, crlPart=[], crSrcFace=None, crDstFace=None, crSrcEdge=None, crDstEdge=None, crSrcNode=None, crDstNode=None, iFaceOpposite=0, dEdgeAngle=0, iEdgeOpposite=0, iAlignMethodType=0, iAdjustPointType=0, iAdjustProjectionType=0, dlAlignVector=[0, 0, 0], dlAdjustPoint=[0, 0, 0], dlAdjustVector=[0, 0, 0], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False, bIsPreview=False, crlCoordSyss=[]):
        message = "Geometry.Transform.MatingFace({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, crSrcFace, crDstFace, crSrcEdge, crDstEdge, crSrcNode, crDstNode, iFaceOpposite, dEdgeAngle, iEdgeOpposite, iAlignMethodType, iAdjustPointType, iAdjustProjectionType, dlAlignVector, dlAdjustPoint, dlAdjustVector, bCreateNewPart, bCopyLBC, bCopyProperty, bIsPreview, crlCoordSyss)
        return JPT_RUN_LINE(message)

    def CylinderFace(self, crlPart, veclPoint=[[0.0, 0.0, 0.0]], bCreateNewPart=False, bCopyLBC=False, bCopyProperty=False):
        message = "Geometry.Transform.CylinderFace({},{},{},{},{})".format(crlPart, veclPoint, bCreateNewPart, bCopyLBC, bCopyProperty)
        return JPT_RUN_LINE(message)

class Groups_RightClick:
    def PropertyGroup(self, strTmp=""):
        message = "Groups.RightClick.PropertyGroup('{}')".format(strTmp)
        return JPT_RUN_LINE(message)

    def Rename(self, strNewName, crItem):
        message = "Groups.RightClick.Rename('{}',{})".format(strNewName, crItem)
        return JPT_RUN_LINE(message)

    def DeleteGroup(self, crlDelGroup, bRemoveAll=False):
        message = "Groups.RightClick.DeleteGroup({},{})".format(crlDelGroup, bRemoveAll)
        return JPT_RUN_LINE(message)

    def CopyGroup(self, crlSrc=[], strlNames=[], crDest=None, bKeep=0):
        message = "Groups.RightClick.CopyGroup({},'{}',{},{})".format(crlSrc, strlNames, crDest, bKeep)
        return JPT_RUN_LINE(message)

    def AddSupGroup(self, crSupGroupSelected=None):
        message = "Groups.RightClick.AddSupGroup({})".format(crSupGroupSelected)
        return JPT_RUN_LINE(message)

    def CreateMatGroup(self, strTmp=""):
        message = "Groups.RightClick.CreateMatGroup('{}')".format(strTmp)
        return JPT_RUN_LINE(message)

class HexModeling_Sweep:
    def Circular(self, crlFace=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0):
        message = "HexModeling.Sweep.Circular({},{},{},{},{},{},{},{},{},{})".format(crlFace, dAngle, dTol, iLayer, vecAxisPt, vecAxisVect, bInterfaceElem, bExtrusion, dTranslationExtrusion, dBDeleteOriginalParts)
        return JPT_RUN_LINE(message)

    def FaceToFace(self, crSrcFace, crDstFace, bDeleteOriginalParts=True):
        message = "HexModeling.Sweep.FaceToFace({},{},{})".format(crSrcFace, crDstFace, bDeleteOriginalParts)
        return JPT_RUN_LINE(message)

    def Layer(self, crlFace=[], dFrontWidth=0.0, dBackWidth=0.0, iFrontLayers=1, iBackLayers=0, iBaseFaceType=0, iSeparate=0):
        message = "HexModeling.Sweep.Layer({},{},{},{},{},{},{})".format(crlFace, dFrontWidth, dBackWidth, iFrontLayers, iBackLayers, iBaseFaceType, iSeparate)
        return JPT_RUN_LINE(message)

    def Linear(self, crlFace=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0):
        message = "HexModeling.Sweep.Linear({},{},{},{},{},{},{},{},{},{},{})".format(crlFace, dLength, iLayer, dlSweepDirection, bInterfaceElemFlag, iLinearMethod, bDeleteOriginalParts, bDeleteTargetParts, iMethodBias, dFactor, iProgression)
        return JPT_RUN_LINE(message)

    def Curve(self, crFace=None, crlEdge=[], crlRefEdge=[], dMeshSize=0.1):
        message = "HexModeling.Sweep.Curve({},{},{},{})".format(crFace, crlEdge, crlRefEdge, dMeshSize)
        return JPT_RUN_LINE(message)

    def FromMidPlane(self, crlPart=[], bRef=True):
        message = "HexModeling.Sweep.FromMidPlane({},{})".format(crlPart, bRef)
        return JPT_RUN_LINE(message)

class Home_ImportCAD:
    def Elysium(self, strlPath=[], dChordHeightTolerance=1.0, dAngleToleranceDegree=5.0, dPointCoincidentTolerance=0.01, iConvertIsolatedCurve=0, iDekCleanselfintersectingloop=2, iDekVolumetopart=4, iIgesFixedcurevepreference=0, iIgesAutostitch=1, dIgesStitchtolerance=0.1, iCatiaConvertnotshowedelement=0, iCatiaConvertnotshowedinstance=0, iCatiaConvertaxis=1, iStepCreateseam=1, dStepPointtolerance=0.0, iAcisHealacisbeforeversion=0, iJtConvertgeometrytype=2, bFaceColor=False, iJtConvertgeneralpart=1, iJtConvertaxis=1, iJtConvertcenterline=0):
        message = "Home.ImportCAD.Elysium('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strlPath, dChordHeightTolerance, dAngleToleranceDegree, dPointCoincidentTolerance, iConvertIsolatedCurve, iDekCleanselfintersectingloop, iDekVolumetopart, iIgesFixedcurevepreference, iIgesAutostitch, dIgesStitchtolerance, iCatiaConvertnotshowedelement, iCatiaConvertnotshowedinstance, iCatiaConvertaxis, iStepCreateseam, dStepPointtolerance, iAcisHealacisbeforeversion, iJtConvertgeometrytype, bFaceColor, iJtConvertgeneralpart, iJtConvertaxis, iJtConvertcenterline)
        return JPT_RUN_LINE(message)

    def Spatial(self, strlPath, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=20.0, dMaxFacetWidth=1000.0, bNXMultipart=True, bHealing=True, bIsNXDirect=False, bSetFaceColor=False, strCsvFilePath=""):
        message = "Home.ImportCAD.Spatial('{}',{},{},{},{},{},{},{},'{}')".format(strlPath, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, bNXMultipart, bHealing, bIsNXDirect, bSetFaceColor, strCsvFilePath)
        return JPT_RUN_LINE(message)

    def Parasolid(self, strlFiles, dChordHeightTolerance=0.0, dAngleToleranceDegree=0.0, iConvertIsolatedCurve=0, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=20.0, dMaxFacetWidth=0.1, dMinFacetWidth=0.0, bICAD=False, iVRMLColorGroups=0, dScale=1.0):
        message = "Home.ImportCAD.Parasolid('{}',{},{},{},{},{},{},{},{},{},{})".format(strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale)
        return JPT_RUN_LINE(message)

    def STL(self, strlFiles, dChordHeightTolerance=0.0, dAngleToleranceDegree=0.0, iConvertIsolatedCurve=0, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=7.0, dMaxFacetWidth=0.0, dMinFacetWidth=0.0, bICAD=False, iVRMLColorGroups=-227253959, dScale=0.001):
        message = "Home.ImportCAD.STL('{}',{},{},{},{},{},{},{},{},{},{})".format(strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale)
        return JPT_RUN_LINE(message)

    def VRML(self, strlFiles, dChordHeightTolerance=0.0, dAngleToleranceDegree=0.0, iConvertIsolatedCurve=0, dSurfacePlaneTolerance=0.0, dSufacePlaneAngle=20.0, dMaxFacetWidth=0.1, dMinFacetWidth=0.0, bICAD=False, iVRMLColorGroups=0, dScale=1.0):
        message = "Home.ImportCAD.VRML('{}',{},{},{},{},{},{},{},{},{},{})".format(strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale)
        return JPT_RUN_LINE(message)

    def ProECreoDirect(self, strlPath, dChordHeightTolerance=0.0, dAngleToleranceDegree=20.0, dStepMaxSize=0.1):
        message = "Home.ImportCAD.ProECreoDirect('{}',{},{},{})".format(strlPath, dChordHeightTolerance, dAngleToleranceDegree, dStepMaxSize)
        return JPT_RUN_LINE(message)

    def TechnoStarGeometry(self, strlPath=[], bUseUnit=True):
        message = "Home.ImportCAD.TechnoStarGeometry('{}',{})".format(strlPath, bUseUnit)
        return JPT_RUN_LINE(message)

class Home_ImportMesh:
    def ADVCADX(self, strPath, dFaceAngle=60.0, dEdgeAngle=60.0):
        message = "Home.ImportMesh.ADVCADX('{}',{},{})".format(strPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def AnsysDat(self, strlPath, dFaceAngle=60.0, dEdgeAngle=60.0):
        message = "Home.ImportMesh.AnsysDat('{}',{},{})".format(strlPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def NastranBdf(self, strlFilePaths, iImportType=2, dFaceAngle=60.0, dEdgeAngle=60.0, bReadNameComment=False, iCreateDup1DElemAnswer=-1):
        message = "Home.ImportMesh.NastranBdf('{}',{},{},{},{},{})".format(strlFilePaths, iImportType, dFaceAngle, dEdgeAngle, bReadNameComment, iCreateDup1DElemAnswer)
        return JPT_RUN_LINE(message)

    def AbaqusINP(self, strlFilePaths, dFaceAngle=60.0, dEdgeAngle=60.0, iImportType=1):
        message = "Home.ImportMesh.AbaqusINP('{}',{},{},{})".format(strlFilePaths, dFaceAngle, dEdgeAngle, iImportType)
        return JPT_RUN_LINE(message)

    def LSDYNA(self, strlPath, dFaceAngle=60.0, dEdgeAngle=60.0):
        message = "Home.ImportMesh.LSDYNA('{}',{},{})".format(strlPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def Universal(self, strPath=""):
        message = "Home.ImportMesh.Universal('{}')".format(strPath)
        return JPT_RUN_LINE(message)

    def TSVPre(self, strImportPath="", strExportPath="", ilModelIndex=None, iMerge=None):
        message = "Home.ImportMesh.TSVPre('{}','{}',{},{})".format(strImportPath, strExportPath, ilModelIndex, iMerge)
        return JPT_RUN_LINE(message)

class MainWindow_RightClick:
    def MergeFaces(self, crlFace, bIsMergeEdge=False, bRemoveNonBoundEdge=True):
        message = "MainWindow.RightClick.MergeFaces({},{},{})".format(crlFace, bIsMergeEdge, bRemoveNonBoundEdge)
        return JPT_RUN_LINE(message)

    def SelectAllParts(self, ):
        message = "MainWindow.RightClick.SelectAllParts({})".format('')
        return JPT_RUN_LINE(message)

    def AssociatedPick(self, crlInput, strTarget, strConnect="UNKNOWN"):
        message = "MainWindow.RightClick.AssociatedPick({},'{}','{}')".format(crlInput, strTarget, strConnect)
        return JPT_RUN_LINE(message)

    def FlipElement(self, crlTarget):
        message = "MainWindow.RightClick.FlipElement({})".format(crlTarget)
        return JPT_RUN_LINE(message)

class ChangeTopology_Element:
    def SurfaceElement(self, ilElement, ilFace, ilPart, iCreateNewPart):
        message = "MeshCleanup.ChangeTopology.Element.SurfaceElement({},{},{},{})".format(ilElement, ilFace, ilPart, iCreateNewPart)
        return JPT_RUN_LINE(message)

class Manual2D_MergeElement:
    def TwoQuadsToQuad(self, crlElem):
        message = "MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad({})".format(crlElem)
        return JPT_RUN_LINE(message)

    def TwoTrisToQuad(self, crlElem=[]):
        message = "MeshCleanup.Manual2D.MergeElement.TwoTrisToQuad({})".format(crlElem)
        return JPT_RUN_LINE(message)

class Manual2D_SplitElement:
    def QuadTo4Quads(self, crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo4Quads({},{},{},{},{},{},{},{})".format(crlElem, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadToTrans4Quads(self, crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0):
        message = "MeshCleanup.Manual2D.SplitElement.QuadToTrans4Quads({},{},{},{},{},{},{},{})".format(crlElem, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadToTrans3Quads(self, crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0):
        message = "MeshCleanup.Manual2D.SplitElement.QuadToTrans3Quads({},{},{},{},{},{},{},{})".format(crlElem, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo2Quads1Tri(self, crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo2Quads1Tri({},{},{},{},{},{},{},{})".format(crlElem, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo3Tris(self, crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo3Tris({},{},{},{},{},{},{},{})".format(crlElem, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo2Quads(self, crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo2Quads({},{},{},{},{},{},{},{})".format(crlElem, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo2Tris(self, crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo2Tris({},{},{},{},{},{},{},{})".format(crlElem, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadToQuadTri(self, crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0):
        message = "MeshCleanup.Manual2D.SplitElement.QuadToQuadTri({},{},{},{},{},{},{},{})".format(crlElem, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo4Tris(self, crlElem=[], crDatumNode0=None, crDatumNode1=None, iMethod=0, iAutoExecute=0, iAutoTransition=0, iCADProject=0, iMergeNode=0):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo4Tris({},{},{},{},{},{},{},{})".format(crlElem, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class Manual3D_Collapse:
    def CenterFaceCollapse(self, crlElem):
        message = "MeshCleanup.Manual3D.Collapse.CenterFaceCollapse({})".format(crlElem)
        return JPT_RUN_LINE(message)

    def HalfEdgeCollapse(self, crplElemEdge):
        message = "MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse({})".format(crplElemEdge)
        return JPT_RUN_LINE(message)

    def EdgeCollapse(self, crplElemEdge=[], crlNode=[]):
        message = "MeshCleanup.Manual3D.Collapse.EdgeCollapse({},{})".format(crplElemEdge, crlNode)
        return JPT_RUN_LINE(message)

class MeshCleanup_Element:
    def SolidElement(self, crlElem, crPart=None):
        message = "MeshCleanup.Element.SolidElement({},{})".format(crlElem, crPart)
        return JPT_RUN_LINE(message)

    def SurfaceElement(self, ilElement=[], ilFace=[], ilPart=[], iCreateNewPart=0):
        message = "MeshCleanup.Element.SurfaceElement({},{},{},{})".format(ilElement, ilFace, ilPart, iCreateNewPart)
        return JPT_RUN_LINE(message)

class MeshCleanup_ChangeTopology:
    Element = ChangeTopology_Element()

class MeshCleanup_Cleanup:
    def CloseGap(self, crlPartCur, dDistanceTol):
        message = "MeshCleanup.Cleanup.CloseGap({},{})".format(crlPartCur, dDistanceTol)
        return JPT_RUN_LINE(message)

class MeshCleanup_Manual2D:
    MergeElement = Manual2D_MergeElement()

    SplitElement = Manual2D_SplitElement()

    def Equivalence(self, crlNode, iTypeEquiva=0, dTolerance=1.0):
        message = "MeshCleanup.Manual2D.Equivalence({},{},{})".format(crlNode, iTypeEquiva, dTolerance)
        return JPT_RUN_LINE(message)

    def DeleteElement(self, crlElem, bKeepShareElem=False):
        message = "MeshCleanup.Manual2D.DeleteElement({},{})".format(crlElem, bKeepShareElem)
        return JPT_RUN_LINE(message)

    def Split(self, crplElemEdge, dRatio=0.0, crNodeRef=None, crProjectPart=None):
        message = "MeshCleanup.Manual2D.Split({},{},{},{})".format(crplElemEdge, dRatio, crNodeRef, crProjectPart)
        return JPT_RUN_LINE(message)

    def Swap(self, crplElemEdge=[]):
        message = "MeshCleanup.Manual2D.Swap({})".format(crplElemEdge)
        return JPT_RUN_LINE(message)

    def Collapse(self, crNodeRef=None, crNodeEq=None):
        message = "MeshCleanup.Manual2D.Collapse({},{})".format(crNodeRef, crNodeEq)
        return JPT_RUN_LINE(message)

    def CreateElement(self, iElemType=0, crParentEntity=None, crlNode=[]):
        message = "MeshCleanup.Manual2D.CreateElement({},{},{})".format(iElemType, crParentEntity, crlNode)
        return JPT_RUN_LINE(message)

    def RemeshElement(self, crlTarget=[], surfaceMesh=SURFACE_MESH(), bUseSetting=False, bGrading=False, bFMesher=False, iOverrideType=0, bKeepConnection=False, bProjCAD=False, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001, bIDchcek=False, bKeepRemeshEdge=False):
        message = "MeshCleanup.Manual2D.RemeshElement({},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlTarget, surfaceMesh, bUseSetting, bGrading, bFMesher, iOverrideType, bKeepConnection, bProjCAD, bTinyFaceMerge, dMinFaceWidth, dMaxFaceWidth, bIDchcek, bKeepRemeshEdge)
        return JPT_RUN_LINE(message)

class MeshCleanup_Manual3D:
    Collapse = Manual3D_Collapse()

    def DeleteNode(self, crlNode):
        message = "MeshCleanup.Manual3D.DeleteNode({})".format(crlNode)
        return JPT_RUN_LINE(message)

    def Swap(self, crplElemEdge):
        message = "MeshCleanup.Manual3D.Swap({})".format(crplElemEdge)
        return JPT_RUN_LINE(message)

    def Equivalence(self, crlNode=[], iMergeTowards=0):
        message = "MeshCleanup.Manual3D.Equivalence({},{})".format(crlNode, iMergeTowards)
        return JPT_RUN_LINE(message)

    def Split(self, crplElemEdge, crlNode=[], dRatioDistance=0.5):
        message = "MeshCleanup.Manual3D.Split({},{},{})".format(crplElemEdge, crlNode, dRatioDistance)
        return JPT_RUN_LINE(message)

    def CreateHex(self, iParentEntityId=0, crlElem=[], iSeprateN=1):
        message = "MeshCleanup.Manual3D.CreateHex({},{},{})".format(iParentEntityId, crlElem, iSeprateN)
        return JPT_RUN_LINE(message)

    def CreatePenta(self, iParentEntityId=0, crlElem=[]):
        message = "MeshCleanup.Manual3D.CreatePenta({},{})".format(iParentEntityId, crlElem)
        return JPT_RUN_LINE(message)

    def CreateTetra(self, iParentEntityId=0, crlNode=[], crlElem=[]):
        message = "MeshCleanup.Manual3D.CreateTetra({},{},{})".format(iParentEntityId, crlNode, crlElem)
        return JPT_RUN_LINE(message)

class MeshCleanup_ManualCheck:
    def Tri(self, crlPart=[], nElemType=0, veQuality=0, nCheckCondition=0, dLimitValue=0.0, CFLValue=0.0, nNonManifold=0, nCleanupMode=0, crlElem=[]):
        message = "MeshCleanup.ManualCheck.Tri({},{},{},{},{},{},{},{},{})".format(crlPart, nElemType, veQuality, nCheckCondition, dLimitValue, CFLValue, nNonManifold, nCleanupMode, crlElem)
        return JPT_RUN_LINE(message)

class MeshEdit_CreateElement:
    def Hex(self, iParentEntityId=0, crlElem=[], iSeprateN=1):
        message = "MeshEdit.CreateElement.Hex({},{},{})".format(iParentEntityId, crlElem, iSeprateN)
        return JPT_RUN_LINE(message)

    def Penta(self, iParentEntityId=0, crlElem=[]):
        message = "MeshEdit.CreateElement.Penta({},{})".format(iParentEntityId, crlElem)
        return JPT_RUN_LINE(message)

    def Tet(self, iParentEntityId=0, crlNode=[], crlElem=[]):
        message = "MeshEdit.CreateElement.Tet({},{},{})".format(iParentEntityId, crlNode, crlElem)
        return JPT_RUN_LINE(message)

    def Tri3(self, iElemType=0, crParentEntity=None, crlNode=[]):
        message = "MeshEdit.CreateElement.Tri3({},{},{})".format(iElemType, crParentEntity, crlNode)
        return JPT_RUN_LINE(message)

    def Quad4(self, iElemType=0, crParentEntity=None, crlNode=[]):
        message = "MeshEdit.CreateElement.Quad4({},{},{})".format(iElemType, crParentEntity, crlNode)
        return JPT_RUN_LINE(message)

class MeshEdit_CreateNode:
    def CircleCenter(self, crlEdge, iNodeID, bImprint=False, crFace=None):
        message = "MeshEdit.CreateNode.CircleCenter({},{},{},{})".format(crlEdge, iNodeID, bImprint, crFace)
        return JPT_RUN_LINE(message)

    def Absolute(self, veclNodeCoord=[], ilNewNodeID=[]):
        message = "MeshEdit.CreateNode.Absolute({},{})".format(veclNodeCoord, ilNewNodeID)
        return JPT_RUN_LINE(message)

    def Import(self, strCsvFilePath):
        message = "MeshEdit.CreateNode.Import('{}')".format(strCsvFilePath)
        return JPT_RUN_LINE(message)

    def Point(self, iNodeID=1, posPoint=[0,0,0], bImprint=True, crShape=None):
        message = "MeshEdit.CreateNode.Point({},{},{},{})".format(iNodeID, posPoint, bImprint, crShape)
        return JPT_RUN_LINE(message)

    def Between2Nodes(self, iNodeID=0, dX=0.0, dY=0.0, dZ=0.0, iNumberofNodes=0, bImprint=False, crlNode=[], crlFace=[]):
        message = "MeshEdit.CreateNode.Between2Nodes({},{},{},{},{},{},{},{})".format(iNodeID, dX, dY, dZ, iNumberofNodes, bImprint, crlNode, crlFace)
        return JPT_RUN_LINE(message)

    def Between3Nodes(self, iNodeID=0, dX=0.0, dY=0.0, dZ=0.0, bImprint=False, crlNode=[], crlFace=[]):
        message = "MeshEdit.CreateNode.Between3Nodes({},{},{},{},{},{},{})".format(iNodeID, dX, dY, dZ, bImprint, crlNode, crlFace)
        return JPT_RUN_LINE(message)

    def ProjectToPlane(self, dX=0.0, dY=0.0, dZ=0.0, crlNode=[], crlFace=[]):
        message = "MeshEdit.CreateNode.ProjectToPlane({},{},{},{},{})".format(dX, dY, dZ, crlNode, crlFace)
        return JPT_RUN_LINE(message)

    def CenterOfCylinder(self, crlFace=[], iNodeID=1):
        message = "MeshEdit.CreateNode.CenterOfCylinder({},{})".format(crlFace, iNodeID)
        return JPT_RUN_LINE(message)

    def CenterOfSphere(self, crlNodeOrFace=[], iNodeID=1):
        message = "MeshEdit.CreateNode.CenterOfSphere({},{})".format(crlNodeOrFace, iNodeID)
        return JPT_RUN_LINE(message)

    def Offset(self, vecOffset=[], iRep=1, crlNode=[], crCoord=None):
        message = "MeshEdit.CreateNode.Offset({},{},{},{})".format(vecOffset, iRep, crlNode, crCoord)
        return JPT_RUN_LINE(message)

    def CenterOfGravity(self, iCreationType=1, iNodeID=0, dX=0.0, dY=0.0, dZ=0.0, crlPart=[], crlBarPart=[], crlFace=[]):
        message = "MeshEdit.CreateNode.CenterOfGravity({},{},{},{},{},{},{},{})".format(iCreationType, iNodeID, dX, dY, dZ, crlPart, crlBarPart, crlFace)
        return JPT_RUN_LINE(message)

    def ProjectToLine(self, crlTa):
        message = "MeshEdit.CreateNode.ProjectToLine({})".format(crlTa)
        return JPT_RUN_LINE(message)

    def IntersectionNode(self, crlFace, crlPart, crlEdge, crlNode):
        message = "MeshEdit.CreateNode.IntersectionNode({},{},{},{})".format(crlFace, crlPart, crlEdge, crlNode)
        return JPT_RUN_LINE(message)

class MeshEdit_MoveNode:
    def Point(self, dX=0.0, dY=0.0, dZ=0.0, ilNodeList=[]):
        message = "MeshEdit.MoveNode.Point({},{},{},{})".format(dX, dY, dZ, ilNodeList)
        return JPT_RUN_LINE(message)

    def ProjectToLine(self, crlRefNodes=[], crlObjNodes=[], iType=0):
        message = "MeshEdit.MoveNode.ProjectToLine({},{},{})".format(crlRefNodes, crlObjNodes, iType)
        return JPT_RUN_LINE(message)

    def ProjectToPlaneElem(self, crlNode=[], crlElem=[]):
        message = "MeshEdit.MoveNode.ProjectToPlaneElem({},{})".format(crlNode, crlElem)
        return JPT_RUN_LINE(message)

    def Equalize(self, crlEdge=[]):
        message = "MeshEdit.MoveNode.Equalize({})".format(crlEdge)
        return JPT_RUN_LINE(message)

    def NormalOffset(self, dMagnitude=0.0, ilNodeList=[]):
        message = "MeshEdit.MoveNode.NormalOffset({},{})".format(dMagnitude, ilNodeList)
        return JPT_RUN_LINE(message)

    def CoincidentNodes(self, crlNode=[], dTol=0.01, bDesOrder=False):
        message = "MeshEdit.MoveNode.CoincidentNodes({},{},{})".format(crlNode, dTol, bDesOrder)
        return JPT_RUN_LINE(message)

    def AlongCylinder(self, crlFace=[], crlNode=[], dIrX=0, dIrY=0, dIrZ=0, dCircleX=0, dCircleY=0, dCircleZ=0, dRadius=0, dHeight=0):
        message = "MeshEdit.MoveNode.AlongCylinder({},{},{},{},{},{},{},{},{},{})".format(crlFace, crlNode, dIrX, dIrY, dIrZ, dCircleX, dCircleY, dCircleZ, dRadius, dHeight)
        return JPT_RUN_LINE(message)

    def ProjectToPlane_3Nodes(self, ilNodeList=[]):
        message = "MeshEdit.MoveNode.ProjectToPlane_3Nodes({})".format(ilNodeList)
        return JPT_RUN_LINE(message)

    def MoveNodeOffset(self, dDeltaX, dDeltaY, dDeltaZ, crlNode, crCoord):
        message = "MeshEdit.MoveNode.MoveNodeOffset({},{},{},{},{})".format(dDeltaX, dDeltaY, dDeltaZ, crlNode, crCoord)
        return JPT_RUN_LINE(message)

    def RefineQuality(self, iMetric=0, crlFace=[], crlElem=[], crlNode=[]):
        message = "MeshEdit.MoveNode.RefineQuality({},{},{},{})".format(iMetric, crlFace, crlElem, crlNode)
        return JPT_RUN_LINE(message)

    def StraightenMidnodes(self, crlPart=[], crlFace=[], crlEdge=[], crlNode=[]):
        message = "MeshEdit.MoveNode.StraightenMidnodes({},{},{},{})".format(crlPart, crlFace, crlEdge, crlNode)
        return JPT_RUN_LINE(message)

    def Offset(self, dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, crCoord=None, crlNode=[]):
        message = "MeshEdit.MoveNode.Offset({},{},{},{},{})".format(dDeltaX, dDeltaY, dDeltaZ, crCoord, crlNode)
        return JPT_RUN_LINE(message)

    def Laplacian(self, crlTarget=[], iType=0, bWithCADFollow=False):
        message = "MeshEdit.MoveNode.Laplacian({},{},{})".format(crlTarget, iType, bWithCADFollow)
        return JPT_RUN_LINE(message)

    def AlongEdge(self, crlNode=[], bMoveX=False, bMoveY=False, bMoveZ=False, dPosX=0.0, dPosY=0.0, dPosZ=0.0, iMoveType=0):
        message = "MeshEdit.MoveNode.AlongEdge({},{},{},{},{},{},{},{})".format(crlNode, bMoveX, bMoveY, bMoveZ, dPosX, dPosY, dPosZ, iMoveType)
        return JPT_RUN_LINE(message)

    def AlongDirection(self, crlNode=[], crElem=None, crFace=None, vecDirection=[0,0,0], dMagnitude=0.0, bDestination=False):
        message = "MeshEdit.MoveNode.AlongDirection({},{},{},{},{},{})".format(crlNode, crElem, crFace, vecDirection, dMagnitude, bDestination)
        return JPT_RUN_LINE(message)

    def CADFollows(self, crlNode=[], dMovedPosX=0.0, dMovedPosY=0.0, dMovedPosZ=0.0):
        message = "MeshEdit.MoveNode.CADFollows({},{},{},{})".format(crlNode, dMovedPosX, dMovedPosY, dMovedPosZ)
        return JPT_RUN_LINE(message)

    def Scale(self, crlNode=[], crlNodeOrigin=[], crCoord=None, posDeltaXYZ=[10.0, 10.0, 10.0]):
        message = "MeshEdit.MoveNode.Scale({},{},{},{})".format(crlNode, crlNodeOrigin, crCoord, posDeltaXYZ)
        return JPT_RUN_LINE(message)

    def Absolute(self, dDeltaX=0.0, dDeltaY=0.0, dDeltaZ=0.0, b1stCoord=True, b2ndCoord=True, b3rdCoord=True, crlNode=[], crCoord=None):
        message = "MeshEdit.MoveNode.Absolute({},{},{},{},{},{},{},{})".format(dDeltaX, dDeltaY, dDeltaZ, b1stCoord, b2ndCoord, b3rdCoord, crlNode, crCoord)
        return JPT_RUN_LINE(message)

class Meshing_CADProjection:
    def Part(self, iMethod=1, crCadPart=None, crMeshedPart=None, bForceProject=False, bProjectCornerNodes=True, bProjectMidNodes=False, bIDcheck=False):
        message = "Meshing.CADProjection.Part({},{},{},{},{},{},{})".format(iMethod, crCadPart, crMeshedPart, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck)
        return JPT_RUN_LINE(message)

    def Face(self, iMethod=2, crCadPart=None, crlMeshedFace=[], bForceProject=False, bProjectCornerNodes=True, bProjectMidNodes=False, bIDcheck=False):
        message = "Meshing.CADProjection.Face({},{},{},{},{},{},{})".format(iMethod, crCadPart, crlMeshedFace, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck)
        return JPT_RUN_LINE(message)

    def FaceToFace(self, iMethod=3, crlCadFace=[], crlMeshedFace=[], bForceProject=False, bProjectCornerNodes=True, bProjectMidNodes=False, bIDcheck=False):
        message = "Meshing.CADProjection.FaceToFace({},{},{},{},{},{},{})".format(iMethod, crlCadFace, crlMeshedFace, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck)
        return JPT_RUN_LINE(message)

    def NodeToFace(self, iMethod=4, crlCadFace=[], crlMeshedNode=[], iDirection=0, iImproveQuality=0):
        message = "Meshing.CADProjection.NodeToFace({},{},{},{},{})".format(iMethod, crlCadFace, crlMeshedNode, iDirection, iImproveQuality)
        return JPT_RUN_LINE(message)

    def NodeToEdge(self, iMethod=5, crCadEdge=None, crlMeshedNode=[], iDirection=0):
        message = "Meshing.CADProjection.NodeToEdge({},{},{},{})".format(iMethod, crCadEdge, crlMeshedNode, iDirection)
        return JPT_RUN_LINE(message)

class Meshing_LocalMeshing:
    def FilletMapping(self, crlFace=[], iIsoDiv=4, dIsoSize=5, dIsoError=0.5):
        message = "Meshing.LocalMeshing.FilletMapping({},{},{},{})".format(crlFace, iIsoDiv, dIsoSize, dIsoError)
        return JPT_RUN_LINE(message)

    def SelectFillet(self, crlItems=[], dSelectWidthMin=1, dSelectWidthMax=10, dSelectRMin=1, dSelectRMax=10, dAngleMin=0.0, dAngleMax=171.0, bConvex=True, bConcave=True):
        message = "Meshing.LocalMeshing.SelectFillet({},{},{},{},{},{},{},{},{})".format(crlItems, dSelectWidthMin, dSelectWidthMax, dSelectRMin, dSelectRMax, dAngleMin, dAngleMax, bConvex, bConcave)
        return JPT_RUN_LINE(message)

class Meshing_LocalSetting:
    def SearchTargetFaces(self, iPartType=0, dlOrigin=[0, 0, 0], dlLength=[0.1, 0.1, 0.1], dlCenterPt=[0.0,0.0,0.0], dlAxisPt1=[0.0,0.0,0.1], dlAxisPt2=[0.0,0.0,0.0], bEnclosed=False):
        message = "Meshing.LocalSetting.SearchTargetFaces({},{},{},{},{},{},{})".format(iPartType, dlOrigin, dlLength, dlCenterPt, dlAxisPt1, dlAxisPt2, bEnclosed)
        return JPT_RUN_LINE(message)

class Meshing_Templates:
    def TemplateCopy(self, crlReferent=[], crlTarget=[], iMethod=0, iCopySub=1, dTolerance=0.001, strSource="", strTarget=""):
        message = "Meshing.Templates.TemplateCopy({},{},{},{},{},'{}','{}')".format(crlReferent, crlTarget, iMethod, iCopySub, dTolerance, strSource, strTarget)
        return JPT_RUN_LINE(message)

class Meshing_LocalRemesh:
    def Solid(self, crlPart=[], dlCenter=[0.0,0.0,0.0], dRadius=5.0, dGradFactor=1.0, dStrechLimit=0.1):
        message = "Meshing.LocalRemesh.Solid({},{},{},{},{})".format(crlPart, dlCenter, dRadius, dGradFactor, dStrechLimit)
        return JPT_RUN_LINE(message)

    def Surfase(self, crlTarget=[], surfaceMesh = SURFACE_MESH(), bUseSetting=True, bGrading=False, bFMesher=False, iOverrideType=1, bKeepConnection=False, bProjCAD=True, bTinyFaceMerge=False, dMinFaceWidth=0, dMaxFaceWidth=0.001,bIDchcek = False, bKeepRemeshEdge = False):
        message = "Meshing.LocalRemesh.Surfase({},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlTarget, surfaceMesh , bUseSetting, bGrading, bFMesher, iOverrideType, bKeepConnection, bProjCAD, bTinyFaceMerge, dMinFaceWidth, dMaxFaceWidth,bIDchcek , bKeepRemeshEdge )
        return JPT_RUN_LINE(message)

class Meshing_LocalSettings:
    def Edge(self, strName, localMesh, crlTarget=[], ilHardPointId=[], veclHardPointXYZ=[], crlHardPointTarget=[], crEditTarget=None):
        message = "Meshing.LocalSettings.Edge('{}',{},{},{},{},{},{})".format(strName, localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

    def Face(self, strName, localMesh, crlTarget=[], ilHardPointId=[], veclHardPointXYZ=[], crlHardPointTarget=[], crEditTarget=None):
        message = "Meshing.LocalSettings.Face('{}',{},{},{},{},{},{})".format(strName, localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

    def FaceElement(self, strName, localMesh, crlTarget=[], ilHardPointId=[], veclHardPointXYZ=[], crlHardPointTarget=[], crEditTarget=None):
        message = "Meshing.LocalSettings.FaceElement('{}',{},{},{},{},{},{})".format(strName, localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

    def Model(self, strName, localMesh, crlTarget=[], ilHardPointId=[], veclHardPointXYZ=[], crlHardPointTarget=[], crEditTarget=None):
        message = "Meshing.LocalSettings.Model('{}',{},{},{},{},{},{})".format(strName, localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

    def Part(self, strName, localMesh, crlTarget=[], ilHardPointId=[], veclHardPointXYZ=[], crlHardPointTarget=[], crEditTarget=None):
        message = "Meshing.LocalSettings.Part('{}',{},{},{},{},{},{})".format(strName, localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

    def Points(self, strName, localMesh, crlTarget=[], ilHardPointId=[], veclHardPointXYZ=[], crlHardPointTarget=[], crEditTarget=None):
        message = "Meshing.LocalSettings.Points('{}',{},{},{},{},{},{})".format(strName, localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

class AddItems_Edge:
    def ProjectEdgeToFace(self, crlEdge, crlFace, bExtendEdge=True):
        message = "MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace({},{},{})".format(crlEdge, crlFace, bExtendEdge)
        return JPT_RUN_LINE(message)

    def FaceTwoFace(self, crRefFace=None, crExtFace=None, iExtendType=0):
        message = "MidPlaneEdit.AddItems.Edge.FaceTwoFace({},{},{})".format(crRefFace, crExtFace, iExtendType)
        return JPT_RUN_LINE(message)

class AddItems_Face:
    def EFExtendFreeEdge(self, crlEdge, crlFace, bMergeFace, bMergeEdge, bUseNeighDir, dMergeEdgeAngle, bMultiEF):
        message = "MidPlaneEdit.AddItems.Face.EFExtendFreeEdge({},{},{},{},{},{},{})".format(crlEdge, crlFace, bMergeFace, bMergeEdge, bUseNeighDir, dMergeEdgeAngle, bMultiEF)
        return JPT_RUN_LINE(message)

    def EFProject(self, crlEdge, crlFace, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF):
        message = "MidPlaneEdit.AddItems.Face.EFProject({},{},{},{},{},{})".format(crlEdge, crlFace, bMergeFace, bMergeEdge, dMergeEdgeAngle, bMultiEF)
        return JPT_RUN_LINE(message)

class MidPlaneEdit_Edge:
    def Nodes(self, crlNode=[]):
        message = "MidPlaneEdit.Edge.Nodes({})".format(crlNode)
        return JPT_RUN_LINE(message)

class MidPlaneEdit_ExtendFace:
    def CylinderFace(self, crlExtFace=[], crRefFace=None, crEdge=None, iExtendType=1, iFaceType=0, iMethod=0, dParaAngleOffset=0.0, dParaArcLength=0.0, dParaZxy=0.0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0.0, crlSelExtendedFace=[], crlSelRefFace=[], dCoMag=0.0, iAxisSystem=0, iCoorSystem=0, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0.0, dOtherArcRadius=0.0):
        message = "MidPlaneEdit.ExtendFace.CylinderFace({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlExtFace, crRefFace, crEdge, iExtendType, iFaceType, iMethod, dParaAngleOffset, dParaArcLength, dParaZxy, iAxisPlane, iParaArcNodesNum, dOffLength, crlSelExtendedFace, crlSelRefFace, dCoMag, iAxisSystem, iCoorSystem, iCoX, iCoY, iCoZ, bOtherSameAsFaceNormal, dOtherArcNodesNum, dOtherArcRadius)
        return JPT_RUN_LINE(message)

    def PlanarFace(self, bIType=False, crExtFace=None, crRefFace=None, crEdge=None, iFaceType=0, iExtendType=0, iMethod=0, dParaZxy=0, iAxisPlane=0, iParaArcNodesNum=0, dOffLength=0, dCoMag=0, iAxisSystem=0, iCoorSystem=0, crCoord=None, iCoX=0, iCoY=0, iCoZ=0, bOtherSameAsFaceNormal=False, dOtherArcNodesNum=0, dOtherArcRadius=0):
        message = "MidPlaneEdit.ExtendFace.PlanarFace({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(bIType, crExtFace, crRefFace, crEdge, iFaceType, iExtendType, iMethod, dParaZxy, iAxisPlane, iParaArcNodesNum, dOffLength, dCoMag, iAxisSystem, iCoorSystem, crCoord, iCoX, iCoY, iCoZ, bOtherSameAsFaceNormal, dOtherArcNodesNum, dOtherArcRadius)
        return JPT_RUN_LINE(message)

class MidPlaneEdit_Face:
    def FaceExtendtoFace(self, crlExtFaces, crlRefFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle):
        message = "MidPlaneEdit.Face.FaceExtendtoFace({},{},{},{},{})".format(crlExtFaces, crlRefFaces, bMergeFace, bMergeEdge, dMergeEdgeAngle)
        return JPT_RUN_LINE(message)

    def FaceExtendToIntersection(self, crEdge0, crEdge1):
        message = "MidPlaneEdit.Face.FaceExtendToIntersection({},{})".format(crEdge0, crEdge1)
        return JPT_RUN_LINE(message)

    def EdgesToEdges(self, crlEdge, bImprint=False, bMultiEdges=False):
        message = "MidPlaneEdit.Face.EdgesToEdges({},{},{})".format(crlEdge, bImprint, bMultiEdges)
        return JPT_RUN_LINE(message)

class MidPlaneEdit_Manual:
    def vecOffset(self, crlFace, crPart, dOffset, bCyl, strNewPartName):
        message = "MidPlaneEdit.Manual.vecOffset({},{},{},{},'{}')".format(crlFace, crPart, dOffset, bCyl, strNewPartName)
        return JPT_RUN_LINE(message)

    def MidByPair(self, crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces):
        message = "MidPlaneEdit.Manual.MidByPair({},{},{},{},{},{},{},{},{},{})".format(crlBaseFaces, crlPairFaces, crlRefFaces, crPart, bMergeFaces, bExtendFaces, bHideFaces, dExtendTol, dMergeEdgesAngle, dStitchFaces)
        return JPT_RUN_LINE(message)

class MidPlaneEdit_AddItems:
    Edge = AddItems_Edge()

    Face = AddItems_Face()

class MMCCarACTools_ACModelCreationTools:
    def MeshedFace(self, crlItem1, crlItem2, crlItem3, crlPart, iType, dMeshSise, bMergeTol, dTol, bCreatePart):
        message = "MMCCarACTools.ACModelCreationTools.MeshedFace({},{},{},{},{},{},{},{},{})".format(crlItem1, crlItem2, crlItem3, crlPart, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
        return JPT_RUN_LINE(message)

class MMCCarACTools_ClearanceElement:
    def Connect(self, crlFace, crlElem, iConnectionMethod):
        message = "MMCCarACTools.ClearanceElement.Connect({},{},{})".format(crlFace, crlElem, iConnectionMethod)
        return JPT_RUN_LINE(message)

    def Edit(self, dDx, dDy, dDz, dLx, dLy, dLz, crlTarget, crlDestNode, poslDestPoint):
        message = "MMCCarACTools.ClearanceElement.Edit({},{},{},{},{},{},{},{},{})".format(dDx, dDy, dDz, dLx, dLy, dLz, crlTarget, crlDestNode, poslDestPoint)
        return JPT_RUN_LINE(message)

class MufflerHA_CreateEdge:
    def PerpendicularLineToEdge(self, crNode, crEdge, crlFace, bBreakFace):
        message = "MufflerHA.CreateEdge.PerpendicularLineToEdge({},{},{},{})".format(crNode, crEdge, crlFace, bBreakFace)
        return JPT_RUN_LINE(message)

class MufflerHA_CreateEdgeClassic:
    def ProjectLine(self, ilAiedgeidForMacro, ilAifaceidForMacro, bDivideFace, crlAiparttargetForMarco):
        message = "MufflerHA.CreateEdgeClassic.ProjectLine({},{},{},{})".format(ilAiedgeidForMacro, ilAifaceidForMacro, bDivideFace, crlAiparttargetForMarco)
        return JPT_RUN_LINE(message)

class SpecialModeling_Rod:
    def Rod(self, crlNode, dRadius, iType, dMeshSize, dStartDist, dWeldDist, iDivNumber, dDeformWidth, iTransitionElem, dlPosDir):
        message = "MufflerT.SpecialModeling.Rod.Rod({},{},{},{},{},{},{},{},{},{})".format(crlNode, dRadius, iType, dMeshSize, dStartDist, dWeldDist, iDivNumber, dDeformWidth, iTransitionElem, dlPosDir)
        return JPT_RUN_LINE(message)

class MufflerT_SpecialModeling:
    Rod = SpecialModeling_Rod()

class MuxWeld_CreateWeld:
    def Auto(self, iIconnectattributeMethod, strStrconnectattributeName, crlMasterTarget, crlSlaveTarget, iIconnectattributeCoordsys, crEdit):
        message = "MuxWeld.CreateWeld.Auto({},'{}',{},{},{},{})".format(iIconnectattributeMethod, strStrconnectattributeName, crlMasterTarget, crlSlaveTarget, iIconnectattributeCoordsys, crEdit)
        return JPT_RUN_LINE(message)

    def CreateBeadWeld(self, crlEdge, crlPrjtedEdge, crlPart, dTol, dRatio, crRefElem):
        message = "MuxWeld.CreateWeld.CreateBeadWeld({},{},{},{},{},{})".format(crlEdge, crlPrjtedEdge, crlPart, dTol, dRatio, crRefElem)
        return JPT_RUN_LINE(message)

class MuxWeld_DefineSequence:
    def Single(self, crEdit):
        message = "MuxWeld.DefineSequence.Single({})".format(crEdit)
        return JPT_RUN_LINE(message)

class OasisAWizard_LocalMeshing:
    def FilletMapMeshing(self, crlPart=[], crlFace=[], dMinLength=0.0, dMaxLength=1.0, dMinRadius=0.0, dMaxRadius=9e-3, bConvex=True, bConcave=True, iTmp=0, dLengthSingleLayer=0, dBMinLengthForSingleLayer=0, dRadiusSingleLayer=0, dBMinRadiusForSingleLayer=0, iMinlayer=0, bMinLayer=False):
        message = "OasisAWizard.LocalMeshing.FilletMapMeshing({},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, crlFace, dMinLength, dMaxLength, dMinRadius, dMaxRadius, bConvex, bConcave, iTmp, dLengthSingleLayer, dBMinLengthForSingleLayer, dRadiusSingleLayer, dBMinRadiusForSingleLayer, iMinlayer, bMinLayer)
        return JPT_RUN_LINE(message)

class Post_ImportResults:
    def ImportOp2Mesh(self, strlFilePaths, iImportType=0, dFaceAngle=60.0, dEdgeAngle=60.0):
        message = "Post.ImportResults.ImportOp2Mesh('{}',{},{},{})".format(strlFilePaths, iImportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def NastranOp2PostJob(self, strName, strlPaths, crEdit=None):
        message = "Post.ImportResults.NastranOp2PostJob('{}','{}',{})".format(strName, strlPaths, crEdit)
        return JPT_RUN_LINE(message)

    def ImportTsdbMesh(self, strTsdbFilePath, strBtxFilePath, iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0):
        message = "Post.ImportResults.ImportTsdbMesh('{}','{}',{},{},{})".format(strTsdbFilePath, strBtxFilePath, iImportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def HDF5Mesh(self, strlFilePaths, iImportType=2, dFaceAngle=60.0, dEdgeAngle=60.0):
        message = "Post.ImportResults.HDF5Mesh('{}',{},{},{})".format(strlFilePaths, iImportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def ADVC(self, strlPath=[], iImportType=1, dFaceAngle=60.0, dEdgeAngle=60.0):
        message = "Post.ImportResults.ADVC('{}',{},{},{})".format(strlPath, iImportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def ADVC2PostJob(self, strName, strlResultFolderPaths, crEdit):
        message = "Post.ImportResults.ADVC2PostJob('{}','{}',{})".format(strName, strlResultFolderPaths, crEdit)
        return JPT_RUN_LINE(message)

    def NastranHDF5(self, strName="", strlPaths=[], crEdit=None):
        message = "Post.ImportResults.NastranHDF5('{}','{}',{})".format(strName, strlPaths, crEdit)
        return JPT_RUN_LINE(message)

class Properties_ElemRelatedInfo:
    def Shell(self, listErishellThetaProp=[], listErishellCsProp=[], listErishellZoffsProp=[]):
        message = "Properties.ElemRelatedInfo.Shell({},{},{})".format(listErishellThetaProp, listErishellCsProp, listErishellZoffsProp)
        return JPT_RUN_LINE(message)

    def Conn(self, listEricontEndProp=[], listEricontOriVecProp=[], listCidProp=[], listEricontDamperLocProp=[], listOcidProp=[], listDamperOffsetVecs=[], listEricontNodeidProp=[]):
        message = "Properties.ElemRelatedInfo.Conn({},{},{},{},{},{},{})".format(listEricontEndProp, listEricontOriVecProp, listCidProp, listEricontDamperLocProp, listOcidProp, listDamperOffsetVecs, listEricontNodeidProp)
        return JPT_RUN_LINE(message)

    def Rod(self, listEricontEndProp=[]):
        message = "Properties.ElemRelatedInfo.Rod({})".format(listEricontEndProp)
        return JPT_RUN_LINE(message)

    def Beam(self, listEribeamEndProp=[], listEribeamOriVecProp=[], listEribeamOriNodeidProp=[], listEribeamOffsetVecA=[], listEribeamOffsetVecB=[], listEribeamPinAProp=[], listEribeamPinBProp=[], listEribeamWarpProp=[]):
        message = "Properties.ElemRelatedInfo.Beam({},{},{},{},{},{},{},{})".format(listEribeamEndProp, listEribeamOriVecProp, listEribeamOriNodeidProp, listEribeamOffsetVecA, listEribeamOffsetVecB, listEribeamPinAProp, listEribeamPinBProp, listEribeamWarpProp)
        return JPT_RUN_LINE(message)

    def Bar(self, listEribeamEndProp=[], listEribeamOriVecProp=[], listEribeamOriNodeidProp=[], listEribeamOffsetVecA=[], listEribeamOffsetVecB=[], listEribeamPinAProp=[], listEribeamPinBProp=[], listEribeamWarpProp=[]):
        message = "Properties.ElemRelatedInfo.Bar({},{},{},{},{},{},{},{})".format(listEribeamEndProp, listEribeamOriVecProp, listEribeamOriNodeidProp, listEribeamOffsetVecA, listEribeamOffsetVecB, listEribeamPinAProp, listEribeamPinBProp, listEribeamWarpProp)
        return JPT_RUN_LINE(message)

    def Gap(self, listEricontEndProp=[], listEricontOriVecProp=[], listCidProp=[], listEricontDamperLocProp=[], listOcidProp=[], listDamperOffsetVecs=[], listEricontNodeidProp=[]):
        message = "Properties.ElemRelatedInfo.Gap({},{},{},{},{},{},{})".format(listEricontEndProp, listEricontOriVecProp, listCidProp, listEricontDamperLocProp, listOcidProp, listDamperOffsetVecs, listEricontNodeidProp)
        return JPT_RUN_LINE(message)

    def Bush(self, listEricontEndProp=[], listEricontOriVecProp=[], listCidProp=[], listEricontDamperLocProp=[], listOcidProp=[], listDamperOffsetVecs=[], listEricontNodeidProp=[]):
        message = "Properties.ElemRelatedInfo.Bush({},{},{},{},{},{},{})".format(listEricontEndProp, listEricontOriVecProp, listCidProp, listEricontDamperLocProp, listOcidProp, listDamperOffsetVecs, listEricontNodeidProp)
        return JPT_RUN_LINE(message)

class Properties_Material:
    def Add(self, strMaterialName, listMaterialProperty):
        message = "Properties.Material.Add('{}',{})".format(strMaterialName, listMaterialProperty)
        return JPT_RUN_LINE(message)

    def Modify(self, strMaterialID, listMaterialProperty):
        message = "Properties.Material.Modify('{}',{})".format(strMaterialID, listMaterialProperty)
        return JPT_RUN_LINE(message)

    def Delete(self, strMaterialID):
        message = "Properties.Material.Delete('{}')".format(strMaterialID)
        return JPT_RUN_LINE(message)

class Properties_Section:
    def Import(self, strImportPath=""):
        message = "Properties.Section.Import('{}')".format(strImportPath)
        return JPT_RUN_LINE(message)

    def ModifyGeneral(self, strName="", crSection=None, iSecType=0, iGeneralType=0, dA=0, dB=0, dH=0, dT1=0, dT2=0, dT3=0, bTapered=False, dDaTap=0, dDbTap=0, dDhTap=0, dDt1Tap=0, dDt2Tap=0, dDt3Tap=0):
        message = "Properties.Section.ModifyGeneral('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, crSection, iSecType, iGeneralType, dA, dB, dH, dT1, dT2, dT3, bTapered, dDaTap, dDbTap, dDhTap, dDt1Tap, dDt2Tap, dDt3Tap)
        return JPT_RUN_LINE(message)

    def ModifyLibrary(self, strName="", crSection=None, iType=0, iLibType=0, dDimSize0=0, dDimSize1=0, dDimSize2=0, dDimSize3=0, dDimSize4=0, dDimSize5=0, dDimSize6=0, dDimSize7=0, dDimSize8=0, dDimSize9=0, dDimSize10=0, dDimSize11=0):
        message = "Properties.Section.ModifyLibrary('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, crSection, iType, iLibType, dDimSize0, dDimSize1, dDimSize2, dDimSize3, dDimSize4, dDimSize5, dDimSize6, dDimSize7, dDimSize8, dDimSize9, dDimSize10, dDimSize11)
        return JPT_RUN_LINE(message)

    def ModifySketcher(self, strName="", crSection=None, iType=0):
        message = "Properties.Section.ModifySketcher('{}',{},{})".format(strName, crSection, iType)
        return JPT_RUN_LINE(message)

    def Export(self, strExportSavePath=""):
        message = "Properties.Section.Export('{}')".format(strExportSavePath)
        return JPT_RUN_LINE(message)

    def Delete(self, crlSection=[]):
        message = "Properties.Section.Delete({})".format(crlSection)
        return JPT_RUN_LINE(message)

    def AddGeneral(self, strName="", iSecType=0, iSecGenType=0, dDsecGensizeA=0, dDsecGensizeB=0, dDsecGensizeH=0, dDsecGensizeT1=0, dDsecGensizeT2=0, dDsecGensizeT3=0, bBsecTapered=False, dDsecGensizeATap=0, dDsecGensizeBTap=0, dDsecGensizeHTap=0, dDsecGensizeT1Tap=0, dDsecGensizeT2Tap=0, dDsecGensizeT3Tap=0):
        message = "Properties.Section.AddGeneral('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iSecType, iSecGenType, dDsecGensizeA, dDsecGensizeB, dDsecGensizeH, dDsecGensizeT1, dDsecGensizeT2, dDsecGensizeT3, bBsecTapered, dDsecGensizeATap, dDsecGensizeBTap, dDsecGensizeHTap, dDsecGensizeT1Tap, dDsecGensizeT2Tap, dDsecGensizeT3Tap)
        return JPT_RUN_LINE(message)

    def AddLibrary(self, strName="", iSecType=1, iLibType=0, dDim1=0, dDim2=0, dDim3=0, dDim4=0, dDim5=0, dDim6=0, dDim7=0, dDim8=0, dDim9=0, dDim10=0, dDim11=0, dDim12=0):
        message = "Properties.Section.AddLibrary('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iSecType, iLibType, dDim1, dDim2, dDim3, dDim4, dDim5, dDim6, dDim7, dDim8, dDim9, dDim10, dDim11, dDim12)
        return JPT_RUN_LINE(message)

    def AddSketcher(self, strName="", iSecType=2):
        message = "Properties.Section.AddSketcher('{}',{})".format(strName, iSecType)
        return JPT_RUN_LINE(message)

class SNOnePush_DropTest:
    def CalcTimestep(self, dRelevantElemRate, dChangeMassRage):
        message = "SNOnePush.DropTest.CalcTimestep({},{})".format(dRelevantElemRate, dChangeMassRage)
        return JPT_RUN_LINE(message)

    def UpdateFloor(self, strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumberOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None):
        message = "SNOnePush.DropTest.UpdateFloor('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iNumberOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

    def DropRotation(self, strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumberOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None):
        message = "SNOnePush.DropTest.DropRotation('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iNumberOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

class SZOnepushReliability_Assembly:
    def CreateWeld(self, crlWelds, dMeshSize, iRrate, dFilletRadius):
        message = "SZOnepushReliability.Assembly.CreateWeld({},{},{},{})".format(crlWelds, dMeshSize, iRrate, dFilletRadius)
        return JPT_RUN_LINE(message)

    def ContactSurface(self, crlSrcFace, crlTarPart, dTolerance, iLayer):
        message = "SZOnepushReliability.Assembly.ContactSurface({},{},{},{})".format(crlSrcFace, crlTarPart, dTolerance, iLayer)
        return JPT_RUN_LINE(message)

class SZOnepushReliability_MeshEdit:
    def FilletMapping(self, crlPart, crlFace, dMinRadius, dMaxRadius, dMinAngle, dMaxAngle, bConvex, bConcave):
        message = "SZOnepushReliability.MeshEdit.FilletMapping({},{},{},{},{},{},{},{})".format(crlPart, crlFace, dMinRadius, dMaxRadius, dMinAngle, dMaxAngle, bConvex, bConcave)
        return JPT_RUN_LINE(message)

class Test_Connection:
    def RRod(self, rbarConnection=RBAR_CONNECTION(), iUlDOFs=1, dTol=0.0, crlMasterTarget=[], crlSlaveTarget=[]):
        message = "Test.Connection.RRod({},{},{},{},{})".format(rbarConnection, iUlDOFs, dTol, crlMasterTarget, crlSlaveTarget)
        return JPT_RUN_LINE(message)

class Test_Muffler:
    def ProjectLineForWeld(self, crlEdge, crlFace):
        message = "Test.Muffler.ProjectLineForWeld({},{})".format(crlEdge, crlFace)
        return JPT_RUN_LINE(message)

class Test_ZGeometryTest:
    def IntersectionCheck(self, crlPart, crlFace, crlElem, iType):
        message = "Test.ZGeometryTest.IntersectionCheck({},{},{},{})".format(crlPart, crlFace, crlElem, iType)
        return JPT_RUN_LINE(message)

    def ShellAssy(self, taPart=[], crlFace=[], _iMeshType=0, _bSelfIntersection=False, _iMethod=3, _dGapTol=2.1):
        message = "Test.ZGeometryTest.ShellAssy({},{},{},{},{},{})".format(taPart, crlFace, _iMeshType, _bSelfIntersection, _iMethod, _dGapTol)
        return JPT_RUN_LINE(message)

class Measure_Angle:
    def TwoNodesAxis(self, crNode1, crNode2, dlAxis=[1,0,0], strTarget="Angle", iPrecision=6):
        message = "Tools.Measure.Angle.TwoNodesAxis({},{},{},'{}',{})".format(crNode1, crNode2, dlAxis, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def ThreeNodes(self, crNode1, crNode2, crNode3, strTarget="All", iPrecision=6):
        message = "Tools.Measure.Angle.ThreeNodes({},{},{},'{}',{})".format(crNode1, crNode2, crNode3, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def ProjectedNode(self, crNode, strTarget="All", iPrecision=6):
        message = "Tools.Measure.Angle.ProjectedNode({},'{}',{})".format(crNode, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoElemEdges(self, crpElemEdge1, crpElemEdge2, strTarget="Angle", iPrecision=6):
        message = "Tools.Measure.Angle.TwoElemEdges({},{},'{}',{})".format(crpElemEdge1, crpElemEdge2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoAxis(self, dlXyz1=[0, 0, 0], dlXyz2=[0, 0, 0], strTarget="Angle", iPrecision=6):
        message = "Tools.Measure.Angle.TwoAxis({},{},'{}',{})".format(dlXyz1, dlXyz2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoEdges(self, crEdge1, crEdge2, strTarget="Angle", iPrecision=6):
        message = "Tools.Measure.Angle.TwoEdges({},{},'{}',{})".format(crEdge1, crEdge2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Measure_Area:
    def Element(self, crlElem=[], iPrecision=6):
        message = "Tools.Measure.Area.Element({},{})".format(crlElem, iPrecision)
        return JPT_RUN_LINE(message)

    def Face(self, crlFace=[], iPrecision=6):
        message = "Tools.Measure.Area.Face({},{})".format(crlFace, iPrecision)
        return JPT_RUN_LINE(message)

    def Part(self, crlPart=[], iPrecision=6):
        message = "Tools.Measure.Area.Part({},{})".format(crlPart, iPrecision)
        return JPT_RUN_LINE(message)

class Measure_Distance:
    def TwoEdges(self, crEdge1, crEdge2, iPrecision=6):
        message = "Tools.Measure.Distance.TwoEdges({},{},{})".format(crEdge1, crEdge2, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoNodes(self, crNode1=None, crNode2=None, strTarget="ALL", iPrecision=6, crCoordinateSystem=None):
        message = "Tools.Measure.Distance.TwoNodes({},{},'{}',{},{})".format(crNode1, crNode2, strTarget, iPrecision, crCoordinateSystem)
        return JPT_RUN_LINE(message)

    def FaceNode(self, crlFace, crlNode, iPrecision=6):
        message = "Tools.Measure.Distance.FaceNode({},{},{})".format(crlFace, crlNode, iPrecision)
        return JPT_RUN_LINE(message)

    def Edge(self, crEdge=None, iPrecision=6):
        message = "Tools.Measure.Distance.Edge({},{})".format(crEdge, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoPoints(self, posPoint1=[0,0,0], posPoint2=[0,0,0], strTarget="ALL", iPrecision=6, crCoordinateSystem=None):
        message = "Tools.Measure.Distance.TwoPoints({},{},'{}',{},{})".format(posPoint1, posPoint2, strTarget, iPrecision, crCoordinateSystem)
        return JPT_RUN_LINE(message)

    def EdgeNode(self, crEdge, crNode, iPrecision=6):
        message = "Tools.Measure.Distance.EdgeNode({},{},{})".format(crEdge, crNode, iPrecision)
        return JPT_RUN_LINE(message)

    def LineNode(self, crlTargetNode, iPrecision=6):
        message = "Tools.Measure.Distance.LineNode({},{})".format(crlTargetNode, iPrecision)
        return JPT_RUN_LINE(message)

    def PlaneElemToNode(self, crNode=None, crElem=None, iPrecision=6):
        message = "Tools.Measure.Distance.PlaneElemToNode({},{},{})".format(crNode, crElem, iPrecision)
        return JPT_RUN_LINE(message)

    def Plane3NodesToNode(self, crNode1, crNode2, crNode3, crNode, iPrecision=6):
        message = "Tools.Measure.Distance.Plane3NodesToNode({},{},{},{},{})".format(crNode1, crNode2, crNode3, crNode, iPrecision)
        return JPT_RUN_LINE(message)

class Measure_Mass:
    def Property(self, crlPart, crlCondition, strTarget="Mass", bGravityCenter=False, iPrecision=6):
        message = "Tools.Measure.Mass.Property({},{},'{}',{},{})".format(crlPart, crlCondition, strTarget, bGravityCenter, iPrecision)
        return JPT_RUN_LINE(message)

    def Material(self, crlPart, crlCondition, strDensity, strTarget="Mass", bGravityCenter=False, iPrecision=6):
        message = "Tools.Measure.Mass.Material({},{},'{}','{}',{},{})".format(crlPart, crlCondition, strDensity, strTarget, bGravityCenter, iPrecision)
        return JPT_RUN_LINE(message)

class Measure_Radius:
    def Edge(self, crEdge, iPrecision=6):
        message = "Tools.Measure.Radius.Edge({},{})".format(crEdge, iPrecision)
        return JPT_RUN_LINE(message)

    def ThreeNodes(self, crNode13, crNode23, crNode33, iPrecision=6):
        message = "Tools.Measure.Radius.ThreeNodes({},{},{},{})".format(crNode13, crNode23, crNode33, iPrecision)
        return JPT_RUN_LINE(message)

class Tools_BySelection:
    def SelectionOrder(self, crlTarget=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True):
        message = "Tools.BySelection.SelectionOrder({},{},{},{},{},{})".format(crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending)
        return JPT_RUN_LINE(message)

    def Position(self, crlTarget=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending1=True, bAscending2=False, bAscending3=False, iSortFirst=0, iSortSecond=1, iSortThird=2, iEnableSortFirst=1, iEnableSortSecond=0, iEnableSortThird=0, iOffset1=0, iOffset2=0, iOffset3=0, dTol1=0.0, dTol2=0.0, dTol3=0.0, crCoord=None, bSpecialFace=False):
        message = "Tools.BySelection.Position({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending1, bAscending2, bAscending3, iSortFirst, iSortSecond, iSortThird, iEnableSortFirst, iEnableSortSecond, iEnableSortThird, iOffset1, iOffset2, iOffset3, dTol1, dTol2, dTol3, crCoord, bSpecialFace)
        return JPT_RUN_LINE(message)

    def OriginalID(self, crlTarget=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True):
        message = "Tools.BySelection.OriginalID({},{},{},{},{},{})".format(crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending)
        return JPT_RUN_LINE(message)

class Tools_Coordinates:
    def CylinderFace(self, strName="CRect1", iCoordType=0, crFace=None):
        message = "Tools.Coordinates.CylinderFace('{}',{},{})".format(strName, iCoordType, crFace)
        return JPT_RUN_LINE(message)

    def ThreeNode(self, strName="CRect1", iCoordType=0, iOrder=0, crlNode=[], veclPoints=[], crRefCoord=None, crEdit=None):
        message = "Tools.Coordinates.ThreeNode('{}',{},{},{},{},{},{})".format(strName, iCoordType, iOrder, crlNode, veclPoints, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def Align(self, strName="CRect1", iCoordType=0, iCoordAxis=0, bCreateNew=True, crlNode=[], crEdge=None, crEdit=None):
        message = "Tools.Coordinates.Align('{}',{},{},{},{},{},{})".format(strName, iCoordType, iCoordAxis, bCreateNew, crlNode, crEdge, crEdit)
        return JPT_RUN_LINE(message)

    def vecOffset(self, strName="CRect1", iCoordType=0, vTranslate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None):
        message = "Tools.Coordinates.vecOffset('{}',{},{},{},{},{})".format(strName, iCoordType, vTranslate, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def Rotate(self, strName="CRect1", iCoordType=0, vecRotate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None):
        message = "Tools.Coordinates.Rotate('{}',{},{},{},{},{})".format(strName, iCoordType, vecRotate, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def AttachCircle(self, strName="CRect1", iCoordType=0, crEdge=None, bCreateNew=True, crRefCoord=None, crEdit=None):
        message = "Tools.Coordinates.AttachCircle('{}',{},{},{},{},{})".format(strName, iCoordType, crEdge, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def AttachNode(self, strName="CRect1", iCoordType=0, crNode=None, bCreateNew=True, crRefCoord=None, crEdit=None):
        message = "Tools.Coordinates.AttachNode('{}',{},{},{},{},{})".format(strName, iCoordType, crNode, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def Face(self, strName="CRect1", iCoordType=0, iOrder=0, veclPoint=[], crlNode=[], crItem=None, crRefCoord=None, crEdit=None):
        message = "Tools.Coordinates.Face('{}',{},{},{},{},{},{},{})".format(strName, iCoordType, iOrder, veclPoint, crlNode, crItem, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def Offset(self, strName="CRect1", iCoordType=0, vecTranslate=[0.0,0.0,0.0], bCreateNew=True, crRefCoord=None, crEdit=None):
        message = "Tools.Coordinates.Offset('{}',{},{},{},{},{})".format(strName, iCoordType, vecTranslate, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

class Tools_Group:
    def DeleteGroupEntity(self, crlDelGroup):
        message = "Tools.Group.DeleteGroupEntity({})".format(crlDelGroup)
        return JPT_RUN_LINE(message)

    def CreateGroup(self, strGroupName, crlTarget=[], crEdit=None):
        message = "Tools.Group.CreateGroup('{}',{},{})".format(strGroupName, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Tools_TotalLoad:
    def LBC(self, crlTarget=[], crCoordinate=None, strOutput="Total", iPrecision=6):
        message = "Tools.TotalLoad.LBC({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

    def Model(self, crlTarget=[], crCoordinate=None, strOutput="Total", iPrecision=6):
        message = "Tools.TotalLoad.Model({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

    def Node(self, crlTarget=[], crCoordinate=None, strOutput="Total", iPrecision=6):
        message = "Tools.TotalLoad.Node({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

    def Part(self, crlTarget=[], crCoordinate=None, strOutput="Total", iPrecision=6):
        message = "Tools.TotalLoad.Part({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

    def Face(self, crlTarget=[], crCoordinate=None, strOutput="Total", iPrecision=6):
        message = "Tools.TotalLoad.Face({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

class Tools_Measure:
    Angle = Measure_Angle()

    Area = Measure_Area()

    Distance = Measure_Distance()

    Mass = Measure_Mass()

    Radius = Measure_Radius()

    def Volume(self, crlPart, iPrecision=6):
        message = "Tools.Measure.Volume({},{})".format(crlPart, iPrecision)
        return JPT_RUN_LINE(message)

class FileMenu:
    def AddJTDB(strFileName, strMethod="AUTO", strTargetModel="IMPORTED", strOption="OFFSET", iInputNode=0, iInputElem=0, iInputPart=0, iInputMaterial=0, iInputProperty=0):
        message = "FileMenu.AddJTDB('{}','{}','{}','{}',{},{},{},{},{})".format(strFileName, strMethod, strTargetModel, strOption, iInputNode, iInputElem, iInputPart, iInputMaterial, iInputProperty)
        return JPT_RUN_LINE(message)

    def Save(strFileName=""):
        message = "FileMenu.Save('{}')".format(strFileName)
        return JPT_RUN_LINE(message)

    def Open(strFileName="", bUseTmpTable=False):
        message = "FileMenu.Open('{}',{})".format(strFileName, bUseTmpTable)
        return JPT_RUN_LINE(message)

class Utility:
    def FindEntities(strTarget, strFindType, bFindMatch=False):
        message = "Utility.FindEntities('{}','{}',{})".format(strTarget, strFindType, bFindMatch)
        return JPT_RUN_LINE(message)

    def MeasureDistanceBy2Edges(crEdgeFirst, crEdgeLast, iPrecision=6):
        message = "Utility.MeasureDistanceBy2Edges({},{},{})".format(crEdgeFirst, crEdgeLast, iPrecision)
        return JPT_RUN_LINE(message)

class ACModeling:
    ACBoundary = ACModeling_ACBoundary()

    Create = ACModeling_Create()

    def CloseHoleAuto(crlClosedHoleParts):
        message = "ACModeling.CloseHoleAuto({})".format(crlClosedHoleParts)
        return JPT_RUN_LINE(message)

    def Cut(crlPart):
        message = "ACModeling.Cut({})".format(crlPart)
        return JPT_RUN_LINE(message)

class Analysis:
    AbaqusStep = Analysis_AbaqusStep()

    ACTRAN = Analysis_ACTRAN()

    Analysis = Analysis_Analysis()

    Ansys = Analysis_Ansys()

    Nastran = Analysis_Nastran()

    Permas = Analysis_Permas()

    TSSolver = Analysis_TSSolver()

    TSSS = Analysis_TSSS()

    def Abaqus(strName, bRBE2toMPC=False, bRenameProcess=False, iCodeType=0, iSurfDefType=0, iUnit=0, iWriteType=0, strDescription="", crlStepSequence=[], crEdit=None, strlUserText=[], bExptNdEleGroups=False, bDeleteFloatingNodes=False, bExptFaceElemGroups2Surface=False, bLoadCase=False, bAutoAssignDummyProperty=True, crDummyMat=None, bOutputGeometryId=True):
        message = "Analysis.Abaqus('{}',{},{},{},{},{},{},'{}',{},{},'{}',{},{},{},{},{},{},{})".format(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat, bOutputGeometryId)
        return JPT_RUN_LINE(message)

    def ExportAnsys(strName="", crAnsysJob=None):
        message = "Analysis.ExportAnsys('{}',{})".format(strName, crAnsysJob)
        return JPT_RUN_LINE(message)

    def ExportAbaqus(crAbaJob=None, crlSelectPart=[], strInpPath=""):
        message = "Analysis.ExportAbaqus({},{},'{}')".format(crAbaJob, crlSelectPart, strInpPath)
        return JPT_RUN_LINE(message)

    def ModifyLbcToStep(listAbaqusLbcStepInfo=[]):
        message = "Analysis.ModifyLbcToStep({})".format(listAbaqusLbcStepInfo)
        return JPT_RUN_LINE(message)

    def ExportAdx(crJob=None, strPath="", iNumType=0, iUiWidth=10, iUiPrecision=1):
        message = "Analysis.ExportAdx({},'{}',{},{},{})".format(crJob, strPath, iNumType, iUiWidth, iUiPrecision)
        return JPT_RUN_LINE(message)

    def ExportLsdyna(strPath="", crJob=None):
        message = "Analysis.ExportLsdyna('{}',{})".format(strPath, crJob)
        return JPT_RUN_LINE(message)

    def NastranJob(strName="Job_1", strDescription="", crlTarget=[], nastranAnalysis=NASTRAN_ANALYSIS(), bDummyPropAutoAssign=False, iDummyPropMaterialID=0, crEdit=None):
        message = "Analysis.NastranJob('{}','{}',{},'{}',{},{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit)
        return JPT_RUN_LINE(message)

    def LSDYNAJob(crEdit=None):
        message = "Analysis.LSDYNAJob({})".format(crEdit)
        return JPT_RUN_LINE(message)

    ADVC = Analysis_ADVC()

class Assemble:
    SeparateFaces = Assemble_SeparateFaces()

    def Boolean(crlPart, iBooleanType=0, dToleranceAlignment=0.01, bLeaveOriginalBodies=False):
        message = "Assemble.Boolean({},{},{},{})".format(crlPart, iBooleanType, dToleranceAlignment, bLeaveOriginalBodies)
        return JPT_RUN_LINE(message)

    def AssembleFace(crlPart, crlFace, dTolerance, iFitEdge, iMeshSetting):
        message = "Assemble.AssembleFace({},{},{},{},{})".format(crlPart, crlFace, dTolerance, iFitEdge, iMeshSetting)
        return JPT_RUN_LINE(message)

    def FullLayer(crPart, dLayerWidth=1.0, iLayer=1, bUsePyramid=False):
        message = "Assemble.FullLayer({},{},{},{})".format(crPart, dLayerWidth, iLayer, bUsePyramid)
        return JPT_RUN_LINE(message)

    def CylinderLayer(crFace=None, crNode=None):
        message = "Assemble.CylinderLayer({},{})".format(crFace, crNode)
        return JPT_RUN_LINE(message)

    def SharedFace():
        message = "Assemble.SharedFace({})".format('')
        return JPT_RUN_LINE(message)

    def AssembleFaces(ilPairFaceToMakeShareFace=[], dTolerance=0.1, iTypeConnectPos=1, bUseSnapInput=False, dSnapTolerance=0.005, bFitEdge=False):
        message = "Assemble.AssembleFaces({},{},{},{},{},{})".format(ilPairFaceToMakeShareFace, dTolerance, iTypeConnectPos, bUseSnapInput, dSnapTolerance, bFitEdge)
        return JPT_RUN_LINE(message)

    def GeneralLayer(crlFace=[], dWidth=1.0, iLayer=1, bSeparatePart=False, bForceStitchToSide=False, bSmoothingEdge=False, bNoImprint=False, bWidthOnSurface=False, bMakeHexa=False):
        message = "Assemble.GeneralLayer({},{},{},{},{},{},{},{},{})".format(crlFace, dWidth, iLayer, bSeparatePart, bForceStitchToSide, bSmoothingEdge, bNoImprint, bWidthOnSurface, bMakeHexa)
        return JPT_RUN_LINE(message)

    def AddRib(crPart=None, crlFace=[], veclPoints=[], dWidth=0.0, dDepth=0.0):
        message = "Assemble.AddRib({},{},{},{},{})".format(crPart, crlFace, veclPoints, dWidth, dDepth)
        return JPT_RUN_LINE(message)

    def FindMatingFace(crlMasterFaces=[], crlSlaveFaces=[], crlPart=[], dTolerance=0.0):
        message = "Assemble.FindMatingFace({},{},{},{})".format(crlMasterFaces, crlSlaveFaces, crlPart, dTolerance)
        return JPT_RUN_LINE(message)

    def AddBoss(crPart=None, iType=0, bMerge=True, posOrgCenter=[0,0,0], vecOrgDirection=[0,0,0], crCoord=None, iAxis=0, dAngle=0.0, bHollow=False, dInnerRadius=0.0, dOrgOuterRadius=1.0, dTaperAngle=0.0, iNodeOnCircle=12, iNodeOnAxis=2, dOriginalHeight=5.0):
        message = "Assemble.AddBoss({},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crPart, iType, bMerge, posOrgCenter, vecOrgDirection, crCoord, iAxis, dAngle, bHollow, dInnerRadius, dOrgOuterRadius, dTaperAngle, iNodeOnCircle, iNodeOnAxis, dOriginalHeight)
        return JPT_RUN_LINE(message)

class Assembly:
    RightClick = Assembly_RightClick()

class BoundaryConditions:
    BoundaryTemperature = BoundaryConditions_BoundaryTemperature()

    Convection = BoundaryConditions_Convection()

    EnforcedLoads = BoundaryConditions_EnforcedLoads()

    HeatFlux = BoundaryConditions_HeatFlux()

    InitialElementalValue = BoundaryConditions_InitialElementalValue()

    InitialTemperature = BoundaryConditions_InitialTemperature()

    LBCCopy = BoundaryConditions_LBCCopy()

    Pressure = BoundaryConditions_Pressure()

    Submodel = BoundaryConditions_Submodel()

    TemperatureLoads = BoundaryConditions_TemperatureLoads()

    def LoadCase(strName="LoadCase1", dFactor=1.0, crlTarget=[], iExportId=1, dlTargetFactor=[], crEdit=None):
        message = "BoundaryConditions.LoadCase('{}',{},{},{},{},{})".format(strName, dFactor, crlTarget, iExportId, dlTargetFactor, crEdit)
        return JPT_RUN_LINE(message)

    def InsideHeatGeneration(strName="InsideHeatGeneration1", dInsideFlux=DFLT_DBL, crTable=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.InsideHeatGeneration('{}',{},{},{},{})".format(strName, dInsideFlux, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def LBCCopyMisc(iMethod=0, iMatchMethod=0, dlTransVec=[0,0,0], dTransMag=0, dTransOffset=0, dTransTol=0, crTranscrCoord=None, dlTransaxisVec=[0,0,0], dlTranscenterVec=[0,0,0], dRotateAngle=0, dRotateTol=0, crRotatecrCoord=None, veclMirrorPoint=[], dMirrordOffset=0, dMirrorTol=0.1, crlTarget=[]):
        message = "BoundaryConditions.LBCCopyMisc({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, dlTransVec, dTransMag, dTransOffset, dTransTol, crTranscrCoord, dlTransaxisVec, dlTranscenterVec, dRotateAngle, dRotateTol, crRotatecrCoord, veclMirrorPoint, dMirrordOffset, dMirrorTol, crlTarget)
        return JPT_RUN_LINE(message)

    def LbcContactConvert(iConvertTo, iTieConvType, crlTarget):
        message = "BoundaryConditions.LbcContactConvert({},{},{})".format(iConvertTo, iTieConvType, crlTarget)
        return JPT_RUN_LINE(message)

    def FieldData(strName="", iType=0, ilSheet=[], crEdit=None, bAbaqusAmp=False, iAmpType=0):
        message = "BoundaryConditions.FieldData('{}',{},{},{},{},{})".format(strName, iType, ilSheet, crEdit, bAbaqusAmp, iAmpType)
        return JPT_RUN_LINE(message)

    def FixedConstraint(strName="Constraint1", iDwDof=7, crCurCoord=None, iType=0, iUsetType=0, crTable=None, bAbaqusFixed=False, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.FixedConstraint('{}',{},{},{},{},{},{},{},{})".format(strName, iDwDof, crCurCoord, iType, iUsetType, crTable, bAbaqusFixed, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def DofSet(strName="", iDwDof=0, crCurCoord=None, crTable=None, crlTarget=[], crEdit=None):
        message = "BoundaryConditions.DofSet('{}',{},{},{},{},{})".format(strName, iDwDof, crCurCoord, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    BodyLoads = BoundaryConditions_BodyLoads()

    Force = BoundaryConditions_Force()

    InitialNodalValue = BoundaryConditions_InitialNodalValue()

class Connections:
    Pretension = Connections_Pretension()

    def MassElements(strName, crlTarget, dMass=0.01, iDof=1, bDesigner=True, crCoordinate=None, dOffset0=0.0, dOffset1=0.0, dOffset2=0.0, dInertia0=0.0, dInertia1=0.0, dInertia2=0.0, dInertia3=0.0, dInertia4=0.0, dInertia5=0.0, crEdit=None, bUpdateDispCS=True):
        message = "Connections.MassElements('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, crlTarget, dMass, iDof, bDesigner, crCoordinate, dOffset0, dOffset1, dOffset2, dInertia0, dInertia1, dInertia2, dInertia3, dInertia4, dInertia5, crEdit, bUpdateDispCS)
        return JPT_RUN_LINE(message)

    def BarBeam(strName, iEType=10, iMethod=1, crProp=None, dlOrient=[], crlMasterTarget=[], crlSlaveTarget=[]):
        message = "Connections.BarBeam('{}',{},{},{},{},{},{})".format(strName, iEType, iMethod, crProp, dlOrient, crlMasterTarget, crlSlaveTarget)
        return JPT_RUN_LINE(message)

    def GapsDetail(crlMaster=[], crlSlave=[], iMethod=0, iOriMode=0, crCoord=None, strName="", dU0=DFLT_DBL, dF0=DFLT_DBL, dKa=DFLT_DBL, dKb=DFLT_DBL, dKt=DFLT_DBL, dMar=DFLT_DBL, dMu1=DFLT_DBL, dMu2=DFLT_DBL, dlOriVec=[], dTmax=DFLT_DBL, dTol=DFLT_DBL, dTrmin=DFLT_DBL, crEditCur=None):
        message = "Connections.GapsDetail({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

    def Plot(strName="PLOT_1", iPID=1, crlTarget=[], crEdit=None):
        message = "Connections.Plot('{}',{},{},{})".format(strName, iPID, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def CreateConnConm(strName, iEType, iMethod, iCoordSys, iConmId, crMatCoord, dMass, dlX=[0, 0, 0], dlVintertia0=[0, 0, 0], dlVintertia1=[0, 0, 0]):
        message = "Connections.CreateConnConm('{}',{},{},{},{},{},{},{},{},{})".format(strName, iEType, iMethod, iCoordSys, iConmId, crMatCoord, dMass, dlX, dlVintertia0, dlVintertia1)
        return JPT_RUN_LINE(message)

    def RBE3(iMethod=0, crlMasterTarget=[], crlSlaveTarget=[], listRbe3TermConnection=[], iTypeRBE3=3, strName="", crCoordSys=None, dTolerance=0.0, posVirtualNodePos=[0, 0, 0], iSurfaceDef=0, crEdit=None, bUpdateDispCS=True, bCornerOnly=False):
        message = "Connections.RBE3({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRbe3TermConnection, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly)
        return JPT_RUN_LINE(message)

    def RigidWall(strName="RigidWall1", iObject=0, iType=0, iMotion=0, iFriction=0, iOrtho=0, iForces=0, dFinite1=DFLT_DBL, dFinite2=DFLT_DBL, dMotionMass=DFLT_DBL, dMotionInitVelo=DFLT_DBL, dFricCoulombCoeff=DFLT_DBL, dFricWeldVelo=DFLT_DBL, iForcesCirclesNum=0, dOrthoStaticCoeff1=DFLT_DBL, dOrthoStaticCoeff2=DFLT_DBL, dOrthoDynamicCoeff1=DFLT_DBL, dOrthoDynamicCoeff2=DFLT_DBL, dOrthoDecayConst1=DFLT_DBL, dOrthoDecayConst2=DFLT_DBL, dOrthoFricVector1=DFLT_DBL, dOrthoFricVector2=DFLT_DBL, dOrthoFricVector3=DFLT_DBL, bAllNodeSlave=False, crCoord=None, crAreaFaceSet=None, crVisualNodeSet=None, crlTarget=[], crEdit=None):
        message = "Connections.RigidWall('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iObject, iType, iMotion, iFriction, iOrtho, iForces, dFinite1, dFinite2, dMotionMass, dMotionInitVelo, dFricCoulombCoeff, dFricWeldVelo, iForcesCirclesNum, dOrthoStaticCoeff1, dOrthoStaticCoeff2, dOrthoDynamicCoeff1, dOrthoDynamicCoeff2, dOrthoDecayConst1, dOrthoDecayConst2, dOrthoFricVector1, dOrthoFricVector2, dOrthoFricVector3, bAllNodeSlave, crCoord, crAreaFaceSet, crVisualNodeSet, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Connector(strName="", iMethod=1, iConnectType=0, iRefNode=0, iElemCs=0, crLocalCS=None, crlElasticity=[], crlDamp=[], crlMasterTarget=[], crlSlaveTarget=[], crEdit=None):
        message = "Connections.Connector('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, iMethod, iConnectType, iRefNode, iElemCs, crLocalCS, crlElasticity, crlDamp, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

    def BoltMeshingSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE_MESH(), bLBCPRETENSIONABAQUSDATABfixedlenght=False, crLBCPRETENSIONABAQUSDATACrtable=None, dLBCPRETENSIONABAQUSDATADvalue=0.0, iLBCPRETENSIONABAQUSDATAIlocalunit=0, strLBCPRETENSIONABAQUSDATAStrnormal="", posLBCPRETENSIONABAQUSDATATvctrolnodepos=[0,0,0], crlTarget=[], poslCutter=[]):
        message = "Connections.BoltMeshingSplitOnly('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iPartcutparamImethod, dPartcutparamDoffset, iPartcutparamBshareface, iPartcutparamBseparateface, iPartcutparamBsplitonly, iPartcutparamBmakesectionface, crPartcutparamCoord, surfaceMesh, bLBCPRETENSIONABAQUSDATABfixedlenght, crLBCPRETENSIONABAQUSDATACrtable, dLBCPRETENSIONABAQUSDATADvalue, iLBCPRETENSIONABAQUSDATAIlocalunit, strLBCPRETENSIONABAQUSDATAStrnormal, posLBCPRETENSIONABAQUSDATATvctrolnodepos, crlTarget, poslCutter)
        return JPT_RUN_LINE(message)

    def BoltMeshingNotSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE_MESH(), iLBCPRETENSIONDATAIdir=0, dLBCPRETENSIONDATADvalue=0.0, bLBCPRETENSIONDATABfixlength=False, crLBCPRETENSIONDATACrtable=None, crLBCPRETENSIONDATACrcoord=None, iLBCPRETENSIONDATAIlocalunit=0, crlTarget=[], poslCutter=[]):
        message = "Connections.BoltMeshingNotSplitOnly('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPartcutparamImethod, dPartcutparamDoffset, iPartcutparamBshareface, iPartcutparamBseparateface, iPartcutparamBsplitonly, iPartcutparamBmakesectionface, crPartcutparamCoord, surfaceMesh, iLBCPRETENSIONDATAIdir, dLBCPRETENSIONDATADvalue, bLBCPRETENSIONDATABfixlength, crLBCPRETENSIONDATACrtable, crLBCPRETENSIONDATACrcoord, iLBCPRETENSIONDATAIlocalunit, crlTarget, poslCutter)
        return JPT_RUN_LINE(message)

    BoltConnections = Connections_BoltConnections()

    Contacts = Connections_Contacts()

    Gaps = Connections_Gaps()

    MPC = Connections_MPC()

    RigidElements = Connections_RigidElements()

    SpringsDampers = Connections_SpringsDampers()

class Designer:
    LBC = Designer_LBC()

    Load = Designer_Load()

    def ContactMerge(crlTarget):
        message = "Designer.ContactMerge({})".format(crlTarget)
        return JPT_RUN_LINE(message)

    def Material(strMatName, strPropName, dThickness, crlTarget):
        message = "Designer.Material('{}','{}',{},{})".format(strMatName, strPropName, dThickness, crlTarget)
        return JPT_RUN_LINE(message)

class EngReliability:
    def SubModelBC(strName, crlTarget, iPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleR, vecOffset, vecRotate, dScaleT, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet):
        message = "EngReliability.SubModelBC('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName, crlTarget, iPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleR, vecOffset, vecRotate, dScaleT, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
        return JPT_RUN_LINE(message)

class ExManifoldModeling:
    SZ = ExManifoldModeling_SZ()

class Geometry:
    Bar = Geometry_Bar()

    BodyCut = Geometry_BodyCut()

    BreakEntity = Geometry_BreakEntity()

    DeleteEntity = Geometry_DeleteEntity()

    Edge = Geometry_Edge()

    ExtractSurfaces = Geometry_ExtractSurfaces()

    Face = Geometry_Face()

    FindFeature = Geometry_FindFeature()

    MergeEntities = Geometry_MergeEntities()

    Part = Geometry_Part()

    ShowAdjacent = Geometry_ShowAdjacent()

    Transform = Geometry_Transform()

    def CADTrim(crlFace, crlPart, dTrimSize=1, dTrimAngle=15):
        message = "Geometry.CADTrim({},{},{},{})".format(crlFace, crlPart, dTrimSize, dTrimAngle)
        return JPT_RUN_LINE(message)

    def StitchEdge(dTolerance=0.3, bKeepSlave=True, crlMaster=[], crlSlave=[]):
        message = "Geometry.StitchEdge({},{},{},{})".format(dTolerance, bKeepSlave, crlMaster, crlSlave)
        return JPT_RUN_LINE(message)

    def LogoRemoval(crlStartFaces=[], crlStopFaces=[], iLayers=5, bMergeFaces=False):
        message = "Geometry.LogoRemoval({},{},{},{})".format(crlStartFaces, crlStopFaces, iLayers, bMergeFaces)
        return JPT_RUN_LINE(message)

    def ShellAsm(crlPartK=[], crlFaceK=[], dTol=0.2, iElemType=0, bSkipTiny=False):
        message = "Geometry.ShellAsm({},{},{},{},{})".format(crlPartK, crlFaceK, dTol, iElemType, bSkipTiny)
        return JPT_RUN_LINE(message)

    def SquareUpFillet(crlFace=[]):
        message = "Geometry.SquareUpFillet({})".format(crlFace)
        return JPT_RUN_LINE(message)

    def MakeFillet(crlEdge=[], dRadius=1.0):
        message = "Geometry.MakeFillet({},{})".format(crlEdge, dRadius)
        return JPT_RUN_LINE(message)

    def MakeFacePlanar(dlPlanePt1=[0.0,0.0,0.0], dlPlanePt2=[0.0,0.0,0.0], dlPlanePt3=[0.0,0.0,0.0], ilFaceIds=[], iMergeFace=0):
        message = "Geometry.MakeFacePlanar({},{},{},{},{})".format(dlPlanePt1, dlPlanePt2, dlPlanePt3, ilFaceIds, iMergeFace)
        return JPT_RUN_LINE(message)

    def FCircleAdjustVertex(crlPart=[]):
        message = "Geometry.FCircleAdjustVertex({})".format(crlPart)
        return JPT_RUN_LINE(message)

    def AdjustHalfCylinder(poslPoint=[], crlFace=[], crCoord=None, iAxisPlane=0, bDivideFace=True, crlPart=[], bMergeEdge=True):
        message = "Geometry.AdjustHalfCylinder({},{},{},{},{},{},{})".format(poslPoint, crlFace, crCoord, iAxisPlane, bDivideFace, crlPart, bMergeEdge)
        return JPT_RUN_LINE(message)

    def FCircVertexAdjust(crlPart, dMinRadius=0.0, bFullCylinder=True, bCylinderMorethan90=False, bSkipFaceHaveLocalSetting=False):
        message = "Geometry.FCircVertexAdjust({},{},{},{},{})".format(crlPart, dMinRadius, bFullCylinder, bCylinderMorethan90, bSkipFaceHaveLocalSetting)
        return JPT_RUN_LINE(message)

    def ExtractSurfaces(crlFace, dAngle=60.0, strName="ExtractFace_1", bMergePart=False):
        message = "Geometry.ExtractSurfaces({},{},'{}',{})".format(crlFace, dAngle, strName, bMergePart)
        return JPT_RUN_LINE(message)

    def RemoveRibBoss(crlFace, dGradiation=1.0, iContinuity=1):
        message = "Geometry.RemoveRibBoss({},{},{})".format(crlFace, dGradiation, iContinuity)
        return JPT_RUN_LINE(message)

    def AdvancedShellAssembly(crlPart=[], crlFace=[], iMeshType=0, bSelfIntersection=False, iMethod=3, dGapTol=2.1):
        message = "Geometry.AdvancedShellAssembly({},{},{},{},{},{})".format(crlPart, crlFace, iMeshType, bSelfIntersection, iMethod, dGapTol)
        return JPT_RUN_LINE(message)

    def ExtractRefSurface(crlFace, dAngle=60.0, strName="ExtractFace_1", bMergePart=False):
        message = "Geometry.ExtractRefSurface({},{},'{}',{})".format(crlFace, dAngle, strName, bMergePart)
        return JPT_RUN_LINE(message)

class Groups:
    RightClick = Groups_RightClick()

class HexModeling:
    Sweep = HexModeling_Sweep()

    def SolidElemInterface(crlFace=[], bFlip=False, crlElms=[]):
        message = "HexModeling.SolidElemInterface({},{},{})".format(crlFace, bFlip, crlElms)
        return JPT_RUN_LINE(message)

    def BallHexa(crPart, vecCenter=[0.0,0.0,0.0], dRadius=5.0, dMeshSize=0.5, iType=0, iLayer=3, bMakeCenterNode=True, strPartName="HexBall_1"):
        message = "HexModeling.BallHexa({},{},{},{},{},{},{},'{}')".format(crPart, vecCenter, dRadius, dMeshSize, iType, iLayer, bMakeCenterNode, strPartName)
        return JPT_RUN_LINE(message)

    def BoxMesh(ilPartIds, dMeshSize, strMaterialName):
        message = "HexModeling.BoxMesh({},{},'{}')".format(ilPartIds, dMeshSize, strMaterialName)
        return JPT_RUN_LINE(message)

    def AutoSweep(crlPart=[], dMeshSize=0.0, bLayers=False, iLayers=2):
        message = "HexModeling.AutoSweep({},{},{},{})".format(crlPart, dMeshSize, bLayers, iLayers)
        return JPT_RUN_LINE(message)

    def Circular(crlFace=[], dAngle=360, dTol=0.0000001, iLayer=36, vecAxisPt=[0.0,0.0,0.0], vecAxisVect=[1.0,0.0,0.0], bInterfaceElem=False, bExtrusion=False, dTranslationExtrusion=0.0, dBDeleteOriginalParts=0.0):
        message = "HexModeling.Circular({},{},{},{},{},{},{},{},{},{})".format(crlFace, dAngle, dTol, iLayer, vecAxisPt, vecAxisVect, bInterfaceElem, bExtrusion, dTranslationExtrusion, dBDeleteOriginalParts)
        return JPT_RUN_LINE(message)

    def FaceToFace(crSrcFace, crDstFace, bDeleteOriginalParts=True):
        message = "HexModeling.FaceToFace({},{},{})".format(crSrcFace, crDstFace, bDeleteOriginalParts)
        return JPT_RUN_LINE(message)

    def Layer(crlFace=[], dFrontWidth=0.0, dBackWidth=0.0, iFrontLayers=1, iBackLayers=0, iBaseFaceType=0, iSeparate=0):
        message = "HexModeling.Layer({},{},{},{},{},{},{})".format(crlFace, dFrontWidth, dBackWidth, iFrontLayers, iBackLayers, iBaseFaceType, iSeparate)
        return JPT_RUN_LINE(message)

    def Linear(crlFace=[], dLength=10, iLayer=10, vecSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0):
        message = "HexModeling.Linear({},{},{},{},{},{},{},{},{},{},{})".format(crlFace, dLength, iLayer, vecSweepDirection, bInterfaceElemFlag, iLinearMethod, bDeleteOriginalParts, bDeleteTargetParts, iMethodBias, dFactor, iProgression)
        return JPT_RUN_LINE(message)

    def FromMidPlane(crlPart=[], bRef=True):
        message = "HexModeling.FromMidPlane({},{})".format(crlPart, bRef)
        return JPT_RUN_LINE(message)

    def Curve(crFace=None, crlEdge=[], crlRefEdge=[], dMeshSize=0.1):
        message = "HexModeling.Curve({},{},{},{})".format(crFace, crlEdge, crlRefEdge, dMeshSize)
        return JPT_RUN_LINE(message)

class Home:
    ImportCAD = Home_ImportCAD()

    ImportMesh = Home_ImportMesh()

    def ExportSTL(strFile="", crlPart=[], dScale=1, bFilterIndex=False):
        message = "Home.ExportSTL('{}',{},{},{})".format(strFile, crlPart, dScale, bFilterIndex)
        return JPT_RUN_LINE(message)

    def ExportGeometryBDF(strFileName, crlPart=[], bBigID=False, bUseUnit=True, bVert=True, bEdge=True, bFace=True, bSolid=True):
        message = "Home.ExportGeometryBDF('{}',{},{},{},{},{},{},{})".format(strFileName, crlPart, bBigID, bUseUnit, bVert, bEdge, bFace, bSolid)
        return JPT_RUN_LINE(message)

    def ToImage(strImgPath, bWhiteBG=False, bTransparentBG=False, bFixedSize=False, iExportWidth=1200, iExportHeight=900):
        message = "Home.ToImage('{}',{},{},{},{},{})".format(strImgPath, bWhiteBG, bTransparentBG, bFixedSize, iExportWidth, iExportHeight)
        return JPT_RUN_LINE(message)

    def Find(strSearch="", strSeletedType="Part", bFindMatch=False):
        message = "Home.Find('{}','{}',{})".format(strSearch, strSeletedType, bFindMatch)
        return JPT_RUN_LINE(message)

    def RectangularCapture(iLeft=0, iTop=0, iRight=0, iBottom=0):
        message = "Home.RectangularCapture({},{},{},{})".format(iLeft, iTop, iRight, iBottom)
        return JPT_RUN_LINE(message)

    def CopyToClipboard(bWhiteBG=False, bTransparentBG=False, bFixedSize=False, iWidth=1200, iHeight=900):
        message = "Home.CopyToClipboard({},{},{},{},{})".format(bWhiteBG, bTransparentBG, bFixedSize, iWidth, iHeight)
        return JPT_RUN_LINE(message)

    def FullScreen():
        message = "Home.FullScreen({})".format('')
        return JPT_RUN_LINE(message)

    def Synchronize():
        message = "Home.Synchronize({})".format('')
        return JPT_RUN_LINE(message)

class MainWindow:
    RightClick = MainWindow_RightClick()

class MeshCleanup:
    Element = MeshCleanup_Element()

    def Face(crlFace=[], crlPart=[], bCreateNewPart=False):
        message = "MeshCleanup.Face({},{},{})".format(crlFace, crlPart, bCreateNewPart)
        return JPT_RUN_LINE(message)

    def CorrectModel(crlPart, iEnableBreakEdge=0, dEdgeAngle=0, iEnableMergeEdge=0, dMergeEdgeAngle=0, iEnableMergePlanarFace=0, iEnableRemoveExtraVertex=0):
        message = "MeshCleanup.CorrectModel({},{},{},{},{},{},{})".format(crlPart, iEnableBreakEdge, dEdgeAngle, iEnableMergeEdge, dMergeEdgeAngle, iEnableMergePlanarFace, iEnableRemoveExtraVertex)
        return JPT_RUN_LINE(message)

    def CloseHoles(crlEdge=[], dAreaMin=0.0, dAreaMax=543210.0, bMergeFace=False, bMergeEdge=False):
        message = "MeshCleanup.CloseHoles({},{},{},{},{})".format(crlEdge, dAreaMin, dAreaMax, bMergeFace, bMergeEdge)
        return JPT_RUN_LINE(message)

    def CloseGap(crlPartCur=[], dDistanceTol=0.01):
        message = "MeshCleanup.CloseGap({},{})".format(crlPartCur, dDistanceTol)
        return JPT_RUN_LINE(message)

    def AutoCheck(crlPart, iElemType, blCheckCondition, blElemQuality, dlLimitValue, crlElem):
        message = "MeshCleanup.AutoCheck({},{},{},{},{},{})".format(crlPart, iElemType, blCheckCondition, blElemQuality, dlLimitValue, crlElem)
        return JPT_RUN_LINE(message)

    def ManualCheck(crlPart=[], iElemType=0, iVeQuality=0, iCheckCondition=0, dLimitValue=0.0, dCFLValue=0.0, iNonManifold=0, iCleanupMode=0, crlElem=[]):
        message = "MeshCleanup.ManualCheck({},{},{},{},{},{},{},{},{})".format(crlPart, iElemType, iVeQuality, iCheckCondition, dLimitValue, dCFLValue, iNonManifold, iCleanupMode, crlElem)
        return JPT_RUN_LINE(message)

    ChangeTopology = MeshCleanup_ChangeTopology()

    Cleanup = MeshCleanup_Cleanup()

    Manual2D = MeshCleanup_Manual2D()

    Manual3D = MeshCleanup_Manual3D()

    ManualCheck = MeshCleanup_ManualCheck()

class MeshEdit:
    CreateElement = MeshEdit_CreateElement()

    CreateNode = MeshEdit_CreateNode()

    MoveNode = MeshEdit_MoveNode()

    def Face(crlFace, crlFaceFixed, iOffsetType=0, crCoord=None, dlOffset=[1.0, 0.0, 0.0], dOffset=0, iDistType=0, dDistStrong=10, dDistWeak=20, iNodeIdPick=-1, dlPickForMacro=[]):
        message = "MeshEdit.Face({},{},{},{},{},{},{},{},{},{},{})".format(crlFace, crlFaceFixed, iOffsetType, crCoord, dlOffset, dOffset, iDistType, dDistStrong, dDistWeak, iNodeIdPick, dlPickForMacro)
        return JPT_RUN_LINE(message)

    def ElementConvert(crlPart=[], iType=1):
        message = "MeshEdit.ElementConvert({},{})".format(crlPart, iType)
        return JPT_RUN_LINE(message)

    def Deform(crlFaceSrcObverse=[], crlFaceDstReverse=[], crlFaceSrcReverse=[], crlFaceDstObverse=[], crlFaceFixed=[], dDistEffect=0.02):
        message = "MeshEdit.Deform({},{},{},{},{},{})".format(crlFaceSrcObverse, crlFaceDstReverse, crlFaceSrcReverse, crlFaceDstObverse, crlFaceFixed, dDistEffect)
        return JPT_RUN_LINE(message)

    def MirrorCopy(crlFace=[]):
        message = "MeshEdit.MirrorCopy({})".format(crlFace)
        return JPT_RUN_LINE(message)

    def DeleteNode(crlNode=[], bRemoveVertex=True):
        message = "MeshEdit.DeleteNode({},{})".format(crlNode, bRemoveVertex)
        return JPT_RUN_LINE(message)

    def FaceImprint(crlFaces=[], bMeshCopy=False):
        message = "MeshEdit.FaceImprint({},{})".format(crlFaces, bMeshCopy)
        return JPT_RUN_LINE(message)

    def AdjustOrientation(crlPart=[], crlFace=[], crlElem=[]):
        message = "MeshEdit.AdjustOrientation({},{},{})".format(crlPart, crlFace, crlElem)
        return JPT_RUN_LINE(message)

    def OneNode(crlNode=[], crlFaceFixed=[], bOffsetvector=False, crCoord=None, dlOffset=[0, 1, 0], dOffset=1.0, iDisttype=0, dDiststrong=10, dDistweak=20):
        message = "MeshEdit.OneNode({},{},{},{},{},{},{},'{}',{})".format(crlNode, crlFaceFixed, bOffsetvector, crCoord, dlOffset, dOffset, iDisttype, dDiststrong, dDistweak)
        return JPT_RUN_LINE(message)

    def SeparateNodes(crlShareNodes=[], crlTarget=[], iKeepNodeIDsOn=0):
        message = "MeshEdit.SeparateNodes({},{},{})".format(crlShareNodes, crlTarget, iKeepNodeIDsOn)
        return JPT_RUN_LINE(message)

    def RefineQuality(iMetric, crlFace, crlElem, crlNode):
        message = "MeshEdit.RefineQuality({},{},{},{})".format(iMetric, crlFace, crlElem, crlNode)
        return JPT_RUN_LINE(message)

    def Import(iSolverType=0, strFilePath="", iStep=0, dScale=1.0):
        message = "MeshEdit.Import({},'{}',{},{})".format(iSolverType, strFilePath, iStep, dScale)
        return JPT_RUN_LINE(message)

    def RemoveSolidMesh(crlPart=[], bConvFirst=False):
        message = "MeshEdit.RemoveSolidMesh({},{})".format(crlPart, bConvFirst)
        return JPT_RUN_LINE(message)

    def MergeNodes(dTolerance=0.01, iKeepType=0, crlTarget=[], bGroup=False, bEquivalence=True):
        message = "MeshEdit.MergeNodes({},{},{},{},{})".format(dTolerance, iKeepType, crlTarget, bGroup, bEquivalence)
        return JPT_RUN_LINE(message)

    def MeshCopy(crlFace=[], crlNode=[]):
        message = "MeshEdit.MeshCopy({},{})".format(crlFace, crlNode)
        return JPT_RUN_LINE(message)

    def RibThickness(crlFaceMove=[], crlFaceFixed=[], dMove=3.00, dDistStrong=10.00, dDistWeak=20.00):
        message = "MeshEdit.RibThickness({},{},{},{},{})".format(crlFaceMove, crlFaceFixed, dMove, dDistStrong, dDistWeak)
        return JPT_RUN_LINE(message)

    def ChangePattern(crlFace=[], iPatternType=0):
        message = "MeshEdit.ChangePattern({},{})".format(crlFace, iPatternType)
        return JPT_RUN_LINE(message)

    def SurfaceMesh(crlPart=[], iType=1):
        message = "MeshEdit.SurfaceMesh({},{})".format(crlPart, iType)
        return JPT_RUN_LINE(message)

    def SolidMesh(crlPart=[], iType=1):
        message = "MeshEdit.SolidMesh({},{})".format(crlPart, iType)
        return JPT_RUN_LINE(message)

    def DividePartByRegion(crlPart=[], crlBoundaryParts=[]):
        message = "MeshEdit.DividePartByRegion({},{})".format(crlPart, crlBoundaryParts)
        return JPT_RUN_LINE(message)

class Meshing:
    CADProjection = Meshing_CADProjection()

    LocalMeshing = Meshing_LocalMeshing()

    LocalSetting = Meshing_LocalSetting()

    Templates = Meshing_Templates()

    def BarMeshing(crlCadEdge, crlBarEdge, crlBarPart, dDocMeshSize=0, iDocNumofElem=4):
        message = "Meshing.BarMeshing({},{},{},{},{})".format(crlCadEdge, crlBarEdge, crlBarPart, dDocMeshSize, iDocNumofElem)
        return JPT_RUN_LINE(message)

    def GridMesh(listGridMesh, bLocalsetting=True):
        message = "Meshing.GridMesh({},{})".format(listGridMesh, bLocalsetting)
        return JPT_RUN_LINE(message)

    def SolidMeshing(crlPart=[], bTet10=False, dGradingFactor=0, bGravCenter=False, dStretchLimit=0, iSpeedVsQual=0, iSpeedVsMem=0, iRegion=0, bInternalNodes=True, bSafeMode=True, iParallel=0, bSurfaceNodes=True, bEdgeNodes=True, bPreservation=True, bInternalMeshOnly=True, bMeshColor=False, iPartColor=2763429):
        message = "Meshing.SolidMeshing({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, bTet10, dGradingFactor, bGravCenter, dStretchLimit, iSpeedVsQual, iSpeedVsMem, iRegion, bInternalNodes, bSafeMode, iParallel, bSurfaceNodes, bEdgeNodes, bPreservation, bInternalMeshOnly, bMeshColor, iPartColor)
        return JPT_RUN_LINE(message)

    def SurfaceMeshing(crlPart=[], surfaceMesh=SURFACE_MESH(), bUseSetting=True, bFMesher=False, iThreadNum=8, bRefData=True, bMeshColor=False, iPartColor=65280):
        message = "Meshing.SurfaceMeshing({},{},{},{},{},{},{},{})".format(crlPart, surfaceMesh, bUseSetting, bFMesher, iThreadNum, bRefData, bMeshColor, iPartColor)
        return JPT_RUN_LINE(message)

    def SetAttib(crlPart = [], surfaceMesh = SURFACE_MESH()):
        message = "Meshing.SetAttib({},{})".format(crlPart , surfaceMesh )
        return JPT_RUN_LINE(message)

    LocalRemesh = Meshing_LocalRemesh()

    LocalSettings = Meshing_LocalSettings()

class MidPlane:
    def AdjustThickness(crlPart=[], dRatio=1.0, bAdjustFaceThick=False, bAdjustPropThick=False):
        message = "MidPlane.AdjustThickness({},{},{},{})".format(crlPart, dRatio, bAdjustFaceThick, bAdjustPropThick)
        return JPT_RUN_LINE(message)

    def FaceCross(crlBodies=[], crlFaces=[]):
        message = "MidPlane.FaceCross({},{})".format(crlBodies, crlFaces)
        return JPT_RUN_LINE(message)

    def CreateThickProps(crlPart=[], dThickDiff=0.1, dMaxThick=DFLT_DBL, dMinThick=DFLT_DBL, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, iMatOrientType=0, dMatOrientX=DFLT_DBL, dMatOrientY=DFLT_DBL, dMatOrientZ=DFLT_DBL, crCoord=None, dThickness=DFLT_DBL, dBendStiff=DFLT_DBL, dThickRatio=1, dNSM=DFLT_DBL, dFiberDist1=DFLT_DBL, dFiberDist2=DFLT_DBL, dPlateOff=DFLT_DBL, iNumInterPts=0, bThickSetting=False, iEntityType=0, bDivideProp=False, crlRefPart=[]):
        message = "MidPlane.CreateThickProps({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, dThickDiff, dMaxThick, dMinThick, crMatMembrane, crMatBend, crMatShear, crMatCoupl, iMatOrientType, dMatOrientX, dMatOrientY, dMatOrientZ, crCoord, dThickness, dBendStiff, dThickRatio, dNSM, dFiberDist1, dFiberDist2, dPlateOff, iNumInterPts, bThickSetting, iEntityType, bDivideProp, crlRefPart)
        return JPT_RUN_LINE(message)

    def FindMidPlane():
        message = "MidPlane.FindMidPlane({})".format('')
        return JPT_RUN_LINE(message)

class MidPlaneEdit:
    Edge = MidPlaneEdit_Edge()

    ExtendFace = MidPlaneEdit_ExtendFace()

    Face = MidPlaneEdit_Face()

    Manual = MidPlaneEdit_Manual()

    AddItems = MidPlaneEdit_AddItems()

class MMCCarACTools:
    ACModelCreationTools = MMCCarACTools_ACModelCreationTools()

    ClearanceElement = MMCCarACTools_ClearanceElement()

class MufflerHA:
    CreateEdge = MufflerHA_CreateEdge()

    CreateEdgeClassic = MufflerHA_CreateEdgeClassic()

    def CopyMeshCount(crlMasterEdge, crlSlaveEdge, strBaseName):
        message = "MufflerHA.CopyMeshCount({},{},'{}')".format(crlMasterEdge, crlSlaveEdge, strBaseName)
        return JPT_RUN_LINE(message)

class MufflerT:
    SpecialModeling = MufflerT_SpecialModeling()

class MuxWeld:
    CreateWeld = MuxWeld_CreateWeld()

    DefineSequence = MuxWeld_DefineSequence()

    def MeshingPass(crPart=None, crlEdge=[], dMeshSize=0.0):
        message = "MuxWeld.MeshingPass({},{},{})".format(crPart, crlEdge, dMeshSize)
        return JPT_RUN_LINE(message)

    def Prop3DWeldBead(strName="Bead_1", crMaterial=None, crlTarget=[], crEdit=None):
        message = "MuxWeld.Prop3DWeldBead('{}',{},{},{})".format(strName, crMaterial, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class NSModeling:
    def NSModeling_Close_Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNode, crlPart):
        message = "NSModeling.NSModeling_Close_Hole({},{},{},{},{},{})".format(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNode, crlPart)
        return JPT_RUN_LINE(message)

class OasisAWizard:
    LocalMeshing = OasisAWizard_LocalMeshing()

class Post:
    ImportResults = Post_ImportResults()

class Properties:
    ElemRelatedInfo = Properties_ElemRelatedInfo()

    Material = Properties_Material()

    Section = Properties_Section()

    def Cohesive(strName, crMaterial, iResponse, bSpecifyThick, dInitialThick, crlTarget, crEdit=None, iFLG=0, iId=0, iSolverType=0, iADVCResponseType=0, iADVCStackDir=0, iEnableADVCThickness=0, dADVCThickness=DFLT_DBL):
        message = "Properties.Cohesive('{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, crMaterial, iResponse, bSpecifyThick, dInitialThick, crlTarget, crEdit, iFLG, iId, iSolverType, iADVCResponseType, iADVCStackDir, iEnableADVCThickness, dADVCThickness)
        return JPT_RUN_LINE(message)

    def Gasket(strName, crMaterial, dThickX, dThickY, dThickZ, crlTarget, crEdit=None, iStData=0, iFLG=0):
        message = "Properties.Gasket('{}',{},{},{},{},{},{},{},{})".format(strName, crMaterial, dThickX, dThickY, dThickZ, crlTarget, crEdit, iStData, iFLG)
        return JPT_RUN_LINE(message)

    def Shell(strName="Shell Property", iPID=1, crMatMembrane=None, crMatBend=None, crMatShear=None, crMatCoupl=None, dMatOrient1=0.0, dMatOrient2=0.0, dMatOrient3=0.0, dThickness=1, dBendStiff=0.0, dThickRatio=0.5, dNSM=0.0, dFiberDist1=0.0, dFiberDist2=0.0, dPlateOff=0.0, iItgPts=0, iMatOrientType=0, crLocalCS=None, crlTarget=[], crEdit=None, iDuplicateOpt=0):
        message = "Properties.Shell('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPID, crMatMembrane, crMatBend, crMatShear, crMatCoupl, dMatOrient1, dMatOrient2, dMatOrient3, dThickness, dBendStiff, dThickRatio, dNSM, dFiberDist1, dFiberDist2, dPlateOff, iItgPts, iMatOrientType, crLocalCS, crlTarget, crEdit, iDuplicateOpt)
        return JPT_RUN_LINE(message)

    def PropertyTable(listRenumberProp=[]):
        message = "Properties.PropertyTable({})".format(listRenumberProp)
        return JPT_RUN_LINE(message)

    def Beam(strNewName="BEAM1", iPId=1, crSection=None, iShapeDataType=0, crMat=None, dArea=0.0, dlVecOrient=[0,0,0], dlVecInertia=[0,0,0], dTorConst=0.0, dNSM=DFLT_DBL, dNSMA=DFLT_DBL, dNSMB=DFLT_DBL, dNSMNode1=DFLT_DBL, dNSMNode2=DFLT_DBL, dNSMNode3=DFLT_DBL, dNSMNode4=DFLT_DBL, dShearStiffnessK1=0.0, dShearStiffnessK2=0.0, dShearAreaReliefS1=DFLT_DBL, dShearAreaReliefS2=DFLT_DBL, dWrapCoeff1=DFLT_DBL, dWrapCoeff2=DFLT_DBL, dNA1=DFLT_DBL, dNA2=DFLT_DBL, dNA3=DFLT_DBL, dNA4=DFLT_DBL, dStressRecoveryCoeffCy=0.0, dStressRecoveryCoeffCz=0.0, dStressRecoveryCoeffDy=0.0, dStressRecoveryCoeffDz=0.0, dStressRecoveryCoeffEy=0.0, dStressRecoveryCoeffEz=0.0, dStressRecoveryCoeffFy=0.0, dStressRecoveryCoeffFz=0.0, bPinA1=False, bPinA2=False, bPinA3=False, bPinA4=False, bPinA5=False, bPinA6=False, bPinB1=False, bPinB2=False, bPinB3=False, bPinB4=False, bPinB5=False, bPinB6=False, dlOffsetA=[DFLT_DBL,DFLT_DBL,DFLT_DBL], dlOffsetB=[DFLT_DBL,DFLT_DBL,DFLT_DBL], iLengthUnit=0, iMassUnit=0, crlTarget=[], crEdit=None, bTapped=False, dTapArea=DFLT_DBL, dlVecTapInertia=[DFLT_DBL,DFLT_DBL,DFLT_DBL], dTapTorConst=DFLT_DBL, dTapNSM=DFLT_DBL, dTapStressRecoveryCoeffCy=DFLT_DBL, dTapStressRecoveryCoeffCz=DFLT_DBL, dTapStressRecoveryCoeffDy=DFLT_DBL, dTapStressRecoveryCoeffDz=DFLT_DBL, dTapStressRecoveryCoeffEy=DFLT_DBL, dTapStressRecoveryCoeffEz=DFLT_DBL, dTapStressRecoveryCoeffFy=DFLT_DBL, dTapStressRecoveryCoeffFz=DFLT_DBL, iIntePtNum=DFLT_INT):
        message = "Properties.Beam('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strNewName, iPId, crSection, iShapeDataType, crMat, dArea, dlVecOrient, dlVecInertia, dTorConst, dNSM, dNSMA, dNSMB, dNSMNode1, dNSMNode2, dNSMNode3, dNSMNode4, dShearStiffnessK1, dShearStiffnessK2, dShearAreaReliefS1, dShearAreaReliefS2, dWrapCoeff1, dWrapCoeff2, dNA1, dNA2, dNA3, dNA4, dStressRecoveryCoeffCy, dStressRecoveryCoeffCz, dStressRecoveryCoeffDy, dStressRecoveryCoeffDz, dStressRecoveryCoeffEy, dStressRecoveryCoeffEz, dStressRecoveryCoeffFy, dStressRecoveryCoeffFz, bPinA1, bPinA2, bPinA3, bPinA4, bPinA5, bPinA6, bPinB1, bPinB2, bPinB3, bPinB4, bPinB5, bPinB6, dlOffsetA, dlOffsetB, iLengthUnit, iMassUnit, crlTarget, crEdit, bTapped, dTapArea, dlVecTapInertia, dTapTorConst, dTapNSM, dTapStressRecoveryCoeffCy, dTapStressRecoveryCoeffCz, dTapStressRecoveryCoeffDy, dTapStressRecoveryCoeffDz, dTapStressRecoveryCoeffEy, dTapStressRecoveryCoeffEz, dTapStressRecoveryCoeffFy, dTapStressRecoveryCoeffFz, iIntePtNum)
        return JPT_RUN_LINE(message)

    def Rod(strName="", iId=1, crSection=None, crMat=None, dArea=DFLT_DBL, dTorConst=DFLT_DBL, dTorStressCoeff=DFLT_DBL, dNSM=DFLT_DBL, iLocalLengthUnit=0, iLocalMassUnit=0, crlTarget=[], crEdit=None):
        message = "Properties.Rod('{}',{},{},{},{},{},{},{},{},{},{},{})".format(strName, iId, crSection, crMat, dArea, dTorConst, dTorStressCoeff, dNSM, iLocalLengthUnit, iLocalMassUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Property1DBeamSimple(strName, iId, crSection=None, crMat=None, vecOrient=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crlTarget=[], crEdit=None):
        message = "Properties.Property1DBeamSimple('{}',{},{},{},{},{},{})".format(strName, iId, crSection, crMat, vecOrient, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Solid(strName="Solid Property", iPID=1, crMaterial=None, iCordM=0, iIN=0, iOutLoc=0, iISOP=0, iFLflag=0, iModifiedElem=0, iModifiedElemADVC=0, bHasDynaRemesh=False, dDynaRemeshVal1=0.0, dDynaRemeshVal2=0.0, iAbaqusPropHGtype=0, dDispHG=0.0, crlTarget=[], crEdit=None, iFLG=0):
        message = "Properties.Solid('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPID, crMaterial, iCordM, iIN, iOutLoc, iISOP, iFLflag, iModifiedElem, iModifiedElemADVC, bHasDynaRemesh, dDynaRemeshVal1, dDynaRemeshVal2, iAbaqusPropHGtype, dDispHG, crlTarget, crEdit, iFLG)
        return JPT_RUN_LINE(message)

    def Section1D(strName="", iSecType=0, iSecGentype=2, dSecGensizeA=0, dSecGensizeB=0, dSecGensizeH=0, dSecGensizeT1=0, dSecGensizeT2=0, dSecGensizeT3=0, bSecTapered=False, dSecGensizeATap=0, dSecGensizeBTap=0, dSecGensizeHTap=0, dSecGensizeT1Tap=0, dSecGensizeT2Tap=0, dSecGensizeT3Tap=0):
        message = "Properties.Section1D('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iSecType, iSecGentype, dSecGensizeA, dSecGensizeB, dSecGensizeH, dSecGensizeT1, dSecGensizeT2, dSecGensizeT3, bSecTapered, dSecGensizeATap, dSecGensizeBTap, dSecGensizeHTap, dSecGensizeT1Tap, dSecGensizeT2Tap, dSecGensizeT3Tap)
        return JPT_RUN_LINE(message)

    def Composite(strName="", iDFT=0, dGE=DFLT_DBL, iDLAM=0, crMat=None, dNSM=DFLT_DBL, iDPID=0, dSB=DFLT_DBL, iDSOUT=0, dTREF=DFLT_DBL, dZ0=DFLT_DBL, dZOFF=DFLT_DBL, crlTarget=[], crEdit=None, crDcrLocalCS=None, iDmatOrientType=0, vecDmatOrient=[DFLT_DBL, DFLT_DBL, DFLT_DBL]):
        message = "Properties.Composite('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDFT, dGE, iDLAM, crMat, dNSM, iDPID, dSB, iDSOUT, dTREF, dZ0, dZOFF, crlTarget, crEdit, crDcrLocalCS, iDmatOrientType, vecDmatOrient)
        return JPT_RUN_LINE(message)

    def BAR(strName="", iId=1, crSection=None, iShapeDataType=0, crDatacrMat=None, dDatadArea=DFLT_DBL, dlDataOrient=[0, 0, 0], dlDataInertia=[0, 0, 0], dDatadTorConst=DFLT_DBL, dDatadNSM=DFLT_DBL, dDataShearAreaFactor0=DFLT_DBL, dDataShearAreaFactor1=DFLT_DBL, dDataStressRecoveryCoeff0=DFLT_DBL, dDataStressRecoveryCoeff1=DFLT_DBL, dDataStressRecoveryCoeff2=DFLT_DBL, dDataStressRecoveryCoeff3=DFLT_DBL, dDataStressRecoveryCoeff4=DFLT_DBL, dDataStressRecoveryCoeff5=DFLT_DBL, dDataStressRecoveryCoeff6=DFLT_DBL, dDataStressRecoveryCoeff7=DFLT_DBL, bDataPinA0=False, bDataPinA1=False, bDataPinA2=False, bDataPinA3=False, bDataPinA4=False, bDataPinA5=False, bDataPinB0=False, bDataPinB1=False, bDataPinB2=False, bDataPinB3=False, bDataPinB4=False, bDataPinB5=False, dlDataOffset0=[DFLT_DBL, DFLT_DBL, DFLT_DBL], dlDataOffset1=[DFLT_DBL, DFLT_DBL, DFLT_DBL], iLocalLengthUnit=0, iLocalMassUnit=0, crlTarget=[], crEdit=None):
        message = "Properties.BAR('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iId, crSection, iShapeDataType, crDatacrMat, dDatadArea, dlDataOrient, dlDataInertia, dDatadTorConst, dDatadNSM, dDataShearAreaFactor0, dDataShearAreaFactor1, dDataStressRecoveryCoeff0, dDataStressRecoveryCoeff1, dDataStressRecoveryCoeff2, dDataStressRecoveryCoeff3, dDataStressRecoveryCoeff4, dDataStressRecoveryCoeff5, dDataStressRecoveryCoeff6, dDataStressRecoveryCoeff7, bDataPinA0, bDataPinA1, bDataPinA2, bDataPinA3, bDataPinA4, bDataPinA5, bDataPinB0, bDataPinB1, bDataPinB2, bDataPinB3, bDataPinB4, bDataPinB5, dlDataOffset0, dlDataOffset1, iLocalLengthUnit, iLocalMassUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ThicknessDistribution(dMax=1, dMin=0, iByEach=0, dlThicknessValueSet=[]):
        message = "Properties.ThicknessDistribution({},{},{},{})".format(dMax, dMin, iByEach, dlThicknessValueSet)
        return JPT_RUN_LINE(message)

    def RigidBody(strName="RigidBody1", iId=1, iRefNodeId=0, crlTarget=[], crEdit=None):
        message = "Properties.RigidBody('{}',{},{},{},{})".format(strName, iId, iRefNodeId, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class SNOnePush:
    DropTest = SNOnePush_DropTest()

    def CADImport(dDsurfaceplaneTolerance, dDsurfaceplaneAngle, dMaxFacetWidth, bBnxMultipart, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, iIigesFixedcurevepreference, iIigesAutostitch, dDigesStitchtolerance, iIcatiaConvertnotshowedelement, iIcatiaConvertnotshowedinstance, iIcatiaConvertaxis, iIstepCreateseam, dDstepPointtolerance, iIacisHealacisbeforeversion, iIjtConvertgeometrytype, iIjtConvertgeneralpart, iIjtConvertaxis, iIjtConvertcenterline, dDcreoChordheighttolerance, dDcreoAngletolerancedegree, strAbsCreoPath, iTransType, iFileType, strFilePath, bRenameDuplicateName, strCSVFilePath):
        message = "SNOnePush.CADImport({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},'{}',{},'{}')".format(dDsurfaceplaneTolerance, dDsurfaceplaneAngle, dMaxFacetWidth, bBnxMultipart, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, iIigesFixedcurevepreference, iIigesAutostitch, dDigesStitchtolerance, iIcatiaConvertnotshowedelement, iIcatiaConvertnotshowedinstance, iIcatiaConvertaxis, iIstepCreateseam, dDstepPointtolerance, iIacisHealacisbeforeversion, iIjtConvertgeometrytype, iIjtConvertgeneralpart, iIjtConvertaxis, iIjtConvertcenterline, dDcreoChordheighttolerance, dDcreoAngletolerancedegree, strAbsCreoPath, iTransType, iFileType, strFilePath, bRenameDuplicateName, strCSVFilePath)
        return JPT_RUN_LINE(message)

    def DropTestSNOnePush(strName="", iDir=0, dRopHeight=0.0, dSolutionTime=0.0, iNumOutput=20, dContactFriction=0.1, iRotAxis=0, dRotAngle=0.0, dRelevantElemRate=0.0, dChangeMassRate=0.0, dMinTimeStep=0.0, strSolverFile="", dFloorSize=0.0, bRename=True, crMat=None):
        message = "SNOnePush.DropTestSNOnePush('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iNumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

    def AutoSweepClosedLoopShaped(crlPart, dMeshSize, dLengthSize):
        message = "SNOnePush.AutoSweepClosedLoopShaped({},{},{})".format(crlPart, dMeshSize, dLengthSize)
        return JPT_RUN_LINE(message)

class StiffCalc:
    def Force(strName, poslForce, poslMoment, iEnArrowDir, iDistributionMethod, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula0, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, crlTarget, crEdit):
        message = "StiffCalc.Force('{}',{},{},{},'{}',{},{},{},{},{},{},'{}','{}','{}','{}','{}','{}',{},{})".format(strName, poslForce, poslMoment, iEnArrowDir, iDistributionMethod, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula0, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class SZOnepushReliability:
    Assembly = SZOnepushReliability_Assembly()

    MeshEdit = SZOnepushReliability_MeshEdit()

    def AlignMidNode(crlSource, crlTarget):
        message = "SZOnepushReliability.AlignMidNode({},{})".format(crlSource, crlTarget)
        return JPT_RUN_LINE(message)

class Test:
    Connection = Test_Connection()

    Muffler = Test_Muffler()

    ZGeometryTest = Test_ZGeometryTest()

    def FindFacesInPart(crPart, strIdentical):
        message = "Test.FindFacesInPart({},'{}')".format(crPart, strIdentical)
        return JPT_RUN_LINE(message)

    def CreateElementForWelding(crlSrcElems, crlDstElems, crlSideElems, crlPart, crMaterial):
        message = "Test.CreateElementForWelding({},{},{},{},{})".format(crlSrcElems, crlDstElems, crlSideElems, crlPart, crMaterial)
        return JPT_RUN_LINE(message)

class Toolbar:
    def Undo(iCntUndo=1):
        message = "Toolbar.Undo({})".format(iCntUndo)
        return JPT_RUN_LINE(message)

    def Redo(iCntRedo=1):
        message = "Toolbar.Redo({})".format(iCntRedo)
        return JPT_RUN_LINE(message)

class Tools:
    BySelection = Tools_BySelection()

    Coordinates = Tools_Coordinates()

    Group = Tools_Group()

    TotalLoad = Tools_TotalLoad()

    def NodeCS(crlInst=[], crCoordSystem=None):
        message = "Tools.NodeCS({},{})".format(crlInst, crCoordSystem)
        return JPT_RUN_LINE(message)

    def NodeCSGroup():
        message = "Tools.NodeCSGroup({})".format('')
        return JPT_RUN_LINE(message)

    def DisplacementCS(crlInst=[], crCoordSystem=None):
        message = "Tools.DisplacementCS({},{})".format(crlInst, crCoordSystem)
        return JPT_RUN_LINE(message)

    def Connections(listConnectRenumberTool):
        message = "Tools.Connections({})".format(listConnectRenumberTool)
        return JPT_RUN_LINE(message)

    def GroupByDCS():
        message = "Tools.GroupByDCS({})".format('')
        return JPT_RUN_LINE(message)

    def Renumber(listRenumberItem=[], bAssignProp=True, bSurfCornerFirst=False):
        message = "Tools.Renumber({},{},{})".format(listRenumberItem, bAssignProp, bSurfCornerFirst)
        return JPT_RUN_LINE(message)

    def RenumberByConnection(connectRenumberTool=CONNECT_RENUMBER_TOOL(), crlTarget=[]):
        message = "Tools.RenumberByConnection({},{})".format(connectRenumberTool, crlTarget)
        return JPT_RUN_LINE(message)

    def RenumberByFile(strCSVPath="", iConfilctStrategy=0, bNeedToUpdateCount=False):
        message = "Tools.RenumberByFile('{}',{},{})".format(strCSVPath, iConfilctStrategy, bNeedToUpdateCount)
        return JPT_RUN_LINE(message)

    def ModelInfo(strPath, strPathName="", listMeshPartInfoTool=[], bPropertyAssignedPart=False, bPropertyAssignedSummary=False, iModelNode=0, iNmodelnodeWithprop=0, ilModelElement=[], ilNmodelelemWithprop=[], ilModelLBC=[], iModelContact=0, ilModelConnection=[], ilModelProperty=[]):
        message = "Tools.ModelInfo('{}','{}',{},{},{},{},{},{},{},{},{},{},{})".format(strPath, strPathName, listMeshPartInfoTool, bPropertyAssignedPart, bPropertyAssignedSummary, iModelNode, iNmodelnodeWithprop, ilModelElement, ilNmodelelemWithprop, ilModelLBC, iModelContact, ilModelConnection, ilModelProperty)
        return JPT_RUN_LINE(message)

    def Section(bSection):
        message = "Tools.Section({})".format(bSection)
        return JPT_RUN_LINE(message)

    def ElementCS(iMethod=0, iDispType=0, bDispXDir=False, bDispCoord=False, dDispScale=1, crlTarget=[]):
        message = "Tools.ElementCS({},{},{},{},{},{})".format(iMethod, iDispType, bDispXDir, bDispCoord, dDispScale, crlTarget)
        return JPT_RUN_LINE(message)

    Measure = Tools_Measure()

