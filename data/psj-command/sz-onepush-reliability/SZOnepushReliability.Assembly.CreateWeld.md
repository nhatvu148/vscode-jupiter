```{module} SZOnepushReliability.Assembly.CreateWeld()
:synopsis: Create welding
```

(SZOnepushReliability.Assembly.CreateWeld)=

# SZOnepushReliability.Assembly.CreateWeld

## Description

Create welding

## Syntax

```python
SZOnepushReliability.Assembly.CreateWeld(crlWelds, dMeshSize, iRrate, dFilletRadius)
```

Macro: {ref}`Macro-SZOnepushReliability-SORCreateWeld`

Ribbon: {menuselection}`SZOnepushReliability --> Assembly --> CreateWeld`

## Inputs

**`crlWelds`**
: A _Cursor List_ specifying the welds. This is a required input.

**`dMeshSize`**
: A _Double_ specifying the mesh size. This is a required input.

**`iRrate`**
: An _Integer_ specifying the rrate. This is a required input.

**`dFilletRadius`**
: A _Double_ specifying the fillet radius. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
SZOnepushReliability.Assembly.CreateWeld(crlWelds, dMeshSize, iRrate, dFilletRadius)
```
