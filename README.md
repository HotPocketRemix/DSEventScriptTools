# DSEventScriptTools
Editing tools and documentation files for FROM Software event scripts.
Supported games are Dark Souls 1 PTDE, Dark Souls 1: Remastered, Bloodborne, and Dark Souls 3.

For event script mod developers:
* [EventScriptResources](EventScriptResources) contains JSON versions of `common.emedf`, either based on an extant file (for DS1, DS1R and BB) or manually re-created (DS3). Also contains an easier-to-read text version, generated using the tool's `-j` flag.
* [documentation](documentation) contains format specifications for the ELD, EVD and EDF formats.

For event script mod developers & Dark Souls technical enthusiasts:
* [Unpacked Emevd](Unpacked%20Emevd) contains numerical and verbose unpacked versions of all the vanilla DS1PTDE `.emevd` files. These include the "dummy" area files `m##.emevd` which rarely contains any scripts and never run. The verbose versions are included so that those who do not wish to unpack the files themselves but still examine them may do so.
* [Unpacked Emeld](Unpacked%20Emeld) contains unpacked versions of the vanilla DS1PTDE `.emeld` event description files. These files are not loaded by the vanilla game, but are useful for determining the purpose of existing events.

Usage Instructions:

A valid Python 3 installation is needed to use these scripts directly. However, a PyInstaller .exe version of the emevd unpacker/repacker and the emeld unpacker/repacker is provided for standalone use.
Both the .py and .exe versions of `EventScriptTool` require the EventScriptResources directory so that they can read the JSON versions of the emedf file.

* To unpack `.emeld` files (although I have put unpacked versions in [Unpacked Emeld](Unpacked%20Emeld)), download and use `EventNameTool.exe` in a command line..
* To unpack, repack, and generate both numeric and verbose versions of `.emevd` files, download and use `EventScriptTool.exe` in a command line.
* For both of these, use the `-h` flag for a short summary of the flags and arguments.

If you are not on Windows, the entry point for `EventNameTool.exe` is `unpack_eld.py` and the entry point for `EventScriptTool.exe` is `emevd_rebuilder.py`.


Thanks to AinTunez, Elissa, Lance, Meowmaritus, Pavuk, TKGP, and others for suggestions, testing and developement help.
