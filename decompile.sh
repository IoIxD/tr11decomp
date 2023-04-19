rm decompiled/TuxRacer11Decomp.rep
/opt/ghidra/support/analyzeHeadless decompiled TuxRacer11Decomp -import $(pwd)/source/tuxracer-bin -postscript decompile.py -max-cpu $(nproc)