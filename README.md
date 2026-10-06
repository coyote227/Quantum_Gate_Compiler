# NMR Pulse Program Compiler

Converts gate sequences into Bruker NMR pulse program (`.am`) files.

## Project Structure

```text
project/
├── src/
│   ├── compiler.py
│   └── compiler_userin.py
├── tests/
│   └── tests.txt
├── lib/
│   ├── header.txt
│   ├── footer.txt
│   ├── gates/
│   └── readOut/
├── out/
└── output_usr/

## Files

- `src/compiler.py` - runs gate sequences from `tests/tests.txt`
- `src/compiler_userin.py` - takes a gate sequence from the terminal
- `lib/gates/` - gate pulse code
- `lib/readOut/` - INIT and OBSPOP code
- `lib/header.txt` - common header
- `lib/footer.txt` - common footer

## Running the Test Compiler

From the project root:

```bash
python src/compiler.py