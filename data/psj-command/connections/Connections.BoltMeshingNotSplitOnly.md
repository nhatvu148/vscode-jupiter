```{module} Connections.BoltMeshingNotSplitOnly()
:synopsis: Unknown Description
```

(Connections.BoltMeshingNotSplitOnly)=

# Connections.BoltMeshingNotSplitOnly

## Description

Unknown Description

## Syntax

```python
Connections.BoltMeshingNotSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE_MESH(), iLBCPRETENSIONDATAIdir=0, dLBCPRETENSIONDATADvalue=0.0, bLBCPRETENSIONDATABfixlength=False, crLBCPRETENSIONDATACrtable=None, crLBCPRETENSIONDATACrcoord=None, iLBCPRETENSIONDATAIlocalunit=0, crlTarget=[], poslCutter=[])
```

Macro: {ref}`Macro-Connections-BoltMeshing2_NotSplitOnly`

Ribbon: {menuselection}`Connections --> BoltMeshingNotSplitOnly`

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

**`iLBCPRETENSIONDATAIdir`**
: An _Integer_ specifying the load boundary condition pretension data direction. The default value is 0.

**`dLBCPRETENSIONDATADvalue`**
: A _Double_ specifying the load boundary condition pretension data value. The default value is 0.0.

**`bLBCPRETENSIONDATABfixlength`**
: A _Boolean_ specifying the load boundary condition pretension data fixed length. The default value is False.

**`crLBCPRETENSIONDATACrtable`**
: A _Cursor_ specifying the load boundary condition pretension data table. The default value is None.

**`crLBCPRETENSIONDATACrcoord`**
: A _Cursor_ specifying the load boundary condition pretension data coordinate. The default value is None.

**`iLBCPRETENSIONDATAIlocalunit`**
: An _Integer_ specifying the load boundary condition pretension data local unit. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`poslCutter`**
: A _Position List_ specifying the cutter. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.BoltMeshingNotSplitOnly(strName="", iPartcutparamImethod=0, dPartcutparamDoffset=0.0, iPartcutparamBshareface=0, iPartcutparamBseparateface=0, iPartcutparamBsplitonly=0, iPartcutparamBmakesectionface=0, crPartcutparamCoord=None, surfaceMesh=SURFACE_MESH(), iLBCPRETENSIONDATAIdir=0, dLBCPRETENSIONDATADvalue=0.0, bLBCPRETENSIONDATABfixlength=False, crLBCPRETENSIONDATACrtable=None, crLBCPRETENSIONDATACrcoord=None, iLBCPRETENSIONDATAIlocalunit=0, crlTarget=[], poslCutter=[])
```
