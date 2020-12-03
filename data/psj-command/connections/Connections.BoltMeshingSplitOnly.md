```{module} Connections.BoltMeshingSplitOnly()
:synopsis: Unknown Description
```

(Connections.BoltMeshingSplitOnly)=

# Connections.BoltMeshingSplitOnly

## Description

Unknown Description

## Syntax

```python
Connections.BoltMeshingSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE_MESH(), bLBCPRETENSIONABAQUSDATABfixedlenght=False, crLBCPRETENSIONABAQUSDATACrtable=None, dLBCPRETENSIONABAQUSDATADvalue=0.0, iLBCPRETENSIONABAQUSDATAIlocalunit=0, strLBCPRETENSIONABAQUSDATAStrnormal="", posLBCPRETENSIONABAQUSDATATvctrolnodepos=[0,0,0], crlTarget=[], poslCutter=[])
```

Macro: {ref}`Macro-Connections-BoltMeshing2_SplitOnly`

Ribbon: {menuselection}`Connections --> BoltMeshingSplitOnly`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iPartcutparamImethod`**
: An _Integer_ specifying the part cut parameter method. The default value is 0.

**`dPartcutparamDoffset`**
: A _Double_ specifying the part cut parameter offset. The default value is 0.0.

**`iPartcutparamBshareface`**
: An _Integer_ specifying the part cut parameter share face. The default value is 0.

**`iPartcutparamBseparateface`**
: An _Integer_ specifying the part cut parameter separate face. The default value is 0.

**`iPartcutparamBsplitonly`**
: An _Integer_ specifying the part cut parameter split only. The default value is 0.

**`iPartcutparamBmakesectionface`**
: An _Integer_ specifying the part cut parameter make section face. The default value is 0.

**`crPartcutparamCoord`**
: A _Cursor_ specifying the part cut parameter coordinate. The default value is None.

**`surfaceMesh`**
: A _SURFACE_MESH_ specifying the mesh. The default value is SURFACE_MESH().

**`bLBCPRETENSIONABAQUSDATABfixedlenght`**
: A _Boolean_ specifying the load boundary condition pretension abaqus data fixed length. The default value is False.

**`crLBCPRETENSIONABAQUSDATACrtable`**
: A _Cursor_ specifying the load boundary condition pretension abaqus data table. The default value is None.

**`dLBCPRETENSIONABAQUSDATADvalue`**
: A _Double_ specifying the load boundary condition pretension abaqus data value. The default value is 0.0.

**`iLBCPRETENSIONABAQUSDATAIlocalunit`**
: An _Integer_ specifying the load boundary condition pretension abaqus data local unit. The default value is 0.

**`strLBCPRETENSIONABAQUSDATAStrnormal`**
: A _String_ specifying the load boundary condition pretension abaqus data normal. The default value is "".

**`posLBCPRETENSIONABAQUSDATATvctrolnodepos`**
: A _Position_ specifying the load boundary condition pretension abaqus data node position. The default value is [0,0,0].

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`poslCutter`**
: A _Position List_ specifying the cutter. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.BoltMeshingSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE_MESH(), bLBCPRETENSIONABAQUSDATABfixedlenght=False, crLBCPRETENSIONABAQUSDATACrtable=None, dLBCPRETENSIONABAQUSDATADvalue=0.0, iLBCPRETENSIONABAQUSDATAIlocalunit=0, strLBCPRETENSIONABAQUSDATAStrnormal="", posLBCPRETENSIONABAQUSDATATvctrolnodepos=[0,0,0], crlTarget=[], poslCutter=[])
```
