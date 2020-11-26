def RemoveEntitiesByID(Input1,Input2):
    message = "JPT.RemoveEntitiesByID({},{})".format(Input1,Input2)
    return JPT_RUN_LINE(message)

def RemoveEntitiesByName(Input1,Input2_str,Input3):
    message = "JPT.RemoveEntitiesByName({},'{}',{})".format(Input1,Input2_str,Input3)
    return JPT_RUN_LINE(message)

def RemoveAllContacts():
    message = "JPT.RemoveAllContacts()".format()
    return JPT_RUN_LINE(message)

def RemoveAllLoadsBCs():
    message = "JPT.RemoveAllLoadsBCs()".format()
    return JPT_RUN_LINE(message)

def RemoveAllMaterials():
    message = "JPT.RemoveAllMaterials()".format()
    return JPT_RUN_LINE(message)

def RemoveWSProperties():
    message = "JPT.RemoveWSProperties()".format()
    return JPT_RUN_LINE(message)

def RemoveAllCoordinates():
    message = "JPT.RemoveAllCoordinates()".format()
    return JPT_RUN_LINE(message)

def RemoveAllMeshSettings():
    message = "JPT.RemoveAllMeshSettings()".format()
    return JPT_RUN_LINE(message)

def RemoveAllFieldTables():
    message = "JPT.RemoveAllFieldTables()".format()
    return JPT_RUN_LINE(message)

def RemoveAllAbaqusStep():
    message = "JPT.RemoveAllAbaqusStep()".format()
    return JPT_RUN_LINE(message)

def RemoveAllConnections():
    message = "JPT.RemoveAllConnections()".format()
    return JPT_RUN_LINE(message)

def RemoveAllByTableType(Input1):
    message = "JPT.RemoveAllByTableType({})".format(Input1)
    return JPT_RUN_LINE(message)

def CreateSubAssembly(Input1_str,Input2):
    message = "JPT.CreateSubAssembly('{}',{})".format(Input1_str,Input2)
    return JPT_RUN_LINE(message)

def DeleteSubAssembly(Input1):
    message = "JPT.DeleteSubAssembly({})".format(Input1)
    return JPT_RUN_LINE(message)

def FindSubAssemblyByName(Input1_str):
    message = "JPT.FindSubAssemblyByName('{}')".format(Input1_str)
    return JPT_RUN_LINE(message)

def FindSubAssemblyByID(Input1):
    message = "JPT.FindSubAssemblyByID({})".format(Input1)
    return JPT_RUN_LINE(message)

def DeleteSubAssemblyRecursively(Input1):
    message = "JPT.DeleteSubAssemblyRecursively({})".format(Input1)
    return JPT_RUN_LINE(message)

def CastToDItem(Input1):
    message = "JPT.CastToDItem({})".format(Input1)
    return JPT_RUN_LINE(message)

def RemoveAllLoadCases():
    message = "JPT.RemoveAllLoadCases()".format()
    return JPT_RUN_LINE(message)

def CastDItemToDBody(Input1):
    message = "JPT.CastDItemToDBody({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetAllPartsInSubAssembly(Input1):
    message = "JPT.GetAllPartsInSubAssembly({})".format(Input1)
    return JPT_RUN_LINE(message)

def RemoveAllSolverjob():
    message = "JPT.RemoveAllSolverjob()".format()
    return JPT_RUN_LINE(message)

def CastDItemToDElem(Input1):
    message = "JPT.CastDItemToDElem({})".format(Input1)
    return JPT_RUN_LINE(message)

def CastDItemToDEdge(Input1):
    message = "JPT.CastDItemToDEdge({})".format(Input1)
    return JPT_RUN_LINE(message)

def CastDItemToDGroup(Input1):
    message = "JPT.CastDItemToDGroup({})".format(Input1)
    return JPT_RUN_LINE(message)

def CastDItemToDNode(Input1):
    message = "JPT.CastDItemToDNode({})".format(Input1)
    return JPT_RUN_LINE(message)

def CastDItemToDFace(Input1):
    message = "JPT.CastDItemToDFace({})".format(Input1)
    return JPT_RUN_LINE(message)

def DItemToMacroTCursorPair(Input1,Input2):
    message = "JPT.DItemToMacroTCursorPair({},{})".format(Input1,Input2)
    return JPT_RUN_LINE(message)

def ListDoubleToMacroVector(Input1,Input2,Input3):
    message = "JPT.ListDoubleToMacroVector({},{},{})".format(Input1,Input2,Input3)
    return JPT_RUN_LINE(message)

def DItemToMacroTCursor(Input1):
    message = "JPT.DItemToMacroTCursor({})".format(Input1)
    return JPT_RUN_LINE(message)

def DItemListToMacroListTCursor(Input1):
    message = "JPT.DItemListToMacroListTCursor({})".format(Input1)
    return JPT_RUN_LINE(message)

def MacroResultParser(Input1_str,Input2_str):
    message = "JPT.MacroResultParser('{}','{}')".format(Input1_str,Input2_str)
    return JPT_RUN_LINE(message)

def DItemToMacroListTCursor(Input1):
    message = "JPT.DItemToMacroListTCursor({})".format(Input1)
    return JPT_RUN_LINE(message)

def MacroListTCursorToListDItem(Input1_str):
    message = "JPT.MacroListTCursorToListDItem('{}')".format(Input1_str)
    return JPT_RUN_LINE(message)

def MacroTCursorToDItem(Input1_str):
    message = "JPT.MacroTCursorToDItem('{}')".format(Input1_str)
    return JPT_RUN_LINE(message)

def CopyToClipBoard(Input1_str):
    message = "JPT.CopyToClipBoard('{}')".format(Input1_str)
    return JPT_RUN_LINE(message)

def GetJTDBVersion():
    message = "JPT.GetJTDBVersion()".format()
    return JPT_RUN_LINE(message)

def IsDefaultDouble(Input1):
    message = "JPT.IsDefaultDouble({})".format(Input1)
    return JPT_RUN_LINE(message)

def IsDefaultInt(Input1):
    message = "JPT.IsDefaultInt({})".format(Input1)
    return JPT_RUN_LINE(message)

def CheckLicense(Input1_str):
    message = "JPT.CheckLicense('{}')".format(Input1_str)
    return JPT_RUN_LINE(message)

def ConvertRGBToJPTColor(Input1):
    message = "JPT.ConvertRGBToJPTColor({})".format(Input1)
    return JPT_RUN_LINE(message)

def ConvertValueToDocUnit(Input1,Input2):
    message = "JPT.ConvertValueToDocUnit({},{})".format(Input1,Input2)
    return JPT_RUN_LINE(message)

def DTVector3dToMacroVector(Input1):
    message = "JPT.DTVector3dToMacroVector({})".format(Input1)
    return JPT_RUN_LINE(message)

def ConvertFromDocUnit(Input1,Input2):
    message = "JPT.ConvertFromDocUnit({},{})".format(Input1,Input2)
    return JPT_RUN_LINE(message)

def ConvertFromMacroUnit(Input1,Input2,Input3_str):
    message = "JPT.ConvertFromMacroUnit({},{},'{}')".format(Input1,Input2,Input3_str)
    return JPT_RUN_LINE(message)

def ConvertValueToMacroUnit(Input1,Input2,Input3_str):
    message = "JPT.ConvertValueToMacroUnit({},{},'{}')".format(Input1,Input2,Input3_str)
    return JPT_RUN_LINE(message)

def GetJPTTempPath():
    message = "JPT.GetJPTTempPath()".format()
    return JPT_RUN_LINE(message)

def GetCurrentDocumentPath():
    message = "JPT.GetCurrentDocumentPath()".format()
    return JPT_RUN_LINE(message)

def GetProgramPath():
    message = "JPT.GetProgramPath()".format()
    return JPT_RUN_LINE(message)

def GetAppPathInfo(Input1):
    message = "JPT.GetAppPathInfo({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetSelectedElems():
    message = "JPT.GetSelectedElems()".format()
    return JPT_RUN_LINE(message)

def GetSelectedNodes():
    message = "JPT.GetSelectedNodes()".format()
    return JPT_RUN_LINE(message)

def QuitApplication():
    message = "JPT.QuitApplication()".format()
    return JPT_RUN_LINE(message)

def GetSelectedFaces():
    message = "JPT.GetSelectedFaces()".format()
    return JPT_RUN_LINE(message)

def GetSelectedEdges():
    message = "JPT.GetSelectedEdges()".format()
    return JPT_RUN_LINE(message)

def GetSelectedGroups():
    message = "JPT.GetSelectedGroups()".format()
    return JPT_RUN_LINE(message)

def GetSelectedParts():
    message = "JPT.GetSelectedParts()".format()
    return JPT_RUN_LINE(message)

def GetAllParts():
    message = "JPT.GetAllParts()".format()
    return JPT_RUN_LINE(message)

def GetAllEdges():
    message = "JPT.GetAllEdges()".format()
    return JPT_RUN_LINE(message)

def GetAllFaces():
    message = "JPT.GetAllFaces()".format()
    return JPT_RUN_LINE(message)

def GetAllElems():
    message = "JPT.GetAllElems()".format()
    return JPT_RUN_LINE(message)

def GetAllGroups():
    message = "JPT.GetAllGroups()".format()
    return JPT_RUN_LINE(message)

def GetAllNodes():
    message = "JPT.GetAllNodes()".format()
    return JPT_RUN_LINE(message)

def GetAllByTypeID(Input1):
    message = "JPT.GetAllByTypeID({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetAllByTableTypeID(Input1):
    message = "JPT.GetAllByTableTypeID({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetAllByType(Input1):
    message = "JPT.GetAllByType({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetCountByType(Input1):
    message = "JPT.GetCountByType({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetCenterOfEntities(Input1):
    message = "JPT.GetCenterOfEntities({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetAllSelected():
    message = "JPT.GetAllSelected()".format()
    return JPT_RUN_LINE(message)

def GetLastCreatedCursor():
    message = "JPT.GetLastCreatedCursor()".format()
    return JPT_RUN_LINE(message)

def GetSharedElements(Input1):
    message = "JPT.GetSharedElements({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetSharedFaces(Input1):
    message = "JPT.GetSharedFaces({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetMaterialXML():
    message = "JPT.GetMaterialXML()".format()
    return JPT_RUN_LINE(message)

def GetMaterialOriginalXML():
    message = "JPT.GetMaterialOriginalXML()".format()
    return JPT_RUN_LINE(message)

def GetMaxMaterialID():
    message = "JPT.GetMaxMaterialID()".format()
    return JPT_RUN_LINE(message)

def GetMaterialDBById():
    message = "JPT.GetMaterialDBById()".format()
    return JPT_RUN_LINE(message)

def GetSelectedNodesCr():
    message = "JPT.GetSelectedNodesCr()".format()
    return JPT_RUN_LINE(message)

def GetSelectedElemsCr():
    message = "JPT.GetSelectedElemsCr()".format()
    return JPT_RUN_LINE(message)

def GetAllLoadsBCs():
    message = "JPT.GetAllLoadsBCs()".format()
    return JPT_RUN_LINE(message)

def GetSelectedEdgesCr():
    message = "JPT.GetSelectedEdgesCr()".format()
    return JPT_RUN_LINE(message)

def GetSharedNodes(Input1):
    message = "JPT.GetSharedNodes({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetSelectedPartsCr():
    message = "JPT.GetSelectedPartsCr()".format()
    return JPT_RUN_LINE(message)

def GetSelectedGroupsCr():
    message = "JPT.GetSelectedGroupsCr()".format()
    return JPT_RUN_LINE(message)

def GetUndoCount():
    message = "JPT.GetUndoCount()".format()
    return JPT_RUN_LINE(message)

def ClearUndo():
    message = "JPT.ClearUndo()".format()
    return JPT_RUN_LINE(message)

def GetRedoCount():
    message = "JPT.GetRedoCount()".format()
    return JPT_RUN_LINE(message)

def GetOpnList():
    message = "JPT.GetOpnList()".format()
    return JPT_RUN_LINE(message)

def GetSelectedFacesCr():
    message = "JPT.GetSelectedFacesCr()".format()
    return JPT_RUN_LINE(message)

def GetPythonAPILog():
    message = "JPT.GetPythonAPILog()".format()
    return JPT_RUN_LINE(message)

def ShowHideEntitiesByID(Input1,Input2,Input3):
    message = "JPT.ShowHideEntitiesByID({},{},{})".format(Input1,Input2,Input3)
    return JPT_RUN_LINE(message)

def ShowHideAllParts(Input1):
    message = "JPT.ShowHideAllParts({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetMacroLog():
    message = "JPT.GetMacroLog()".format()
    return JPT_RUN_LINE(message)

def InverseHideBodies(Input1):
    message = "JPT.InverseHideBodies({})".format(Input1)
    return JPT_RUN_LINE(message)

def Exec(Input1_str):
    message = "JPT.Exec('{}')".format(Input1_str)
    return JPT_RUN_LINE(message)

def GetMaxIDEntity(Input1):
    message = "JPT.GetMaxIDEntity({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetMinIDEntity(Input1):
    message = "JPT.GetMinIDEntity({})".format(Input1)
    return JPT_RUN_LINE(message)

def ViewFitToModel(Input1):
    message = "JPT.ViewFitToModel({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetEntitiesByName(Input1,Input2_str,Input3):
    message = "JPT.GetEntitiesByName({},'{}',{})".format(Input1,Input2_str,Input3)
    return JPT_RUN_LINE(message)

def ClearRedo():
    message = "JPT.ClearRedo()".format()
    return JPT_RUN_LINE(message)

def GetEntitiesByID(Input1,Input2):
    message = "JPT.GetEntitiesByID({},{})".format(Input1,Input2)
    return JPT_RUN_LINE(message)

def GetEntitiesByPosition(Input1,Input2,Input3,Input4):
    message = "JPT.GetEntitiesByPosition({},{},{},{})".format(Input1,Input2,Input3,Input4)
    return JPT_RUN_LINE(message)

def GetEntitiesByAdjacent(Input1,Input2,Input3):
    message = "JPT.GetEntitiesByAdjacent({},{},{})".format(Input1,Input2,Input3)
    return JPT_RUN_LINE(message)

def MsgOut(Input1_str):
    message = "JPT.MsgOut('{}')".format(Input1_str)
    return JPT_RUN_LINE(message)

def PrintPSJUtilityManual():
    message = "JPT.PrintPSJUtilityManual()".format()
    return JPT_RUN_LINE(message)

def GetEntitiesByAssociation(Input1,Input2,Input3):
    message = "JPT.GetEntitiesByAssociation({},{},{})".format(Input1,Input2,Input3)
    return JPT_RUN_LINE(message)

def GetElemsByKind(Input1):
    message = "JPT.GetElemsByKind({})".format(Input1)
    return JPT_RUN_LINE(message)

def GetRandomJPTColor():
    message = "JPT.GetRandomJPTColor()".format()
    return JPT_RUN_LINE(message)

def ConvertJPTColorToRGB(Input1):
    message = "JPT.ConvertJPTColorToRGB({})".format(Input1)
    return JPT_RUN_LINE(message)

def ClearLog():
    message = "JPT.ClearLog()".format()
    return JPT_RUN_LINE(message)

def Debugger(Input1):
    message = "JPT.Debugger({})".format(Input1)
    return JPT_RUN_LINE(message)

def MacroTCursorPairToDItemPair(Input1_str):
    message = "JPT.MacroTCursorPairToDItemPair('{}')".format(Input1_str)
    return JPT_RUN_LINE(message)

def SetSelectMethod(Input1):
    message = "JPT.SetSelectMethod({})".format(Input1)
    return JPT_RUN_LINE(message)

def PrintAppPathInfo():
    message = "JPT.PrintAppPathInfo()".format()
    return JPT_RUN_LINE(message)

def MessageBoxPSJ(Input1_str,Input2):
    message = "JPT.MessageBoxPSJ('{}',{})".format(Input1_str,Input2)
    return JPT_RUN_LINE(message)

