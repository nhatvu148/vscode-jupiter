```{module} Assemble.AssembleFaces()
:synopsis: Assemble AssembleFaces
```

(Assemble.AssembleFaces)=

# Assemble.AssembleFaces

## Description

Assemble AssembleFaces

## Syntax

```python
Assemble.AssembleFaces(ilPairFaceToMakeShareFace=[], dTolerance=0.1, iTypeConnectPos=1, bUseSnapInput=False, dSnapTolerance=0.005, bFitEdge=False)
```

Macro: {ref}`Macro-Assemble-Assemble_Faces`

Ribbon: {menuselection}`Assemble --> AssembleFaces`

## Inputs

**`ilPairFaceToMakeShareFace`**
: A _Integer List_ specifying the pair face to make share face. The default value is [].

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 0.1.

**`iTypeConnectPos`**
: An _Integer_ specifying the type connect position. The default value is 1.

**`bUseSnapInput`**
: A _Boolean_ specifying the use snap input. The default value is False.

**`dSnapTolerance`**
: A _Double_ specifying the snap tolerance. The default value is 0.005.

**`bFitEdge`**
: A _Boolean_ specifying the fit edge. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assemble.AssembleFaces(ilPairFaceToMakeShareFace=[], dTolerance=0.1, iTypeConnectPos=1, bUseSnapInput=False, dSnapTolerance=0.005, bFitEdge=False)
```
