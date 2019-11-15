#!/bin/sh

# TODO - test if emcc, if not activate

# traditional compile
# emcc core.cpp -s WASM=1 -s USE_SDL=2 -O3 -o index.js

# export set_note_played() function
emcc core.cpp -s WASM=1 -s USE_SDL=2 -O3 -o index.js -s EXPORTED_FUNCTIONS='["_main", "_set_note_played"]' -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]'
