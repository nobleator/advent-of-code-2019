import math
import numpy as np
import sys


def d10_1(data):
    # asteroids = {<point>: set(<angles in degrees>)}
    asteroids = {}
    for r_indx, r_val in enumerate(data.split(",")):
        for c_indx, c_val in enumerate(r_val):
            if c_val == "#":
                asteroids[(c_indx, r_indx)] = set()
    # Get set of unique angles
    for asteroid_a in asteroids:
        for asteroid_b in asteroids:
            if asteroid_a[0] == asteroid_b[0] and asteroid_a[1] == asteroid_b[1]:
                continue
            angle = math.atan2(asteroid_a[0] - asteroid_b[0], asteroid_a[1] - asteroid_b[1])
            asteroids[asteroid_a].add(angle)
    station = max   (asteroids, key=lambda x: len(asteroids[x]))
    return station, len(asteroids[station])

def get_dist(p1, p2):
    return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

def d10_2(data):
    asteroids = set()
    for r_indx, r_val in enumerate(data.split(",")):
        for c_indx, c_val in enumerate(r_val):
            if c_val == "#":
                asteroids.add((c_indx, r_indx))
    station, _ = d10_1(data)
    print(f"station {station}")
    vaporizations = [station]
    while len(vaporizations) < 201:
        visible = {}
        for asteroid in asteroids:
            angle = math.atan2(station[1] - asteroid[1], station[0] - asteroid[0]) * 180 / math.pi
            # Shift angles to convert up to be 0
            angle -= 90
            if angle < 0:
                angle += 360
            if angle in visible:
                if get_dist(asteroid, station) < get_dist(visible[angle], station):
                    visible[angle] = asteroid
            else:
                visible[angle] = asteroid
        targets = [visible[k] for k in sorted(visible.keys())]
        for t in targets:
            asteroids.remove(t)
        vaporizations += targets
    mat = np.zeros((33, 33))
    mat[station[0], station[1]] = -1
    mat[station] = -1
    for i, v in enumerate(vaporizations):
        mat[v[0], v[1]] = i
    np.set_printoptions(threshold=sys.maxsize)
    print(mat)
    np.set_printoptions(threshold=1000)
    return vaporizations[200][0] * 100 + vaporizations[200][1]

# My input
with open("d10.txt", "r") as f:
    data = "".join(f.readlines())
    data = data.rstrip("\n").replace("\n", ", ")

# Part 1
# Test cases
print(f"Expected {(3,4), 8} and got {d10_1('.#..#,.....,#####,....#,...##')}")
print(f"Expected {(5,8), 33} and got {d10_1('......#.#.,#..#.#....,..#######.,.#.#.###..,.#..#.....,..#....#.#,#..#....#.,.##.#..###,##...#..#.,.#....####')}")
print(f"Expected {(1,2), 35} and got {d10_1('#.#...#.#.,.###....#.,.#....#...,##.#.#.#.#,....#.#.#.,.##..###.#,..#...##..,..##....##,......#...,.####.###.')}")
print(f"Expected {(6,3), 41} and got {d10_1('.#..#..###,####.###.#,....###.#.,..###.##.#,##.##.#.#.,....###..#,..#.#..#.#,#..#.#.###,.##...##.#,.....#.#..')}")
print(f"Expected {(11,13), 210} and got {d10_1('.#..##.###...#######,##.############..##.,.#.######.########.#,.###.#######.####.#.,#####.##.#.##.###.##,..#####..#.#########,####################,#.####....###.#.#.##,##.#################,#####.##.###..####..,..######..##.#######,####.##.####...##..#,.#####..#.######.###,##...#.##########...,#.##########.#######,.####.#.###.###.#.##,....##.##.###..#####,.#.#.###########.###,#.#.#.#####.####.###,###.##.####.##.#..##')}")

print(f"Part 1 {d10_1(data)}")

# Part 2
# Test cases
print(f"Expected {(802)} and got {d10_2('.#..##.###...#######,##.############..##.,.#.######.########.#,.###.#######.####.#.,#####.##.#.##.###.##,..#####..#.#########,####################,#.####....###.#.#.##,##.#################,#####.##.###..####..,..######..##.#######,####.##.####...##..#,.#####..#.######.###,##...#.##########...,#.##########.#######,.####.#.###.###.#.##,....##.##.###..#####,.#.#.###########.###,#.#.#.#####.####.###,###.##.####.##.#..##')}")

# 1410 too low
# 2021 too high
print(f"Part 2 {d10_2(data)}")
