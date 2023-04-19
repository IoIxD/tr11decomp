Project for decompiling Tux Racer 1.1 and allowing it to be ported to other consoles and modern OSes.

# How to contribute

Before contributing it should be noted that **everything in the `decompiled` and `source` folders to not get pushed to the repo.** These are for local work only! To actually contribute to the repo, you must edit files in the `patches` folder according to the instructions in the README in ther.

1. Get Ghidra. The decompiler .sh file assumes that the ghidra files are in `/opt/ghidra`; there is currently no script for Windows users.
2. Extract the contents of the Tux Racer 1.1 iso somewhere, and pout `program files/Sunspire Studios/Tux Racer/bin/x86/glibc-2.1/tuxracer-bin` into the `source` folder. No other file matters.
3. Run `decompile.sh`.
4. Wait until I find out how files will be modified without ghidra itself.