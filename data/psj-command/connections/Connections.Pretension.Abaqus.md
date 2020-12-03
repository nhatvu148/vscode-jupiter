```{module} Connections.Pretension.Abaqus()
:synopsis: Create Pretension Abaqus
```

(Connections.Pretension.Abaqus)=

# Connections.Pretension.Abaqus

## Description

Create Pretension Abaqus

## Syntax

```python
Connections.Pretension.Abaqus(strName="PreTensionAbaqus1", bFixedLenght=False, crTable=None, dValue=DFLT_DBL, iLocalUnit=0, strNormal="", dlNodePos=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crEdit=None, crlTarget=[])
```

Macro: {ref}`Macro-Connections-PretensionAbaqus`

Ribbon: {menuselection}`Connections --> Pretension --> Abaqus`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "PreTensionAbaqus1".

**`bFixedLenght`**
: A _Boolean_ specifying the fixed length. The default value is False.

**`crTable`**
: A _Cursor_ specifying the table. The default value is None.

**`dValue`**
: A _Double_ specifying the value. The default value is DFLT_DBL.

**`iLocalUnit`**
: An _Integer_ specifying the local unit. The default value is 0.

**`strNormal`**
: A _String_ specifying the normal. The default value is "".

**`dlNodePos`**
: A _Double List_ specifying the node position. The default value is [DFLT_DBL,DFLT_DBL,DFLT_DBL].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Pretension.Abaqus(strName="PreTensionAbaqus1", bFixedLenght=False, crTable=None, dValue=DFLT_DBL, iLocalUnit=0, strNormal="", dlNodePos=[DFLT_DBL,DFLT_DBL,DFLT_DBL], crEdit=None, crlTarget=[])
```
