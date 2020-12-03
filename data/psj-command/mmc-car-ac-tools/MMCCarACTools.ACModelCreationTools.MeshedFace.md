```{module} MMCCarACTools.ACModelCreationTools.MeshedFace()
:synopsis:
```

(MMCCarACTools.ACModelCreationTools.MeshedFace)=

# MMCCarACTools.ACModelCreationTools.MeshedFace

## Description

## Syntax

```python
MMCCarACTools.ACModelCreationTools.MeshedFace(crlItem1, crlItem2, crlItem3, crlPart, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
```

Macro: {ref}`Macro-MMCCarACTools-MMCMeshedFace`

Ribbon: {menuselection}`MMCCarACTools --> ACModelCreationTools --> MeshedFace`

## Inputs

**`crlItem1`**
: A _Cursor List_ specifying the item1. This is a required input.

**`crlItem2`**
: A _Cursor List_ specifying the item2. This is a required input.

**`crlItem3`**
: A _Cursor List_ specifying the item3. This is a required input.

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

**`iType`**
: An _Integer_ specifying the type. This is a required input.

**`dMeshSise`**
: A _Double_ specifying the mesh sise. This is a required input.

**`bMergeTol`**
: A _Boolean_ specifying the merge tolerance. This is a required input.

**`dTol`**
: A _Double_ specifying the tolerance. This is a required input.

**`bCreatePart`**
: A _Boolean_ specifying the create part. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MMCCarACTools.ACModelCreationTools.MeshedFace(crlItem1, crlItem2, crlItem3, crlPart, iType, dMeshSise, bMergeTol, dTol, bCreatePart)
```
