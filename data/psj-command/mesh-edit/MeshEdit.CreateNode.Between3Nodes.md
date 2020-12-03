```{module} MeshEdit.CreateNode.Between3Nodes()
:synopsis: create node point
```

(MeshEdit.CreateNode.Between3Nodes)=

# MeshEdit.CreateNode.Between3Nodes

## Description

create node point

## Syntax

```python
MeshEdit.CreateNode.Between3Nodes(iNodeID=0, dX=0.0, dY=0.0, dZ=0.0, bImprint=False, crlNode=[], crlFace=[])
```

Macro: {ref}`Macro-MeshEdit-MeshEditCreateNodeBetween3Nodes`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> Between3Nodes`

## Inputs

**`iNodeID`**
: An _Integer_ specifying the node ID. The default value is 0.

**`dX`**
: A _Double_ specifying the x. The default value is 0.0.

**`dY`**
: A _Double_ specifying the y. The default value is 0.0.

**`dZ`**
: A _Double_ specifying the z. The default value is 0.0.

**`bImprint`**
: A _Boolean_ specifying the imprint. The default value is False.

**`crlNode`**
: A _Cursor List_ specifying the node. The default value is [].

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.Between3Nodes(iNodeID=0, dX=0.0, dY=0.0, dZ=0.0, bImprint=False, crlNode=[], crlFace=[])
```
