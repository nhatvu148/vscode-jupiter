class MakeProcess:
    def Static(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.own.Static('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def Creep(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, bThetaDefined, dTheta, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.own.Creep('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, dStabilizationFactor, bThetaDefined, dTheta, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def Dynamic(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, bDynamic, advcDynamic, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.own.Dynamic('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, bDynamic, advcDynamic, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def EigenValue(self, strName, bEigenValue, iNumberOfModes, iEigenvecNorm, dShift, dCgcgpiTol, dCgcgpiEigTol, iCgcgpiLoopMax, dCgcgpiInnerTol, iCgcgpiBlockSize, iCgcgpiExtraMode, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.own.EigenValue('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, bEigenValue, iNumberOfModes, iEigenvecNorm, dShift, dCgcgpiTol, dCgcgpiEigTol, iCgcgpiLoopMax, dCgcgpiInnerTol, iCgcgpiBlockSize, iCgcgpiExtraMode, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def DynamicExplicit(self, strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, iLogMessageInterval, iLinearApproximation, dBulkViscosityCoef1, dBulkViscosityCoef2, dMassScalingdt, dDtScaleFactor, dPenaltyScaleFactor, iContactSearchInterval, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.own.DynamicExplicit('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, iGeomNonlinear, advcStructTimeStep, bConvergence, advcConvergence, bContact, advcContactIter, bAutoIncrement, advcAutoIncrement, iLogMessageInterval, iLinearApproximation, dBulkViscosityCoef1, dBulkViscosityCoef2, dMassScalingdt, dDtScaleFactor, dPenaltyScaleFactor, iContactSearchInterval, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def ModalFreqResp(self, strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.own.ModalFreqResp('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def ResponseSpectrum(self, strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, iPropMethod, iSpttype, dSptFactor0, crSpt0, dSptFactor1, crSpt1, dSptFactor2, crSpt2, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.own.ResponseSpectrum('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, iPropMethod, iSpttype, dSptFactor0, crSpt0, dSptFactor1, crSpt1, dSptFactor2, crSpt2, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def SteadyState(self, strName, iEndType, dMaxTime, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList):
        message = "Analysis.ADVC.MakeProcess.own.SteadyState('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iEndType, dMaxTime, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList)
        return JPT_RUN_LINE(message)

    def Transient(self, strName, iEndType, dMaxTime, dSteadyRate, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList):
        message = "Analysis.ADVC.MakeProcess.own.Transient('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iEndType, dMaxTime, dSteadyRate, iFixedOrAuto, dMaxChange, dInitDt, iDefineMaxDt, dMaxDt, iDefineMinDt, dMinDt, dFixedDt, iOutputLast, iOutputInterval, iRestartLast, iRestartInterval, dOutputTimeInterval, dRestartTimeInterval, iOutputInit, iListOutputInterval, bConvergence, dCgTol, dCgNrTol, dCgDispTol, dCgNrDispTol, dCgDispLimitTol, dCgTotalDispLimitTol, dNewtonTol, dNewtonDispTol, dNewtonDispLimitTol, dNewtonTotalDispLimitTol, iCgloopMax, iNewtonMax, dHtNlLoopTol, iHtNlLoopMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList)
        return JPT_RUN_LINE(message)

    def Fatigue(self, strName, bFatigue, iMethod, iStressAxis, iSafetyType, dSearchResolution, dSafetyMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.own.Fatigue('{}',{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, bFatigue, iMethod, iStressAxis, iSafetyType, dSearchResolution, dSafetyMax, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

    def RandomResponse(self, strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, iPropMethod, iPSDtype, iPSDdir, crPSDLoad, dPSDFactor, dGravityAccel, iOutputEigenFreqStep, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult):
        message = "Analysis.ADVC.MakeProcess.own.RandomResponse('{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{})".format(strName, strRefEigenDir, dRefLowFreq, dRefHighFreq, crModalDampingRatio, crExcitationFreq, bAutoFreqInterval, dMaxFreq, dMinFreq, iNumFreqPoint, dBiasParam, iPropMethod, iPSDtype, iPSDdir, crPSDLoad, dPSDFactor, dGravityAccel, iOutputEigenFreqStep, crEdit, listLoadNode, listLoadCaseNode, listLoadNodeContact, ilOutputParamList, iRefType, strRefPath, listAdvcRefStressResult)
        return JPT_RUN_LINE(message)

class CentrifugalForce:
    def CoordinateSystems(self, strName, dFVelocity, dFAcceleration, iAxisDirection, iVelocityUnit, iAccelerationUnit, crCurCoord, crlTarget, crEdit):
        message = "BoundaryConditions.BodyLoads.CentrifugalForce.own.CoordinateSystems('{}',{},{},{},{},{},{},{},{})".format(strName, dFVelocity, dFAcceleration, iAxisDirection, iVelocityUnit, iAccelerationUnit, crCurCoord, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def TwoPositions(self, strName, dFBasePoint1, dFBasePoint2, dFBasePoint3, dFTipPoint1, dFTipPoint2, dFTipPoint3, dFVelocity, dFAcceleration, iVelocityUnit, iAccelerationUnit, crlTarget, crEdit):
        message = "BoundaryConditions.BodyLoads.CentrifugalForce.own.TwoPositions('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dFBasePoint1, dFBasePoint2, dFBasePoint3, dFTipPoint1, dFTipPoint2, dFTipPoint3, dFVelocity, dFAcceleration, iVelocityUnit, iAccelerationUnit, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class FunctionLoadCylinder:
    def Quadratic(self, strName, dFTotalForce, dA, dB, crCoord, iAngleBase, dAngleRange, iEnArrowDir, crlTargets, crEdit):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.own.Quadratic('{}',{},{},{},{},{},{},{},{},{})".format(strName, dFTotalForce, dA, dB, crCoord, iAngleBase, dAngleRange, iEnArrowDir, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

    def Sine(self, strName, dFTotalForce, dA, crCoord, iAngleBase, dAngleRange, iEnArrowDir, bDistributeInAxis, crlTarget, crEdit):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.own.Sine('{}',{},{},{},{},{},{},'{}',{},{})".format(strName, dFTotalForce, dA, crCoord, iAngleBase, dAngleRange, iEnArrowDir, bDistributeInAxis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def Vector(self, strName, dFTotalForce, dA, dX, dY, crCoord, iEnDirection, dAngleRange, iArrowDir, bDistributeInAxis, crlTarget, crEdit):
        message = "BoundaryConditions.Force.FunctionLoadCylinder.own.Vector('{}',{},{},{},{},{},{},{},{},'{}',{},{})".format(strName, dFTotalForce, dA, dX, dY, crCoord, iEnDirection, dAngleRange, iArrowDir, bDistributeInAxis, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class NonlinearForce:
    def NOLIN3(self, strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit):
        message = "BoundaryConditions.Force.NonlinearForce.own.NOLIN3('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

    def NOLIN4(self, strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit):
        message = "BoundaryConditions.Force.NonlinearForce.own.NOLIN4('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, dForcePowerA, dMomentPowerA, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCurCoord, crlMasterTarget, crlSlaveTarget, crEdit)
        return JPT_RUN_LINE(message)

    def NOLIN1(self, strName, dForceScale, dMomentScale, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCoord, crForceTable, crMomentTable, crlVcrMaster, crlVcrSlave, crEdit):
        message = "BoundaryConditions.Force.NonlinearForce.own.NOLIN1('{}',{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, dForceScale, dMomentScale, iForcDir, iForceDepends, iMomentDir, iMomentDepends, crCoord, crForceTable, crMomentTable, crlVcrMaster, crlVcrSlave, crEdit)
        return JPT_RUN_LINE(message)

class InitialAngularVelocity:
    def Abaqus(self, strName, dVelocity, strFirstCoord, strSecondCoord, crlTargets, crEdit):
        message = "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.own.Abaqus('{}',{},'{}','{}',{},{})".format(strName, dVelocity, strFirstCoord, strSecondCoord, crlTargets, crEdit)
        return JPT_RUN_LINE(message)

    def General(self, strName, stData, crlTarget, crEdit):
        message = "BoundaryConditions.InitialNodalValue.InitialAngularVelocity.own.General('{}',{},{},{})".format(strName, stData, crlTarget, crEdit)
        return JPT_RUN_LINE(message)

class Edge:
    def TypeC(self, crlEdgeCur1,crlEdgeCur2, strRbeName, dPlaneTol, dMaxBoltHeight, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth):
        message = "Connections.BoltConnections.Edge.own.TypeC({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1,crlEdgeCur2, strRbeName, dPlaneTol, dMaxBoltHeight, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth)
        return JPT_RUN_LINE(message)

    def TypeB(self, crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, bIfCreate2ADVCStaticProcessForBoltFixLength):
        message = "Connections.BoltConnections.Edge.own.TypeB({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, bIfCreate2ADVCStaticProcessForBoltFixLength)
        return JPT_RUN_LINE(message)

    def TypeD(self, crlEdgeCur1,crlEdgeCur2, strMpcName, dConnRadius, dPlaneTol):
        message = "Connections.BoltConnections.Edge.own.TypeD({},{},'{}',{},{})".format(crlEdgeCur1,crlEdgeCur2, strMpcName, dConnRadius, dPlaneTol)
        return JPT_RUN_LINE(message)

    def TypeA(self, crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, bIsCreate2ADVCStaticProcessForFixLength):
        message = "Connections.BoltConnections.Edge.own.TypeA({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlEdgeCur1,crlEdgeCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, bIsCreate2ADVCStaticProcessForFixLength)
        return JPT_RUN_LINE(message)

class Face:
    def TypeC(self, crlFaceCur1,crlFaceCur2, strRbeName, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth):
        message = "Connections.BoltConnections.Face.own.TypeC({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1,crlFaceCur2, strRbeName, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, iConnectionType, iCoincidentNodes, dTolerance, iGround, dStiffnessX, dStiffnessY, dStiffnessZ, iLocalStiffUnit, dRotateStiffX, dRotateStiffY, dRotateStiffZ, iLocalRotateStiffUnit, dDampCoef, dStressCoef, crCurCoord, iTopRbeType, dTopPitch, dTopRemoveDepth, iBotRbeType, dBotPitch, dBotRemoveDepth)
        return JPT_RUN_LINE(message)

    def TypeB(self, crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, dScale1, bIsCreate2ADVCStaticProcessForFixLength):
        message = "Connections.BoltConnections.Face.own.TypeB({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, dRBE2, dBotDtDia, dPitch, iBotRbeConnType, dScale1, bIsCreate2ADVCStaticProcessForFixLength)
        return JPT_RUN_LINE(message)

    def TypeA(self, crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, dScale1, bIfCreate2ADVCStaticProcessForBoltFixLength):
        message = "Connections.BoltConnections.Face.own.TypeA({},{},'{}','{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceCur1,crlFaceCur2, strRbeName, strBarName, iShaftType, crCurBarProperty, dPlaneTol, dMaxBoltHeight, dMaxDiameter, dMinDiameter, bPretensionLoad, iSolverType, dForceValue, iPreTenDof, crCurCoord, iBoltFixLength, iTopSlot, dRBE1, iBotSlot, dRBE2, dScale1, bIfCreate2ADVCStaticProcessForBoltFixLength)
        return JPT_RUN_LINE(message)

class Abaqus:
    def ContactTable(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.own.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.own.ManualGroup('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ManualFace(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.own.ManualFace('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.own.ContactGroupByMatrix('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Abaqus.own.ContactShareFace('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iContactMethod, iContactType, iAlg, dAdjustVal, dExtensionZone, dMaxPenetration, iSmallSliding, dSmooth, iFrictionType, dFrictionCoef1, dFrictionCoef2, dShearLimit, dSlipTol, dStaticFrictionCoef, dKineticFrictionCoef, dDecayCoef, iAdjust, dPositonTol, iIformula, iTie, iPOCType, iAllowSeparation, dSlope, tshPOCTsheet, iClearanceType, iClearanceTypeId, bTemperatureDependency, iDependencies, tshCDTsheet, iPrsTypeId, bPrsTemperatureDependency, iPrsDependencies, tshPrsDTsheet, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class ADVC:
    def ContactClearance(self, strName,dClearanceVal,iLocalUnit,iSolverType,crlTarget, crEdit):
        message = "Connections.Contacts.ADVC.own.ContactClearance('{}',{},{},{},{},{})".format(strName,dClearanceVal,iLocalUnit,iSolverType,crlTarget, crEdit)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.own.ManualGroup('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.own.ManualFace({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def Contact(self, strName, iType, slidingType, InitialState, initialStateTol, kineticFrictionCoef, exponentialCoef, Behavior, Clearance, adjust2Clearance, interference, adjust2Interference, autoShrink, badvAdjust, adjustValue, FrictionCoef, MaxShear, elastic_slip, slip_tolerance, searchWidth, SearchGap, searchDepth, critialPenetration, estimation_impact_time, formula, constraintType, iDataType, TypeId, btemperatureDependency, idependencies, table, stabilized, type, residual_factor, effective_dist, cn, ct, taCClearance, taTarget, crEdit, searchAngle, constraintType_explicit, penaltyFact, penaltyFactExplicit, Color, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.own.Contact('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iType, slidingType, InitialState, initialStateTol, kineticFrictionCoef, exponentialCoef, Behavior, Clearance, adjust2Clearance, interference, adjust2Interference, autoShrink, badvAdjust, adjustValue, FrictionCoef, MaxShear, elastic_slip, slip_tolerance, searchWidth, SearchGap, searchDepth, critialPenetration, estimation_impact_time, formula, constraintType, iDataType, TypeId, btemperatureDependency, idependencies, table, stabilized, type, residual_factor, effective_dist, cn, ct, taCClearance, taTarget, crEdit, searchAngle, constraintType_explicit, penaltyFact, penaltyFactExplicit, Color, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.own.ContactShareFace({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(crlShareFace, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.own.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod):
        message = "Connections.Contacts.ADVC.own.ContactGroupByMatrix('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},'{}',{},{},{},{},{})".format(strName, iContactType, iSlidingType, iInitialState, dInitialStateTol, dKineticFrictionCoef, dExponentialCoef, iBehavior, dClearance, iAdjust2Clearance, dInterference, iAdjust2Interference, iAutoShrink, iAdvAdjust, dAdjustValue, dFrictionCoef, dMaxShear, dElasticSlip, dSlipTolerance, dSearchWidth, dSearchGap, dSearchDepth, dCritialPenetration, iEstimationImpactTime, iFormula, iConstraintType, iDataType, iTypeId, bTemperatureDependency, iNumDependencies, tshTableClearance, bStabilized, iStabilizeType, dResidualFactor, dEffectiveDist, dCN, dCT, crlCClearance, crplTarget, crEdit, dSearchAngle, iConstraintTypeExplicit, dPenaltyFact, dPenaltyFactExplicit, iColor, iAlg, iMethod)
        return JPT_RUN_LINE(message)

class Ansys:
    def ManualGroup(self, strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Ansys.own.ManualGroup('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor):
        message = "Connections.Contacts.Ansys.own.ManualFace({},{},'{}',{},{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Ansys.own.ContactGroupByMatrix('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor):
        message = "Connections.Contacts.Ansys.own.ContactShareFace({},'{}',{},{},{},{},{},{})".format(crlShareFace, strName, iMethod, iType, iContactAlgorithm, ansysContact, crEdit, iColor)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor):
        message = "Connections.Contacts.Ansys.own.ContactTable('{}',{},{},{},{},{},{},{})".format(strName, iMethod, iType, iContactAlgorithm, ansysContact, crplTarget, crEdit, iColor)
        return JPT_RUN_LINE(message)

class MSCNastran:
    def ManualGroup(self, strName, tssolverContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.own.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.own.ContactGroupByMatrix('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.own.ManualFace({},{},'{}','{}',{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace, strName, nastranContact, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.own.ContactShareFace({},'{}','{}',{},{},{})".format(crlShareFace, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.MSCNastran.own.ContactTable('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class NXNastran:
    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.own.ManualFace({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

    def ContactShareFace(self, crlShareFace, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.own.ContactShareFace({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crlShareFace, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName, iType, iAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, crplTargetPair, crEdit, iColor, iMethod):
        message = "Connections.Contacts.NXNastran.own.ContactTable('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(strName, iType, iAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, crplTargetPair, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.own.ManualGroup({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

    def ContactGroupByMatrix(self, crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit):
        message = "Connections.Contacts.NXNastran.own.ContactGroupByMatrix({},{},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(crTaFaceMaster, crTaFaceSlave, strName, iContactType, iContactAlg, dNorPenFactor, dTanPenFactor, dForceConTol, dMaxForceIter, dMaxStaIter, dChangeNum, dMinContactPer, iShellThickness, iContactStatus, iInitGapPenetra, iRegionRefine, iEvaluPts, dMinSearDist, dMaxSearDist, dFricCoef, dSearchDist, dPenatlyFactor, iShellOffset, iColor, iMethod, crEdit)
        return JPT_RUN_LINE(message)

class TSSolver:
    def ManualFace(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSolver.own.ManualFace('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def Auto(self, strlNames,crllMasterFaceTargets,crllSlaveFaceTargets, crlContactTypes, dlTaInterferenceClosures, dlTaFrictionCoefficients, blTaInitialAdjustments, crlColors, crlCrEdit, crlCrMasterGroup, crlCrSlaveGroup):
        message = "Connections.Contacts.TSSolver.own.Auto('{}',{},{},{},{},{},{},{},{},{},{})".format(strlNames,crllMasterFaceTargets,crllSlaveFaceTargets, crlContactTypes, dlTaInterferenceClosures, dlTaFrictionCoefficients, blTaInitialAdjustments, crlColors, crlCrEdit, crlCrMasterGroup, crlCrSlaveGroup)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName, tssolverContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSolver.own.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class TSSS:
    def ManualFace(self, crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSS.own.ManualFace({},{},'{}','{}',{},{},{})".format(crlFaceMaster, crlFaceSlave, strName, nastranContact, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ManualGroup(self, strName, tssolverContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSS.own.ManualGroup('{}',{},{},{},{},{})".format(strName, tssolverContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

    def ContactTable(self, strName, nastranContact, crplTarget, crEdit, iColor, iMethod):
        message = "Connections.Contacts.TSSS.own.ContactTable('{}','{}',{},{},{},{})".format(strName, nastranContact, crplTarget, crEdit, iColor, iMethod)
        return JPT_RUN_LINE(message)

class Equation:
    def MultiNodes(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.Equation.own.MultiNodes('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def TwoFace(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.Equation.own.TwoFace('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def SemiAuto(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.Equation.own.SemiAuto('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class General:
    def NodeToNode(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.own.NodeToNode('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodeToEdges(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.own.NodeToEdges('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodeToFaces(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.own.NodeToFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def TwoEdges(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.own.TwoEdges('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def FacesToFaces(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.own.FacesToFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodesToNodes(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.own.NodesToNodes('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def TwoFaces(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.own.TwoFaces('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodeToAny(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.own.NodeToAny('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    def NodesWithTolerance(self, strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit):
        message = "Connections.MPC.General.own.NodesWithTolerance('{}',{},{},{},{},{},{},{},{},{},{})".format(strName, crlMaster, crlSlave, listMpcConnection, dSearchTol, dValue, iMPCType, iSearchType, iCoordSys, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

class RBar:
    def OneToOne(self, strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBar.own.OneToOne('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

    def OneToMany(self, strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBar.own.OneToMany('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

    def OneToOneNodesWithTolerance(self, strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit):
        message = "Connections.RigidElements.RBar.own.OneToOneNodesWithTolerance('{}',{},{},{},{},{},{},{})".format(strName, crlMasterTarget, crlSlaveTarget, iMethod, iUlDOFs, dTol, crCoord, crEdit)
        return JPT_RUN_LINE(message)

class RBE2:
    def OneToMany(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.own.OneToMany({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def OneToOne(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.own.OneToOne({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def OneToOneNodesWithTolerance(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.own.OneToOneNodesWithTolerance({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def ToCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.own.ToCenter({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

    def ToCircleCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode):
        message = "Connections.RigidElements.RBE2.own.ToCircleCenter({},{},{},{},'{}',{},{},{},{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, iEType, strName, crCoordSys, dTolerance, iUlDOFs, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly, iBCheckDulplicate, iDuplicateMode)
        return JPT_RUN_LINE(message)

class RBE3:
    def OneToMany(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.own.OneToMany({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

    def OneToOne(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.own.OneToOne({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

    def ToCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.own.ToCenter({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
        return JPT_RUN_LINE(message)

    def ToCircleCenter(self, iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly):
        message = "Connections.RigidElements.RBE3.own.ToCircleCenter({},{},{},{},{},'{}',{},{},{},{},{},{},{})".format(iMethod, crlMasterTarget, crlSlaveTarget, listRBE3TermAtbs, iTypeRBE3, strName, crCoordSys, dTolerance, dlVirtualNodePos, iSurfaceDef, crEdit, iBUpdateDispCS, iBCornerOnly)
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
        message = "Connections.SpringsDampers.Damper.own.AnyEntities11DoFS({},'{}',{},{},{},{},{},{},{},{},{})".format(iMethod,strName,crlMasterTarget,crlSlaveTarget, crCoordSys, iGround, dTolerance, vecTDamper, vecRDamper, crEdit, bUpdateDispCS)
        return JPT_RUN_LINE(message)

class Bush:
    def TwoNodes(self, iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj):
        message = "Connections.SpringsDampers.Bush.own.TwoNodes({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

    def AnyEntities(self, iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj):
        message = "Connections.SpringsDampers.Bush.own.AnyEntities({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

    def OnetoOne(self, iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj):
        message = "Connections.SpringsDampers.Bush.own.OnetoOne({},'{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMaster, crlSlave, crCoord, dTol, iGround, iOriMode, iEqual, poslVector, dlStiffness, dlDampCoef, dlDampConst, dRotStrain, dTransStrain, dRotStress, dTransStress, crEditObj)
        return JPT_RUN_LINE(message)

class Spring:
    def GroundedSpring(self, iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit):
        message = "Connections.SpringsDampers.Spring.own.GroundedSpring({},'{}',{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{})".format(iMethod, strName, crlMasterTarget, crlSlaveTarget, crCoordSys, iSpringType, iGround, dTolerance, iDirection, iDistributeMode, iDof1, iDof2, dDampCoef, dStressCoef, posTStiffness, posRStiffness, bUpdateDispCS, crEdit)
        return JPT_RUN_LINE(message)

    Nodeswithtolerance = Nodeswithtolerance()

    OneToOne = OneToOne()

class Element:
    def SurfaceElement(self, ilElement,ilFace,ilPart,iCreateNewPart):
        message = "MeshCleanup.ChangeTopology.Element.own.SurfaceElement({},{},{},{})".format(ilElement,ilFace,ilPart,iCreateNewPart)
        return JPT_RUN_LINE(message)

class MergeElement:
    def TwoQuadsToQuad(self, crlElements):
        message = "MeshCleanup.Manual2D.MergeElement.own.TwoQuadsToQuad({})".format(crlElements)
        return JPT_RUN_LINE(message)

    def TwoQuadsToQuad(self, crlElements):
        message = "MeshCleanup.Manual2D.MergeElement.own.TwoQuadsToQuad({})".format(crlElements)
        return JPT_RUN_LINE(message)

    def TwoTrisToQuad(self, crlElems):
        message = "MeshCleanup.Manual2D.MergeElement.own.TwoTrisToQuad({})".format(crlElems)
        return JPT_RUN_LINE(message)

class SplitElement:
    def QuadTo4Quads(self, crlElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.own.QuadTo4Quads({},{},{},{},{},{},{},{})".format(crlElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadToTrans4Quads(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.own.QuadToTrans4Quads({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadToTrans3Quads(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.own.QuadToTrans3Quads({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo2Quads1Tri(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.own.QuadTo2Quads1Tri({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo3Tris(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.own.QuadTo3Tris({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo2Quads(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.own.QuadTo2Quads({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo2Tris(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.own.QuadTo2Tris({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadToQuadTri(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.own.QuadToQuadTri({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

    def QuadTo4Tris(self, taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode):
        message = "MeshCleanup.Manual2D.SplitElement.own.QuadTo4Tris({},{},{},{},{},{},{},{})".format(taElems, crDatumNode0, crDatumNode1, iMethod, iAutoExecute, iAutoTransition, iCADProject, iMergeNode)
        return JPT_RUN_LINE(message)

class Collapse:
    def CenterFaceCollapse(self, crlElem):
        message = "MeshCleanup.Manual3D.Collapse.own.CenterFaceCollapse({})".format(crlElem)
        return JPT_RUN_LINE(message)

    def HalfEdgeCollapse(self, crplElemEdge):
        message = "MeshCleanup.Manual3D.Collapse.own.HalfEdgeCollapse({})".format(crplElemEdge)
        return JPT_RUN_LINE(message)

    def EdgeCollapse(self, crplElemEdge, crlNode):
        message = "MeshCleanup.Manual3D.Collapse.own.EdgeCollapse({},{})".format(crplElemEdge, crlNode)
        return JPT_RUN_LINE(message)

class Edge:
    def ProjectEdgeToFace(self, crlEdge,crlFace, bExtendEdge):
        message = "MidPlaneEdit.AddItems.Edge.own.ProjectEdgeToFace({},{},{})".format(crlEdge,crlFace, bExtendEdge)
        return JPT_RUN_LINE(message)

    def FaceTwoFace(self, crRefFace, crExtFace, iExtendType):
        message = "MidPlaneEdit.AddItems.Edge.own.FaceTwoFace({},{},{})".format(crRefFace, crExtFace, iExtendType)
        return JPT_RUN_LINE(message)

class Face:
    def EFExtendFreeEdge(self, crlEdges,crlFaces,bMergeFace,bMergeEdge,bUseNeighDir,dMergeEdgeAngle,bMultiEF):
        message = "MidPlaneEdit.AddItems.Face.own.EFExtendFreeEdge({},{},{},{},{},{},{})".format(crlEdges,crlFaces,bMergeFace,bMergeEdge,bUseNeighDir,dMergeEdgeAngle,bMultiEF)
        return JPT_RUN_LINE(message)

    def EFProject(self, crlEdges,crlFaces,bMergeFace,bMergeEdge,dMergeEdgeAngle,bMultiEF):
        message = "MidPlaneEdit.AddItems.Face.own.EFProject({},{},{},{},{},{})".format(crlEdges,crlFaces,bMergeFace,bMergeEdge,dMergeEdgeAngle,bMultiEF)
        return JPT_RUN_LINE(message)

class Rod:
    def Rod(self, crlNode,dRadius,iType,dMeshSize,dStartDist,dWeldDist,iDivNumber,dDeformWidth,iTransitionElem,dlPosDir):
        message = "MufflerT.SpecialModeling.Rod.own.Rod({},{},{},{},{},{},{},{},{},{})".format(crlNode,dRadius,iType,dMeshSize,dStartDist,dWeldDist,iDivNumber,dDeformWidth,iTransitionElem,dlPosDir)
        return JPT_RUN_LINE(message)

class Angle:
    def ProjectedNode(self, crNode, strTarget, iPrecision):
        message = "Tool.Measure.Angle.own.ProjectedNode({},'{}',{})".format(crNode, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoNodesAxis(self, crNode1,crNode2,dlAxis,strTarget,iPrecision):
        message = "Tool.Measure.Angle.own.TwoNodesAxis({},{},{},'{}',{})".format(crNode1,crNode2,dlAxis,strTarget,iPrecision)
        return JPT_RUN_LINE(message)

    def By2Axis(self, xyz1, xyz2, target, Precision):
        message = "Tool.Measure.Angle.own.By2Axis({},{},{},{})".format(xyz1, xyz2, target, Precision)
        return JPT_RUN_LINE(message)

class Distance:
    def Edge(self, crEdge, option, iPrecision):
        message = "Tool.Measure.Distance.own.Edge({},{},{})".format(crEdge, option, iPrecision)
        return JPT_RUN_LINE(message)

    def EdgeNode(self, crPoint,crEdge, option, iPrecision):
        message = "Tool.Measure.Distance.own.EdgeNode({},{},{},{})".format(crPoint,crEdge, option, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoPoints(self, posPoint1, posPoint2, iPrecision):
        message = "Tool.Measure.Distance.own.TwoPoints({},{},{})".format(posPoint1, posPoint2, iPrecision)
        return JPT_RUN_LINE(message)

    def LineNode(self, crlTargetNode, iPrecision):
        message = "Tool.Measure.Distance.own.LineNode({},{})".format(crlTargetNode, iPrecision)
        return JPT_RUN_LINE(message)

    def Plane3NodesToNode(self, crNode, crNode1, crNode2, crNode3, iPrecision):
        message = "Tool.Measure.Distance.own.Plane3NodesToNode({},{},{},{},{})".format(crNode, crNode1, crNode2, crNode3, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoEdges(self, crEdge1,crEdge2,iOptions,iPrecision):
        message = "Tool.Measure.Distance.own.TwoEdges({},{},{},{})".format(crEdge1,crEdge2,iOptions,iPrecision)
        return JPT_RUN_LINE(message)

    def PlaneElemToNode(self, crNode, crElem, iPrecision):
        message = "Tool.Measure.Distance.own.PlaneElemToNode({},{},{})".format(crNode, crElem, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoNodes(self, crNode1,crNode2,iPrecision):
        message = "Tool.Measure.Distance.own.TwoNodes({},{},{})".format(crNode1,crNode2,iPrecision)
        return JPT_RUN_LINE(message)

    def FaceNode(self, crlFace,crlNode,iPrecision):
        message = "Tool.Measure.Distance.own.FaceNode({},{},{})".format(crlFace,crlNode,iPrecision)
        return JPT_RUN_LINE(message)

class Mass:
    def ByMaterial(self, crlPart,strDensity,strTarget,iPrecision):
        message = "Tool.Measure.Mass.own.ByMaterial({},'{}','{}',{})".format(crlPart,strDensity,strTarget,iPrecision)
        return JPT_RUN_LINE(message)

class Radius:
    def ByThreeNodes(self, crNode1_3,crNode2_3,crNode3_3,iPrecision):
        message = "Tool.Measure.Radius.own.ByThreeNodes({},{},{},{})".format(crNode1_3,crNode2_3,crNode3_3,iPrecision)
        return JPT_RUN_LINE(message)

    def MeasureRadiusBy3Nodes(self, crNode1_3,crNode2_3,crNode3_3,iPrecision):
        message = "Tool.Measure.Radius.own.MeasureRadiusBy3Nodes({},{},{},{})".format(crNode1_3,crNode2_3,crNode3_3,iPrecision)
        return JPT_RUN_LINE(message)

class Manual:
    def CleanTetCollapse(self, crlElem,iKeep,iCheckCondition,dLimitValue,iCleanupMode):
        message = "Tool.MeshQuality.Manual.own.CleanTetCollapse({},{},{},{},{})".format(crlElem,iKeep,iCheckCondition,dLimitValue,iCleanupMode)
        return JPT_RUN_LINE(message)

    def CleaningVolumeMesh(self, crlPart,crlElem,dLimitVolume,iMode):
        message = "Tool.MeshQuality.Manual.own.CleaningVolumeMesh({},{},{},{})".format(crlPart,crlElem,dLimitVolume,iMode)
        return JPT_RUN_LINE(message)

class Angle:
    def TwoNodesAxis(self, crNode1,crNode2, dlAxis, strTarget, iPrecision):
        message = "Tools.Measure.Angle.own.TwoNodesAxis({},{},{},'{}',{})".format(crNode1,crNode2, dlAxis, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def ThreeNodes(self, crNode1,crNode2,crNode3, strTarget, iPrecision):
        message = "Tools.Measure.Angle.own.ThreeNodes({},{},{},'{}',{})".format(crNode1,crNode2,crNode3, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def ProjectedNode(self, crNode, strTarget, iPrecision):
        message = "Tools.Measure.Angle.own.ProjectedNode({},'{}',{})".format(crNode, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoElemEdges(self, crpElemEdge1,crpElemEdge2, strTarget, iPrecision):
        message = "Tools.Measure.Angle.own.TwoElemEdges({},{},'{}',{})".format(crpElemEdge1,crpElemEdge2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def ThreeNodes(self, crNode1,crNode2,crNode3, strTarget, iPrecision):
        message = "Tools.Measure.Angle.own.ThreeNodes({},{},{},'{}',{})".format(crNode1,crNode2,crNode3, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoAxis(self, dlXyz1, dlXyz2, strTarget, iPrecision):
        message = "Tools.Measure.Angle.own.TwoAxis({},{},'{}',{})".format(dlXyz1, dlXyz2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoEdges(self, crEdge1,crEdge2, strTarget, iPrecision):
        message = "Tools.Measure.Angle.own.TwoEdges({},{},'{}',{})".format(crEdge1,crEdge2, strTarget, iPrecision)
        return JPT_RUN_LINE(message)

class Area:
    def Element(self, taElem , iPrecision ):
        message = "Tools.Measure.Area.own.Element({},{})".format(taElem , iPrecision )
        return JPT_RUN_LINE(message)

    def Face(self, taFace , iPrecision ):
        message = "Tools.Measure.Area.own.Face({},{})".format(taFace , iPrecision )
        return JPT_RUN_LINE(message)

    def Body(self, taBody , iPrecision ):
        message = "Tools.Measure.Area.own.Body({},{})".format(taBody , iPrecision )
        return JPT_RUN_LINE(message)

class Distance:
    def TwoEdges(self, crEdge1,crEdge2, iPrecision):
        message = "Tools.Measure.Distance.own.TwoEdges({},{},{})".format(crEdge1,crEdge2, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoNodes(self, crNode1, crNode2, strTarget, iPrecision, crCoordinateSystem):
        message = "Tools.Measure.Distance.own.TwoNodes({},{},'{}',{},{})".format(crNode1, crNode2, strTarget, iPrecision, crCoordinateSystem)
        return JPT_RUN_LINE(message)

    def FaceNode(self, crlFace,crlNode, iPrecision):
        message = "Tools.Measure.Distance.own.FaceNode({},{},{})".format(crlFace,crlNode, iPrecision)
        return JPT_RUN_LINE(message)

    def Edge(self, crEdge, iPrecision):
        message = "Tools.Measure.Distance.own.Edge({},{})".format(crEdge, iPrecision)
        return JPT_RUN_LINE(message)

    def TwoPoints(self, posPoint1, posPoint2, strTarget, iPrecision, crCoordinateSystem):
        message = "Tools.Measure.Distance.own.TwoPoints({},{},'{}',{},{})".format(posPoint1, posPoint2, strTarget, iPrecision, crCoordinateSystem)
        return JPT_RUN_LINE(message)

    def EdgeNode(self, crEdge,crNode, iPrecision):
        message = "Tools.Measure.Distance.own.EdgeNode({},{},{})".format(crEdge,crNode, iPrecision)
        return JPT_RUN_LINE(message)

    def LineNode(self, crlTargetNode, iPrecision):
        message = "Tools.Measure.Distance.own.LineNode({},{})".format(crlTargetNode, iPrecision)
        return JPT_RUN_LINE(message)

    def PlaneElemToNode(self, crNode, crElem, iPrecision):
        message = "Tools.Measure.Distance.own.PlaneElemToNode({},{},{})".format(crNode, crElem, iPrecision)
        return JPT_RUN_LINE(message)

    def Plane3NodesToNode(self, crNode1,crNode2,crNode3,crNode, iPrecision):
        message = "Tools.Measure.Distance.own.Plane3NodesToNode({},{},{},{},{})".format(crNode1,crNode2,crNode3,crNode, iPrecision)
        return JPT_RUN_LINE(message)

class Mass:
    def Property(self, crlPart,crlCondition, strTarget, bGravityCenter, iPrecision):
        message = "Tools.Measure.Mass.own.Property({},{},'{}',{},{})".format(crlPart,crlCondition, strTarget, bGravityCenter, iPrecision)
        return JPT_RUN_LINE(message)

    def Material(self, crlPart,crlCondition,strDensity, strTarget, bGravityCenter, iPrecision):
        message = "Tools.Measure.Mass.own.Material({},{},'{}','{}',{},{})".format(crlPart,crlCondition,strDensity, strTarget, bGravityCenter, iPrecision)
        return JPT_RUN_LINE(message)

class Radius:
    def Edge(self, crEdge, iPrecision):
        message = "Tools.Measure.Radius.own.Edge({},{})".format(crEdge, iPrecision)
        return JPT_RUN_LINE(message)

    def ThreeNodes(self, crCrnode13,crCrnode23,crCrnode33, iPrecision):
        message = "Tools.Measure.Radius.own.ThreeNodes({},{},{},{})".format(crCrnode13,crCrnode23,crCrnode33, iPrecision)
        return JPT_RUN_LINE(message)

