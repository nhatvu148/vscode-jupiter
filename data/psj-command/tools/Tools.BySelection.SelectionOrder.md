```{module} Tools.BySelection.SelectionOrder()
:synopsis: Renumber by selection order
```

(Tools.BySelection.SelectionOrder)=

# Tools.BySelection.SelectionOrder

## Description

Renumber by selection order

## Syntax

```python
Tools.BySelection.SelectionOrder(crlTarget=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True)
```

Macro: {ref}`Macro-Tools-RenumberSpecify`

Ribbon: {menuselection}`Tools --> BySelection --> SelectionOrder`

## Inputs

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iStartID`**
: An _Integer_ specifying the start ID. The default value is 1.

**`iIncrementStep`**
: An _Integer_ specifying the increment step. The default value is 1.

**`bAscending`**
: A _Boolean_ specifying the ascending. The default value is True.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.BySelection.SelectionOrder(crlTarget=[], iType=0, iMethod=0, iStartID=1, iIncrementStep=1, bAscending=True)
```
