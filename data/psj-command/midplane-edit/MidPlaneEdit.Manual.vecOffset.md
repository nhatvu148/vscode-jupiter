```{module} MidPlaneEdit.Manual.vecOffset()
:synopsis: Unknown Description
```

(MidPlaneEdit.Manual.vecOffset)=

# MidPlaneEdit.Manual.vecOffset

## Description

Unknown Description

## Syntax

```python
MidPlaneEdit.Manual.vecOffset(crlFace, crPart, dOffset, bCyl, strNewPartName)
```

Macro: {ref}`Macro-MidPlaneEdit-MidplaneManualOffset`

Ribbon: {menuselection}`MidPlaneEdit --> Manual --> vecOffset`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`crPart`**
: A _Cursor_ specifying the part. This is a required input.

**`dOffset`**
: A _Double_ specifying the offset. This is a required input.

**`bCyl`**
: A _Boolean_ specifying the cylinder. This is a required input.

**`strNewPartName`**
: A _String_ specifying the new part name. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MidPlaneEdit.Manual.vecOffset(crlFace, crPart, dOffset, bCyl, strNewPartName)
```
