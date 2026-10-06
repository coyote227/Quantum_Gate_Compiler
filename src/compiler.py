from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "lib"
TESTS = ROOT / "tests" / "tests.txt"
OUT = ROOT / "out"

EXT = ".am"
MAX_NAME = 15


def load_library():
    blocks = {}

    for folder in ["gates", "readOut"]:
        for file in (LIB / folder).glob("*.txt"):
            blocks[file.stem.upper()] = file.read_text()

    return blocks


def parse_tests():
    sequences = []

    for line in TESTS.read_text().splitlines():
        line = line.split("//")[0].strip()

        if not line:
            continue

        if not (line.startswith("[") and line.endswith("]")):
            print(f"ERROR: invalid format: {line}")
            continue

        line = line[1:-1].strip()

        if not line:
            sequences.append([])
            continue

        gates = [
            gate.strip().upper()
            for gate in line.split(",")
            if gate.strip()
        ]

        sequences.append(gates)

    return sequences


def build_program(gates, blocks, header, footer):
    if not gates:
        raise ValueError("empty gate list")

    for gate in gates:
        if gate not in blocks:
            raise ValueError(f"unknown gate: {gate}")

    program = header

    if not program.endswith("\n"):
        program += "\n"

    for gate in gates:
        program += blocks[gate]

        if not blocks[gate].endswith("\n"):
            program += "\n"

    program += footer

    if not program.endswith("\n"):
        program += "\n"

    return program


def make_filename(gates, used):
    base = "_".join(gates)[:MAX_NAME]
    name = base
    number = 1

    while name.lower() in used:
        number += 1
        suffix = str(number)
        name = base[:MAX_NAME - len(suffix)] + suffix

    used.add(name.lower())

    return name + EXT


def main():
    blocks = load_library()

    header = (LIB / "header.txt").read_text()
    footer = (LIB / "footer.txt").read_text()

    sequences = parse_tests()

    OUT.mkdir(parents=True, exist_ok=True)

    used = set()

    for number, gates in enumerate(sequences, 1):
        display = "[" + ", ".join(gates) + "]"

        try:
            program = build_program(gates, blocks, header, footer)

            filename = make_filename(gates, used)
            path = OUT / filename

            path.write_text(program)

            print(f"{number}. {display} -> {filename}")

        except ValueError as error:
            print(f"{number}. {display} -> ERROR: {error}")


if __name__ == "__main__":
    main()