from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "lib"
OUT = ROOT / "output_usr"

EXT = ".am"
MAX_NAME = 15


def load_folder(folder):
    blocks = {}

    for file in (LIB / folder).glob("*.txt"):
        blocks[file.stem.upper()] = file.read_text()

    return blocks


def parse_input(text):
    text = text.strip()

    if not (text.startswith("[") and text.endswith("]")):
        raise ValueError("input must be in [GATE1,GATE2] format")

    text = text[1:-1].strip()

    if not text:
        raise ValueError("empty gate list")

    return [gate.strip().upper() for gate in text.split(",") if gate.strip()]


def build_program(gates, blocks, readout, header, footer):
    for gate in gates:
        if gate not in blocks:
            raise ValueError(f"unknown gate: {gate}")

    program = header

    if not program.endswith("\n"):
        program += "\n"

    for gate in gates:
        program += blocks[gate].strip() + "\n\n"

        if not blocks[gate].endswith("\n"):
            program += "\n"

    program += readout

    if not readout.endswith("\n"):
        program += "\n"

    program += footer

    if not program.endswith("\n"):
        program += "\n"

    return program


def make_filename(gates, readout_name):
    name = "_".join(gates + [readout_name])
    return name[:MAX_NAME] + EXT


def main():
    blocks = load_folder("gates")
    readouts = load_folder("readOut")

    header = (LIB / "header.txt").read_text()
    footer = (LIB / "footer.txt").read_text()

    try:
        user_input = input("Enter gate sequence: ")
        gates = parse_input(user_input)

        choice = input("Choose readout (INIT/OBSPOP): ").strip().upper()

        if choice not in ["INIT", "OBSPOP"]:
            raise ValueError("readout must be INIT or OBSPOP")

        if choice not in readouts:
            raise ValueError(f"{choice}.txt not found in lib/readOut")

        program = build_program(
            gates,
            blocks,
            readouts[choice],
            header,
            footer
        )

        OUT.mkdir(parents=True, exist_ok=True)

        filename = make_filename(gates, choice)
        path = OUT / filename

        path.write_text(program)

        print(f"Created: {filename}")

    except ValueError as error:
        print(f"ERROR: {error}")


if __name__ == "__main__":
    main()