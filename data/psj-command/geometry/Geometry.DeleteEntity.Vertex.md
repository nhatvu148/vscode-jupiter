```{module} Geometry.DeleteEntity.Vertex()
:synopsis: delete vertex
```

(Geometry.DeleteEntity.Vertex)=

# Geometry.DeleteEntity.Vertex

## Description

delete vertex

## Syntax

```python
Geometry.DeleteEntity.Vertex(crlVertex=[])
```

Macro: {ref}`Macro-Geometry-DeleteVertexCr`

Ribbon: {menuselection}`Geometry --> DeleteEntity --> Vertex`

## Inputs

**`crlVertex`**
: A _Cursor List_ specifying the vertex. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.DeleteEntity.Vertex(crlVertex=[])
```
