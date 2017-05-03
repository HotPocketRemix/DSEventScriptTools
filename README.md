# DSEventScriptTools
Editing tools and documentation files for the Dark Souls 1 event scripts.

For event script mod developers:
* [documentation](documentation) contains files useful when making mods, most importantly an unpacked version of `common.emedf` and its enums. For those interested in writing their own tools to deal with `.emevd` files, the file format specification sheet is also included here.

For event script mod developers & Dark Souls technical enthusiasts:
* [Unpacked Emevd](Unpacked%20Emevd) contains numerical and verbose unpacked versions of all the vanilla `.emevd` files in the game. These include the "dummy" area files `m##.emevd` which rarely contains any scripts and never run. The verbose versions are included so that those who do not wish to unpack the files themselves but still examine them may do so.
* [Unpacked Emeld](Unpacked%20Emeld) contains unpacked versions of the vanilla `.emeld` event description files. These files are not loaded by the vanilla game, but are useful for determining the purpose of existing events.

Usage Instructions:

A valid Python installation is needed to use these tools. I use Python 2.7, so some changes in Python 3 may break these.

* To unpack `.emeld` files (although I have put unpacked versions in [Unpacked Emeld](Unpacked%20Emeld)), download and use `unpack_eld.py`.
* To unpack, repack, and generate both numeric and verbose versions of `.emevd` files, download `emevd_handler.py`, `emevd_opener.py`, `emevd_rebuilder.py` and `evd_command_to_readable.py`. The main file is `emevd_rebuilder.py`; use `python emevd_rebuilder.py -h` for a short summary of the flags and arguments.
