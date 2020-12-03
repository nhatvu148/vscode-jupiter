```{module} MeshEdit.CreateNode.Offset()
:synopsis: MeshEdit CreateNode CreateNodeNodeOffset
```

(MeshEdit.CreateNode.Offset)=

# MeshEdit.CreateNode.Offset

## Description

MeshEdit CreateNode CreateNodeNodeOffset

## Syntax

```python
MeshEdit.CreateNode.Offset(vecOffset=[], iRep=1, crlNode=[], crCoord=None)
```

Macro: {ref}`Macro-MeshEdit-CreateNodeOffset`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> Offset`

## Inputs

**`vecOffset`**
: A _Vector_ specifying the offset. The default value is [].

**`iRep`**
: An _Integer_ specifying the repeat times. The default value is 1.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.Offset(vecOffset=[], iRep=1, crlNode=[], crCoord=None)
```
