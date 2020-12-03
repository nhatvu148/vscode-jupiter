```{module} HexModeling.Sweep.Linear()
:synopsis: Unknown Description
```

(HexModeling.Sweep.Linear)=

# HexModeling.Sweep.Linear

## Description

Unknown Description

## Syntax

```python
HexModeling.Sweep.Linear(crlFace=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0)
```

Macro: {ref}`Macro-HexModeling-HexSweepLinear`

Ribbon: {menuselection}`HexModeling --> Sweep --> Linear`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`dLength`**
: A _Double_ specifying the length. The default value is 10.

**`iLayer`**
: An _Integer_ specifying the layer. The default value is 10.

**`dlSweepDirection`**
: A _Double List_ specifying the sweep direction. The default value is [].

**`bInterfaceElemFlag`**
: A _Boolean_ specifying the interface element flag. The default value is False.

**`iLinearMethod`**
: An _Integer_ specifying the linear method. The default value is 0.

**`bDeleteOriginalParts`**
: A _Boolean_ specifying the delete original parts. The default value is False.

**`bDeleteTargetParts`**
: A _Boolean_ specifying the delete target parts. The default value is False.

**`iMethodBias`**
: An _Integer_ specifying the method bias. The default value is 0.

**`dFactor`**
: A _Double_ specifying the factor. The default value is 2.0.

**`iProgression`**
: An _Integer_ specifying the progression. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
HexModeling.Sweep.Linear(crlFace=[], dLength=10, iLayer=10, dlSweepDirection=[], bInterfaceElemFlag=False, iLinearMethod=0, bDeleteOriginalParts=False, bDeleteTargetParts=False, iMethodBias=0, dFactor=2.0, iProgression=0)
```
