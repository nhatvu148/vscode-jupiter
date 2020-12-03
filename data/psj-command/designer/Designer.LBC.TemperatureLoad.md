```{module} Designer.LBC.TemperatureLoad()
:synopsis: create temperature load Desiner
```

(Designer.LBC.TemperatureLoad)=

# Designer.LBC.TemperatureLoad

## Description

create temperature load Desiner

## Syntax

```python
Designer.LBC.TemperatureLoad(strName="", iDnType=0, dFTemp=0, strDstrFilePathName="", crDcrTable=None, crlTarget=[], crEdit=None, bDbUseAsMaterialReferenceTemp=False)
```

Macro: {ref}`Macro-Designer-TemperatureLoad`

Ribbon: {menuselection}`Designer --> LBC --> TemperatureLoad`

## Inputs

**`strName`**
: A _String_ specifying the name. The default value is "".

**`iDnType`**
: An _Integer_ specifying the dn type. The default value is 0.

**`dFTemp`**
: A _Double_ specifying the temperature. The default value is 0.

**`strDstrFilePathName`**
: A _String_ specifying the dstr file path name. The default value is "".

**`crDcrTable`**
: A _Cursor_ specifying the dcr table. The default value is None.

**`crlTarget`**
: A _Cursor List_ specifying the target. The default value is [].

**`crEdit`**
: A _Cursor_ specifying the edit. The default value is None.

**`bDbUseAsMaterialReferenceTemp`**
: A _Boolean_ specifying the db use as material reference temperature. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Designer.LBC.TemperatureLoad(strName="", iDnType=0, dFTemp=0, strDstrFilePathName="", crDcrTable=None, crlTarget=[], crEdit=None, bDbUseAsMaterialReferenceTemp=False)
```
