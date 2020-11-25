def RemoveEntitiesByID(Input1,Input2):
    message = "JPT.RemoveEntitiesByID({},{})".format(Input1,Input2)
    return get_res_from_jupiter(message)

def RemoveEntitiesByName(Input1,Input2,Input3):
    message = "JPT.RemoveEntitiesByName({},{},{})".format(Input1,Input2,Input3)
    return get_res_from_jupiter(message)

def RemoveAllConnections():
    message = "JPT.RemoveAllConnections()".format()
    return get_res_from_jupiter(message)

def RemoveAllMaterials():
    message = "JPT.RemoveAllMaterials()".format()
    return get_res_from_jupiter(message)

def RemoveWSProperties():
    message = "JPT.RemoveWSProperties()".format()
    return get_res_from_jupiter(message)

def RemoveAllLoadsBCs():
    message = "JPT.RemoveAllLoadsBCs()".format()
    return get_res_from_jupiter(message)

def RemoveAllMeshSettings():
    message = "JPT.RemoveAllMeshSettings()".format()
    return get_res_from_jupiter(message)

def RemoveAllFieldTables():
    message = "JPT.RemoveAllFieldTables()".format()
    return get_res_from_jupiter(message)

def RemoveAllAbaqusStep():
    message = "JPT.RemoveAllAbaqusStep()".format()
    return get_res_from_jupiter(message)

def RemoveAllSolverjob():
    message = "JPT.RemoveAllSolverjob()".format()
    return get_res_from_jupiter(message)

def RemoveAllByTableType(Input1):
    message = "JPT.RemoveAllByTableType({})".format(Input1)
    return get_res_from_jupiter(message)

def CreateSubAssembly(Input1,Input2):
    message = "JPT.CreateSubAssembly({},{})".format(Input1,Input2)
    return get_res_from_jupiter(message)

def DeleteSubAssembly(Input1):
    message = "JPT.DeleteSubAssembly({})".format(Input1)
    return get_res_from_jupiter(message)

def FindSubAssemblyByName(Input1):
    message = "JPT.FindSubAssemblyByName({})".format(Input1)
    return get_res_from_jupiter(message)

def FindSubAssemblyByID(Input1):
    message = "JPT.FindSubAssemblyByID({})".format(Input1)
    return get_res_from_jupiter(message)

def DeleteSubAssemblyRecursively(Input1):
    message = "JPT.DeleteSubAssemblyRecursively({})".format(Input1)
    return get_res_from_jupiter(message)

def GetAllPartsInSubAssembly(Input1):
    message = "JPT.GetAllPartsInSubAssembly({})".format(Input1)
    return get_res_from_jupiter(message)

def CastToDItem(Input1):
    message = "JPT.CastToDItem({})".format(Input1)
    return get_res_from_jupiter(message)

def CastDItemToDBody(Input1):
    message = "JPT.CastDItemToDBody({})".format(Input1)
    return get_res_from_jupiter(message)

def CastDItemToDFace(Input1):
    message = "JPT.CastDItemToDFace({})".format(Input1)
    return get_res_from_jupiter(message)

def CastDItemToDElem(Input1):
    message = "JPT.CastDItemToDElem({})".format(Input1)
    return get_res_from_jupiter(message)

def CastDItemToDEdge(Input1):
    message = "JPT.CastDItemToDEdge({})".format(Input1)
    return get_res_from_jupiter(message)

def CastDItemToDGroup(Input1):
    message = "JPT.CastDItemToDGroup({})".format(Input1)
    return get_res_from_jupiter(message)

def CastDItemToDNode(Input1):
    message = "JPT.CastDItemToDNode({})".format(Input1)
    return get_res_from_jupiter(message)

def DItemToMacroTCursorPair(Input1,Input2):
    message = "JPT.DItemToMacroTCursorPair({},{})".format(Input1,Input2)
    return get_res_from_jupiter(message)

def ListDoubleToMacroVector(Input1,Input2,Input3):
    message = "JPT.ListDoubleToMacroVector({},{},{})".format(Input1,Input2,Input3)
    return get_res_from_jupiter(message)

def DTVector3dToMacroVector(Input1):
    message = "JPT.DTVector3dToMacroVector({})".format(Input1)
    return get_res_from_jupiter(message)

def DItemToMacroTCursor(Input1):
    message = "JPT.DItemToMacroTCursor({})".format(Input1)
    return get_res_from_jupiter(message)

def DItemListToMacroListTCursor(Input1):
    message = "JPT.DItemListToMacroListTCursor({})".format(Input1)
    return get_res_from_jupiter(message)

def DItemToMacroListTCursor(Input1):
    message = "JPT.DItemToMacroListTCursor({})".format(Input1)
    return get_res_from_jupiter(message)

def MacroResultParser(Input1,Input2):
    message = "JPT.MacroResultParser({},{})".format(Input1,Input2)
    return get_res_from_jupiter(message)

def MacroListTCursorToListDItem(Input1):
    message = "JPT.MacroListTCursorToListDItem({})".format(Input1)
    return get_res_from_jupiter(message)

def ConvertRGBToJPTColor(Input1):
    message = "JPT.ConvertRGBToJPTColor({})".format(Input1)
    return get_res_from_jupiter(message)

def MacroTCursorToDItem(Input1):
    message = "JPT.MacroTCursorToDItem({})".format(Input1)
    return get_res_from_jupiter(message)

def GetJTDBVersion():
    message = "JPT.GetJTDBVersion()".format()
    return get_res_from_jupiter(message)

def CopyToClipBoard(Input1):
    message = "JPT.CopyToClipBoard({})".format(Input1)
    return get_res_from_jupiter(message)

def CheckLicense(Input1):
    message = "JPT.CheckLicense({})".format(Input1)
    return get_res_from_jupiter(message)

def IsDefaultDouble(Input1):
    message = "JPT.IsDefaultDouble({})".format(Input1)
    return get_res_from_jupiter(message)

def IsDefaultInt(Input1):
    message = "JPT.IsDefaultInt({})".format(Input1)
    return get_res_from_jupiter(message)

def ConvertFromDocUnit(Input1,Input2):
    message = "JPT.ConvertFromDocUnit({},{})".format(Input1,Input2)
    return get_res_from_jupiter(message)

def ConvertValueToDocUnit(Input1,Input2):
    message = "JPT.ConvertValueToDocUnit({},{})".format(Input1,Input2)
    return get_res_from_jupiter(message)

def ConvertFromMacroUnit(Input1,Input2,Input3):
    message = "JPT.ConvertFromMacroUnit({},{},{})".format(Input1,Input2,Input3)
    return get_res_from_jupiter(message)

def ConvertValueToMacroUnit(Input1,Input2,Input3):
    message = "JPT.ConvertValueToMacroUnit({},{},{})".format(Input1,Input2,Input3)
    return get_res_from_jupiter(message)

def GetJPTTempPath():
    message = "JPT.GetJPTTempPath()".format()
    return get_res_from_jupiter(message)

def GetProgramPath():
    message = "JPT.GetProgramPath()".format()
    return get_res_from_jupiter(message)

def GetCurrentDocumentPath():
    message = "JPT.GetCurrentDocumentPath()".format()
    return get_res_from_jupiter(message)

def QuitApplication():
    message = "JPT.QuitApplication()".format()
    return get_res_from_jupiter(message)

def GetAppPathInfo(Input1):
    message = "JPT.GetAppPathInfo({})".format(Input1)
    return get_res_from_jupiter(message)

def GetSelectedNodes():
    message = "JPT.GetSelectedNodes()".format()
    return get_res_from_jupiter(message)

def GetSelectedElems():
    message = "JPT.GetSelectedElems()".format()
    return get_res_from_jupiter(message)

def GetSelectedFaces():
    message = "JPT.GetSelectedFaces()".format()
    return get_res_from_jupiter(message)

def GetSelectedEdges():
    message = "JPT.GetSelectedEdges()".format()
    return get_res_from_jupiter(message)

def GetSelectedParts():
    message = "JPT.GetSelectedParts()".format()
    return get_res_from_jupiter(message)

def GetSelectedGroups():
    message = "JPT.GetSelectedGroups()".format()
    return get_res_from_jupiter(message)

def GetAllParts():
    message = "JPT.GetAllParts()".format()
    return get_res_from_jupiter(message)

def GetAllFaces():
    message = "JPT.GetAllFaces()".format()
    return get_res_from_jupiter(message)

def GetAllEdges():
    message = "JPT.GetAllEdges()".format()
    return get_res_from_jupiter(message)

def GetAllElems():
    message = "JPT.GetAllElems()".format()
    return get_res_from_jupiter(message)

def GetAllNodes():
    message = "JPT.GetAllNodes()".format()
    return get_res_from_jupiter(message)

def GetAllGroups():
    message = "JPT.GetAllGroups()".format()
    return get_res_from_jupiter(message)

def GetAllByTableTypeID(Input1):
    message = "JPT.GetAllByTableTypeID({})".format(Input1)
    return get_res_from_jupiter(message)

def GetAllByTypeID(Input1):
    message = "JPT.GetAllByTypeID({})".format(Input1)
    return get_res_from_jupiter(message)

def GetAllByType(Input1):
    message = "JPT.GetAllByType({})".format(Input1)
    return get_res_from_jupiter(message)

def GetCountByType(Input1: DItem Type):
    message = "JPT.GetCountByType({})".format(Input1: DItem Type)
    return get_res_from_jupiter(message)

def GetLastCreatedCursor():
    message = "JPT.GetLastCreatedCursor()".format()
    return get_res_from_jupiter(message)

def GetAllSelected():
    message = "JPT.GetAllSelected()".format()
    return get_res_from_jupiter(message)

def GetSharedFaces(Input1):
    message = "JPT.GetSharedFaces({})".format(Input1)
    return get_res_from_jupiter(message)

def GetCenterOfEntities(Input1):
    message = "JPT.GetCenterOfEntities({})".format(Input1)
    return get_res_from_jupiter(message)

def GetSharedElements(Input1):
    message = "JPT.GetSharedElements({})".format(Input1)
    return get_res_from_jupiter(message)

def GetSharedNodes(Input1):
    message = "JPT.GetSharedNodes({})".format(Input1)
    return get_res_from_jupiter(message)

def GetAllLoadsBCs():
    message = "JPT.GetAllLoadsBCs()".format()
    return get_res_from_jupiter(message)

def GetMaterialXML():
    message = "JPT.GetMaterialXML()".format()
    return get_res_from_jupiter(message)

def GetMaterialOriginalXML():
    message = "JPT.GetMaterialOriginalXML()".format()
    return get_res_from_jupiter(message)

def GetMaxMaterialID():
    message = "JPT.GetMaxMaterialID()".format()
    return get_res_from_jupiter(message)

def GetMaterialDBById():
    message = "JPT.GetMaterialDBById()".format()
    return get_res_from_jupiter(message)

def GetSelectedNodesCr():
    message = "JPT.GetSelectedNodesCr()".format()
    return get_res_from_jupiter(message)

def GetSelectedElemsCr():
    message = "JPT.GetSelectedElemsCr()".format()
    return get_res_from_jupiter(message)

def GetSelectedFacesCr():
    message = "JPT.GetSelectedFacesCr()".format()
    return get_res_from_jupiter(message)

def GetSelectedEdgesCr():
    message = "JPT.GetSelectedEdgesCr()".format()
    return get_res_from_jupiter(message)

def GetSelectedPartsCr():
    message = "JPT.GetSelectedPartsCr()".format()
    return get_res_from_jupiter(message)

def GetSelectedGroupsCr():
    message = "JPT.GetSelectedGroupsCr()".format()
    return get_res_from_jupiter(message)

def GetUndoCount():
    message = "JPT.GetUndoCount()".format()
    return get_res_from_jupiter(message)

def ClearUndo():
    message = "JPT.ClearUndo()".format()
    return get_res_from_jupiter(message)

def GetRedoCount():
    message = "JPT.GetRedoCount()".format()
    return get_res_from_jupiter(message)

def ClearRedo():
    message = "JPT.ClearRedo()".format()
    return get_res_from_jupiter(message)

def GetOpnList():
    message = "JPT.GetOpnList()".format()
    return get_res_from_jupiter(message)

def GetMacroLog():
    message = "JPT.GetMacroLog()".format()
    return get_res_from_jupiter(message)

def GetPythonAPILog():
    message = "JPT.GetPythonAPILog()".format()
    return get_res_from_jupiter(message)

def ShowHideEntitiesByID(Input1,Input2,Input3):
    message = "JPT.ShowHideEntitiesByID({},{},{})".format(Input1,Input2,Input3)
    return get_res_from_jupiter(message)

def ShowHideAllParts(Input1):
    message = "JPT.ShowHideAllParts({})".format(Input1)
    return get_res_from_jupiter(message)

def InverseHideBodies(Input1):
    message = "JPT.InverseHideBodies({})".format(Input1)
    return get_res_from_jupiter(message)

def ViewFitToModel(Input1):
    message = "JPT.ViewFitToModel({})".format(Input1)
    return get_res_from_jupiter(message)

def Exec(Input1):
    message = "JPT.Exec({})".format(Input1)
    return get_res_from_jupiter(message)

def GetMaxIDEntity(Input1):
    message = "JPT.GetMaxIDEntity({})".format(Input1)
    return get_res_from_jupiter(message)

def GetMinIDEntity(Input1):
    message = "JPT.GetMinIDEntity({})".format(Input1)
    return get_res_from_jupiter(message)

def GetEntitiesByName(Input1,Input2,Input3):
    message = "JPT.GetEntitiesByName({},{},{})".format(Input1,Input2,Input3)
    return get_res_from_jupiter(message)

def GetEntitiesByPosition(Input1,Input2,Input3,Input4):
    message = "JPT.GetEntitiesByPosition({},{},{},{})".format(Input1,Input2,Input3,Input4)
    return get_res_from_jupiter(message)

def GetEntitiesByID(Input1,Input2):
    message = "JPT.GetEntitiesByID({},{})".format(Input1,Input2)
    return get_res_from_jupiter(message)

def GetEntitiesByAssociation(Input1,Input2,Input3):
    message = "JPT.GetEntitiesByAssociation({},{},{})".format(Input1,Input2,Input3)
    return get_res_from_jupiter(message)

def MsgOut(Input1):
    message = "JPT.MsgOut({})".format(Input1)
    return get_res_from_jupiter(message)

def PrintAppPathInfo():
    message = "JPT.PrintAppPathInfo()".format()
    return get_res_from_jupiter(message)

def GetEntitiesByAdjacent(Input1,Input2,Input3):
    message = "JPT.GetEntitiesByAdjacent({},{},{})".format(Input1,Input2,Input3)
    return get_res_from_jupiter(message)

def PrintPSJUtilityManual():
    message = "JPT.PrintPSJUtilityManual()".format()
    return get_res_from_jupiter(message)

def Debugger(Input1):
    message = "JPT.Debugger({})".format(Input1)
    return get_res_from_jupiter(message)

def GetElemsByKind(Input1):
    message = "JPT.GetElemsByKind({})".format(Input1)
    return get_res_from_jupiter(message)

def GetRandomJPTColor():
    message = "JPT.GetRandomJPTColor()".format()
    return get_res_from_jupiter(message)

def ConvertJPTColorToRGB(Input1):
    message = "JPT.ConvertJPTColorToRGB({})".format(Input1)
    return get_res_from_jupiter(message)

def ClearLog():
    message = "JPT.ClearLog()".format()
    return get_res_from_jupiter(message)

def SetSelectMethod(Input1):
    message = "JPT.SetSelectMethod({})".format(Input1)
    return get_res_from_jupiter(message)

def MacroTCursorPairToDItemPair(Input1):
    message = "JPT.MacroTCursorPairToDItemPair({})".format(Input1)
    return get_res_from_jupiter(message)

def MessageBoxPSJ(Input1,Input2):
    message = "JPT.MessageBoxPSJ({},{})".format(Input1,Input2)
    return get_res_from_jupiter(message)

def RemoveAllContacts():
    message = "JPT.RemoveAllContacts()".format()
    return get_res_from_jupiter(message)

def RemoveAllLoadCases():
    message = "JPT.RemoveAllLoadCases()".format()
    return get_res_from_jupiter(message)

def RemoveAllCoordinates():
    message = "JPT.RemoveAllCoordinates()".format()
    return get_res_from_jupiter(message)

