# RLE Image Encoder

What it is: Run-length encoding toolkit with a menu-driven CLI. Supports loading sample/flat/hex data, converting between raw pixels, RLE, and hex, and rendering images in the console.

Key files:
- `P2_A.py` – Menu + basic load/display.
- `P2_B.py` – Core encode/decode and hex helpers.
- `P2_C.py` – Full integration of menu + encode/decode/formatting.
- `console_gfx.py` – Palette constants, test images, and console renderer.

How to run:
1) `python P2_C.py`
2) Use menu options to load data, view RLE strings, or display the image.

What I learned:
- Implementing RLE encode/decode with length caps.
- Converting between numeric pixel data, hex strings, and colon-delimited RLE.
- Building a text UI that stitches together utility functions.
