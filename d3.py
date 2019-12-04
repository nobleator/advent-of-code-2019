def manhattan_dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def process_path(wire):
    curr = [0, 0]
    path = [tuple(curr)]
    for move in wire.split(","):
        direction = move[0]
        magnitude = int(move[1:])
        for _ in range(magnitude):
            if direction == "R":
                curr[0] += 1
            if direction == "L":
                curr[0] -= 1
            if direction == "U":
                curr[1] += 1
            if direction == "D":
                curr[1] -= 1
            path.append(tuple(curr))
    return path

def d3_1(data):
    wire1, wire2, _ = data.split("\n")
    path1 = process_path(wire1)
    path2 = process_path(wire2)
    # Remove start point from paths
    path1 = path1[1:]
    path2 = path2[1:]
    intersections = list(set(path1).intersection(path2))
    return min(manhattan_dist((0, 0), i) for i in intersections)

def d3_2(data):
    wire1, wire2, _ = data.split("\n")
    path1 = process_path(wire1)
    path2 = process_path(wire2)
    # Remove start point from paths
    path1 = path1[1:]
    path2 = path2[1:]
    intersections = list(set(path1).intersection(path2))
    return min([path1.index(i) + path2.index(i) + 2 for i in intersections])

# My input
with open("d3.txt", "r") as f:
    data = "".join(f.readlines())
    # data = data.rstrip("\n").replace("\n", ", ")

# Part 1
# Test cases
test_data = "R8,U5,L5,D3\nU7,R6,D4,L4\n"
print(f"Expected {6} and got {d3_1(test_data)}")
test_data = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83\n"
print(f"Expected {159} and got {d3_1(test_data)}")
test_data = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7\n"
print(f"Expected {135} and got {d3_1(test_data)}")

print(f"Part 1 {d3_1(data)}")

# Part 2
# Test cases
test_data = "R8,U5,L5,D3\nU7,R6,D4,L4\n"
print(f"Expected {30} and got {d3_2(test_data)}")
test_data = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83\n"
print(f"Expected {610} and got {d3_2(test_data)}")
test_data = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7\n"
print(f"Expected {410} and got {d3_2(test_data)}")

print(f"Part 2 {d3_2(data)}")
