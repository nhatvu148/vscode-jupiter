```{module} Home.Find()
:synopsis: Unknown Description
```

(Home.Find)=

# Home.Find

## Description

Unknown Description

## Syntax

```python
Home.Find(strSearch="", strSeletedType="Part", bFindMatch=False)
```

Macro: {ref}`Macro-Home-ViewFindEntities`

Ribbon: {menuselection}`Home --> Find`

## Inputs

**`strSearch`**
: A _String_ specifying the search. The default value is "".

**`strSeletedType`**
: A _String_ specifying the seleted type. The default value is "Part".

**`bFindMatch`**
: A _Boolean_ specifying the find match. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.Find(strSearch="", strSeletedType="Part", bFindMatch=False)
```
