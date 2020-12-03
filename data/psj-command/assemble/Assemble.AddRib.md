```{module} Assemble.AddRib()
:synopsis: create Rib
```

(Assemble.AddRib)=

# Assemble.AddRib

## Description

create Rib

## Syntax

```python
Assemble.AddRib(crPart=None, crlFace=[], veclPoints=[], dWidth=0.0, dDepth=0.0)
```

Macro: {ref}`Macro-Assemble-AddRib`

Ribbon: {menuselection}`Assemble --> AddRib`

## Inputs

**`crPart`**
: A _Cursor_ specifying the part. The default value is None.

**`crlFace`**
: A _Cursor List_ specifying the face. The default value is [].

**`veclPoints`**
: A _Vector List_ specifying the points. The default value is [].

**`dWidth`**
: A _Double_ specifying the width. The default value is 0.0.

**`dDepth`**
: A _Double_ specifying the depth. The default value is 0.0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assemble.AddRib(crPart=None, crlFace=[], veclPoints=[], dWidth=0.0, dDepth=0.0)
```
