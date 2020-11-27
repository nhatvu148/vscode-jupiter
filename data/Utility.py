class Export:
    def STL(strFile, crlPart, dScale, bFilterIndex):
        message = "Export.STL('{}',{},{},{})".format(strFile, crlPart, dScale, bFilterIndex)
        return JPT_RUN_LINE(message)

class FileMenu:
    def AddJTDB(strFileName, strMethod, strTargetModel, strOption, iInputNode, iInputElem, iInputPart, iInputMaterial, iInputProperty):
        message = "FileMenu.AddJTDB('{}','{}','{}','{}',{},{},{},{},{})".format(strFileName, strMethod, strTargetModel, strOption, iInputNode, iInputElem, iInputPart, iInputMaterial, iInputProperty)
        return JPT_RUN_LINE(message)

class FileMenu:
    def Save(strPath, strHistoryTree):
        message = "FileMenu.Save('{}','{}')".format(strPath, strHistoryTree)
        return JPT_RUN_LINE(message)

class ImportCAD:
    def Spatial(strlPath, param, bIsNXDirect, bSetFaceColor, strCsvFilePath):
        message = "ImportCAD.Spatial('{}',{},{},{},'{}')".format(strlPath, param, bIsNXDirect, bSetFaceColor, strCsvFilePath)
        return JPT_RUN_LINE(message)

class FileMenu:
    def LoadDB(strPath, bUseTmpTable):
        message = "FileMenu.LoadDB('{}',{})".format(strPath, bUseTmpTable)
        return JPT_RUN_LINE(message)

class HGTMufflerModeling:
    def CreateBeadWeld(crlEdge,crlPrjtedEdge,crlPart,dTol,dRatio,crRefElem):
        message = "HGTMufflerModeling.CreateBeadWeld({},{},{},{},{},{})".format(crlEdge,crlPrjtedEdge,crlPart,dTol,dRatio,crRefElem)
        return JPT_RUN_LINE(message)

class ImportCAD:
    def TechnoStarGeometry(strlPath, bUseUnit):
        message = "ImportCAD.TechnoStarGeometry('{}',{})".format(strlPath, bUseUnit)
        return JPT_RUN_LINE(message)

class ImportCAD:
    def CreoDirect(vecPath, param):
        message = "ImportCAD.CreoDirect({},{})".format(vecPath, param)
        return JPT_RUN_LINE(message)

class ImportCAD:
    def Elysium(strlPath, param, bFaceColor):
        message = "ImportCAD.Elysium('{}',{},{})".format(strlPath, param, bFaceColor)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def NastranBdf(strlFilePaths, iMportType, dFaceAngle, dEdgeAngle, bReadNameComment, iCreateDup1DElemAnswer):
        message = "ImportMesh.NastranBdf('{}',{},{},{},{},{})".format(strlFilePaths, iMportType, dFaceAngle, dEdgeAngle, bReadNameComment, iCreateDup1DElemAnswer)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def ADVCADX(strPath, dFaceAngle, dEdgeAngle):
        message = "ImportMesh.ADVCADX('{}',{},{})".format(strPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def LSDYNA(strlPath, dFaceAngle, dEdgeAngle):
        message = "ImportMesh.LSDYNA('{}',{},{})".format(strlPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def AbaqusINP(strlFilePaths, dFaceAngle, dEdgeAngle, iMportType):
        message = "ImportMesh.AbaqusINP('{}',{},{},{})".format(strlFilePaths, dFaceAngle, dEdgeAngle, iMportType)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def Universal(strPath):
        message = "ImportMesh.Universal('{}')".format(strPath)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def AnsysDat(strlPath, dFaceAngle, dEdgeAngle):
        message = "ImportMesh.AnsysDat('{}',{},{})".format(strlPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def TSVPre(strImportPath, strExportPath, ilModelIndex, iMerge):
        message = "ImportMesh.TSVPre('{}','{}',{},{})".format(strImportPath, strExportPath, ilModelIndex, iMerge)
        return JPT_RUN_LINE(message)

class Utility:
    def FindEntities(strTarget, strTargetType, bFindMatch):
        message = "Utility.FindEntities('{}','{}',{})".format(strTarget, strTargetType, bFindMatch)
        return JPT_RUN_LINE(message)

class Utility:
    def MeasureDistanceBy2Edges(crEdgeFirst,crEdgeLast, iPrecision):
        message = "Utility.MeasureDistanceBy2Edges({},{},{})".format(crEdgeFirst,crEdgeLast, iPrecision)
        return JPT_RUN_LINE(message)

class ACBoundary:
    def Method1(self, crlPart,bIsMergePart,bIsRenumber):
        message = "ACModeling.ACBoundary.Method1({},{},{})".format(crlPart,bIsMergePart,bIsRenumber)
        return JPT_RUN_LINE(message)

class Create:
    def Convex(self, crlTacrBodies, dMeshSize, dOffset, dRadius, iDAxisGround, dScale):
        message = "ACModeling.Create.Convex({},{},{},{},{},{})".format(crlTacrBodies, dMeshSize, dOffset, dRadius, iDAxisGround, dScale)
        return JPT_RUN_LINE(message)

class ACModeling:
    def CloseHoleAuto(crlClosedHoleParts):
        message = "ACModeling.CloseHoleAuto({})".format(crlClosedHoleParts)
        return JPT_RUN_LINE(message)

class ACModeling:
    def Cut(crlPart):
        message = "ACModeling.Cut({})".format(crlPart)
        return JPT_RUN_LINE(message)

class AbaqusStep:
    def DynamicStep(self, param, crEdit):
        message = "Analysis.AbaqusStep.DynamicStep({},{})".format(param, crEdit)
        return JPT_RUN_LINE(message)

class Analysis:
    AbaqusStep = AbaqusStep()

class AbaqusStep:
    def TransientStep(self, strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, dMaxAllowTChange, iEndsteptBchecked, dlEndsteptTlist, dMaxAllowEmissivityChange, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, dAdjustFactor, iMaxContactIter, iBNlgeom, dTimePeriod, iConvertDscntIter, iRamp, iExtrapolateMethod, listAbaqusOutputRequest, crEdit):
        message = "Analysis.AbaqusStep.TransientStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, dMaxAllowTChange, iEndsteptBchecked, dlEndsteptTlist, dMaxAllowEmissivityChange, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, dAdjustFactor, iMaxContactIter, iBNlgeom, dTimePeriod, iConvertDscntIter, iRamp, iExtrapolateMethod, listAbaqusOutputRequest, crEdit)
        return JPT_RUN_LINE(message)

class ACModeling:
    Create = Create()

class Analysis:
    AbaqusStep = AbaqusStep()

class AbaqusStep:
    def DynamicCoupledTDExplicitStep(self, strName,strDesp,iBAutomatic,iMaxSizebchecked,dlMaxSizeTList,iIncrmtEstimator,iUserTimeIncrmtbchecked,dlUserTimeIncrmtTList,dTimeScalfactor,iBNlgeom,dTimePeriod,dLinearBlkVisco,dQuadrBlkVisco,listAbaqusOutputRequest,crEdit):
        message = "Analysis.AbaqusStep.DynamicCoupledTDExplicitStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName,strDesp,iBAutomatic,iMaxSizebchecked,dlMaxSizeTList,iIncrmtEstimator,iUserTimeIncrmtbchecked,dlUserTimeIncrmtTList,dTimeScalfactor,iBNlgeom,dTimePeriod,dLinearBlkVisco,dQuadrBlkVisco,listAbaqusOutputRequest,crEdit)
        return JPT_RUN_LINE(message)

class ACModeling:
    ACBoundary = ACBoundary()

class Analysis:
    AbaqusStep = AbaqusStep()

class Analysis:
    AbaqusStep = AbaqusStep()

class AbaqusStep:
    def CoupledTDStep(self, strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, abaqusPair1, abaqusPair2, iCSVIntegration, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, dAdjustFactor, iMaxContactIter, iType, iBUseAdaptive, dDampingfactor, dMaxRationofStrainEnergy, iBNlgeom, dTimePeriod, iTransient, iConvertDscntIter, iRamp, iExtrapolateMethod, iBIncldCSV, listOutput, crEdit):
        message = "Analysis.AbaqusStep.CoupledTDStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, abaqusPair1, abaqusPair2, iCSVIntegration, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, dAdjustFactor, iMaxContactIter, iType, iBUseAdaptive, dDampingfactor, dMaxRationofStrainEnergy, iBNlgeom, dTimePeriod, iTransient, iConvertDscntIter, iRamp, iExtrapolateMethod, iBIncldCSV, listOutput, crEdit)
        return JPT_RUN_LINE(message)

class AbaqusStep:
    def DynamicExplicitStep(self, strName, strDesp, iBAutomatic, iIncrmtEstimator, abaqusPair1, dTimeScalfactor, abaqusPair2, iBNlgeom, dTimePeriod, iBIncldHeatEffect, dLinearBlkVisco, dQuadrBlkVisco, listOutput, crEdit):
        message = "Analysis.AbaqusStep.DynamicExplicitStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iBAutomatic, iIncrmtEstimator, abaqusPair1, dTimeScalfactor, abaqusPair2, iBNlgeom, dTimePeriod, iBIncldHeatEffect, dLinearBlkVisco, dQuadrBlkVisco, listOutput, crEdit)
        return JPT_RUN_LINE(message)

class AbaqusStep:
    def ModalStep(self, strName, strDesp, iEigenSolver, iNFreqRequestbchecked, ilNFreqRequestTList, iFreqShiftbchecked, ilFreqShiftTList, iFreqRangebchecked, ilFreqRangeTList, iIncldAcoustic, iBlockSizebchecked, ilBlockSizeTList, iMaxBlkNumofLanczosStepbchecked, ilMaxBlkNumofLanczosStepTList, iBUseSIM, iBIncldResMods, iNEigenRequest, iMaxItersUsed, iVectorsUsed, iMethod, iMatrixStorage, iNormalizeEigenBy, iEvalPropFreqbchecked, ilEvalPropFreqTList, abaqusOutputRequest, crEdit):
        message = "Analysis.AbaqusStep.ModalStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iEigenSolver, iNFreqRequestbchecked, ilNFreqRequestTList, iFreqShiftbchecked, ilFreqShiftTList, iFreqRangebchecked, ilFreqRangeTList, iIncldAcoustic, iBlockSizebchecked, ilBlockSizeTList, iMaxBlkNumofLanczosStepbchecked, ilMaxBlkNumofLanczosStepTList, iBUseSIM, iBIncldResMods, iNEigenRequest, iMaxItersUsed, iVectorsUsed, iMethod, iMatrixStorage, iNormalizeEigenBy, iEvalPropFreqbchecked, ilEvalPropFreqTList, abaqusOutputRequest, crEdit)
        return JPT_RUN_LINE(message)

class Analysis:
    AbaqusStep = AbaqusStep()

class Analysis:
    AbaqusStep = AbaqusStep()

class AbaqusStep:
    def StaticRiskStep(self, strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, iMethod, iMatrixStorage, dMaxLdPropFactor, iBMaxLdPropFactor, iBMaxDisp, dMaxDisp, iMaxDispDof, strNdRgn, iBNlgeom, iBIncldHeatEffect, iConvertDscntIter, dTotalArcLength, iExtrapolateMethod, iBAcceptByMaxIters, iBLongTerm, iBPerturbation, iFullplasticregionBchecked, strlFullplasticregionTlist, iOutput, crEdit):
        message = "Analysis.AbaqusStep.StaticRiskStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},'{}',{},{})".format(strName, strDesp, iBAutomatic, iMaxInc, dInitSize, dMinSize, dMaxSize, iMethod, iMatrixStorage, dMaxLdPropFactor, iBMaxLdPropFactor, iBMaxDisp, dMaxDisp, iMaxDispDof, strNdRgn, iBNlgeom, iBIncldHeatEffect, iConvertDscntIter, dTotalArcLength, iExtrapolateMethod, iBAcceptByMaxIters, iBLongTerm, iBPerturbation, iFullplasticregionBchecked, strlFullplasticregionTlist, iOutput, crEdit)
        return JPT_RUN_LINE(message)

class AbaqusStep:
    def SteadyStateStep(self, strName, strDesp, iAutomatic, iMaxInc, iNitSize, dMinSize, dMaxSize, dMaxAllowTChange, iEndStepbchecked, dlEndStepTList, dMaxAllowEmissivityChange, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, iAdjustFactor, iMaxContactIter, iNlgeom, dTimePeriod, iConvertDscntIter, iRamp, iExtrapolateMethod, iOutput, crEdit):
        message = "Analysis.AbaqusStep.SteadyStateStep('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, strDesp, iAutomatic, iMaxInc, iNitSize, dMinSize, dMaxSize, dMaxAllowTChange, iEndStepbchecked, dlEndStepTList, dMaxAllowEmissivityChange, iMethod, iMatrixStorage, iSolutionTech, iAllowedIters, iAdjustFactor, iMaxContactIter, iNlgeom, dTimePeriod, iConvertDscntIter, iRamp, iExtrapolateMethod, iOutput, crEdit)
        return JPT_RUN_LINE(message)

class Analysis:
    AbaqusStep = AbaqusStep()

class Analysis:
    ACTRAN = ACTRAN()

class Analysis:
    AbaqusStep = AbaqusStep()

class ACTRAN:
    def ExportBdf(self, strPath):
        message = "Analysis.ACTRAN.ExportBdf('{}')".format(strPath)
        return JPT_RUN_LINE(message)

class ACTRAN:
    def Run(self, actranAnalysis, crlTarget, crEdit):
        message = "Analysis.ACTRAN.Run({},{},{})".format(actranAnalysis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Analysis:
    ACTRAN = ACTRAN()

class ACTRAN:
    def CreateEdat(self, actranAnalysis, crlTarget, crEdit):
        message = "Analysis.ACTRAN.CreateEdat({},{},{})".format(actranAnalysis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Analysis:
    Ansys = Ansys()

class Analysis:
    ACTRAN = ACTRAN()

class Ansys:
    def LinearStatic(self, strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob):
        message = "Analysis.Ansys.LinearStatic('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

class Ansys:
    def HeadTransferSteady(self, strName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit):
        message = "Analysis.Ansys.HeadTransferSteady('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit)
        return JPT_RUN_LINE(message)

class Analysis:
    Ansys = Ansys()

class Ansys:
    def NormalModes(self, strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob):
        message = "Analysis.Ansys.NormalModes('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

class Analysis:
    Ansys = Ansys()

class Ansys:
    def Harmonic(self, strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob):
        message = "Analysis.Ansys.Harmonic('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

class Ansys:
    def Steady(self, strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob):
        message = "Analysis.Ansys.Steady('{}',{},{},'{}','{}',{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strJobName, iJobdataAnatype, iJobdataSoltype, strJobdataJobname, strJobdataJobdescription, bBasicdataBoutputdisplacements, bBasicdataBoutputreactionload, bBasicdataBoutputstrain, bBasicdataBoutputstress, iBasicdataIanalysisopt, bBasicdataBcalPressEffects, dBasicdataFunitem, dBasicdataFreftemp, dBasicdataFendloadtime, iBasicdataItimestep, iBasicdataIstepchosen, iBasicdataIsubstepnum, iBasicdataImaxsubstep, iBasicdataIminstepnum, dBasicdataFtimestepsize, dBasicdataFmintimestep, dBasicdataFmaxtimestep, iBasicdataIwritereslutfre, iBasicdataIn, bRunAPDL, bWriteResultDB, dFEndFreq, dFStartFreq, iFulltransdataIsolutionoption, dFulltransdataFpropchange, iFulltransdataIpointnum, dFulltransdataFmintemp, dFulltransdataFmaxtemp, iFulltransdataIequationsolv, dFulltransdataFtollevel, dFulltransdataFmultiplier, bFulltransdataBsignleprecision, bFulltransdataBmemorysave, dFulltransdataFtempdiff, dHarmonicdataFstartfreq, dHarmonicdataFendfreq, iHarmonicdataNsubsteps, dHarmonicdataFalphad, dHarmonicdataFbetad, dHarmonicdataFdmprat, bHarmonicdataBoutputdisplacements, bHarmonicdataBoutputstrain, bHarmonicdataBoutputstress, iLCId, iModeShape, iModaldataImodemethod, iModaldataIextractnum, bModaldataBexpandshape, iModaldataIexpandnum, bModaldataBuseapprox, bModaldataBinclprsseff, bModaldataBmemorysave, bModaldataBrsvec, bModaldataBoutputdisplacements, bModaldataBoutputstrain, bModaldataBoutputstress, iReduceddataIprintnum, bSsdataBmemorysave, bSsdataBoutputheatflux, bSsdataBoutputtemperature, bSsdataBpivotscheck, bSsdataBsignleprecision, dSsdataFmultiplier, dSsdataFtempdiff, dSsdataFtollevel, iSsdataIadaptivedes, iSsdataIequationsolv, iSsdataInpoption, strAnsysVersion, strCommandLineOption, bOutputSOLVE, iSubspacedataIrigidmode, iSubspacedataIworksize, iSubspacedataInpadnum, iSubspacedataIblocknum, iSubspacedataImaxiteratcnt, iSubspacedataIminnshift, iSubspacedataIseqcheck, bTransientdataBtraneffect, iTransientdataIloadingtype, dTransientdataFmassmatrixmult, dTransientdataFstiffmatrixmult, bTransientdataBmidstep, dTransientdataFtolerancebisection, dTransientdataFtolerancetimestep, iTransientdataItimeinteralgor, iTransientdataItimeinter, dTransientdataFgamma, dTransientdataFalpha, dTransientdataFdelta, dTransientdataFalphaf, dTransientdataFalpham, bTransientdataBoutputtemperature, bTransientdataBoutputheatflux, crEdit, strFileName, crAnsysJob)
        return JPT_RUN_LINE(message)

class Analysis:
    Ansys = Ansys()

class Nastran:
    def ModalTransientResponse(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.ModalTransientResponse('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis:
    Nastran = Nastran()

class Nastran:
    def LinearBuckling(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.LinearBuckling('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis:
    Nastran = Nastran()

class Nastran:
    def Transient(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.Transient('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Nastran:
    def SteadyState(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.SteadyState('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis:
    Nastran = Nastran()

class Analysis:
    Nastran = Nastran()

class Nastran:
    def ModalFrequencyResponse(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.ModalFrequencyResponse('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis:
    Nastran = Nastran()

class Nastran:
    def LinearStatic(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.LinearStatic('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Nastran:
    def NormalModes(self, strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.Nastran.NormalModes('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis:
    Ansys = Ansys()

class Analysis:
    Nastran = Nastran()

class Permas:
    def Job(self, strName,strDescription,iType,crEdit,crlTarget,bElStress,bElStressMis,bElStrain,bNodeStess,bGZip,bIdeas,bNLResult,iNLStepType,dEquiStart,dEquiStep,dEquiEnd,strNLStepList,bTimeStep,iTimeStepKind,dTimeStart,dTimeStep,dTimeEnd,iLCId):
        message = "Analysis.Permas.Job('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{})".format(strName,strDescription,iType,crEdit,crlTarget,bElStress,bElStressMis,bElStrain,bNodeStess,bGZip,bIdeas,bNLResult,iNLStepType,dEquiStart,dEquiStep,dEquiEnd,strNLStepList,bTimeStep,iTimeStepKind,dTimeStart,dTimeStep,dTimeEnd,iLCId)
        return JPT_RUN_LINE(message)

class Analysis:
    Permas = Permas()

class Analysis:
    Nastran = Nastran()

class TSSolver:
    def ExportDynamisBdf(self, strPath,crJob):
        message = "Analysis.TSSolver.ExportDynamisBdf('{}',{})".format(strPath,crJob)
        return JPT_RUN_LINE(message)

class TSSolver:
    def Job(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit):
        message = "Analysis.TSSolver.Job('{}','{}',{},'{}',{})".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSolver = TSSolver()

class TSSolver:
    def LinearBucking(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.LinearBucking('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSolver = TSSolver()

class TSSolver:
    def LinearStatic(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.LinearStatic('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class TSSolver:
    def NonlinearStatic(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.NonlinearStatic('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSolver = TSSolver()

class Analysis:
    TSSolver = TSSolver()

class TSSolver:
    def NormalModes(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.NormalModes('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSolver = TSSolver()

class Analysis:
    TSSolver = TSSolver()

class TSSolver:
    def NonlinearFrequency(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.NonlinearFrequency('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class TSSolver:
    def ModalTransientResponse(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.ModalTransientResponse('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSolver = TSSolver()

class Analysis:
    TSSolver = TSSolver()

class Analysis:
    TSSolver = TSSolver()

class TSSolver:
    def ModalFrequencyResponse(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.ModalFrequencyResponse('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class TSSolver:
    def SteadyStateHeatTransfer(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.SteadyStateHeatTransfer('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSolver = TSSolver()

class TSSolver:
    def TransientHeatTransfer(self, strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath):
        message = "Analysis.TSSolver.TransientHeatTransfer('{}','{}',{},'{}',{},'{}')".format(strName, strDescription, crlTarget, nastranAnalysis, crEdit, strPath)
        return JPT_RUN_LINE(message)

class TSSS:
    def TransientHeatTransfer(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.TransientHeatTransfer('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSS = TSSS()

class TSSS:
    def LinearStatic(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer, iNitTempType):
        message = "Analysis.TSSS.LinearStatic('{}','{}',{},'{}',{},{},{},'{}',{},{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer, iNitTempType)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSolver = TSSolver()

class TSSS:
    def NonlinearStatic(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.NonlinearStatic('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSS = TSSS()

class Analysis:
    TSSS = TSSS()

class TSSS:
    def NormalModes(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.NormalModes('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSS = TSSS()

class TSSS:
    def LinearBuckling(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.LinearBuckling('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class TSSS:
    def ModalFrequencyResponse(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.ModalFrequencyResponse('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class TSSS:
    def SteadyStateHeatTransfer(self, strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer):
        message = "Analysis.TSSS.SteadyStateHeatTransfer('{}','{}',{},'{}',{},{},{},'{}',{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, iRadialReturn, listNlparmsForSubcase, crEdit, strPath, iModelCheckAnswer, iDeleteSlaveNodesAnswer)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSS = TSSS()

class Analysis:
    TSSS = TSSS()

class Analysis:
    def Abaqus(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat):
        message = "Analysis.Abaqus('{}',{},{},{},{},{},{},'{}',{},{},'{}',{},{},{},{},{},{})".format(strName, bRBE2toMPC, bRenameProcess, iCodeType, iSurfDefType, iUnit, iWriteType, strDescription, crlStepSequence, crEdit, strlUserText, bExptNdEleGroups, bDeleteFloatingNodes, bExptFaceElemGroups2Surface, bLoadCase, bAutoAssignDummyProperty, crDummyMat)
        return JPT_RUN_LINE(message)

class Analysis:
    def ExportAnsys(strName, crAnsysJob):
        message = "Analysis.ExportAnsys('{}',{})".format(strName, crAnsysJob)
        return JPT_RUN_LINE(message)

class Analysis:
    def ExportAbaqus(crAbaJob, crlSelectPart, strInpPath):
        message = "Analysis.ExportAbaqus({},{},'{}')".format(crAbaJob, crlSelectPart, strInpPath)
        return JPT_RUN_LINE(message)

class Analysis:
    def ExportAdx(crJob, strPath, iNumType, iUiWidth, iUiPrecision):
        message = "Analysis.ExportAdx({},'{}',{},{},{})".format(crJob, strPath, iNumType, iUiWidth, iUiPrecision)
        return JPT_RUN_LINE(message)

class Analysis:
    TSSS = TSSS()

class Analysis:
    def ModifyLbcToStep(listabaqusLbcStepInfo):
        message = "Analysis.ModifyLbcToStep({})".format(listabaqusLbcStepInfo)
        return JPT_RUN_LINE(message)

class Analysis:
    def ExportLsdyna(strPath, crJob):
        message = "Analysis.ExportLsdyna('{}',{})".format(strPath, crJob)
        return JPT_RUN_LINE(message)

class Analysis:
    def NastranJob(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit):
        message = "Analysis.NastranJob('{}','{}',{},'{}',{},{},{})".format(strName, strDescription, crlTarget, nastranAnalysis, bDummyPropAutoAssign, iDummyPropMaterialID, crEdit)
        return JPT_RUN_LINE(message)

class Analysis:
    def LSDYNAJob(crEdit):
        message = "Analysis.LSDYNAJob({})".format(crEdit)
        return JPT_RUN_LINE(message)

class MakeProcess:
    def Static(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.Static('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class Analysis:
    ADVC = ADVC()

class ADVC:
    MakeProcess = MakeProcess()

class ADVC:
    MakeProcess = MakeProcess()

class MakeProcess:
    def Creep(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, bThetaDefined, dTheta, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.Creep('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, bThetaDefined, dTheta, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class ADVC:
    MakeProcess = MakeProcess()

class Analysis:
    ADVC = ADVC()

class MakeProcess:
    def Dynamic(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, bDynamic, advcDynamic, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.Dynamic('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, bDynamic, advcDynamic, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class MakeProcess:
    def EigenValue(self, strName, bEigenValue, iNumberOfModes, iEigenvecNorm, dShift, dCgcgpiTol, dCgcgpiEigTol, iCgcgpiLoopMax, dCgcgpiInnerTol, iCgcgpiBlockSize, iCgcgpiExtraMode, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.EigenValue('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, bEigenValue, iNumberOfModes, iEigenvecNorm, dShift, dCgcgpiTol, dCgcgpiEigTol, iCgcgpiLoopMax, dCgcgpiInnerTol, iCgcgpiBlockSize, iCgcgpiExtraMode, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class ADVC:
    MakeProcess = MakeProcess()

class Analysis:
    ADVC = ADVC()

class MakeProcess:
    def DynamicExplicit(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, iLogMessageInterval, iLinearApproximation, dBulkViscosityCoef1, dBulkViscosityCoef2, dMassScalingdt, dDtScaleFactor, dPenaltyScaleFactor, iContactSearchInterval, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.DynamicExplicit('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, iLogMessageInterval, iLinearApproximation, dBulkViscosityCoef1, dBulkViscosityCoef2, dMassScalingdt, dDtScaleFactor, dPenaltyScaleFactor, iContactSearchInterval, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class Analysis:
    ADVC = ADVC()

class ADVC:
    MakeProcess = MakeProcess()

class MakeProcess:
    def ModalFreqResp(self, strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.ModalFreqResp('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class Analysis:
    ADVC = ADVC()

class ADVC:
    MakeProcess = MakeProcess()

class MakeProcess:
    def ResponseSpectrum(self, strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, iPropMethod, iSpttype, dSptFactor0, crSpt0, dSptFactor1, crSpt1, dSptFactor2, crSpt2, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.ResponseSpectrum('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, iPropMethod, iSpttype, dSptFactor0, crSpt0, dSptFactor1, crSpt1, dSptFactor2, crSpt2, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class Analysis:
    ADVC = ADVC()

class Analysis:
    ADVC = ADVC()

class ADVC:
    MakeProcess = MakeProcess()

class MakeProcess:
    def SteadyState(self, strName, iEndType, dMaxTime, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList):
        message = "Analysis.ADVC.MakeProcess.SteadyState('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iEndType, dMaxTime, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList)
        return JPT_RUN_LINE(message)

class Analysis:
    ADVC = ADVC()

class ADVC:
    MakeProcess = MakeProcess()

class ADVC:
    MakeProcess = MakeProcess()

class MakeProcess:
    def Transient(self, strName, iEndType, dMaxTime, dSteadyRate, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList):
        message = "Analysis.ADVC.MakeProcess.Transient('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iEndType, dMaxTime, dSteadyRate, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList)
        return JPT_RUN_LINE(message)

class Analysis:
    ADVC = ADVC()

class ADVC:
    MakeProcess = MakeProcess()

class Analysis:
    ADVC = ADVC()

class ADVC:
    MakeProcess = MakeProcess()

class MakeProcess:
    def RandomResponse(self, strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, iPropMethod, iPSDtype, iPSDdir, crPSDLoad, dPSDFactor, dGravityAccel, iOutputEigenFreqStep, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.RandomResponse('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, iPropMethod, iPSDtype, iPSDdir, crPSDLoad, dPSDFactor, dGravityAccel, iOutputEigenFreqStep, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class Analysis:
    ADVC = ADVC()

class MakeProcess:
    def Fatigue(self, strName, bFatigue, iMethod, iStressAxis, iSafetyType, dSearchResolution, dSafetyMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.Fatigue('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, bFatigue, iMethod, iStressAxis, iSafetyType, dSearchResolution, dSafetyMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class ADVC:
    def Structure(self, strName, strDescription, iEJobType, crlProcessSequence, crlElemLocationGroup, crlNodeLocationGroup, bWriteGroup, crEdit, bResultReference, iSeparateFile, bExportRelatedAllLBCs, bUseEntityName, bMatrixSloverParam, iPreconditionType, iMatrixStructure, crlTarget, iLoadType, bSameOutputOnAllProcess, bDeleteFloatingNode, bBC, bCheckBCDuplicate, bAutoAssignDummyProp, crDummyPropMaterial, bReferenceRestartData, strReferenceRestartDataPath, iReferenceRestartDataProcessNum, iReferenceRestartDataStepNum, iReferenceRestartDataCoordType, iReferenceRestartDataUpdateContactSearch, listLoadNodeContact, iHeatConvection, iCreateProcessForBoltFixedLength, strPath, iNumType, iUiWidth, iUiPrecision):
        message = "Analysis.ADVC.Structure('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, strDescription, iEJobType, crlProcessSequence, crlElemLocationGroup, crlNodeLocationGroup, bWriteGroup, crEdit, bResultReference, iSeparateFile, bExportRelatedAllLBCs, bUseEntityName, bMatrixSloverParam, iPreconditionType, iMatrixStructure, crlTarget, iLoadType, bSameOutputOnAllProcess, bDeleteFloatingNode, bBC, bCheckBCDuplicate, bAutoAssignDummyProp, crDummyPropMaterial, bReferenceRestartData, strReferenceRestartDataPath, iReferenceRestartDataProcessNum, iReferenceRestartDataStepNum, iReferenceRestartDataCoordType, iReferenceRestartDataUpdateContactSearch, listLoadNodeContact, iHeatConvection, iCreateProcessForBoltFixedLength, strPath, iNumType, iUiWidth, iUiPrecision)
        return JPT_RUN_LINE(message)

class ADVC:
    def HeatTransfer(self, strName, strDescription, iEJobType, crlProcessSequence, crlElemLocationGroup, crlNodeLocationGroup, bWriteGroup, crEdit, bResultReference, iSeparateFile, bExportRelatedAllLBCs, bUseEntityName, bMatrixSloverParam, iPreconditionType, iMatrixStructure, crlTarget, iLoadType, bSameOutputOnAllProcess, bDeleteFloatingNode, bBC, bCheckBCDuplicate, bAutoAssignDummyProp, crDummyPropMaterial, bReferenceRestartData, strReferenceRestartDataPath, iReferenceRestartDataProcessNum, iReferenceRestartDataStepNum, iReferenceRestartDataCoordType, iReferenceRestartDataUpdateContactSearch, listLoadNodeContact, iHeatConvection, strPath, iNumType, iUiWidth, iUiPrecision):
        message = "Analysis.ADVC.HeatTransfer('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},'{}',{},{},{})".format(strName, strDescription, iEJobType, crlProcessSequence, crlElemLocationGroup, crlNodeLocationGroup, bWriteGroup, crEdit, bResultReference, iSeparateFile, bExportRelatedAllLBCs, bUseEntityName, bMatrixSloverParam, iPreconditionType, iMatrixStructure, crlTarget, iLoadType, bSameOutputOnAllProcess, bDeleteFloatingNode, bBC, bCheckBCDuplicate, bAutoAssignDummyProp, crDummyPropMaterial, bReferenceRestartData, strReferenceRestartDataPath, iReferenceRestartDataProcessNum, iReferenceRestartDataStepNum, iReferenceRestartDataCoordType, iReferenceRestartDataUpdateContactSearch, listLoadNodeContact, iHeatConvection, strPath, iNumType, iUiWidth, iUiPrecision)
        return JPT_RUN_LINE(message)

class Analysis:
    ADVC = ADVC()

class SeparateFaces:
    def AllSharedNodes(self, ):
        message = "Assemble.SeparateFaces.AllSharedNodes({})".format()
        return JPT_RUN_LINE(message)

class Assemble:
    SeparateFaces = SeparateFaces()

class SeparateFaces:
    def Shell(self, iType, crlEntity, bCreateGroup):
        message = "Assemble.SeparateFaces.Shell({},{},{})".format(iType, crlEntity, bCreateGroup)
        return JPT_RUN_LINE(message)

class Assemble:
    SeparateFaces = SeparateFaces()

class SeparateFaces:
    def Solid(self, ilPartKeys, ilFaceKeys, bCreateGroup):
        message = "Assemble.SeparateFaces.Solid({},{},{})".format(ilPartKeys, ilFaceKeys, bCreateGroup)
        return JPT_RUN_LINE(message)

class Analysis:
    ADVC = ADVC()

class Assemble:
    SeparateFaces = SeparateFaces()

class Assemble:
    def Boolean(crlPart, iBooleanType, dToleranceAlignment, bLeaveOriginalBodies):
        message = "Assemble.Boolean({},{},{},{})".format(crlPart, iBooleanType, dToleranceAlignment, bLeaveOriginalBodies)
        return JPT_RUN_LINE(message)

class Assemble:
    def AssembleFace(crlPart,crlFace,dTolerance,iFitEdge,iMeshSetting):
        message = "Assemble.AssembleFace({},{},{},{},{})".format(crlPart,crlFace,dTolerance,iFitEdge,iMeshSetting)
        return JPT_RUN_LINE(message)

class Assemble:
    def FullLayer(crPart, dLayerWidth, iLayer, bUsePyramid):
        message = "Assemble.FullLayer({},{},{},{})".format(crPart, dLayerWidth, iLayer, bUsePyramid)
        return JPT_RUN_LINE(message)

class Assemble:
    def CylinderLayer(crFace, crNode):
        message = "Assemble.CylinderLayer({},{})".format(crFace, crNode)
        return JPT_RUN_LINE(message)

class Assemble:
    def SharedFace():
        message = "Assemble.SharedFace({})".format()
        return JPT_RUN_LINE(message)

class Assemble:
    def AssembleFaces(ilPairFaceToMakeShareFace, dTolerance, iTypeConnectPos, bUseSnapInput, dSnapTolerance, bFitEdge):
        message = "Assemble.AssembleFaces({},{},{},{},{},{})".format(ilPairFaceToMakeShareFace, dTolerance, iTypeConnectPos, bUseSnapInput, dSnapTolerance, bFitEdge)
        return JPT_RUN_LINE(message)

class Assemble:
    def GeneralLayer(crlTacrfacesForMacro, dWidth, iLayer, bSeparatePart, bForceStitchToSide, bSmoothingEdge, bNoImprint, bWidthOnSurface, bMakeHexa):
        message = "Assemble.GeneralLayer({},{},{},{},{},{},{},{},{})".format(crlTacrfacesForMacro, dWidth, iLayer, bSeparatePart, bForceStitchToSide, bSmoothingEdge, bNoImprint, bWidthOnSurface, bMakeHexa)
        return JPT_RUN_LINE(message)

class Assemble:
    def AddRib(crPart, crlFaces, veclPoints, dWidth, dDepth):
        message = "Assemble.AddRib({},{},{},{},{})".format(crPart, crlFaces, veclPoints, dWidth, dDepth)
        return JPT_RUN_LINE(message)

class Assemble:
    def FindMatingFace(crlMasterFaces, crlSlaveFaces, crlPart, dTolerance):
        message = "Assemble.FindMatingFace({},{},{},{})".format(crlMasterFaces, crlSlaveFaces, crlPart, dTolerance)
        return JPT_RUN_LINE(message)

class Assemble:
    def AddBoss(crPart, iType, bMerge, posOrgCenter, vecOrgDirection, crCoord, iAxis, dAngle, bHollow, dInnerRadius, dOrgOuterRadius, dTaperAngle, iNodeOnCircle, iNodeOnAxis, dOriginalHeight):
        message = "Assemble.AddBoss({},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crPart, iType, bMerge, posOrgCenter, vecOrgDirection, crCoord, iAxis, dAngle, bHollow, dInnerRadius, dOrgOuterRadius, dTaperAngle, iNodeOnCircle, iNodeOnAxis, dOriginalHeight)
        return JPT_RUN_LINE(message)

class Assembly:
    RightClick = RightClick()

class RightClick:
    def AddToReference(self, crSrcPart,crDestPart):
        message = "Assembly.RightClick.AddToReference({},{})".format(crSrcPart,crDestPart)
        return JPT_RUN_LINE(message)

class Assembly:
    RightClick = RightClick()

class RightClick:
    def Suppress(self, crlParts):
        message = "Assembly.RightClick.Suppress({})".format(crlParts)
        return JPT_RUN_LINE(message)

class RightClick:
    def UnSuppress(self, taParts):
        message = "Assembly.RightClick.UnSuppress({})".format(taParts)
        return JPT_RUN_LINE(message)

class RightClick:
    def RestoreOriginalPart(self, crlCrBodies, bKeepShareFace):
        message = "Assembly.RightClick.RestoreOriginalPart({},{})".format(crlCrBodies, bKeepShareFace)
        return JPT_RUN_LINE(message)

class Assembly:
    RightClick = RightClick()

class RightClick:
    def Rename(self, strNewName, crItem):
        message = "Assembly.RightClick.Rename('{}',{})".format(strNewName, crItem)
        return JPT_RUN_LINE(message)

class Assembly:
    RightClick = RightClick()

class Assembly:
    RightClick = RightClick()

class Assembly:
    RightClick = RightClick()

class RightClick:
    def ChangeEntityColor(self, crlEntity, iColor):
        message = "Assembly.RightClick.ChangeEntityColor({},{})".format(crlEntity, iColor)
        return JPT_RUN_LINE(message)

class RightClick:
    def AddSubAssembly(self, crInst):
        message = "Assembly.RightClick.AddSubAssembly({})".format(crInst)
        return JPT_RUN_LINE(message)

class RightClick:
    def ChangeBodyColor(self, listPartColorPair, bResetFaceColor):
        message = "Assembly.RightClick.ChangeBodyColor({},{})".format(listPartColorPair, bResetFaceColor)
        return JPT_RUN_LINE(message)

class RightClick:
    def ChangeMeshLineColor(self, crlFace, iColor):
        message = "Assembly.RightClick.ChangeMeshLineColor({},{})".format(crlFace, iColor)
        return JPT_RUN_LINE(message)

class Assembly:
    RightClick = RightClick()

class Assembly:
    RightClick = RightClick()

class Assembly:
    RightClick = RightClick()

class BoundaryTemperature:
    def Constant(self, strName, dFTemp, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.BoundaryTemperature.Constant('{}',{},{},{},{})".format(strName, dFTemp, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    BoundaryTemperature = BoundaryTemperature()

class BoundaryTemperature:
    def SurfaceMapping(self, strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, iMappedCpIndexArr1, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strPath, crEdit, iMappingMethod, iSubmodeLBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet):
        message = "BoundaryConditions.BoundaryTemperature.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, iMappedCpIndexArr1, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strPath, crEdit, iMappingMethod, iSubmodeLBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
        return JPT_RUN_LINE(message)

class Convection:
    def Constant(self, strName, dExtTemp, crTableTimeTemp, dDcoef, crTableTimeCoeff, crTableTempCoeff, crlTarget, crEdit):
        message = "BoundaryConditions.Convection.Constant('{}',{},{},{},{},{},{},{})".format(strName, dExtTemp, crTableTimeTemp, dDcoef, crTableTimeCoeff, crTableTempCoeff, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Convection:
    def SurfaceMapping(self, strName, crlTarget, iPos, iViewCp, iCp, iSrcType, iMappedCpIndex0, iMappedCpIndex1, dRScale, posOffset, posAxis, dTScale, dSearchRange, iHTCUnit, iTempUnit, strPath, crEdit):
        message = "BoundaryConditions.Convection.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, crlTarget, iPos, iViewCp, iCp, iSrcType, iMappedCpIndex0, iMappedCpIndex1, dRScale, posOffset, posAxis, dTScale, dSearchRange, iHTCUnit, iTempUnit, strPath, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Convection = Convection()

class BoundaryConditions:
    BoundaryTemperature = BoundaryTemperature()

class BoundaryConditions:
    Convection = Convection()

class BoundaryConditions:
    EnforcedLoads = EnforcedLoads()

class EnforcedLoads:
    def Acceleration(self, strName, iDwDof, dFVel1, dFVel2, dFVel3, dFVel4, dFVel5, dFVel6, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, bExport, crMEExport1, crMEExport2, crMEExport3, crMEExport4, crMEExport5, crMEExport6, iAcUnit, iRotUnit, crlTarget, crEdit):
        message = "BoundaryConditions.EnforcedLoads.Acceleration('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDwDof, dFVel1, dFVel2, dFVel3, dFVel4, dFVel5, dFVel6, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, bExport, crMEExport1, crMEExport2, crMEExport3, crMEExport4, crMEExport5, crMEExport6, iAcUnit, iRotUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    EnforcedLoads = EnforcedLoads()

class EnforcedLoads:
    def Velocity(self, strName, iDwDof, dFVel0, dFVel1, dFVel2, dFVel3, dFVel4, dFVel5, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, iVelUnit, iRotUnit, bExport, crExportData0, crExportData1, crExportData2, crExportData3, crExportData4, crExportData5, crlTarget, crEdit, bADVCStatic):
        message = "BoundaryConditions.EnforcedLoads.Velocity('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDwDof, dFVel0, dFVel1, dFVel2, dFVel3, dFVel4, dFVel5, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, iVelUnit, iRotUnit, bExport, crExportData0, crExportData1, crExportData2, crExportData3, crExportData4, crExportData5, crlTarget, crEdit, bADVCStatic)
        return JPT_RUN_LINE(message)

class EnforcedLoads:
    def Displacement(self, strName, iDwDof, dFDisp0, dFDisp1, dFDisp2, dFDisp3, dFDisp4, dFDisp5, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, crlTarget, crEdit):
        message = "BoundaryConditions.EnforcedLoads.Displacement('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDwDof, dFDisp0, dFDisp1, dFDisp2, dFDisp3, dFDisp4, dFDisp5, crCurCoord, iEnArrowDir, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class HeatFlux:
    def SurfaceFlux(self, strName,dFflux,iDistributionMethod,crTable,crlTarget, crEdit):
        message = "BoundaryConditions.HeatFlux.SurfaceFlux('{}',{},'{}',{},{},{})".format(strName,dFflux,iDistributionMethod,crTable,crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    EnforcedLoads = EnforcedLoads()

class BoundaryConditions:
    HeatFlux = HeatFlux()

class BoundaryConditions:
    HeatFlux = HeatFlux()

class HeatFlux:
    def SurfaceMapping(self, strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strStrpath, crEdit, iMappingMethod, iSubmodeLBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet):
        message = "BoundaryConditions.HeatFlux.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strStrpath, crEdit, iMappingMethod, iSubmodeLBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    HeatFlux = HeatFlux()

class HeatFlux:
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

class BoundaryConditions:
    InitialElementalValue = InitialElementalValue()

class BoundaryConditions:
    InitialTemperature = InitialTemperature()

class InitialTemperature:
    def Constant(self, strName,dFTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.InitialTemperature.Constant('{}',{},'{}',{},{},{},{})".format(strName,dFTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    InitialTemperature = InitialTemperature()

class InitialTemperature:
    def ADVC(self, strName,fTemp, strFilePathName, bUseDefault, crTable, taTarget, crEdit):
        message = "BoundaryConditions.InitialTemperature.ADVC('{}',{},'{}',{},{},{},{})".format(strName,fTemp, strFilePathName, bUseDefault, crTable, taTarget, crEdit)
        return JPT_RUN_LINE(message)

class InitialTemperature:
    def NastranPunch(self, strName,fTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.InitialTemperature.NastranPunch('{}',{},'{}',{},{},{},{})".format(strName,fTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class LBCCopy:
    def PropertiesCopyTranslate(self, iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.PropertiesCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    InitialTemperature = InitialTemperature()

class BoundaryConditions:
    InitialTemperature = InitialTemperature()

class BoundaryConditions:
    LBCCopy = LBCCopy()

class LBCCopy:
    def PropertiesCopyRotate(self, iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.PropertiesCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    LBCCopy = LBCCopy()

class BoundaryConditions:
    LBCCopy = LBCCopy()

class LBCCopy:
    def PropertiesCopyMirror(self, iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget):
        message = "BoundaryConditions.LBCCopy.PropertiesCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

class LBCCopy:
    def ConnectionCopyTranslate(self, iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.ConnectionCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    LBCCopy = LBCCopy()

class LBCCopy:
    def ConnectionCopyRotate(self, iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.ConnectionCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

class LBCCopy:
    def ConnectionCopyMirror(self, iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget):
        message = "BoundaryConditions.LBCCopy.ConnectionCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    LBCCopy = LBCCopy()

class LBCCopy:
    def GroupCopyTranslate(self, iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.GroupCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    LBCCopy = LBCCopy()

class BoundaryConditions:
    LBCCopy = LBCCopy()

class LBCCopy:
    def GroupCopyRotate(self, iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.GroupCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    LBCCopy = LBCCopy()

class LBCCopy:
    def GroupCopyMirror(self, iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget):
        message = "BoundaryConditions.LBCCopy.GroupCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

class LBCCopy:
    def LBCCopyTranslate(self, iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.LBCCopyTranslate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posVecTrans, dMagnitude, dTrandataDoffset, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    LBCCopy = LBCCopy()

class BoundaryConditions:
    LBCCopy = LBCCopy()

class BoundaryConditions:
    LBCCopy = LBCCopy()

class LBCCopy:
    def LBCCopyRotate(self, iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget):
        message = "BoundaryConditions.LBCCopy.LBCCopyRotate({},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, posAxis, posCenter, dAngle, dTol, crCoord, crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    LBCCopy = LBCCopy()

class LBCCopy:
    def LBCCopyMirror(self, iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget):
        message = "BoundaryConditions.LBCCopy.LBCCopyMirror({},{},{},{},{},{})".format(iMethod, iMatchMethod, poslPoints, dOffset, dTol, crlTarget)
        return JPT_RUN_LINE(message)

class Pressure:
    def SurfaceLoads(self, strName, dlPressure, iArrowdir, crCoordinate, crlTargetFace, crEditCur):
        message = "BoundaryConditions.Pressure.SurfaceLoads('{}',{},{},{},{},{})".format(strName, dlPressure, iArrowdir, crCoordinate, crlTargetFace, crEditCur)
        return JPT_RUN_LINE(message)

class Pressure:
    def By2Nodes(self, strName, crNodeA, dPressureA, iNodeAUnit, crNodeB, dPressureB, iNodeBUnit, iDirection, crlTarget, crEdit):
        message = "BoundaryConditions.Pressure.By2Nodes('{}',{},{},{},{},{},{},{},{},{})".format(strName, crNodeA, dPressureA, iNodeAUnit, crNodeB, dPressureB, iNodeBUnit, iDirection, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Pressure:
    def General(self, strName, dFpressure, iIdistribute, crCrtable, dDphase, dDdelay, crPhaseTable, strFormularValue, crCrcoord, dlVdirection, strFormularDirX, strFormularDirY, strFormularDirZ, iArrowDir, crlTatarget, crCredit):
        message = "BoundaryConditions.Pressure.General('{}',{},'{}',{},{},{},{},'{}',{},{},'{}','{}','{}',{},{},{})".format(strName, dFpressure, iIdistribute, crCrtable, dDphase, dDdelay, crPhaseTable, strFormularValue, crCrcoord, dlVdirection, strFormularDirX, strFormularDirY, strFormularDirZ, iArrowDir, crlTatarget, crCredit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Pressure = Pressure()

class BoundaryConditions:
    Pressure = Pressure()

class Pressure:
    def Quadratic(self, strName, dA, dB, crCoordinate, dAngleRange, iPressureDirectionMode, dlPressureDirection, crlTargets, crEdit):
        message = "BoundaryConditions.Pressure.Quadratic('{}',{},{},{},{},{},{},{},{})".format(strName, dA, dB, crCoordinate, dAngleRange, iPressureDirectionMode, dlPressureDirection, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Pressure = Pressure()

class BoundaryConditions:
    Pressure = Pressure()

class Pressure:
    def FunctionLoadToCylinderSine(self, strName, dA, crCoordinate, dAngleRange, bDistributionAxis, iPressureDirectionMode, bIsTotalForceAdjustment, dTotalForce, vecPressureDirection, crCoordinateSystemForDirection, bIsCornerNodesDistribution, strFormulaForA, crlTargets, crEdit):
        message = "BoundaryConditions.Pressure.FunctionLoadToCylinderSine('{}',{},{},{},'{}',{},{},{},{},{},'{}','{}',{},{})".format(strName, dA, crCoordinate, dAngleRange, bDistributionAxis, iPressureDirectionMode, bIsTotalForceAdjustment, dTotalForce, vecPressureDirection, crCoordinateSystemForDirection, bIsCornerNodesDistribution, strFormulaForA, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Pressure = Pressure()

class Pressure:
    def Hydrostatic(self, strName, dFHPressure, dFDensity, iDensityUnit, dFGravity, iGravityUnit, iGravityDir, dFWaterSuface, iSufaceUnit, iEnDistrbute, crlTarget, crEdit):
        message = "BoundaryConditions.Pressure.Hydrostatic('{}',{},{},{},{},{},{},{},{},'{}',{},{})".format(strName, dFHPressure, dFDensity, iDensityUnit, dFGravity, iGravityUnit, iGravityDir, dFWaterSuface, iSufaceUnit, iEnDistrbute, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Pressure = Pressure()

class BoundaryConditions:
    Pressure = Pressure()

class BoundaryConditions:
    Submodel = Submodel()

class Pressure:
    def SurfaceMapping(self, strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strPath, crEdit):
        message = "BoundaryConditions.Pressure.SurfaceMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr, dScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, iUnit, strPath, crEdit)
        return JPT_RUN_LINE(message)

class Submodel:
    def SubmodelForcedFlux(self, strName, iSolver, strFilePathName, iProcessNo, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit):
        message = "BoundaryConditions.Submodel.SubmodelForcedFlux('{}',{},'{}',{},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(strName, iSolver, strFilePathName, iProcessNo, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Submodel:
    def ForcedTempertature(self, strName, iSolver, strFilePathName, iProcessNo, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit):
        message = "BoundaryConditions.Submodel.ForcedTempertature('{}',{},'{}',{},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(strName, iSolver, strFilePathName, iProcessNo, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Submodel:
    def ForcedDisplacement(self, strName, iSolver, strFilePathName, iProcessNo, bTranslationX, bTranslationY, bTranslationZ, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit):
        message = "BoundaryConditions.Submodel.ForcedDisplacement('{}',{},'{}',{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(strName, iSolver, strFilePathName, iProcessNo, bTranslationX, bTranslationY, bTranslationZ, iReferType, dExtensionRange, dExtensionTol, dExtensionLimitTol, strGlobalElementSet, iUseBucket, iNumBucketMaxX, iNumBucketMaxY, iNumBucketMaxZ, iPrevBc, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Submodel = Submodel()

class TemperatureLoads:
    def Constant(self, strName, dTemperature, crTable, crlTarget, crEdit, bUseDefaultTemp):
        message = "BoundaryConditions.TemperatureLoads.Constant('{}',{},{},{},{},{})".format(strName, dTemperature, crTable, crlTarget, crEdit, bUseDefaultTemp)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Submodel = Submodel()

class BoundaryConditions:
    TemperatureLoads = TemperatureLoads()

class BoundaryConditions:
    TemperatureLoads = TemperatureLoads()

class TemperatureLoads:
    def ADVCFile(self, strName, strFilePathName, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.TemperatureLoads.ADVCFile('{}','{}',{},{},{})".format(strName, strFilePathName, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class TemperatureLoads:
    def NastranPunch(self, strName, strFilePathName, crTable, crlTarget, crEdit, bUseAsMaterialReferenceTemp):
        message = "BoundaryConditions.TemperatureLoads.NastranPunch('{}','{}',{},{},{},{})".format(strName, strFilePathName, crTable, crlTarget, crEdit, bUseAsMaterialReferenceTemp)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    TemperatureLoads = TemperatureLoads()

class TemperatureLoads:
    def WholeMapping(self, strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, iMappedCpIndexArr1, iDScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet):
        message = "BoundaryConditions.TemperatureLoads.WholeMapping('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName, crlTarget, iMAPPos, iViewCp, iCp, iSrcType, iMappedCpIndexArr0, iMappedCpIndexArr1, iDScaleFactor, posOffset, posRotate, dCorScale, dSearchRange, strPath, crEdit, iMappingMethod, iSubmodelBCMappingType, iMappingFromStepNo, bSetADVCFile, strADVCResultFile, bSetDetATol, dDetATol, bSetElementSet, strElementSet)
        return JPT_RUN_LINE(message)

class TemperatureLoads:
    def LbcInitialTemperature(self, strName, iType, dFTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.TemperatureLoads.LbcInitialTemperature('{}',{},{},'{}',{},{},{},{})".format(strName, iType, dFTemp, strFilePathName, bUseDefault, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    TemperatureLoads = TemperatureLoads()

class BoundaryConditions:
    def LoadCase(strName, dFactor, crlTatarget, iExportId, dlTargetFactor, crEdit):
        message = "BoundaryConditions.LoadCase('{}',{},{},{},{},{})".format(strName, dFactor, crlTatarget, iExportId, dlTargetFactor, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    def LBCCopyMisc(iMethod, iMatchMethod, dlTransVec, dTransMag, dTransOffset, dTransTol, crTranscrCoord, dlTransaxisVec, dlTranscenterVec, dRotateAngle, dRotateTol, crRotatecrCoord, veclMirrorPoint, dMirrordOffset, dMirrorTol, crlTarget):
        message = "BoundaryConditions.LBCCopyMisc({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, iMatchMethod, dlTransVec, dTransMag, dTransOffset, dTransTol, crTranscrCoord, dlTransaxisVec, dlTranscenterVec, dRotateAngle, dRotateTol, crRotatecrCoord, veclMirrorPoint, dMirrordOffset, dMirrorTol, crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    def LbcContactConvert(iConvertTo,iTieConvType,crlTarget):
        message = "BoundaryConditions.LbcContactConvert({},{},{})".format(iConvertTo,iTieConvType,crlTarget)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    def InsideHeatGeneration(strName, dInsideFlux, crTable, crlTargets, crEdit):
        message = "BoundaryConditions.InsideHeatGeneration('{}',{},{},{},{})".format(strName, dInsideFlux, crTable, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    def FieldData(strName, iType, ilSheet, crEdit, bAbaqusAmp, iAmpType):
        message = "BoundaryConditions.FieldData('{}',{},{},{},{},{})".format(strName, iType, ilSheet, crEdit, bAbaqusAmp, iAmpType)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    def FixedConstraint(strName, iDwDof, crCurCoord, iType, iUsetType, crTable, bAbaqusFixed, crlTarget, crEdit):
        message = "BoundaryConditions.FixedConstraint('{}',{},{},{},{},{},{},{},{})".format(strName, iDwDof, crCurCoord, iType, iUsetType, crTable, bAbaqusFixed, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    def DofSet(strName, iDwDof, crCurCoord, crTable, crlTarget, crEdit):
        message = "BoundaryConditions.DofSet('{}',{},{},{},{},{})".format(strName, iDwDof, crCurCoord, crTable, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class CentrifugalForce:
    def CoordinateSystems(self, strName, dFVelocity, dFAcceleration, iAxisDirection, iVelocityUnit, iAccelerationUnit, crCurCoord, crlTarget, crEdit):
        message = "BoundaryConditions.BodyLoads.CentrifugalForce.CoordinateSystems('{}',{},{},{},{},{},{},{},{})".format(strName, dFVelocity, dFAcceleration, iAxisDirection, iVelocityUnit, iAccelerationUnit, crCurCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BodyLoads:
    CentrifugalForce = CentrifugalForce()

class BoundaryConditions:
    TemperatureLoads = TemperatureLoads()

class CentrifugalForce:
    def TwoPositions(self, strName, dFBasePoint1, dFBasePoint2, dFBasePoint3, dFTipPoint1, dFTipPoint2, dFTipPoint3, dFVelocity, dFAcceleration, iVelocityUnit, iAccelerationUnit, crlTarget, crEdit):
        message = "BoundaryConditions.BodyLoads.CentrifugalForce.TwoPositions('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dFBasePoint1, dFBasePoint2, dFBasePoint3, dFTipPoint1, dFTipPoint2, dFTipPoint3, dFVelocity, dFAcceleration, iVelocityUnit, iAccelerationUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    BodyLoads = BodyLoads()

class BoundaryConditions:
    BodyLoads = BodyLoads()

class BodyLoads:
    CentrifugalForce = CentrifugalForce()

class BodyLoads:
    def Gravity(self, strName,dlGravity, crCurCoord, crlTarget, crEdit):
        message = "BoundaryConditions.BodyLoads.Gravity('{}',{},{},{},{})".format(strName,dlGravity, crCurCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class FunctionLoadCylinder:
    def Quadratic(self, strName, dFTotalForce, dA, dB, crCoord, iAngleBase, dAngleRange, iEnArrowDir, crlTargets, crEdit):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.Quadratic('{}',{},{},{},{},{},{},{},{},{})".format(strName, dFTotalForce, dA, dB, crCoord, iAngleBase, dAngleRange, iEnArrowDir, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    BodyLoads = BodyLoads()

class Force:
    FunctionLoadCylinder = FunctionLoadCylinder()

class Force:
    FunctionLoadCylinder = FunctionLoadCylinder()

class FunctionLoadCylinder:
    def Sine(self, strName, dFTotalForce, dA, crCoord, iAngleBase, dAngleRange, iEnArrowDir, bDistributeInAxis, crlTarget, crEdit):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.Sine('{}',{},{},{},{},{},{},'{}',{},{})".format(strName, dFTotalForce, dA, crCoord, iAngleBase, dAngleRange, iEnArrowDir, bDistributeInAxis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Force = Force()

class FunctionLoadCylinder:
    def Vector(self, strName, dFTotalForce, dA, dX, dY, crCoord, iEnDirection, dAngleRange, iArrowDir, bDistributeInAxis, crlTarget, crEdit):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.Vector('{}',{},{},{},{},{},{},{},{},'{}',{},{})".format(strName, dFTotalForce, dA, dX, dY, crCoord, iEnDirection, dAngleRange, iArrowDir, bDistributeInAxis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Force = Force()

class BoundaryConditions:
    Force = Force()

class Force:
    FunctionLoadCylinder = FunctionLoadCylinder()

class NonlinearForce:
    def NOLIN3(self, strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit):
        message = "BoundaryConditions.Force.NonlinearForce.NOLIN3('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

class NonlinearForce:
    def NOLIN4(self, strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit):
        message = "BoundaryConditions.Force.NonlinearForce.NOLIN4('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

class Force:
    NonlinearForce = NonlinearForce()

class Force:
    NonlinearForce = NonlinearForce()

class BoundaryConditions:
    Force = Force()

class NonlinearForce:
    def NOLIN1(self, strName, dForceScale, dMomentScale, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCoord, crForceTable, crMomentTable, crlVcrMaster, crlVcrSlave, crEdit):
        message = "BoundaryConditions.Force.NonlinearForce.NOLIN1('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCoord, crForceTable, crMomentTable, crlVcrMaster, crlVcrSlave, crEdit)
        return JPT_RUN_LINE(message)

class Force:
    NonlinearForce = NonlinearForce()

class BoundaryConditions:
    Force = Force()

class Force:
    def General(self, strName, vecForce, vecMoment, iEnArrowDir, iEnDistrbute, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, strFormula6, crlTarget, crEdit):
        message = "BoundaryConditions.Force.General('{}',{},{},{},'{}',{},{},{},{},{},{},'{}','{}','{}','{}','{}','{}',{},{})".format(strName, vecForce, vecMoment, iEnArrowDir, iEnDistrbute, crCurCoord, crTable, crNodeSet, dFPhase, dFDelay, crPhaseTable, strFormula1, strFormula2, strFormula3, strFormula4, strFormula5, strFormula6, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Force = Force()

class BoundaryConditions:
    Force = Force()

class Force:
    def ForceNormalDirection(self, strName, vecForce, iEnArrowDir, iEnDistrbute, crCurCoord, crlTarget, crEdit):
        message = "BoundaryConditions.Force.ForceNormalDirection('{}',{},{},'{}',{},{},{})".format(strName, vecForce, iEnArrowDir, iEnDistrbute, crCurCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class InitialNodalValue:
    InitialAngularVelocity = InitialAngularVelocity()

class InitialAngularVelocity:
    def Abaqus(self, strName, dVelocity, strFirstCoord, strSecondCoord, crlTargets, crEdit):
        message = "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.Abaqus('{}',{},'{}','{}',{},{})".format(strName, dVelocity, strFirstCoord, strSecondCoord, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    Force = Force()

class BoundaryConditions:
    InitialNodalValue = InitialNodalValue()

class InitialAngularVelocity:
    def General(self, strName, stData, crlTarget, crEdit):
        message = "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.General('{}',{},{},{})".format(strName, stData, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class InitialNodalValue:
    InitialAngularVelocity = InitialAngularVelocity()

class InitialNodalValue:
    def Displacement(self, strName, iType, vecInit, bSelNode, crNodeSet, crTable, crCoord, crlTarget, crEdit):
        message = "BoundaryConditions.InitialNodalValue.Displacement('{}',{},{},{},{},{},{},{},{})".format(strName, iType, vecInit, bSelNode, crNodeSet, crTable, crCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class InitialNodalValue:
    def Velocity(self, strName, stData, crlTarget, crEdit):
        message = "BoundaryConditions.InitialNodalValue.Velocity('{}',{},{},{})".format(strName, stData, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class BoundaryConditions:
    InitialNodalValue = InitialNodalValue()

class BoundaryConditions:
    InitialNodalValue = InitialNodalValue()

class BoundaryConditions:
    InitialNodalValue = InitialNodalValue()

class BoundaryConditions:
    InitialNodalValue = InitialNodalValue()

class InitialNodalValue:
    def RotationAngle(self, strName, stData, taTarget, crEdit):
        message = "BoundaryConditions.InitialNodalValue.RotationAngle('{}',{},{},{})".format(strName, stData, taTarget, crEdit)
        return JPT_RUN_LINE(message)

class Pretension:
    def General(self, strName, iDir, dValue, bFixLength, crTable, crCoord, iLocalUnit, crlTarget, crEdit, bCreate2ADVCStatic):
        message = "Connections.Pretension.General('{}',{},{},{},{},{},{},{},{},{})".format(strName, iDir, dValue, bFixLength, crTable, crCoord, iLocalUnit, crlTarget, crEdit, bCreate2ADVCStatic)
        return JPT_RUN_LINE(message)

class Pretension:
    def Abaqus(self, strName, bFixedLenght, crTable, dValue, iLocalUnit, strNormal, dlNodePos, crEdit, crlTarget):
        message = "Connections.Pretension.Abaqus('{}',{},{},{},{},'{}',{},{},{})".format(strName, bFixedLenght, crTable, dValue, iLocalUnit, strNormal, dlNodePos, crEdit, crlTarget)
        return JPT_RUN_LINE(message)

class Connections:
    Pretension = Pretension()

class Pretension:
    def Advc(self, strName, bFixedLength, crEnforcedVelocity, dDvalue, iDirUpdateType, dlVnormal, dlCtrolNodePos, iRefNodeId, crEdit, crlTarget):
        message = "Connections.Pretension.Advc('{}',{},{},{},{},{},{},{},{},{})".format(strName, bFixedLength, crEnforcedVelocity, dDvalue, iDirUpdateType, dlVnormal, dlCtrolNodePos, iRefNodeId, crEdit, crlTarget)
        return JPT_RUN_LINE(message)

class Connections:
    Pretension = Pretension()

class Connections:
    def MassElements(strName,crlTarget, dMass, iDof, bDesigner, crCoordinate, dOffset0, dOffset1, dOffset2, dInertia0, dInertia1, dInertia2, dInertia3, dInertia4, dInertia5, crEdit, bUpdateDispCS):
        message = "Connections.MassElements('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName,crlTarget, dMass, iDof, bDesigner, crCoordinate, dOffset0, dOffset1, dOffset2, dInertia0, dInertia1, dInertia2, dInertia3, dInertia4, dInertia5, crEdit, bUpdateDispCS)
        return JPT_RUN_LINE(message)

class Connections:
    def BarBeam(strName, iEType, iMethod, crProp, dlOrient, crlMasterTarget, crlSlaveTarget):
        message = "Connections.BarBeam('{}',{},{},{},{},{},{})".format(strName, iEType, iMethod, crProp, dlOrient, crlMasterTarget, crlSlaveTarget)
        return JPT_RUN_LINE(message)

class Connections:
    def GapsDetail(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur):
        message = "Connections.GapsDetail({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

class Connections:
    def Plot(strName, iPID, crlTarget, crEdit):
        message = "Connections.Plot('{}',{},{},{})".format(strName, iPID, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    def CreateConnConm(strName,iEType,iMethod,iCoordSys,iConmId,crMatCoord,dMass, dlX, dlVintertia0, dlVintertia1):
        message = "Connections.CreateConnConm('{}',{},{},{},{},{},{},{},{},{})".format(strName,iEType,iMethod,iCoordSys,iConmId,crMatCoord,dMass, dlX, dlVintertia0, dlVintertia1)
        return JPT_RUN_LINE(message)

class Connections:
    def RBE3(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly):
        message = "Connections.RBE3({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly)
        return JPT_RUN_LINE(message)

class Connections:
    def RigidWall(strName, iObject, iType, iMotion, iFriction, iOrtho, iForces, dFinite1, dFinite2, dMotionMass, dMotionInitVelo, dFricCoulombCoeff, dFricWeldVelo, iForcesCirclesNum, dOrthoStaticCoeff1, dOrthoStaticCoeff2, dOrthoDynamicCoeff1, dOrthoDynamicCoeff2, dOrthoDecayConst1, dOrthoDecayConst2, dOrthoFricVector1, dOrthoFricVector2, dOrthoFricVector3, bAllNodeSlave, crCoord, crAreaFaceSet, crVisualNodeSet, crlTarget, crEdit):
        message = "Connections.RigidWall('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iObject, iType, iMotion, iFriction, iOrtho, iForces, dFinite1, dFinite2, dMotionMass, dMotionInitVelo, dFricCoulombCoeff, dFricWeldVelo, iForcesCirclesNum, dOrthoStaticCoeff1, dOrthoStaticCoeff2, dOrthoDynamicCoeff1, dOrthoDynamicCoeff2, dOrthoDecayConst1, dOrthoDecayConst2, dOrthoFricVector1, dOrthoFricVector2, dOrthoFricVector3, bAllNodeSlave, crCoord, crAreaFaceSet, crVisualNodeSet, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    def Connector(strName, iMethod, iConnectType, iRefNode, iElemCs, crLocalCS, crlElasticity, crlDamp, crlMasterTarget, crlSlaveTarget, crEdit):
        message = "Connections.Connector('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, iMethod, iConnectType, iRefNode, iElemCs, crLocalCS, crlElasticity, crlDamp, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    def BoltMeshingSplitOnly(strName, iPartcutparamImethod, dPartcutparamDoffset, iPartcutparamBshareface, iPartcutparamBseparateface, iPartcutparamBsplitonly, iPartcutparamBmakesectionface, crPartcutparamCoord, surfaceMesh, bLBCPRETENSIONABAQUSDATABfixedlenght, crLBCPRETENSIONABAQUSDATACrtable, dLBCPRETENSIONABAQUSDATADvalue, iLBCPRETENSIONABAQUSDATAIlocalunit, strLBCPRETENSIONABAQUSDATAStrnormal, posLBCPRETENSIONABAQUSDATATvctrolnodepos, crlTarget, poslCutter):
        message = "Connections.BoltMeshingSplitOnly('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iPartcutparamImethod, dPartcutparamDoffset, iPartcutparamBshareface, iPartcutparamBseparateface, iPartcutparamBsplitonly, iPartcutparamBmakesectionface, crPartcutparamCoord, surfaceMesh, bLBCPRETENSIONABAQUSDATABfixedlenght, crLBCPRETENSIONABAQUSDATACrtable, dLBCPRETENSIONABAQUSDATADvalue, iLBCPRETENSIONABAQUSDATAIlocalunit, strLBCPRETENSIONABAQUSDATAStrnormal, posLBCPRETENSIONABAQUSDATATvctrolnodepos, crlTarget, poslCutter)
        return JPT_RUN_LINE(message)

class Connections:
    def BoltMeshingNotSplitOnly(strName, iPartcutparamImethod, dPartcutparamDoffset, iPartcutparamBshareface, iPartcutparamBseparateface, iPartcutparamBsplitonly, iPartcutparamBmakesectionface, crPartcutparamCoord, surfaceMesh, iLBCPRETENSIONDATAIdir, dLBCPRETENSIONDATADvalue, bLBCPRETENSIONDATABfixlength, crLBCPRETENSIONDATACrtable, crLBCPRETENSIONDATACrcoord, iLBCPRETENSIONDATAIlocalunit, crlTarget, poslCutter):
        message = "Connections.BoltMeshingNotSplitOnly('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPartcutparamImethod, dPartcutparamDoffset, iPartcutparamBshareface, iPartcutparamBseparateface, iPartcutparamBsplitonly, iPartcutparamBmakesectionface, crPartcutparamCoord, surfaceMesh, iLBCPRETENSIONDATAIdir, dLBCPRETENSIONDATADvalue, bLBCPRETENSIONDATABfixlength, crLBCPRETENSIONDATACrtable, crLBCPRETENSIONDATACrcoord, iLBCPRETENSIONDATAIlocalunit, crlTarget, poslCutter)
        return JPT_RUN_LINE(message)

class Connections:
    Pretension = Pretension()

class Edge:
    def TypeC(self, crlEdgeCur1,crlEdgeCur2, strRbeName, dPlaneTol, dMaxBoltHeight, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth):
        message = "Connections.BoltConnections.Edge.TypeC({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1,crlEdgeCur2, strRbeName, dPlaneTol, dMaxBoltHeight, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth)
        return JPT_RUN_LINE(message)

class BoltConnections:
    Edge = Edge()

class Connections:
    BoltConnections = BoltConnections()

class Edge:
    def TypeB(self, crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, bIfCreate2ADVCStaticProcessForBoltFixLength):
        message = "Connections.BoltConnections.Edge.TypeB({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, bIfCreate2ADVCStaticProcessForBoltFixLength)
        return JPT_RUN_LINE(message)

class Edge:
    def TypeD(self, crlEdgeCur1,crlEdgeCur2, strMpcName, dConnRadius, dPlaneTol):
        message = "Connections.BoltConnections.Edge.TypeD({},{},'{}',{},{})".format(crlEdgeCur1,crlEdgeCur2, strMpcName, dConnRadius, dPlaneTol)
        return JPT_RUN_LINE(message)

class BoltConnections:
    Edge = Edge()

class Connections:
    BoltConnections = BoltConnections()

class Connections:
    BoltConnections = BoltConnections()

class BoltConnections:
    Edge = Edge()

class Edge:
    def TypeA(self, crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, bIsCreate2ADVCStaticProcessForFixLength):
        message = "Connections.BoltConnections.Edge.TypeA({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, bIsCreate2ADVCStaticProcessForFixLength)
        return JPT_RUN_LINE(message)

class Connections:
    BoltConnections = BoltConnections()

class BoltConnections:
    Edge = Edge()

class Connections:
    BoltConnections = BoltConnections()

class Face:
    def TypeC(self, crlFaceCur1,crlFaceCur2, strRbeName, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth):
        message = "Connections.BoltConnections.Face.TypeC({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1,crlFaceCur2, strRbeName, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth)
        return JPT_RUN_LINE(message)

class Face:
    def TypeB(self, crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, dScale1, bIsCreate2ADVCStaticProcessForFixLength):
        message = "Connections.BoltConnections.Face.TypeB({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, dScale1, bIsCreate2ADVCStaticProcessForFixLength)
        return JPT_RUN_LINE(message)

class BoltConnections:
    Face = Face()

class Connections:
    BoltConnections = BoltConnections()

class BoltConnections:
    Face = Face()

class Face:
    def TypeA(self, crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, dScale1, bIfCreate2ADVCStaticProcessForBoltFixLength):
        message = "Connections.BoltConnections.Face.TypeA({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, dScale1, bIfCreate2ADVCStaticProcessForBoltFixLength)
        return JPT_RUN_LINE(message)

class Connections:
    BoltConnections = BoltConnections()

class Abaqus:
    def ContactTable(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class BoltConnections:
    Face = Face()

class Connections:
    Contacts = Contacts()

class Abaqus:
    def ManualGroup(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.ManualGroup('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Contacts:
    Abaqus = Abaqus()

class Connections:
    Contacts = Contacts()

class Contacts:
    Abaqus = Abaqus()

class Contacts:
    Abaqus = Abaqus()

class Abaqus:
    def ManualFace(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.ManualFace('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Abaqus:
    def ContactGroupByMatrix(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.ContactGroupByMatrix('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Connections:
    Contacts = Contacts()

class Abaqus:
    def ContactShareFace(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.ContactShareFace('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Contacts:
    Abaqus = Abaqus()

class Connections:
    Contacts = Contacts()

class ADVC:
    def ContactClearance(self, strName,dClearanceVal,iLocalUnit,iSolverType,crlTarget, crEdit):
        message = "Connections.Contacts.ADVC.ContactClearance('{}',{},{},{},{},{})".format(strName,dClearanceVal,iLocalUnit,iSolverType,crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Contacts:
    Abaqus = Abaqus()

class Contacts:
    ADVC = ADVC()

class Connections:
    Contacts = Contacts()

class ADVC:
    def ManualGroup(self, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.ManualGroup('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

class ADVC:
    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.ManualFace({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

class Contacts:
    ADVC = ADVC()

class Connections:
    Contacts = Contacts()

class Contacts:
    ADVC = ADVC()

class Connections:
    Contacts = Contacts()

class ADVC:
    def Contact(self, strName, iType, slidingType, InitialState, initialStateTol, kineticFrictionCoef, exponentialCoef, Behavior, Clearance, adjust2Clearance, interference, adjust2Interference, autoShrink, badvAdjust, adjustValue, FrictionCoef, MaxShear, elastic_slip, slip_tolerance, searchWidth, SearchGap, searchDepth, critialPenetration, estimation_impact_time, formula, constraintType, iDataType, TypeId, btemperatureDependency, idependencies, table, stabilized, type, residual_factor, effective_dist, cn, ct, taCClearance, taTarget, crEdit, searchAngle, constraintType_explicit, penaltyFact, penaltyFactExplicit, Color, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.Contact('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iType, slidingType, InitialState, initialStateTol, kineticFrictionCoef, exponentialCoef, Behavior, Clearance, adjust2Clearance, interference, adjust2Interference, autoShrink, badvAdjust, adjustValue, FrictionCoef, MaxShear, elastic_slip, slip_tolerance, searchWidth, SearchGap, searchDepth, critialPenetration, estimation_impact_time, formula, constraintType, iDataType, TypeId, btemperatureDependency, idependencies, table, stabilized, type, residual_factor, effective_dist, cn, ct, taCClearance, taTarget, crEdit, searchAngle, constraintType_explicit, penaltyFact, penaltyFactExplicit, Color, iAlg, iMethod)
        return JPT_RUN_LINE(message)

class Contacts:
    ADVC = ADVC()

class Connections:
    Contacts = Contacts()

class ADVC:
    def ContactShareFace(self, crlShareFace, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.ContactShareFace({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(crlShareFace, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

class Contacts:
    ADVC = ADVC()

class Connections:
    Contacts = Contacts()

class ADVC:
    def ContactTable(self, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

class Contacts:
    ADVC = ADVC()

class Connections:
    Contacts = Contacts()

class ADVC:
    def ContactGroupByMatrix(self, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.ContactGroupByMatrix('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

class Contacts:
    ADVC = ADVC()

class Connections:
    Contacts = Contacts()

class Ansys:
    def ManualGroup(self, strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Ansys.ManualGroup('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Contacts:
    Ansys = Ansys()

class Ansys:
    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor):
        message = "Connections.Contacts.Ansys.ManualFace({},{},'{}',{},{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Contacts:
    Ansys = Ansys()

class Connections:
    Contacts = Contacts()

class Ansys:
    def ContactGroupByMatrix(self, strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Ansys.ContactGroupByMatrix('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Contacts:
    Ansys = Ansys()

class Ansys:
    def ContactShareFace(self, crlShareFace, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor):
        message = "Connections.Contacts.Ansys.ContactShareFace({},'{}',{},{},{},{},{},{})".format(crlShareFace, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Contacts:
    Ansys = Ansys()

class Connections:
    Contacts = Contacts()

class Ansys:
    def ContactTable(self, strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Ansys.ContactTable('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class Contacts:
    MSCNastran = MSCNastran()

class Contacts:
    Ansys = Ansys()

class Connections:
    Contacts = Contacts()

class MSCNastran:
    def ManualGroup(self, strName, tssolverContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class MSCNastran:
    def ContactGroupByMatrix(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.ContactGroupByMatrix('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Contacts:
    MSCNastran = MSCNastran()

class Connections:
    Contacts = Contacts()

class Contacts:
    MSCNastran = MSCNastran()

class MSCNastran:
    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.ManualFace({},{},'{}','{}',{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class MSCNastran:
    def ContactShareFace(self, crlShareFace, strName, nastranContact, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.ContactShareFace({},'{}','{}',{},{},{})".format(crlShareFace, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Contacts:
    MSCNastran = MSCNastran()

class Connections:
    Contacts = Contacts()

class MSCNastran:
    def ContactTable(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.ContactTable('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Contacts:
    MSCNastran = MSCNastran()

class NXNastran:
    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.ManualFace({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Contacts:
    NXNastran = NXNastran()

class Connections:
    Contacts = Contacts()

class NXNastran:
    def ContactShareFace(self, crlShareFace, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.ContactShareFace({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlShareFace, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

class Contacts:
    NXNastran = NXNastran()

class Connections:
    Contacts = Contacts()

class NXNastran:
    def ContactTable(self, strName, iType, iAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, crplTargetPair, crEdit, iColor, iMethod):
        message = "Connections.Contacts.NXNastran.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iType, iAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, crplTargetPair, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Contacts:
    NXNastran = NXNastran()

class NXNastran:
    def ManualGroup(self, crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.ManualGroup({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Connections:
    Contacts = Contacts()

class Contacts:
    NXNastran = NXNastran()

class Contacts:
    NXNastran = NXNastran()

class NXNastran:
    def ContactGroupByMatrix(self, crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.ContactGroupByMatrix({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Contacts:
    TSSolver = TSSolver()

class TSSolver:
    def ManualFace(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSolver.ManualFace('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class TSSolver:
    def Auto(self, strlNames,crllMasterFaceTargets,crllSlaveFaceTargets, crlContactTypes, dlTaInterferenceClosures, dlTaFrictionCoefficients, blTaInitialAdjustments, crlColors, crlCrEdit, crlCrMasterGroup, crlCrSlaveGroup):
        message = "Connections.Contacts.TSSolver.Auto('{}',{},{},{},{},{},{},{},{},{},{})".format(strlNames,crllMasterFaceTargets,crllSlaveFaceTargets, crlContactTypes, dlTaInterferenceClosures, dlTaFrictionCoefficients, blTaInitialAdjustments, crlColors, crlCrEdit, crlCrMasterGroup, crlCrSlaveGroup)
        return JPT_RUN_LINE(message)

class Contacts:
    TSSolver = TSSolver()

class Connections:
    Contacts = Contacts()

class TSSolver:
    def ManualGroup(self, strName, tssolverContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSolver.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Contacts:
    TSSolver = TSSolver()

class Contacts:
    TSSS = TSSS()

class TSSS:
    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSS.ManualFace({},{},'{}','{}',{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Contacts:
    TSSS = TSSS()

class Connections:
    Contacts = Contacts()

class TSSS:
    def ManualGroup(self, strName, tssolverContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSS.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class TSSS:
    def ContactTable(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSS.ContactTable('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Connections:
    Contacts = Contacts()

class Contacts:
    TSSS = TSSS()

class Contacts:
    def CheckPattern(self, crlParts, bShowMismatch, bShowMatch, dTol):
        message = "Connections.Contacts.CheckPattern({},{},{},{})".format(crlParts, bShowMismatch, bShowMatch, dTol)
        return JPT_RUN_LINE(message)

class Contacts:
    def NXNastranGeneral(self, strName, iPiType, iPiAlg, dPdNorPenFactor, dPdTanPenFactor, dPdForceConTol, dPdMaxForceIter, dPdMaxStaIter, dPdChangeNum, dPdMinContactPer, iPiShellThickness, iPiContactStatus, iPiInitGapPenetra, iPiRegionRefine, iPiEvaluPts, dPdMinSearDist, dPdMaxSearDist, dPdFricCoef, dPdSearchDist, dPdPenatlyFactor, iPiShellOffset, crlTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.NXNastranGeneral('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPiType, iPiAlg, dPdNorPenFactor, dPdTanPenFactor, dPdForceConTol, dPdMaxForceIter, dPdMaxStaIter, dPdChangeNum, dPdMinContactPer, iPiShellThickness, iPiContactStatus, iPiInitGapPenetra, iPiRegionRefine, iPiEvaluPts, dPdMinSearDist, dPdMaxSearDist, dPdFricCoef, dPdSearchDist, dPdPenatlyFactor, iPiShellOffset, crlTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Contacts:
    def ExportCheckReport(self, strFullPath, dZoomFactor, iFitBy, iListBy, iListOrder, iFormat):
        message = "Connections.Contacts.ExportCheckReport('{}',{},{},{},{},{})".format(strFullPath, dZoomFactor, iFitBy, iListBy, iListOrder, iFormat)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Gaps:
    def TwoNodes(self, crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur):
        message = "Connections.Gaps.TwoNodes({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

class Connections:
    Contacts = Contacts()

class Connections:
    Gaps = Gaps()

class Gaps:
    def TwoEdges(self, crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur):
        message = "Connections.Gaps.TwoEdges({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

class Connections:
    Gaps = Gaps()

class Gaps:
    def TwoFaces(self, crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur):
        message = "Connections.Gaps.TwoFaces({},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlMaster, crlSlave, iMethod, iOriMode, crCoord, strName, dU0, dF0, dKa, dKb, dKt, dMar, dMu1, dMu2, dlOriVec, dTmax, dTol, dTrmin, crEditCur)
        return JPT_RUN_LINE(message)

class Connections:
    MPC = MPC()

class Connections:
    Gaps = Gaps()

class Equation:
    def MultiNodes(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.Equation.MultiNodes('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class MPC:
    Equation = Equation()

class Equation:
    def TwoFace(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.Equation.TwoFace('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class MPC:
    Equation = Equation()

class Equation:
    def SemiAuto(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.Equation.SemiAuto('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    MPC = MPC()

class MPC:
    Equation = Equation()

class General:
    def NodeToNode(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodeToNode('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class MPC:
    General = General()

class General:
    def NodeToEdges(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodeToEdges('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    MPC = MPC()

class Connections:
    MPC = MPC()

class MPC:
    General = General()

class Connections:
    MPC = MPC()

class General:
    def NodeToFaces(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodeToFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class MPC:
    General = General()

class General:
    def TwoEdges(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.TwoEdges('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    MPC = MPC()

class Connections:
    MPC = MPC()

class General:
    def FacesToFaces(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.FacesToFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class MPC:
    General = General()

class MPC:
    General = General()

class Connections:
    MPC = MPC()

class General:
    def NodesToNodes(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodesToNodes('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class MPC:
    General = General()

class General:
    def TwoFaces(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.TwoFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class MPC:
    General = General()

class General:
    def NodeToAny(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodeToAny('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    MPC = MPC()

class MPC:
    General = General()

class Connections:
    MPC = MPC()

class Connections:
    MPC = MPC()

class General:
    def NodesWithTolerance(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.NodesWithTolerance('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class MPC:
    General = General()

class Connections:
    MPC = MPC()

class RBar:
    def OneToOne(self, strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBar.OneToOne('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

class RigidElements:
    RBar = RBar()

class RBar:
    def OneToMany(self, strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBar.OneToMany('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    RigidElements = RigidElements()

class Connections:
    RigidElements = RigidElements()

class RBar:
    def OneToOneNodesWithTolerance(self, strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBar.OneToOneNodesWithTolerance('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

class RigidElements:
    RBar = RBar()

class Connections:
    RigidElements = RigidElements()

class RBE2:
    def OneToMany(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.OneToMany({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

class RigidElements:
    RBE2 = RBE2()

class Connections:
    RigidElements = RigidElements()

class RigidElements:
    RBar = RBar()

class RigidElements:
    RBE2 = RBE2()

class RBE2:
    def OneToOne(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.OneToOne({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

class Connections:
    RigidElements = RigidElements()

class RBE2:
    def OneToOneNodesWithTolerance(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.OneToOneNodesWithTolerance({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

class Connections:
    RigidElements = RigidElements()

class RigidElements:
    RBE2 = RBE2()

class RBE2:
    def ToCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.ToCenter({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

class RBE2:
    def ToCircleCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.ToCircleCenter({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

class RigidElements:
    RBE2 = RBE2()

class Connections:
    RigidElements = RigidElements()

class RigidElements:
    RBE2 = RBE2()

class RBE3:
    def OneToMany(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.OneToMany({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

class Connections:
    RigidElements = RigidElements()

class RBE3:
    def OneToOne(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.OneToOne({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

class RigidElements:
    RBE3 = RBE3()

class Connections:
    RigidElements = RigidElements()

class Connections:
    RigidElements = RigidElements()

class RigidElements:
    RBE3 = RBE3()

class RBE3:
    def ToCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.ToCenter({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

class RigidElements:
    RBE3 = RBE3()

class Connections:
    RigidElements = RigidElements()

class RBE3:
    def ToCircleCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.ToCircleCenter({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

class RigidElements:
    RBE3 = RBE3()

class RigidElements:
    def RBarGeneral(self, rbarConnection, crlMasterTarget, crlSlaveTarget, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBarGeneral({},{},{},{},{},{},{})".format(rbarConnection, crlMasterTarget, crlSlaveTarget, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

class RigidElements:
    def RBE2General(self, iMethod,crlMasterTarget,crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iDuplicateMode):
        message = "Connections.RigidElements.RBE2General({},{},{},{},'{}',{},{},{},{},{},{},{},{},{})".format(iMethod,crlMasterTarget,crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iDuplicateMode)
        return JPT_RUN_LINE(message)

class Connections:
    RigidElements = RigidElements()

class Connections:
    RigidElements = RigidElements()

class Connections:
    RigidElements = RigidElements()

class RigidElements:
    def RBE3General(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly):
        message = "Connections.RigidElements.RBE3General({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly)
        return JPT_RUN_LINE(message)

class Damper:
    def AnyEntities11DoFS(self, iMethod,strName,crlMasterTarget,crlSlaveTarget, crCoordSys, iGround, dTolerance, vecTDamper, vecRDamper, crEdit, bUpdateDispCS):
        message = "Connections.SpringsDampers.Damper.AnyEntities11DoFS({},'{}',{},{},{},{},{},{},{},{},{})".format(iMethod,strName,crlMasterTarget,crlSlaveTarget, crCoordSys, iGround, dTolerance, vecTDamper, vecRDamper, crEdit, bUpdateDispCS)
        return JPT_RUN_LINE(message)

class Connections:
    RigidElements = RigidElements()

class Connections:
    SpringsDampers = SpringsDampers()

class SpringsDampers:
    def BushGeneral(self, iMethod,strName,crlMaster,crlSlave,crCoord,dTol,iGround,iOriMode,iEqual,poslVector,dlStiffness,dlDampCoef,dlDampConst,dRotStrain,dTransStrain,dRotStress,dTransStress,crEditObj):
        message = "Connections.SpringsDampers.BushGeneral({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod,strName,crlMaster,crlSlave,crCoord,dTol,iGround,iOriMode,iEqual,poslVector,dlStiffness,dlDampCoef,dlDampConst,dRotStrain,dTransStrain,dRotStress,dTransStress,crEditObj)
        return JPT_RUN_LINE(message)

class SpringsDampers:
    Damper = Damper()

class Bush:
    def TwoNodes(self, iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj):
        message = "Connections.SpringsDampers.Bush.TwoNodes({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

class Connections:
    SpringsDampers = SpringsDampers()

class Connections:
    SpringsDampers = SpringsDampers()

class SpringsDampers:
    Bush = Bush()

class Bush:
    def AnyEntities(self, iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj):
        message = "Connections.SpringsDampers.Bush.AnyEntities({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

class Connections:
    SpringsDampers = SpringsDampers()

class Bush:
    def OnetoOne(self, iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj):
        message = "Connections.SpringsDampers.Bush.OnetoOne({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

class SpringsDampers:
    Bush = Bush()

class Connections:
    SpringsDampers = SpringsDampers()

class Spring:
    def GroundedSpring(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.GroundedSpring({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class SpringsDampers:
    Bush = Bush()

class SpringsDampers:
    Spring = Spring()

class Nodeswithtolerance:
    def sameDoFs(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.Nodeswithtolerance.sameDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    SpringsDampers = SpringsDampers()

class Connections:
    SpringsDampers = SpringsDampers()

class Spring:
    Nodeswithtolerance = Nodeswithtolerance()

class Nodeswithtolerance:
    def differentDoFs(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.Nodeswithtolerance.differentDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class Spring:
    Nodeswithtolerance = Nodeswithtolerance()

class SpringsDampers:
    Spring = Spring()

class SpringsDampers:
    Spring = Spring()

class Connections:
    SpringsDampers = SpringsDampers()

class OneToOne:
    def sameDoFs(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.OneToOne.sameDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class Connections:
    SpringsDampers = SpringsDampers()

class Spring:
    OneToOne = OneToOne()

class SpringsDampers:
    Spring = Spring()

class Connections:
    SpringsDampers = SpringsDampers()

class OneToOne:
    def differentDoFs(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.OneToOne.differentDoFs({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class EngReliability:
    def SubModelBC(strName,crlTarget,iPos,iViewCp,iCp,iSrcType,iMappedCpIndexArr0,dScaleR,vecOffset,vecRotate,dScaleT,strPath,crEdit,iMappingMethod,iSubmodelBCMappingType,iMappingFromStepNo,bSetADVCFile,strADVCResultFile,bSetDetATol,dDetATol,bSetElementSet,strElementSet):
        message = "EngReliability.SubModelBC('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},'{}',{},{},{},'{}')".format(strName,crlTarget,iPos,iViewCp,iCp,iSrcType,iMappedCpIndexArr0,dScaleR,vecOffset,vecRotate,dScaleT,strPath,crEdit,iMappingMethod,iSubmodelBCMappingType,iMappingFromStepNo,bSetADVCFile,strADVCResultFile,bSetDetATol,dDetATol,bSetElementSet,strElementSet)
        return JPT_RUN_LINE(message)

class SpringsDampers:
    Spring = Spring()

class SZ:
    def WeldLine2(self, crlFaces,crlParts,dLayerWidth,iLayerNumber):
        message = "ExManifoldModeling.SZ.WeldLine2({},{},{},{})".format(crlFaces,crlParts,dLayerWidth,iLayerNumber)
        return JPT_RUN_LINE(message)

class ExManifoldModeling:
    SZ = SZ()

class Spring:
    OneToOne = OneToOne()

class Bar:
    def TwoNodes(self, strPartName, iMeshCount, crStartNode, crEndNode):
        message = "Geometry.Bar.TwoNodes('{}',{},{},{})".format(strPartName, iMeshCount, crStartNode, crEndNode)
        return JPT_RUN_LINE(message)

class Geometry:
    Bar = Bar()

class Bar:
    def Arc(self, crlVcrNode, crPart, strBarName):
        message = "Geometry.Bar.Arc({},{},'{}')".format(crlVcrNode, crPart, strBarName)
        return JPT_RUN_LINE(message)

class Bar:
    def Spline(self, crlVcrNode, crPart, strBarName):
        message = "Geometry.Bar.Spline({},{},'{}')".format(crlVcrNode, crPart, strBarName)
        return JPT_RUN_LINE(message)

class Geometry:
    Bar = Bar()

class BodyCut:
    def XXYYOnOnePoint(self, crPart, posCutPos, iType, dOffset, bSplit, bSectionFace, bShateFace, crLocalCoor):
        message = "Geometry.BodyCut.XXYYOnOnePoint({},{},{},{},{},{},{},{})".format(crPart, posCutPos, iType, dOffset, bSplit, bSectionFace, bShateFace, crLocalCoor)
        return JPT_RUN_LINE(message)

class Geometry:
    Bar = Bar()

class Geometry:
    BodyCut = BodyCut()

class BodyCut:
    def BySurface(self, crlPart,crCutter, bSplitOnly, bMakeSectionFace, bShareFace, bSeparateFace):
        message = "Geometry.BodyCut.BySurface({},{},{},{},{},{})".format(crlPart,crCutter, bSplitOnly, bMakeSectionFace, bShareFace, bSeparateFace)
        return JPT_RUN_LINE(message)

class BodyCut:
    def By3Points(self, crPart, poslPosition, dOffset, bSplitonly, bMakesectionface, bShareface):
        message = "Geometry.BodyCut.By3Points({},{},{},{},{},{})".format(crPart, poslPosition, dOffset, bSplitonly, bMakesectionface, bShareface)
        return JPT_RUN_LINE(message)

class Geometry:
    BodyCut = BodyCut()

class BreakEntity:
    def StlPart(self, crlPart, iMinNoOfFaces, iMethod):
        message = "Geometry.BreakEntity.StlPart({},{},{})".format(crlPart, iMinNoOfFaces, iMethod)
        return JPT_RUN_LINE(message)

class Geometry:
    BodyCut = BodyCut()

class Geometry:
    BreakEntity = BreakEntity()

class BreakEntity:
    def Face(self, crlFaces):
        message = "Geometry.BreakEntity.Face({})".format(crlFaces)
        return JPT_RUN_LINE(message)

class BreakEntity:
    def Edge(self, crlPart, crlFace, crlEdge, crlNode, bAutoByAngle, dEdgeAngle):
        message = "Geometry.BreakEntity.Edge({},{},{},{},{},{})".format(crlPart, crlFace, crlEdge, crlNode, bAutoByAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class Geometry:
    BreakEntity = BreakEntity()

class BreakEntity:
    def Part(self, crlPart):
        message = "Geometry.BreakEntity.Part({})".format(crlPart)
        return JPT_RUN_LINE(message)

class DeleteEntity:
    def Part(self, crlPart):
        message = "Geometry.DeleteEntity.Part({})".format(crlPart)
        return JPT_RUN_LINE(message)

class Geometry:
    BreakEntity = BreakEntity()

class Geometry:
    DeleteEntity = DeleteEntity()

class DeleteEntity:
    def Edge(self, crlEdge):
        message = "Geometry.DeleteEntity.Edge({})".format(crlEdge)
        return JPT_RUN_LINE(message)

class Geometry:
    BreakEntity = BreakEntity()

class Geometry:
    DeleteEntity = DeleteEntity()

class DeleteEntity:
    def Vertex(self, crlVertex):
        message = "Geometry.DeleteEntity.Vertex({})".format(crlVertex)
        return JPT_RUN_LINE(message)

class Geometry:
    DeleteEntity = DeleteEntity()

class Edge:
    def Line(self, poslPositions,crlCrTargetFace, bBreakFace):
        message = "Geometry.Edge.Line({},{},{})".format(poslPositions,crlCrTargetFace, bBreakFace)
        return JPT_RUN_LINE(message)

class Geometry:
    Edge = Edge()

class Geometry:
    DeleteEntity = DeleteEntity()

class Edge:
    def Spline(self, veclAprroxiPositions,crlTargetFace, bBreakFace):
        message = "Geometry.Edge.Spline({},{},{})".format(veclAprroxiPositions,crlTargetFace, bBreakFace)
        return JPT_RUN_LINE(message)

class DeleteEntity:
    def Face(self, crlFace, bKeepSolid):
        message = "Geometry.DeleteEntity.Face({},{})".format(crlFace, bKeepSolid)
        return JPT_RUN_LINE(message)

class Geometry:
    Edge = Edge()

class Edge:
    def PlanarLine(self, veclPosition,crlTargetFace, crLocalCoord, iType, bBreakFace):
        message = "Geometry.Edge.PlanarLine({},{},{},{},{})".format(veclPosition,crlTargetFace, crLocalCoord, iType, bBreakFace)
        return JPT_RUN_LINE(message)

class Geometry:
    Edge = Edge()

class Geometry:
    Edge = Edge()

class Edge:
    def Circle(self, veclPositions,crlTargetFace, dInRadius, dOutRadius, iNoOfLayer, iNoOfDiv, bBreakFace):
        message = "Geometry.Edge.Circle({},{},{},{},{},{},{})".format(veclPositions,crlTargetFace, dInRadius, dOutRadius, iNoOfLayer, iNoOfDiv, bBreakFace)
        return JPT_RUN_LINE(message)

class Geometry:
    Edge = Edge()

class Edge:
    def PerpendicularLineOfEdge(self, crlNodes,crlFaces, dOffset, bReakFace):
        message = "Geometry.Edge.PerpendicularLineOfEdge({},{},{},{})".format(crlNodes,crlFaces, dOffset, bReakFace)
        return JPT_RUN_LINE(message)

class Edge:
    def ExtendLine(self, crlVcrEdges, iMethod, iEnd, iNoFittingPoints, iDiv, iBBreakFace):
        message = "Geometry.Edge.ExtendLine({},{},{},{},{},{})".format(crlVcrEdges, iMethod, iEnd, iNoFittingPoints, iDiv, iBBreakFace)
        return JPT_RUN_LINE(message)

class Geometry:
    Edge = Edge()

class Edge:
    def ElementEdges(self, crplElemEdge, bBreakEdge):
        message = "Geometry.Edge.ElementEdges({},{})".format(crplElemEdge, bBreakEdge)
        return JPT_RUN_LINE(message)

class Edge:
    def Angle(self, crpPair, dAngle, bCurvature, bBreakFace):
        message = "Geometry.Edge.Angle({},{},{},{})".format(crpPair, dAngle, bCurvature, bBreakFace)
        return JPT_RUN_LINE(message)

class Edge:
    def NodeShortestPath(self, crFirstNode,crSecondNode, iBreakFace):
        message = "Geometry.Edge.NodeShortestPath({},{},{})".format(crFirstNode,crSecondNode, iBreakFace)
        return JPT_RUN_LINE(message)

class Geometry:
    Edge = Edge()

class Edge:
    def OffsetLine(self, crlFaces, crlEdges, bBreakFace, dOffsetDistance, iNumberLayer, bMerge, bExtend, iLayerMethod, dlVlayerOffset, bAutoCollapse, iRLType):
        message = "Geometry.Edge.OffsetLine({},{},{},{},{},{},{},{},{},{},{})".format(crlFaces, crlEdges, bBreakFace, dOffsetDistance, iNumberLayer, bMerge, bExtend, iLayerMethod, dlVlayerOffset, bAutoCollapse, iRLType)
        return JPT_RUN_LINE(message)

class Geometry:
    Edge = Edge()

class Geometry:
    Edge = Edge()

class Geometry:
    Edge = Edge()

class Edge:
    def SplineFreeEdges(self, crlVcrNode, iBArc, crPart, strBarName):
        message = "Geometry.Edge.SplineFreeEdges({},{},{},'{}')".format(crlVcrNode, iBArc, crPart, strBarName)
        return JPT_RUN_LINE(message)

class Geometry:
    Edge = Edge()

class Edge:
    def ClosedLine(self, veclPositions,crlCrTargetFace, iBBreakFace):
        message = "Geometry.Edge.ClosedLine({},{},{})".format(veclPositions,crlCrTargetFace, iBBreakFace)
        return JPT_RUN_LINE(message)

class Edge:
    def PerpendicularCylinderLine(self, crlNode, crlFaces, iMethod, dOffset, bOppositeSide, bBreakFace):
        message = "Geometry.Edge.PerpendicularCylinderLine({},{},{},{},{},{})".format(crlNode, crlFaces, iMethod, dOffset, bOppositeSide, bBreakFace)
        return JPT_RUN_LINE(message)

class Edge:
    def IntersectionLine(self, crlCrFaces, bBreakFace):
        message = "Geometry.Edge.IntersectionLine({},{})".format(crlCrFaces, bBreakFace)
        return JPT_RUN_LINE(message)

class Geometry:
    Edge = Edge()

class Geometry:
    Edge = Edge()

class Geometry:
    Edge = Edge()

class Geometry:
    Edge = Edge()

class Edge:
    def ProjectLine(self, crlCrEdges, crlCrFaces, crlCrNodes, bBreakFace, iType, bCheckGap, dGap):
        message = "Geometry.Edge.ProjectLine({},{},{},{},{},{},{})".format(crlCrEdges, crlCrFaces, crlCrNodes, bBreakFace, iType, bCheckGap, dGap)
        return JPT_RUN_LINE(message)

class Face:
    def FourEdges(self, crlVcrEdges):
        message = "Geometry.Face.FourEdges({})".format(crlVcrEdges)
        return JPT_RUN_LINE(message)

class Edge:
    def PerpendicularLineToEdge(self, crNode, crEdge, crlFace, bBreakFace):
        message = "Geometry.Edge.PerpendicularLineToEdge({},{},{},{})".format(crNode, crEdge, crlFace, bBreakFace)
        return JPT_RUN_LINE(message)

class Geometry:
    Face = Face()

class Face:
    def FromMesh(self, crlFace):
        message = "Geometry.Face.FromMesh({})".format(crlFace)
        return JPT_RUN_LINE(message)

class Geometry:
    Edge = Edge()

class Face:
    def CreateSmoothFace(self, bInterPoration,crlTargetCa,iElemGeneration,dGradation,iBFaceSmooth,crTargetPart):
        message = "Geometry.Face.CreateSmoothFace({},{},{},{},{},{})".format(bInterPoration,crlTargetCa,iElemGeneration,dGradation,iBFaceSmooth,crTargetPart)
        return JPT_RUN_LINE(message)

class Geometry:
    Face = Face()

class Geometry:
    Face = Face()

class Geometry:
    Face = Face()

class Face:
    def Elements(self, crlElem, bShareFace):
        message = "Geometry.Face.Elements({},{})".format(crlElem, bShareFace)
        return JPT_RUN_LINE(message)

class Face:
    def Edges(self, crlEdge, crlPart, crlNode, bSharedFace, bSmoothFace, bCreatePart, bImproved, bBarsOnly, bOnlyOnePart, bUseMidNodes):
        message = "Geometry.Face.Edges({},{},{},{},{},{},{},{},{},{})".format(crlEdge, crlPart, crlNode, bSharedFace, bSmoothFace, bCreatePart, bImproved, bBarsOnly, bOnlyOnePart, bUseMidNodes)
        return JPT_RUN_LINE(message)

class Geometry:
    FindFeature = FindFeature()

class FindFeature:
    def DelCircChamfer(self, crlPart, dMaxThick, dMinThick):
        message = "Geometry.FindFeature.DelCircChamfer({},{},{})".format(crlPart, dMaxThick, dMinThick)
        return JPT_RUN_LINE(message)

class FindFeature:
    def Fillet(self, crPart, crFace, dMinAngle, dMaxAngle, dMinFaceWidth, dMaxFaceWidth, dMinCurveRadius, dMaxCurveRadius, dScale):
        message = "Geometry.FindFeature.Fillet({},{},{},{},{},{},{},{},{})".format(crPart, crFace, dMinAngle, dMaxAngle, dMinFaceWidth, dMaxFaceWidth, dMinCurveRadius, dMaxCurveRadius, dScale)
        return JPT_RUN_LINE(message)

class Geometry:
    FindFeature = FindFeature()

class Geometry:
    Face = Face()

class Geometry:
    FindFeature = FindFeature()

class FindFeature:
    def Faces(self, taBodyKey,iOption, taEdgeKey, bCylinder, bDisc, bFourCorners, dMinThickness, dMaxThickness, dDiameterMin, dDiameterMax, taFaceKey):
        message = "Geometry.FindFeature.Faces({},{},{},{},{},{},{},{},{},{},{})".format(taBodyKey,iOption, taEdgeKey, bCylinder, bDisc, bFourCorners, dMinThickness, dMaxThickness, dDiameterMin, dDiameterMax, taFaceKey)
        return JPT_RUN_LINE(message)

class FindFeature:
    def Edges(self, taBodyKey,iOption, taEdgeKey, bCylinder, bDisc, bFourCorners, dMinThickness, dMaxThickness, dDiameterMin, dDiameterMax, taFaceKey):
        message = "Geometry.FindFeature.Edges({},{},{},{},{},{},{},{},{},{},{})".format(taBodyKey,iOption, taEdgeKey, bCylinder, bDisc, bFourCorners, dMinThickness, dMaxThickness, dDiameterMin, dDiameterMax, taFaceKey)
        return JPT_RUN_LINE(message)

class Geometry:
    FindFeature = FindFeature()

class MergeEntities:
    def Faces(self, crlFace, bMergeEdge, bRemoveNonBoundEdge):
        message = "Geometry.MergeEntities.Faces({},{},{})".format(crlFace, bMergeEdge, bRemoveNonBoundEdge)
        return JPT_RUN_LINE(message)

class MergeEntities:
    def TinyFacesMerge(self, ilPartkeys, ilFacekeys, dMinFaceWidth, dMaxFaceWidth, dFaceAngle, bReferLocalSetting, bConnectFace):
        message = "Geometry.MergeEntities.TinyFacesMerge({},{},{},{},{},{},{})".format(ilPartkeys, ilFacekeys, dMinFaceWidth, dMaxFaceWidth, dFaceAngle, bReferLocalSetting, bConnectFace)
        return JPT_RUN_LINE(message)

class Geometry:
    MergeEntities = MergeEntities()

class MergeEntities:
    def CBarParts(self, crlPart):
        message = "Geometry.MergeEntities.CBarParts({})".format(crlPart)
        return JPT_RUN_LINE(message)

class Geometry:
    MergeEntities = MergeEntities()

class Geometry:
    MergeEntities = MergeEntities()

class MergeEntities:
    def Edges(self, crlEdge):
        message = "Geometry.MergeEntities.Edges({})".format(crlEdge)
        return JPT_RUN_LINE(message)

class MergeEntities:
    def Parts(self, dTolerance, bRemovesharefaceflag, crlPart):
        message = "Geometry.MergeEntities.Parts({},{},{})".format(dTolerance, bRemovesharefaceflag, crlPart)
        return JPT_RUN_LINE(message)

class Geometry:
    MergeEntities = MergeEntities()

class MergeEntities:
    def PartFaces(self, crlPart, crlFace, bAngle, dTolAngle, bWidth, dTolWidth):
        message = "Geometry.MergeEntities.PartFaces({},{},{},{},{},{})".format(crlPart, crlFace, bAngle, dTolAngle, bWidth, dTolWidth)
        return JPT_RUN_LINE(message)

class Part:
    def Cube(self, dlVdOrigin, dlVdLength, ilVlNodeCnt, strPartName, iColPart, crCoord):
        message = "Geometry.Part.Cube({},{},{},'{}',{},{})".format(dlVdOrigin, dlVdLength, ilVlNodeCnt, strPartName, iColPart, crCoord)
        return JPT_RUN_LINE(message)

class Geometry:
    MergeEntities = MergeEntities()

class Geometry:
    Part = Part()

class Geometry:
    MergeEntities = MergeEntities()

class Geometry:
    Part = Part()

class Part:
    def Wedge(self, vecOrigin, vecLength, vecNodeCount, strPartName, iPartColor, crCoordinate):
        message = "Geometry.Part.Wedge({},{},{},'{}',{},{})".format(vecOrigin, vecLength, vecNodeCount, strPartName, iPartColor, crCoordinate)
        return JPT_RUN_LINE(message)

class Part:
    def Sphere(self, dlVdOrigin, dRadius, iLatitudeNodeCnt, iLongitudeNodeCnt, strPartName, iColPart, crCoord):
        message = "Geometry.Part.Sphere({},{},{},{},'{}',{},{})".format(dlVdOrigin, dRadius, iLatitudeNodeCnt, iLongitudeNodeCnt, strPartName, iColPart, crCoord)
        return JPT_RUN_LINE(message)

class Geometry:
    Part = Part()

class Part:
    def Torus(self, dlVdOrigin, dInnerRadius, dRingRadius, iLatitudeNodeCnt, iLongitudeNodeCnt, strPartName, iColPart, crCoord):
        message = "Geometry.Part.Torus({},{},{},{},{},'{}',{},{})".format(dlVdOrigin, dInnerRadius, dRingRadius, iLatitudeNodeCnt, iLongitudeNodeCnt, strPartName, iColPart, crCoord)
        return JPT_RUN_LINE(message)

class Geometry:
    Part = Part()

class Part:
    def Elems(self, crlListElem,strPartName):
        message = "Geometry.Part.Elems({},'{}')".format(crlListElem,strPartName)
        return JPT_RUN_LINE(message)

class Geometry:
    Part = Part()

class Part:
    def Cylinder(self, dlOrigin, dTopRadius, dBotRadius, dHeight, iCircleNodeCnt, iAxisNodeCnt, strName, iPartCol, crCoord):
        message = "Geometry.Part.Cylinder({},{},{},{},{},{},'{}',{},{})".format(dlOrigin, dTopRadius, dBotRadius, dHeight, iCircleNodeCnt, iAxisNodeCnt, strName, iPartCol, crCoord)
        return JPT_RUN_LINE(message)

class Part:
    def Tube(self, dlOrigin, dTopInnerRadius, dTopOuterRadius, dBotInnerRadius, dBotOuterRadius, dHeight, iCircleNodeCnt, iAxisNodeCnt, strName, iPartCol, crCoord):
        message = "Geometry.Part.Tube({},{},{},{},{},{},{},{},'{}',{},{})".format(dlOrigin, dTopInnerRadius, dTopOuterRadius, dBotInnerRadius, dBotOuterRadius, dHeight, iCircleNodeCnt, iAxisNodeCnt, strName, iPartCol, crCoord)
        return JPT_RUN_LINE(message)

class Geometry:
    Part = Part()

class Geometry:
    Part = Part()

class Part:
    def Trapezoid(self, dlVdOrigin, dlVdLength, dTopXLength, dRadius, ilVlNodeCnt, strPartName, iColPart, crCoord):
        message = "Geometry.Part.Trapezoid({},{},{},{},{},'{}',{},{})".format(dlVdOrigin, dlVdLength, dTopXLength, dRadius, ilVlNodeCnt, strPartName, iColPart, crCoord)
        return JPT_RUN_LINE(message)

class Part:
    def Cone(self, dlOriginXyz, dBottomRadius, dHeight, iCircleNodeCount, iAxisNodeCnt, strPartName, iPartColor, crCoordinate):
        message = "Geometry.Part.Cone({},{},{},{},{},'{}',{},{})".format(dlOriginXyz, dBottomRadius, dHeight, iCircleNodeCount, iAxisNodeCnt, strPartName, iPartColor, crCoordinate)
        return JPT_RUN_LINE(message)

class Geometry:
    Part = Part()

class Geometry:
    Part = Part()

class ShowAdjacent:
    def Faces(self, Angle, IncludeStopFace, Layer,IsPreview, taStartFaceCr,taStopFaceCr):
        message = "Geometry.ShowAdjacent.Faces({},{},{},{},{},{})".format(Angle, IncludeStopFace, Layer,IsPreview, taStartFaceCr,taStopFaceCr)
        return JPT_RUN_LINE(message)

class ShowAdjacent:
    def Elements(self, Angle, IncludeStopElem, Layer,IsPreview, taStartElemCr,taStopElemCr):
        message = "Geometry.ShowAdjacent.Elements({},{},{},{},{},{})".format(Angle, IncludeStopElem, Layer,IsPreview, taStartElemCr,taStopElemCr)
        return JPT_RUN_LINE(message)

class Geometry:
    ShowAdjacent = ShowAdjacent()

class Transform:
    def Rotation(self, crlPart, posCenter, vecAxis, dAngle, bCreateNewPart, bCopyLBC, bCopyProperty, iCopyCount, bMergeNode, dTol):
        message = "Geometry.Transform.Rotation({},{},{},{},{},{},{},{},{},{})".format(crlPart, posCenter, vecAxis, dAngle, bCreateNewPart, bCopyLBC, bCopyProperty, iCopyCount, bMergeNode, dTol)
        return JPT_RUN_LINE(message)

class Geometry:
    ShowAdjacent = ShowAdjacent()

class Transform:
    def Scaling(self, crlPart, dlScaleVector, dlScaleCentre, crCoordinate, bCreateNew, bCopyLbc, bCopyProperty, bUsepartcenter):
        message = "Geometry.Transform.Scaling({},{},{},{},{},{},{},{})".format(crlPart, dlScaleVector, dlScaleCentre, crCoordinate, bCreateNew, bCopyLbc, bCopyProperty, bUsepartcenter)
        return JPT_RUN_LINE(message)

class Geometry:
    Transform = Transform()

class Geometry:
    Transform = Transform()

class Transform:
    def Mirror(self, crlPart, veclPoint, dOffset, bCreateNewPart, bCopyLBC, bCopyProperty, bRemoveDupFace, bMergeNode, dTol):
        message = "Geometry.Transform.Mirror({},{},{},{},{},{},{},{},{})".format(crlPart, veclPoint, dOffset, bCreateNewPart, bCopyLBC, bCopyProperty, bRemoveDupFace, bMergeNode, dTol)
        return JPT_RUN_LINE(message)

class Transform:
    def Position(self, crlPart, veclPoint, bCreateNewPart, bCopyLBC, bCopyProperty):
        message = "Geometry.Transform.Position({},{},{},{},{})".format(crlPart, veclPoint, bCreateNewPart, bCopyLBC, bCopyProperty)
        return JPT_RUN_LINE(message)

class Geometry:
    Transform = Transform()

class Geometry:
    Transform = Transform()

class Transform:
    def Translation(self, crlPart, poslTavdTranslates, crCoord, bCreateNewPart, bCopyLBC, bCopyProperty, iCopyCount):
        message = "Geometry.Transform.Translation({},{},{},{},{},{},{})".format(crlPart, poslTavdTranslates, crCoord, bCreateNewPart, bCopyLBC, bCopyProperty, iCopyCount)
        return JPT_RUN_LINE(message)

class Geometry:
    Transform = Transform()

class Geometry:
    Transform = Transform()

class Transform:
    def MatingFace(self, crlPart, crSrcFace, crDstFace, crSrcEdge, crDstEdge, crSrcNode, crDstNode, iFaceOpposite, dEdgeAngle, iEdgeOpposite, iAlignMethodType, iAdjustPointType, iAdjustProjectionType, dlAlignVector, dlAdjustPoint, dlAdjustVector, bCreateNewPart, bCopyLBC, bCopyProperty, bIsPreview, crlCoordSyss):
        message = "Geometry.Transform.MatingFace({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, crSrcFace, crDstFace, crSrcEdge, crDstEdge, crSrcNode, crDstNode, iFaceOpposite, dEdgeAngle, iEdgeOpposite, iAlignMethodType, iAdjustPointType, iAdjustProjectionType, dlAlignVector, dlAdjustPoint, dlAdjustVector, bCreateNewPart, bCopyLBC, bCopyProperty, bIsPreview, crlCoordSyss)
        return JPT_RUN_LINE(message)

class Transform:
    def CylinderFace(self, crlPart, veclPoint, bCreateNewPart, bCopyLBC, bCopyProperty):
        message = "Geometry.Transform.CylinderFace({},{},{},{},{})".format(crlPart, veclPoint, bCreateNewPart, bCopyLBC, bCopyProperty)
        return JPT_RUN_LINE(message)

class Geometry:
    Transform = Transform()

class Geometry:
    def CADTrim(crlListFace,crlListPart, dTrimSize, dTrimAngle):
        message = "Geometry.CADTrim({},{},{},{})".format(crlListFace,crlListPart, dTrimSize, dTrimAngle)
        return JPT_RUN_LINE(message)

class Geometry:
    def LogoRemoval(crlStartFaces, crlStopFaces, iLayers, bMergeFaces):
        message = "Geometry.LogoRemoval({},{},{},{})".format(crlStartFaces, crlStopFaces, iLayers, bMergeFaces)
        return JPT_RUN_LINE(message)

class Geometry:
    def ShellAsm(crlPartK, crlFaceK, dTol, iElemType, bSkipTiny):
        message = "Geometry.ShellAsm({},{},{},{},{})".format(crlPartK, crlFaceK, dTol, iElemType, bSkipTiny)
        return JPT_RUN_LINE(message)

class Geometry:
    def SquareUpFillet(crlFaces):
        message = "Geometry.SquareUpFillet({})".format(crlFaces)
        return JPT_RUN_LINE(message)

class Geometry:
    def StitchEdge(dTolerance, bKeepSlave, crlMaster, crlSlave):
        message = "Geometry.StitchEdge({},{},{},{})".format(dTolerance, bKeepSlave, crlMaster, crlSlave)
        return JPT_RUN_LINE(message)

class Geometry:
    def MakeFacePlanar(dlPlanePt1, dlPlanePt2, dlPlanePt3, ilFaceIds, iMergeFace):
        message = "Geometry.MakeFacePlanar({},{},{},{},{})".format(dlPlanePt1, dlPlanePt2, dlPlanePt3, ilFaceIds, iMergeFace)
        return JPT_RUN_LINE(message)

class Geometry:
    def AdjustHalfCylinder(poslPoint, crlFace, crCoord, nAxisPlane, bDivideFace, crlPartTarget, bMergeEdge):
        message = "Geometry.AdjustHalfCylinder({},{},{},{},{},{},{})".format(poslPoint, crlFace, crCoord, nAxisPlane, bDivideFace, crlPartTarget, bMergeEdge)
        return JPT_RUN_LINE(message)

class Geometry:
    def FCircVertexAdjust(crlPart, dMinRadius, bFullCylinder, bCylinderMorethan90, bSkipFaceHaveLocalSetting):
        message = "Geometry.FCircVertexAdjust({},{},{},{},{})".format(crlPart, dMinRadius, bFullCylinder, bCylinderMorethan90, bSkipFaceHaveLocalSetting)
        return JPT_RUN_LINE(message)

class Geometry:
    def FCircleAdjustVertex(crlPart):
        message = "Geometry.FCircleAdjustVertex({})".format(crlPart)
        return JPT_RUN_LINE(message)

class Geometry:
    def MakeFillet(crlEdges, dRadius):
        message = "Geometry.MakeFillet({},{})".format(crlEdges, dRadius)
        return JPT_RUN_LINE(message)

class Geometry:
    def ExtractSurfaces(crlFace, dAngle, strName, bMergePart):
        message = "Geometry.ExtractSurfaces({},{},'{}',{})".format(crlFace, dAngle, strName, bMergePart)
        return JPT_RUN_LINE(message)

class Geometry:
    def AdvancedShellAssembly(crlPart, crlFace, iMeshType, bSelfIntersection, iMethod, dGapTol):
        message = "Geometry.AdvancedShellAssembly({},{},{},{},{},{})".format(crlPart, crlFace, iMeshType, bSelfIntersection, iMethod, dGapTol)
        return JPT_RUN_LINE(message)

class Geometry:
    def RemoveRibBoss(crlFace, dGradiation, iContinuity):
        message = "Geometry.RemoveRibBoss({},{},{})".format(crlFace, dGradiation, iContinuity)
        return JPT_RUN_LINE(message)

class Groups:
    RightClick = RightClick()

class RightClick:
    def PropertyGroup(self, strTmp):
        message = "Groups.RightClick.PropertyGroup('{}')".format(strTmp)
        return JPT_RUN_LINE(message)

class RightClick:
    def DeleteGroup(self, crlDelGroup, bRemoveAll):
        message = "Groups.RightClick.DeleteGroup({},{})".format(crlDelGroup, bRemoveAll)
        return JPT_RUN_LINE(message)

class RightClick:
    def Rename(self, strNewName,crItem):
        message = "Groups.RightClick.Rename('{}',{})".format(strNewName,crItem)
        return JPT_RUN_LINE(message)

class Groups:
    RightClick = RightClick()

class Groups:
    RightClick = RightClick()

class Groups:
    RightClick = RightClick()

class RightClick:
    def CopyGroup(self, crlSrc, strlNames, crDest, bKeep):
        message = "Groups.RightClick.CopyGroup({},'{}',{},{})".format(crlSrc, strlNames, crDest, bKeep)
        return JPT_RUN_LINE(message)

class Groups:
    RightClick = RightClick()

class RightClick:
    def CreateMatGroup(self, strTmp):
        message = "Groups.RightClick.CreateMatGroup('{}')".format(strTmp)
        return JPT_RUN_LINE(message)

class RightClick:
    def AddSupGroup(self, crSupGroupSelected):
        message = "Groups.RightClick.AddSupGroup({})".format(crSupGroupSelected)
        return JPT_RUN_LINE(message)

class HexModeling:
    def SolidElemInterface(crlFaces, bFlip, crlElms):
        message = "HexModeling.SolidElemInterface({},{},{})".format(crlFaces, bFlip, crlElms)
        return JPT_RUN_LINE(message)

class HexModeling:
    def BallHexa(crPart, vecCenter, dRadius, dMeshSize, iType, iLayer, bMakeCenterNode, strPartName):
        message = "HexModeling.BallHexa({},{},{},{},{},{},{},'{}')".format(crPart, vecCenter, dRadius, dMeshSize, iType, iLayer, bMakeCenterNode, strPartName)
        return JPT_RUN_LINE(message)

class HexModeling:
    def BoxMesh(ilPartIds,dMeshSize,strMaterialName):
        message = "HexModeling.BoxMesh({},{},'{}')".format(ilPartIds,dMeshSize,strMaterialName)
        return JPT_RUN_LINE(message)

class HexModeling:
    def AutoSweep(crl, dMeshSize, bLayers, iLayers):
        message = "HexModeling.AutoSweep({},{},{},{})".format(crl, dMeshSize, bLayers, iLayers)
        return JPT_RUN_LINE(message)

class Groups:
    RightClick = RightClick()

class HexModeling:
    def Circular(crlFace, dAngle, dTol, iLayer, vecAxisPt, vecAxisVect, bInterfaceElem, bExtrusion, dTranslationExtrusion, dBDeleteOriginalParts):
        message = "HexModeling.Circular({},{},{},{},{},{},{},{},{},{})".format(crlFace, dAngle, dTol, iLayer, vecAxisPt, vecAxisVect, bInterfaceElem, bExtrusion, dTranslationExtrusion, dBDeleteOriginalParts)
        return JPT_RUN_LINE(message)

class HexModeling:
    def Layer(crlFace, dFrontWidth, dBackWidth, iFrontLayers, iBackLayers, iBaseFaceType, iSeparate):
        message = "HexModeling.Layer({},{},{},{},{},{},{})".format(crlFace, dFrontWidth, dBackWidth, iFrontLayers, iBackLayers, iBaseFaceType, iSeparate)
        return JPT_RUN_LINE(message)

class HexModeling:
    def Linear(crlFace, dLength, nLayer, vecSweepDirection, bInterfaceElemFlag, nLinearMethod, bDeleteOriginalParts, bDeleteTargetParts, nMethodBias, dFactor, nProgression):
        message = "HexModeling.Linear({},{},{},{},{},{},{},{},{},{},{})".format(crlFace, dLength, nLayer, vecSweepDirection, bInterfaceElemFlag, nLinearMethod, bDeleteOriginalParts, bDeleteTargetParts, nMethodBias, dFactor, nProgression)
        return JPT_RUN_LINE(message)

class HexModeling:
    def FaceToFace(crSrcFace,crDstFace, bDeleteOriginalParts):
        message = "HexModeling.FaceToFace({},{},{})".format(crSrcFace,crDstFace, bDeleteOriginalParts)
        return JPT_RUN_LINE(message)

class HexModeling:
    def FromMidPlane(crlPart, bRef):
        message = "HexModeling.FromMidPlane({},{})".format(crlPart, bRef)
        return JPT_RUN_LINE(message)

class HexModeling:
    def Curve(crFace, crlVcrEdges, crlVcrRefEdges, dMeshSize):
        message = "HexModeling.Curve({},{},{},{})".format(crFace, crlVcrEdges, crlVcrRefEdges, dMeshSize)
        return JPT_RUN_LINE(message)

class ImportCAD:
    def Elysium(self, strlPath, dChordHeightTolerance, dAngleToleranceDegree, dPointCoincidentTolerance, iConvertIsolatedCurve, iDekCleanselfintersectingloop, iDekVolumetopart, iIgesFixedcurevepreference, iIgesAutostitch, dIgesStitchtolerance, iCatiaConvertnotshowedelement, iCatiaConvertnotshowedinstance, iCatiaConvertaxis, iStepCreateseam, dStepPointtolerance, iAcisHealacisbeforeversion, iJtConvertgeometrytype, bFaceColor, iJtConvertgeneralpart, iJtConvertaxis, iJtConvertcenterline):
        message = "Home.ImportCAD.Elysium('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strlPath, dChordHeightTolerance, dAngleToleranceDegree, dPointCoincidentTolerance, iConvertIsolatedCurve, iDekCleanselfintersectingloop, iDekVolumetopart, iIgesFixedcurevepreference, iIgesAutostitch, dIgesStitchtolerance, iCatiaConvertnotshowedelement, iCatiaConvertnotshowedinstance, iCatiaConvertaxis, iStepCreateseam, dStepPointtolerance, iAcisHealacisbeforeversion, iJtConvertgeometrytype, bFaceColor, iJtConvertgeneralpart, iJtConvertaxis, iJtConvertcenterline)
        return JPT_RUN_LINE(message)

class ImportCAD:
    def Spatial(self, strlPath, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, bNXMultipart, bHealing, bIsNXDirect, bSetFaceColor, strCsvFilePath):
        message = "Home.ImportCAD.Spatial('{}',{},{},{},{},{},{},{},'{}')".format(strlPath, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, bNXMultipart, bHealing, bIsNXDirect, bSetFaceColor, strCsvFilePath)
        return JPT_RUN_LINE(message)

class Home:
    ImportCAD = ImportCAD()

class ImportCAD:
    def Parasolid(self, strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale):
        message = "Home.ImportCAD.Parasolid('{}',{},{},{},{},{},{},{},{},{},{})".format(strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale)
        return JPT_RUN_LINE(message)

class Home:
    ImportCAD = ImportCAD()

class Home:
    ImportCAD = ImportCAD()

class ImportCAD:
    def STL(self, strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale):
        message = "Home.ImportCAD.STL('{}',{},{},{},{},{},{},{},{},{},{})".format(strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale)
        return JPT_RUN_LINE(message)

class Home:
    ImportCAD = ImportCAD()

class ImportCAD:
    def VRML(self, strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale):
        message = "Home.ImportCAD.VRML('{}',{},{},{},{},{},{},{},{},{},{})".format(strlFiles, dChordHeightTolerance, dAngleToleranceDegree, iConvertIsolatedCurve, dSurfacePlaneTolerance, dSufacePlaneAngle, dMaxFacetWidth, dMinFacetWidth, bICAD, iVRMLColorGroups, dScale)
        return JPT_RUN_LINE(message)

class Home:
    ImportCAD = ImportCAD()

class ImportCAD:
    def ProECreoDirect(self, strlPath, dChordHeightTolerance, dAngleToleranceDegree, dStepMaxSize):
        message = "Home.ImportCAD.ProECreoDirect('{}',{},{},{})".format(strlPath, dChordHeightTolerance, dAngleToleranceDegree, dStepMaxSize)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def ADVCADX(self, strPath, dFaceAngle, dEdgeAngle):
        message = "Home.ImportMesh.ADVCADX('{}',{},{})".format(strPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class Home:
    ImportCAD = ImportCAD()

class Home:
    ImportMesh = ImportMesh()

class ImportMesh:
    def AnsysDat(self, strlPath, dFaceAngle, dEdgeAngle):
        message = "Home.ImportMesh.AnsysDat('{}',{},{})".format(strlPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def NastranBdf(self, strlFilePaths, iMportType, dFaceAngle, dEdgeAngle, bReadNameComment, iCreateDup1DElemAnswer):
        message = "Home.ImportMesh.NastranBdf('{}',{},{},{},{},{})".format(strlFilePaths, iMportType, dFaceAngle, dEdgeAngle, bReadNameComment, iCreateDup1DElemAnswer)
        return JPT_RUN_LINE(message)

class ImportMesh:
    def AbaqusINP(self, strlFilePaths, dFaceAngle, dEdgeAngle, iMportType):
        message = "Home.ImportMesh.AbaqusINP('{}',{},{},{})".format(strlFilePaths, dFaceAngle, dEdgeAngle, iMportType)
        return JPT_RUN_LINE(message)

class Home:
    ImportMesh = ImportMesh()

class Home:
    ImportMesh = ImportMesh()

class ImportMesh:
    def LSDYNA(self, strlPath, dFaceAngle, dEdgeAngle):
        message = "Home.ImportMesh.LSDYNA('{}',{},{})".format(strlPath, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class Home:
    ImportMesh = ImportMesh()

class ImportMesh:
    def Universal(self, strPath):
        message = "Home.ImportMesh.Universal('{}')".format(strPath)
        return JPT_RUN_LINE(message)

class Home:
    ImportMesh = ImportMesh()

class Home:
    ImportMesh = ImportMesh()

class Home:
    def Export(strFileName, crlBodies, bBigID, bUseUnit, bVert, bEdge, bFace, bSolid):
        message = "Home.Export('{}',{},{},{},{},{},{},{})".format(strFileName, crlBodies, bBigID, bUseUnit, bVert, bEdge, bFace, bSolid)
        return JPT_RUN_LINE(message)

class Home:
    def ToImage(strImgPath, bWhiteBG, bTransparentBG, bFixedSize, iExportWidth, iExportHeight):
        message = "Home.ToImage('{}',{},{},{},{},{})".format(strImgPath, bWhiteBG, bTransparentBG, bFixedSize, iExportWidth, iExportHeight)
        return JPT_RUN_LINE(message)

class Home:
    def RectangularCapture(iLeft, iTop, iRight, iBottom):
        message = "Home.RectangularCapture({},{},{},{})".format(iLeft, iTop, iRight, iBottom)
        return JPT_RUN_LINE(message)

class Home:
    def Find(strSearch, strSeletedType, bFindMatch):
        message = "Home.Find('{}','{}',{})".format(strSearch, strSeletedType, bFindMatch)
        return JPT_RUN_LINE(message)

class Home:
    def CopyToClipboard(bWhiteBG, bTransparentBG, bFixedSize, iWidth, iHeight):
        message = "Home.CopyToClipboard({},{},{},{},{})".format(bWhiteBG, bTransparentBG, bFixedSize, iWidth, iHeight)
        return JPT_RUN_LINE(message)

class Home:
    def FullScreen():
        message = "Home.FullScreen({})".format()
        return JPT_RUN_LINE(message)

class Home:
    def Synchronize():
        message = "Home.Synchronize({})".format()
        return JPT_RUN_LINE(message)

class RightClick:
    def MergeFaces(self, crlListFace, bIsMergeEdge, bRemoveNonBoundEdge):
        message = "MainWindow.RightClick.MergeFaces({},{},{})".format(crlListFace, bIsMergeEdge, bRemoveNonBoundEdge)
        return JPT_RUN_LINE(message)

class MainWindow:
    RightClick = RightClick()

class RightClick:
    def SelectAllParts(self, ):
        message = "MainWindow.RightClick.SelectAllParts({})".format()
        return JPT_RUN_LINE(message)

class MainWindow:
    RightClick = RightClick()

class MainWindow:
    RightClick = RightClick()

class RightClick:
    def AssociatedPick(self, crlInput,strTarget, strConnect):
        message = "MainWindow.RightClick.AssociatedPick({},'{}','{}')".format(crlInput,strTarget, strConnect)
        return JPT_RUN_LINE(message)

class MainWindow:
    RightClick = RightClick()

class RightClick:
    def FlipElement(self, crlTargets):
        message = "MainWindow.RightClick.FlipElement({})".format(crlTargets)
        return JPT_RUN_LINE(message)

class Element:
    def SolidElement(self, crlListElem, crPart):
        message = "MeshCleanup.Element.SolidElement({},{})".format(crlListElem, crPart)
        return JPT_RUN_LINE(message)

class Element:
    def SurfaceElement(self, ilElement, ilFace, ilPart, iCreateNewPart):
        message = "MeshCleanup.Element.SurfaceElement({},{},{},{})".format(ilElement, ilFace, ilPart, iCreateNewPart)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Element = Element()

class MeshCleanup:
    def Face(crlFace, crlPart, bCreateNewPart):
        message = "MeshCleanup.Face({},{},{})".format(crlFace, crlPart, bCreateNewPart)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    def CorrectModel(crlVcrParts, iBBreakEdge, dEdgeAngle, iBMergeEdge, dMergeEdgeAngle, iBMergePlanarFace, iBRemoveExtraVertex):
        message = "MeshCleanup.CorrectModel({},{},{},{},{},{},{})".format(crlVcrParts, iBBreakEdge, dEdgeAngle, iBMergeEdge, dMergeEdgeAngle, iBMergePlanarFace, iBRemoveExtraVertex)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    def CloseHoles(crlEdge, dAreaMin, dAreaMax, bMergeFace, bMergeEdge):
        message = "MeshCleanup.CloseHoles({},{},{},{},{})".format(crlEdge, dAreaMin, dAreaMax, bMergeFace, bMergeEdge)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Element = Element()

class MeshCleanup:
    def CloseGap(crlPartCur, dDistanceTol):
        message = "MeshCleanup.CloseGap({},{})".format(crlPartCur, dDistanceTol)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    def AutoCheck(crlPart,iElemType,blTaCheckCondition,blTaElemQuality,dlTaLimitValue,crlElem):
        message = "MeshCleanup.AutoCheck({},{},{},{},{},{})".format(crlPart,iElemType,blTaCheckCondition,blTaElemQuality,dlTaLimitValue,crlElem)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    def ManualCheck(crlPart, iElemType, iVeQuality, iCheckCondition, dLimitValue, dCFLValue, iNonManifold, iCleanupMode, crlElem):
        message = "MeshCleanup.ManualCheck({},{},{},{},{},{},{},{},{})".format(crlPart, iElemType, iVeQuality, iCheckCondition, dLimitValue, dCFLValue, iNonManifold, iCleanupMode, crlElem)
        return JPT_RUN_LINE(message)

class ChangeTopology:
    Element = Element()

class MeshCleanup:
    ChangeTopology = ChangeTopology()

class Element:
    def SurfaceElement(self, ilElement,ilFace,ilPart,iCreateNewPart):
        message = "MeshCleanup.ChangeTopology.Element.SurfaceElement({},{},{},{})".format(ilElement,ilFace,ilPart,iCreateNewPart)
        return JPT_RUN_LINE(message)

class Cleanup:
    def CloseGap(self, crlPartCur,dDistanceTol):
        message = "MeshCleanup.Cleanup.CloseGap({},{})".format(crlPartCur,dDistanceTol)
        return JPT_RUN_LINE(message)

class MergeElement:
    def TwoQuadsToQuad(self, crlElements):
        message = "MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad({})".format(crlElements)
        return JPT_RUN_LINE(message)

class Manual2D:
    MergeElement = MergeElement()

class MeshCleanup:
    Cleanup = Cleanup()

class MeshCleanup:
    Manual2D = Manual2D()

class MergeElement:
    def TwoQuadsToQuad(self, crlElements):
        message = "MeshCleanup.Manual2D.MergeElement.TwoQuadsToQuad({})".format(crlElements)
        return JPT_RUN_LINE(message)

class Manual2D:
    MergeElement = MergeElement()

class MergeElement:
    def TwoTrisToQuad(self, crlElems):
        message = "MeshCleanup.Manual2D.MergeElement.TwoTrisToQuad({})".format(crlElems)
        return JPT_RUN_LINE(message)

class Manual2D:
    MergeElement = MergeElement()

class MeshCleanup:
    Manual2D = Manual2D()

class MeshCleanup:
    Manual2D = Manual2D()

class SplitElement:
    def QuadTo4Quads(self, crlElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo4Quads({},{},{},{},{},{},{},{})".format(crlElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class Manual2D:
    SplitElement = SplitElement()

class MeshCleanup:
    Manual2D = Manual2D()

class SplitElement:
    def QuadToTrans4Quads(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadToTrans4Quads({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class Manual2D:
    SplitElement = SplitElement()

class SplitElement:
    def QuadToTrans3Quads(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadToTrans3Quads({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual2D = Manual2D()

class MeshCleanup:
    Manual2D = Manual2D()

class Manual2D:
    SplitElement = SplitElement()

class Manual2D:
    SplitElement = SplitElement()

class SplitElement:
    def QuadTo2Quads1Tri(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo2Quads1Tri({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class SplitElement:
    def QuadTo3Tris(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo3Tris({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual2D = Manual2D()

class Manual2D:
    SplitElement = SplitElement()

class SplitElement:
    def QuadTo2Quads(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo2Quads({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual2D = Manual2D()

class Manual2D:
    SplitElement = SplitElement()

class SplitElement:
    def QuadTo2Tris(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo2Tris({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual2D = Manual2D()

class Manual2D:
    SplitElement = SplitElement()

class SplitElement:
    def QuadToQuadTri(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadToQuadTri({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual2D = Manual2D()

class Manual2D:
    SplitElement = SplitElement()

class SplitElement:
    def QuadTo4Tris(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.QuadTo4Tris({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual2D = Manual2D()

class Manual2D:
    SplitElement = SplitElement()

class Manual2D:
    def Equivalence(self, crlNode, iTypeEquiva, dTolerance):
        message = "MeshCleanup.Manual2D.Equivalence({},{},{})".format(crlNode, iTypeEquiva, dTolerance)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual2D = Manual2D()

class MeshCleanup:
    Manual2D = Manual2D()

class Manual2D:
    def DeleteElement(self, crlElems, bKeepShareElem):
        message = "MeshCleanup.Manual2D.DeleteElement({},{})".format(crlElems, bKeepShareElem)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual2D = Manual2D()

class MeshCleanup:
    Manual2D = Manual2D()

class Manual2D:
    def Swap(self, crplElemEdge):
        message = "MeshCleanup.Manual2D.Swap({})".format(crplElemEdge)
        return JPT_RUN_LINE(message)

class Manual2D:
    def Split(self, crplElemEdge, dRatio, crNodeRef, crProjPart):
        message = "MeshCleanup.Manual2D.Split({},{},{},{})".format(crplElemEdge, dRatio, crNodeRef, crProjPart)
        return JPT_RUN_LINE(message)

class Manual2D:
    def Collapse(self, crNodeRef, crNodeEq):
        message = "MeshCleanup.Manual2D.Collapse({},{})".format(crNodeRef, crNodeEq)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual2D = Manual2D()

class Manual2D:
    def CreateElement(self, nElemType, crParentEntity, crlViNodeKey):
        message = "MeshCleanup.Manual2D.CreateElement({},{},{})".format(nElemType, crParentEntity, crlViNodeKey)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual2D = Manual2D()

class MeshCleanup:
    Manual2D = Manual2D()

class MeshCleanup:
    Manual2D = Manual2D()

class Manual2D:
    def RemeshElement(self, crlTarget, surfaceMesh, bUseSetting, bGrading, bFMesher, iOverrideType, bKeepConnection, bProjCAD, bTinyFaceMerge, dMinFaceWidth, dMaxFaceWidth, bIDchcek, bKeepRemeshEdge):
        message = "MeshCleanup.Manual2D.RemeshElement({},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlTarget, surfaceMesh, bUseSetting, bGrading, bFMesher, iOverrideType, bKeepConnection, bProjCAD, bTinyFaceMerge, dMinFaceWidth, dMaxFaceWidth, bIDchcek, bKeepRemeshEdge)
        return JPT_RUN_LINE(message)

class Manual3D:
    Collapse = Collapse()

class Collapse:
    def CenterFaceCollapse(self, crlElem):
        message = "MeshCleanup.Manual3D.Collapse.CenterFaceCollapse({})".format(crlElem)
        return JPT_RUN_LINE(message)

class Collapse:
    def HalfEdgeCollapse(self, crplElemEdge):
        message = "MeshCleanup.Manual3D.Collapse.HalfEdgeCollapse({})".format(crplElemEdge)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual3D = Manual3D()

class MeshCleanup:
    Manual3D = Manual3D()

class Manual3D:
    Collapse = Collapse()

class Collapse:
    def EdgeCollapse(self, crplElemEdge, crlNode):
        message = "MeshCleanup.Manual3D.Collapse.EdgeCollapse({},{})".format(crplElemEdge, crlNode)
        return JPT_RUN_LINE(message)

class Manual3D:
    def DeleteNode(self, crlNode):
        message = "MeshCleanup.Manual3D.DeleteNode({})".format(crlNode)
        return JPT_RUN_LINE(message)

class Manual3D:
    Collapse = Collapse()

class MeshCleanup:
    Manual3D = Manual3D()

class MeshCleanup:
    Manual3D = Manual3D()

class Manual3D:
    def Swap(self, crplElemEdge):
        message = "MeshCleanup.Manual3D.Swap({})".format(crplElemEdge)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual3D = Manual3D()

class Manual3D:
    def Equivalence(self, crlNode, iMergeTowards):
        message = "MeshCleanup.Manual3D.Equivalence({},{})".format(crlNode, iMergeTowards)
        return JPT_RUN_LINE(message)

class Manual3D:
    def Split(self, crplElemEdge, crlNode, dRatioDistance):
        message = "MeshCleanup.Manual3D.Split({},{},{})".format(crplElemEdge, crlNode, dRatioDistance)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual3D = Manual3D()

class Manual3D:
    def CreateHex(self, iParentEntityId, crlElem, iSeprateN):
        message = "MeshCleanup.Manual3D.CreateHex({},{},{})".format(iParentEntityId, crlElem, iSeprateN)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual3D = Manual3D()

class Manual3D:
    def CreatePenta(self, iParentEntityId, crlVcrElem):
        message = "MeshCleanup.Manual3D.CreatePenta({},{})".format(iParentEntityId, crlVcrElem)
        return JPT_RUN_LINE(message)

class Manual3D:
    def CreateTetra(self, iParentEntityId, crlNode, crlElem):
        message = "MeshCleanup.Manual3D.CreateTetra({},{},{})".format(iParentEntityId, crlNode, crlElem)
        return JPT_RUN_LINE(message)

class MeshCleanup:
    Manual3D = Manual3D()

class MeshCleanup:
    Manual3D = Manual3D()

class MeshEdit:
    CreateElement = CreateElement()

class CreateElement:
    def Hex(self, iParentEntityId, crlElem, iSeprateN):
        message = "MeshEdit.CreateElement.Hex({},{},{})".format(iParentEntityId, crlElem, iSeprateN)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateElement = CreateElement()

class CreateElement:
    def Penta(self, iParentEntityId, crlElem):
        message = "MeshEdit.CreateElement.Penta({},{})".format(iParentEntityId, crlElem)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateElement = CreateElement()

class MeshCleanup:
    Manual3D = Manual3D()

class CreateElement:
    def Tet(self, iParentEntityId, crlNode, crlElem):
        message = "MeshEdit.CreateElement.Tet({},{},{})".format(iParentEntityId, crlNode, crlElem)
        return JPT_RUN_LINE(message)

class CreateElement:
    def Tri3(self, iElemType, crParentEntity, crlNode):
        message = "MeshEdit.CreateElement.Tri3({},{},{})".format(iElemType, crParentEntity, crlNode)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateElement = CreateElement()

class CreateElement:
    def Quad4(self, iElemType, crParentEntity, crlNode):
        message = "MeshEdit.CreateElement.Quad4({},{},{})".format(iElemType, crParentEntity, crlNode)
        return JPT_RUN_LINE(message)

class CreateNode:
    def CircleCenter(self, crlEdges,iNodeID, bImprint, crFace):
        message = "MeshEdit.CreateNode.CircleCenter({},{},{},{})".format(crlEdges,iNodeID, bImprint, crFace)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateElement = CreateElement()

class MeshEdit:
    CreateNode = CreateNode()

class CreateNode:
    def Absolute(self, veclNodeCoord, ilNewNodeID):
        message = "MeshEdit.CreateNode.Absolute({},{})".format(veclNodeCoord, ilNewNodeID)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateNode = CreateNode()

class CreateNode:
    def Import(self, strCsvFilePath):
        message = "MeshEdit.CreateNode.Import('{}')".format(strCsvFilePath)
        return JPT_RUN_LINE(message)

class CreateNode:
    def Point(self, iodeID, posPoint, bImprint, crShape):
        message = "MeshEdit.CreateNode.Point({},{},{},{})".format(iodeID, posPoint, bImprint, crShape)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateNode = CreateNode()

class CreateNode:
    def Between2Nodes(self, iNodeID, dX, dY, dZ, iNumberofNodes, bImprint, crlNode, crlFace):
        message = "MeshEdit.CreateNode.Between2Nodes({},{},{},{},{},{},{},{})".format(iNodeID, dX, dY, dZ, iNumberofNodes, bImprint, crlNode, crlFace)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateNode = CreateNode()

class CreateNode:
    def Between3Nodes(self, iNodeID, dX, dY, dZ, bImprint, crlNode, crlFace):
        message = "MeshEdit.CreateNode.Between3Nodes({},{},{},{},{},{},{})".format(iNodeID, dX, dY, dZ, bImprint, crlNode, crlFace)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateNode = CreateNode()

class MeshEdit:
    CreateNode = CreateNode()

class CreateNode:
    def ProjectToPlane(self, dX, dY, dZ, crlNode, crlFace):
        message = "MeshEdit.CreateNode.ProjectToPlane({},{},{},{},{})".format(dX, dY, dZ, crlNode, crlFace)
        return JPT_RUN_LINE(message)

class CreateNode:
    def CenterOfCylinder(self, crlTagetFace, iewNodeKey):
        message = "MeshEdit.CreateNode.CenterOfCylinder({},{})".format(crlTagetFace, iewNodeKey)
        return JPT_RUN_LINE(message)

class CreateNode:
    def CenterOfSphere(self, crlTacrNodesOrFaces, iNodeID):
        message = "MeshEdit.CreateNode.CenterOfSphere({},{})".format(crlTacrNodesOrFaces, iNodeID)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateNode = CreateNode()

class MeshEdit:
    CreateNode = CreateNode()

class CreateNode:
    def Offset(self, vecOffset, iRep, crlCrNodes, crCoord):
        message = "MeshEdit.CreateNode.Offset({},{},{},{})".format(vecOffset, iRep, crlCrNodes, crCoord)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateNode = CreateNode()

class CreateNode:
    def CenterOfGravity(self, iCreationType, iodeID, dX, dY, dZ, crlPart, crlBarPart, crlFace):
        message = "MeshEdit.CreateNode.CenterOfGravity({},{},{},{},{},{},{},{})".format(iCreationType, iodeID, dX, dY, dZ, crlPart, crlBarPart, crlFace)
        return JPT_RUN_LINE(message)

class CreateNode:
    def ProjectToLine(self, crlTa):
        message = "MeshEdit.CreateNode.ProjectToLine({})".format(crlTa)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateNode = CreateNode()

class MeshEdit:
    CreateNode = CreateNode()

class MeshEdit:
    CreateNode = CreateNode()

class CreateNode:
    def IntersectionNode(self, crlFaces,crlBodies,crlEdges,crlNodes):
        message = "MeshEdit.CreateNode.IntersectionNode({},{},{},{})".format(crlFaces,crlBodies,crlEdges,crlNodes)
        return JPT_RUN_LINE(message)

class MoveNode:
    def Point(self, dX, dY, dZ, ilNodeList):
        message = "MeshEdit.MoveNode.Point({},{},{},{})".format(dX, dY, dZ, ilNodeList)
        return JPT_RUN_LINE(message)

class MeshEdit:
    CreateNode = CreateNode()

class MoveNode:
    def ProjectToLine(self, crlRefNodes, crlObjNodes, iType):
        message = "MeshEdit.MoveNode.ProjectToLine({},{},{})".format(crlRefNodes, crlObjNodes, iType)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def ProjectToPlaneElem(self, ilNodeKeys, ilElemKeys):
        message = "MeshEdit.MoveNode.ProjectToPlaneElem({},{})".format(ilNodeKeys, ilElemKeys)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def Equalize(self, crlEdge):
        message = "MeshEdit.MoveNode.Equalize({})".format(crlEdge)
        return JPT_RUN_LINE(message)

class MoveNode:
    def StraightenMidnodes(self, crlPart, crlFace, crlEdge, crlNode):
        message = "MeshEdit.MoveNode.StraightenMidnodes({},{},{},{})".format(crlPart, crlFace, crlEdge, crlNode)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def NormalOffset(self, dMagnitude, ilNodeList):
        message = "MeshEdit.MoveNode.NormalOffset({},{})".format(dMagnitude, ilNodeList)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def CoincidentNodes(self, crlNode, dTol, bDesOrder):
        message = "MeshEdit.MoveNode.CoincidentNodes({},{},{})".format(crlNode, dTol, bDesOrder)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def AlongCylinder(self, crlFace, crlNode, dIrX, dIrY, dIrZ, dCircleX, dCircleY, dCircleZ, dRadius, dHeight):
        message = "MeshEdit.MoveNode.AlongCylinder({},{},{},{},{},{},{},{},{},{})".format(crlFace, crlNode, dIrX, dIrY, dIrZ, dCircleX, dCircleY, dCircleZ, dRadius, dHeight)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def ProjectToPlane_3Nodes(self, ilNodeList):
        message = "MeshEdit.MoveNode.ProjectToPlane_3Nodes({})".format(ilNodeList)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def MoveNodeOffset(self, dDeltaX,dDeltaY,dDeltaZ,crlNode,crCoord):
        message = "MeshEdit.MoveNode.MoveNodeOffset({},{},{},{},{})".format(dDeltaX,dDeltaY,dDeltaZ,crlNode,crCoord)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def RefineQuality(self, iMetric, crlFace, crlElem, crlNode):
        message = "MeshEdit.MoveNode.RefineQuality({},{},{},{})".format(iMetric, crlFace, crlElem, crlNode)
        return JPT_RUN_LINE(message)

class MoveNode:
    def StraightenMidnodes(self, crlPart, crlFace, crlEdge, crlNode):
        message = "MeshEdit.MoveNode.StraightenMidnodes({},{},{},{})".format(crlPart, crlFace, crlEdge, crlNode)
        return JPT_RUN_LINE(message)

class MoveNode:
    def Offset(self, dDeltaX, dDeltaY, dDeltaZ, crCoord, crlNode):
        message = "MeshEdit.MoveNode.Offset({},{},{},{},{})".format(dDeltaX, dDeltaY, dDeltaZ, crCoord, crlNode)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def Laplacian(self, crlTarget, iType, bWithCADFollow):
        message = "MeshEdit.MoveNode.Laplacian({},{},{})".format(crlTarget, iType, bWithCADFollow)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def AlongEdge(self, crlNodes, bMoveX, bMoveY, bMoveZ, dPosX, dPosY, dPosZ, iMoveType):
        message = "MeshEdit.MoveNode.AlongEdge({},{},{},{},{},{},{},{})".format(crlNodes, bMoveX, bMoveY, bMoveZ, dPosX, dPosY, dPosZ, iMoveType)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def AlongDirection(self, crlNodes, crElem, crFace, vecDirection, dMagnitude, bDestination):
        message = "MeshEdit.MoveNode.AlongDirection({},{},{},{},{},{})".format(crlNodes, crElem, crFace, vecDirection, dMagnitude, bDestination)
        return JPT_RUN_LINE(message)

class MoveNode:
    def CADFollows(self, crlNodes, dMovedPosX, dMovedPosY, dMovedPosZ):
        message = "MeshEdit.MoveNode.CADFollows({},{},{},{})".format(crlNodes, dMovedPosX, dMovedPosY, dMovedPosZ)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def Scale(self, crlNode, crlNodeOrigin, crCoord, posDeltaXYZ):
        message = "MeshEdit.MoveNode.Scale({},{},{},{})".format(crlNode, crlNodeOrigin, crCoord, posDeltaXYZ)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MeshEdit:
    MoveNode = MoveNode()

class MoveNode:
    def Absolute(self, dDeltaX, dDeltaY, dDeltaZ, b1stCoord, b2ndCoord, b3rdCoord, crlNode, crCoord):
        message = "MeshEdit.MoveNode.Absolute({},{},{},{},{},{},{},{})".format(dDeltaX, dDeltaY, dDeltaZ, b1stCoord, b2ndCoord, b3rdCoord, crlNode, crCoord)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def Face(crlFaceTarget,crlFaceFixed, iOffsetType, crCoord, dlOffset, dOffset, iDistType, dDistStrong, dDistWeak, iNodeIdPick, dlPickForMacro):
        message = "MeshEdit.Face({},{},{},{},{},{},{},{},{},{},{})".format(crlFaceTarget,crlFaceFixed, iOffsetType, crCoord, dlOffset, dOffset, iDistType, dDistStrong, dDistWeak, iNodeIdPick, dlPickForMacro)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def Deform(crlFaceSrcObverse, crlFaceDstReverse, crlFaceSrcReverse, crlFaceDstObverse, crlFaceFixed, dDistEffect):
        message = "MeshEdit.Deform({},{},{},{},{},{})".format(crlFaceSrcObverse, crlFaceDstReverse, crlFaceSrcReverse, crlFaceDstObverse, crlFaceFixed, dDistEffect)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def ElementConvert(crlPart, iType):
        message = "MeshEdit.ElementConvert({},{})".format(crlPart, iType)
        return JPT_RUN_LINE(message)

class MeshEdit:
    MoveNode = MoveNode()

class MeshEdit:
    def MirrorCopy(crlFaces):
        message = "MeshEdit.MirrorCopy({})".format(crlFaces)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def FaceImprint(crlCrFaces, bMeshCopy):
        message = "MeshEdit.FaceImprint({},{})".format(crlCrFaces, bMeshCopy)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def AdjustOrientation(crlPart, crlFace, crlElem):
        message = "MeshEdit.AdjustOrientation({},{},{})".format(crlPart, crlFace, crlElem)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def OneNode(crlNodes, crlFaceFixed, bOffsetvector, crCoord, dlOffset, dOffset, iDisttype, dDiststrong, dDistweak):
        message = "MeshEdit.OneNode({},{},{},{},{},{},{},'{}',{})".format(crlNodes, crlFaceFixed, bOffsetvector, crCoord, dlOffset, dOffset, iDisttype, dDiststrong, dDistweak)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def SeparateNodes(crlShareNodes, crlTargets, iKeepNodeIDsOn):
        message = "MeshEdit.SeparateNodes({},{},{})".format(crlShareNodes, crlTargets, iKeepNodeIDsOn)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def Import(iSolverType, strFilePath, iStep, dScale):
        message = "MeshEdit.Import({},'{}',{},{})".format(iSolverType, strFilePath, iStep, dScale)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def DeleteNode(crlNodes, bRemoveVertex):
        message = "MeshEdit.DeleteNode({},{})".format(crlNodes, bRemoveVertex)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def RefineQuality(iMetric,crlFace,crlElem,crlNode):
        message = "MeshEdit.RefineQuality({},{},{},{})".format(iMetric,crlFace,crlElem,crlNode)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def MergeNodes(dTolerance, iKeepType, crlTarget, bGroup, bEquivalence):
        message = "MeshEdit.MergeNodes({},{},{},{},{})".format(dTolerance, iKeepType, crlTarget, bGroup, bEquivalence)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def RemoveSolidMesh(crlPart, bConvFirst):
        message = "MeshEdit.RemoveSolidMesh({},{})".format(crlPart, bConvFirst)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def MeshCopy(crlFace, crlNode):
        message = "MeshEdit.MeshCopy({},{})".format(crlFace, crlNode)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def RibThickness(crlFaceMove, crlFaceFixed, dMove, dDistStrong, dDistWeak):
        message = "MeshEdit.RibThickness({},{},{},{},{})".format(crlFaceMove, crlFaceFixed, dMove, dDistStrong, dDistWeak)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def ChangePattern(crlFace, iPatternType):
        message = "MeshEdit.ChangePattern({},{})".format(crlFace, iPatternType)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def SolidMesh(crlPart, iType):
        message = "MeshEdit.SolidMesh({},{})".format(crlPart, iType)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def SurfaceMesh(crlPart, iType):
        message = "MeshEdit.SurfaceMesh({},{})".format(crlPart, iType)
        return JPT_RUN_LINE(message)

class CADProjection:
    def Part(self, iMethod, crCadPart, crMeshedPart, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck):
        message = "Meshing.CADProjection.Part({},{},{},{},{},{},{})".format(iMethod, crCadPart, crMeshedPart, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck)
        return JPT_RUN_LINE(message)

class CADProjection:
    def Face(self, iMethod, crCadPart, crlMeshedFace, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck):
        message = "Meshing.CADProjection.Face({},{},{},{},{},{},{})".format(iMethod, crCadPart, crlMeshedFace, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck)
        return JPT_RUN_LINE(message)

class Meshing:
    CADProjection = CADProjection()

class CADProjection:
    def FaceToFace(self, iMethod, crlCadFace, crlMeshedFace, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck):
        message = "Meshing.CADProjection.FaceToFace({},{},{},{},{},{},{})".format(iMethod, crlCadFace, crlMeshedFace, bForceProject, bProjectCornerNodes, bProjectMidNodes, bIDcheck)
        return JPT_RUN_LINE(message)

class Meshing:
    CADProjection = CADProjection()

class Meshing:
    CADProjection = CADProjection()

class CADProjection:
    def NodeToFace(self, iMethod, crlCadFace, crlMeshedNode, iDirection, iImproveQuality):
        message = "Meshing.CADProjection.NodeToFace({},{},{},{},{})".format(iMethod, crlCadFace, crlMeshedNode, iDirection, iImproveQuality)
        return JPT_RUN_LINE(message)

class Meshing:
    CADProjection = CADProjection()

class LocalMeshing:
    def FilletMapping(self, taFaces, nIsoDiv, dIsoSize, dIsoError):
        message = "Meshing.LocalMeshing.FilletMapping({},{},{},{})".format(taFaces, nIsoDiv, dIsoSize, dIsoError)
        return JPT_RUN_LINE(message)

class CADProjection:
    def NodeToEdge(self, iMethod, crCadEdge, crlMeshedNode, iDirection):
        message = "Meshing.CADProjection.NodeToEdge({},{},{},{})".format(iMethod, crCadEdge, crlMeshedNode, iDirection)
        return JPT_RUN_LINE(message)

class LocalMeshing:
    def SelectFillet(self, crlItems, dSelectWidthMin, dSelectWidthMax, dSelectRMin, dSelectRMax, dAngleMin, dAngleMax, bConvex, bConcave):
        message = "Meshing.LocalMeshing.SelectFillet({},{},{},{},{},{},{},{},{})".format(crlItems, dSelectWidthMin, dSelectWidthMax, dSelectRMin, dSelectRMax, dAngleMin, dAngleMax, bConvex, bConcave)
        return JPT_RUN_LINE(message)

class Meshing:
    LocalMeshing = LocalMeshing()

class Meshing:
    CADProjection = CADProjection()

class LocalSetting:
    def SearchTargetFaces(self, iPartType, dlOrigin, dlLength, dlCenterPt, dlAxisPt1, dlAxisPt2, bEnclosed):
        message = "Meshing.LocalSetting.SearchTargetFaces({},{},{},{},{},{},{})".format(iPartType, dlOrigin, dlLength, dlCenterPt, dlAxisPt1, dlAxisPt2, bEnclosed)
        return JPT_RUN_LINE(message)

class Meshing:
    LocalMeshing = LocalMeshing()

class Templates:
    def TemplateCopy(self, crlReferent, crlTarget, iMethod, iCopySub, dTolerance, strSource, strTarget):
        message = "Meshing.Templates.TemplateCopy({},{},{},{},{},'{}','{}')".format(crlReferent, crlTarget, iMethod, iCopySub, dTolerance, strSource, strTarget)
        return JPT_RUN_LINE(message)

class Meshing:
    LocalSetting = LocalSetting()

class Meshing:
    def BarMeshing(ilVcrCadEdge,ilVcrBarEdge,ilVcrBarPart, dDocMeshSize, iDocNumofElem):
        message = "Meshing.BarMeshing({},{},{},{},{})".format(ilVcrCadEdge,ilVcrBarEdge,ilVcrBarPart, dDocMeshSize, iDocNumofElem)
        return JPT_RUN_LINE(message)

class Meshing:
    def SolidMeshing(crlPart, bTet10, dGradingFactor, bGravCenter, dStretchLimit, iSpeedVsQual, iSpeedVsMem, iRegion, bInternalNodes, bSafeMode, iParallel, bSurfaceNodes, bEdgeNodes, bPreservation, bInternalMeshOnly, bMeshColor, iPartColor):
        message = "Meshing.SolidMeshing({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, bTet10, dGradingFactor, bGravCenter, dStretchLimit, iSpeedVsQual, iSpeedVsMem, iRegion, bInternalNodes, bSafeMode, iParallel, bSurfaceNodes, bEdgeNodes, bPreservation, bInternalMeshOnly, bMeshColor, iPartColor)
        return JPT_RUN_LINE(message)

class Meshing:
    Templates = Templates()

class Meshing:
    def SetAttib(crlPart , surfaceMesh ):
        message = "Meshing.SetAttib({},{})".format(crlPart , surfaceMesh )
        return JPT_RUN_LINE(message)

class Meshing:
    def SurfaceMeshing(crlPart, surfaceMesh, bUseSetting, bFMesher, iThreadNum, bRefData, bMeshColor, iPartColor):
        message = "Meshing.SurfaceMeshing({},{},{},{},{},{},{},{})".format(crlPart, surfaceMesh, bUseSetting, bFMesher, iThreadNum, bRefData, bMeshColor, iPartColor)
        return JPT_RUN_LINE(message)

class LocalRemesh:
    def Solid(self, crlParts, dlCenter, dRadius, dGradFactor, dStrechLimit):
        message = "Meshing.LocalRemesh.Solid({},{},{},{},{})".format(crlParts, dlCenter, dRadius, dGradFactor, dStrechLimit)
        return JPT_RUN_LINE(message)

class LocalRemesh:
    def Surfase(self, crlTarget, surfaceMesh , bUseSetting, bGrading, bFMesher, iOverrideType, bKeepConnection, bProjCAD, bTinyFaceMerge, dMinFaceWidth, dMaxFaceWidth,bIDchcek , bKeepRemeshEdge ):
        message = "Meshing.LocalRemesh.Surfase({},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlTarget, surfaceMesh , bUseSetting, bGrading, bFMesher, iOverrideType, bKeepConnection, bProjCAD, bTinyFaceMerge, dMinFaceWidth, dMaxFaceWidth,bIDchcek , bKeepRemeshEdge )
        return JPT_RUN_LINE(message)

class Meshing:
    LocalRemesh = LocalRemesh()

class LocalSettings:
    def Edge(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.Edge('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

class Meshing:
    LocalRemesh = LocalRemesh()

class LocalSettings:
    def Face(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.Face('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

class Meshing:
    LocalSettings = LocalSettings()

class LocalSettings:
    def FaceElement(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.FaceElement('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

class Meshing:
    LocalSettings = LocalSettings()

class LocalSettings:
    def Model(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.Model('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

class Meshing:
    LocalSettings = LocalSettings()

class LocalSettings:
    def Part(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.Part('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

class Meshing:
    LocalSettings = LocalSettings()

class LocalSettings:
    def Points(self, strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget):
        message = "Meshing.LocalSettings.Points('{}',{},{},{},{},{},{})".format(strName,localMesh, crlTarget, ilHardPointId, veclHardPointXYZ, crlHardPointTarget, crEditTarget)
        return JPT_RUN_LINE(message)

class Meshing:
    LocalSettings = LocalSettings()

class MidPlane:
    def AdjustThickness(crlCrPart, dRatio, bAdjustFaceThick, bAdjustPropThick):
        message = "MidPlane.AdjustThickness({},{},{},{})".format(crlCrPart, dRatio, bAdjustFaceThick, bAdjustPropThick)
        return JPT_RUN_LINE(message)

class Meshing:
    LocalSettings = LocalSettings()

class MidPlane:
    def FaceCross(crlCrBodies, crlCrFaces):
        message = "MidPlane.FaceCross({},{})".format(crlCrBodies, crlCrFaces)
        return JPT_RUN_LINE(message)

class MidPlane:
    def CreateThickProps(crlPart, dThickDiff, dMaxThick, dMinThick, crMatMembrane, crMatBend, crMatShear, crMatCoupl, iMatOrientType, dMatOrientX, dMatOrientY, dMatOrientZ, crCoor, dThickness, dBendStiff, dThickRatio, dNSM, dFiberDist1, dFiberDist2, dPlateOff, iNumInterPts, bThickSetting, iEntityType, bDivideProp, crlRefPart):
        message = "MidPlane.CreateThickProps({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, dThickDiff, dMaxThick, dMinThick, crMatMembrane, crMatBend, crMatShear, crMatCoupl, iMatOrientType, dMatOrientX, dMatOrientY, dMatOrientZ, crCoor, dThickness, dBendStiff, dThickRatio, dNSM, dFiberDist1, dFiberDist2, dPlateOff, iNumInterPts, bThickSetting, iEntityType, bDivideProp, crlRefPart)
        return JPT_RUN_LINE(message)

class MidPlaneEdit:
    Edge = Edge()

class MidPlane:
    def FindMidPlane():
        message = "MidPlane.FindMidPlane({})".format()
        return JPT_RUN_LINE(message)

class Edge:
    def Nodes(self, crlNode):
        message = "MidPlaneEdit.Edge.Nodes({})".format(crlNode)
        return JPT_RUN_LINE(message)

class ExtendFace:
    def CylinderFace(self, crlExtFace, crRefFace, crEdge, iExtendType, iFaceType, iMethod, dParaAngleOffset, dParaArcLength, dParaZxy, iAxisPlane, iParaArcNodesNum, dOffLength, crlSelExtendedFace, crlSelRefFace, dCoMag, iAxisSystem, iCoorSystem, iCoX, iCoY, iCoZ, bOtherSameAsFaceNormal, dOtherArcNodesNum, dOtherArcRadius):
        message = "MidPlaneEdit.ExtendFace.CylinderFace({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlExtFace, crRefFace, crEdge, iExtendType, iFaceType, iMethod, dParaAngleOffset, dParaArcLength, dParaZxy, iAxisPlane, iParaArcNodesNum, dOffLength, crlSelExtendedFace, crlSelRefFace, dCoMag, iAxisSystem, iCoorSystem, iCoX, iCoY, iCoZ, bOtherSameAsFaceNormal, dOtherArcNodesNum, dOtherArcRadius)
        return JPT_RUN_LINE(message)

class MidPlaneEdit:
    ExtendFace = ExtendFace()

class ExtendFace:
    def PlanarFace(self, bIType, crExtFace, crRefFace, crEdge, iFaceType, iExtendType, iMethod, dParaZxy, iAxisPlane, iParaArcNodesNum, dOffLength, dCoMag, iAxisSystem, iCoorSystem, crCoord, iCoX, iCoY, iCoZ, bOtherSameAsFaceNormal, dOtherArcNodesNum, dOtherArcRadius):
        message = "MidPlaneEdit.ExtendFace.PlanarFace({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(bIType, crExtFace, crRefFace, crEdge, iFaceType, iExtendType, iMethod, dParaZxy, iAxisPlane, iParaArcNodesNum, dOffLength, dCoMag, iAxisSystem, iCoorSystem, crCoord, iCoX, iCoY, iCoZ, bOtherSameAsFaceNormal, dOtherArcNodesNum, dOtherArcRadius)
        return JPT_RUN_LINE(message)

class MidPlaneEdit:
    ExtendFace = ExtendFace()

class Face:
    def FaceExtendtoFace(self, crlExtFaces,crlRefFaces,bMergeFace,bMergeEdge,dMergeEdgeAngle):
        message = "MidPlaneEdit.Face.FaceExtendtoFace({},{},{},{},{})".format(crlExtFaces,crlRefFaces,bMergeFace,bMergeEdge,dMergeEdgeAngle)
        return JPT_RUN_LINE(message)

class MidPlaneEdit:
    Face = Face()

class Face:
    def FaceExtendToIntersection(self, crEdge0,crEdge1):
        message = "MidPlaneEdit.Face.FaceExtendToIntersection({},{})".format(crEdge0,crEdge1)
        return JPT_RUN_LINE(message)

class Face:
    def EdgesToEdges(self, crlEdges, bImprint, bMultiEdges):
        message = "MidPlaneEdit.Face.EdgesToEdges({},{},{})".format(crlEdges, bImprint, bMultiEdges)
        return JPT_RUN_LINE(message)

class MidPlaneEdit:
    Face = Face()

class MidPlaneEdit:
    Manual = Manual()

class Manual:
    def vecOffset(self, crlFaces,crPart,dOffset,bCyl,strNewPartName):
        message = "MidPlaneEdit.Manual.vecOffset({},{},{},{},'{}')".format(crlFaces,crPart,dOffset,bCyl,strNewPartName)
        return JPT_RUN_LINE(message)

class Manual:
    def MidByPair(self, crlBaseFaces,crlPairFaces,crlRefFaces,crPart,bMergeFaces,bExtendFaces,bHideFaces,dExtendTol,dMergeEdgesAngle,dStitchFaces):
        message = "MidPlaneEdit.Manual.MidByPair({},{},{},{},{},{},{},{},{},{})".format(crlBaseFaces,crlPairFaces,crlRefFaces,crPart,bMergeFaces,bExtendFaces,bHideFaces,dExtendTol,dMergeEdgesAngle,dStitchFaces)
        return JPT_RUN_LINE(message)

class MidPlaneEdit:
    Manual = Manual()

class MidPlaneEdit:
    Face = Face()

class Edge:
    def ProjectEdgeToFace(self, crlEdge,crlFace, bExtendEdge):
        message = "MidPlaneEdit.AddItems.Edge.ProjectEdgeToFace({},{},{})".format(crlEdge,crlFace, bExtendEdge)
        return JPT_RUN_LINE(message)

class Edge:
    def FaceTwoFace(self, crRefFace, crExtFace, iExtendType):
        message = "MidPlaneEdit.AddItems.Edge.FaceTwoFace({},{},{})".format(crRefFace, crExtFace, iExtendType)
        return JPT_RUN_LINE(message)

class AddItems:
    Edge = Edge()

class MidPlaneEdit:
    AddItems = AddItems()

class MidPlaneEdit:
    AddItems = AddItems()

class AddItems:
    Edge = Edge()

class Face:
    def EFExtendFreeEdge(self, crlEdges,crlFaces,bMergeFace,bMergeEdge,bUseNeighDir,dMergeEdgeAngle,bMultiEF):
        message = "MidPlaneEdit.AddItems.Face.EFExtendFreeEdge({},{},{},{},{},{},{})".format(crlEdges,crlFaces,bMergeFace,bMergeEdge,bUseNeighDir,dMergeEdgeAngle,bMultiEF)
        return JPT_RUN_LINE(message)

class AddItems:
    Face = Face()

class MidPlaneEdit:
    AddItems = AddItems()

class Face:
    def EFProject(self, crlEdges,crlFaces,bMergeFace,bMergeEdge,dMergeEdgeAngle,bMultiEF):
        message = "MidPlaneEdit.AddItems.Face.EFProject({},{},{},{},{},{})".format(crlEdges,crlFaces,bMergeFace,bMergeEdge,dMergeEdgeAngle,bMultiEF)
        return JPT_RUN_LINE(message)

class AddItems:
    Face = Face()

class MidPlaneEdit:
    AddItems = AddItems()

class CreateEdge:
    def PerpendicularLineToEdge(self, crNode,crEdge,crlFace,bBreakFace):
        message = "MufflerHA.CreateEdge.PerpendicularLineToEdge({},{},{},{})".format(crNode,crEdge,crlFace,bBreakFace)
        return JPT_RUN_LINE(message)

class CreateEdgeClassic:
    def ProjectLine(self, ilAiedgeidForMacro,ilAifaceidForMacro,bDivideFace,crlAiparttargetForMarco):
        message = "MufflerHA.CreateEdgeClassic.ProjectLine({},{},{},{})".format(ilAiedgeidForMacro,ilAifaceidForMacro,bDivideFace,crlAiparttargetForMarco)
        return JPT_RUN_LINE(message)

class MufflerHA:
    CreateEdge = CreateEdge()

class MufflerHA:
    CreateEdgeClassic = CreateEdgeClassic()

class MufflerHA:
    def CopyMeshCount(crlMasterEdge,crlSlaveEdge,strBaseName):
        message = "MufflerHA.CopyMeshCount({},{},'{}')".format(crlMasterEdge,crlSlaveEdge,strBaseName)
        return JPT_RUN_LINE(message)

class Rod:
    def Rod(self, crlNode,dRadius,iType,dMeshSize,dStartDist,dWeldDist,iDivNumber,dDeformWidth,iTransitionElem,dlPosDir):
        message = "MufflerT.SpecialModeling.Rod.Rod({},{},{},{},{},{},{},{},{},{})".format(crlNode,dRadius,iType,dMeshSize,dStartDist,dWeldDist,iDivNumber,dDeformWidth,iTransitionElem,dlPosDir)
        return JPT_RUN_LINE(message)

class SpecialModeling:
    Rod = Rod()

class MufflerT:
    SpecialModeling = SpecialModeling()

class CreateWeld:
    def Auto(self, iIconnectattributeMethod,strStrconnectattributeName,crlMasterTarget,crlSlaveTarget,iIconnectattributeCoordsys,crEdit):
        message = "MuxWeld.CreateWeld.Auto({},'{}',{},{},{},{})".format(iIconnectattributeMethod,strStrconnectattributeName,crlMasterTarget,crlSlaveTarget,iIconnectattributeCoordsys,crEdit)
        return JPT_RUN_LINE(message)

class MuxWeld:
    CreateWeld = CreateWeld()

class DefineSequence:
    def Single(self, crEdit):
        message = "MuxWeld.DefineSequence.Single({})".format(crEdit)
        return JPT_RUN_LINE(message)

class MuxWeld:
    DefineSequence = DefineSequence()

class MuxWeld:
    def MeshingPass(crPart,dlTaEdge,dMeshSize):
        message = "MuxWeld.MeshingPass({},{},{})".format(crPart,dlTaEdge,dMeshSize)
        return JPT_RUN_LINE(message)

class MuxWeld:
    def Prop3DWeldBead(strName, crMaterial, crlTarget, crEdit):
        message = "MuxWeld.Prop3DWeldBead('{}',{},{},{})".format(strName, crMaterial, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class LocalMeshing:
    def FilletMapMeshing(self, crlPart, crlFace, dMinLength, dMaxLength, dMinRadius, dMaxRadius, bConvex, bConcave, iTmp, dLengthSingleLayer, dBMinLengthForSingleLayer, dRadiusSingleLayer, dBMinRadiusForSingleLayer, iMinlayer, bMinLayer):
        message = "OasisAWizard.LocalMeshing.FilletMapMeshing({},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlPart, crlFace, dMinLength, dMaxLength, dMinRadius, dMaxRadius, bConvex, bConcave, iTmp, dLengthSingleLayer, dBMinLengthForSingleLayer, dRadiusSingleLayer, dBMinRadiusForSingleLayer, iMinlayer, bMinLayer)
        return JPT_RUN_LINE(message)

class NSModeling:
    def NSModeling_Close_Hole(iType,dMaxLength,bMergeFaces,bSetCenterPoint,crlNodes,crlPart):
        message = "NSModeling.NSModeling_Close_Hole({},{},{},{},{},{})".format(iType,dMaxLength,bMergeFaces,bSetCenterPoint,crlNodes,crlPart)
        return JPT_RUN_LINE(message)

class ImportResults:
    def ImportOp2Mesh(self, strlFilePaths, iMportType, dFaceAngle, dEdgeAngle):
        message = "Post.ImportResults.ImportOp2Mesh('{}',{},{},{})".format(strlFilePaths, iMportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class OasisAWizard:
    LocalMeshing = LocalMeshing()

class Post:
    ImportResults = ImportResults()

class ImportResults:
    def NastranOp2PostJob(self, strName,strlPaths, crEdit):
        message = "Post.ImportResults.NastranOp2PostJob('{}','{}',{})".format(strName,strlPaths, crEdit)
        return JPT_RUN_LINE(message)

class Post:
    ImportResults = ImportResults()

class Post:
    ImportResults = ImportResults()

class ImportResults:
    def ImportTsdbMesh(self, strTsdbFilePath,strBtxFilePath, iMportType, dFaceAngle, dEdgeAngle):
        message = "Post.ImportResults.ImportTsdbMesh('{}','{}',{},{},{})".format(strTsdbFilePath,strBtxFilePath, iMportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class Post:
    ImportResults = ImportResults()

class ImportResults:
    def HDF5Mesh(self, strlFilePaths, iMportType, dFaceAngle, dEdgeAngle):
        message = "Post.ImportResults.HDF5Mesh('{}',{},{},{})".format(strlFilePaths, iMportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class Post:
    ImportResults = ImportResults()

class ImportResults:
    def ADVC(self, strlPath, iMportType, dFaceAngle, dEdgeAngle):
        message = "Post.ImportResults.ADVC('{}',{},{},{})".format(strlPath, iMportType, dFaceAngle, dEdgeAngle)
        return JPT_RUN_LINE(message)

class ImportResults:
    def ADVC2PostJob(self, strName,strlResultFolderPaths,crEdit):
        message = "Post.ImportResults.ADVC2PostJob('{}','{}',{})".format(strName,strlResultFolderPaths,crEdit)
        return JPT_RUN_LINE(message)

class Post:
    ImportResults = ImportResults()

class ImportResults:
    def NastranHDF5(self, strName, strlPaths, crEdit):
        message = "Post.ImportResults.NastranHDF5('{}','{}',{})".format(strName, strlPaths, crEdit)
        return JPT_RUN_LINE(message)

class ElemRelatedInfo:
    def Shell(self, listErishellThetaProp, listErishellCsProp, listErishellZoffsProp):
        message = "Properties.ElemRelatedInfo.Shell({},{},{})".format(listErishellThetaProp, listErishellCsProp, listErishellZoffsProp)
        return JPT_RUN_LINE(message)

class Post:
    ImportResults = ImportResults()

class Properties:
    ElemRelatedInfo = ElemRelatedInfo()

class ElemRelatedInfo:
    def Conn(self, listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds):
        message = "Properties.ElemRelatedInfo.Conn({},{},{},{},{},{},{})".format(listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds)
        return JPT_RUN_LINE(message)

class ElemRelatedInfo:
    def Rod(self, listEnds):
        message = "Properties.ElemRelatedInfo.Rod({})".format(listEnds)
        return JPT_RUN_LINE(message)

class Properties:
    ElemRelatedInfo = ElemRelatedInfo()

class Properties:
    ElemRelatedInfo = ElemRelatedInfo()

class ElemRelatedInfo:
    def Beam(self, listEnds, listOrientVecs, listOrientNodeIds, listOffsetVecsA, listOffsetVecsB, listAs, listBs, listWarps):
        message = "Properties.ElemRelatedInfo.Beam({},{},{},{},{},{},{},{})".format(listEnds, listOrientVecs, listOrientNodeIds, listOffsetVecsA, listOffsetVecsB, listAs, listBs, listWarps)
        return JPT_RUN_LINE(message)

class Properties:
    ElemRelatedInfo = ElemRelatedInfo()

class Properties:
    ElemRelatedInfo = ElemRelatedInfo()

class ElemRelatedInfo:
    def Bar(self, listEnds, listOrientVecs, listOrientNodeIds, listOffsetVecsA, listOffsetVecsB, listAs, listBs, listWarps):
        message = "Properties.ElemRelatedInfo.Bar({},{},{},{},{},{},{},{})".format(listEnds, listOrientVecs, listOrientNodeIds, listOffsetVecsA, listOffsetVecsB, listAs, listBs, listWarps)
        return JPT_RUN_LINE(message)

class Properties:
    ElemRelatedInfo = ElemRelatedInfo()

class ElemRelatedInfo:
    def Gap(self, listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds):
        message = "Properties.ElemRelatedInfo.Gap({},{},{},{},{},{},{})".format(listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds)
        return JPT_RUN_LINE(message)

class ElemRelatedInfo:
    def Bush(self, listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds):
        message = "Properties.ElemRelatedInfo.Bush({},{},{},{},{},{},{})".format(listEnds, listOrientVecs, listCids, listDamperLocs, listOcids, listDamperOffsetVecs, listNodeIds)
        return JPT_RUN_LINE(message)

class Properties:
    Section = Section()

class Section:
    def Import(self, strImportPath):
        message = "Properties.Section.Import('{}')".format(strImportPath)
        return JPT_RUN_LINE(message)

class Section:
    def ModifyGeneral(self, strName, crSection, iSecType, iGeneralType, dA, dB, dH, dT1, dT2, dT3, bTapered, dDaTap, dDbTap, dDhTap, dDt1Tap, dDt2Tap, dDt3Tap):
        message = "Properties.Section.ModifyGeneral('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, crSection, iSecType, iGeneralType, dA, dB, dH, dT1, dT2, dT3, bTapered, dDaTap, dDbTap, dDhTap, dDt1Tap, dDt2Tap, dDt3Tap)
        return JPT_RUN_LINE(message)

class Section:
    def ModifyLibrary(self, strName, crSection, iType, iLibType, dDimSize0, dDimSize1, dDimSize2, dDimSize3, dDimSize4, dDimSize5, dDimSize6, dDimSize7, dDimSize8, dDimSize9, dDimSize10, dDimSize11):
        message = "Properties.Section.ModifyLibrary('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, crSection, iType, iLibType, dDimSize0, dDimSize1, dDimSize2, dDimSize3, dDimSize4, dDimSize5, dDimSize6, dDimSize7, dDimSize8, dDimSize9, dDimSize10, dDimSize11)
        return JPT_RUN_LINE(message)

class Properties:
    ElemRelatedInfo = ElemRelatedInfo()

class Properties:
    Section = Section()

class Section:
    def ModifySketcher(self, strName, crSection, iType):
        message = "Properties.Section.ModifySketcher('{}',{},{})".format(strName, crSection, iType)
        return JPT_RUN_LINE(message)

class Properties:
    Section = Section()

class Properties:
    Section = Section()

class Section:
    def Export(self, strExportSavePath):
        message = "Properties.Section.Export('{}')".format(strExportSavePath)
        return JPT_RUN_LINE(message)

class Properties:
    Section = Section()

class Properties:
    Section = Section()

class Section:
    def AddGeneral(self, strName, iSecType, iSecGenType, dDsecGensizeA, dDsecGensizeB, dDsecGensizeH, dDsecGensizeT1, dDsecGensizeT2, dDsecGensizeT3, bBsecTapered, dDsecGensizeATap, dDsecGensizeBTap, dDsecGensizeHTap, dDsecGensizeT1Tap, dDsecGensizeT2Tap, dDsecGensizeT3Tap):
        message = "Properties.Section.AddGeneral('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iSecType, iSecGenType, dDsecGensizeA, dDsecGensizeB, dDsecGensizeH, dDsecGensizeT1, dDsecGensizeT2, dDsecGensizeT3, bBsecTapered, dDsecGensizeATap, dDsecGensizeBTap, dDsecGensizeHTap, dDsecGensizeT1Tap, dDsecGensizeT2Tap, dDsecGensizeT3Tap)
        return JPT_RUN_LINE(message)

class Section:
    def AddLibrary(self, strName, iSecType, iLibType, dDim1, dDim2, dDim3, dDim4, dDim5, dDim6, dDim7, dDim8, dDim9, dDim10, dDim11, dDim12):
        message = "Properties.Section.AddLibrary('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iSecType, iLibType, dDim1, dDim2, dDim3, dDim4, dDim5, dDim6, dDim7, dDim8, dDim9, dDim10, dDim11, dDim12)
        return JPT_RUN_LINE(message)

class Section:
    def Delete(self, crlSection):
        message = "Properties.Section.Delete({})".format(crlSection)
        return JPT_RUN_LINE(message)

class Properties:
    Section = Section()

class Section:
    def AddSketcher(self, strName, iSecType):
        message = "Properties.Section.AddSketcher('{}',{})".format(strName, iSecType)
        return JPT_RUN_LINE(message)

class Properties:
    Section = Section()

class Properties:
    Section = Section()

class Properties:
    def Cohesive(strName,crMaterial,iResponse,bSpecifyThick,dInitialThick,crlTarget, crEdit, iFLG, iId, iSolverType, iADVCResponseType, iADVCStackDir, iBADVCThickness, dADVCThickness):
        message = "Properties.Cohesive('{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName,crMaterial,iResponse,bSpecifyThick,dInitialThick,crlTarget, crEdit, iFLG, iId, iSolverType, iADVCResponseType, iADVCStackDir, iBADVCThickness, dADVCThickness)
        return JPT_RUN_LINE(message)

class Properties:
    def Gasket(strName,crMaterial,dThickX,dThickY,dThickZ,crlTarget, crEdit, iStData, iFLG):
        message = "Properties.Gasket('{}',{},{},{},{},{},{},{},{})".format(strName,crMaterial,dThickX,dThickY,dThickZ,crlTarget, crEdit, iStData, iFLG)
        return JPT_RUN_LINE(message)

class Properties:
    def Beam(strNewName, iPId, crSection, iShapeDataType, crMat, dArea, dlVecOrient, dlVecInertia, dTorConst, dNSM, dNSMA, dNSMB, dNSMNode1, dNSMNode2, dNSMNode3, dNSMNode4, dShearStiffnessK1, dShearStiffnessK2, dShearAreaReliefS1, dShearAreaReliefS2, dWrapCoeff1, dWrapCoeff2, dNA1, dNA2, dNA3, dNA4, dStressRecoveryCoeffCy, dStressRecoveryCoeffCz, dStressRecoveryCoeffDy, dStressRecoveryCoeffDz, dStressRecoveryCoeffEy, dStressRecoveryCoeffEz, dStressRecoveryCoeffFy, dStressRecoveryCoeffFz, bPinA1, bPinA2, bPinA3, bPinA4, bPinA5, bPinA6, bPinB1, bPinB2, bPinB3, bPinB4, bPinB5, bPinB6, dlOffsetA, dlOffsetB, iLengthUnit, iMassUnit, crlTarget, crEdit, bTapped, dTapArea, dlVecTapInertia, dTapTorConst, dTapNSM, dTapStressRecoveryCoeffCy, dTapStressRecoveryCoeffCz, dTapStressRecoveryCoeffDy, dTapStressRecoveryCoeffDz, dTapStressRecoveryCoeffEy, dTapStressRecoveryCoeffEz, dTapStressRecoveryCoeffFy, dTapStressRecoveryCoeffFz, iIntePtNum):
        message = "Properties.Beam('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strNewName, iPId, crSection, iShapeDataType, crMat, dArea, dlVecOrient, dlVecInertia, dTorConst, dNSM, dNSMA, dNSMB, dNSMNode1, dNSMNode2, dNSMNode3, dNSMNode4, dShearStiffnessK1, dShearStiffnessK2, dShearAreaReliefS1, dShearAreaReliefS2, dWrapCoeff1, dWrapCoeff2, dNA1, dNA2, dNA3, dNA4, dStressRecoveryCoeffCy, dStressRecoveryCoeffCz, dStressRecoveryCoeffDy, dStressRecoveryCoeffDz, dStressRecoveryCoeffEy, dStressRecoveryCoeffEz, dStressRecoveryCoeffFy, dStressRecoveryCoeffFz, bPinA1, bPinA2, bPinA3, bPinA4, bPinA5, bPinA6, bPinB1, bPinB2, bPinB3, bPinB4, bPinB5, bPinB6, dlOffsetA, dlOffsetB, iLengthUnit, iMassUnit, crlTarget, crEdit, bTapped, dTapArea, dlVecTapInertia, dTapTorConst, dTapNSM, dTapStressRecoveryCoeffCy, dTapStressRecoveryCoeffCz, dTapStressRecoveryCoeffDy, dTapStressRecoveryCoeffDz, dTapStressRecoveryCoeffEy, dTapStressRecoveryCoeffEz, dTapStressRecoveryCoeffFy, dTapStressRecoveryCoeffFz, iIntePtNum)
        return JPT_RUN_LINE(message)

class Properties:
    def PropertyTable(listItems):
        message = "Properties.PropertyTable({})".format(listItems)
        return JPT_RUN_LINE(message)

class Properties:
    def Shell(strName, iPID, crMatMembrane, crMatBend, crMatShear, crMatCoupl, dMatOrient1, dMatOrient2, dMatOrient3, dThickness, dBendStiff, dThickRatio, dNSM, dFiberDist1, dFiberDist2, dPlateOff, iItgPts, iMatOrientType, crLocalCS, crlTarget, crEdit, iDuplicateOpt):
        message = "Properties.Shell('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPID, crMatMembrane, crMatBend, crMatShear, crMatCoupl, dMatOrient1, dMatOrient2, dMatOrient3, dThickness, dBendStiff, dThickRatio, dNSM, dFiberDist1, dFiberDist2, dPlateOff, iItgPts, iMatOrientType, crLocalCS, crlTarget, crEdit, iDuplicateOpt)
        return JPT_RUN_LINE(message)

class Properties:
    def Rod(strName, iId, crSection, crMat, dArea, dTorConst, dTorStressCoeff, dNSM, iLocalLengthUnit, iLocalMassUnit, crlTarget, crEdit):
        message = "Properties.Rod('{}',{},{},{},{},{},{},{},{},{},{},{})".format(strName, iId, crSection, crMat, dArea, dTorConst, dTorStressCoeff, dNSM, iLocalLengthUnit, iLocalMassUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Properties:
    def Solid(strName, iPID, crMaterial, iCordM, iIN, iOutLoc, iISOP, iFLflag, iModifiedElem, iModifiedElemADVC, bHasDynaRemesh, dDynaRemeshVal1, dDynaRemeshVal2, iAbaqusPropHGtype, dDispHG, crlTarget, crEdit, iFLG):
        message = "Properties.Solid('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iPID, crMaterial, iCordM, iIN, iOutLoc, iISOP, iFLflag, iModifiedElem, iModifiedElemADVC, bHasDynaRemesh, dDynaRemeshVal1, dDynaRemeshVal2, iAbaqusPropHGtype, dDispHG, crlTarget, crEdit, iFLG)
        return JPT_RUN_LINE(message)

class Properties:
    def Section1D(strName, iSecType, iSecGentype, dSecGensizeA, dSecGensizeB, dSecGensizeH, dSecGensizeT1, dSecGensizeT2, dSecGensizeT3, bSecTapered, dSecGensizeATap, dSecGensizeBTap, dSecGensizeHTap, dSecGensizeT1Tap, dSecGensizeT2Tap, dSecGensizeT3Tap):
        message = "Properties.Section1D('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iSecType, iSecGentype, dSecGensizeA, dSecGensizeB, dSecGensizeH, dSecGensizeT1, dSecGensizeT2, dSecGensizeT3, bSecTapered, dSecGensizeATap, dSecGensizeBTap, dSecGensizeHTap, dSecGensizeT1Tap, dSecGensizeT2Tap, dSecGensizeT3Tap)
        return JPT_RUN_LINE(message)

class Properties:
    def BAR(strName, iId, crSection, iShapeDataType, crDatacrMat, dDatadArea, dlDataOrient, dlDataInertia, dDatadTorConst, dDatadNSM, dDataShearAreaFactor0, dDataShearAreaFactor1, dDataStressRecoveryCoeff0, dDataStressRecoveryCoeff1, dDataStressRecoveryCoeff2, dDataStressRecoveryCoeff3, dDataStressRecoveryCoeff4, dDataStressRecoveryCoeff5, dDataStressRecoveryCoeff6, dDataStressRecoveryCoeff7, bDataPinA0, bDataPinA1, bDataPinA2, bDataPinA3, bDataPinA4, bDataPinA5, bDataPinB0, bDataPinB1, bDataPinB2, bDataPinB3, bDataPinB4, bDataPinB5, dlDataOffset0, dlDataOffset1, iLocalLengthUnit, iLocalMassUnit, crlTarget, crEdit):
        message = "Properties.BAR('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iId, crSection, iShapeDataType, crDatacrMat, dDatadArea, dlDataOrient, dlDataInertia, dDatadTorConst, dDatadNSM, dDataShearAreaFactor0, dDataShearAreaFactor1, dDataStressRecoveryCoeff0, dDataStressRecoveryCoeff1, dDataStressRecoveryCoeff2, dDataStressRecoveryCoeff3, dDataStressRecoveryCoeff4, dDataStressRecoveryCoeff5, dDataStressRecoveryCoeff6, dDataStressRecoveryCoeff7, bDataPinA0, bDataPinA1, bDataPinA2, bDataPinA3, bDataPinA4, bDataPinA5, bDataPinB0, bDataPinB1, bDataPinB2, bDataPinB3, bDataPinB4, bDataPinB5, dlDataOffset0, dlDataOffset1, iLocalLengthUnit, iLocalMassUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Properties:
    def Property1DBeamSimple(strName,iId, crSection, crMat, vecOrient, crlTarget, crEdit):
        message = "Properties.Property1DBeamSimple('{}',{},{},{},{},{},{})".format(strName,iId, crSection, crMat, vecOrient, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Properties:
    def Composite(strName, iDFT, dGE, iDLAM, crMat, dNSM, iDPID, dSB, iDSOUT, dTREF, dZ0, dZOFF, crlTarget, crEdit, crDcrLocalCS, iDmatOrientType, vecDmatOrient):
        message = "Properties.Composite('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iDFT, dGE, iDLAM, crMat, dNSM, iDPID, dSB, iDSOUT, dTREF, dZ0, dZOFF, crlTarget, crEdit, crDcrLocalCS, iDmatOrientType, vecDmatOrient)
        return JPT_RUN_LINE(message)

class Properties:
    def RigidBody(strName, iId, iRefNodeId, crlTarget, crEdit):
        message = "Properties.RigidBody('{}',{},{},{},{})".format(strName, iId, iRefNodeId, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Properties:
    def ThicknessDistribution(dMax, dMin, iByEach, dlTaThicknessValueSet):
        message = "Properties.ThicknessDistribution({},{},{},{})".format(dMax, dMin, iByEach, dlTaThicknessValueSet)
        return JPT_RUN_LINE(message)

class DropTest:
    def CalcTimestep(self, dRelevantElemRate,dChangeMassRage):
        message = "SNOnePush.DropTest.CalcTimestep({},{})".format(dRelevantElemRate,dChangeMassRage)
        return JPT_RUN_LINE(message)

class DropTest:
    def UpdateFloor(self, strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat):
        message = "SNOnePush.DropTest.UpdateFloor('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

class SNOnePush:
    DropTest = DropTest()

class DropTest:
    def DropRotation(self, strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat):
        message = "SNOnePush.DropTest.DropRotation('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

class SNOnePush:
    DropTest = DropTest()

class DropTest:
    def DropRotation(self, strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat):
        message = "SNOnePush.DropTest.DropRotation('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

class SNOnePush:
    DropTest = DropTest()

class SNOnePush:
    def CADImport(dDsurfaceplaneTolerance,dDsurfaceplaneAngle,dMaxFacetWidth,bBnxMultipart,dChordHeightTolerance,dAngleToleranceDegree,iConvertIsolatedCurve,iIigesFixedcurevepreference,iIigesAutostitch,dDigesStitchtolerance,iIcatiaConvertnotshowedelement,iIcatiaConvertnotshowedinstance,iIcatiaConvertaxis,iIstepCreateseam,dDstepPointtolerance,iIacisHealacisbeforeversion,iIjtConvertgeometrytype,iIjtConvertgeneralpart,iIjtConvertaxis,iIjtConvertcenterline,dDcreoChordheighttolerance,dDcreoAngletolerancedegree,strAbsCreoPath,iTransType,iFileType,strFilePath,bRenameDuplicateName,strCSVFilePath):
        message = "SNOnePush.CADImport({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},'{}',{},'{}')".format(dDsurfaceplaneTolerance,dDsurfaceplaneAngle,dMaxFacetWidth,bBnxMultipart,dChordHeightTolerance,dAngleToleranceDegree,iConvertIsolatedCurve,iIigesFixedcurevepreference,iIigesAutostitch,dDigesStitchtolerance,iIcatiaConvertnotshowedelement,iIcatiaConvertnotshowedinstance,iIcatiaConvertaxis,iIstepCreateseam,dDstepPointtolerance,iIacisHealacisbeforeversion,iIjtConvertgeometrytype,iIjtConvertgeneralpart,iIjtConvertaxis,iIjtConvertcenterline,dDcreoChordheighttolerance,dDcreoAngletolerancedegree,strAbsCreoPath,iTransType,iFileType,strFilePath,bRenameDuplicateName,strCSVFilePath)
        return JPT_RUN_LINE(message)

class SNOnePush:
    DropTest = DropTest()

class SNOnePush:
    def DropTestSNOnePush(strName, iDir, dRopHeight, dSolutionTime, iNumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat):
        message = "SNOnePush.DropTestSNOnePush('{}',{},{},{},{},{},{},{},{},{},{},'{}',{},{},{})".format(strName, iDir, dRopHeight, dSolutionTime, iNumOutput, dContactFriction, iRotAxis, dRotAngle, dRelevantElemRate, dChangeMassRate, dMinTimeStep, strSolverFile, dFloorSize, bRename, crMat)
        return JPT_RUN_LINE(message)

class SNOnePush:
    def AutoSweepClosedLoopShaped(crlPart,dMeshSize,dLengthSize):
        message = "SNOnePush.AutoSweepClosedLoopShaped({},{},{})".format(crlPart,dMeshSize,dLengthSize)
        return JPT_RUN_LINE(message)

class StiffCalc:
    def Force(strName,poslForce,poslMoment,iEnArrowDir,iEnDistrbute,crCurCoord,crTable,crNodeSet,dFPhase,dFDelay,crPhaseTable,strFormula0,strFormula1,strFormula2,strFormula3,strFormula4,strFormula5,crlTarget,crEdit):
        message = "StiffCalc.Force('{}',{},{},{},'{}',{},{},{},{},{},{},'{}','{}','{}','{}','{}','{}',{},{})".format(strName,poslForce,poslMoment,iEnArrowDir,iEnDistrbute,crCurCoord,crTable,crNodeSet,dFPhase,dFDelay,crPhaseTable,strFormula0,strFormula1,strFormula2,strFormula3,strFormula4,strFormula5,crlTarget,crEdit)
        return JPT_RUN_LINE(message)

class SZOnepushReliability:
    Assembly = Assembly()

class SZOnepushReliability:
    Assembly = Assembly()

class Assembly:
    def CreateWeld(self, crlWelds,dMeshSize,iRrate,dFilletRadius):
        message = "SZOnepushReliability.Assembly.CreateWeld({},{},{},{})".format(crlWelds,dMeshSize,iRrate,dFilletRadius)
        return JPT_RUN_LINE(message)

class MeshEdit:
    def FilletMapping(self, crlPart,crlFace,dMinRadius,dMaxRadius,dMinAngle,dMaxAngle,bConvex,bConcave):
        message = "SZOnepushReliability.MeshEdit.FilletMapping({},{},{},{},{},{},{},{})".format(crlPart,crlFace,dMinRadius,dMaxRadius,dMinAngle,dMaxAngle,bConvex,bConcave)
        return JPT_RUN_LINE(message)

class SZOnepushReliability:
    MeshEdit = MeshEdit()

class Assembly:
    def ContactSurface(self, crlSrcFace,crlTarPart,dTolerance,iLayer):
        message = "SZOnepushReliability.Assembly.ContactSurface({},{},{},{})".format(crlSrcFace,crlTarPart,dTolerance,iLayer)
        return JPT_RUN_LINE(message)

class Connection:
    def RRod(self, rbarConnection, iUlDOFs, dTol, crlMasterTarget, crlSlaveTarget):
        message = "Test.Connection.RRod({},{},{},{},{})".format(rbarConnection, iUlDOFs, dTol, crlMasterTarget, crlSlaveTarget)
        return JPT_RUN_LINE(message)

class Muffler:
    def ProjectLineForWeld(self, crlEdge,crlFace):
        message = "Test.Muffler.ProjectLineForWeld({},{})".format(crlEdge,crlFace)
        return JPT_RUN_LINE(message)

class Test:
    Connection = Connection()

class SZOnepushReliability:
    def AlignMidNode(crlSource,crlTarget):
        message = "SZOnepushReliability.AlignMidNode({},{})".format(crlSource,crlTarget)
        return JPT_RUN_LINE(message)

class ZGeometryTest:
    def IntersectionCheck(self, crlPart,crlFace,crlElem,iType):
        message = "Test.ZGeometryTest.IntersectionCheck({},{},{},{})".format(crlPart,crlFace,crlElem,iType)
        return JPT_RUN_LINE(message)

class Test:
    Muffler = Muffler()

class Test:
    ZGeometryTest = ZGeometryTest()

class ZGeometryTest:
    def ShellAssy(self, taPart, taFace, _iMeshType, _bSelfIntersection, _iMethod, _dGapTol):
        message = "Test.ZGeometryTest.ShellAssy({},{},{},{},{},{})".format(taPart, taFace, _iMeshType, _bSelfIntersection, _iMethod, _dGapTol)
        return JPT_RUN_LINE(message)

class Test:
    def FindFacesInPart(crPart,strIdentical):
        message = "Test.FindFacesInPart({},'{}')".format(crPart,strIdentical)
        return JPT_RUN_LINE(message)

class Test:
    def CreateElementForWelding(crlSrcElems,crlDstElems,crlSideElems,crlPart,crMaterial):
        message = "Test.CreateElementForWelding({},{},{},{},{})".format(crlSrcElems,crlDstElems,crlSideElems,crlPart,crMaterial)
        return JPT_RUN_LINE(message)

class Connections:
    def Contact(self, strName, iContactType, dInterferenceClosure, dFrictionCoefficient, iShellOffset, iMasterShellOrientation, iSlaveShellOrientation, iMarkerColor, bInitialAdjustment, crlMaster, crlSlave, crMasterGroup, crSlaveGroup, crEdit):
        message = "Tool.Connections.Contact('{}',{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactType, dInterferenceClosure, dFrictionCoefficient, iShellOffset, iMasterShellOrientation, iSlaveShellOrientation, iMarkerColor, bInitialAdjustment, crlMaster, crlSlave, crMasterGroup, crSlaveGroup, crEdit)
        return JPT_RUN_LINE(message)

class Test:
    ZGeometryTest = ZGeometryTest()

class Tool:
    Connections = Connections()

class Connections:
    def Spring(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Tool.Connections.Spring({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class Tool:
    Connections = Connections()

class Tool:
    Connections = Connections()

class Connections:
    def RBE3(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly):
        message = "Tool.Connections.RBE3({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, posVirtualNodePos, iSurfaceDef, crEdit, bUpdateDispCS, bCornerOnly)
        return JPT_RUN_LINE(message)

class Connections:
    def Mass(self, strName, crlTargetNodes, dMass, iDof, crEdit):
        message = "Tool.Connections.Mass('{}',{},{},{},{})".format(strName, crlTargetNodes, dMass, iDof, crEdit)
        return JPT_RUN_LINE(message)

class Coordinates:
    def CylinderFace(self, strName, iCoordType, crFace):
        message = "Tool.Coordinates.CylinderFace('{}',{},{})".format(strName, iCoordType, crFace)
        return JPT_RUN_LINE(message)

class Tool:
    Connections = Connections()

class Tool:
    Coordinates = Coordinates()

class Coordinates:
    def ThreeNode(self, strName, iCoordType, iOrder, crlNodes, veclPoints, crRefCoord, crEdit):
        message = "Tool.Coordinates.ThreeNode('{}',{},{},{},{},{},{})".format(strName, iCoordType, iOrder, crlNodes, veclPoints, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

class Coordinates:
    def Align(self, strName, iCoordType, iCoordAxis, bCreateNew, crlNodes, crEdge, crEdit):
        message = "Tool.Coordinates.Align('{}',{},{},{},{},{},{})".format(strName, iCoordType, iCoordAxis, bCreateNew, crlNodes, crEdge, crEdit)
        return JPT_RUN_LINE(message)

class Tool:
    Coordinates = Coordinates()

class Tool:
    Coordinates = Coordinates()

class Coordinates:
    def vecOffset(self, strName, iCoordType, vTranslate, bCreateNew, crRefCoord, crEdit):
        message = "Tool.Coordinates.vecOffset('{}',{},{},{},{},{})".format(strName, iCoordType, vTranslate, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

class Coordinates:
    def Rotate(self, strName, iCoordType, vecRotate, bCreateNew, crRefCoord, crEdit):
        message = "Tool.Coordinates.Rotate('{}',{},{},{},{},{})".format(strName, iCoordType, vecRotate, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

class Coordinates:
    def AttachCircle(self, strName, iCoordType, crEdge, bCreateNew, crRefCoord, crEdit):
        message = "Tool.Coordinates.AttachCircle('{}',{},{},{},{},{})".format(strName, iCoordType, crEdge, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

class Tool:
    Coordinates = Coordinates()

class Tool:
    Coordinates = Coordinates()

class Coordinates:
    def AttachNode(self, strName, iCoordType, crNode, bCreateNew, crRefCoord, crEdit):
        message = "Tool.Coordinates.AttachNode('{}',{},{},{},{},{})".format(strName, iCoordType, crNode, bCreateNew, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

class Coordinates:
    def Face(self, strName, iCoordType, iOrder, veclPoint, crlNodes, crItem, crRefCoord, crEdit):
        message = "Tool.Coordinates.Face('{}',{},{},{},{},{},{},{})".format(strName, iCoordType, iOrder, veclPoint, crlNodes, crItem, crRefCoord, crEdit)
        return JPT_RUN_LINE(message)

class Tool:
    Coordinates = Coordinates()

class Tool:
    Coordinates = Coordinates()

class Group:
    def DeleteGroupEntity(self, crlDelGroup):
        message = "Tool.Group.DeleteGroupEntity({})".format(crlDelGroup)
        return JPT_RUN_LINE(message)

class Tool:
    Group = Group()

class ImprintEdges:
    def Line(self, veclAvPoint, bDivideFace, crlPartTarget):
        message = "Tool.ImprintEdges.Line({},{},{})".format(veclAvPoint, bDivideFace, crlPartTarget)
        return JPT_RUN_LINE(message)

class Tool:
    ImprintEdges = ImprintEdges()

class ImprintEdges:
    def ClosedLine(self, veclPositions,crlCrTargetFace,iBBreakFace):
        message = "Tool.ImprintEdges.ClosedLine({},{},{})".format(veclPositions,crlCrTargetFace,iBBreakFace)
        return JPT_RUN_LINE(message)

class Tool:
    ImprintEdges = ImprintEdges()

class ImprintEdges:
    def ClosedLine2(self, poslPointPos,bDivide, crlPartTarges):
        message = "Tool.ImprintEdges.ClosedLine2({},{},{})".format(poslPointPos,bDivide, crlPartTarges)
        return JPT_RUN_LINE(message)

class Tool:
    def ElementCS(iMethod, iDispType, bDispXDir, bDispCoord, dDispScale, crlTarget):
        message = "Tool.ElementCS({},{},{},{},{},{})".format(iMethod, iDispType, bDispXDir, bDispCoord, dDispScale, crlTarget)
        return JPT_RUN_LINE(message)

class Tool:
    ImprintEdges = ImprintEdges()

class Angle:
    def ProjectedNode(self, crNode, strTarget, iPrecision):
        message = "Tool.Measure.Angle.ProjectedNode({},'{}',{})".format(crNode, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Tool:
    Coordinates = Coordinates()

class Tool:
    Measure = Measure()

class Angle:
    def TwoNodesAxis(self, crNode1,crNode2,dlAxis,strTarget,iPrecision):
        message = "Tool.Measure.Angle.TwoNodesAxis({},{},{},'{}',{})".format(crNode1,crNode2,dlAxis,strTarget,iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Angle = Angle()

class Tool:
    Measure = Measure()

class Angle:
    def By2Axis(self, xyz1, xyz2, target, Precision):
        message = "Tool.Measure.Angle.By2Axis({},{},{},{})".format(xyz1, xyz2, target, Precision)
        return JPT_RUN_LINE(message)

class Measure:
    Angle = Angle()

class Tool:
    Measure = Measure()

class Measure:
    Angle = Angle()

class Distance:
    def Edge(self, crEdge, option, iPrecision):
        message = "Tool.Measure.Distance.Edge({},{},{})".format(crEdge, option, iPrecision)
        return JPT_RUN_LINE(message)

class Tool:
    Measure = Measure()

class Measure:
    Distance = Distance()

class Distance:
    def EdgeNode(self, crPoint,crEdge, option, iPrecision):
        message = "Tool.Measure.Distance.EdgeNode({},{},{},{})".format(crPoint,crEdge, option, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Distance = Distance()

class Tool:
    Measure = Measure()

class Distance:
    def TwoPoints(self, posPoint1, posPoint2, iPrecision):
        message = "Tool.Measure.Distance.TwoPoints({},{},{})".format(posPoint1, posPoint2, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Distance = Distance()

class Tool:
    Measure = Measure()

class Distance:
    def LineNode(self, crlTargetNode, iPrecision):
        message = "Tool.Measure.Distance.LineNode({},{})".format(crlTargetNode, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Distance = Distance()

class Tool:
    Measure = Measure()

class Distance:
    def Plane3NodesToNode(self, crNode, crNode1, crNode2, crNode3, iPrecision):
        message = "Tool.Measure.Distance.Plane3NodesToNode({},{},{},{},{})".format(crNode, crNode1, crNode2, crNode3, iPrecision)
        return JPT_RUN_LINE(message)

class Tool:
    Measure = Measure()

class Measure:
    Distance = Distance()

class Distance:
    def TwoEdges(self, crEdge1,crEdge2,iOptions,iPrecision):
        message = "Tool.Measure.Distance.TwoEdges({},{},{},{})".format(crEdge1,crEdge2,iOptions,iPrecision)
        return JPT_RUN_LINE(message)

class Distance:
    def PlaneElemToNode(self, crNode, crElem, iPrecision):
        message = "Tool.Measure.Distance.PlaneElemToNode({},{},{})".format(crNode, crElem, iPrecision)
        return JPT_RUN_LINE(message)

class Tool:
    Measure = Measure()

class Measure:
    Distance = Distance()

class Measure:
    Distance = Distance()

class Distance:
    def TwoNodes(self, crNode1,crNode2,iPrecision):
        message = "Tool.Measure.Distance.TwoNodes({},{},{})".format(crNode1,crNode2,iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Distance = Distance()

class Tool:
    Measure = Measure()

class Tool:
    Measure = Measure()

class Distance:
    def FaceNode(self, crlFace,crlNode,iPrecision):
        message = "Tool.Measure.Distance.FaceNode({},{},{})".format(crlFace,crlNode,iPrecision)
        return JPT_RUN_LINE(message)

class Tool:
    Measure = Measure()

class Measure:
    Distance = Distance()

class Tool:
    Measure = Measure()

class Mass:
    def ByMaterial(self, crlPart,strDensity,strTarget,iPrecision):
        message = "Tool.Measure.Mass.ByMaterial({},'{}','{}',{})".format(crlPart,strDensity,strTarget,iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Mass = Mass()

class Measure:
    Radius = Radius()

class Radius:
    def ByThreeNodes(self, crNode1_3,crNode2_3,crNode3_3,iPrecision):
        message = "Tool.Measure.Radius.ByThreeNodes({},{},{},{})".format(crNode1_3,crNode2_3,crNode3_3,iPrecision)
        return JPT_RUN_LINE(message)

class Radius:
    def MeasureRadiusBy3Nodes(self, crNode1_3,crNode2_3,crNode3_3,iPrecision):
        message = "Tool.Measure.Radius.MeasureRadiusBy3Nodes({},{},{},{})".format(crNode1_3,crNode2_3,crNode3_3,iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Radius = Radius()

class Tool:
    Measure = Measure()

class Measure:
    def Volume(self, crlParts, iPrecision):
        message = "Tool.Measure.Volume({},{})".format(crlParts, iPrecision)
        return JPT_RUN_LINE(message)

class Tool:
    Measure = Measure()

class Tool:
    Measure = Measure()

class Manual:
    def CleanTetCollapse(self, crlElem,iKeep,iCheckCondition,dLimitValue,iCleanupMode):
        message = "Tool.MeshQuality.Manual.CleanTetCollapse({},{},{},{},{})".format(crlElem,iKeep,iCheckCondition,dLimitValue,iCleanupMode)
        return JPT_RUN_LINE(message)

class MeshQuality:
    Manual = Manual()

class Manual:
    def CleaningVolumeMesh(self, crlPart,crlElem,dLimitVolume,iMode):
        message = "Tool.MeshQuality.Manual.CleaningVolumeMesh({},{},{},{})".format(crlPart,crlElem,dLimitVolume,iMode)
        return JPT_RUN_LINE(message)

class MeshQuality:
    Manual = Manual()

class Tool:
    MeshQuality = MeshQuality()

class Toolbar:
    def Redo(iCntRedo):
        message = "Toolbar.Redo({})".format(iCntRedo)
        return JPT_RUN_LINE(message)

class Tool:
    MeshQuality = MeshQuality()

class Toolbar:
    def Undo(iCntUndo):
        message = "Toolbar.Undo({})".format(iCntUndo)
        return JPT_RUN_LINE(message)

class BySelection:
    def SelectionOrder(self, crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending):
        message = "Tools.BySelection.SelectionOrder({},{},{},{},{},{})".format(crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending)
        return JPT_RUN_LINE(message)

class BySelection:
    def Position(self, crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending1, bAscending2, bAscending3, iSortFirst, iSortSecond, iSortThird, iBSortFirst, iBSortSecond, iBSortThird, iOffset1, iOffset2, iOffset3, dTol1, dTol2, dTol3, crCoord, bSpecialFace):
        message = "Tools.BySelection.Position({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending1, bAscending2, bAscending3, iSortFirst, iSortSecond, iSortThird, iBSortFirst, iBSortSecond, iBSortThird, iOffset1, iOffset2, iOffset3, dTol1, dTol2, dTol3, crCoord, bSpecialFace)
        return JPT_RUN_LINE(message)

class Tools:
    BySelection = BySelection()

class BySelection:
    def OriginalID(self, crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending):
        message = "Tools.BySelection.OriginalID({},{},{},{},{},{})".format(crlTarget, iType, iMethod, iStartID, iIncrementStep, bAscending)
        return JPT_RUN_LINE(message)

class Tools:
    BySelection = BySelection()

class Group:
    def DeleteGroupEntity(self, crlDelGroup):
        message = "Tools.Group.DeleteGroupEntity({})".format(crlDelGroup)
        return JPT_RUN_LINE(message)

class Group:
    def CreateGroup(self, strGroupName, crlTargets, crEdit):
        message = "Tools.Group.CreateGroup('{}',{},{})".format(strGroupName, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

class Tools:
    BySelection = BySelection()

class Tools:
    Group = Group()

class TotalLoad:
    def LBC(self, crlTarget, crCoordinate, strOutput, iPrecision):
        message = "Tools.TotalLoad.LBC({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    Group = Group()

class Tools:
    TotalLoad = TotalLoad()

class TotalLoad:
    def Model(self, crlTarget, crCoordinate, strOutput, iPrecision):
        message = "Tools.TotalLoad.Model({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    TotalLoad = TotalLoad()

class TotalLoad:
    def Node(self, crlTarget, crCoordinate, strOutput, iPrecision):
        message = "Tools.TotalLoad.Node({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    TotalLoad = TotalLoad()

class TotalLoad:
    def Part(self, crlTarget, crCoordinate, strOutput, iPrecision):
        message = "Tools.TotalLoad.Part({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    TotalLoad = TotalLoad()

class TotalLoad:
    def Face(self, crlTarget, crCoordinate, strOutput, iPrecision):
        message = "Tools.TotalLoad.Face({},{},'{}',{})".format(crlTarget, crCoordinate, strOutput, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    def NodeCSGroup():
        message = "Tools.NodeCSGroup({})".format()
        return JPT_RUN_LINE(message)

class Tools:
    def NodeCS(crlInst, crCoordSystem):
        message = "Tools.NodeCS({},{})".format(crlInst, crCoordSystem)
        return JPT_RUN_LINE(message)

class Tools:
    def DisplacementCS(crlInst, crCoordSystem):
        message = "Tools.DisplacementCS({},{})".format(crlInst, crCoordSystem)
        return JPT_RUN_LINE(message)

class Tools:
    def Connections(listConnectRenumberTool):
        message = "Tools.Connections({})".format(listConnectRenumberTool)
        return JPT_RUN_LINE(message)

class Tools:
    def Renumber(listRenumberItem, bAssignProp, bSurfCornerFirst):
        message = "Tools.Renumber({},{},{})".format(listRenumberItem, bAssignProp, bSurfCornerFirst)
        return JPT_RUN_LINE(message)

class Tools:
    TotalLoad = TotalLoad()

class Tools:
    def GroupByDCS():
        message = "Tools.GroupByDCS({})".format()
        return JPT_RUN_LINE(message)

class Tools:
    def RenumberByFile(strCSVPath, iConfilctStrategy, bNeedToUpdateCount):
        message = "Tools.RenumberByFile('{}',{},{})".format(strCSVPath, iConfilctStrategy, bNeedToUpdateCount)
        return JPT_RUN_LINE(message)

class Tools:
    def ModelInfo(strPath, strPathName, listPartInfo, bPropertyAssignedPart, bPropertyAssignedSummary, iModelNode, iNmodelnodeWithprop, ilModelElement, ilNmodelelemWithprop, ilModelLBC, iModelContact, ilModelConnection, ilModelProperty):
        message = "Tools.ModelInfo('{}','{}',{},{},{},{},{},{},{},{},{},{},{})".format(strPath, strPathName, listPartInfo, bPropertyAssignedPart, bPropertyAssignedSummary, iModelNode, iNmodelnodeWithprop, ilModelElement, ilNmodelelemWithprop, ilModelLBC, iModelContact, ilModelConnection, ilModelProperty)
        return JPT_RUN_LINE(message)

class Tools:
    def Section(bSection):
        message = "Tools.Section({})".format(bSection)
        return JPT_RUN_LINE(message)

class Tools:
    def RenumberByConnection(connectRenumberTool, crlTarget):
        message = "Tools.RenumberByConnection({},{})".format(connectRenumberTool, crlTarget)
        return JPT_RUN_LINE(message)

class Angle:
    def TwoNodesAxis(self, crNode1,crNode2, dlAxis, strTarget, iPrecision):
        message = "Tools.Measure.Angle.TwoNodesAxis({},{},{},'{}',{})".format(crNode1,crNode2, dlAxis, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Angle = Angle()

class Tools:
    Measure = Measure()

class Angle:
    def ThreeNodes(self, crNode1,crNode2,crNode3, strTarget, iPrecision):
        message = "Tools.Measure.Angle.ThreeNodes({},{},{},'{}',{})".format(crNode1,crNode2,crNode3, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Angle = Angle()

class Tools:
    Measure = Measure()

class Angle:
    def ProjectedNode(self, crNode, strTarget, iPrecision):
        message = "Tools.Measure.Angle.ProjectedNode({},'{}',{})".format(crNode, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    Measure = Measure()

class Measure:
    Angle = Angle()

class Angle:
    def TwoElemEdges(self, crpElemEdge1,crpElemEdge2, strTarget, iPrecision):
        message = "Tools.Measure.Angle.TwoElemEdges({},{},'{}',{})".format(crpElemEdge1,crpElemEdge2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Angle = Angle()

class Tools:
    Measure = Measure()

class Angle:
    def ThreeNodes(self, crNode1,crNode2,crNode3, strTarget, iPrecision):
        message = "Tools.Measure.Angle.ThreeNodes({},{},{},'{}',{})".format(crNode1,crNode2,crNode3, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Angle:
    def TwoAxis(self, dlXyz1, dlXyz2, strTarget, iPrecision):
        message = "Tools.Measure.Angle.TwoAxis({},{},'{}',{})".format(dlXyz1, dlXyz2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Angle = Angle()

class Tools:
    Measure = Measure()

class Tools:
    Measure = Measure()

class Measure:
    Angle = Angle()

class Measure:
    Angle = Angle()

class Angle:
    def TwoEdges(self, crEdge1,crEdge2, strTarget, iPrecision):
        message = "Tools.Measure.Angle.TwoEdges({},{},'{}',{})".format(crEdge1,crEdge2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    Measure = Measure()

class Area:
    def Element(self, taElem , iPrecision ):
        message = "Tools.Measure.Area.Element({},{})".format(taElem , iPrecision )
        return JPT_RUN_LINE(message)

class Area:
    def Face(self, taFace , iPrecision ):
        message = "Tools.Measure.Area.Face({},{})".format(taFace , iPrecision )
        return JPT_RUN_LINE(message)

class Measure:
    Area = Area()

class Tools:
    Measure = Measure()

class Tools:
    Measure = Measure()

class Area:
    def Body(self, taBody , iPrecision ):
        message = "Tools.Measure.Area.Body({},{})".format(taBody , iPrecision )
        return JPT_RUN_LINE(message)

class Measure:
    Area = Area()

class Measure:
    Area = Area()

class Distance:
    def TwoEdges(self, crEdge1,crEdge2, iPrecision):
        message = "Tools.Measure.Distance.TwoEdges({},{},{})".format(crEdge1,crEdge2, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    Measure = Measure()

class Measure:
    Distance = Distance()

class Tools:
    Measure = Measure()

class Distance:
    def TwoNodes(self, crNode1, crNode2, strTarget, iPrecision, crCoordinateSystem):
        message = "Tools.Measure.Distance.TwoNodes({},{},'{}',{},{})".format(crNode1, crNode2, strTarget, iPrecision, crCoordinateSystem)
        return JPT_RUN_LINE(message)

class Distance:
    def FaceNode(self, crlFace,crlNode, iPrecision):
        message = "Tools.Measure.Distance.FaceNode({},{},{})".format(crlFace,crlNode, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Distance = Distance()

class Tools:
    Measure = Measure()

class Measure:
    Distance = Distance()

class Tools:
    Measure = Measure()

class Distance:
    def Edge(self, crEdge, iPrecision):
        message = "Tools.Measure.Distance.Edge({},{})".format(crEdge, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Distance = Distance()

class Distance:
    def TwoPoints(self, posPoint1, posPoint2, strTarget, iPrecision, crCoordinateSystem):
        message = "Tools.Measure.Distance.TwoPoints({},{},'{}',{},{})".format(posPoint1, posPoint2, strTarget, iPrecision, crCoordinateSystem)
        return JPT_RUN_LINE(message)

class Tools:
    Measure = Measure()

class Measure:
    Distance = Distance()

class Tools:
    Measure = Measure()

class Distance:
    def EdgeNode(self, crEdge,crNode, iPrecision):
        message = "Tools.Measure.Distance.EdgeNode({},{},{})".format(crEdge,crNode, iPrecision)
        return JPT_RUN_LINE(message)

class Distance:
    def LineNode(self, crlTargetNode, iPrecision):
        message = "Tools.Measure.Distance.LineNode({},{})".format(crlTargetNode, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    Measure = Measure()

class Measure:
    Distance = Distance()

class Tools:
    Measure = Measure()

class Measure:
    Distance = Distance()

class Distance:
    def PlaneElemToNode(self, crNode, crElem, iPrecision):
        message = "Tools.Measure.Distance.PlaneElemToNode({},{},{})".format(crNode, crElem, iPrecision)
        return JPT_RUN_LINE(message)

class Distance:
    def Plane3NodesToNode(self, crNode1,crNode2,crNode3,crNode, iPrecision):
        message = "Tools.Measure.Distance.Plane3NodesToNode({},{},{},{},{})".format(crNode1,crNode2,crNode3,crNode, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Distance = Distance()

class Tools:
    Measure = Measure()

class Measure:
    Distance = Distance()

class Mass:
    def Property(self, crlPart,crlCondition, strTarget, bGravityCenter, iPrecision):
        message = "Tools.Measure.Mass.Property({},{},'{}',{},{})".format(crlPart,crlCondition, strTarget, bGravityCenter, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    Measure = Measure()

class Measure:
    Mass = Mass()

class Mass:
    def Material(self, crlPart,crlCondition,strDensity, strTarget, bGravityCenter, iPrecision):
        message = "Tools.Measure.Mass.Material({},{},'{}','{}',{},{})".format(crlPart,crlCondition,strDensity, strTarget, bGravityCenter, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    Measure = Measure()

class Tools:
    Measure = Measure()

class Radius:
    def Edge(self, crEdge, iPrecision):
        message = "Tools.Measure.Radius.Edge({},{})".format(crEdge, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Mass = Mass()

class Measure:
    Radius = Radius()

class Tools:
    Measure = Measure()

class Radius:
    def ThreeNodes(self, crCrnode13,crCrnode23,crCrnode33, iPrecision):
        message = "Tools.Measure.Radius.ThreeNodes({},{},{},{})".format(crCrnode13,crCrnode23,crCrnode33, iPrecision)
        return JPT_RUN_LINE(message)

class Measure:
    Radius = Radius()

class Measure:
    def Volume(self, crlParts, iPrecision):
        message = "Tools.Measure.Volume({},{})".format(crlParts, iPrecision)
        return JPT_RUN_LINE(message)

class Tools:
    Measure = Measure()

class ACModelCreationTools:
    def MeshedFace(self, crlItem1, crlItem2, crlItem3, crlPart, iType, dMeshSise, bMergeTol, dTol, bCreatePart):
        message = "MMCCarACTools.ACModelCreationTools.MeshedFace({},{},{},{},{},{},{},{},{})".format(crlItem1, crlItem2, crlItem3, crlPart, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
        return JPT_RUN_LINE(message)

class Tools:
    Measure = Measure()

class ClearanceElement:
    def Connect(self, crlFaces, crlElems, iConnectionMethod):
        message = "MMCCarACTools.ClearanceElement.Connect({},{},{})".format(crlFaces, crlElems, iConnectionMethod)
        return JPT_RUN_LINE(message)

class MMCCarACTools:
    ClearanceElement = ClearanceElement()

class MMCCarACTools:
    ACModelCreationTools = ACModelCreationTools()

class ClearanceElement:
    def Edit(self, dDx, dDy, dDz, dLx, dLy, dLz, crlTarget, crlDestNode, poslDestPoint):
        message = "MMCCarACTools.ClearanceElement.Edit({},{},{},{},{},{},{},{},{})".format(dDx, dDy, dDz, dLx, dLy, dLz, crlTarget, crlDestNode, poslDestPoint)
        return JPT_RUN_LINE(message)

class Designer:
    LBC = LBC()

class MMCCarACTools:
    ClearanceElement = ClearanceElement()

class LBC:
    def TemperatureLoad(self, strName, iDnType, dFTemp, strDstrFilePathName, crDcrTable, crlTarget, crEdit, bDbUseAsMaterialReferenceTemp):
        message = "Designer.LBC.TemperatureLoad('{}',{},{},'{}',{},{},{},{})".format(strName, iDnType, dFTemp, strDstrFilePathName, crDcrTable, crlTarget, crEdit, bDbUseAsMaterialReferenceTemp)
        return JPT_RUN_LINE(message)

class Designer:
    Load = Load()

class Load:
    def Moment(self, strName, crlFaces, dlVecMomentXYZ, crCoord, crEdit):
        message = "Designer.Load.Moment('{}',{},{},{},{})".format(strName, crlFaces, dlVecMomentXYZ, crCoord, crEdit)
        return JPT_RUN_LINE(message)

class Designer:
    def Material(strMatName, strPropName, dThickness, crlTargets):
        message = "Designer.Material('{}','{}',{},{})".format(strMatName, strPropName, dThickness, crlTargets)
        return JPT_RUN_LINE(message)

class Designer:
    def ContactMerge(crlTarget):
        message = "Designer.ContactMerge({})".format(crlTarget)
        return JPT_RUN_LINE(message)

