```{module} MufflerHA.CreateEdge.PerpendicularLineToEdge()
:synopsis: Unknown Description
```

(MufflerHA.CreateEdge.PerpendicularLineToEdge)=

# MufflerHA.CreateEdge.PerpendicularLineToEdge

## Description

Unknown Description

## Syntax

```python
MufflerHA.CreateEdge.PerpendicularLineToEdge(crNode, crEdge, crlFace, bBreakFace)
```

Macro: {ref}`Macro-MufflerHA-ImprintPerpendicularLine2`

Ribbon: {menuselection}`MufflerHA --> CreateEdge --> PerpendicularLineToEdge`

## Inputs

**`crNode`**
: A _Cursor_ specifying the node. This is a required input.

**`crEdge`**
: A _Cursor_ specifying the edge. This is a required input.

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`bBreakFace`**
: A _Boolean_ specifying the break face. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MufflerHA.CreateEdge.PerpendicularLineToEdge(crNode, crEdge, crlFace, bBreakFace)
```
