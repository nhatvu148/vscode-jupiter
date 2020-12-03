```{module} Meshing.CADProjection.Part()
:synopsis: CadProject for Part
```

(Meshing.CADProjection.Part)=

# Meshing.CADProjection.Part

## Description

CadProject for Part

## Syntax

```python
Meshing.CADProjection.Part(iMethod=1, crCadPart=None, crMeshedPart=None, bForceProject=False, bProjectCornerNodes=True, bProjectMidNodes=False, bIDcheck=False)
```

Macro: {ref}`Macro-Meshing-CadProject_Part`

Ribbon: {menuselection}`Meshing --> CADProjection --> Part`

## Inputs

**`iMethod`**
: An _Integer_ specifying the method. The default value is 1.

**`crCadPart`**
: A _Cursor_ specifying the CAD part. The default value is None.

**`crMeshedPart`**
: A _Cursor_ specifying the meshed part. The default value is None.

**`bForceProject`**
: A _Boolean_ specifying the force project. The default value is False.

**`bProjectCornerNodes`**
: A _Boolean_ specifying the project corner nodes. The default value is True.

**`bProjectMidNodes`**
: A _Boolean_ specifying the project mid nodes. The default value is False.

**`bIDcheck`**
: A _Boolean_ specifying the i dcheck. The default value is False.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Meshing.CADProjection.Part(iMethod=1, crCadPart=None, crMeshedPart=None, bForceProject=False, bProjectCornerNodes=True, bProjectMidNodes=False, bIDcheck=False)
```
