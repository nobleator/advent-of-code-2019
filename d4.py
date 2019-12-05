def adjacent_pair(num_str):
    for i, c1 in enumerate(num_str):
        if (i > 1 and num_str[i - 1] == c1) or (i < 5 and num_str[i + 1] == c1):
            return True
    return False

def increasing(num_str):
    return all(int(i) <= int(j) for i, j in zip(num_str, num_str[1:]))

def d4_1(data):
    start, end = data.split("-")
    ctr = 0
    for num in range(int(start), int(end) + 1):
        if adjacent_pair(str(num)) and increasing(str(num)):
            ctr += 1
    return ctr

def adjacent_sole_pair(num_str):
    i = 0
    while i < len(num_str) - 1:
        curr = num_str[i]
        count = 1
        n = i + 1
        while n < len(num_str) and curr == num_str[n]:
            count += 1
            n += 1
        if count == 1:
            i += 1
        elif count == 2:
            return True
        else:
            i = n
    return False

def d4_2(data):
    start, end = data.split("-")
    ctr = 0
    for num in range(int(start), int(end) + 1):
        if adjacent_sole_pair(str(num)) and increasing(str(num)):
            ctr += 1
    return ctr

# My input
data = "168630-718098"

# Part 1
# print(f"Part 1 {d4_1(data)}")

# Part 2
print(f"Part 2 {d4_2(data)}")
