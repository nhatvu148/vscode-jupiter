```{module} MeshEdit.ElementConvert()
:synopsis: Element Conversion
```

(MeshEdit.ElementConvert)=

# MeshEdit.ElementConvert

## Description

Element Conversion

## Syntax

```python
MeshEdit.ElementConvert(crlPart=[], iType=1)
```

Macro: {ref}`Macro-MeshEdit-ElementConvert`

Ribbon: {menuselection}`MeshEdit --> ElementConvert`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`iType`**
: An _Integer_ specifying the type. The default value is 1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.ElementConvert(crlPart=[], iType=1)
```
