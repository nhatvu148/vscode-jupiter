```{module} ACModeling.Create.Convex()
:synopsis: Create Convex In Boundary
```

(ACModeling.Create.Convex)=

# ACModeling.Create.Convex

## Description

Create Convex In Boundary

## Syntax

```python
ACModeling.Create.Convex(crlPart=[], dMeshSize=0.005, dOffset=0.02, dRadius=0.02, iDAxisGround=0, dScale=0.001)
```

Macro: {ref}`Macro-ACModeling-CreateConvex`

Ribbon: {menuselection}`ACModeling --> Create --> Convex`

## Inputs

**`crlPart`**
: A _Cursor List_ specifying the part. The default value is [].

**`dMeshSize`**
: A _Double_ specifying the mesh size. The default value is 0.005.

**`dOffset`**
: A _Double_ specifying the offset. The default value is 0.02.

**`dRadius`**
: A _Double_ specifying the radius. The default value is 0.02.

**`iDAxisGround`**
: An _Integer_ specifying the axis ground. The default value is 0.

**`dScale`**
: A _Double_ specifying the scale. The default value is 0.001.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
ACModeling.Create.Convex(crlPart=[], dMeshSize=0.005, dOffset=0.02, dRadius=0.02, iDAxisGround=0, dScale=0.001)
```
