```{module} MufflerHA.CreateEdgeClassic.ProjectLine()
:synopsis: create edge
```

(MufflerHA.CreateEdgeClassic.ProjectLine)=

# MufflerHA.CreateEdgeClassic.ProjectLine

## Description

create edge

## Syntax

```python
MufflerHA.CreateEdgeClassic.ProjectLine(ilAiedgeidForMacro, ilAifaceidForMacro, bDivideFace, crlAiparttargetForMarco)
```

Macro: {ref}`Macro-MufflerHA-Imprint_ProjectionLine`

Ribbon: {menuselection}`MufflerHA --> CreateEdgeClassic --> ProjectLine`

## Inputs

**`ilAiedgeidForMacro`**
: A _Integer List_ specifying the aiedgeid for macro. This is a required input.

**`ilAifaceidForMacro`**
: A _Integer List_ specifying the aifaceid for macro. This is a required input.

**`bDivideFace`**
: A _Boolean_ specifying the divide face. This is a required input.

**`crlAiparttargetForMarco`**
: A _Cursor List_ specifying the part target for marco. This is a required input.

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
MufflerHA.CreateEdgeClassic.ProjectLine(ilAiedgeidForMacro, ilAifaceidForMacro, bDivideFace, crlAiparttargetForMarco)
```
