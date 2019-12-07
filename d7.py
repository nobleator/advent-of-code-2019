import itertools


def execute(opcodes, phase_setting, input_signal):
    output = None
    phase = phase_setting.pop()
    first_input = True
    ptr = 0
    while opcodes[ptr] != 99:
        instr = str(opcodes[ptr]).zfill(5)
        opcode = instr[-2:]
        _, mode2, mode1 = [int(e) for e in list(instr[:-2])]
        
        if opcode == "01":
            param1, param2, param3 = opcodes[ptr + 1:ptr + 4]
            arg1 = opcodes[param1] if mode1 == 0 else param1
            arg2 = opcodes[param2] if mode2 == 0 else param2
            opcodes[param3] = arg1 + arg2
            ptr += 4
        elif opcode == "02":
            param1, param2, param3 = opcodes[ptr + 1:ptr + 4]
            arg1 = opcodes[param1] if mode1 == 0 else param1
            arg2 = opcodes[param2] if mode2 == 0 else param2
            opcodes[param3] = arg1 * arg2
            ptr += 4
        elif opcode == "03":
            param1 = opcodes[ptr + 1]
            opcodes[param1] = phase if first_input else input_signal
            first_input = False
            ptr += 2
        elif opcode == "04":
            param1 = opcodes[ptr + 1]
            output = opcodes[param1]
            if len(phase_setting) == 0:
                return output
            else:
                return execute(opcodes, phase_setting, output)
        elif opcode == "05":
            param1, param2 = opcodes[ptr + 1:ptr + 3]
            arg1 = opcodes[param1] if mode1 == 0 else param1
            if arg1 != 0:
                ptr = opcodes[param2] if mode2 == 0 else param2
            else:
                ptr += 3
        elif opcode == "06":
            param1, param2 = opcodes[ptr + 1:ptr + 3]
            arg1 = opcodes[param1] if mode1 == 0 else param1
            if arg1 == 0:
                ptr = opcodes[param2] if mode2 == 0 else param2
            else:
                ptr += 3
        elif opcode == "07":
            param1, param2, param3 = opcodes[ptr + 1:ptr + 4]
            arg1 = opcodes[param1] if mode1 == 0 else param1
            arg2 = opcodes[param2] if mode2 == 0 else param2
            opcodes[param3] = 1 if arg1 < arg2 else 0
            ptr += 4
        elif opcode == "08":
            param1, param2, param3 = opcodes[ptr + 1:ptr + 4]
            arg1 = opcodes[param1] if mode1 == 0 else param1
            arg2 = opcodes[param2] if mode2 == 0 else param2
            opcodes[param3] = 1 if arg1 == arg2 else 0
            ptr += 4
    return None

def d7_1(data):
    opcodes = [int(d) for d in data.split(",")]
    max_thruster_signal = 0
    for phase_setting in itertools.permutations([0, 1, 2, 3, 4]):
        phase_setting = list(phase_setting)
        thruster_signal = execute(opcodes, phase_setting, 0)
        if thruster_signal > max_thruster_signal:
            max_thruster_signal = thruster_signal
    return max_thruster_signal


class Amplifier:
    def __init__(self, opcodes: list, phase: int):
        self.opcodes = [code for code in opcodes]
        self.ptr = 0
        self.inputs = [phase]
        self.output = None
    
    def execute(self):
        while True:
            instr = str(self.opcodes[self.ptr]).zfill(5)
            opcode = instr[-2:]
            _, mode2, mode1 = [int(e) for e in list(instr[:-2])]
            
            if opcode == "01":
                param1, param2, param3 = self.opcodes[self.ptr + 1:self.ptr + 4]
                arg1 = self.opcodes[param1] if mode1 == 0 else param1
                arg2 = self.opcodes[param2] if mode2 == 0 else param2
                self.opcodes[param3] = arg1 + arg2
                self.ptr += 4
            elif opcode == "02":
                param1, param2, param3 = self.opcodes[self.ptr + 1:self.ptr + 4]
                arg1 = self.opcodes[param1] if mode1 == 0 else param1
                arg2 = self.opcodes[param2] if mode2 == 0 else param2
                self.opcodes[param3] = arg1 * arg2
                self.ptr += 4
            elif opcode == "03":
                param1 = self.opcodes[self.ptr + 1]
                self.opcodes[param1] = self.inputs.pop(0)
                self.ptr += 2
            elif opcode == "04":
                param1 = self.opcodes[self.ptr + 1]
                self.output = self.opcodes[param1]
                self.ptr += 2
                return self.output
            elif opcode == "05":
                param1, param2 = self.opcodes[self.ptr + 1:self.ptr + 3]
                arg1 = self.opcodes[param1] if mode1 == 0 else param1
                if arg1 != 0:
                    self.ptr = self.opcodes[param2] if mode2 == 0 else param2
                else:
                    self.ptr += 3
            elif opcode == "06":
                param1, param2 = self.opcodes[self.ptr + 1:self.ptr + 3]
                arg1 = self.opcodes[param1] if mode1 == 0 else param1
                if arg1 == 0:
                    self.ptr = self.opcodes[param2] if mode2 == 0 else param2
                else:
                    self.ptr += 3
            elif opcode == "07":
                param1, param2, param3 = self.opcodes[self.ptr + 1:self.ptr + 4]
                arg1 = self.opcodes[param1] if mode1 == 0 else param1
                arg2 = self.opcodes[param2] if mode2 == 0 else param2
                self.opcodes[param3] = 1 if arg1 < arg2 else 0
                self.ptr += 4
            elif opcode == "08":
                param1, param2, param3 = self.opcodes[self.ptr + 1:self.ptr + 4]
                arg1 = self.opcodes[param1] if mode1 == 0 else param1
                arg2 = self.opcodes[param2] if mode2 == 0 else param2
                self.opcodes[param3] = 1 if arg1 == arg2 else 0
                self.ptr += 4
            elif opcode == "99":
                # Returning None signals a stop
                return None
        # Return last output when exit code is reached
        return self.output


def d7_2(data):
    opcodes = [int(d) for d in data.split(",")]
    max_thruster_signal = 0
    for phase_setting in itertools.permutations([5, 6, 7, 8, 9]):
        phase_setting = list(phase_setting)
        amps = [Amplifier(opcodes, phase) for phase in phase_setting]
        # Initialize first amp starting input 0
        curr_amp_indx = 0
        curr_amp = amps[curr_amp_indx]
        curr_amp.inputs.append(0)
        loop_count = 1
        output = -1
        while True:
            output = curr_amp.execute()
            if output is None:
                break
            curr_amp_indx += 1
            if curr_amp_indx >= len(amps):
                curr_amp_indx = 0
                loop_count += 1
            curr_amp = amps[curr_amp_indx]
            curr_amp.inputs.append(output)

        thruster_signal = amps[-1].output
        if thruster_signal > max_thruster_signal:
            max_thruster_signal = thruster_signal
    return max_thruster_signal

# My input
with open("d7.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n").replace("\n", ", ")

# Part 1
# Test cases
print(f"Expected {43210} and got {d7_1('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0')}")
print(f"Expected {54321} and got {d7_1('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0')}")
print(f"Expected {65210} and got {d7_1('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0')}")

print(f"Part 1 {d7_1(data)}")

# Part 2
# Test cases
print(f"Expected {139629729} and got {d7_2('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5')}")
print(f"Expected {18216} and got {d7_2('3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10')}")

print(f"Part 2 {d7_2(data)}")
