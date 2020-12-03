```{module} OasisAWizard.LocalMeshing.FilletMapMeshing()
:synopsis:
```

(OasisAWizard.LocalMeshing.FilletMapMeshing)=

# OasisAWizard.LocalMeshing.FilletMapMeshing

## Description

## Syntax

```python
OasisAWizard.LocalMeshing.FilletMapMeshing(crlPart=[], crlFace=[], dMinLength=0.0, dMaxLength=1.0, dMinRadius=0.0, dMaxRadius=9e-3, bConvex=True, bConcave=True, iTmp=0, dLengthSingleLayer=0, dBMinLengthForSingleLayer=0, dRadiusSingleLayer=0, dBMinRadiusForSingleLayer=0, iMinlayer=0, bMinLayer=False)
```

Macro: {ref}`Macro-OasisAWizard-FilletMapMeshing`

Ribbon: {menuselection}`OasisAWizard --> LocalMeshing --> FilletMapMeshing`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`dMinLength`**
: A _Double_ specifying the minimum length. The default value is 0.0.

**`dMaxLength`**
: A _Double_ specifying the maximum length. The default value is 1.0.

**`dMinRadius`**
: A _Double_ specifying the minimum radius. The default value is 0.0.

**`dMaxRadius`**
: A _Double_ specifying the maximum radius. The default value is 9e-3.

**`bConvex`**
: A _Boolean_ specifying the convex. The default value is True.

**`bConcave`**
: A _Boolean_ specifying the concave. The default value is True.

**`iTmp`**
: An _Integer_ specifying the temporary. The default value is 0.

**`dLengthSingleLayer`**
: A _Double_ specifying the length single layer. The default value is 0.

**`dBMinLengthForSingleLayer`**
: A _Double_ specifying the minimum length for single layer. The default value is 0.

**`dRadiusSingleLayer`**
: A _Double_ specifying the radius single layer. The default value is 0.

**`dBMinRadiusForSingleLayer`**
: A _Double_ specifying the minimum radius for single layer. The default value is 0.

**`iMinlayer`**
: An _Integer_ specifying the minlayer. The default value is 0.

**`bMinLayer`**
: A _Boolean_ specifying the minimum layer. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
OasisAWizard.LocalMeshing.FilletMapMeshing(crlPart=[], crlFace=[], dMinLength=0.0, dMaxLength=1.0, dMinRadius=0.0, dMaxRadius=9e-3, bConvex=True, bConcave=True, iTmp=0, dLengthSingleLayer=0, dBMinLengthForSingleLayer=0, dRadiusSingleLayer=0, dBMinRadiusForSingleLayer=0, iMinlayer=0, bMinLayer=False)
```
