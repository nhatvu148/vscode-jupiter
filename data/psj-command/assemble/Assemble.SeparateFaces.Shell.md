```{module} Assemble.SeparateFaces.Shell()
:synopsis: Separate Faces for Shell
```

(Assemble.SeparateFaces.Shell)=

# Assemble.SeparateFaces.Shell

## Description

Separate Faces for Shell

## Syntax

```python
Assemble.SeparateFaces.Shell(iType=0, crlEntity=[], bCreateGroup=False)
```

Macro: {ref}`Macro-Assemble-ASMSeparateShellCr`

Ribbon: {menuselection}`Assemble --> SeparateFaces --> Shell`

## Inputs

**`iType`**
: An _Integer_ specifying the type. The default value is 0.

**`crlEntity`**
: A _Cursor List_ specifying the entity. The default value is [].

**`bCreateGroup`**
: A _Boolean_ specifying the create group. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Assemble.SeparateFaces.Shell(iType=0, crlEntity=[], bCreateGroup=False)
```
