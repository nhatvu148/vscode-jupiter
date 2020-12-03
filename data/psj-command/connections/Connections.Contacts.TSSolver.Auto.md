```{module} Connections.Contacts.TSSolver.Auto()
:synopsis: find contact
```

(Connections.Contacts.TSSolver.Auto)=

# Connections.Contacts.TSSolver.Auto

## Description

find contact

## Syntax

```python
Connections.Contacts.TSSolver.Auto(strlNames, crllMasterFaceTargets, crllSlaveFaceTargets, crlContactTypes=[1], dlInterferenceClosures=[1.0], dlFrictionCoefficients=[DFLT_DBL], blInitialAdjustments=[False], crlColors=[65280], crlEdit=[], crlMasterGroup=[], crlSlaveGroup=[])
```

Macro: {ref}`Macro-Connections-FindContact`

Ribbon: {menuselection}`Connections --> Contacts --> TSSolver --> Auto`

## Inputs

**`strlNames`**
: A _String List_ specifying the names. This is a required input.

**`crllMasterFaceTargets`**
: A _Cursor List List_ specifying the master face targets. This is a required input.

**`crllSlaveFaceTargets`**
: A _Cursor List List_ specifying the slave face targets. This is a required input.

**`crlContactTypes`**
: A _Cursor List_ specifying the contact types. The default value is [1].

**`dlInterferenceClosures`**
: A _Double List_ specifying the interference closures. The default value is [1.0].

**`dlFrictionCoefficients`**
: A _Double List_ specifying the friction coefficients. The default value is [DFLT_DBL].

**`blInitialAdjustments`**
: A _Boolean List_ specifying the initial adjustments. The default value is [False].

**`crlColors`**
: A _Cursor List_ specifying the colors. The default value is [65280].

**`crlEdit`**
: A _Cursor List_ specifying the edit. The default value is [].

**`crlMasterGroup`**
: A _Cursor List_ specifying the master group. The default value is [].

**`crlSlaveGroup`**
: A _Cursor List_ specifying the slave group. The default value is [].

## Return Code

An _String_ of 1 if successed, or 0 if failed.

## Sample Code

```python
Connections.Contacts.TSSolver.Auto(strlNames, crllMasterFaceTargets, crllSlaveFaceTargets, crlContactTypes=[1], dlInterferenceClosures=[1.0], dlFrictionCoefficients=[DFLT_DBL], blInitialAdjustments=[False], crlColors=[65280], crlEdit=[], crlMasterGroup=[], crlSlaveGroup=[])
```
