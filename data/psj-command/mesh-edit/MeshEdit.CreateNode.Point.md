```{module} MeshEdit.CreateNode.Point()
:synopsis: create node point
```

(MeshEdit.CreateNode.Point)=

# MeshEdit.CreateNode.Point

## Description

create node point

## Syntax

```python
MeshEdit.CreateNode.Point(iNodeID=1, posPoint=[0,0,0], bImprint=True, crShape=None)
```

Macro: {ref}`Macro-MeshEdit-MeshEditCreateNodePoint`

Ribbon: {menuselection}`MeshEdit --> CreateNode --> Point`

## Inputs

**`iNodeID`**
: An _Integer_ specifying the node ID. The default value is 1.

**`posPoint`**
: A _Position_ specifying the point. The default value is [0,0,0].

**`bImprint`**
: A _Boolean_ specifying the imprint. The default value is True.

**`crShape`**
: A _Cursor_ specifying the shape. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.CreateNode.Point(iNodeID=1, posPoint=[0,0,0], bImprint=True, crShape=None)
```
