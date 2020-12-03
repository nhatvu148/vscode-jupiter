```{module} SNOnePush.AutoSweepClosedLoopShaped()
:synopsis: Make hexa for closed loop shaped
```

(SNOnePush.AutoSweepClosedLoopShaped)=

# SNOnePush.AutoSweepClosedLoopShaped

## Description

Make hexa for closed loop shaped

## Syntax

```python
SNOnePush.AutoSweepClosedLoopShaped(crlPart, dMeshSize, dLengthSize)
```

Macro: {ref}`Macro-SNOnePush-AutoSweepClosedLoopShaped`

Ribbon: {menuselection}`SNOnePush --> AutoSweepClosedLoopShaped`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`dMeshSize`**
: A _Double_ specifying the mesh size. This is a required input.

**`dLengthSize`**
: A _Double_ specifying the length size. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
SNOnePush.AutoSweepClosedLoopShaped(crlPart, dMeshSize, dLengthSize)
```
