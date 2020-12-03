```{module} MeshEdit.ChangePattern()
:synopsis: Element ChangePattern
```

(MeshEdit.ChangePattern)=

# MeshEdit.ChangePattern

## Description

Element ChangePattern

## Syntax

```python
MeshEdit.ChangePattern(crlFace=[], iPatternType=0)
```

Macro: {ref}`Macro-MeshEdit-GeomEditChangePatternCr`

Ribbon: {menuselection}`MeshEdit --> ChangePattern`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`iPatternType`**
: An _Integer_ specifying the pattern type. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.ChangePattern(crlFace=[], iPatternType=0)
```
