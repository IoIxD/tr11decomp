#!/usr/bin/python
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.program.flatapi import FlatProgramAPI

# get the current program
# here currentProgram is predefined

program = currentProgram
decompinterface = DecompInterface()
decompinterface.openProgram(program)
functions = program.getFunctionManager().getFunctions(True)

for function in list(functions):
    fnname = str(function)
    if fnname.startswith("<EXTERNAL>"):
        continue
    f = open("decompiled/"+fnname+".c", "w")
    # decompile each function
    tokengrp = decompinterface.decompileFunction(
        function, 0, ConsoleTaskMonitor())
    f.write(tokengrp.getDecompiledFunction().getC())
    f.close()
