def d6_1(data):
    data = data.split(",")
    parents = {}
    for orbit in data:
        inner, outer = orbit.split(")")
        inner = inner.strip()
        outer = outer.strip()
        parents[outer] = inner
    total_dist = 0
    for obj in parents:
        total_dist += 1
        parent = parents[obj]
        while parent != "COM":
            total_dist += 1
            parent = parents[parent]
    return total_dist

def d6_2(data):
    data = data.split(",")
    parents = {}
    for orbit in data:
        inner, outer = orbit.split(")")
        inner = inner.strip()
        outer = outer.strip()
        parents[outer] = inner
    
    path_san_to_com = []
    path_you_to_com = []

    parent = parents["SAN"]
    while parent != "COM":
        path_san_to_com.append(parent)
        parent = parents[parent]

    parent = parents["YOU"]
    while parent != "COM":
        path_you_to_com.append(parent)
        parent = parents[parent]

    for node in path_you_to_com:
        if node in path_san_to_com:
            indx_san = path_san_to_com.index(node)
            indx_you = path_you_to_com.index(node)
            return len(path_san_to_com[:indx_san]) + len(path_you_to_com[:indx_you])
    
    return None

# My input
with open("d6.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n").replace("\n", ", ")

# Part 1
# Test cases
print(f"Expected {42} and got {d6_1('COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L')}")

print(f"Part 1 {d6_1(data)}")

# Part 2
print(f"Expected {4} and got {d6_2('COM)B,B)C,C)D,D)E,E)F,B)G,G)H,D)I,E)J,J)K,K)L,K)YOU,I)SAN')}")

print(f"Part 2 {d6_2(data)}")
