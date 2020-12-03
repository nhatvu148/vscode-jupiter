```{module} Geometry.Part.Elems()
:synopsis: create part from element
```

(Geometry.Part.Elems)=

# Geometry.Part.Elems

## Description

create part from element

## Syntax

```python
Geometry.Part.Elems(crlElem, strPartName)
```

Macro: {ref}`Macro-Geometry-CreatePartFromElems`

Ribbon: {menuselection}`Geometry --> Part --> Elems`

## Inputs

**`crlElem`**
: A _Cursor List_ specifying the element. This is a required input.

**`strPartName`**
: A _String_ specifying the part name. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Geometry.Part.Elems(crlElem, strPartName)
```
