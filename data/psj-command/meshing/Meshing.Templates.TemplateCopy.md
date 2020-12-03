```{module} Meshing.Templates.TemplateCopy()
:synopsis: Template Copy local setting
```

(Meshing.Templates.TemplateCopy)=

# Meshing.Templates.TemplateCopy

## Description

Template Copy local setting

## Syntax

```python
Meshing.Templates.TemplateCopy(crlReferent=[], crlTarget=[], iMethod=0, iCopySub=1, dTolerance=0.001, strSource="", strTarget="")
```

Macro: {ref}`Macro-Meshing-TemplateCopy`

Ribbon: {menuselection}`Meshing --> Templates --> TemplateCopy`

## Inputs

**`crlReferent`**
: A _Cursor List_ specifying the reference. The default value is [].

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`iMethod`**
: An _Integer_ specifying the method. The default value is 0.

**`iCopySub`**
: An _Integer_ specifying the copy sub. The default value is 1.

**`dTolerance`**
: A _Double_ specifying the tolerance. The default value is 0.001.

**`strSource`**
: A _String_ specifying the source. The default value is "".

**`strTarget`**
: A _String_ specifying the target. The default value is "".

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.Templates.TemplateCopy(crlReferent=[], crlTarget=[], iMethod=0, iCopySub=1, dTolerance=0.001, strSource="", strTarget="")
```
