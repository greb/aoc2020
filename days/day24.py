dirs = {
    'e': (1,0),
    'se': (1,1),
    'sw': (0, 1),
    'w': (-1, 0),
    'nw': (-1,-1),
    'ne': (0, -1)
}

def parse(inp):
    paths = []
    for line in inp.splitlines():
        path = []
        while line:
            if line[0] in ('s', 'n'):
                path.append(line[:2])
                line = line[2:]
            else:
                path.append(line[0])
                line = line[1:]
        paths.append(path)
    return paths


def end_tile(tile, path):
    x,y = tile
    for p in path:
        dx, dy  = dirs[p]
        x += dx
        y += dy
    return x,y

def tile_plane(paths):
    black_tiles = set()
    for path in paths:
        tile = end_tile((0,0), path)

        if tile in black_tiles:
            black_tiles.discard(tile)
        else:
            black_tiles.add(tile)
    return black_tiles

def part1(inp):
    paths = parse(inp)
    black_tiles = tile_plane(paths)
    return len(black_tiles)


def perform_art(black_tiles):
    num_neighbors = dict()
    for tile in black_tiles:
        x,y = tile
        for dx,dy in dirs.values():
            neighbor = x+dx, y+dy
            if neighbor not in num_neighbors:
                num_neighbors[neighbor] = 1
            else:
                num_neighbors[neighbor] += 1

    new_black_tiles = set()
    for tile, num in num_neighbors.items():
        if tile in black_tiles:
            if 0 < num <= 2:
                new_black_tiles.add(tile)
        else:
            if num == 2:
                new_black_tiles.add(tile)
    return new_black_tiles


def part2(inp):
    paths = parse(inp)
    black_tiles = tile_plane(paths)

    for _ in range(100):
        black_tiles = perform_art(black_tiles)
    
    return len(black_tiles)
