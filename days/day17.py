def parse(inp):
    cubes = set()
    lines = inp.splitlines()

    z = 0
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            if cell == '#':
                cubes.add((x,y,z))

    return cubes


def cube_bounds(cubes):
    bounds = []
    for axis in range(3):
        vals = [a[axis] for a in cubes]
        bounds.append((min(vals), max(vals)))
    return bounds


def cube_neighbors(cube):
    cx,cy,cz = cube
    for x in range(cx-1, cx+2):
        for y in range(cy-1, cy+2):
            for z in range(cz-1, cz+2):
                neighbor = (x,y,z)
                if neighbor != cube:
                    yield neighbor


def cube_active(cube, cubes):
    cnt = 0
    for n in cube_neighbors(cube):
        if n in cubes:
            cnt += 1

    if cube in cubes:
        return cnt in [2,3]

    return cnt == 3


def cube_cycle(cubes):
    (xmin,xmax), (ymin,ymax), (zmin,zmax) = cube_bounds(cubes)

    new_cubes = set()
    for x in range(xmin-1, xmax+2):
        for y in range(ymin-1, ymax+2):
            for z in range(zmin-1, zmax+2):
                cube = (x,y,z)
                if cube_active(cube, cubes):
                    new_cubes.add(cube)

    return new_cubes


def parse4(inp):
    cubes = set()
    lines = inp.splitlines()

    z = 0
    w = 0
    for y, line in enumerate(lines):
        for x, cell in enumerate(line):
            if cell == '#':
                cubes.add((x,y,z,w))

    return cubes


def cube_bounds4(cubes):
    bounds = []
    for axis in range(4):
        vals = [a[axis] for a in cubes]
        bounds.append((min(vals), max(vals)))
    return bounds


def cube_neighbors4(cube):
    cx,cy,cz,cw = cube
    for x in range(cx-1, cx+2):
        for y in range(cy-1, cy+2):
            for z in range(cz-1, cz+2):
                for w in range(cw-1, cw+2):
                    neighbor = (x,y,z,w)
                    if neighbor != cube:
                        yield neighbor


def cube_active4(cube, cubes):
    cnt = 0
    for n in cube_neighbors4(cube):
        if n in cubes:
            cnt += 1

    if cube in cubes:
        return cnt in [2,3]

    return cnt == 3


def cube_cycle4(cubes):
    (xmin,xmax), (ymin,ymax), (zmin,zmax), (wmin, wmax) = cube_bounds4(cubes)

    new_cubes = set()
    for x in range(xmin-1, xmax+2):
        for y in range(ymin-1, ymax+2):
            for z in range(zmin-1, zmax+2):
                for w in range(wmin-1, wmax+2):
                    cube = (x,y,z,w)
                    if cube_active4(cube, cubes):
                        new_cubes.add(cube)

    return new_cubes


def solve_part1(inp):
    cubes = parse(inp)

    for cycle in range(6):
        cubes = cube_cycle(cubes)

    return len(cubes)

def solve_part2(inp):
    cubes = parse4(inp)

    for cycle in range(6):
        cubes = cube_cycle4(cubes)

    return len(cubes)

