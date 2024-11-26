import sys
import yaml

COMMANDS = {
    "LOAD_CONST": 0x7C,
    "READ_MEM": 0x27,
    "WRITE_MEM": 0x75,
    "BITREVERSE": 0x1C,
}


def assemble_line(line):
    tokens = line.split()
    command = tokens[0]

    if command == "LOAD_CONST":
        A = COMMANDS["LOAD_CONST"]
        B = int(tokens[1])  # Константа (24 бита)
        C = int(tokens[2])  # Адрес (6 бит)
        return [
            A,
            (B >> 16) & 0xFF,  # Старшие 8 бит константы
            (B >> 8) & 0xFF,   # Средние 8 бит
            B & 0xFF,          # Младшие 8 бит
            C & 0x3F           # Адрес в пределах 6 бит
        ]

    elif command == "READ_MEM":
        A = COMMANDS["READ_MEM"]
        B = int(tokens[1])  # Адрес регистра (6 бит)
        C = int(tokens[2])  # Смещение (12 бит)
        D = int(tokens[3])  # Адрес регистра (6 бит)
        return [
            A,
            (B & 0x3F) << 2 | (C >> 10) & 0x03,  # Адрес регистра и старшие 2 бита смещения
            (C >> 2) & 0xFF,                    # Средние 8 бит смещения
            (C & 0x03) << 6 | (D & 0x3F)        # Младшие 2 бита смещения и адрес регистра
        ]

    elif command == "WRITE_MEM":
        A = COMMANDS["WRITE_MEM"]
        B = int(tokens[1])  # Адрес регистра (6 бит)
        C = int(tokens[2])  # Адрес памяти (12 бит)
        return [
            A,
            (B & 0x3F) << 2 | (C >> 10) & 0x03,  # Адрес регистра и старшие 2 бита адреса
            (C >> 2) & 0xFF,                    # Средние 8 бит адреса
            (C & 0x03) << 6                     # Младшие 2 бита адреса
        ]

    elif command == "BITREVERSE":
        A = COMMANDS["BITREVERSE"]
        B = int(tokens[1])  # Адрес регистра (6 бит)
        C = int(tokens[2])  # Адрес регистра (6 бит)
        return [
            A,
            (B & 0x3F) << 2 | (C >> 4) & 0x03,  # Адрес регистра и старшие 2 бита второго адреса
            (C & 0x0F) << 4                     # Младшие 4 бита второго адреса
        ]

    else:
        print(f"[ Error: Unknown command '{command}' at line '{line}' ]")
        return []


def assemble(file_path):
    bin_code = []
    log = {}

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                cmd_bytes = assemble_line(line)
                bin_code.extend(cmd_bytes)
                log[line] = [f"0x{byte:02X}" for byte in cmd_bytes]

    return bin_code, log


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("[ Usage: python assembler.py <input_file> <output_bin_file> <output_log_file> ]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_bin_file = sys.argv[2]
    log_file = sys.argv[3]

    bin_code, log = assemble(input_file)

    # Формируем бинарный файл в нужном формате
    with open(output_bin_file, 'w') as binf:
        binf.write(", ".join([f"0x{byte:02X}" for byte in bin_code]))

    # Сохраняем лог
    with open(log_file, 'w') as logf:
        yaml.dump(log, logf)

