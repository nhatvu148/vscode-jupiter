class ACBoundary:
    def Method1(self, crlPart,bIsMergePart,bIsRenumber):
        message = "ACModeling.ACBoundary.Method1({},{},{})".format(crlPart,bIsMergePart,bIsRenumber)
        return JPT_RUN_LINE(message)

class Create:
    def Convex(self, crlTacrBodies, dMeshSize, dOffset, dRadius, iDAxisGround, dScale):
        message = "ACModeling.Create.Convex({},{},{},{},{},{})".format(crlTacrBodies, dMeshSize, dOffset, dRadius, iDAxisGround, dScale)
        return JPT_RUN_LINE(message)

class MakeProcess:
    def Static(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.Static('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def Creep(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, bThetaDefined, dTheta, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.Creep('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, bThetaDefined, dTheta, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def Dynamic(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, bDynamic, advcDynamic, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.Dynamic('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, bDynamic, advcDynamic, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def EigenValue(self, strName, bEigenValue, iNumberOfModes, iEigenvecNorm, dShift, dCgcgpiTol, dCgcgpiEigTol, iCgcgpiLoopMax, dCgcgpiInnerTol, iCgcgpiBlockSize, iCgcgpiExtraMode, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.EigenValue('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, bEigenValue, iNumberOfModes, iEigenvecNorm, dShift, dCgcgpiTol, dCgcgpiEigTol, iCgcgpiLoopMax, dCgcgpiInnerTol, iCgcgpiBlockSize, iCgcgpiExtraMode, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def DynamicExplicit(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, iLogMessageInterval, iLinearApproximation, dBulkViscosityCoef1, dBulkViscosityCoef2, dMassScalingdt, dDtScaleFactor, dPenaltyScaleFactor, iContactSearchInterval, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.DynamicExplicit('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, iLogMessageInterval, iLinearApproximation, dBulkViscosityCoef1, dBulkViscosityCoef2, dMassScalingdt, dDtScaleFactor, dPenaltyScaleFactor, iContactSearchInterval, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def ModalFreqResp(self, strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.ModalFreqResp('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def ResponseSpectrum(self, strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, iPropMethod, iSpttype, dSptFactor0, crSpt0, dSptFactor1, crSpt1, dSptFactor2, crSpt2, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.ResponseSpectrum('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, iPropMethod, iSpttype, dSptFactor0, crSpt0, dSptFactor1, crSpt1, dSptFactor2, crSpt2, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def SteadyState(self, strName, iEndType, dMaxTime, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList):
        message = "Analysis.ADVC.MakeProcess.SteadyState('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iEndType, dMaxTime, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList)
        return JPT_RUN_LINE(message)

    def Transient(self, strName, iEndType, dMaxTime, dSteadyRate, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList):
        message = "Analysis.ADVC.MakeProcess.Transient('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iEndType, dMaxTime, dSteadyRate, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList)
        return JPT_RUN_LINE(message)

    def Fatigue(self, strName, bFatigue, iMethod, iStressAxis, iSafetyType, dSearchResolution, dSafetyMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.Fatigue('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, bFatigue, iMethod, iStressAxis, iSafetyType, dSearchResolution, dSafetyMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def RandomResponse(self, strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, iPropMethod, iPSDtype, iPSDdir, crPSDLoad, dPSDFactor, dGravityAccel, iOutputEigenFreqStep, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.RandomResponse('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, iPropMethod, iPSDtype, iPSDdir, crPSDLoad, dPSDFactor, dGravityAccel, iOutputEigenFreqStep, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class AbaqusStep:
    def DynamicStep(self, param, crEdit):
        message = "Analysis.AbaqusStep.DynamicStep({},{})".format(param, crEdit)
        return JPT_RUN_LINE(message)

    def TransientStep(self, strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, dMaxAllowTChange, iEndsteptBchecked, dlEndsteptTlist, dMaxAllowEmissivityChange, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, dAdjustFactor, iMaxContactIter, iBNlgeom, dTimePeriod, iConvertDscntIter, iRamp, iExtrapolateMethod, listAbaqusOutputRequest, crEdit):
        message = "Analysis.AbaqusStep.TransientStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, dMaxAllowTChange, iEndsteptBchecked, dlEndsteptTlist, dMaxAllowEmissivityChange, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, dAdjustFactor, iMaxContactIter, iBNlgeom, dTimePeriod, iConvertDscntIter, iRamp, iExtrapolateMethod, listAbaqusOutputRequest, crEdit)
        return JPT_RUN_LINE(message)

    def DynamicCoupledTDExplicitStep(self, strName,strDesp,iBAutomatic,iMaxSizebchecked,dlMaxSizeTList,iIncrmtEstimator,iUserTimeIncrmtbchecked,dlUserTimeIncrmtTList,dTimeScalfactor,iBNlgeom,dTimePeriod,dLinearBlkVisco,dQuadrBlkVisco,listAbaqusOutputRequest,crEdit):
        message = "Analysis.AbaqusStep.DynamicCoupledTDExplicitStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName,strDesp,iBAutomatic,iMaxSizebchecked,dlMaxSizeTList,iIncrmtEstimator,iUserTimeIncrmtbchecked,dlUserTimeIncrmtTList,dTimeScalfactor,iBNlgeom,dTimePeriod,dLinearBlkVisco,dQuadrBlkVisco,listAbaqusOutputRequest,crEdit)
        return JPT_RUN_LINE(message)

    def CoupledTDStep(self, strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, abaqusPair1, abaqusPair2, iCSVIntegration, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, dAdjustFactor, iMaxContactIter, iType, iBUseAdaptive, dDampingfactor, dMaxRationofStrainEnergy, iBNlgeom, dTimePeriod, iTransient, iConvertDscntIter, iRamp, iExtrapolateMethod, iBIncldCSV, listOutput, crEdit):
        message = "Analysis.AbaqusStep.CoupledTDStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, abaqusPair1, abaqusPair2, iCSVIntegration, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, dAdjustFactor, iMaxContactIter, iType, iBUseAdaptive, dDampingfactor, dMaxRationofStrainEnergy, iBNlgeom, dTimePeriod, iTransient, iConvertDscntIter, iRamp, iExtrapolateMethod, iBIncldCSV, listOutput, crEdit)
        return JPT_RUN_LINE(message)

    def DynamicExplicitStep(self, strName, strDesp, iBAutomatic, iIncrmtEstimator, abaqusPair1, dTimeScalfactor, abaqusPair2, iBNlgeom, dTimePeriod, iBIncldHeatEffect, dLinearBlkVisco, dQuadrBlkVisco, listOutput, crEdit):
        message = "Analysis.AbaqusStep.DynamicExplicitStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iBAutomatic, iIncrmtEstimator, abaqusPair1, dTimeScalfactor, abaqusPair2, iBNlgeom, dTimePeriod, iBIncldHeatEffect, dLinearBlkVisco, dQuadrBlkVisco, listOutput, crEdit)
        return JPT_RUN_LINE(message)

    def ModalStep(self, strName, strDesp, iEigenSolver, iNFreqRequestbchecked, ilNFreqRequestTList, iFreqShiftbchecked, ilFreqShiftTList, iFreqRangebchecked, ilFreqRangeTList, iIncldAcoustic, iBlockSizebchecked, ilBlockSizeTList, iMaxBlkNumofLanczosStepbchecked, ilMaxBlkNumofLanczosStepTList, iBUseSIM, iBIncldResMods, iNEigenRequest, iMaxItersUsed, iVectorsUsed, iMethod, iMatrixStorage, iNormalizeEigenBy, iEvalPropFreqbchecked, ilEvalPropFreqTList, abaqusOutputRequest, crEdit):
        message = "Analysis.AbaqusStep.ModalStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iEigenSolver, iNFreqRequestbchecked, ilNFreqRequestTList, iFreqShiftbchecked, ilFreqShiftTList, iFreqRangebchecked, ilFreqRangeTList, iIncldAcoustic, iBlockSizebchecked, ilBlockSizeTList, iMaxBlkNumofLanczosStepbchecked, ilMaxBlkNumofLanczosStepTList, iBUseSIM, iBIncldResMods, iNEigenRequest, iMaxItersUsed, iVectorsUsed, iMethod, iMatrixStorage, iNormalizeEigenBy, iEvalPropFreqbchecked, ilEvalPropFreqTList, abaqusOutputRequest, crEdit)
        return JPT_RUN_LINE(message)

    def StaticRiskStep(self, strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, iMethod, iMatrixStorage, dMaxLdPropFactor, iBMaxLdPropFactor, iBMaxDisp, dMaxDisp, iMaxDispDof, strNdRgn, iBNlgeom, iBIncldHeatEffect, iConvertDscntIter, dTotalArcLength, iExtrapolateMethod, iBAcceptByMaxIters, iBLongTerm, iBPerturbation, iFullplasticregionBchecked, strlFullplasticregionTlist, iOutput, crEdit):
        message = "Analysis.AbaqusStep.StaticRiskStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},'{}',{},{})".format(strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, iMethod, iMatrixStorage, dMaxLdPropFactor, iBMaxLdPropFactor, iBMaxDisp, dMaxDisp, iMaxDispDof, strNdRgn, iBNlgeom, iBIncldHeatEffect, iConvertDscntIter, dTotalArcLength, iExtrapolateMethod, iBAcceptByMaxIters, iBLongTerm, iBPerturbation, iFullplasticregionBchecked, strlFullplasticregionTlist, iOutput, crEdit)
        return JPT_RUN_LINE(message)

    def SteadyStateStep(self, strName, strDesp, iAutomatic, iMaxInc, iNitSize, dMinSize, dMaxSize, dMaxAllowTChange, iEndStepbchecked, dlEndStepTList, dMaxAllowEmissivityChange, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, iAdjustFactor, iMaxContactIter, iNlgeom, dTimePeriod, iConvertDscntIter, iRamp, iExtrapolateMethod, iOutput, crEdit):
        message = "Analysis.AbaqusStep.SteadyStateStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iAutomatic, iMaxInc, iNitSize, dMinSize, dMaxSize, dMaxAllowTChange, iEndStepbchecked, dlEndStepTList, dMaxAllowEmissivityChange, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, iAdjustFactor, iMaxContactIter, iNlgeom, dTimePeriod, iConvertDscntIter, iRamp, iExtrapolateMethod, iOutput, crEdit)
        return JPT_RUN_LINE(message)

class ACTRAN:
    def ExportBdf(self, strPath):
        message = "Analysis.ACTRAN.ExportBdf('{}')".format(strPath)
        return JPT_RUN_LINE(message)

    def Run(self, actranAnalysis, crlTarget, crEdit):
        message = "Analysis.ACTRAN.Run({},{},{})".format(actranAnalysis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def CreateEdat(self, actranAnalysis, crlTarget, crEdit):
        message = "Analysis.ACTRAN.CreateEdat({},{},{})".format(actranAnalysis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Ansys:
    def HeadTransferSteady(self, strName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit):
        message = "Analysis.Ansys.HeadTransferSteady('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit)
        return JPT_RUN_LINE(message)

    def LinearStatic(self, strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob):
        message = "Analysis.Ansys.LinearStatic('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

    def NormalModes(self, strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob):
        message = "Analysis.Ansys.NormalModes('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

    def Harmonic(self, strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob):
        message = "Analysis.Ansys.Harmonic('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

    def Steady(self, strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob):
        message = "Analysis.Ansys.Steady('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

class Nastran:
    def ModalTransientResponse(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.ModalTransientResponse('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def LinearBuckling(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.LinearBuckling('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def Transient(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.Transient('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def SteadyState(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.SteadyState('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def ModalFrequencyResponse(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.ModalFrequencyResponse('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def LinearStatic(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.LinearStatic('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def NormalModes(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.NormalModes('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Permas:
    def Job(self, strName,strDescription,iType,crEdit,crlTarget,bElStress,bElStressMis,bElStrain,bNodeStess,bGZip,bIdeas,bNLResult,iNLStepType,dEquiStart,dEquiStep,dEquiEnd,strNLStepList,bTimeStep,iTimeStepKind,dTimeStart,dTimeStep,dTimeEnd,iLCId):
        message = "Analysis.Permas.Job('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{})".format(strName,strDescription,iType,crEdit,crlTarget,bElStress,bElStressMis,bElStrain,bNodeStess,bGZip,bIdeas,bNLResult,iNLStepType,dEquiStart,dEquiStep,dEquiEnd,strNLStepList,bTimeStep,iTimeStepKind,dTimeStart,dTimeStep,dTimeEnd,iLCId)
        return JPT_RUN_LINE(message)

class TSSolver:
    def ExportDynamisBdf(self, strPath,crJob):
        message = "Analysis.TSSolver.ExportDynamisBdf('{}',{})".format(strPath,crJob)
        return JPT_RUN_LINE(message)

    def Job(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit):
        message = "Analysis.TSSolver.Job('{}','{}',{},'{}',{})".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit)
        return JPT_RUN_LINE(message)

    def LinearBucking(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.LinearBucking('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def LinearStatic(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.LinearStatic('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def NonlinearStatic(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.NonlinearStatic('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def NormalModes(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.NormalModes('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def NonlinearFrequency(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.NonlinearFrequency('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def ModalTransientResponse(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.ModalTransientResponse('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def TransientHeatTransfer(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.TransientHeatTransfer('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def ModalFrequencyResponse(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.ModalFrequencyResponse('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

    def SteadyStateHeatTransfer(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.SteadyStateHeatTransfer('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class TSSS:
    def TransientHeatTransfer(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.TransientHeatTransfer('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def LinearStatic(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer, iNitTempType):
        message = "Analysis.TSSS.LinearStatic('{}','{}',{},'{}',{},{},{},'{}',{},{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer, iNitTempType)
        return JPT_RUN_LINE(message)

    def NonlinearStatic(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.NonlinearStatic('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def NormalModes(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.NormalModes('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def LinearBuckling(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.LinearBuckling('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def ModalFrequencyResponse(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.ModalFrequencyResponse('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

    def SteadyStateHeatTransfer(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.SteadyStateHeatTransfer('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class ADVC:
    MakeProcess = MakeProcess()

    def Structure(self, strName, strDescription, iEJobType, crlProcessSequence, crlElemLocationGroup, crlNodeLocationGroup, bWriteGroup, crEdit, bResultReference, iSeparateFile, bExportRelatedAllLBCs, bUseEntityName, bMatrixSloverParam, iPreconditionType, iMatrixStructure, crlTarget, iLoadType, bSameOutputOnAllProcess, bDeleteFloatingNode, bBC, bCheckBCDuplicate, bAutoAssignDummyProp, crDummyPropMaterial, bReferenceRestartData, strReferenceRestartDataPath, iReferenceRestartDataProcessNum, iReferenceRestartDataStepNum, iReferenceRestartDataCoordType, iReferenceRestartDataUpdateContactSearch, listLoadNodeContact, iHeatConvection, iCreateProcessForBoltFixedLength, strPath, iNumType, iUiWidth, iUiPrecision):
        message = "Analysis.ADVC.Structure('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, strDescription, iEJobType, crlProcessSequence, crlElemLocationGroup, crlNodeLocationGroup, bWriteGroup, crEdit, bResultReference, iSeparateFile, bExportRelatedAllLBCs, bUseEntityName, bMatrixSloverParam, iPreconditionType, iMatrixStructure, crlTarget, iLoadType, bSameOutputOnAllProcess, bDeleteFloatingNode, bBC, bCheckBCDuplicate, bAutoAssignDummyProp, crDummyPropMaterial, bReferenceRestartData, strReferenceRestartDataPath, iReferenceRestartDataProcessNum, iReferenceRestartDataStepNum, iReferenceRestartDataCoordType, iReferenceRestartDataUpdateContactSearch, listLoadNodeContact, iHeatConvection, iCreateProcessForBoltFixedLength, strPath, iNumType, iUiWidth, iUiPrecision)
        return JPT_RUN_LINE(message)

    def HeatTransfer(self, strName, strDescription, iEJobType, crlProcessSequence, crlElemLocationGroup, crlNodeLocationGroup, bWriteGroup, crEdit, bResultReference, iSeparateFile, bExportRelatedAllLBCs, bUseEntityName, bMatrixSloverParam, iPreconditionType, iMatrixStructure, crlTarget, iLoadType, bSameOutputOnAllProcess, bDeleteFloatingNode, bBC, bCheckBCDuplicate, bAutoAssignDummyProp, crDummyPropMaterial, bReferenceRestartData, strReferenceRestartDataPath, iReferenceRestartDataProcessNum, iReferenceRestartDataStepNum, iReferenceRestartDataCoordType, iReferenceRestartDataUpdateContactSearch, listLoadNodeContact, iHeatConvection, strPath, iNumType, iUiWidth, iUiPrecision):
        message = "Analysis.ADVC.HeatTransfer('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},'{}',{},{},{})".format(strName, strDescription, iEJobType, crlProcessSequence, crlElemLocationGroup, crlNodeLocationGroup, bWriteGroup, crEdit, bResultReference, iSeparateFile, bExportRelatedAllLBCs, bUseEntityName, bMatrixSloverParam, iPreconditionType, iMatrixStructure, crlTarget, iLoadType, bSameOutputOnAllProcess, bDeleteFloatingNode, bBC, bCheckBCDuplicate, bAutoAssignDummyProp, crDummyPropMaterial, bReferenceRestartData, strReferenceRestartDataPath, iReferenceRestartDataProcessNum, iReferenceRestartDataStepNum, iReferenceRestartDataCoordType, iReferenceRestartDataUpdateContactSearch, listLoadNodeContact, iHeatConvection, strPath, iNumType, iUiWidth, iUiPrecision)
        return JPT_RUN_LINE(message)

class SeparateFaces:
    def AllSharedNodes(self, ):
        message = "Assemble.SeparateFaces.AllSharedNodes({})".format()
        return JPT_RUN_LINE(message)

    def Shell(self, iType, crlEntity, bCreateGroup):
        message = "Assemble.SeparateFaces.Shell({},{},{})".format(iType, crlEntity, bCreateGroup)
        return JPT_RUN_LINE(message)

    def Solid(self, ilPartKeys, ilFaceKeys, bCreateGroup):
        message = "Assemble.SeparateFaces.Solid({},{},{})".format(ilPartKeys, ilFaceKeys, bCreateGroup)
        return JPT_RUN_LINE(message)

class RightClick:
    def AddToReference(self, crSrcPart,crDestPart):
        message = "Assembly.RightClick.AddToReference({},{})".format(crSrcPart,crDestPart)
        return JPT_RUN_LINE(message)

    def Suppress(self, crlParts):
        message = "Assembly.RightClick.Suppress({})".format(crlParts)
        return JPT_RUN_LINE(message)

    def UnSuppress(self, taParts):
        message = "Assembly.RightClick.UnSuppress({})".format(taParts)
        return JPT_RUN_LINE(message)

    def RestoreOriginalPart(self, crlCrBodies, bKeepShareFace):
        message = "Assembly.RightClick.RestoreOriginalPart({},{})".format(crlCrBodies, bKeepShareFace)
        return JPT_RUN_LINE(message)

    def Rename(self, strNewName, crItem):
        message = "Assembly.RightClick.Rename('{}',{})".format(strNewName, crItem)
        return JPT_RUN_LINE(message)

    def ChangeEntityColor(self, crlEntity, iColor):
        message = "Assembly.RightClick.ChangeEntityColor({},{})".format(crlEntity, iColor)
        return JPT_RUN_LINE(message)

    def AddSubAssembly(self, crInst):
        message = "Assembly.RightClick.AddSubAssembly({})".format(crInst)
        return JPT_RUN_LINE(message)

    def ChangeBodyColor(self, listPartColorPair, bResetFaceColor):
        message = "Assembly.RightClick.ChangeBodyColor({},{})".format(listPartColorPair, bResetFaceColor)
        return JPT_RUN_LINE(message)

    def ChangeMeshLineColor(self, crlFace, iColor):
        message = "Assembly.RightClick.ChangeMeshLineColor({},{})".format(crlFace, iColor)
        return JPT_RUN_LINE(message)

class CentrifugalForce:
    def CoordinateSystems(self, strName, dFVelocity, dFAcceleration, iAxisDirection, iVelocityUnit, iAccelerationUnit, crCurCoord, crlTarget, crEdit):
        message = "BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems('{}',{},{},{},{},{},{},{},{})".format(strName, dFVelocity, dFAcceleration, iAxisDirection, iVelocityUnit, iAccelerationUnit, crCurCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def TwoPositions(self, strName, dFBasePoint1, dFBasePoint2, dFBasePoint3, dFTipPoint1, dFTipPoint2, dFTipPoint3, dFVelocity, dFAcceleration, iVelocityUnit, iAccelerationUnit, crlTarget, crEdit):
        message = "BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dFBasePoint1, dFBasePoint2, dFBasePoint3, dFTipPoint1, dFTipPoint2, dFTipPoint3, dFVelocity, dFAcceleration, iVelocityUnit, iAccelerationUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class FunctionLoadCylinder:
    def Quadratic(self, strName, dFTotalForce, dA, dB, crCoord, iAngleBase, dAngleRange, iEnArrowDir, crlTargets, crEdit):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.Quadratic('{}',{},{},{},{},{},{},{},{},{})".format(strName, dFTotalForce, dA, dB, crCoord, iAngleBase, dAngleRange, iEnArrowDir, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

    def Sine(self, strName, dFTotalForce, dA, crCoord, iAngleBase, dAngleRange, iEnArrowDir, bDistributeInAxis, crlTarget, crEdit):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.Sine('{}',{},{},{},{},{},{},'{}',{},{})".format(strName, dFTotalForce, dA, crCoord, iAngleBase, dAngleRange, iEnArrowDir, bDistributeInAxis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Vector(self, strName, dFTotalForce, dA, dX, dY, crCoord, iEnDirection, dAngleRange, iArrowDir, bDistributeInAxis, crlTarget, crEdit):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.Vector('{}',{},{},{},{},{},{},{},{},'{}',{},{})".format(strName, dFTotalForce, dA, dX, dY, crCoord, iEnDirection, dAngleRange, iArrowDir, bDistributeInAxis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class NonlinearForce:
    def NOLIN3(self, strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit):
        message = "BoundaryConditions.Force.NonlinearForce.NOLIN3('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

    def NOLIN4(self, strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit):
        message = "BoundaryConditions.Force.NonlinearForce.NOLIN4('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

    def NOLIN1(self, strName, dForceScale, dMomentScale, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCoord, crForceTable, crMomentTable, crlVcrMaster, crlVcrSlave, crEdit):
        message = "BoundaryConditions.Force.NonlinearForce.NOLIN1('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCoord, crForceTable, crMomentTable, crlVcrMaster, crlVcrSlave, crEdit)
        return JPT_RUN_LINE(message)

class InitialAngularVelocity:
    def Abaqus(self, strName, dVelocity, strFirstCoord, strSecondCoord, crlTargets, crEdit):
        message = "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus('{}',{},'{}','{}',{},{})".format(strName, dVelocity, strFirstCoord, strSecondCoord, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

    def General(self, strName, stData, crlTarget, crEdit):
        message = "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General('{}',{},{},{})".format(strName, stData, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryTemperature:
    def Constant(self, strName, dFTemp, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.BoundaryTemperature.Constant('{}',{},{},{},{})".format(strName, dFTemp, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def SurfaceMapping(self, strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, iMappedCpIndexArr1, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strPath, crEdit, iMappingMethod, iSubmodeLBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet):
        message = "BoundaryConditions.BoundaryTemperature.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, iMappedCpIndexArr1, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strPath, crEdit, iMappingMethod, iSubmodeLBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
        return JPT_RUN_LINE(message)

class Convection:
    def Constant(self, strName, dExtTemp, crTableTimeTemp, dDcoef, crTableTimeCoeff, crTableTempCoeff, crlTarget, crEdit):
        message = "BoundaryConditions.Convection.Constant('{}',{},{},{},{},{},{},{})".format(strName, dExtTemp, crTableTimeTemp, dDcoef, crTableTimeCoeff, crTableTempCoeff, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def SurfaceMapping(self, strName, crlTarget, iPos, iViewCp, iCp, iSrcType, iMappedCpIndex0, iMappedCpIndex1, dRScale, posOffset, posAxis, dTScale, dSearchRange, iHTCUnit, iTempUnit, strPath, crEdit):
        message = "BoundaryConditions.Convection.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, crlTarget, iPos, iViewCp, iCp, iSrcType, iMappedCpIndex0, iMappedCpIndex1, dRScale, posOffset, posAxis, dTScale, dSearchRange, iHTCUnit, iTempUnit, strPath, crEdit)
        return JPT_RUN_LINE(message)

class EnforcedLoads:
    def Acceleration(self, strName, iDwDof, dFVel1, dFVel2, dFVel3, dFVel4, dFVel5, dFVel6, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, bExport, crMEExport1, crMEExport2, crMEExport3, crMEExport4, crMEExport5, crMEExport6, iAcUnit, iRotUnit, crlTarget, crEdit):
        message = "BoundaryConditions.EnforcedLoads.Acceleration('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDwDof, dFVel1, dFVel2, dFVel3, dFVel4, dFVel5, dFVel6, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, bExport, crMEExport1, crMEExport2, crMEExport3, crMEExport4, crMEExport5, crMEExport6, iAcUnit, iRotUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Velocity(self, strName, iDwDof, dFVel0, dFVel1, dFVel2, dFVel3, dFVel4, dFVel5, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, iVelUnit, iRotUnit, bExport, crExportData0, crExportData1, crExportData2, crExportData3, crExportData4, crExportData5, crlTarget, crEdit, bADVCStatic):
        message = "BoundaryConditions.EnforcedLoads.Velocity('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDwDof, dFVel0, dFVel1, dFVel2, dFVel3, dFVel4, dFVel5, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, iVelUnit, iRotUnit, bExport, crExportData0, crExportData1, crExportData2, crExportData3, crExportData4, crExportData5, crlTarget, crEdit, bADVCStatic)
        return JPT_RUN_LINE(message)

    def Displacement(self, strName, iDwDof, dFDisp0, dFDisp1, dFDisp2, dFDisp3, dFDisp4, dFDisp5, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, crlTarget, crEdit):
        message = "BoundaryConditions.EnforcedLoads.Displacement('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDwDof, dFDisp0, dFDisp1, dFDisp2, dFDisp3, dFDisp4, dFDisp5, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class HeatFlux:
    def SurfaceFlux(self, strName,dFflux,iDistributionMethod,crTable,crlTarget, crEdit):
        message = "BoundaryConditions.HeatFlux.SurfaceFlux('{}',{},'{}',{},{},{})".format(strName,dFflux,iDistributionMethod,crTable,crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def SurfaceMapping(self, strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strStrpath, crEdit, iMappingMethod, iSubmodeLBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet):
        message = "BoundaryConditions.HeatFlux.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strStrpath, crEdit, iMappingMethod, iSubmodeLBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
        return JPT_RUN_LINE(message)

    def ConcentrateFlux(self, strName , stData, taTarget, crEdit):
        message = "BoundaryConditions.HeatFlux.ConcentrateFlux('{}',{},{},{})".format(strName , stData, taTarget, crEdit)
        return JPT_RUN_LINE(message)

class InitialElementalValue:
    def InitialStress(self, strName, iDimension, iElemCs, dSXX, dSYY, dSXY, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.InitialElementalValue.InitialStress('{}',{},{},{},{},{},{},{},{})".format(strName, iDimension, iElemCs, dSXX, dSYY, dSXY, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class InitialTemperature:
    def WholeMapping(self, strName, iMapSourceType, strPath, iMappingMethod, iIsubcase, crEdit):
        message = "BoundaryConditions.InitialTemperature.WholeMapping('{}',{},'{}',{},{},{})".format(strName, iMapSourceType, strPath, iMappingMethod, iIsubcase, crEdit)
        return JPT_RUN_LINE(message)

    def Constant(self, strName,dFTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.InitialTemperature.Constant('{}',{},'{}',{},{},{},{})".format(strName,dFTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ADVC(self, strName,fTemp, strFilePathName, bUseDefault, crTable, taTarget, crEdit):
        message = "BoundaryConditions.InitialTemperature.ADVC('{}',{},'{}',{},{},{},{})".format(strName,fTemp, strFilePathName, bUseDefault, crTable, taTarget, crEdit)
        return JPT_RUN_LINE(message)

    def NastranPunch(self, strName,fTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.InitialTemperature.NastranPunch('{}',{},'{}',{},{},{},{})".format(strName,fTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class LBCCopy:
    def PropertiesCopyTranslate(self, iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.PropertiesCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def PropertiesCopyRotate(self, iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.PropertiesCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def PropertiesCopyMirror(self, iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget):
        message = "BoundaryConditions.LBCCopy.PropertiesCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

    def ConnectionCopyTranslate(self, iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.ConnectionCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def ConnectionCopyRotate(self, iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.ConnectionCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def ConnectionCopyMirror(self, iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget):
        message = "BoundaryConditions.LBCCopy.ConnectionCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

    def GroupCopyTranslate(self, iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.GroupCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def GroupCopyRotate(self, iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.GroupCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def GroupCopyMirror(self, iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget):
        message = "BoundaryConditions.LBCCopy.GroupCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

    def LBCCopyTranslate(self, iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.LBCCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def LBCCopyRotate(self, iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.LBCCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

    def LBCCopyMirror(self, iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget):
        message = "BoundaryConditions.LBCCopy.LBCCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

class Pressure:
    def SurfaceLoads(self, strName, dlPressure, iArrowdir, crCoordinate, crlTargetFace, crEditCur):
        message = "BoundaryConditions.Pressure.SurfaceLoads('{}',{},{},{},{},{})".format(strName, dlPressure, iArrowdir, crCoordinate, crlTargetFace, crEditCur)
        return JPT_RUN_LINE(message)

    def By2Nodes(self, strName, crNodeA, dPressureA, iNodeAUnit, crNodeB, dPressureB, iNodeBUnit, iDirection, crlTarget, crEdit):
        message = "BoundaryConditions.Pressure.By2Nodes('{}',{},{},{},{},{},{},{},{},{})".format(strName, crNodeA, dPressureA, iNodeAUnit, crNodeB, dPressureB, iNodeBUnit, iDirection, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def General(self, strName, dFpressure, iIdistribute, crCrtable, dDphase, dDdelay, crPhaseTable, strFormularValue, crCrcoord, dlVdirection, strFormularDirX, strFormularDirY, strFormularDirZ, iArrowDir, crlTatarget, crCredit):
        message = "BoundaryConditions.Pressure.General('{}',{},'{}',{},{},{},{},'{}',{},{},'{}','{}','{}',{},{},{})".format(strName, dFpressure, iIdistribute, crCrtable, dDphase, dDdelay, crPhaseTable, strFormularValue, crCrcoord, dlVdirection, strFormularDirX, strFormularDirY, strFormularDirZ, iArrowDir, crlTatarget, crCredit)
        return JPT_RUN_LINE(message)

    def Quadratic(self, strName, dA, dB, crCoordinate, dAngleRange, iPressureDirectionMode, dlPressureDirection, crlTargets, crEdit):
        message = "BoundaryConditions.Pressure.Quadratic('{}',{},{},{},{},{},{},{},{})".format(strName, dA, dB, crCoordinate, dAngleRange, iPressureDirectionMode, dlPressureDirection, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

    def FunctionLoadToCylinderSine(self, strName, dA, crCoordinate, dAngleRange, bDistributionAxis, iPressureDirectionMode, bIsTotalForceAdjustment, dTotalForce, vecPressureDirection, crCoordinateSystemForDirection, bIsCornerNodesDistribution, strFormulaForA, crlTargets, crEdit):
        message = "BoundaryConditions.Pressure.FunctionLoadToCylinderSine('{}',{},{},{},'{}',{},{},{},{},{},'{}','{}',{},{})".format(strName, dA, crCoordinate, dAngleRange, bDistributionAxis, iPressureDirectionMode, bIsTotalForceAdjustment, dTotalForce, vecPressureDirection, crCoordinateSystemForDirection, bIsCornerNodesDistribution, strFormulaForA, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

    def Hydrostatic(self, strName, dFHPressure, dFDensity, iDensityUnit, dFGravity, iGravityUnit, iGravityDir, dFWaterSuface, iSufaceUnit, iEnDistrbute, crlTarget, crEdit):
        message = "BoundaryConditions.Pressure.Hydrostatic('{}',{},{},{},{},{},{},{},{},'{}',{},{})".format(strName, dFHPressure, dFDensity, iDensityUnit, dFGravity, iGravityUnit, iGravityDir, dFWaterSuface, iSufaceUnit, iEnDistrbute, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def SurfaceMapping(self, strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strPath, crEdit):
        message = "BoundaryConditions.Pressure.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strPath, crEdit)
        return JPT_RUN_LINE(message)

class Submodel:
    def SubmodelForcedFlux(self, strName, iSolver, strFilePathName, iProcessNo, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit):
        message = "BoundaryConditions.Submodel.SubmodelForcedFlux('{}',{},'{}',{},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(strName, iSolver, strFilePathName, iProcessNo, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ForcedTempertature(self, strName, iSolver, strFilePathName, iProcessNo, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit):
        message = "BoundaryConditions.Submodel.ForcedTempertature('{}',{},'{}',{},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(strName, iSolver, strFilePathName, iProcessNo, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ForcedDisplacement(self, strName, iSolver, strFilePathName, iProcessNo, bTranslationX, bTranslationY, bTranslationZ, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit):
        message = "BoundaryConditions.Submodel.ForcedDisplacement('{}',{},'{}',{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(strName, iSolver, strFilePathName, iProcessNo, bTranslationX, bTranslationY, bTranslationZ, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class TemperatureLoads:
    def Constant(self, strName, dTemperature, crTable, crlTarget, crEdit, bUseDefaultTemp):
        message = "BoundaryConditions.TemperatureLoads.Constant('{}',{},{},{},{},{})".format(strName, dTemperature, crTable, crlTarget, crEdit, bUseDefaultTemp)
        return JPT_RUN_LINE(message)

    def ADVCFile(self, strName, strFilePathName, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.TemperatureLoads.ADVCFile('{}','{}',{},{},{})".format(strName, strFilePathName, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def NastranPunch(self, strName, strFilePathName, crTable, crlTarget, crEdit, bUseAsMaterialReferenceTemp):
        message = "BoundaryConditions.TemperatureLoads.NastranPunch('{}','{}',{},{},{},{})".format(strName, strFilePathName, crTable, crlTarget, crEdit, bUseAsMaterialReferenceTemp)
        return JPT_RUN_LINE(message)

    def WholeMapping(self, strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, iMappedCpIndexArr1, iDScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet):
        message = "BoundaryConditions.TemperatureLoads.WholeMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, iMappedCpIndexArr1, iDScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
        return JPT_RUN_LINE(message)

    def LbcInitialTemperature(self, strName, iType, dFTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.TemperatureLoads.LbcInitialTemperature('{}',{},{},'{}',{},{},{},{})".format(strName, iType, dFTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BodyLoads:
    CentrifugalForce = CentrifugalForce()

    def Gravity(self, strName,dlGravity, crCurCoord, crlTarget, crEdit):
        message = "BoundaryConditions.BodyLoads.Gravity('{}',{},{},{},{})".format(strName,dlGravity, crCurCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Force:
    FunctionLoadCylinder = FunctionLoadCylinder()

    NonlinearForce = NonlinearForce()

    def General(self, strName, vecForce, vecMoment, iEnArrowDir, iEnDistrbute, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, strFormula6, crlTarget, crEdit):
        message = "BoundaryConditions.Force.General('{}',{},{},{},'{}',{},{},{},{},{},{},'{}','{}','{}','{}','{}','{}',{},{})".format(strName, vecForce, vecMoment, iEnArrowDir, iEnDistrbute, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, strFormula6, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ForceNormalDirection(self, strName, vecForce, iEnArrowDir, iEnDistrbute, crCurCoord, crlTarget, crEdit):
        message = "BoundaryConditions.Force.ForceNormalDirection('{}',{},{},'{}',{},{},{})".format(strName, vecForce, iEnArrowDir, iEnDistrbute, crCurCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class InitialNodalValue:
    InitialAngularVelocity = InitialAngularVelocity()

    def Displacement(self, strName, iType, vecInit, bSelNode, crNodeSet, crTable, crCoord, crlTarget, crEdit):
        message = "BoundaryConditions.InitialNodalValue.Displacement('{}',{},{},{},{},{},{},{},{})".format(strName, iType, vecInit, bSelNode, crNodeSet, crTable, crCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Velocity(self, strName, stData, crlTarget, crEdit):
        message = "BoundaryConditions.InitialNodalValue.Velocity('{}',{},{},{})".format(strName, stData, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def RotationAngle(self, strName, stData, taTarget, crEdit):
        message = "BoundaryConditions.InitialNodalValue.RotationAngle('{}',{},{},{})".format(strName, stData, taTarget, crEdit)
        return JPT_RUN_LINE(message)

class Edge:
    def TypeC(self, crlEdgeCur1,crlEdgeCur2, strRbeName, dPlaneTol, dMaxBoltHeight, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth):
        message = "Connections.BoltConnections.Edge.TypeC({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1,crlEdgeCur2, strRbeName, dPlaneTol, dMaxBoltHeight, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth)
        return JPT_RUN_LINE(message)

    def TypeB(self, crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, bIfCreate2ADVCStaticProcessForBoltFixLength):
        message = "Connections.BoltConnections.Edge.TypeB({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, bIfCreate2ADVCStaticProcessForBoltFixLength)
        return JPT_RUN_LINE(message)

    def TypeD(self, crlEdgeCur1,crlEdgeCur2, strMpcName, dConnRadius, dPlaneTol):
        message = "Connections.BoltConnections.Edge.TypeD({},{},'{}',{},{})".format(crlEdgeCur1,crlEdgeCur2, strMpcName, dConnRadius, dPlaneTol)
        return JPT_RUN_LINE(message)

    def TypeA(self, crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, bIsCreate2ADVCStaticProcessForFixLength):
        message = "Connections.BoltConnections.Edge.TypeA({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, bIsCreate2ADVCStaticProcessForFixLength)
        return JPT_RUN_LINE(message)

class Face:
    def TypeC(self, crlFaceCur1,crlFaceCur2, strRbeName, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth):
        message = "Connections.BoltConnections.Face.TypeC({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1,crlFaceCur2, strRbeName, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth)
        return JPT_RUN_LINE(message)

    def TypeB(self, crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, dScale1, bIsCreate2ADVCStaticProcessForFixLength):
        message = "Connections.BoltConnections.Face.TypeB({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, dScale1, bIsCreate2ADVCStaticProcessForFixLength)
        return JPT_RUN_LINE(message)

    def TypeA(self, crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, dScale1, bIfCreate2ADVCStaticProcessForBoltFixLength):
        message = "Connections.BoltConnections.Face.TypeA({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, dScale1, bIfCreate2ADVCStaticProcessForBoltFixLength)
        return JPT_RUN_LINE(message)

class Abaqus:
    def ContactTable(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.ManualGroup('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ManualFace(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.ManualFace('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.ContactGroupByMatrix('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.ContactShareFace('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class ADVC:
    def ContactClearance(self, strName,dClearanceVal,iLocalUnit,iSolverType,crlTarget, crEdit):
        message = "Connections.Contacts.ADVC.ContactClearance('{}',{},{},{},{},{})".format(strName,dClearanceVal,iLocalUnit,iSolverType,crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.ManualGroup('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.ManualFace({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def Contact(self, strName, iType, slidingType, InitialState, initialStateTol, kineticFrictionCoef, exponentialCoef, Behavior, Clearance, adjust2Clearance, interference, adjust2Interference, autoShrink, badvAdjust, adjustValue, FrictionCoef, MaxShear, elastic_slip, slip_tolerance, searchWidth, SearchGap, searchDepth, critialPenetration, estimation_impact_time, formula, constraintType, iDataType, TypeId, btemperatureDependency, idependencies, table, stabilized, type, residual_factor, effective_dist, cn, ct, taCClearance, taTarget, crEdit, searchAngle, constraintType_explicit, penaltyFact, penaltyFactExplicit, Color, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.Contact('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iType, slidingType, InitialState, initialStateTol, kineticFrictionCoef, exponentialCoef, Behavior, Clearance, adjust2Clearance, interference, adjust2Interference, autoShrink, badvAdjust, adjustValue, FrictionCoef, MaxShear, elastic_slip, slip_tolerance, searchWidth, SearchGap, searchDepth, critialPenetration, estimation_impact_time, formula, constraintType, iDataType, TypeId, btemperatureDependency, idependencies, table, stabilized, type, residual_factor, effective_dist, cn, ct, taCClearance, taTarget, crEdit, searchAngle, constraintType_explicit, penaltyFact, penaltyFactExplicit, Color, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.ContactShareFace({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(crlShareFace, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.ContactGroupByMatrix('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

class Ansys:
    def ManualGroup(self, strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Ansys.ManualGroup('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor):
        message = "Connections.Contacts.Ansys.ManualFace({},{},'{}',{},{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Ansys.ContactGroupByMatrix('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor):
        message = "Connections.Contacts.Ansys.ContactShareFace({},'{}',{},{},{},{},{},{})".format(crlShareFace, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Ansys.ContactTable('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class MSCNastran:
    def ManualGroup(self, strName, tssolverContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.ContactGroupByMatrix('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.ManualFace({},{},'{}','{}',{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace, strName, nastranContact, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.ContactShareFace({},'{}','{}',{},{},{})".format(crlShareFace, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.ContactTable('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class NXNastran:
    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.ManualFace({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.ContactShareFace({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlShareFace, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName, iType, iAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, crplTargetPair, crEdit, iColor, iMethod):
        message = "Connections.Contacts.NXNastran.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iType, iAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, crplTargetPair, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.ManualGroup({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.ContactGroupByMatrix({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

class TSSolver:
    def ManualFace(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSolver.ManualFace('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def Auto(self, strlNames,crllMasterFaceTargets,crllSlaveFaceTargets, crlContactTypes, dlTaInterferenceClosures, dlTaFrictionCoefficients, blTaInitialAdjustments, crlColors, crlCrEdit, crlCrMasterGroup, crlCrSlaveGroup):
        message = "Connections.Contacts.TSSolver.Auto('{}',{},{},{},{},{},{},{},{},{},{})".format(strlNames,crllMasterFaceTargets,crllSlaveFaceTargets, crlContactTypes, dlTaInterferenceClosures, dlTaFrictionCoefficients, blTaInitialAdjustments, crlColors, crlCrEdit, crlCrMasterGroup, crlCrSlaveGroup)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName, tssolverContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSolver.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class TSSS:
    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSS.ManualFace({},{},'{}','{}',{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName, tssolverContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSS.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSS.ContactTable('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Equation:
    def MultiNodes(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.Equation.MultiNodes('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def TwoFace(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.Equation.TwoFace('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def SemiAuto(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.Equation.SemiAuto('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class General:
    def NodeToNode(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodeToNode('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodeToEdges(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodeToEdges('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodeToFaces(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodeToFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def TwoEdges(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.TwoEdges('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def FacesToFaces(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.FacesToFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodesToNodes(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodesToNodes('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def TwoFaces(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.TwoFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodeToAny(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodeToAny('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodesWithTolerance(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodesWithTolerance('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class RBar:
    def OneToOne(self, strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBar.OneToOne('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

    def OneToMany(self, strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBar.OneToMany('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

    def OneToOneNodesWithTolerance(self, strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBar.OneToOneNodesWithTolerance('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

class RBE2:
    def OneToMany(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.OneToMany({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def OneToOne(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.OneToOne({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def OneToOneNodesWithTolerance(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.OneToOneNodesWithTolerance({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def ToCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.ToCenter({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def ToCircleCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.ToCircleCenter({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

class RBE3:
    def OneToMany(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.OneToMany({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

    def OneToOne(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.OneToOne({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

    def ToCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.ToCenter({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

    def ToCircleCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.ToCircleCenter({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

class Nodeswithtolerance:
    def sameDoFs(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.Nodeswithtolerance.sameDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def differentDoFs(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.Nodeswithtolerance.differentDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class OneToOne:
    def sameDoFs(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.OneToOne.sameDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def differentDoFs(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.OneToOne.differentDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class Damper:
    def AnyEntities11DoFS(self, iMethod,strName,crlMasterTarget,crlSlaveTarget, crCoordSys, iGround, dTolerance, vecTDamper, vecRDamper, crEdit, bUpdateDispCS):
        message = "Connections.SpringsDampers.Damper.AnyEntities11DoFS({},'{}',{},{},{},{},{},{},{},{},{})".format(iMethod,strName,crlMasterTarget,crlSlaveTarget, crCoordSys, iGround, dTolerance, vecTDamper, vecRDamper, crEdit, bUpdateDispCS)
        return JPT_RUN_LINE(message)

class Bush:
    def TwoNodes(self, iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj):
        message = "Connections.SpringsDampers.Bush.TwoNodes({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

    def AnyEntities(self, iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj):
        message = "Connections.SpringsDampers.Bush.AnyEntities({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

    def OnetoOne(self, iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj):
        message = "Connections.SpringsDampers.Bush.OnetoOne({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

class Spring:
    def GroundedSpring(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.GroundedSpring({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    Nodeswithtolerance = Nodeswithtolerance()

    OneToOne = OneToOne()

class Pretension:
    def General(self, strName, iDir, dValue, bFixLength, crTable, crCoord, iLocalUnit, crlTarget, crEdit, bCreate2ADVCStatic):
        message = "Connections.Pretension.General('{}',{},{},{},{},{},{},{},{},{})".format(strName, iDir, dValue, bFixLength, crTable, crCoord, iLocalUnit, crlTarget, crEdit, bCreate2ADVCStatic)
        return JPT_RUN_LINE(message)

    def Abaqus(self, strName, bFixedLenght, crTable, dValue, iLocalUnit, strNormal, dlNodePos, crEdit, crlTarget):
        message = "Connections.Pretension.Abaqus('{}',{},{},{},{},'{}',{},{},{})".format(strName, bFixedLenght, crTable, dValue, iLocalUnit, strNormal, dlNodePos, crEdit, crlTarget)
        return JPT_RUN_LINE(message)

    def Advc(self, strName, bFixedLength, crEnforcedVelocity, dDvalue, iDirUpdateType, dlVnormal, dlCtrolNodePos, iRefNodeId, crEdit, crlTarget):
        message = "Connections.Pretension.Advc('{}',{},{},{},{},{},{},{},{},{})".format(strName, bFixedLength, crEnforcedVelocity, dDvalue, iDirUpdateType, dlVnormal, dlCtrolNodePos, iRefNodeId, crEdit, crlTarget)
        return JPT_RUN_LINE(message)

class BoltConnections:
    Edge = Edge()

    Face = Face()

class Contacts:
    Abaqus = Abaqus()

    ADVC = ADVC()

    Ansys = Ansys()

    MSCNastran = MSCNastran()

    NXNastran = NXNastran()

    TSSolver = TSSolver()

    TSSS = TSSS()

    def CheckPattern(self, crlParts, bShowMismatch, bShowMatch, dTol):
        message = "Connections.Contacts.CheckPattern({},{},{},{})".format(crlParts, bShowMismatch, bShowMatch, dTol)
        return JPT_RUN_LINE(message)

    def NXNastranGeneral(self, strName, iPiType, iPiAlg, dPdNorPenFactor, dPdTanPenFactor, dPdForceConTol, dPdMaxForceIter, dPdMaxStaIter, dPdChangeNum, dPdMinContactPer, iPiShellThickness, iPiContactStatus, iPiInitGapPenetra, iPiRegionRefine, iPiEvaluPts, dPdMinSearDist, dPdMaxSearDist, dPdFricCoef, dPdSearchDist, dPdPenatlyFactor, iPiShellOffset, crlTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.NXNastranGeneral('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPiType, iPiAlg, dPdNorPenFactor, dPdTanPenFactor, dPdForceConTol, dPdMaxForceIter, dPdMaxStaIter, dPdChangeNum, dPdMinContactPer, iPiShellThickness, iPiContactStatus, iPiInitGapPenetra, iPiRegionRefine, iPiEvaluPts, dPdMinSearDist, dPdMaxSearDist, dPdFricCoef, dPdSearchDist, dPdPenatlyFactor, iPiShellOffset, crlTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ExportCheckReport(self, strFullPath, dZoomFactor, iFitBy, iListBy, iListOrder, iFormat):
        message = "Connections.Contacts.ExportCheckReport('{}',{},{},{},{},{})".format(strFullPath, dZoomFactor, iFitBy, iListBy, iListOrder, iFormat)
        return JPT_RUN_LINE(message)

class Gaps:
    def TwoNodes(self, crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur):
        message = "Connections.Gaps.TwoNodes({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

    def TwoEdges(self, crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur):
        message = "Connections.Gaps.TwoEdges({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

    def TwoFaces(self, crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur):
        message = "Connections.Gaps.TwoFaces({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

class MPC:
    Equation = Equation()

    General = General()

class RigidElements:
    RBar = RBar()

    RBE2 = RBE2()

    RBE3 = RBE3()

    def RBarGeneral(self, rbarConnection, crlMasterTarget, crlSlaveTarget, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBarGeneral({},{},{},{},{},{},{})".format(rbarConnection, crlMasterTarget, crlSlaveTarget, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

    def RBE2General(self, iMethod,crlMasterTarget,crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iDuplicateMode):
        message = "Connections.RigidElements.RBE2General({},{},{},{},'{}',{},{},{},{},{},{},{},{},{})".format(iMethod,crlMasterTarget,crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def RBE3General(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly):
        message = "Connections.RigidElements.RBE3General({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly)
        return JPT_RUN_LINE(message)

class SpringsDampers:
    Damper = Damper()

    def BushGeneral(self, iMethod,strName,crlMaster,crlSlave,crCoord,dTol,iGround,iOriMode,iEqual,poslVector,dlStiffness,dlDampCoef,dlDampConst,dRotStrain,dTransStrain,dRotStress,dTransStress,crEditObj):
        message = "Connections.SpringsDampers.BushGeneral({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod,strName,crlMaster,crlSlave,crCoord,dTol,iGround,iOriMode,iEqual,poslVector,dlStiffness,dlDampCoef,dlDampConst,dRotStrain,dTransStrain,dRotStress,dTransStress,crEditObj)
        return JPT_RUN_LINE(message)

    Bush = Bush()

    Spring = Spring()

class SZ:
    def WeldLine2(self, crlFaces,crlParts,dLayerWidth,iLayerNumber):
        message = "ExManifoldModeling.SZ.WeldLine2({},{},{},{})".format(crlFaces,crlParts,dLayerWidth,iLayerNumber)
        return JPT_RUN_LINE(message)

class Bar:
    def TwoNodes(self, strPartName, iMeshCount, crStartNode, crEndNode):
        message = "Geometry.Bar.TwoNodes('{}',{},{},{})".format(strPartName, iMeshCount, crStartNode, crEndNode)
        return JPT_RUN_LINE(message)

    def Arc(self, crlVcrNode, crPart, strBarName):
        message = "Geometry.Bar.Arc({},{},'{}')".format(crlVcrNode, crPart, strBarName)
        return JPT_RUN_LINE(message)

    def Spline(self, crlVcrNode, crPart, strBarName):
        message = "Geometry.Bar.Spline({},{},'{}')".format(crlVcrNode, crPart, strBarName)
        return JPT_RUN_LINE(message)

class BodyCut:
    def XXYYOnOnePoint(self, crPart, posCutPos, iType, dOffset, bSplit, bSectionFace, bShateFace, crLocalCoor):
        message = "Geometry.BodyCut.XXYYOnOnePoint({},{},{},{},{},{},{},{})".format(crPart, posCutPos, iType, dOffset, bSplit, bSectionFace, bShateFace, crLocalCoor)
        return JPT_RUN_LINE(message)

    def BySurface(self, crlPart,crCutter, bSplitOnly, bMakeSectionFace, bShareFace, bSeparateFace):
        message = "Geometry.BodyCut.BySurface({},{},{},{},{},{})".format(crlPart,crCutter, bSplitOnly, bMakeSectionFace, bShareFace, bSeparateFace)
        return JPT_RUN_LINE(message)

    def By3Points(self, crPart, poslPosition, dOffset, bSplitonly, bMakesectionface, bShareface):
        message = "Geometry.BodyCut.By3Points({},{},{},{},{},{})".format(crPart, poslPosition, dOffset, bSplitonly, bMakesectionface, bShareface)
        return JPT_RUN_LINE(message)

class BreakEntity:
    def StlPart(self, crlPart, iMinNoOfFaces, iMethod):
        message = "Geometry.BreakEntity.StlPart({},{},{})".format(crlPart, iMinNoOfFaces, iMethod)
        return JPT_RUN_LINE(message)

    def Face(self, crlFaces):
        message = "Geometry.BreakEntity.Face({})".format(crlFaces)
        return JPT_RUN_LINE(message)

    def Edge(self, crlPart, crlFace, crlEdge, crlNode, bAutoByAngle, dEdgeAngle):
        message = "Geometry.BreakEntity.Edge({},{},{},{},{},{})".format(crlPart, crlFace, crlEdge, crlNode, bAutoByAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def Part(self, crlPart):
        message = "Geometry.BreakEntity.Part({})".format(crlPart)
        return JPT_RUN_LINE(message)

class DeleteEntity:
    def Part(self, crlPart):
        message = "Geometry.DeleteEntity.Part({})".format(crlPart)
        return JPT_RUN_LINE(message)

    def Edge(self, crlEdge):
        message = "Geometry.DeleteEntity.Edge({})".format(crlEdge)
        return JPT_RUN_LINE(message)

    def Vertex(self, crlVertex):
        message = "Geometry.DeleteEntity.Vertex({})".format(crlVertex)
        return JPT_RUN_LINE(message)

    def Face(self, crlFace, bKeepSolid):
        message = "Geometry.DeleteEntity.Face({},{})".format(crlFace, bKeepSolid)
        return JPT_RUN_LINE(message)

class Edge:
    def Line(self, poslPositions,crlCrTargetFace, bBreakFace):
        message = "Geometry.Edge.Line({},{},{})".format(poslPositions,crlCrTargetFace, bBreakFace)
        return JPT_RUN_LINE(message)

    def Spline(self, veclAprroxiPositions,crlTargetFace, bBreakFace):
        message = "Geometry.Edge.Spline({},{},{})".format(veclAprroxiPositions,crlTargetFace, bBreakFace)
        return JPT_RUN_LINE(message)

    def PlanarLine(self, veclPosition,crlTargetFace, crLocalCoord, iType, bBreakFace):
        message = "Geometry.Edge.PlanarLine({},{},{},{},{})".format(veclPosition,crlTargetFace, crLocalCoord, iType, bBreakFace)
        return JPT_RUN_LINE(message)

    def Circle(self, veclPositions,crlTargetFace, dInRadius, dOutRadius, iNoOfLayer, iNoOfDiv, bBreakFace):
        message = "Geometry.Edge.Circle({},{},{},{},{},{},{})".format(veclPositions,crlTargetFace, dInRadius, dOutRadius, iNoOfLayer, iNoOfDiv, bBreakFace)
        return JPT_RUN_LINE(message)

    def PerpendicularLineOfEdge(self, crlNodes,crlFaces, dOffset, bReakFace):
        message = "Geometry.Edge.PerpendicularLineOfEdge({},{},{},{})".format(crlNodes,crlFaces, dOffset, bReakFace)
        return JPT_RUN_LINE(message)

    def ExtendLine(self, crlVcrEdges, iMethod, iEnd, iNoFittingPoints, iDiv, iBBreakFace):
        message = "Geometry.Edge.ExtendLine({},{},{},{},{},{})".format(crlVcrEdges, iMethod, iEnd, iNoFittingPoints, iDiv, iBBreakFace)
        return JPT_RUN_LINE(message)

    def ElementEdges(self, crplElemEdge, bBreakEdge):
        message = "Geometry.Edge.ElementEdges({},{})".format(crplElemEdge, bBreakEdge)
        return JPT_RUN_LINE(message)

    def Angle(self, crpPair, dAngle, bCurvature, bBreakFace):
        message = "Geometry.Edge.Angle({},{},{},{})".format(crpPair, dAngle, bCurvature, bBreakFace)
        return JPT_RUN_LINE(message)

    def NodeShortestPath(self, crFirstNode,crSecondNode, iBreakFace):
        message = "Geometry.Edge.NodeShortestPath({},{},{})".format(crFirstNode,crSecondNode, iBreakFace)
        return JPT_RUN_LINE(message)

    def OffsetLine(self, crlFaces, crlEdges, bBreakFace, dOffsetDistance, iNumberLayer, bMerge, bExtend, iLayerMethod, dlVlayerOffset, bAutoCollapse, iRLType):
        message = "Geometry.Edge.OffsetLine({},{},{},{},{},{},{},{},{},{},{})".format(crlFaces, crlEdges, bBreakFace, dOffsetDistance, iNumberLayer, bMerge, bExtend, iLayerMethod, dlVlayerOffset, bAutoCollapse, iRLType)
        return JPT_RUN_LINE(message)

    def SplineFreeEdges(self, crlVcrNode, iBArc, crPart, strBarName):
        message = "Geometry.Edge.SplineFreeEdges({},{},{},'{}')".format(crlVcrNode, iBArc, crPart, strBarName)
        return JPT_RUN_LINE(message)

    def ClosedLine(self, veclPositions,crlCrTargetFace, iBBreakFace):
        message = "Geometry.Edge.ClosedLine({},{},{})".format(veclPositions,crlCrTargetFace, iBBreakFace)
        return JPT_RUN_LINE(message)

    def PerpendicularCylinderLine(self, crlNode, crlFaces, iMethod, dOffset, bOppositeSide, bBreakFace):
        message = "Geometry.Edge.PerpendicularCylinderLine({},{},{},{},{},{})".format(crlNode, crlFaces, iMethod, dOffset, bOppositeSide, bBreakFace)
        return JPT_RUN_LINE(message)

    def IntersectionLine(self, crlCrFaces, bBreakFace):
        message = "Geometry.Edge.IntersectionLine({},{})".format(crlCrFaces, bBreakFace)
        return JPT_RUN_LINE(message)

    def ProjectLine(self, crlCrEdges, crlCrFaces, crlCrNodes, bBreakFace, iType, bCheckGap, dGap):
        message = "Geometry.Edge.ProjectLine({},{},{},{},{},{},{})".format(crlCrEdges, crlCrFaces, crlCrNodes, bBreakFace, iType, bCheckGap, dGap)
        return JPT_RUN_LINE(message)

    def PerpendicularLineToEdge(self, crNode, crEdge, crlFace, bBreakFace):
        message = "Geometry.Edge.PerpendicularLineToEdge({},{},{},{})".format(crNode, crEdge, crlFace, bBreakFace)
        return JPT_RUN_LINE(message)

class Face:
    def FourEdges(self, crlVcrEdges):
        message = "Geometry.Face.FourEdges({})".format(crlVcrEdges)
        return JPT_RUN_LINE(message)

    def FromMesh(self, crlFace):
        message = "Geometry.Face.FromMesh({})".format(crlFace)
        return JPT_RUN_LINE(message)

    def CreateSmoothFace(self, bInterPoration,crlTargetCa,iElemGeneration,dGradation,iBFaceSmooth,crTargetPart):
        message = "Geometry.Face.CreateSmoothFace({},{},{},{},{},{})".format(bInterPoration,crlTargetCa,iElemGeneration,dGradation,iBFaceSmooth,crTargetPart)
        return JPT_RUN_LINE(message)

    def Edges(self, crlEdge, crlPart, crlNode, bSharedFace, bSmoothFace, bCreatePart, bImproved, bBarsOnly, bOnlyOnePart, bUseMidNodes):
        message = "Geometry.Face.Edges({},{},{},{},{},{},{},{},{},{})".format(crlEdge, crlPart, crlNode, bSharedFace, bSmoothFace, bCreatePart, bImproved, bBarsOnly, bOnlyOnePart, bUseMidNodes)
        return JPT_RUN_LINE(message)

    def Elements(self, crlElem, bShareFace):
        message = "Geometry.Face.Elements({},{})".format(crlElem, bShareFace)
        return JPT_RUN_LINE(message)

class FindFeature:
    def DelCircChamfer(self, crlPart, dMaxThick, dMinThick):
        message = "Geometry.FindFeature.DelCircChamfer({},{},{})".format(crlPart, dMaxThick, dMinThick)
        return JPT_RUN_LINE(message)

    def Fillet(self, crPart, crFace, dMinAngle, dMaxAngle, dMinFaceWidth, dMaxFaceWidth, dMinCurveRadius, dMaxCurveRadius, dScale):
        message = "Geometry.FindFeature.Fillet({},{},{},{},{},{},{},{},{})".format(crPart, crFace, dMinAngle, dMaxAngle, dMinFaceWidth, dMaxFaceWidth, dMinCurveRadius, dMaxCurveRadius, dScale)
        return JPT_RUN_LINE(message)

    def Faces(self, taBodyKey,iOption, taEdgeKey, bCylinder, bDisc, bFourCorners, dMinThickness, dMaxThickness, dDiameterMin, dDiameterMax, taFaceKey):
        message = "Geometry.FindFeature.Faces({},{},{},{},{},{},{},{},{},{},{})".format(taBodyKey,iOption, taEdgeKey, bCylinder, bDisc, bFourCorners, dMinThickness, dMaxThickness, dDiameterMin, dDiameterMax, taFaceKey)
        return JPT_RUN_LINE(message)

    def Edges(self, taBodyKey,iOption, taEdgeKey, bCylinder, bDisc, bFourCorners, dMinThickness, dMaxThickness, dDiameterMin, dDiameterMax, taFaceKey):
        message = "Geometry.FindFeature.Edges({},{},{},{},{},{},{},{},{},{},{})".format(taBodyKey,iOption, taEdgeKey, bCylinder, bDisc, bFourCorners, dMinThickness, dMaxThickness, dDiameterMin, dDiameterMax, taFaceKey)
        return JPT_RUN_LINE(message)

class MergeEntities:
    def Faces(self, crlFace, bMergeEdge, bRemoveNonBoundEdge):
        message = "Geometry.MergeEntities.Faces({},{},{})".format(crlFace, bMergeEdge, bRemoveNonBoundEdge)
        return JPT_RUN_LINE(message)

    def TinyFacesMerge(self, ilPartkeys, ilFacekeys, dMinFaceWidth, dMaxFaceWidth, dFaceAngle, bReferLocalSetting, bConnectFace):
        message = "Geometry.MergeEntities.TinyFacesMerge({},{},{},{},{},{},{})".format(ilPartkeys, ilFacekeys, dMinFaceWidth, dMaxFaceWidth, dFaceAngle, bReferLocalSetting, bConnectFace)
        return JPT_RUN_LINE(message)

    def CBarParts(self, crlPart):
        message = "Geometry.MergeEntities.CBarParts({})".format(crlPart)
        return JPT_RUN_LINE(message)

    def Edges(self, crlEdge):
        message = "Geometry.MergeEntities.Edges({})".format(crlEdge)
        return JPT_RUN_LINE(message)

    def Parts(self, dTolerance, bRemovesharefaceflag, crlPart):
        message = "Geometry.MergeEntities.Parts({},{},{})".format(dTolerance, bRemovesharefaceflag, crlPart)
        return JPT_RUN_LINE(message)

    def PartFaces(self, crlPart, crlFace, bAngle, dTolAngle, bWidth, dTolWidth):
        message = "Geometry.MergeEntities.PartFaces({},{},{},{},{},{})".format(crlPart, crlFace, bAngle, dTolAngle, bWidth, dTolWidth)
        return JPT_RUN_LINE(message)

class Part:
    def Cube(self, dlVdOrigin, dlVdLength, ilVlNodeCnt, strPartName, iColPart, crCoord):
        message = "Geometry.Part.Cube({},{},{},'{}',{},{})".format(dlVdOrigin, dlVdLength, ilVlNodeCnt, strPartName, iColPart, crCoord)
        return JPT_RUN_LINE(message)

    def Wedge(self, vecOrigin, vecLength, vecNodeCount, strPartName, iPartColor, crCoordinate):
        message = "Geometry.Part.Wedge({},{},{},'{}',{},{})".format(vecOrigin, vecLength, vecNodeCount, strPartName, iPartColor, crCoordinate)
        return JPT_RUN_LINE(message)

    def Sphere(self, dlVdOrigin, dRadius, iLatitudeNodeCnt, iLongitudeNodeCnt, strPartName, iColPart, crCoord):
        message = "Geometry.Part.Sphere({},{},{},{},'{}',{},{})".format(dlVdOrigin, dRadius, iLatitudeNodeCnt, iLongitudeNodeCnt, strPartName, iColPart, crCoord)
        return JPT_RUN_LINE(message)

    def Torus(self, dlVdOrigin, dInnerRadius, dRingRadius, iLatitudeNodeCnt, iLongitudeNodeCnt, strPartName, iColPart, crCoord):
        message = "Geometry.Part.Torus({},{},{},{},{},'{}',{},{})".format(dlVdOrigin, dInnerRadius, dRingRadius, iLatitudeNodeCnt, iLongitudeNodeCnt, strPartName, iColPart, crCoord)
        return JPT_RUN_LINE(message)

    def Elems(self, crlListElem,strPartName):
        message = "Geometry.Part.Elems({},'{}')".format(crlListElem,strPartName)
        return JPT_RUN_LINE(message)

    def Cylinder(self, dlOrigin, dTopRadius, dBotRadius, dHeight, iCircleNodeCnt, iAxisNodeCnt, strName, iPartCol, crCoord):
        message = "Geometry.Part.Cylinder({},{},{},{},{},{},'{}',{},{})".format(dlOrigin, dTopRadius, dBotRadius, dHeight, iCircleNodeCnt, iAxisNodeCnt, strName, iPartCol, crCoord)
        return JPT_RUN_LINE(message)

    def Tube(self, dlOrigin, dTopInnerRadius, dTopOuterRadius, dBotInnerRadius, dBotOuterRadius, dHeight, iCircleNodeCnt, iAxisNodeCnt, strName, iPartCol, crCoord):
        message = "Geometry.Part.Tube({},{},{},{},{},{},{},{},'{}',{},{})".format(dlOrigin, dTopInnerRadius, dTopOuterRadius, dBotInnerRadius, dBotOuterRadius, dHeight, iCircleNodeCnt, iAxisNodeCnt, strName, iPartCol, crCoord)
        return JPT_RUN_LINE(message)

    def Trapezoid(self, dlVdOrigin, dlVdLength, dTopXLength, dRadius, ilVlNodeCnt, strPartName, iColPart, crCoord):
        message = "Geometry.Part.Trapezoid({},{},{},{},{},'{}',{},{})".format(dlVdOrigin, dlVdLength, dTopXLength, dRadius, ilVlNodeCnt, strPartName, iColPart, crCoord)
        return JPT_RUN_LINE(message)

    def Cone(self, dlOriginXyz, dBottomRadius, dHeight, iCircleNodeCount, iAxisNodeCnt, strPartName, iPartColor, crCoordinate):
        message = "Geometry.Part.Cone({},{},{},{},{},'{}',{},{})".format(dlOriginXyz, dBottomRadius, dHeight, iCircleNodeCount, iAxisNodeCnt, strPartName, iPartColor, crCoordinate)
        return JPT_RUN_LINE(message)

class ShowAdjacent:
    def Faces(self, Angle, IncludeStopFace, Layer,IsPreview, taStartFaceCr,taStopFaceCr):
        message = "Geometry.ShowAdjacent.Faces({},{},{},{},{},{})".format(Angle, IncludeStopFace, Layer,IsPreview, taStartFaceCr,taStopFaceCr)
        return JPT_RUN_LINE(message)

    def Elements(self, Angle, IncludeStopElem, Layer,IsPreview, taStartElemCr,taStopElemCr):
        message = "Geometry.ShowAdjacent.Elements({},{},{},{},{},{})".format(Angle, IncludeStopElem, Layer,IsPreview, taStartElemCr,taStopElemCr)
        return JPT_RUN_LINE(message)

class Transform:
    def Rotation(self, crlPart, posCenter, vecAxis, dAngle, bCreateNewPart, bCopyLBC, bCopyProperty, iCopyCount, bMergeNode, dTol):
        message = "Geometry.Transform.Rotation({},{},{},{},{},{},{},{},{},{})".format(crlPart, posCenter, vecAxis, dAngle, bCreateNewPart, bCopyLBC, bCopyProperty, iCopyCount, bMergeNode, dTol)
        return JPT_RUN_LINE(message)

    def Scaling(self, crlPart, dlScaleVector, dlScaleCentre, crCoordinate, bCreateNew, bCopyLbc, bCopyProperty, bUsepartcenter):
        message = "Geometry.Transform.Scaling({},{},{},{},{},{},{},{})".format(crlPart, dlScaleVector, dlScaleCentre, crCoordinate, bCreateNew, bCopyLbc, bCopyProperty, bUsepartcenter)
        return JPT_RUN_LINE(message)

    def Mirror(self, crlPart, veclPoint, dOffset, bCreateNewPart, bCopyLBC, bCopyProperty, bRemoveDupFace, bMergeNode, dTol):
        message = "Geometry.Transform.Mirror({},{},{},{},{},{},{},{},{})".format(crlPart, veclPoint, dOffset, bCreateNewPart, bCopyLBC, bCopyProperty, bRemoveDupFace, bMergeNode, dTol)
        return JPT_RUN_LINE(message)

    def Position(self, crlPart, veclPoint, bCreateNewPart, bCopyLBC, bCopyProperty):
        message = "Geometry.Transform.Position({},{},{},{},{})".format(crlPart, veclPoint, bCreateNewPart, bCopyLBC, bCopyProperty)
        return JPT_RUN_LINE(message)

    def Translation(self, crlPart, poslTavdTranslates, crCoord, bCreateNewPart, bCopyLBC, bCopyProperty, iCopyCount):
        message = "Geometry.Transform.Translation({},{},{},{},{},{},{})".format(crlPart, poslTavdTranslates, crCoord, bCreateNewPart, bCopyLBC, bCopyProperty, iCopyCount)
        return JPT_RUN_LINE(message)

    def MatingFace(self, crlPart, crSrcFace, crDstFace, crSrcEdge, crDstEdge, crSrcNode, crDstNode, iFaceOpposite, dEdgeAngle, iEdgeOpposite, iAlignMethodType, iAdjustPointType, iAdjustProjectionType, dlAlignVector, dlAdjustPoint, dlAdjustVector, bCreateNewPart, bCopyLBC, bCopyProperty, bIsPreview, crlCoordSyss):
        message = "Geometry.Transform.MatingFace({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, crSrcFace, crDstFace, crSrcEdge, crDstEdge, crSrcNode, crDstNode, iFaceOpposite, dEdgeAngle, iEdgeOpposite, iAlignMethodType, iAdjustPointType, iAdjustProjectionType, dlAlignVector, dlAdjustPoint, dlAdjustVector, bCreateNewPart, bCopyLBC, bCopyProperty, bIsPreview, crlCoordSyss)
        return JPT_RUN_LINE(message)

    def CylinderFace(self, crlPart, veclPoint, bCreateNewPart, bCopyLBC, bCopyProperty):
        message = "Geometry.Transform.CylinderFace({},{},{},{},{})".format(crlPart, veclPoint, bCreateNewPart, bCopyLBC, bCopyProperty)
        return JPT_RUN_LINE(message)

class RightClick:
    def PropertyGroup(self, strTmp):
        message = "Groups.RightClick.PropertyGroup('{}')".format(strTmp)
        return JPT_RUN_LINE(message)

    def Rename(self, strNewName,crItem):
        message = "Groups.RightClick.Rename('{}',{})".format(strNewName,crItem)
        return JPT_RUN_LINE(message)

    def DeleteGroup(self, crlDelGroup, bRemoveAll):
        message = "Groups.RightClick.DeleteGroup({},{})".format(crlDelGroup, bRemoveAll)
        return JPT_RUN_LINE(message)

    def CopyGroup(self, crlSrc, strlNames, crDest, bKeep):
        message = "Groups.RightClick.CopyGroup({},'{}',{},{})".format(crlSrc, strlNames, crDest, bKeep)
        return JPT_RUN_LINE(message)

    def AddSupGroup(self, crSupGroupSelected):
        message = "Groups.RightClick.AddSupGroup({})".format(crSupGroupSelected)
        return JPT_RUN_LINE(message)

    def CreateMatGroup(self, strTmp):
        message = "Groups.RightClick.CreateMatGroup('{}')".format(strTmp)
        return JPT_RUN_LINE(message)

class ImportCAD:
    def Elysium(self, strlPath, dChordHeightTolerance, dAngleToleranceDegree, dPointCoincidentTolerance, iConvertIsolatedCurve, iDekCleanselfintersectingloop, iDekVolumetopart, iIgesFixedcurevepreference, iIgesAutostitch, dIgesStitchtolerance, iCatiaConvertnotshowedelement, iCatiaConvertnotshowedinstance, iCatiaConvertaxis, iStepCreateseam, dStepPointtolerance, iAcisHealacisbeforeversion, iJtConvertgeometrytype, bFaceColor, iJtConvertgeneralpart, iJtConvertaxis, iJtConvertcenterline):
        message = "Home.ImportCAD.Elysium('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strlPath, dChordHeightTolerance, dAngleToleranceDegree, dPointCoincidentTolerance, iConvertIsolatedCurve, iDekCleanselfintersectingloop, iDekVolumetopart, iIgesFixedcurevepreference, iIgesAutostitch, dIgesStitchtolerance, iCatiaConvertnotshowedelement, iCatiaConvertnotshowedinstance, iCatiaConvertaxis, iStepCreateseam, dStepPointtolerance, iAcisHealacisbeforeversion, iJtConvertgeometrytype, bFaceColor, iJtConvertgeneralpart, iJtConvertaxis, iJtConvertcenterline)
        return JPT_RUN_LINE(message)

    def Spatial(self, strlPath, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, bNXMultipart, bHealing, bIsNXDirect, bSetFaceColor, strCsvFilePath):
        message = "Home.ImportCAD.Spatial('{}',{},{},{},{},{},{},{},'{}')".format(strlPath, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, bNXMultipart, bHealing, bIsNXDirect, bSetFaceColor, strCsvFilePath)
        return JPT_RUN_LINE(message)

    def Parasolid(self, strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale):
        message = "Home.ImportCAD.Parasolid('{}',{},{},{},{},{},{},{},{},{},{})".format(strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale)
        return JPT_RUN_LINE(message)

    def STL(self, strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale):
        message = "Home.ImportCAD.STL('{}',{},{},{},{},{},{},{},{},{},{})".format(strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale)
        return JPT_RUN_LINE(message)

    def VRML(self, strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale):
        message = "Home.ImportCAD.VRML('{}',{},{},{},{},{},{},{},{},{},{})".format(strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale)
        return JPT_RUN_LINE(message)

    def ProECreoDirect(self, strlPath, dChordHeightTolerance, dAngleToleranceDegree, dStepMaxSize):
        message = "Home.ImportCAD.ProECreoDirect('{}',{},{},{})".format(strlPath, dChordHeightTolerance, dAngleToleranceDegree, dStepMaxSize)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def ADVCADX(self, strPath, dFaceAngle, dEdgeAngle):
        message = "Home.ImportMesh.ADVCADX('{}',{},{})".format(strPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def AnsysDat(self, strlPath, dFaceAngle, dEdgeAngle):
        message = "Home.ImportMesh.AnsysDat('{}',{},{})".format(strlPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def NastranBdf(self, strlFilePaths, iMportType, dFaceAngle, dEdgeAngle, bReadNameComment, iCreateDup1DElemAnswer):
        message = "Home.ImportMesh.NastranBdf('{}',{},{},{},{},{})".format(strlFilePaths, iMportType, dFaceAngle, dEdgeAngle, bReadNameComment, iCreateDup1DElemAnswer)
        return JPT_RUN_LINE(message)

    def AbaqusINP(self, strlFilePaths, dFaceAngle, dEdgeAngle, iMportType):
        message = "Home.ImportMesh.AbaqusINP('{}',{},{},{})".format(strlFilePaths, dFaceAngle, dEdgeAngle, iMportType)
        return JPT_RUN_LINE(message)

    def LSDYNA(self, strlPath, dFaceAngle, dEdgeAngle):
        message = "Home.ImportMesh.LSDYNA('{}',{},{})".format(strlPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def Universal(self, strPath):
        message = "Home.ImportMesh.Universal('{}')".format(strPath)
        return JPT_RUN_LINE(message)

class RightClick:
    def MergeFaces(self, crlListFace, bIsMergeEdge, bRemoveNonBoundEdge):
        message = "MainWindow.RightClick.MergeFaces({},{},{})".format(crlListFace, bIsMergeEdge, bRemoveNonBoundEdge)
        return JPT_RUN_LINE(message)

    def SelectAllParts(self, ):
        message = "MainWindow.RightClick.SelectAllParts({})".format()
        return JPT_RUN_LINE(message)

    def AssociatedPick(self, crlInput,strTarget, strConnect):
        message = "MainWindow.RightClick.AssociatedPick({},'{}','{}')".format(crlInput,strTarget, strConnect)
        return JPT_RUN_LINE(message)

    def FlipElement(self, crlTargets):
        message = "MainWindow.RightClick.FlipElement({})".format(crlTargets)
        return JPT_RUN_LINE(message)

class Element:
    def SurfaceElement(self, ilElement,ilFace,ilPart,iCreateNewPart):
        message = "MeshCleanup.ChangeTopology.Element.SurfaceElement({},{},{},{})".format(ilElement,ilFace,ilPart,iCreateNewPart)
        return JPT_RUN_LINE(message)

class MergeElement:
    def TwoQuadsToQuad(self, crlElements):
        message = "MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad({})".format(crlElements)
        return JPT_RUN_LINE(message)

    def TwoQuadsToQuad(self, crlElements):
        message = "MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad({})".format(crlElements)
        return JPT_RUN_LINE(message)

    def TwoTrisToQuad(self, crlElems):
        message = "MeshCleanup.Manual2D.MergeElement.TwoTrisToQuad({})".format(crlElems)
        return JPT_RUN_LINE(message)

class SplitElement:
    def QuadTo4Quads(self, crlElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo4Quads({},{},{},{},{},{},{},{})".format(crlElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadToTrans4Quads(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadToTrans4Quads({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadToTrans3Quads(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadToTrans3Quads({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo2Quads1Tri(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo2Quads1Tri({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo3Tris(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo3Tris({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo2Quads(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo2Quads({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo2Tris(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo2Tris({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadToQuadTri(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadToQuadTri({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo4Tris(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo4Tris({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class Collapse:
    def CenterFaceCollapse(self, crlElem):
        message = "MeshCleanup.Manual3D.Collapse.CenterFaceCollapse({})".format(crlElem)
        return JPT_RUN_LINE(message)

    def HalfEdgeCollapse(self, crplElemEdge):
        message = "MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse({})".format(crplElemEdge)
        return JPT_RUN_LINE(message)

    def EdgeCollapse(self, crplElemEdge, crlNode):
        message = "MeshCleanup.Manual3D.Collapse.EdgeCollapse({},{})".format(crplElemEdge, crlNode)
        return JPT_RUN_LINE(message)

class Element:
    def SolidElement(self, crlListElem, crPart):
        message = "MeshCleanup.Element.SolidElement({},{})".format(crlListElem, crPart)
        return JPT_RUN_LINE(message)

    def SurfaceElement(self, ilElement, ilFace, ilPart, iCreateNewPart):
        message = "MeshCleanup.Element.SurfaceElement({},{},{},{})".format(ilElement, ilFace, ilPart, iCreateNewPart)
        return JPT_RUN_LINE(message)

class ChangeTopology:
    Element = Element()

class Cleanup:
    def CloseGap(self, crlPartCur,dDistanceTol):
        message = "MeshCleanup.Cleanup.CloseGap({},{})".format(crlPartCur,dDistanceTol)
        return JPT_RUN_LINE(message)

class Manual2D:
    MergeElement = MergeElement()

    SplitElement = SplitElement()

    def Equivalence(self, crlNode, iTypeEquiva, dTolerance):
        message = "MeshCleanup.Manual2D.Equivalence({},{},{})".format(crlNode, iTypeEquiva, dTolerance)
        return JPT_RUN_LINE(message)

    def DeleteElement(self, crlElems, bKeepShareElem):
        message = "MeshCleanup.Manual2D.DeleteElement({},{})".format(crlElems, bKeepShareElem)
        return JPT_RUN_LINE(message)

    def Split(self, crplElemEdge, dRatio, crNodeRef, crProjPart):
        message = "MeshCleanup.Manual2D.Split({},{},{},{})".format(crplElemEdge, dRatio, crNodeRef, crProjPart)
        return JPT_RUN_LINE(message)

    def Swap(self, crplElemEdge):
        message = "MeshCleanup.Manual2D.Swap({})".format(crplElemEdge)
        return JPT_RUN_LINE(message)

    def Collapse(self, crNodeRef, crNodeEq):
        message = "MeshCleanup.Manual2D.Collapse({},{})".format(crNodeRef, crNodeEq)
        return JPT_RUN_LINE(message)

    def CreateElement(self, nElemType, crParentEntity, crlViNodeKey):
        message = "MeshCleanup.Manual2D.CreateElement({},{},{})".format(nElemType, crParentEntity, crlViNodeKey)
        return JPT_RUN_LINE(message)

    def RemeshElement(self, crlTarget, surfaceMesh, bUseSetting, bGrading, bFMesher, iOverrideType, bKeepConnection, bProjCAD, bTinyFaceMerge, dMinFaceWidth, dMaxFaceWidth, bIDchcek, bKeepRemeshEdge):
        message = "MeshCleanup.Manual2D.RemeshElement({},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlTarget, surfaceMesh, bUseSetting, bGrading, bFMesher, iOverrideType, bKeepConnection, bProjCAD, bTinyFaceMerge, dMinFaceWidth, dMaxFaceWidth, bIDchcek, bKeepRemeshEdge)
        return JPT_RUN_LINE(message)

class Manual3D:
    Collapse = Collapse()

    def DeleteNode(self, crlNode):
        message = "MeshCleanup.Manual3D.DeleteNode({})".format(crlNode)
        return JPT_RUN_LINE(message)

    def Swap(self, crplElemEdge):
        message = "MeshCleanup.Manual3D.Swap({})".format(crplElemEdge)
        return JPT_RUN_LINE(message)

    def Equivalence(self, crlNode, iMergeTowards):
        message = "MeshCleanup.Manual3D.Equivalence({},{})".format(crlNode, iMergeTowards)
        return JPT_RUN_LINE(message)

    def Split(self, crplElemEdge, crlNode, dRatioDistance):
        message = "MeshCleanup.Manual3D.Split({},{},{})".format(crplElemEdge, crlNode, dRatioDistance)
        return JPT_RUN_LINE(message)

    def CreateHex(self, iParentEntityId, crlElem, iSeprateN):
        message = "MeshCleanup.Manual3D.CreateHex({},{},{})".format(iParentEntityId, crlElem, iSeprateN)
        return JPT_RUN_LINE(message)

    def CreatePenta(self, iParentEntityId, crlVcrElem):
        message = "MeshCleanup.Manual3D.CreatePenta({},{})".format(iParentEntityId, crlVcrElem)
        return JPT_RUN_LINE(message)

    def CreateTetra(self, iParentEntityId, crlNode, crlElem):
        message = "MeshCleanup.Manual3D.CreateTetra({},{},{})".format(iParentEntityId, crlNode, crlElem)
        return JPT_RUN_LINE(message)

class CreateElement:
    def Hex(self, iParentEntityId, crlElem, iSeprateN):
        message = "MeshEdit.CreateElement.Hex({},{},{})".format(iParentEntityId, crlElem, iSeprateN)
        return JPT_RUN_LINE(message)

    def Penta(self, iParentEntityId, crlElem):
        message = "MeshEdit.CreateElement.Penta({},{})".format(iParentEntityId, crlElem)
        return JPT_RUN_LINE(message)

    def Tet(self, iParentEntityId, crlNode, crlElem):
        message = "MeshEdit.CreateElement.Tet({},{},{})".format(iParentEntityId, crlNode, crlElem)
        return JPT_RUN_LINE(message)

    def Tri3(self, iElemType, crParentEntity, crlNode):
        message = "MeshEdit.CreateElement.Tri3({},{},{})".format(iElemType, crParentEntity, crlNode)
        return JPT_RUN_LINE(message)

    def Quad4(self, iElemType, crParentEntity, crlNode):
        message = "MeshEdit.CreateElement.Quad4({},{},{})".format(iElemType, crParentEntity, crlNode)
        return JPT_RUN_LINE(message)

class CreateNode:
    def CircleCenter(self, crlEdges,iNodeID, bImprint, crFace):
        message = "MeshEdit.CreateNode.CircleCenter({},{},{},{})".format(crlEdges,iNodeID, bImprint, crFace)
        return JPT_RUN_LINE(message)

    def Absolute(self, veclNodeCoord, ilNewNodeID):
        message = "MeshEdit.CreateNode.Absolute({},{})".format(veclNodeCoord, ilNewNodeID)
        return JPT_RUN_LINE(message)

    def Import(self, strCsvFilePath):
        message = "MeshEdit.CreateNode.Import('{}')".format(strCsvFilePath)
        return JPT_RUN_LINE(message)

    def Point(self, iodeID, posPoint, bImprint, crShape):
        message = "MeshEdit.CreateNode.Point({},{},{},{})".format(iodeID, posPoint, bImprint, crShape)
        return JPT_RUN_LINE(message)

    def Between2Nodes(self, iNodeID, dX, dY, dZ, iNumberofNodes, bImprint, crlNode, crlFace):
        message = "MeshEdit.CreateNode.Between2Nodes({},{},{},{},{},{},{},{})".format(iNodeID, dX, dY, dZ, iNumberofNodes, bImprint, crlNode, crlFace)
        return JPT_RUN_LINE(message)

    def Between3Nodes(self, iNodeID, dX, dY, dZ, bImprint, crlNode, crlFace):
        message = "MeshEdit.CreateNode.Between3Nodes({},{},{},{},{},{},{})".format(iNodeID, dX, dY, dZ, bImprint, crlNode, crlFace)
        return JPT_RUN_LINE(message)

    def ProjectToPlane(self, dX, dY, dZ, crlNode, crlFace):
        message = "MeshEdit.CreateNode.ProjectToPlane({},{},{},{},{})".format(dX, dY, dZ, crlNode, crlFace)
        return JPT_RUN_LINE(message)

    def CenterOfCylinder(self, crlTagetFace, iewNodeKey):
        message = "MeshEdit.CreateNode.CenterOfCylinder({},{})".format(crlTagetFace, iewNodeKey)
        return JPT_RUN_LINE(message)

    def CenterOfSphere(self, crlTacrNodesOrFaces, iNodeID):
        message = "MeshEdit.CreateNode.CenterOfSphere({},{})".format(crlTacrNodesOrFaces, iNodeID)
        return JPT_RUN_LINE(message)

    def Offset(self, vecOffset, iRep, crlCrNodes, crCoord):
        message = "MeshEdit.CreateNode.Offset({},{},{},{})".format(vecOffset, iRep, crlCrNodes, crCoord)
        return JPT_RUN_LINE(message)

    def CenterOfGravity(self, iCreationType, iodeID, dX, dY, dZ, crlPart, crlBarPart, crlFace):
        message = "MeshEdit.CreateNode.CenterOfGravity({},{},{},{},{},{},{},{})".format(iCreationType, iodeID, dX, dY, dZ, crlPart, crlBarPart, crlFace)
        return JPT_RUN_LINE(message)

    def ProjectToLine(self, crlTa):
        message = "MeshEdit.CreateNode.ProjectToLine({})".format(crlTa)
        return JPT_RUN_LINE(message)

    def IntersectionNode(self, crlFaces,crlBodies,crlEdges,crlNodes):
        message = "MeshEdit.CreateNode.IntersectionNode({},{},{},{})".format(crlFaces,crlBodies,crlEdges,crlNodes)
        return JPT_RUN_LINE(message)

class MoveNode:
    def Point(self, dX, dY, dZ, ilNodeList):
        message = "MeshEdit.MoveNode.Point({},{},{},{})".format(dX, dY, dZ, ilNodeList)
        return JPT_RUN_LINE(message)

    def ProjectToLine(self, crlRefNodes, crlObjNodes, iType):
        message = "MeshEdit.MoveNode.ProjectToLine({},{},{})".format(crlRefNodes, crlObjNodes, iType)
        return JPT_RUN_LINE(message)

    def ProjectToPlaneElem(self, ilNodeKeys, ilElemKeys):
        message = "MeshEdit.MoveNode.ProjectToPlaneElem({},{})".format(ilNodeKeys, ilElemKeys)
        return JPT_RUN_LINE(message)

    def Equalize(self, crlEdge):
        message = "MeshEdit.MoveNode.Equalize({})".format(crlEdge)
        return JPT_RUN_LINE(message)

    def StraightenMidnodes(self, crlPart, crlFace, crlEdge, crlNode):
        message = "MeshEdit.MoveNode.StraightenMidnodes({},{},{},{})".format(crlPart, crlFace, crlEdge, crlNode)
        return JPT_RUN_LINE(message)

    def NormalOffset(self, dMagnitude, ilNodeList):
        message = "MeshEdit.MoveNode.NormalOffset({},{})".format(dMagnitude, ilNodeList)
        return JPT_RUN_LINE(message)

    def CoincidentNodes(self, crlNode, dTol, bDesOrder):
        message = "MeshEdit.MoveNode.CoincidentNodes({},{},{})".format(crlNode, dTol, bDesOrder)
        return JPT_RUN_LINE(message)

    def AlongCylinder(self, crlFace, crlNode, dIrX, dIrY, dIrZ, dCircleX, dCircleY, dCircleZ, dRadius, dHeight):
        message = "MeshEdit.MoveNode.AlongCylinder({},{},{},{},{},{},{},{},{},{})".format(crlFace, crlNode, dIrX, dIrY, dIrZ, dCircleX, dCircleY, dCircleZ, dRadius, dHeight)
        return JPT_RUN_LINE(message)

    def ProjectToPlane_3Nodes(self, ilNodeList):
        message = "MeshEdit.MoveNode.ProjectToPlane_3Nodes({})".format(ilNodeList)
        return JPT_RUN_LINE(message)

    def MoveNodeOffset(self, dDeltaX,dDeltaY,dDeltaZ,crlNode,crCoord):
        message = "MeshEdit.MoveNode.MoveNodeOffset({},{},{},{},{})".format(dDeltaX,dDeltaY,dDeltaZ,crlNode,crCoord)
        return JPT_RUN_LINE(message)

    def RefineQuality(self, iMetric, crlFace, crlElem, crlNode):
        message = "MeshEdit.MoveNode.RefineQuality({},{},{},{})".format(iMetric, crlFace, crlElem, crlNode)
        return JPT_RUN_LINE(message)

    def StraightenMidnodes(self, crlPart, crlFace, crlEdge, crlNode):
        message = "MeshEdit.MoveNode.StraightenMidnodes({},{},{},{})".format(crlPart, crlFace, crlEdge, crlNode)
        return JPT_RUN_LINE(message)

    def Offset(self, dDeltaX, dDeltaY, dDeltaZ, crCoord, crlNode):
        message = "MeshEdit.MoveNode.Offset({},{},{},{},{})".format(dDeltaX, dDeltaY, dDeltaZ, crCoord, crlNode)
        return JPT_RUN_LINE(message)

    def Laplacian(self, crlTarget, iType, bWithCADFollow):
        message = "MeshEdit.MoveNode.Laplacian({},{},{})".format(crlTarget, iType, bWithCADFollow)
        return JPT_RUN_LINE(message)

    def AlongEdge(self, crlNodes, bMoveX, bMoveY, bMoveZ, dPosX, dPosY, dPosZ, iMoveType):
        message = "MeshEdit.MoveNode.AlongEdge({},{},{},{},{},{},{},{})".format(crlNodes, bMoveX, bMoveY, bMoveZ, dPosX, dPosY, dPosZ, iMoveType)
        return JPT_RUN_LINE(message)

    def AlongDirection(self, crlNodes, crElem, crFace, vecDirection, dMagnitude, bDestination):
        message = "MeshEdit.MoveNode.AlongDirection({},{},{},{},{},{})".format(crlNodes, crElem, crFace, vecDirection, dMagnitude, bDestination)
        return JPT_RUN_LINE(message)

    def CADFollows(self, crlNodes, dMovedPosX, dMovedPosY, dMovedPosZ):
        message = "MeshEdit.MoveNode.CADFollows({},{},{},{})".format(crlNodes, dMovedPosX, dMovedPosY, dMovedPosZ)
        return JPT_RUN_LINE(message)

    def Scale(self, crlNode, crlNodeOrigin, crCoord, posDeltaXYZ):
        message = "MeshEdit.MoveNode.Scale({},{},{},{})".format(crlNode, crlNodeOrigin, crCoord, posDeltaXYZ)
        return JPT_RUN_LINE(message)

    def Absolute(self, dDeltaX, dDeltaY, dDeltaZ, b1stCoord, b2ndCoord, b3rdCoord, crlNode, crCoord):
        message = "MeshEdit.MoveNode.Absolute({},{},{},{},{},{},{},{})".format(dDeltaX, dDeltaY, dDeltaZ, b1stCoord, b2ndCoord, b3rdCoord, crlNode, crCoord)
        return JPT_RUN_LINE(message)

class CADProjection:
    def Part(self, iMethod, crCadPart, crMeshedPart, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck):
        message = "Meshing.CADProjection.Part({},{},{},{},{},{},{})".format(iMethod, crCadPart, crMeshedPart, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck)
        return JPT_RUN_LINE(message)

    def Face(self, iMethod, crCadPart, crlMeshedFace, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck):
        message = "Meshing.CADProjection.Face({},{},{},{},{},{},{})".format(iMethod, crCadPart, crlMeshedFace, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck)
        return JPT_RUN_LINE(message)

    def FaceToFace(self, iMethod, crlCadFace, crlMeshedFace, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck):
        message = "Meshing.CADProjection.FaceToFace({},{},{},{},{},{},{})".format(iMethod, crlCadFace, crlMeshedFace, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck)
        return JPT_RUN_LINE(message)

    def NodeToFace(self, iMethod, crlCadFace, crlMeshedNode, iDirection, iImproveQuality):
        message = "Meshing.CADProjection.NodeToFace({},{},{},{},{})".format(iMethod, crlCadFace, crlMeshedNode, iDirection, iImproveQuality)
        return JPT_RUN_LINE(message)

    def NodeToEdge(self, iMethod, crCadEdge, crlMeshedNode, iDirection):
        message = "Meshing.CADProjection.NodeToEdge({},{},{},{})".format(iMethod, crCadEdge, crlMeshedNode, iDirection)
        return JPT_RUN_LINE(message)

class LocalMeshing:
    def FilletMapping(self, taFaces, nIsoDiv, dIsoSize, dIsoError):
        message = "Meshing.LocalMeshing.FilletMapping({},{},{},{})".format(taFaces, nIsoDiv, dIsoSize, dIsoError)
        return JPT_RUN_LINE(message)

    def SelectFillet(self, crlItems, dSelectWidthMin, dSelectWidthMax, dSelectRMin, dSelectRMax, dAngleMin, dAngleMax, bConvex, bConcave):
        message = "Meshing.LocalMeshing.SelectFillet({},{},{},{},{},{},{},{},{})".format(crlItems, dSelectWidthMin, dSelectWidthMax, dSelectRMin, dSelectRMax, dAngleMin, dAngleMax, bConvex, bConcave)
        return JPT_RUN_LINE(message)

class LocalSetting:
    def SearchTargetFaces(self, iPartType, dlOrigin, dlLength, dlCenterPt, dlAxisPt1, dlAxisPt2, bEnclosed):
        message = "Meshing.LocalSetting.SearchTargetFaces({},{},{},{},{},{},{})".format(iPartType, dlOrigin, dlLength, dlCenterPt, dlAxisPt1, dlAxisPt2, bEnclosed)
        return JPT_RUN_LINE(message)

class Templates:
    def TemplateCopy(self, crlReferent, crlTarget, iMethod, iCopySub, dTolerance, strSource, strTarget):
        message = "Meshing.Templates.TemplateCopy({},{},{},{},{},'{}','{}')".format(crlReferent, crlTarget, iMethod, iCopySub, dTolerance, strSource, strTarget)
        return JPT_RUN_LINE(message)

class LocalRemesh:
    def Solid(self, crlParts, dlCenter, dRadius, dGradFactor, dStrechLimit):
        message = "Meshing.LocalRemesh.Solid({},{},{},{},{})".format(crlParts, dlCenter, dRadius, dGradFactor, dStrechLimit)
        return JPT_RUN_LINE(message)

    def Surfase(self, crlTarget, surfaceMesh , bUseSetting, bGrading, bFMesher, iOverrideType, bKeepConnection, bProjCAD, bTinyFaceMerge, dMinFaceWidth, dMaxFaceWidth,bIDchcek , bKeepRemeshEdge ):
        message = "Meshing.LocalRemesh.Surfase({},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlTarget, surfaceMesh , bUseSetting, bGrading, bFMesher, iOverrideType, bKeepConnection, bProjCAD, bTinyFaceMerge, dMinFaceWidth, dMaxFaceWidth,bIDchcek , bKeepRemeshEdge )
        return JPT_RUN_LINE(message)

class LocalSettings:
    def Edge(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.Edge('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

    def Face(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.Face('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

    def FaceElement(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.FaceElement('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

    def Model(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.Model('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

    def Part(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.Part('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

    def Points(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.Points('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

class Edge:
    def ProjectEdgeToFace(self, crlEdge,crlFace, bExtendEdge):
        message = "MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace({},{},{})".format(crlEdge,crlFace, bExtendEdge)
        return JPT_RUN_LINE(message)

    def FaceTwoFace(self, crRefFace, crExtFace, iExtendType):
        message = "MidPlaneEdit.AddItems.Edge.FaceTwoFace({},{},{})".format(crRefFace, crExtFace, iExtendType)
        return JPT_RUN_LINE(message)

class Face:
    def EFExtendFreeEdge(self, crlEdges,crlFaces,bMergeFace,bMergeEdge,bUseNeighDir,dMergeEdgeAngle,bMultiEF):
        message = "MidPlaneEdit.AddItems.Face.EFExtendFreeEdge({},{},{},{},{},{},{})".format(crlEdges,crlFaces,bMergeFace,bMergeEdge,bUseNeighDir,dMergeEdgeAngle,bMultiEF)
        return JPT_RUN_LINE(message)

    def EFProject(self, crlEdges,crlFaces,bMergeFace,bMergeEdge,dMergeEdgeAngle,bMultiEF):
        message = "MidPlaneEdit.AddItems.Face.EFProject({},{},{},{},{},{})".format(crlEdges,crlFaces,bMergeFace,bMergeEdge,dMergeEdgeAngle,bMultiEF)
        return JPT_RUN_LINE(message)

class Edge:
    def Nodes(self, crlNode):
        message = "MidPlaneEdit.Edge.Nodes({})".format(crlNode)
        return JPT_RUN_LINE(message)

class ExtendFace:
    def CylinderFace(self, crlExtFace, crRefFace, crEdge, iExtendType, iFaceType, iMethod, dParaAngleOffset, dParaArcLength, dParaZxy, iAxisPlane, iParaArcNodesNum, dOffLength, crlSelExtendedFace, crlSelRefFace, dCoMag, iAxisSystem, iCoorSystem, iCoX, iCoY, iCoZ, bOtherSameAsFaceNormal, dOtherArcNodesNum, dOtherArcRadius):
        message = "MidPlaneEdit.ExtendFace.CylinderFace({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlExtFace, crRefFace, crEdge, iExtendType, iFaceType, iMethod, dParaAngleOffset, dParaArcLength, dParaZxy, iAxisPlane, iParaArcNodesNum, dOffLength, crlSelExtendedFace, crlSelRefFace, dCoMag, iAxisSystem, iCoorSystem, iCoX, iCoY, iCoZ, bOtherSameAsFaceNormal, dOtherArcNodesNum, dOtherArcRadius)
        return JPT_RUN_LINE(message)

    def PlanarFace(self, bIType, crExtFace, crRefFace, crEdge, iFaceType, iExtendType, iMethod, dParaZxy, iAxisPlane, iParaArcNodesNum, dOffLength, dCoMag, iAxisSystem, iCoorSystem, crCoord, iCoX, iCoY, iCoZ, bOtherSameAsFaceNormal, dOtherArcNodesNum, dOtherArcRadius):
        message = "MidPlaneEdit.ExtendFace.PlanarFace({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(bIType, crExtFace, crRefFace, crEdge, iFaceType, iExtendType, iMethod, dParaZxy, iAxisPlane, iParaArcNodesNum, dOffLength, dCoMag, iAxisSystem, iCoorSystem, crCoord, iCoX, iCoY, iCoZ, bOtherSameAsFaceNormal, dOtherArcNodesNum, dOtherArcRadius)
        return JPT_RUN_LINE(message)

class Face:
    def FaceExtendtoFace(self, crlExtFaces,crlRefFaces,bMergeFace,bMergeEdge,dMergeEdgeAngle):
        message = "MidPlaneEdit.Face.FaceExtendtoFace({},{},{},{},{})".format(crlExtFaces,crlRefFaces,bMergeFace,bMergeEdge,dMergeEdgeAngle)
        return JPT_RUN_LINE(message)

    def FaceExtendToIntersection(self, crEdge0,crEdge1):
        message = "MidPlaneEdit.Face.FaceExtendToIntersection({},{})".format(crEdge0,crEdge1)
        return JPT_RUN_LINE(message)

    def EdgesToEdges(self, crlEdges, bImprint, bMultiEdges):
        message = "MidPlaneEdit.Face.EdgesToEdges({},{},{})".format(crlEdges, bImprint, bMultiEdges)
        return JPT_RUN_LINE(message)

class Manual:
    def vecOffset(self, crlFaces,crPart,dOffset,bCyl,strNewPartName):
        message = "MidPlaneEdit.Manual.vecOffset({},{},{},{},'{}')".format(crlFaces,crPart,dOffset,bCyl,strNewPartName)
        return JPT_RUN_LINE(message)

    def MidByPair(self, crlBaseFaces,crlPairFaces,crlRefFaces,crPart,bMergeFaces,bExtendFaces,bHideFaces,dExtendTol,dMergeEdgesAngle,dStitchFaces):
        message = "MidPlaneEdit.Manual.MidByPair({},{},{},{},{},{},{},{},{},{})".format(crlBaseFaces,crlPairFaces,crlRefFaces,crPart,bMergeFaces,bExtendFaces,bHideFaces,dExtendTol,dMergeEdgesAngle,dStitchFaces)
        return JPT_RUN_LINE(message)

class AddItems:
    Edge = Edge()

    Face = Face()

class CreateEdge:
    def PerpendicularLineToEdge(self, crNode,crEdge,crlFace,bBreakFace):
        message = "MufflerHA.CreateEdge.PerpendicularLineToEdge({},{},{},{})".format(crNode,crEdge,crlFace,bBreakFace)
        return JPT_RUN_LINE(message)

class CreateEdgeClassic:
    def ProjectLine(self, ilAiedgeidForMacro,ilAifaceidForMacro,bDivideFace,crlAiparttargetForMarco):
        message = "MufflerHA.CreateEdgeClassic.ProjectLine({},{},{},{})".format(ilAiedgeidForMacro,ilAifaceidForMacro,bDivideFace,crlAiparttargetForMarco)
        return JPT_RUN_LINE(message)

class Rod:
    def Rod(self, crlNode,dRadius,iType,dMeshSize,dStartDist,dWeldDist,iDivNumber,dDeformWidth,iTransitionElem,dlPosDir):
        message = "MufflerT.SpecialModeling.Rod.Rod({},{},{},{},{},{},{},{},{},{})".format(crlNode,dRadius,iType,dMeshSize,dStartDist,dWeldDist,iDivNumber,dDeformWidth,iTransitionElem,dlPosDir)
        return JPT_RUN_LINE(message)

class SpecialModeling:
    Rod = Rod()

class CreateWeld:
    def Auto(self, iIconnectattributeMethod,strStrconnectattributeName,crlMasterTarget,crlSlaveTarget,iIconnectattributeCoordsys,crEdit):
        message = "MuxWeld.CreateWeld.Auto({},'{}',{},{},{},{})".format(iIconnectattributeMethod,strStrconnectattributeName,crlMasterTarget,crlSlaveTarget,iIconnectattributeCoordsys,crEdit)
        return JPT_RUN_LINE(message)

class DefineSequence:
    def Single(self, crEdit):
        message = "MuxWeld.DefineSequence.Single({})".format(crEdit)
        return JPT_RUN_LINE(message)

class LocalMeshing:
    def FilletMapMeshing(self, crlPart, crlFace, dMinLength, dMaxLength, dMinRadius, dMaxRadius, bConvex, bConcave, iTmp, dLengthSingleLayer, dBMinLengthForSingleLayer, dRadiusSingleLayer, dBMinRadiusForSingleLayer, iMinlayer, bMinLayer):
        message = "OasisAWizard.LocalMeshing.FilletMapMeshing({},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, crlFace, dMinLength, dMaxLength, dMinRadius, dMaxRadius, bConvex, bConcave, iTmp, dLengthSingleLayer, dBMinLengthForSingleLayer, dRadiusSingleLayer, dBMinRadiusForSingleLayer, iMinlayer, bMinLayer)
        return JPT_RUN_LINE(message)

class ImportResults:
    def ImportOp2Mesh(self, strlFilePaths, iMportType, dFaceAngle, dEdgeAngle):
        message = "Post.ImportResults.ImportOp2Mesh('{}',{},{},{})".format(strlFilePaths, iMportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def NastranOp2PostJob(self, strName,strlPaths, crEdit):
        message = "Post.ImportResults.NastranOp2PostJob('{}','{}',{})".format(strName,strlPaths, crEdit)
        return JPT_RUN_LINE(message)

    def ImportTsdbMesh(self, strTsdbFilePath,strBtxFilePath, iMportType, dFaceAngle, dEdgeAngle):
        message = "Post.ImportResults.ImportTsdbMesh('{}','{}',{},{},{})".format(strTsdbFilePath,strBtxFilePath, iMportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def HDF5Mesh(self, strlFilePaths, iMportType, dFaceAngle, dEdgeAngle):
        message = "Post.ImportResults.HDF5Mesh('{}',{},{},{})".format(strlFilePaths, iMportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def ADVC(self, strlPath, iMportType, dFaceAngle, dEdgeAngle):
        message = "Post.ImportResults.ADVC('{}',{},{},{})".format(strlPath, iMportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def ADVC2PostJob(self, strName,strlResultFolderPaths,crEdit):
        message = "Post.ImportResults.ADVC2PostJob('{}','{}',{})".format(strName,strlResultFolderPaths,crEdit)
        return JPT_RUN_LINE(message)

    def NastranHDF5(self, strName, strlPaths, crEdit):
        message = "Post.ImportResults.NastranHDF5('{}','{}',{})".format(strName, strlPaths, crEdit)
        return JPT_RUN_LINE(message)

class ElemRelatedInfo:
    def Shell(self, listErishellThetaProp, listErishellCsProp, listErishellZoffsProp):
        message = "Properties.ElemRelatedInfo.Shell({},{},{})".format(listErishellThetaProp, listErishellCsProp, listErishellZoffsProp)
        return JPT_RUN_LINE(message)

    def Conn(self, listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds):
        message = "Properties.ElemRelatedInfo.Conn({},{},{},{},{},{},{})".format(listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds)
        return JPT_RUN_LINE(message)

    def Rod(self, listEnds):
        message = "Properties.ElemRelatedInfo.Rod({})".format(listEnds)
        return JPT_RUN_LINE(message)

    def Beam(self, listEnds, listOrientVecs, listOrientNodeIds, listOffsetVecsA, listOffsetVecsB, listAs, listBs, listWarps):
        message = "Properties.ElemRelatedInfo.Beam({},{},{},{},{},{},{},{})".format(listEnds, listOrientVecs, listOrientNodeIds, listOffsetVecsA, listOffsetVecsB, listAs, listBs, listWarps)
        return JPT_RUN_LINE(message)

    def Bar(self, listEnds, listOrientVecs, listOrientNodeIds, listOffsetVecsA, listOffsetVecsB, listAs, listBs, listWarps):
        message = "Properties.ElemRelatedInfo.Bar({},{},{},{},{},{},{},{})".format(listEnds, listOrientVecs, listOrientNodeIds, listOffsetVecsA, listOffsetVecsB, listAs, listBs, listWarps)
        return JPT_RUN_LINE(message)

    def Gap(self, listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds):
        message = "Properties.ElemRelatedInfo.Gap({},{},{},{},{},{},{})".format(listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds)
        return JPT_RUN_LINE(message)

    def Bush(self, listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds):
        message = "Properties.ElemRelatedInfo.Bush({},{},{},{},{},{},{})".format(listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds)
        return JPT_RUN_LINE(message)

class Section:
    def Import(self, strImportPath):
        message = "Properties.Section.Import('{}')".format(strImportPath)
        return JPT_RUN_LINE(message)

    def ModifyGeneral(self, strName, crSection, iSecType, iGeneralType, dA, dB, dH, dT1, dT2, dT3, bTapered, dDaTap, dDbTap, dDhTap, dDt1Tap, dDt2Tap, dDt3Tap):
        message = "Properties.Section.ModifyGeneral('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, crSection, iSecType, iGeneralType, dA, dB, dH, dT1, dT2, dT3, bTapered, dDaTap, dDbTap, dDhTap, dDt1Tap, dDt2Tap, dDt3Tap)
        return JPT_RUN_LINE(message)

    def ModifyLibrary(self, strName, crSection, iType, iLibType, dDimSize0, dDimSize1, dDimSize2, dDimSize3, dDimSize4, dDimSize5, dDimSize6, dDimSize7, dDimSize8, dDimSize9, dDimSize10, dDimSize11):
        message = "Properties.Section.ModifyLibrary('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, crSection, iType, iLibType, dDimSize0, dDimSize1, dDimSize2, dDimSize3, dDimSize4, dDimSize5, dDimSize6, dDimSize7, dDimSize8, dDimSize9, dDimSize10, dDimSize11)
        return JPT_RUN_LINE(message)

    def ModifySketcher(self, strName, crSection, iType):
        message = "Properties.Section.ModifySketcher('{}',{},{})".format(strName, crSection, iType)
        return JPT_RUN_LINE(message)

    def Export(self, strExportSavePath):
        message = "Properties.Section.Export('{}')".format(strExportSavePath)
        return JPT_RUN_LINE(message)

    def Delete(self, crlSection):
        message = "Properties.Section.Delete({})".format(crlSection)
        return JPT_RUN_LINE(message)

    def AddGeneral(self, strName, iSecType, iSecGenType, dDsecGensizeA, dDsecGensizeB, dDsecGensizeH, dDsecGensizeT1, dDsecGensizeT2, dDsecGensizeT3, bBsecTapered, dDsecGensizeATap, dDsecGensizeBTap, dDsecGensizeHTap, dDsecGensizeT1Tap, dDsecGensizeT2Tap, dDsecGensizeT3Tap):
        message = "Properties.Section.AddGeneral('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iSecType, iSecGenType, dDsecGensizeA, dDsecGensizeB, dDsecGensizeH, dDsecGensizeT1, dDsecGensizeT2, dDsecGensizeT3, bBsecTapered, dDsecGensizeATap, dDsecGensizeBTap, dDsecGensizeHTap, dDsecGensizeT1Tap, dDsecGensizeT2Tap, dDsecGensizeT3Tap)
        return JPT_RUN_LINE(message)

    def AddLibrary(self, strName, iSecType, iLibType, dDim1, dDim2, dDim3, dDim4, dDim5, dDim6, dDim7, dDim8, dDim9, dDim10, dDim11, dDim12):
        message = "Properties.Section.AddLibrary('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iSecType, iLibType, dDim1, dDim2, dDim3, dDim4, dDim5, dDim6, dDim7, dDim8, dDim9, dDim10, dDim11, dDim12)
        return JPT_RUN_LINE(message)

    def AddSketcher(self, strName, iSecType):
        message = "Properties.Section.AddSketcher('{}',{})".format(strName, iSecType)
        return JPT_RUN_LINE(message)

class DropTest:
    def CalcTimestep(self, dRelevantElemRate,dChangeMassRage):
        message = "SNOnePush.DropTest.CalcTimestep({},{})".format(dRelevantElemRate,dChangeMassRage)
        return JPT_RUN_LINE(message)

    def UpdateFloor(self, strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat):
        message = "SNOnePush.DropTest.UpdateFloor('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

    def DropRotation(self, strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat):
        message = "SNOnePush.DropTest.DropRotation('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

    def DropRotation(self, strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat):
        message = "SNOnePush.DropTest.DropRotation('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

class Assembly:
    def CreateWeld(self, crlWelds,dMeshSize,iRrate,dFilletRadius):
        message = "SZOnepushReliability.Assembly.CreateWeld({},{},{},{})".format(crlWelds,dMeshSize,iRrate,dFilletRadius)
        return JPT_RUN_LINE(message)

    def ContactSurface(self, crlSrcFace,crlTarPart,dTolerance,iLayer):
        message = "SZOnepushReliability.Assembly.ContactSurface({},{},{},{})".format(crlSrcFace,crlTarPart,dTolerance,iLayer)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def FilletMapping(self, crlPart,crlFace,dMinRadius,dMaxRadius,dMinAngle,dMaxAngle,bConvex,bConcave):
        message = "SZOnepushReliability.MeshEdit.FilletMapping({},{},{},{},{},{},{},{})".format(crlPart,crlFace,dMinRadius,dMaxRadius,dMinAngle,dMaxAngle,bConvex,bConcave)
        return JPT_RUN_LINE(message)

class Connection:
    def RRod(self, rbarConnection, iUlDOFs, dTol, crlMasterTarget, crlSlaveTarget):
        message = "Test.Connection.RRod({},{},{},{},{})".format(rbarConnection, iUlDOFs, dTol, crlMasterTarget, crlSlaveTarget)
        return JPT_RUN_LINE(message)

class Muffler:
    def ProjectLineForWeld(self, crlEdge,crlFace):
        message = "Test.Muffler.ProjectLineForWeld({},{})".format(crlEdge,crlFace)
        return JPT_RUN_LINE(message)

class ZGeometryTest:
    def IntersectionCheck(self, crlPart,crlFace,crlElem,iType):
        message = "Test.ZGeometryTest.IntersectionCheck({},{},{},{})".format(crlPart,crlFace,crlElem,iType)
        return JPT_RUN_LINE(message)

    def ShellAssy(self, taPart, taFace, _iMeshType, _bSelfIntersection, _iMethod, _dGapTol):
        message = "Test.ZGeometryTest.ShellAssy({},{},{},{},{},{})".format(taPart, taFace, _iMeshType, _bSelfIntersection, _iMethod, _dGapTol)
        return JPT_RUN_LINE(message)

class Angle:
    def ProjectedNode(self, crNode, strTarget, iPrecision):
        message = "Tool.Measure.Angle.ProjectedNode({},'{}',{})".format(crNode, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoNodesAxis(self, crNode1,crNode2,dlAxis,strTarget,iPrecision):
        message = "Tool.Measure.Angle.TwoNodesAxis({},{},{},'{}',{})".format(crNode1,crNode2,dlAxis,strTarget,iPrecision)
        return JPT_RUN_LINE(message)

    def By2Axis(self, xyz1, xyz2, target, Precision):
        message = "Tool.Measure.Angle.By2Axis({},{},{},{})".format(xyz1, xyz2, target, Precision)
        return JPT_RUN_LINE(message)

class Distance:
    def Edge(self, crEdge, option, iPrecision):
        message = "Tool.Measure.Distance.Edge({},{},{})".format(crEdge, option, iPrecision)
        return JPT_RUN_LINE(message)

    def EdgeNode(self, crPoint,crEdge, option, iPrecision):
        message = "Tool.Measure.Distance.EdgeNode({},{},{},{})".format(crPoint,crEdge, option, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoPoints(self, posPoint1, posPoint2, iPrecision):
        message = "Tool.Measure.Distance.TwoPoints({},{},{})".format(posPoint1, posPoint2, iPrecision)
        return JPT_RUN_LINE(message)

    def LineNode(self, crlTargetNode, iPrecision):
        message = "Tool.Measure.Distance.LineNode({},{})".format(crlTargetNode, iPrecision)
        return JPT_RUN_LINE(message)

    def Plane3NodesToNode(self, crNode, crNode1, crNode2, crNode3, iPrecision):
        message = "Tool.Measure.Distance.Plane3NodesToNode({},{},{},{},{})".format(crNode, crNode1, crNode2, crNode3, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoEdges(self, crEdge1,crEdge2,iOptions,iPrecision):
        message = "Tool.Measure.Distance.TwoEdges({},{},{},{})".format(crEdge1,crEdge2,iOptions,iPrecision)
        return JPT_RUN_LINE(message)

    def PlaneElemToNode(self, crNode, crElem, iPrecision):
        message = "Tool.Measure.Distance.PlaneElemToNode({},{},{})".format(crNode, crElem, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoNodes(self, crNode1,crNode2,iPrecision):
        message = "Tool.Measure.Distance.TwoNodes({},{},{})".format(crNode1,crNode2,iPrecision)
        return JPT_RUN_LINE(message)

    def FaceNode(self, crlFace,crlNode,iPrecision):
        message = "Tool.Measure.Distance.FaceNode({},{},{})".format(crlFace,crlNode,iPrecision)
        return JPT_RUN_LINE(message)

class Mass:
    def ByMaterial(self, crlPart,strDensity,strTarget,iPrecision):
        message = "Tool.Measure.Mass.ByMaterial({},'{}','{}',{})".format(crlPart,strDensity,strTarget,iPrecision)
        return JPT_RUN_LINE(message)

class Radius:
    def ByThreeNodes(self, crNode1_3,crNode2_3,crNode3_3,iPrecision):
        message = "Tool.Measure.Radius.ByThreeNodes({},{},{},{})".format(crNode1_3,crNode2_3,crNode3_3,iPrecision)
        return JPT_RUN_LINE(message)

    def MeasureRadiusBy3Nodes(self, crNode1_3,crNode2_3,crNode3_3,iPrecision):
        message = "Tool.Measure.Radius.MeasureRadiusBy3Nodes({},{},{},{})".format(crNode1_3,crNode2_3,crNode3_3,iPrecision)
        return JPT_RUN_LINE(message)

class Manual:
    def CleanTetCollapse(self, crlElem,iKeep,iCheckCondition,dLimitValue,iCleanupMode):
        message = "Tool.MeshQuality.Manual.CleanTetCollapse({},{},{},{},{})".format(crlElem,iKeep,iCheckCondition,dLimitValue,iCleanupMode)
        return JPT_RUN_LINE(message)

    def CleaningVolumeMesh(self, crlPart,crlElem,dLimitVolume,iMode):
        message = "Tool.MeshQuality.Manual.CleaningVolumeMesh({},{},{},{})".format(crlPart,crlElem,dLimitVolume,iMode)
        return JPT_RUN_LINE(message)

class Connections:
    def Contact(self, strName, iContactType, dInterferenceClosure, dFrictionCoefficient, iShellOffset, iMasterShellOrientation, iSlaveShellOrientation, iMarkerColor, bInitialAdjustment, crlMaster, crlSlave, crMasterGroup, crSlaveGroup, crEdit):
        message = "Tool.Connections.Contact('{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactType, dInterferenceClosure, dFrictionCoefficient, iShellOffset, iMasterShellOrientation, iSlaveShellOrientation, iMarkerColor, bInitialAdjustment, crlMaster, crlSlave, crMasterGroup, crSlaveGroup, crEdit)
        return JPT_RUN_LINE(message)

    def Spring(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Tool.Connections.Spring({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def RBE3(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly):
        message = "Tool.Connections.RBE3({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly)
        return JPT_RUN_LINE(message)

    def Mass(self, strName, crlTargetNodes, dMass, iDof, crEdit):
        message = "Tool.Connections.Mass('{}',{},{},{},{})".format(strName, crlTargetNodes, dMass, iDof, crEdit)
        return JPT_RUN_LINE(message)

class Coordinates:
    def CylinderFace(self, strName, iCoordType, crFace):
        message = "Tool.Coordinates.CylinderFace('{}',{},{})".format(strName, iCoordType, crFace)
        return JPT_RUN_LINE(message)

    def ThreeNode(self, strName, iCoordType, iOrder, crlNodes, veclPoints, crRefCoord, crEdit):
        message = "Tool.Coordinates.ThreeNode('{}',{},{},{},{},{},{})".format(strName, iCoordType, iOrder, crlNodes, veclPoints, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def Align(self, strName, iCoordType, iCoordAxis, bCreateNew, crlNodes, crEdge, crEdit):
        message = "Tool.Coordinates.Align('{}',{},{},{},{},{},{})".format(strName, iCoordType, iCoordAxis, bCreateNew, crlNodes, crEdge, crEdit)
        return JPT_RUN_LINE(message)

    def vecOffset(self, strName, iCoordType, vTranslate, bCreateNew, crRefCoord, crEdit):
        message = "Tool.Coordinates.vecOffset('{}',{},{},{},{},{})".format(strName, iCoordType, vTranslate, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def Rotate(self, strName, iCoordType, vecRotate, bCreateNew, crRefCoord, crEdit):
        message = "Tool.Coordinates.Rotate('{}',{},{},{},{},{})".format(strName, iCoordType, vecRotate, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def AttachCircle(self, strName, iCoordType, crEdge, bCreateNew, crRefCoord, crEdit):
        message = "Tool.Coordinates.AttachCircle('{}',{},{},{},{},{})".format(strName, iCoordType, crEdge, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def AttachNode(self, strName, iCoordType, crNode, bCreateNew, crRefCoord, crEdit):
        message = "Tool.Coordinates.AttachNode('{}',{},{},{},{},{})".format(strName, iCoordType, crNode, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

    def Face(self, strName, iCoordType, iOrder, veclPoint, crlNodes, crItem, crRefCoord, crEdit):
        message = "Tool.Coordinates.Face('{}',{},{},{},{},{},{},{})".format(strName, iCoordType, iOrder, veclPoint, crlNodes, crItem, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

class Group:
    def DeleteGroupEntity(self, crlDelGroup):
        message = "Tool.Group.DeleteGroupEntity({})".format(crlDelGroup)
        return JPT_RUN_LINE(message)

class ImprintEdges:
    def Line(self, veclAvPoint, bDivideFace, crlPartTarget):
        message = "Tool.ImprintEdges.Line({},{},{})".format(veclAvPoint, bDivideFace, crlPartTarget)
        return JPT_RUN_LINE(message)

    def ClosedLine(self, veclPositions,crlCrTargetFace,iBBreakFace):
        message = "Tool.ImprintEdges.ClosedLine({},{},{})".format(veclPositions,crlCrTargetFace,iBBreakFace)
        return JPT_RUN_LINE(message)

    def ClosedLine2(self, poslPointPos,bDivide, crlPartTarges):
        message = "Tool.ImprintEdges.ClosedLine2({},{},{})".format(poslPointPos,bDivide, crlPartTarges)
        return JPT_RUN_LINE(message)

class Measure:
    Angle = Angle()

    Distance = Distance()

    Mass = Mass()

    Radius = Radius()

    def Volume(self, crlParts, iPrecision):
        message = "Tool.Measure.Volume({},{})".format(crlParts, iPrecision)
        return JPT_RUN_LINE(message)

class MeshQuality:
    Manual = Manual()

class Angle:
    def TwoNodesAxis(self, crNode1,crNode2, dlAxis, strTarget, iPrecision):
        message = "Tools.Measure.Angle.TwoNodesAxis({},{},{},'{}',{})".format(crNode1,crNode2, dlAxis, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def ThreeNodes(self, crNode1,crNode2,crNode3, strTarget, iPrecision):
        message = "Tools.Measure.Angle.ThreeNodes({},{},{},'{}',{})".format(crNode1,crNode2,crNode3, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def ProjectedNode(self, crNode, strTarget, iPrecision):
        message = "Tools.Measure.Angle.ProjectedNode({},'{}',{})".format(crNode, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoElemEdges(self, crpElemEdge1,crpElemEdge2, strTarget, iPrecision):
        message = "Tools.Measure.Angle.TwoElemEdges({},{},'{}',{})".format(crpElemEdge1,crpElemEdge2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def ThreeNodes(self, crNode1,crNode2,crNode3, strTarget, iPrecision):
        message = "Tools.Measure.Angle.ThreeNodes({},{},{},'{}',{})".format(crNode1,crNode2,crNode3, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoAxis(self, dlXyz1, dlXyz2, strTarget, iPrecision):
        message = "Tools.Measure.Angle.TwoAxis({},{},'{}',{})".format(dlXyz1, dlXyz2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoEdges(self, crEdge1,crEdge2, strTarget, iPrecision):
        message = "Tools.Measure.Angle.TwoEdges({},{},'{}',{})".format(crEdge1,crEdge2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Area:
    def Element(self, taElem , iPrecision ):
        message = "Tools.Measure.Area.Element({},{})".format(taElem , iPrecision )
        return JPT_RUN_LINE(message)

    def Face(self, taFace , iPrecision ):
        message = "Tools.Measure.Area.Face({},{})".format(taFace , iPrecision )
        return JPT_RUN_LINE(message)

    def Body(self, taBody , iPrecision ):
        message = "Tools.Measure.Area.Body({},{})".format(taBody , iPrecision )
        return JPT_RUN_LINE(message)

class Distance:
    def TwoEdges(self, crEdge1,crEdge2, iPrecision):
        message = "Tools.Measure.Distance.TwoEdges({},{},{})".format(crEdge1,crEdge2, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoNodes(self, crNode1, crNode2, strTarget, iPrecision, crCoordinateSystem):
        message = "Tools.Measure.Distance.TwoNodes({},{},'{}',{},{})".format(crNode1, crNode2, strTarget, iPrecision, crCoordinateSystem)
        return JPT_RUN_LINE(message)

    def FaceNode(self, crlFace,crlNode, iPrecision):
        message = "Tools.Measure.Distance.FaceNode({},{},{})".format(crlFace,crlNode, iPrecision)
        return JPT_RUN_LINE(message)

    def Edge(self, crEdge, iPrecision):
        message = "Tools.Measure.Distance.Edge({},{})".format(crEdge, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoPoints(self, posPoint1, posPoint2, strTarget, iPrecision, crCoordinateSystem):
        message = "Tools.Measure.Distance.TwoPoints({},{},'{}',{},{})".format(posPoint1, posPoint2, strTarget, iPrecision, crCoordinateSystem)
        return JPT_RUN_LINE(message)

    def EdgeNode(self, crEdge,crNode, iPrecision):
        message = "Tools.Measure.Distance.EdgeNode({},{},{})".format(crEdge,crNode, iPrecision)
        return JPT_RUN_LINE(message)

    def LineNode(self, crlTargetNode, iPrecision):
        message = "Tools.Measure.Distance.LineNode({},{})".format(crlTargetNode, iPrecision)
        return JPT_RUN_LINE(message)

    def PlaneElemToNode(self, crNode, crElem, iPrecision):
        message = "Tools.Measure.Distance.PlaneElemToNode({},{},{})".format(crNode, crElem, iPrecision)
        return JPT_RUN_LINE(message)

    def Plane3NodesToNode(self, crNode1,crNode2,crNode3,crNode, iPrecision):
        message = "Tools.Measure.Distance.Plane3NodesToNode({},{},{},{},{})".format(crNode1,crNode2,crNode3,crNode, iPrecision)
        return JPT_RUN_LINE(message)

class Mass:
    def Property(self, crlPart,crlCondition, strTarget, bGravityCenter, iPrecision):
        message = "Tools.Measure.Mass.Property({},{},'{}',{},{})".format(crlPart,crlCondition, strTarget, bGravityCenter, iPrecision)
        return JPT_RUN_LINE(message)

    def Material(self, crlPart,crlCondition,strDensity, strTarget, bGravityCenter, iPrecision):
        message = "Tools.Measure.Mass.Material({},{},'{}','{}',{},{})".format(crlPart,crlCondition,strDensity, strTarget, bGravityCenter, iPrecision)
        return JPT_RUN_LINE(message)

class Radius:
    def Edge(self, crEdge, iPrecision):
        message = "Tools.Measure.Radius.Edge({},{})".format(crEdge, iPrecision)
        return JPT_RUN_LINE(message)

    def ThreeNodes(self, crCrnode13,crCrnode23,crCrnode33, iPrecision):
        message = "Tools.Measure.Radius.ThreeNodes({},{},{},{})".format(crCrnode13,crCrnode23,crCrnode33, iPrecision)
        return JPT_RUN_LINE(message)

class BySelection:
    def SelectionOrder(self, crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending):
        message = "Tools.BySelection.SelectionOrder({},{},{},{},{},{})".format(crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending)
        return JPT_RUN_LINE(message)

    def Position(self, crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending1, bAscending2, bAscending3, iSortFirst, iSortSecond, iSortThird, iBSortFirst, iBSortSecond, iBSortThird, iOffset1, iOffset2, iOffset3, dTol1, dTol2, dTol3, crCoord, bSpecialFace):
        message = "Tools.BySelection.Position({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending1, bAscending2, bAscending3, iSortFirst, iSortSecond, iSortThird, iBSortFirst, iBSortSecond, iBSortThird, iOffset1, iOffset2, iOffset3, dTol1, dTol2, dTol3, crCoord, bSpecialFace)
        return JPT_RUN_LINE(message)

    def OriginalID(self, crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending):
        message = "Tools.BySelection.OriginalID({},{},{},{},{},{})".format(crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending)
        return JPT_RUN_LINE(message)

class Group:
    def DeleteGroupEntity(self, crlDelGroup):
        message = "Tools.Group.DeleteGroupEntity({})".format(crlDelGroup)
        return JPT_RUN_LINE(message)

    def CreateGroup(self, strGroupName, crlTargets, crEdit):
        message = "Tools.Group.CreateGroup('{}',{},{})".format(strGroupName, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

class TotalLoad:
    def LBC(self, crlTarget, crCoordinate, strOutput, iPrecision):
        message = "Tools.TotalLoad.LBC({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

    def Model(self, crlTarget, crCoordinate, strOutput, iPrecision):
        message = "Tools.TotalLoad.Model({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

    def Node(self, crlTarget, crCoordinate, strOutput, iPrecision):
        message = "Tools.TotalLoad.Node({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

    def Part(self, crlTarget, crCoordinate, strOutput, iPrecision):
        message = "Tools.TotalLoad.Part({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

    def Face(self, crlTarget, crCoordinate, strOutput, iPrecision):
        message = "Tools.TotalLoad.Face({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Angle = Angle()

    Area = Area()

    Distance = Distance()

    Mass = Mass()

    Radius = Radius()

    def Volume(self, crlParts, iPrecision):
        message = "Tools.Measure.Volume({},{})".format(crlParts, iPrecision)
        return JPT_RUN_LINE(message)

class ACModelCreationTools:
    def MeshedFace(self, crlItem1, crlItem2, crlItem3, crlPart, iType, dMeshSise, bMergeTol, dTol, bCreatePart):
        message = "MMCCarACTools.ACModelCreationTools.MeshedFace({},{},{},{},{},{},{},{},{})".format(crlItem1, crlItem2, crlItem3, crlPart, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
        return JPT_RUN_LINE(message)

class ClearanceElement:
    def Connect(self, crlFaces, crlElems, iConnectionMethod):
        message = "MMCCarACTools.ClearanceElement.Connect({},{},{})".format(crlFaces, crlElems, iConnectionMethod)
        return JPT_RUN_LINE(message)

    def Edit(self, dDx, dDy, dDz, dLx, dLy, dLz, crlTarget, crlDestNode, poslDestPoint):
        message = "MMCCarACTools.ClearanceElement.Edit({},{},{},{},{},{},{},{},{})".format(dDx, dDy, dDz, dLx, dLy, dLz, crlTarget, crlDestNode, poslDestPoint)
        return JPT_RUN_LINE(message)

class LBC:
    def TemperatureLoad(self, strName, iDnType, dFTemp, strDstrFilePathName, crDcrTable, crlTarget, crEdit, bDbUseAsMaterialReferenceTemp):
        message = "Designer.LBC.TemperatureLoad('{}',{},{},'{}',{},{},{},{})".format(strName, iDnType, dFTemp, strDstrFilePathName, crDcrTable, crlTarget, crEdit, bDbUseAsMaterialReferenceTemp)
        return JPT_RUN_LINE(message)

class Load:
    def Moment(self, strName, crlFaces, dlVecMomentXYZ, crCoord, crEdit):
        message = "Designer.Load.Moment('{}',{},{},{},{})".format(strName, crlFaces, dlVecMomentXYZ, crCoord, crEdit)
        return JPT_RUN_LINE(message)

class Export:
    def STL(strFile, crlPart, dScale, bFilterIndex):
        message = "Export.STL('{}',{},{},{})".format(strFile, crlPart, dScale, bFilterIndex)
        return JPT_RUN_LINE(message)

class FileMenu:
    def AddJTDB(strFileName, strMethod, strTargetModel, strOption, iInputNode, iInputElem, iInputPart, iInputMaterial, iInputProperty):
        message = "FileMenu.AddJTDB('{}','{}','{}','{}',{},{},{},{},{})".format(strFileName, strMethod, strTargetModel, strOption, iInputNode, iInputElem, iInputPart, iInputMaterial, iInputProperty)
        return JPT_RUN_LINE(message)

    def Save(strPath, strHistoryTree):
        message = "FileMenu.Save('{}','{}')".format(strPath, strHistoryTree)
        return JPT_RUN_LINE(message)

    def LoadDB(strPath, bUseTmpTable):
        message = "FileMenu.LoadDB('{}',{})".format(strPath, bUseTmpTable)
        return JPT_RUN_LINE(message)

class HGTMufflerModeling:
    def CreateBeadWeld(crlEdge,crlPrjtedEdge,crlPart,dTol,dRatio,crRefElem):
        message = "HGTMufflerModeling.CreateBeadWeld({},{},{},{},{},{})".format(crlEdge,crlPrjtedEdge,crlPart,dTol,dRatio,crRefElem)
        return JPT_RUN_LINE(message)

class ImportCAD:
    def Spatial(strlPath, param, bIsNXDirect, bSetFaceColor, strCsvFilePath):
        message = "ImportCAD.Spatial('{}',{},{},{},'{}')".format(strlPath, param, bIsNXDirect, bSetFaceColor, strCsvFilePath)
        return JPT_RUN_LINE(message)

    def TechnoStarGeometry(strlPath, bUseUnit):
        message = "ImportCAD.TechnoStarGeometry('{}',{})".format(strlPath, bUseUnit)
        return JPT_RUN_LINE(message)

    def CreoDirect(vecPath, param):
        message = "ImportCAD.CreoDirect({},{})".format(vecPath, param)
        return JPT_RUN_LINE(message)

    def Elysium(strlPath, param, bFaceColor):
        message = "ImportCAD.Elysium('{}',{},{})".format(strlPath, param, bFaceColor)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def NastranBdf(strlFilePaths, iMportType, dFaceAngle, dEdgeAngle, bReadNameComment, iCreateDup1DElemAnswer):
        message = "ImportMesh.NastranBdf('{}',{},{},{},{},{})".format(strlFilePaths, iMportType, dFaceAngle, dEdgeAngle, bReadNameComment, iCreateDup1DElemAnswer)
        return JPT_RUN_LINE(message)

    def AbaqusINP(strlFilePaths, dFaceAngle, dEdgeAngle, iMportType):
        message = "ImportMesh.AbaqusINP('{}',{},{},{})".format(strlFilePaths, dFaceAngle, dEdgeAngle, iMportType)
        return JPT_RUN_LINE(message)

    def LSDYNA(strlPath, dFaceAngle, dEdgeAngle):
        message = "ImportMesh.LSDYNA('{}',{},{})".format(strlPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def ADVCADX(strPath, dFaceAngle, dEdgeAngle):
        message = "ImportMesh.ADVCADX('{}',{},{})".format(strPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def Universal(strPath):
        message = "ImportMesh.Universal('{}')".format(strPath)
        return JPT_RUN_LINE(message)

    def AnsysDat(strlPath, dFaceAngle, dEdgeAngle):
        message = "ImportMesh.AnsysDat('{}',{},{})".format(strlPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

    def TSVPre(strImportPath, strExportPath, ilModelIndex, iMerge):
        message = "ImportMesh.TSVPre('{}','{}',{},{})".format(strImportPath, strExportPath, ilModelIndex, iMerge)
        return JPT_RUN_LINE(message)

class Utility:
    def FindEntities(strTarget, strTargetType, bFindMatch):
        message = "Utility.FindEntities('{}','{}',{})".format(strTarget, strTargetType, bFindMatch)
        return JPT_RUN_LINE(message)

    def MeasureDistanceBy2Edges(crEdgeFirst,crEdgeLast, iPrecision):
        message = "Utility.MeasureDistanceBy2Edges({},{},{})".format(crEdgeFirst,crEdgeLast, iPrecision)
        return JPT_RUN_LINE(message)

class ACModeling:
    ACBoundary = ACBoundary()

    Create = Create()

    def CloseHoleAuto(crlClosedHoleParts):
        message = "ACModeling.CloseHoleAuto({})".format(crlClosedHoleParts)
        return JPT_RUN_LINE(message)

    def Cut(crlPart):
        message = "ACModeling.Cut({})".format(crlPart)
        return JPT_RUN_LINE(message)

class Analysis:
    AbaqusStep = AbaqusStep()

    ACTRAN = ACTRAN()

    Ansys = Ansys()

    Nastran = Nastran()

    Permas = Permas()

    TSSolver = TSSolver()

    TSSS = TSSS()

    def Abaqus(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat):
        message = "Analysis.Abaqus('{}',{},{},{},{},{},{},'{}',{},{},'{}',{},{},{},{},{},{})".format(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat)
        return JPT_RUN_LINE(message)

    def ExportAnsys(strName, crAnsysJob):
        message = "Analysis.ExportAnsys('{}',{})".format(strName, crAnsysJob)
        return JPT_RUN_LINE(message)

    def ExportAbaqus(crAbaJob, crlSelectPart, strInpPath):
        message = "Analysis.ExportAbaqus({},{},'{}')".format(crAbaJob, crlSelectPart, strInpPath)
        return JPT_RUN_LINE(message)

    def ModifyLbcToStep(listabaqusLbcStepInfo):
        message = "Analysis.ModifyLbcToStep({})".format(listabaqusLbcStepInfo)
        return JPT_RUN_LINE(message)

    def ExportAdx(crJob, strPath, iNumType, iUiWidth, iUiPrecision):
        message = "Analysis.ExportAdx({},'{}',{},{},{})".format(crJob, strPath, iNumType, iUiWidth, iUiPrecision)
        return JPT_RUN_LINE(message)

    def ExportLsdyna(strPath, crJob):
        message = "Analysis.ExportLsdyna('{}',{})".format(strPath, crJob)
        return JPT_RUN_LINE(message)

    def NastranJob(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit):
        message = "Analysis.NastranJob('{}','{}',{},'{}',{},{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit)
        return JPT_RUN_LINE(message)

    def LSDYNAJob(crEdit):
        message = "Analysis.LSDYNAJob({})".format(crEdit)
        return JPT_RUN_LINE(message)

    ADVC = ADVC()

class Assemble:
    SeparateFaces = SeparateFaces()

    def Boolean(crlPart, iBooleanType, dToleranceAlignment, bLeaveOriginalBodies):
        message = "Assemble.Boolean({},{},{},{})".format(crlPart, iBooleanType, dToleranceAlignment, bLeaveOriginalBodies)
        return JPT_RUN_LINE(message)

    def AssembleFace(crlPart,crlFace,dTolerance,iFitEdge,iMeshSetting):
        message = "Assemble.AssembleFace({},{},{},{},{})".format(crlPart,crlFace,dTolerance,iFitEdge,iMeshSetting)
        return JPT_RUN_LINE(message)

    def FullLayer(crPart, dLayerWidth, iLayer, bUsePyramid):
        message = "Assemble.FullLayer({},{},{},{})".format(crPart, dLayerWidth, iLayer, bUsePyramid)
        return JPT_RUN_LINE(message)

    def CylinderLayer(crFace, crNode):
        message = "Assemble.CylinderLayer({},{})".format(crFace, crNode)
        return JPT_RUN_LINE(message)

    def SharedFace():
        message = "Assemble.SharedFace({})".format()
        return JPT_RUN_LINE(message)

    def AssembleFaces(ilPairFaceToMakeShareFace, dTolerance, iTypeConnectPos, bUseSnapInput, dSnapTolerance, bFitEdge):
        message = "Assemble.AssembleFaces({},{},{},{},{},{})".format(ilPairFaceToMakeShareFace, dTolerance, iTypeConnectPos, bUseSnapInput, dSnapTolerance, bFitEdge)
        return JPT_RUN_LINE(message)

    def GeneralLayer(crlTacrfacesForMacro, dWidth, iLayer, bSeparatePart, bForceStitchToSide, bSmoothingEdge, bNoImprint, bWidthOnSurface, bMakeHexa):
        message = "Assemble.GeneralLayer({},{},{},{},{},{},{},{},{})".format(crlTacrfacesForMacro, dWidth, iLayer, bSeparatePart, bForceStitchToSide, bSmoothingEdge, bNoImprint, bWidthOnSurface, bMakeHexa)
        return JPT_RUN_LINE(message)

    def AddRib(crPart, crlFaces, veclPoints, dWidth, dDepth):
        message = "Assemble.AddRib({},{},{},{},{})".format(crPart, crlFaces, veclPoints, dWidth, dDepth)
        return JPT_RUN_LINE(message)

    def FindMatingFace(crlMasterFaces, crlSlaveFaces, crlPart, dTolerance):
        message = "Assemble.FindMatingFace({},{},{},{})".format(crlMasterFaces, crlSlaveFaces, crlPart, dTolerance)
        return JPT_RUN_LINE(message)

    def AddBoss(crPart, iType, bMerge, posOrgCenter, vecOrgDirection, crCoord, iAxis, dAngle, bHollow, dInnerRadius, dOrgOuterRadius, dTaperAngle, iNodeOnCircle, iNodeOnAxis, dOriginalHeight):
        message = "Assemble.AddBoss({},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crPart, iType, bMerge, posOrgCenter, vecOrgDirection, crCoord, iAxis, dAngle, bHollow, dInnerRadius, dOrgOuterRadius, dTaperAngle, iNodeOnCircle, iNodeOnAxis, dOriginalHeight)
        return JPT_RUN_LINE(message)

class Assembly:
    RightClick = RightClick()

class BoundaryConditions:
    BoundaryTemperature = BoundaryTemperature()

    Convection = Convection()

    EnforcedLoads = EnforcedLoads()

    HeatFlux = HeatFlux()

    InitialElementalValue = InitialElementalValue()

    InitialTemperature = InitialTemperature()

    LBCCopy = LBCCopy()

    Pressure = Pressure()

    Submodel = Submodel()

    TemperatureLoads = TemperatureLoads()

    def LoadCase(strName, dFactor, crlTatarget, iExportId, dlTargetFactor, crEdit):
        message = "BoundaryConditions.LoadCase('{}',{},{},{},{},{})".format(strName, dFactor, crlTatarget, iExportId, dlTargetFactor, crEdit)
        return JPT_RUN_LINE(message)

    def InsideHeatGeneration(strName, dInsideFlux, crTable, crlTargets, crEdit):
        message = "BoundaryConditions.InsideHeatGeneration('{}',{},{},{},{})".format(strName, dInsideFlux, crTable, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

    def LBCCopyMisc(iMethod, iMatchMethod, dlTransVec, dTransMag, dTransOffset, dTransTol, crTranscrCoord, dlTransaxisVec, dlTranscenterVec, dRotateAngle, dRotateTol, crRotatecrCoord, veclMirrorPoint, dMirrordOffset, dMirrorTol, crlTarget):
        message = "BoundaryConditions.LBCCopyMisc({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, dlTransVec, dTransMag, dTransOffset, dTransTol, crTranscrCoord, dlTransaxisVec, dlTranscenterVec, dRotateAngle, dRotateTol, crRotatecrCoord, veclMirrorPoint, dMirrordOffset, dMirrorTol, crlTarget)
        return JPT_RUN_LINE(message)

    def LbcContactConvert(iConvertTo,iTieConvType,crlTarget):
        message = "BoundaryConditions.LbcContactConvert({},{},{})".format(iConvertTo,iTieConvType,crlTarget)
        return JPT_RUN_LINE(message)

    def FieldData(strName, iType, ilSheet, crEdit, bAbaqusAmp, iAmpType):
        message = "BoundaryConditions.FieldData('{}',{},{},{},{},{})".format(strName, iType, ilSheet, crEdit, bAbaqusAmp, iAmpType)
        return JPT_RUN_LINE(message)

    def FixedConstraint(strName, iDwDof, crCurCoord, iType, iUsetType, crTable, bAbaqusFixed, crlTarget, crEdit):
        message = "BoundaryConditions.FixedConstraint('{}',{},{},{},{},{},{},{},{})".format(strName, iDwDof, crCurCoord, iType, iUsetType, crTable, bAbaqusFixed, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def DofSet(strName, iDwDof, crCurCoord, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.DofSet('{}',{},{},{},{},{})".format(strName, iDwDof, crCurCoord, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    BodyLoads = BodyLoads()

    Force = Force()

    InitialNodalValue = InitialNodalValue()

class Connections:
    Pretension = Pretension()

    def MassElements(strName,crlTarget, dMass, iDof, bDesigner, crCoordinate, dOffset0, dOffset1, dOffset2, dInertia0, dInertia1, dInertia2, dInertia3, dInertia4, dInertia5, crEdit, bUpdateDispCS):
        message = "Connections.MassElements('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName,crlTarget, dMass, iDof, bDesigner, crCoordinate, dOffset0, dOffset1, dOffset2, dInertia0, dInertia1, dInertia2, dInertia3, dInertia4, dInertia5, crEdit, bUpdateDispCS)
        return JPT_RUN_LINE(message)

    def BarBeam(strName, iEType, iMethod, crProp, dlOrient, crlMasterTarget, crlSlaveTarget):
        message = "Connections.BarBeam('{}',{},{},{},{},{},{})".format(strName, iEType, iMethod, crProp, dlOrient, crlMasterTarget, crlSlaveTarget)
        return JPT_RUN_LINE(message)

    def GapsDetail(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur):
        message = "Connections.GapsDetail({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

    def Plot(strName, iPID, crlTarget, crEdit):
        message = "Connections.Plot('{}',{},{},{})".format(strName, iPID, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def CreateConnConm(strName,iEType,iMethod,iCoordSys,iConmId,crMatCoord,dMass, dlX, dlVintertia0, dlVintertia1):
        message = "Connections.CreateConnConm('{}',{},{},{},{},{},{},{},{},{})".format(strName,iEType,iMethod,iCoordSys,iConmId,crMatCoord,dMass, dlX, dlVintertia0, dlVintertia1)
        return JPT_RUN_LINE(message)

    def RBE3(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly):
        message = "Connections.RBE3({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly)
        return JPT_RUN_LINE(message)

    def RigidWall(strName, iObject, iType, iMotion, iFriction, iOrtho, iForces, dFinite1, dFinite2, dMotionMass, dMotionInitVelo, dFricCoulombCoeff, dFricWeldVelo, iForcesCirclesNum, dOrthoStaticCoeff1, dOrthoStaticCoeff2, dOrthoDynamicCoeff1, dOrthoDynamicCoeff2, dOrthoDecayConst1, dOrthoDecayConst2, dOrthoFricVector1, dOrthoFricVector2, dOrthoFricVector3, bAllNodeSlave, crCoord, crAreaFaceSet, crVisualNodeSet, crlTarget, crEdit):
        message = "Connections.RigidWall('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iObject, iType, iMotion, iFriction, iOrtho, iForces, dFinite1, dFinite2, dMotionMass, dMotionInitVelo, dFricCoulombCoeff, dFricWeldVelo, iForcesCirclesNum, dOrthoStaticCoeff1, dOrthoStaticCoeff2, dOrthoDynamicCoeff1, dOrthoDynamicCoeff2, dOrthoDecayConst1, dOrthoDecayConst2, dOrthoFricVector1, dOrthoFricVector2, dOrthoFricVector3, bAllNodeSlave, crCoord, crAreaFaceSet, crVisualNodeSet, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Connector(strName, iMethod, iConnectType, iRefNode, iElemCs, crLocalCS, crlElasticity, crlDamp, crlMasterTarget, crlSlaveTarget, crEdit):
        message = "Connections.Connector('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, iMethod, iConnectType, iRefNode, iElemCs, crLocalCS, crlElasticity, crlDamp, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

    def BoltMeshingSplitOnly(strName, iPartcutparamImethod, dPartcutparamDoffset, iPartcutparamBshareface, iPartcutparamBseparateface, iPartcutparamBsplitonly, iPartcutparamBmakesectionface, crPartcutparamCoord, surfaceMesh, bLBCPRETENSIONABAQUSDATABfixedlenght, crLBCPRETENSIONABAQUSDATACrtable, dLBCPRETENSIONABAQUSDATADvalue, iLBCPRETENSIONABAQUSDATAIlocalunit, strLBCPRETENSIONABAQUSDATAStrnormal, posLBCPRETENSIONABAQUSDATATvctrolnodepos, crlTarget, poslCutter):
        message = "Connections.BoltMeshingSplitOnly('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iPartcutparamImethod, dPartcutparamDoffset, iPartcutparamBshareface, iPartcutparamBseparateface, iPartcutparamBsplitonly, iPartcutparamBmakesectionface, crPartcutparamCoord, surfaceMesh, bLBCPRETENSIONABAQUSDATABfixedlenght, crLBCPRETENSIONABAQUSDATACrtable, dLBCPRETENSIONABAQUSDATADvalue, iLBCPRETENSIONABAQUSDATAIlocalunit, strLBCPRETENSIONABAQUSDATAStrnormal, posLBCPRETENSIONABAQUSDATATvctrolnodepos, crlTarget, poslCutter)
        return JPT_RUN_LINE(message)

    def BoltMeshingNotSplitOnly(strName, iPartcutparamImethod, dPartcutparamDoffset, iPartcutparamBshareface, iPartcutparamBseparateface, iPartcutparamBsplitonly, iPartcutparamBmakesectionface, crPartcutparamCoord, surfaceMesh, iLBCPRETENSIONDATAIdir, dLBCPRETENSIONDATADvalue, bLBCPRETENSIONDATABfixlength, crLBCPRETENSIONDATACrtable, crLBCPRETENSIONDATACrcoord, iLBCPRETENSIONDATAIlocalunit, crlTarget, poslCutter):
        message = "Connections.BoltMeshingNotSplitOnly('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPartcutparamImethod, dPartcutparamDoffset, iPartcutparamBshareface, iPartcutparamBseparateface, iPartcutparamBsplitonly, iPartcutparamBmakesectionface, crPartcutparamCoord, surfaceMesh, iLBCPRETENSIONDATAIdir, dLBCPRETENSIONDATADvalue, bLBCPRETENSIONDATABfixlength, crLBCPRETENSIONDATACrtable, crLBCPRETENSIONDATACrcoord, iLBCPRETENSIONDATAIlocalunit, crlTarget, poslCutter)
        return JPT_RUN_LINE(message)

    BoltConnections = BoltConnections()

    Contacts = Contacts()

    Gaps = Gaps()

    MPC = MPC()

    RigidElements = RigidElements()

    SpringsDampers = SpringsDampers()

class EngReliability:
    def SubModelBC(strName,crlTarget,iPos,iViewCp,iCp,iSrcType,iMappedCpIndexArr0,dScaleR,vecOffset,vecRotate,dScaleT,strPath,crEdit,iMappingMethod,iSubmodelBCMappingType,iMappingFromStepNo,bSetADVCFile,strADVCResultFile,bSetDetATol,dDetATol,bSetElementSet,strElementSet):
        message = "EngReliability.SubModelBC('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName,crlTarget,iPos,iViewCp,iCp,iSrcType,iMappedCpIndexArr0,dScaleR,vecOffset,vecRotate,dScaleT,strPath,crEdit,iMappingMethod,iSubmodelBCMappingType,iMappingFromStepNo,bSetADVCFile,strADVCResultFile,bSetDetATol,dDetATol,bSetElementSet,strElementSet)
        return JPT_RUN_LINE(message)

class ExManifoldModeling:
    SZ = SZ()

class Geometry:
    Bar = Bar()

    BodyCut = BodyCut()

    BreakEntity = BreakEntity()

    DeleteEntity = DeleteEntity()

    Edge = Edge()

    Face = Face()

    FindFeature = FindFeature()

    MergeEntities = MergeEntities()

    Part = Part()

    ShowAdjacent = ShowAdjacent()

    Transform = Transform()

    def CADTrim(crlListFace,crlListPart, dTrimSize, dTrimAngle):
        message = "Geometry.CADTrim({},{},{},{})".format(crlListFace,crlListPart, dTrimSize, dTrimAngle)
        return JPT_RUN_LINE(message)

    def StitchEdge(dTolerance, bKeepSlave, crlMaster, crlSlave):
        message = "Geometry.StitchEdge({},{},{},{})".format(dTolerance, bKeepSlave, crlMaster, crlSlave)
        return JPT_RUN_LINE(message)

    def LogoRemoval(crlStartFaces, crlStopFaces, iLayers, bMergeFaces):
        message = "Geometry.LogoRemoval({},{},{},{})".format(crlStartFaces, crlStopFaces, iLayers, bMergeFaces)
        return JPT_RUN_LINE(message)

    def ShellAsm(crlPartK, crlFaceK, dTol, iElemType, bSkipTiny):
        message = "Geometry.ShellAsm({},{},{},{},{})".format(crlPartK, crlFaceK, dTol, iElemType, bSkipTiny)
        return JPT_RUN_LINE(message)

    def SquareUpFillet(crlFaces):
        message = "Geometry.SquareUpFillet({})".format(crlFaces)
        return JPT_RUN_LINE(message)

    def MakeFillet(crlEdges, dRadius):
        message = "Geometry.MakeFillet({},{})".format(crlEdges, dRadius)
        return JPT_RUN_LINE(message)

    def MakeFacePlanar(dlPlanePt1, dlPlanePt2, dlPlanePt3, ilFaceIds, iMergeFace):
        message = "Geometry.MakeFacePlanar({},{},{},{},{})".format(dlPlanePt1, dlPlanePt2, dlPlanePt3, ilFaceIds, iMergeFace)
        return JPT_RUN_LINE(message)

    def FCircleAdjustVertex(crlPart):
        message = "Geometry.FCircleAdjustVertex({})".format(crlPart)
        return JPT_RUN_LINE(message)

    def AdjustHalfCylinder(poslPoint, crlFace, crCoord, nAxisPlane, bDivideFace, crlPartTarget, bMergeEdge):
        message = "Geometry.AdjustHalfCylinder({},{},{},{},{},{},{})".format(poslPoint, crlFace, crCoord, nAxisPlane, bDivideFace, crlPartTarget, bMergeEdge)
        return JPT_RUN_LINE(message)

    def FCircVertexAdjust(crlPart, dMinRadius, bFullCylinder, bCylinderMorethan90, bSkipFaceHaveLocalSetting):
        message = "Geometry.FCircVertexAdjust({},{},{},{},{})".format(crlPart, dMinRadius, bFullCylinder, bCylinderMorethan90, bSkipFaceHaveLocalSetting)
        return JPT_RUN_LINE(message)

    def ExtractSurfaces(crlFace, dAngle, strName, bMergePart):
        message = "Geometry.ExtractSurfaces({},{},'{}',{})".format(crlFace, dAngle, strName, bMergePart)
        return JPT_RUN_LINE(message)

    def RemoveRibBoss(crlFace, dGradiation, iContinuity):
        message = "Geometry.RemoveRibBoss({},{},{})".format(crlFace, dGradiation, iContinuity)
        return JPT_RUN_LINE(message)

    def AdvancedShellAssembly(crlPart, crlFace, iMeshType, bSelfIntersection, iMethod, dGapTol):
        message = "Geometry.AdvancedShellAssembly({},{},{},{},{},{})".format(crlPart, crlFace, iMeshType, bSelfIntersection, iMethod, dGapTol)
        return JPT_RUN_LINE(message)

class Groups:
    RightClick = RightClick()

class HexModeling:
    def SolidElemInterface(crlFaces, bFlip, crlElms):
        message = "HexModeling.SolidElemInterface({},{},{})".format(crlFaces, bFlip, crlElms)
        return JPT_RUN_LINE(message)

    def BallHexa(crPart, vecCenter, dRadius, dMeshSize, iType, iLayer, bMakeCenterNode, strPartName):
        message = "HexModeling.BallHexa({},{},{},{},{},{},{},'{}')".format(crPart, vecCenter, dRadius, dMeshSize, iType, iLayer, bMakeCenterNode, strPartName)
        return JPT_RUN_LINE(message)

    def BoxMesh(ilPartIds,dMeshSize,strMaterialName):
        message = "HexModeling.BoxMesh({},{},'{}')".format(ilPartIds,dMeshSize,strMaterialName)
        return JPT_RUN_LINE(message)

    def AutoSweep(crl, dMeshSize, bLayers, iLayers):
        message = "HexModeling.AutoSweep({},{},{},{})".format(crl, dMeshSize, bLayers, iLayers)
        return JPT_RUN_LINE(message)

    def Circular(crlFace, dAngle, dTol, iLayer, vecAxisPt, vecAxisVect, bInterfaceElem, bExtrusion, dTranslationExtrusion, dBDeleteOriginalParts):
        message = "HexModeling.Circular({},{},{},{},{},{},{},{},{},{})".format(crlFace, dAngle, dTol, iLayer, vecAxisPt, vecAxisVect, bInterfaceElem, bExtrusion, dTranslationExtrusion, dBDeleteOriginalParts)
        return JPT_RUN_LINE(message)

    def FaceToFace(crSrcFace,crDstFace, bDeleteOriginalParts):
        message = "HexModeling.FaceToFace({},{},{})".format(crSrcFace,crDstFace, bDeleteOriginalParts)
        return JPT_RUN_LINE(message)

    def Layer(crlFace, dFrontWidth, dBackWidth, iFrontLayers, iBackLayers, iBaseFaceType, iSeparate):
        message = "HexModeling.Layer({},{},{},{},{},{},{})".format(crlFace, dFrontWidth, dBackWidth, iFrontLayers, iBackLayers, iBaseFaceType, iSeparate)
        return JPT_RUN_LINE(message)

    def Linear(crlFace, dLength, nLayer, vecSweepDirection, bInterfaceElemFlag, nLinearMethod, bDeleteOriginalParts, bDeleteTargetParts, nMethodBias, dFactor, nProgression):
        message = "HexModeling.Linear({},{},{},{},{},{},{},{},{},{},{})".format(crlFace, dLength, nLayer, vecSweepDirection, bInterfaceElemFlag, nLinearMethod, bDeleteOriginalParts, bDeleteTargetParts, nMethodBias, dFactor, nProgression)
        return JPT_RUN_LINE(message)

    def FromMidPlane(crlPart, bRef):
        message = "HexModeling.FromMidPlane({},{})".format(crlPart, bRef)
        return JPT_RUN_LINE(message)

    def Curve(crFace, crlVcrEdges, crlVcrRefEdges, dMeshSize):
        message = "HexModeling.Curve({},{},{},{})".format(crFace, crlVcrEdges, crlVcrRefEdges, dMeshSize)
        return JPT_RUN_LINE(message)

class Home:
    ImportCAD = ImportCAD()

    ImportMesh = ImportMesh()

    def Export(strFileName, crlBodies, bBigID, bUseUnit, bVert, bEdge, bFace, bSolid):
        message = "Home.Export('{}',{},{},{},{},{},{},{})".format(strFileName, crlBodies, bBigID, bUseUnit, bVert, bEdge, bFace, bSolid)
        return JPT_RUN_LINE(message)

    def ToImage(strImgPath, bWhiteBG, bTransparentBG, bFixedSize, iExportWidth, iExportHeight):
        message = "Home.ToImage('{}',{},{},{},{},{})".format(strImgPath, bWhiteBG, bTransparentBG, bFixedSize, iExportWidth, iExportHeight)
        return JPT_RUN_LINE(message)

    def Find(strSearch, strSeletedType, bFindMatch):
        message = "Home.Find('{}','{}',{})".format(strSearch, strSeletedType, bFindMatch)
        return JPT_RUN_LINE(message)

    def RectangularCapture(iLeft, iTop, iRight, iBottom):
        message = "Home.RectangularCapture({},{},{},{})".format(iLeft, iTop, iRight, iBottom)
        return JPT_RUN_LINE(message)

    def CopyToClipboard(bWhiteBG, bTransparentBG, bFixedSize, iWidth, iHeight):
        message = "Home.CopyToClipboard({},{},{},{},{})".format(bWhiteBG, bTransparentBG, bFixedSize, iWidth, iHeight)
        return JPT_RUN_LINE(message)

    def FullScreen():
        message = "Home.FullScreen({})".format()
        return JPT_RUN_LINE(message)

    def Synchronize():
        message = "Home.Synchronize({})".format()
        return JPT_RUN_LINE(message)

class MainWindow:
    RightClick = RightClick()

class MeshCleanup:
    Element = Element()

    def Face(crlFace, crlPart, bCreateNewPart):
        message = "MeshCleanup.Face({},{},{})".format(crlFace, crlPart, bCreateNewPart)
        return JPT_RUN_LINE(message)

    def CorrectModel(crlVcrParts, iBBreakEdge, dEdgeAngle, iBMergeEdge, dMergeEdgeAngle, iBMergePlanarFace, iBRemoveExtraVertex):
        message = "MeshCleanup.CorrectModel({},{},{},{},{},{},{})".format(crlVcrParts, iBBreakEdge, dEdgeAngle, iBMergeEdge, dMergeEdgeAngle, iBMergePlanarFace, iBRemoveExtraVertex)
        return JPT_RUN_LINE(message)

    def CloseHoles(crlEdge, dAreaMin, dAreaMax, bMergeFace, bMergeEdge):
        message = "MeshCleanup.CloseHoles({},{},{},{},{})".format(crlEdge, dAreaMin, dAreaMax, bMergeFace, bMergeEdge)
        return JPT_RUN_LINE(message)

    def CloseGap(crlPartCur, dDistanceTol):
        message = "MeshCleanup.CloseGap({},{})".format(crlPartCur, dDistanceTol)
        return JPT_RUN_LINE(message)

    def AutoCheck(crlPart,iElemType,blTaCheckCondition,blTaElemQuality,dlTaLimitValue,crlElem):
        message = "MeshCleanup.AutoCheck({},{},{},{},{},{})".format(crlPart,iElemType,blTaCheckCondition,blTaElemQuality,dlTaLimitValue,crlElem)
        return JPT_RUN_LINE(message)

    def ManualCheck(crlPart, iElemType, iVeQuality, iCheckCondition, dLimitValue, dCFLValue, iNonManifold, iCleanupMode, crlElem):
        message = "MeshCleanup.ManualCheck({},{},{},{},{},{},{},{},{})".format(crlPart, iElemType, iVeQuality, iCheckCondition, dLimitValue, dCFLValue, iNonManifold, iCleanupMode, crlElem)
        return JPT_RUN_LINE(message)

    ChangeTopology = ChangeTopology()

    Cleanup = Cleanup()

    Manual2D = Manual2D()

    Manual3D = Manual3D()

class MeshEdit:
    CreateElement = CreateElement()

    CreateNode = CreateNode()

    MoveNode = MoveNode()

    def Face(crlFaceTarget,crlFaceFixed, iOffsetType, crCoord, dlOffset, dOffset, iDistType, dDistStrong, dDistWeak, iNodeIdPick, dlPickForMacro):
        message = "MeshEdit.Face({},{},{},{},{},{},{},{},{},{},{})".format(crlFaceTarget,crlFaceFixed, iOffsetType, crCoord, dlOffset, dOffset, iDistType, dDistStrong, dDistWeak, iNodeIdPick, dlPickForMacro)
        return JPT_RUN_LINE(message)

    def ElementConvert(crlPart, iType):
        message = "MeshEdit.ElementConvert({},{})".format(crlPart, iType)
        return JPT_RUN_LINE(message)

    def Deform(crlFaceSrcObverse, crlFaceDstReverse, crlFaceSrcReverse, crlFaceDstObverse, crlFaceFixed, dDistEffect):
        message = "MeshEdit.Deform({},{},{},{},{},{})".format(crlFaceSrcObverse, crlFaceDstReverse, crlFaceSrcReverse, crlFaceDstObverse, crlFaceFixed, dDistEffect)
        return JPT_RUN_LINE(message)

    def MirrorCopy(crlFaces):
        message = "MeshEdit.MirrorCopy({})".format(crlFaces)
        return JPT_RUN_LINE(message)

    def DeleteNode(crlNodes, bRemoveVertex):
        message = "MeshEdit.DeleteNode({},{})".format(crlNodes, bRemoveVertex)
        return JPT_RUN_LINE(message)

    def FaceImprint(crlCrFaces, bMeshCopy):
        message = "MeshEdit.FaceImprint({},{})".format(crlCrFaces, bMeshCopy)
        return JPT_RUN_LINE(message)

    def AdjustOrientation(crlPart, crlFace, crlElem):
        message = "MeshEdit.AdjustOrientation({},{},{})".format(crlPart, crlFace, crlElem)
        return JPT_RUN_LINE(message)

    def OneNode(crlNodes, crlFaceFixed, bOffsetvector, crCoord, dlOffset, dOffset, iDisttype, dDiststrong, dDistweak):
        message = "MeshEdit.OneNode({},{},{},{},{},{},{},'{}',{})".format(crlNodes, crlFaceFixed, bOffsetvector, crCoord, dlOffset, dOffset, iDisttype, dDiststrong, dDistweak)
        return JPT_RUN_LINE(message)

    def SeparateNodes(crlShareNodes, crlTargets, iKeepNodeIDsOn):
        message = "MeshEdit.SeparateNodes({},{},{})".format(crlShareNodes, crlTargets, iKeepNodeIDsOn)
        return JPT_RUN_LINE(message)

    def RefineQuality(iMetric,crlFace,crlElem,crlNode):
        message = "MeshEdit.RefineQuality({},{},{},{})".format(iMetric,crlFace,crlElem,crlNode)
        return JPT_RUN_LINE(message)

    def Import(iSolverType, strFilePath, iStep, dScale):
        message = "MeshEdit.Import({},'{}',{},{})".format(iSolverType, strFilePath, iStep, dScale)
        return JPT_RUN_LINE(message)

    def RemoveSolidMesh(crlPart, bConvFirst):
        message = "MeshEdit.RemoveSolidMesh({},{})".format(crlPart, bConvFirst)
        return JPT_RUN_LINE(message)

    def MergeNodes(dTolerance, iKeepType, crlTarget, bGroup, bEquivalence):
        message = "MeshEdit.MergeNodes({},{},{},{},{})".format(dTolerance, iKeepType, crlTarget, bGroup, bEquivalence)
        return JPT_RUN_LINE(message)

    def MeshCopy(crlFace, crlNode):
        message = "MeshEdit.MeshCopy({},{})".format(crlFace, crlNode)
        return JPT_RUN_LINE(message)

    def RibThickness(crlFaceMove, crlFaceFixed, dMove, dDistStrong, dDistWeak):
        message = "MeshEdit.RibThickness({},{},{},{},{})".format(crlFaceMove, crlFaceFixed, dMove, dDistStrong, dDistWeak)
        return JPT_RUN_LINE(message)

    def ChangePattern(crlFace, iPatternType):
        message = "MeshEdit.ChangePattern({},{})".format(crlFace, iPatternType)
        return JPT_RUN_LINE(message)

    def SurfaceMesh(crlPart, iType):
        message = "MeshEdit.SurfaceMesh({},{})".format(crlPart, iType)
        return JPT_RUN_LINE(message)

    def SolidMesh(crlPart, iType):
        message = "MeshEdit.SolidMesh({},{})".format(crlPart, iType)
        return JPT_RUN_LINE(message)

class Meshing:
    CADProjection = CADProjection()

    LocalMeshing = LocalMeshing()

    LocalSetting = LocalSetting()

    Templates = Templates()

    def BarMeshing(ilVcrCadEdge,ilVcrBarEdge,ilVcrBarPart, dDocMeshSize, iDocNumofElem):
        message = "Meshing.BarMeshing({},{},{},{},{})".format(ilVcrCadEdge,ilVcrBarEdge,ilVcrBarPart, dDocMeshSize, iDocNumofElem)
        return JPT_RUN_LINE(message)

    def SolidMeshing(crlPart, bTet10, dGradingFactor, bGravCenter, dStretchLimit, iSpeedVsQual, iSpeedVsMem, iRegion, bInternalNodes, bSafeMode, iParallel, bSurfaceNodes, bEdgeNodes, bPreservation, bInternalMeshOnly, bMeshColor, iPartColor):
        message = "Meshing.SolidMeshing({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, bTet10, dGradingFactor, bGravCenter, dStretchLimit, iSpeedVsQual, iSpeedVsMem, iRegion, bInternalNodes, bSafeMode, iParallel, bSurfaceNodes, bEdgeNodes, bPreservation, bInternalMeshOnly, bMeshColor, iPartColor)
        return JPT_RUN_LINE(message)

    def SurfaceMeshing(crlPart, surfaceMesh, bUseSetting, bFMesher, iThreadNum, bRefData, bMeshColor, iPartColor):
        message = "Meshing.SurfaceMeshing({},{},{},{},{},{},{},{})".format(crlPart, surfaceMesh, bUseSetting, bFMesher, iThreadNum, bRefData, bMeshColor, iPartColor)
        return JPT_RUN_LINE(message)

    def SetAttib(crlPart , surfaceMesh ):
        message = "Meshing.SetAttib({},{})".format(crlPart , surfaceMesh )
        return JPT_RUN_LINE(message)

    LocalRemesh = LocalRemesh()

    LocalSettings = LocalSettings()

class MidPlane:
    def AdjustThickness(crlCrPart, dRatio, bAdjustFaceThick, bAdjustPropThick):
        message = "MidPlane.AdjustThickness({},{},{},{})".format(crlCrPart, dRatio, bAdjustFaceThick, bAdjustPropThick)
        return JPT_RUN_LINE(message)

    def FaceCross(crlCrBodies, crlCrFaces):
        message = "MidPlane.FaceCross({},{})".format(crlCrBodies, crlCrFaces)
        return JPT_RUN_LINE(message)

    def CreateThickProps(crlPart, dThickDiff, dMaxThick, dMinThick, crMatMembrane, crMatBend, crMatShear, crMatCoupl, iMatOrientType, dMatOrientX, dMatOrientY, dMatOrientZ, crCoor, dThickness, dBendStiff, dThickRatio, dNSM, dFiberDist1, dFiberDist2, dPlateOff, iNumInterPts, bThickSetting, iEntityType, bDivideProp, crlRefPart):
        message = "MidPlane.CreateThickProps({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, dThickDiff, dMaxThick, dMinThick, crMatMembrane, crMatBend, crMatShear, crMatCoupl, iMatOrientType, dMatOrientX, dMatOrientY, dMatOrientZ, crCoor, dThickness, dBendStiff, dThickRatio, dNSM, dFiberDist1, dFiberDist2, dPlateOff, iNumInterPts, bThickSetting, iEntityType, bDivideProp, crlRefPart)
        return JPT_RUN_LINE(message)

    def FindMidPlane():
        message = "MidPlane.FindMidPlane({})".format()
        return JPT_RUN_LINE(message)

class MidPlaneEdit:
    Edge = Edge()

    ExtendFace = ExtendFace()

    Face = Face()

    Manual = Manual()

    AddItems = AddItems()

class MufflerHA:
    CreateEdge = CreateEdge()

    CreateEdgeClassic = CreateEdgeClassic()

    def CopyMeshCount(crlMasterEdge,crlSlaveEdge,strBaseName):
        message = "MufflerHA.CopyMeshCount({},{},'{}')".format(crlMasterEdge,crlSlaveEdge,strBaseName)
        return JPT_RUN_LINE(message)

class MufflerT:
    SpecialModeling = SpecialModeling()

class MuxWeld:
    CreateWeld = CreateWeld()

    DefineSequence = DefineSequence()

    def MeshingPass(crPart,dlTaEdge,dMeshSize):
        message = "MuxWeld.MeshingPass({},{},{})".format(crPart,dlTaEdge,dMeshSize)
        return JPT_RUN_LINE(message)

    def Prop3DWeldBead(strName, crMaterial, crlTarget, crEdit):
        message = "MuxWeld.Prop3DWeldBead('{}',{},{},{})".format(strName, crMaterial, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class NSModeling:
    def NSModeling_Close_Hole(iType,dMaxLength,bMergeFaces,bSetCenterPoint,crlNodes,crlPart):
        message = "NSModeling.NSModeling_Close_Hole({},{},{},{},{},{})".format(iType,dMaxLength,bMergeFaces,bSetCenterPoint,crlNodes,crlPart)
        return JPT_RUN_LINE(message)

class OasisAWizard:
    LocalMeshing = LocalMeshing()

class Post:
    ImportResults = ImportResults()

class Properties:
    ElemRelatedInfo = ElemRelatedInfo()

    Section = Section()

    def Cohesive(strName,crMaterial,iResponse,bSpecifyThick,dInitialThick,crlTarget, crEdit, iFLG, iId, iSolverType, iADVCResponseType, iADVCStackDir, iBADVCThickness, dADVCThickness):
        message = "Properties.Cohesive('{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName,crMaterial,iResponse,bSpecifyThick,dInitialThick,crlTarget, crEdit, iFLG, iId, iSolverType, iADVCResponseType, iADVCStackDir, iBADVCThickness, dADVCThickness)
        return JPT_RUN_LINE(message)

    def Gasket(strName,crMaterial,dThickX,dThickY,dThickZ,crlTarget, crEdit, iStData, iFLG):
        message = "Properties.Gasket('{}',{},{},{},{},{},{},{},{})".format(strName,crMaterial,dThickX,dThickY,dThickZ,crlTarget, crEdit, iStData, iFLG)
        return JPT_RUN_LINE(message)

    def Shell(strName, iPID, crMatMembrane, crMatBend, crMatShear, crMatCoupl, dMatOrient1, dMatOrient2, dMatOrient3, dThickness, dBendStiff, dThickRatio, dNSM, dFiberDist1, dFiberDist2, dPlateOff, iItgPts, iMatOrientType, crLocalCS, crlTarget, crEdit, iDuplicateOpt):
        message = "Properties.Shell('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPID, crMatMembrane, crMatBend, crMatShear, crMatCoupl, dMatOrient1, dMatOrient2, dMatOrient3, dThickness, dBendStiff, dThickRatio, dNSM, dFiberDist1, dFiberDist2, dPlateOff, iItgPts, iMatOrientType, crLocalCS, crlTarget, crEdit, iDuplicateOpt)
        return JPT_RUN_LINE(message)

    def PropertyTable(listItems):
        message = "Properties.PropertyTable({})".format(listItems)
        return JPT_RUN_LINE(message)

    def Beam(strNewName, iPId, crSection, iShapeDataType, crMat, dArea, dlVecOrient, dlVecInertia, dTorConst, dNSM, dNSMA, dNSMB, dNSMNode1, dNSMNode2, dNSMNode3, dNSMNode4, dShearStiffnessK1, dShearStiffnessK2, dShearAreaReliefS1, dShearAreaReliefS2, dWrapCoeff1, dWrapCoeff2, dNA1, dNA2, dNA3, dNA4, dStressRecoveryCoeffCy, dStressRecoveryCoeffCz, dStressRecoveryCoeffDy, dStressRecoveryCoeffDz, dStressRecoveryCoeffEy, dStressRecoveryCoeffEz, dStressRecoveryCoeffFy, dStressRecoveryCoeffFz, bPinA1, bPinA2, bPinA3, bPinA4, bPinA5, bPinA6, bPinB1, bPinB2, bPinB3, bPinB4, bPinB5, bPinB6, dlOffsetA, dlOffsetB, iLengthUnit, iMassUnit, crlTarget, crEdit, bTapped, dTapArea, dlVecTapInertia, dTapTorConst, dTapNSM, dTapStressRecoveryCoeffCy, dTapStressRecoveryCoeffCz, dTapStressRecoveryCoeffDy, dTapStressRecoveryCoeffDz, dTapStressRecoveryCoeffEy, dTapStressRecoveryCoeffEz, dTapStressRecoveryCoeffFy, dTapStressRecoveryCoeffFz, iIntePtNum):
        message = "Properties.Beam('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strNewName, iPId, crSection, iShapeDataType, crMat, dArea, dlVecOrient, dlVecInertia, dTorConst, dNSM, dNSMA, dNSMB, dNSMNode1, dNSMNode2, dNSMNode3, dNSMNode4, dShearStiffnessK1, dShearStiffnessK2, dShearAreaReliefS1, dShearAreaReliefS2, dWrapCoeff1, dWrapCoeff2, dNA1, dNA2, dNA3, dNA4, dStressRecoveryCoeffCy, dStressRecoveryCoeffCz, dStressRecoveryCoeffDy, dStressRecoveryCoeffDz, dStressRecoveryCoeffEy, dStressRecoveryCoeffEz, dStressRecoveryCoeffFy, dStressRecoveryCoeffFz, bPinA1, bPinA2, bPinA3, bPinA4, bPinA5, bPinA6, bPinB1, bPinB2, bPinB3, bPinB4, bPinB5, bPinB6, dlOffsetA, dlOffsetB, iLengthUnit, iMassUnit, crlTarget, crEdit, bTapped, dTapArea, dlVecTapInertia, dTapTorConst, dTapNSM, dTapStressRecoveryCoeffCy, dTapStressRecoveryCoeffCz, dTapStressRecoveryCoeffDy, dTapStressRecoveryCoeffDz, dTapStressRecoveryCoeffEy, dTapStressRecoveryCoeffEz, dTapStressRecoveryCoeffFy, dTapStressRecoveryCoeffFz, iIntePtNum)
        return JPT_RUN_LINE(message)

    def Rod(strName, iId, crSection, crMat, dArea, dTorConst, dTorStressCoeff, dNSM, iLocalLengthUnit, iLocalMassUnit, crlTarget, crEdit):
        message = "Properties.Rod('{}',{},{},{},{},{},{},{},{},{},{},{})".format(strName, iId, crSection, crMat, dArea, dTorConst, dTorStressCoeff, dNSM, iLocalLengthUnit, iLocalMassUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Property1DBeamSimple(strName,iId, crSection, crMat, vecOrient, crlTarget, crEdit):
        message = "Properties.Property1DBeamSimple('{}',{},{},{},{},{},{})".format(strName,iId, crSection, crMat, vecOrient, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Solid(strName, iPID, crMaterial, iCordM, iIN, iOutLoc, iISOP, iFLflag, iModifiedElem, iModifiedElemADVC, bHasDynaRemesh, dDynaRemeshVal1, dDynaRemeshVal2, iAbaqusPropHGtype, dDispHG, crlTarget, crEdit, iFLG):
        message = "Properties.Solid('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPID, crMaterial, iCordM, iIN, iOutLoc, iISOP, iFLflag, iModifiedElem, iModifiedElemADVC, bHasDynaRemesh, dDynaRemeshVal1, dDynaRemeshVal2, iAbaqusPropHGtype, dDispHG, crlTarget, crEdit, iFLG)
        return JPT_RUN_LINE(message)

    def Section1D(strName, iSecType, iSecGentype, dSecGensizeA, dSecGensizeB, dSecGensizeH, dSecGensizeT1, dSecGensizeT2, dSecGensizeT3, bSecTapered, dSecGensizeATap, dSecGensizeBTap, dSecGensizeHTap, dSecGensizeT1Tap, dSecGensizeT2Tap, dSecGensizeT3Tap):
        message = "Properties.Section1D('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iSecType, iSecGentype, dSecGensizeA, dSecGensizeB, dSecGensizeH, dSecGensizeT1, dSecGensizeT2, dSecGensizeT3, bSecTapered, dSecGensizeATap, dSecGensizeBTap, dSecGensizeHTap, dSecGensizeT1Tap, dSecGensizeT2Tap, dSecGensizeT3Tap)
        return JPT_RUN_LINE(message)

    def Composite(strName, iDFT, dGE, iDLAM, crMat, dNSM, iDPID, dSB, iDSOUT, dTREF, dZ0, dZOFF, crlTarget, crEdit, crDcrLocalCS, iDmatOrientType, vecDmatOrient):
        message = "Properties.Composite('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDFT, dGE, iDLAM, crMat, dNSM, iDPID, dSB, iDSOUT, dTREF, dZ0, dZOFF, crlTarget, crEdit, crDcrLocalCS, iDmatOrientType, vecDmatOrient)
        return JPT_RUN_LINE(message)

    def BAR(strName, iId, crSection, iShapeDataType, crDatacrMat, dDatadArea, dlDataOrient, dlDataInertia, dDatadTorConst, dDatadNSM, dDataShearAreaFactor0, dDataShearAreaFactor1, dDataStressRecoveryCoeff0, dDataStressRecoveryCoeff1, dDataStressRecoveryCoeff2, dDataStressRecoveryCoeff3, dDataStressRecoveryCoeff4, dDataStressRecoveryCoeff5, dDataStressRecoveryCoeff6, dDataStressRecoveryCoeff7, bDataPinA0, bDataPinA1, bDataPinA2, bDataPinA3, bDataPinA4, bDataPinA5, bDataPinB0, bDataPinB1, bDataPinB2, bDataPinB3, bDataPinB4, bDataPinB5, dlDataOffset0, dlDataOffset1, iLocalLengthUnit, iLocalMassUnit, crlTarget, crEdit):
        message = "Properties.BAR('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iId, crSection, iShapeDataType, crDatacrMat, dDatadArea, dlDataOrient, dlDataInertia, dDatadTorConst, dDatadNSM, dDataShearAreaFactor0, dDataShearAreaFactor1, dDataStressRecoveryCoeff0, dDataStressRecoveryCoeff1, dDataStressRecoveryCoeff2, dDataStressRecoveryCoeff3, dDataStressRecoveryCoeff4, dDataStressRecoveryCoeff5, dDataStressRecoveryCoeff6, dDataStressRecoveryCoeff7, bDataPinA0, bDataPinA1, bDataPinA2, bDataPinA3, bDataPinA4, bDataPinA5, bDataPinB0, bDataPinB1, bDataPinB2, bDataPinB3, bDataPinB4, bDataPinB5, dlDataOffset0, dlDataOffset1, iLocalLengthUnit, iLocalMassUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ThicknessDistribution(dMax, dMin, iByEach, dlTaThicknessValueSet):
        message = "Properties.ThicknessDistribution({},{},{},{})".format(dMax, dMin, iByEach, dlTaThicknessValueSet)
        return JPT_RUN_LINE(message)

    def RigidBody(strName, iId, iRefNodeId, crlTarget, crEdit):
        message = "Properties.RigidBody('{}',{},{},{},{})".format(strName, iId, iRefNodeId, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class SNOnePush:
    DropTest = DropTest()

    def CADImport(dDsurfaceplaneTolerance,dDsurfaceplaneAngle,dMaxFacetWidth,bBnxMultipart,dChordHeightTolerance,dAngleToleranceDegree,iConvertIsolatedCurve,iIigesFixedcurevepreference,iIigesAutostitch,dDigesStitchtolerance,iIcatiaConvertnotshowedelement,iIcatiaConvertnotshowedinstance,iIcatiaConvertaxis,iIstepCreateseam,dDstepPointtolerance,iIacisHealacisbeforeversion,iIjtConvertgeometrytype,iIjtConvertgeneralpart,iIjtConvertaxis,iIjtConvertcenterline,dDcreoChordheighttolerance,dDcreoAngletolerancedegree,strAbsCreoPath,iTransType,iFileType,strFilePath,bRenameDuplicateName,strCSVFilePath):
        message = "SNOnePush.CADImport({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},'{}',{},'{}')".format(dDsurfaceplaneTolerance,dDsurfaceplaneAngle,dMaxFacetWidth,bBnxMultipart,dChordHeightTolerance,dAngleToleranceDegree,iConvertIsolatedCurve,iIigesFixedcurevepreference,iIigesAutostitch,dDigesStitchtolerance,iIcatiaConvertnotshowedelement,iIcatiaConvertnotshowedinstance,iIcatiaConvertaxis,iIstepCreateseam,dDstepPointtolerance,iIacisHealacisbeforeversion,iIjtConvertgeometrytype,iIjtConvertgeneralpart,iIjtConvertaxis,iIjtConvertcenterline,dDcreoChordheighttolerance,dDcreoAngletolerancedegree,strAbsCreoPath,iTransType,iFileType,strFilePath,bRenameDuplicateName,strCSVFilePath)
        return JPT_RUN_LINE(message)

    def DropTestSNOnePush(strName, iDir, dRopHeight, dSolutionTime, iNumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat):
        message = "SNOnePush.DropTestSNOnePush('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iNumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

    def AutoSweepClosedLoopShaped(crlPart,dMeshSize,dLengthSize):
        message = "SNOnePush.AutoSweepClosedLoopShaped({},{},{})".format(crlPart,dMeshSize,dLengthSize)
        return JPT_RUN_LINE(message)

class StiffCalc:
    def Force(strName,poslForce,poslMoment,iEnArrowDir,iEnDistrbute,crCurCoord,crTable,crNodeSet,dFPhase,dFDelay,crPhaseTable,strFormula0,strFormula1,strFormula2,strFormula3,strFormula4,strFormula5,crlTarget,crEdit):
        message = "StiffCalc.Force('{}',{},{},{},'{}',{},{},{},{},{},{},'{}','{}','{}','{}','{}','{}',{},{})".format(strName,poslForce,poslMoment,iEnArrowDir,iEnDistrbute,crCurCoord,crTable,crNodeSet,dFPhase,dFDelay,crPhaseTable,strFormula0,strFormula1,strFormula2,strFormula3,strFormula4,strFormula5,crlTarget,crEdit)
        return JPT_RUN_LINE(message)

class SZOnepushReliability:
    Assembly = Assembly()

    MeshEdit = MeshEdit()

    def AlignMidNode(crlSource,crlTarget):
        message = "SZOnepushReliability.AlignMidNode({},{})".format(crlSource,crlTarget)
        return JPT_RUN_LINE(message)

class Test:
    Connection = Connection()

    Muffler = Muffler()

    ZGeometryTest = ZGeometryTest()

    def FindFacesInPart(crPart,strIdentical):
        message = "Test.FindFacesInPart({},'{}')".format(crPart,strIdentical)
        return JPT_RUN_LINE(message)

    def CreateElementForWelding(crlSrcElems,crlDstElems,crlSideElems,crlPart,crMaterial):
        message = "Test.CreateElementForWelding({},{},{},{},{})".format(crlSrcElems,crlDstElems,crlSideElems,crlPart,crMaterial)
        return JPT_RUN_LINE(message)

class Tool:
    Connections = Connections()

    Coordinates = Coordinates()

    Group = Group()

    ImprintEdges = ImprintEdges()

    def ElementCS(iMethod, iDispType, bDispXDir, bDispCoord, dDispScale, crlTarget):
        message = "Tool.ElementCS({},{},{},{},{},{})".format(iMethod, iDispType, bDispXDir, bDispCoord, dDispScale, crlTarget)
        return JPT_RUN_LINE(message)

    Measure = Measure()

    MeshQuality = MeshQuality()

class Toolbar:
    def Undo(iCntUndo):
        message = "Toolbar.Undo({})".format(iCntUndo)
        return JPT_RUN_LINE(message)

    def Redo(iCntRedo):
        message = "Toolbar.Redo({})".format(iCntRedo)
        return JPT_RUN_LINE(message)

class Tools:
    BySelection = BySelection()

    Group = Group()

    TotalLoad = TotalLoad()

    def NodeCS(crlInst, crCoordSystem):
        message = "Tools.NodeCS({},{})".format(crlInst, crCoordSystem)
        return JPT_RUN_LINE(message)

    def NodeCSGroup():
        message = "Tools.NodeCSGroup({})".format()
        return JPT_RUN_LINE(message)

    def DisplacementCS(crlInst, crCoordSystem):
        message = "Tools.DisplacementCS({},{})".format(crlInst, crCoordSystem)
        return JPT_RUN_LINE(message)

    def Connections(listConnectRenumberTool):
        message = "Tools.Connections({})".format(listConnectRenumberTool)
        return JPT_RUN_LINE(message)

    def GroupByDCS():
        message = "Tools.GroupByDCS({})".format()
        return JPT_RUN_LINE(message)

    def Renumber(listRenumberItem, bAssignProp, bSurfCornerFirst):
        message = "Tools.Renumber({},{},{})".format(listRenumberItem, bAssignProp, bSurfCornerFirst)
        return JPT_RUN_LINE(message)

    def RenumberByConnection(connectRenumberTool, crlTarget):
        message = "Tools.RenumberByConnection({},{})".format(connectRenumberTool, crlTarget)
        return JPT_RUN_LINE(message)

    def RenumberByFile(strCSVPath, iConfilctStrategy, bNeedToUpdateCount):
        message = "Tools.RenumberByFile('{}',{},{})".format(strCSVPath, iConfilctStrategy, bNeedToUpdateCount)
        return JPT_RUN_LINE(message)

    def ModelInfo(strPath, strPathName, listPartInfo, bPropertyAssignedPart, bPropertyAssignedSummary, iModelNode, iNmodelnodeWithprop, ilModelElement, ilNmodelelemWithprop, ilModelLBC, iModelContact, ilModelConnection, ilModelProperty):
        message = "Tools.ModelInfo('{}','{}',{},{},{},{},{},{},{},{},{},{},{})".format(strPath, strPathName, listPartInfo, bPropertyAssignedPart, bPropertyAssignedSummary, iModelNode, iNmodelnodeWithprop, ilModelElement, ilNmodelelemWithprop, ilModelLBC, iModelContact, ilModelConnection, ilModelProperty)
        return JPT_RUN_LINE(message)

    def Section(bSection):
        message = "Tools.Section({})".format(bSection)
        return JPT_RUN_LINE(message)

    Measure = Measure()

class MMCCarACTools:
    ACModelCreationTools = ACModelCreationTools()

    ClearanceElement = ClearanceElement()

class Designer:
    LBC = LBC()

    Load = Load()

    def ContactMerge(crlTarget):
        message = "Designer.ContactMerge({})".format(crlTarget)
        return JPT_RUN_LINE(message)

    def Material(strMatName, strPropName, dThickness, crlTargets):
        message = "Designer.Material('{}','{}',{},{})".format(strMatName, strPropName, dThickness, crlTargets)
        return JPT_RUN_LINE(message)

