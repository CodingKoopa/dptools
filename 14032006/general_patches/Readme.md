# General Patches
This directory contains general patches for building and using the prototype.
- `0001-Remove-broken-backslashes.patch`: Removes backslashes which break the build process. These bashslashes are used to escape the newline, making make think that there is more to the list, when there isn't. This fixes the issue of `No rule to make '` (with a newline).