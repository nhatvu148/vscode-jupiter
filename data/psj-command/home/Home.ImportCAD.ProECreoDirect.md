```{module} Home.ImportCAD.ProECreoDirect()
:synopsis: import Creo by Direct
```

(Home.ImportCAD.ProECreoDirect)=

# Home.ImportCAD.ProECreoDirect

## Description

import Creo by Direct

## Syntax

```python
Home.ImportCAD.ProECreoDirect(strlPath, dChordHeightTolerance=0.0, dAngleToleranceDegree=20.0, dStepMaxSize=0.1)
```

Macro: {ref}`Macro-Home-ImportCreo`

Ribbon: {menuselection}`Home --> ImportCAD --> ProECreoDirect`

## Inputs

**`strlPath`**
: A _String List_ specifying the path. This is a required input.

**`dChordHeightTolerance`**
: A _Double_ specifying the chord height tolerance. The default value is 0.0.

**`dAngleToleranceDegree`**
: A _Double_ specifying the angle tolerance degree. The default value is 20.0.

**`dStepMaxSize`**
: A _Double_ specifying the step maximum size. The default value is 0.1.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Home.ImportCAD.ProECreoDirect(strlPath, dChordHeightTolerance=0.0, dAngleToleranceDegree=20.0, dStepMaxSize=0.1)
```
