```{module} HexModeling.AutoSweep()
:synopsis: Hex Modeling Auto Sweep
```

(HexModeling.AutoSweep)=

# HexModeling.AutoSweep

## Description

Hex Modeling Auto Sweep

## Syntax

```python
HexModeling.AutoSweep(crlPart=[], dMeshSize=0.0, bLayers=False, iLayers=2)
```

Macro: {ref}`Macro-HexModeling-HexModelAutoSweep`

Ribbon: {menuselection}`HexModeling --> AutoSweep`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`dMeshSize`**
: A _Double_ specifying the mesh size. The default value is 0.0.

**`bLayers`**
: A _Boolean_ specifying the layers. The default value is False.

**`iLayers`**
: An _Integer_ specifying the layers. The default value is 2.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
HexModeling.AutoSweep(crlPart=[], dMeshSize=0.0, bLayers=False, iLayers=2)
```
