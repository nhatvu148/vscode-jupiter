```{module} MeshEdit.RefineQuality()
:synopsis: Unknown Description
```

(MeshEdit.RefineQuality)=

# MeshEdit.RefineQuality

## Description

Unknown Description

## Syntax

```python
MeshEdit.RefineQuality(iMetric, crlFace, crlElem, crlNode)
```

Macro: {ref}`Macro-MeshEdit-MeshEdit_RefineQuality`

Ribbon: {menuselection}`MeshEdit --> RefineQuality`

## Inputs

**`iMetric`**
: An _Integer_ specifying the metric. This is a required input.

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`crlElem`**
: A _Cursor List_ specifying the element. This is a required input.

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MeshEdit.RefineQuality(iMetric, crlFace, crlElem, crlNode)
```
