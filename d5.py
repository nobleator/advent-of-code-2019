def d5_1(data, input_value):
    opcodes = [int(d) for d in data.split(",")]
    output = "OUTPUT"
    ptr = 0
    while opcodes[ptr] != 99:
        instr = str(opcodes[ptr]).zfill(5)
        opcode = instr[-2:]
        mode3, mode2, mode1 = [int(e) for e in list(instr[:-2])]
        
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
            opcodes[param1] = input_value
            ptr += 2
        elif opcode == "04":
            param1 = opcodes[ptr + 1]
            output = opcodes[param1]
            print(f"OUTPUT: {output}")
            ptr += 2
    return output

def d5_2(data, input_value):
    opcodes = [int(d) for d in data.split(",")]
    output = "OUTPUT"
    ptr = 0
    while opcodes[ptr] != 99:
        instr = str(opcodes[ptr]).zfill(5)
        opcode = instr[-2:]
        mode3, mode2, mode1 = [int(e) for e in list(instr[:-2])]
        
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
            opcodes[param1] = input_value
            ptr += 2
        elif opcode == "04":
            param1 = opcodes[ptr + 1]
            output = opcodes[param1]
            print(f"OUTPUT: {output}")
            ptr += 2
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
    return output

# My input
with open("d5.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n").replace("\n", ", ")

# Part 1
# Test cases
print(f"Expected {99} and got {d5_1('1002,4,3,4,33', 1)}")

print(f"Part 1 {d5_1(data, input_value=1)}")

# Part 2

print(f"Part 2 {d5_2(data, input_value=5)}")
