import sys
import yaml

class VirtualMachine:
    def __init__(self, mem_size):
        self.memory = [0] * mem_size
        self.registers = [0] * 64
        self.pc = 0

    def execute(self, bin_file):
        with open(bin_file, 'rb') as f:
            code = f.read()

        while self.pc < len(code):
            instruction = code[self.pc]
            self.pc += 1

            if instruction == 0x7C:  # LOAD_CONST
                B = code[self.pc]
                self.pc += 1
                C = code[self.pc]
                self.pc += 1
                D = code[self.pc]
                self.pc += 1
                self.registers[C] = (B << 16) | (C << 8) | D
                print(f"LOAD_CONST: R[{C}] = {self.registers[C]}, Registers: {self.registers}")
                continue

            elif instruction == 0x27:  # READ_MEM
                B = code[self.pc]
                self.pc += 1
                tmp = code[self.pc]
                self.pc += 1
                C = (tmp << 2) | (B >> 6)
                D = B & 0x3F
                self.registers[D] = self.memory[self.registers[C] + self.registers[D]]
                print(f"READ_MEM: R[{D}] = M[R[{C}] + R[{D}]] ({self.registers[D]}), Registers: {self.registers}, Memory: {self.memory}")
                continue

            elif instruction == 0x75:  # WRITE_MEM
                B = code[self.pc]
                self.pc += 1
                tmp = code[self.pc]
                self.pc += 1
                C = (tmp << 2) | (B >> 6)
                self.memory[self.registers[C] + self.registers[D]] = self.registers[B]
                print(f"WRITE_MEM: M[R[{C}] + R[{D}]] = R[{B}] ({self.registers[B]}), Registers: {self.registers}, Memory: {self.memory}")
                continue

            elif instruction == 0x1C:  # BITREVERSE
                B = code[self.pc]
                self.pc += 1
                C = code[self.pc]
                self.pc += 1
                value = self.registers[C]
                rev_value = int('{:032b}'.format(value)[::-1], 2)
                self.registers[B] = rev_value
                print(f"BITREVERSE: R[{B}] = ~R[{C}] ({value}) => {rev_value}, Registers: {self.registers}")
                continue

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("[ Usage: python interpreter.py <binary_file> <result_file> ]")
        sys.exit(1)

    bin_file = sys.argv[1]
    res_file = sys.argv[2]

    vm = VirtualMachine(mem_size=256)
    vm.execute(bin_file)

    res_data = {
        "registers": vm.registers,
        "memory": vm.memory
    }

    with open(res_file, 'w') as f:
        yaml.dump(res_data, f)
