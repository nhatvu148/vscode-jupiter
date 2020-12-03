# GetAllLoadsBCs

## Description

Get information of all loads and BCs

## Syntax

GetAllLoadsBCs()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- DItemVector

Load information (type, type ID, id, key, name, info, targets, isValid, masters, slaves, parent, children)

## Sample Code

_Input:_

```python
lbc= JPT.GetAllLoadsBCs()
for bc in lbc:
    for e in g.targets:
            print('type="{0}", typeID="{1}", name="{2}", id="{3}", key="{4}", info="{5}", isValid="{6}"'.format(bc.type, bc.typeID, bc.name, bc.id, bc.key, bc.info, bc.isValid))
```

_Output:_

\> `type="LBC_CONSTRAINT", typeID="37", name="Constraint1", id="1", key="1", info="{}", isValid="True"`

\> `type="LBC_G\_PRESSURE", typeID="40", name="Pressure1", id="1", key="1", info="{}", isValid="True"`
