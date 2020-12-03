```{module} MeshEdit.CreateElement.Tet()
:synopsis: create element Tet
```

(MeshEdit.CreateElement.Tet)=

# MeshEdit.CreateElement.Tet

## Description

create element Tet

## Syntax

```python
MeshEdit.CreateElement.Tet(iParentEntityId=0, crlNode=[], crlElem=[])
```

Macro: {ref}`Macro-MeshEdit-CreateElementTET4_ME`

Ribbon: {menuselection}`MeshEdit --> CreateElement --> Tet`

## Inputs

**`iParentEntityId`**
: An _Integer_ specifying the parent entity ID. The default value is 0.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crlElem`**
: A _Cursor List_ specifying the element. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateElement.Tet(iParentEntityId=0, crlNode=[], crlElem=[])
```
