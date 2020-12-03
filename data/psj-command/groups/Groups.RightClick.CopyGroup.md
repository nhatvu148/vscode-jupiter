```{module} Groups.RightClick.CopyGroup()
:synopsis: Copy Group
```

(Groups.RightClick.CopyGroup)=

# Groups.RightClick.CopyGroup

## Description

Copy Group

## Syntax

```python
Groups.RightClick.CopyGroup(crlSrc=[], strlNames=[], crDest=None, bKeep=0)
```

Macro: {ref}`Macro-Groups-CopyGroup`

Ribbon: {menuselection}`Groups --> RightClick --> CopyGroup`

## Inputs

**`crlSrc`**
: A _Cursor List_ specifying the source. The default value is [].

**`strlNames`**
: A _String List_ specifying the names. The default value is [].

**`crDest`**
: A _Cursor_ specifying the dest. The default value is None.

**`bKeep`**
: A _Boolean_ specifying the keep. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Groups.RightClick.CopyGroup(crlSrc=[], strlNames=[], crDest=None, bKeep=0)
```
