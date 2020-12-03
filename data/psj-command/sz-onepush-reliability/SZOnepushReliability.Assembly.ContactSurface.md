```{module} SZOnepushReliability.Assembly.ContactSurface()
:synopsis: Contact surface
```

(SZOnepushReliability.Assembly.ContactSurface)=

# SZOnepushReliability.Assembly.ContactSurface

## Description

Contact surface

## Syntax

```python
SZOnepushReliability.Assembly.ContactSurface(crlSrcFace, crlTarPart, dTolerance, iLayer)
```

Macro: {ref}`Macro-SZOnepushReliability-SOR_CopyContactSurface`

Ribbon: {menuselection}`SZOnepushReliability --> Assembly --> ContactSurface`

## Inputs

**`crlSrcFace`**
: A _Cursor List_ specifying the source face. This is a required input.

**`crlTarPart`**
: A _Cursor List_ specifying the tar part. This is a required input.

**`dTolerance`**
: A _Double_ specifying the tolerance. This is a required input.

**`iLayer`**
: An _Integer_ specifying the layer. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
SZOnepushReliability.Assembly.ContactSurface(crlSrcFace, crlTarPart, dTolerance, iLayer)
```
