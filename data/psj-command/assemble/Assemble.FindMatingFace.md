```{module} Assemble.FindMatingFace()
:synopsis: Find Mating Face For Assemble Faces
```

(Assemble.FindMatingFace)=

# Assemble.FindMatingFace

## Description

Find Mating Face For Assemble Faces

## Syntax

```python
Assemble.FindMatingFace(crlMasterFaces=[], crlSlaveFaces=[], crlPart=[], dTolerance=0.0)
```

Macro: {ref}`Macro-Assemble-Assemble_Faces_MatingStep`

Ribbon: {menuselection}`Assemble --> FindMatingFace`

## Inputs

**`crlMasterFaces`**
: A _Cursor List_ specifying the master faces. The default value is [].

**`crlSlaveFaces`**
: A _Cursor List_ specifying the slave faces. The default value is [].

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 0.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assemble.FindMatingFace(crlMasterFaces=[], crlSlaveFaces=[], crlPart=[], dTolerance=0.0)
```
