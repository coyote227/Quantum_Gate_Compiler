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
```

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
```

The gate sequences are read from:

```text
tests/tests.txt
```

Generated `.am` files are saved in:

```text
out/
```

Errors are displayed in the terminal. No output file is created for a failed sequence.

## Running the User Input Compiler

From the project root:

```bash
python src/compiler_userin.py
```

Enter the gate sequence when prompted:

```text
Enter gate sequence: [NOT1,CNOT12,HAD]
Choose readout (INIT/OBSPOP): OBSPOP
```

Generated `.am` files are saved in:

```text
output_usr/
```

## Output

Each generated `.am` file contains the header, gate blocks in the given order, readout code where applicable, and footer.

Output filenames are based on the input gate sequence and are limited to 15 characters before `.am`.