rm project/decompiled/*.c
rm project/decompiled/*.h
python -m ghidrecomp \
    --project-path project/ghidra \
    --output-path project/decompiled \
    --symbols-path project/symbols \
    ./source/tuxracer-bin