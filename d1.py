def d1_1(data):
    data = data.split(", ")
    return sum(((int(elem) // 3) - 2) for elem in data)

def d1_2(data):
    data = data.split(", ")
    fuel_required = 0
    for elem in data:
        fuel_added = (int(elem) // 3) - 2
        fuel_required += fuel_added
        remainder = (fuel_added // 3) - 2
        while remainder > 0:
            fuel_required += remainder
            remainder = (remainder // 3) - 2
    return fuel_required

# My input
with open("d1.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n").replace("\n", ", ")

# Part 1
# Test cases
print(f"Expected {2} and got {d1_1('12')}")
print(f"Expected {2} and got {d1_1('14')}")
print(f"Expected {654} and got {d1_1('1969')}")
print(f"Expected {33583} and got {d1_1('100756')}")

print(f"Part 1 {d1_1(data)}")

# Part 2
# Test cases
print(f"Expected {2} and got {d1_2('14')}")
print(f"Expected {966} and got {d1_2('1969')}")
print(f"Expected {50346} and got {d1_2('100756')}")

print(f"Part 2 {d1_2(data)}")

