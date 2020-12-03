```{module} Geometry.DeleteEntity.Edge()
:synopsis: Delete Edge
```

(Geometry.DeleteEntity.Edge)=

# Geometry.DeleteEntity.Edge

## Description

Delete Edge

## Syntax

```python
Geometry.DeleteEntity.Edge(crlEdge=[])
```

Macro: {ref}`Macro-Geometry-DeleteEdgeCr`

Ribbon: {menuselection}`Geometry --> DeleteEntity --> Edge`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.DeleteEntity.Edge(crlEdge=[])
```
