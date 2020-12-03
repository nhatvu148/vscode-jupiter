```{module} Tools.ElementCS()
:synopsis: create element coordinate system
```

(Tools.ElementCS)=

# Tools.ElementCS

## Description

create element coordinate system

## Syntax

```python
Tools.ElementCS(iMethod=0, iDispType=0, bDispXDir=False, bDispCoord=False, dDispScale=1, crlTarget=[])
```

Macro: {ref}`Macro-Tools-ModifyElemDir`

Ribbon: {menuselection}`Tools --> ElementCS`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iDispType`**
: An _Integer_ specifying the displacement type. The default value is 0.

**`bDispXDir`**
: A _Boolean_ specifying the displacement x direction. The default value is False.

**`bDispCoord`**
: A _Boolean_ specifying the displacement coordinate. The default value is False.

**`dDispScale`**
: A _Double_ specifying the displacement scale. The default value is 1.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Tools.ElementCS(iMethod=0, iDispType=0, bDispXDir=False, bDispCoord=False, dDispScale=1, crlTarget=[])
```
