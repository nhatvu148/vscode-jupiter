# GetAllSelected

## Description

Get entity information from the selected entity (Connections, Contacts, Parts, ...)

## Syntax

GetAllSelected()

## Inputs

1. None

No input value

## Return Code

_Python Output_

- DItemVector

Entity information (name, type, typeID, id, info, key, masters, slaves, targets, children, parent )

## Sample Code

_Input:_

```python
sel = JPT.GetAllSelected()
for s in sel:
    print('name = "{}"'.format(s.name))
    print('type = {}'.format(s.type))
    print('typeID = {}'.format(s.typeID))
    print('info = {}'.format(s.info))
    print('key = {}'.format(s.key))
    for m in s.masters:
        print('masters ID = {}'.format(m.id))
    for s in s.slaves:
    print('slaves ID = {}'.format(s.id))
```

_Output:_

\> `name="MPC_3"`

\> `type=CONNECT_MPC`

\> `typeID=96`

\> `info={}`

\> `key=3`

\> `masters ID=20`

\> `slaves ID=44`
