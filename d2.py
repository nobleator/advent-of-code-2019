def d2_1(data, override1 = None, override2 = None):
    opcodes = [int(d) for d in data.split(",")]
    if override1 is not None:
        opcodes[1] = override1
    if override2 is not None:
        opcodes[2] = override2
    ptr = 0
    while opcodes[ptr] != 99:
        instr, indx1, indx2, dest = opcodes[ptr:ptr + 4]
        arg1 = opcodes[indx1]
        arg2 = opcodes[indx2]
        opcodes[dest] = arg1 + arg2 if instr == 1 else arg1 * arg2
        ptr += 4
    return opcodes[0]

def d2_2(data):
    for noun in range(0, 100):
        for verb in range(0, 100):
            output = d2_1(data, override1=noun, override2=verb)
            # print(noun, verb, output)
            if output == 19690720:
                return (100 * noun) + verb
    return None

# My input
with open("d2.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n").replace("\n", ", ")

# Part 1
# Test cases
print(f"Expected {3500} and got {d2_1('1,9,10,3,2,3,11,0,99,30,40,50')}")
print(f"Expected {2} and got {d2_1('1,0,0,0,99')}")
print(f"Expected {2} and got {d2_1('2,3,0,3,99')}")
print(f"Expected {30} and got {d2_1('1,1,1,4,99,5,6,0,99')}")

print(f"Part 1 {d2_1(data, override1=12, override2=2)}")

# Part 2
print(f"Part 2 {d2_2(data)}")
