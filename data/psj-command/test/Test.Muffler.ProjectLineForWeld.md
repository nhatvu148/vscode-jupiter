```{module} Test.Muffler.ProjectLineForWeld()
:synopsis: Projec line for weld
```

(Test.Muffler.ProjectLineForWeld)=

# Test.Muffler.ProjectLineForWeld

## Description

Projec line for weld

## Syntax

```python
Test.Muffler.ProjectLineForWeld(crlEdge, crlFace)
```

Macro: {ref}`Macro-Test-WeldingEdgeHGA`

Ribbon: {menuselection}`Test --> Muffler --> ProjectLineForWeld`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Test.Muffler.ProjectLineForWeld(crlEdge, crlFace)
```
