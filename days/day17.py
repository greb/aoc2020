import itertools
import collections

def parse(inp, dims):
    cubes = set()

    for y, line in enumerate(inp.splitlines()):
        for x, cube in enumerate(line):
            if cube == '#':
                coord = tuple([x,y] + [0]*(dims-2))
                cubes.add(coord)
    return cubes


def neigbors(cube):
    dims = len(cube)
    deltas = itertools.product([-1, 0, 1], repeat=dims)
    for delta in deltas:
        coord = tuple(c+d for c,d in zip(cube, delta))
        if coord != cube:
            yield coord


def cycle(cubes):
    neighbor_counts = collections.defaultdict(int)
    for cube in cubes:
        for neighbor in neigbors(cube):
            neighbor_counts[neighbor] += 1

    new_cubes = set()
    for cube, count in neighbor_counts.items():
        if cube in cubes:
            if count in (2,3):
                new_cubes.add(cube)
        else:
            if count == 3:
                new_cubes.add(cube)

    return new_cubes

def solve_part1(inp):
    cubes = parse(inp, 3)
    for _ in range(6):
        cubes = cycle(cubes)
    return len(cubes)

def solve_part2(inp):
    cubes = parse(inp, 4)
    for _ in range(6):
        cubes = cycle(cubes)
    return len(cubes)
