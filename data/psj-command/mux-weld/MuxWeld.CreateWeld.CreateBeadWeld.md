```{module} MuxWeld.CreateWeld.CreateBeadWeld()
:synopsis: Unknown Description
```

(MuxWeld.CreateWeld.CreateBeadWeld)=

# MuxWeld.CreateWeld.CreateBeadWeld

## Description

Unknown Description

## Syntax

```python
MuxWeld.CreateWeld.CreateBeadWeld(crlEdge, crlPrjtedEdge, crlPart, dTol, dRatio, crRefElem)
```

Macro: {ref}`Macro-MuxWeld-CreateBeadWeld`

Ribbon: {menuselection}`MuxWeld --> CreateWeld --> CreateBeadWeld`

## Inputs

**`crlEdge`**
: A _Cursor List_ specifying the edge. This is a required input.

**`crlPrjtedEdge`**
: A _Cursor List_ specifying the projected edge. This is a required input.

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`dTol`**
: A _Double_ specifying the tolerance. This is a required input.

**`dRatio`**
: A _Double_ specifying the ratio. This is a required input.

**`crRefElem`**
: A _Cursor_ specifying the reference element. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MuxWeld.CreateWeld.CreateBeadWeld(crlEdge, crlPrjtedEdge, crlPart, dTol, dRatio, crRefElem)
```
