```{module} Geometry.Bar.TwoNodes()
:synopsis: Create Bar Body
```

(Geometry.Bar.TwoNodes)=

# Geometry.Bar.TwoNodes

## Description

Create Bar Body

## Syntax

```python
Geometry.Bar.TwoNodes(strPartName="Bar_1", iMeshCount=5, crStartNode=None, crEndNode=None)
```

Macro: {ref}`Macro-Geometry-CreateBar`

Ribbon: {menuselection}`Geometry --> Bar --> TwoNodes`

## Inputs

**`strPartName`**
: A _String_ specifying the part name. The default value is "Bar_1".

**`iMeshCount`**
: An _Integer_ specifying the mesh count. The default value is 5.

**`crStartNode`**
: A _Cursor_ specifying the start node. The default value is None.

**`crEndNode`**
: A _Cursor_ specifying the end node. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Bar.TwoNodes(strPartName="Bar_1", iMeshCount=5, crStartNode=None, crEndNode=None)
```
