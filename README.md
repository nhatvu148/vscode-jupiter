## Purpose

Add language support for PSJ (Python Script in Jupiter) and JPL (Jupiter Macro) to Visual Studio Code.

## Overview

**PSJ** (_Python Script in Jupiter_) is a set of Jupiter’s technologies enable user-customization for automation purpose.

When user executes an operation via Jupiter UI, a respective macro based on Python scripting language will be generated. User can use this macro for the same model, or implement advanced Python scripting for different models/specifications. In addition, a customized Python script language is also available for user to implement necessary UI to interact with end user when needed.

## Benefits

- **CAD designer** wants to do simple but repeated analysis using his/her design rule.

- **CAE engineer** wants to automate work, shorten modelling time, reduce workload and improve productivity.

- **CAE expert** with programming background wants to do advanced modelling, which required different software interaction, data read-in/written-out ability.

- **CAE company** with standard workflow wants to make its in-housed CAD-CAE automation system, from concept design to analysis report, through a Worksheet template or customized wizard. The company can build and maintain this system based on its own resource.

## Key features

User can operate Jupiter with Python and develop new functions using Jupiter.
The GUI Command Builder makes it easy to create a GUI without any knowledge of Python.
Besides, PSJ also has supporting tools such as “Customized IDE” and “Linkage between GUI and program”

## Note

- This extension uses [TabNine](https://tabnine.com/)'s binaries as a machine learning based autocompleter to provide responsive, reliable, and relevant suggestions.

- A note on licensing: this repo includes packaged Tabnine binaries. The MIT license only applies to the source code, not the packaged Tabnine binaries. The binaries are covered by the [Tabnine End User License Agreement](https://tabnine.com/eula).

- TabNine's local deep learning completion might be enabled by default. It is very CPU-intensive if your device can't handle it. You can check by typing "TabNine::config" in any buffer (your browser should then automatically open to TabNine's config page) and disable Deep TabNine Local (you will lose local deep learning completion).