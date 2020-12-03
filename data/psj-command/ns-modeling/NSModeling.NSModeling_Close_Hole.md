```{module} NSModeling.NSModeling_Close_Hole()
:synopsis: NSModeling NSModeling_Close_Hole
```

(NSModeling.NSModeling_Close_Hole)=

# NSModeling.NSModeling_Close_Hole

## Description

NSModeling NSModeling_Close_Hole

## Syntax

```python
NSModeling.NSModeling_Close_Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNode, crlPart)
```

Macro: {ref}`Macro-NSModeling-NSModeling_Close_Hole`

Ribbon: {menuselection}`NSModeling --> NSModeling_Close_Hole`

## Inputs

**`iType`**
: An _Integer_ specifying the type. This is a required input.

**`dMaxLength`**
: A _Double_ specifying the maximum length. This is a required input.

**`bMergeFaces`**
: A _Boolean_ specifying the merge faces. This is a required input.

**`bSetCenterPoint`**
: A _Boolean_ specifying the set center point. This is a required input.

**`crlNode`**
: A _Cursor List_ specifying the node. This is a required input.

**`crlPart`**
: A _Cursor List_ specifying the part. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
NSModeling.NSModeling_Close_Hole(iType, dMaxLength, bMergeFaces, bSetCenterPoint, crlNode, crlPart)
```
