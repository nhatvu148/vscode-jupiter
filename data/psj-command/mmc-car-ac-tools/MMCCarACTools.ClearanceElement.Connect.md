```{module} MMCCarACTools.ClearanceElement.Connect()
:synopsis: MMCCarACTools ClearanceElement Connect
```

(MMCCarACTools.ClearanceElement.Connect)=

# MMCCarACTools.ClearanceElement.Connect

## Description

MMCCarACTools ClearanceElement Connect

## Syntax

```python
MMCCarACTools.ClearanceElement.Connect(crlFace, crlElem, iConnectionMethod)
```

Macro: {ref}`Macro-MMCCarACTools-MMC_CONNECTION_CLEARANCE_ELEMENT`

Ribbon: {menuselection}`MMCCarACTools --> ClearanceElement --> Connect`

## Inputs

**`crlFace`**
: A _Cursor List_ specifying the face. This is a required input.

**`crlElem`**
: A _Cursor List_ specifying the element. This is a required input.

**`iConnectionMethod`**
: An _Integer_ specifying the connection method. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MMCCarACTools.ClearanceElement.Connect(crlFace, crlElem, iConnectionMethod)
```
