class IntCode:
    def __init__(self, opcodes: list, phase: int=None):
        self.opcodes = [code for code in opcodes]
        self.ptr = 0
        self.relative_base = 0
        if phase is not None:
            self.inputs = [phase]
        else:
            self.inputs = []
        self.output = None

    def get_value(self, mode, param):
        if mode == 0:
            if param >= len(self.opcodes):
                self.opcodes.extend([0 for _ in range(len(self.opcodes), param + 1)])
            return self.opcodes[param]
        elif mode == 1:
            return param
        elif mode == 2:
            if param + self.relative_base >= len(self.opcodes):
                self.opcodes.extend([0 for _ in range(len(self.opcodes), param + self.relative_base + 1)])
            return self.opcodes[param + self.relative_base]

    def set_value(self, mode, indx, val):
        if mode == 0:
            if indx >= len(self.opcodes):
                self.opcodes.extend([0 for _ in range(len(self.opcodes), indx + 1)])
            self.opcodes[indx] = val
        elif mode == 1:
            return "ERROR ERROR THIS SHOULD NOT HAPPEN"
        elif mode == 2:
            if indx + self.relative_base >= len(self.opcodes):
                self.opcodes.extend([0 for _ in range(len(self.opcodes), indx + self.relative_base + 1)])
            self.opcodes[indx + self.relative_base] = val
    
    def execute(self):
        while True:
            instr = str(self.opcodes[self.ptr]).zfill(5)
            opcode = instr[-2:]
            mode3, mode2, mode1 = [int(e) for e in list(instr[:-2])]
            self.ptr += 1

            if opcode == "01":
                param1, param2, param3 = self.opcodes[self.ptr:self.ptr + 3]
                arg1 = self.get_value(mode1, param1)
                arg2 = self.get_value(mode2, param2)
                self.set_value(mode3, param3, arg1 + arg2)
                self.ptr += 3
            elif opcode == "02":
                param1, param2, param3 = self.opcodes[self.ptr:self.ptr + 3]
                arg1 = self.get_value(mode1, param1)
                arg2 = self.get_value(mode2, param2)
                self.set_value(mode3, param3, arg1 * arg2)
                self.ptr += 3
            elif opcode == "03":
                param1 = self.opcodes[self.ptr]
                self.set_value(mode1, param1, self.inputs.pop(0))
                self.ptr += 1
            elif opcode == "04":
                param1 = self.opcodes[self.ptr]
                self.output = self.get_value(mode1, param1)
                self.ptr += 1
                # print(self.output)
                # return self.output
            elif opcode == "05":
                param1, param2 = self.opcodes[self.ptr:self.ptr + 2]
                arg1 = self.get_value(mode1, param1)
                if arg1 != 0:
                    self.ptr = self.get_value(mode2, param2)
                else:
                    self.ptr += 2
            elif opcode == "06":
                param1, param2 = self.opcodes[self.ptr:self.ptr + 2]
                arg1 = self.get_value(mode1, param1)
                if arg1 == 0:
                    self.ptr = self.get_value(mode2, param2)
                else:
                    self.ptr += 2
            elif opcode == "07":
                param1, param2, param3 = self.opcodes[self.ptr:self.ptr + 3]
                arg1 = self.get_value(mode1, param1)
                arg2 = self.get_value(mode2, param2)
                self.set_value(mode3, param3, 1 if arg1 < arg2 else 0)
                # self.opcodes[param3] = 1 if arg1 < arg2 else 0
                self.ptr += 3
            elif opcode == "08":
                param1, param2, param3 = self.opcodes[self.ptr:self.ptr + 3]
                arg1 = self.get_value(mode1, param1)
                arg2 = self.get_value(mode2, param2)
                self.set_value(mode3, param3, 1 if arg1 == arg2 else 0)
                # self.opcodes[param3] = 1 if arg1 == arg2 else 0
                self.ptr += 3
            elif opcode == "09":
                param1 = self.opcodes[self.ptr]
                self.relative_base += self.get_value(mode1, param1)
                self.ptr += 1
            elif opcode == "99":
                # Returning None signals a stop
                return None
        # Return last output when exit code is reached
        return self.output

def d9_1(data, input_signal=None):
    opcodes = [int(d) for d in data.split(",")]
    computer = IntCode(opcodes)
    if input_signal is not None:
        computer.inputs.append(input_signal)
    computer.execute()
    return computer.output

def d9_2(data, input_signal=None):
    opcodes = [int(d) for d in data.split(",")]
    computer = IntCode(opcodes)
    if input_signal is not None:
        computer.inputs.append(input_signal)
    computer.execute()
    return computer.output

# My input
with open("d9.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n").replace("\n", ", ")

# Part 1
# Test cases
print(f"Expected {109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99} and got {d9_1('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')}")
print(f"Expected [some 16 digit number] and got {d9_1('1102,34915192,34915192,7,4,7,99,0')}")
print(f"Expected {1125899906842624} and got {d9_1('104,1125899906842624,99')}")

print(f"Part 1 {d9_1(data, 1)}")

# Part 2
print(f"Part 2 {d9_2(data, 2)}")
