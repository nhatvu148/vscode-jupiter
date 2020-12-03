```{module} Home.ToImage()
:synopsis: Unknown Description
```

(Home.ToImage)=

# Home.ToImage

## Description

Unknown Description

## Syntax

```python
Home.ToImage(strImgPath, bWhiteBG=False, bTransparentBG=False, bFixedSize=False, iExportWidth=1200, iExportHeight=900)
```

Macro: {ref}`Macro-Home-Capture_ToImageEx`

Ribbon: {menuselection}`Home --> ToImage`

## Inputs

**`strImgPath`**
: A _String_ specifying the image path. This is a required input.

**`bWhiteBG`**
: A _Boolean_ specifying the white back ground. The default value is False.

**`bTransparentBG`**
: A _Boolean_ specifying the transparent back ground. The default value is False.

**`bFixedSize`**
: A _Boolean_ specifying the fixed size. The default value is False.

**`iExportWidth`**
: An _Integer_ specifying the export width. The default value is 1200.

**`iExportHeight`**
: An _Integer_ specifying the export height. The default value is 900.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ToImage(strImgPath, bWhiteBG=False, bTransparentBG=False, bFixedSize=False, iExportWidth=1200, iExportHeight=900)
```
