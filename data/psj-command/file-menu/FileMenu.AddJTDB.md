```{module} FileMenu.AddJTDB()
:synopsis: add jtdb into model
```

(FileMenu.AddJTDB)=

# FileMenu.AddJTDB

## Description

add jtdb into model

## Syntax

```python
FileMenu.AddJTDB(strFileName, strMethod="AUTO", strTargetModel="IMPORTED", strOption="OFFSET", iInputNode=0, iInputElem=0, iInputPart=0, iInputMaterial=0, iInputProperty=0)
```

Macro: {ref}`Macro-FileMenu-AddJTDB`

Ribbon: {menuselection}`FileMenu --> AddJTDB`

## Inputs

**`strFileName`**
: A _String_ specifying the file name. This is a required input.

**`strMethod`**
: A _String_ specifying the method. The default value is "AUTO".

**`strTargetModel`**
: A _String_ specifying the target model. The default value is "IMPORTED".

**`strOption`**
: A _String_ specifying the option. The default value is "OFFSET".

**`iInputNode`**
: An _Integer_ specifying the input node. The default value is 0.

**`iInputElem`**
: An _Integer_ specifying the input element. The default value is 0.

**`iInputPart`**
: An _Integer_ specifying the input part. The default value is 0.

**`iInputMaterial`**
: An _Integer_ specifying the input material. The default value is 0.

**`iInputProperty`**
: An _Integer_ specifying the input property. The default value is 0.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
FileMenu.AddJTDB(strFileName, strMethod="AUTO", strTargetModel="IMPORTED", strOption="OFFSET", iInputNode=0, iInputElem=0, iInputPart=0, iInputMaterial=0, iInputProperty=0)
```
