```{module} MeshEdit.DividePartByRegion()
:synopsis: Divide Part By Region
```

(MeshEdit.DividePartByRegion)=

# MeshEdit.DividePartByRegion

## Description

Divide Part By Region

## Syntax

```python
MeshEdit.DividePartByRegion(crlPart=[], crlBoundaryParts=[])
```

Macro: {ref}`Macro-MeshEdit-DividePartByRegion`

Ribbon: {menuselection}`MeshEdit --> DividePartByRegion`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`crlBoundaryParts`**
: A _Cursor List_ specifying the boundary parts. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.DividePartByRegion(crlPart=[], crlBoundaryParts=[])
```
