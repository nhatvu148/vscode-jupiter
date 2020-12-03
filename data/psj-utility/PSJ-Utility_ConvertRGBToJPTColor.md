# ConvertRGBToJPTColor

## Description

Convert a RGB (red,green,blue) value to JPT color number

## Inputs

1.  RGB (red,green,blue)

## Return Code

JPT color number (int)

## Sample Code

```python
newcolor = JPT.ConvertRGBToJPTColor(RGB(255,0,0)) # red color
listbody = JPT.GetEntitiesByName(JPT.DTableType.DTABLE_BODY, "Cube_1", 1)
listbody[0].color = newcolor
```
