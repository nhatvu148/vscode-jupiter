```{module} Connections.Pretension.General()
:synopsis: Pretension general
```

(Connections.Pretension.General)=

# Connections.Pretension.General

## Description

Pretension general

## Syntax

```python
Connections.Pretension.General(strName="BoltLoad001", iDir=0, dValue=DFLT_DBL, bFixLength=False, crTable=None, crCoord=None, iLocalUnit=0, crlTarget=[], crEdit=None, bCreate2ADVCStatic=False)
```

Macro: {ref}`Macro-Connections-Pretension`

Ribbon: {menuselection}`Connections --> Pretension --> General`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "BoltLoad001".

**`iDir`**
: An _Integer_ specifying the direction. The default value is 0.

**`dValue`**
: A _Double_ specifying the value. The default value is DFLT_DBL.

**`bFixLength`**
: A _Boolean_ specifying the fix length. The default value is False.

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`crCoord`**
: A _Cursor_ specifying the coordinate. The default value is None.

**`iLocalUnit`**
: An _Integer_ specifying the local unit. The default value is 0.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`bCreate2ADVCStatic`**
: A _Boolean_ specifying the create2 ADVC static. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Pretension.General(strName="BoltLoad001", iDir=0, dValue=DFLT_DBL, bFixLength=False, crTable=None, crCoord=None, iLocalUnit=0, crlTarget=[], crEdit=None, bCreate2ADVCStatic=False)
```
