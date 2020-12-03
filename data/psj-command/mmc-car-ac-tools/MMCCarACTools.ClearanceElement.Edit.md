```{module} MMCCarACTools.ClearanceElement.Edit()
:synopsis: Edit clearance elment
```

(MMCCarACTools.ClearanceElement.Edit)=

# MMCCarACTools.ClearanceElement.Edit

## Description

Edit clearance elment

## Syntax

```python
MMCCarACTools.ClearanceElement.Edit(dDx, dDy, dDz, dLx, dLy, dLz, crlTarget, crlDestNode, poslDestPoint)
```

Macro: {ref}`Macro-MMCCarACTools-MMC_EDIT_CLEARANCE_ELEMENT`

Ribbon: {menuselection}`MMCCarACTools --> ClearanceElement --> Edit`

## Inputs

**`dDx`**
: A _Double_ specifying the dx. This is a required input.

**`dDy`**
: A _Double_ specifying the dy. This is a required input.

**`dDz`**
: A _Double_ specifying the dz. This is a required input.

**`dLx`**
: A _Double_ specifying the lx. This is a required input.

**`dLy`**
: A _Double_ specifying the ly. This is a required input.

**`dLz`**
: A _Double_ specifying the lz. This is a required input.

**`crlTarget`**
: A _Cursor List_ specifying the target. This is a required input.

**`crlDestNode`**
: A _Cursor List_ specifying the dest node. This is a required input.

**`poslDestPoint`**
: A _Position List_ specifying the dest point. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MMCCarACTools.ClearanceElement.Edit(dDx, dDy, dDz, dLx, dLy, dLz, crlTarget, crlDestNode, poslDestPoint)
```
