```{module} MuxWeld.Prop3DWeldBead()
:synopsis: create Property 3D Weld Bead
```

(MuxWeld.Prop3DWeldBead)=

# MuxWeld.Prop3DWeldBead

## Description

create Property 3D Weld Bead

## Syntax

```python
MuxWeld.Prop3DWeldBead(strName="Bead_1", crMaterial=None, crlTarget=[], crEdit=None)
```

Macro: {ref}`Macro-MuxWeld-Prop3DWeldBead`

Ribbon: {menuselection}`MuxWeld --> Prop3DWeldBead`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "Bead_1".

**`crMaterial`**
: A _Cursor_ specifying the material. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MuxWeld.Prop3DWeldBead(strName="Bead_1", crMaterial=None, crlTarget=[], crEdit=None)
```
