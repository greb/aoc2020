import copy
import math

monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
]

def parse(inp):
    tiles = {}
    size = 9

    lines = inp.splitlines()
    for idx in range(0, len(lines), size+3):
        tile = int(lines[idx][5:-1])
        tiles[tile] = lines[idx+1:idx+size+2]
    return tiles


def tile_border(tile):
    north = tile[0]
    east  = ''.join(row[-1] for row in tile)
    south = tile[-1]
    west  = ''.join(row[0] for row in tile)
    return [north, east, south, west]


def tile_vflip(tile):
    return [''.join(reversed(row)) for row in tile]

def tile_rotcw(tile):
    return [''.join(reversed(row)) for row in zip(*tile)]


def tile_orientations(tile):
    # Because of symmetries 4 rotations and 1 vert flip for each
    # rotation is enough to get all orientations

    yield tile
    yield tile_vflip(tile)

    for _ in range(3):
        tile = tile_rotcw(tile)
        yield tile
        yield tile_vflip(tile)


def tile_remove_border(tile):
    return [row[1:-1] for row in tile[1:-1]]


def find_arrangement(tiles, size, arrangement=[], x=0, y=0, i=0):
    ind = ' '*i

    if y == size:
        return arrangement

    if x == size:
        return find_arrangement(tiles, size,
                arrangement, 0, y+1, i+1)

    canidates = []
    for num, tile in tiles.items():
        if num in (a[0] for a in arrangement):
            continue

        for orientation in tile_orientations(tile):
            idx = y*size + x

            border = tile_border(orientation)

            if x > 0:
                # has left neighbor
                neighbor_border = tile_border(arrangement[idx-1][1])
                if border[3] != neighbor_border[1]:
                    continue

            if y > 0:
                # has top neighbor
                neighbor_border = tile_border(arrangement[idx-size][1])
                if border[0] != neighbor_border[2]:
                    continue

            # valid orientation found
            canidates.append((num, orientation))

    for canidate in canidates:
        found = find_arrangement(tiles, size,
                arrangement + [canidate], x+1, y, i+1)
        if found:
            return found

    return None


def corner_product(arrangement, size):
    prod = 1
    indices = [0, size-1, size*(size-1), (size-1*size-1)]

    for idx in indices:
        prod *= arrangement[idx][0]
    return prod


def part1(inp):
    tiles = parse(inp)

    size = int(math.sqrt(len(tiles)))
    arrangement = find_arrangement(tiles, size)

    return corner_product(arrangement, size)


def generate_image(arrangement, size):
    tiles = [tile_remove_border(a[1]) for a in arrangement]
    tile_size = len(tiles[0])
    rows  = []

    for y in range(size):
        for y_row in range(tile_size):
            row = []
            for x in range(size):
                idx = y*size + x
                tile = tiles[idx]
                row.append(tile[y_row])
            rows.append(''.join(row))
    return rows


def count_pattern(image, pattern):
    w, h   = len(image[0]), len(image)
    pw, ph = len(pattern[0]), len(pattern)
    match = lambda p,i: p != '#' or p == i

    cnt = 0
    for y in range(0, h-ph+1):
        for x in range(0, w-pw+1):
            subimg = [row[x:x+pw] for row in image[y:y+ph]]

            hit = all( all(match(p,i) for p,i in zip(p_row, i_row))
                        for p_row, i_row in zip(pattern, subimg))

            if hit: cnt += 1
    return cnt

def count_symbol(image, symbol):
    cnt = 0
    for row in image:
        for pixel in row:
            if pixel == symbol:
                cnt += 1
    return cnt

def part2(inp):
    tiles = parse(inp)

    size = int(math.sqrt(len(tiles)))
    arrangement = find_arrangement(tiles, size)
    image = generate_image(arrangement, size)

    for oriented_image in tile_orientations(image):
        num_monster = count_pattern(oriented_image, monster)
        if num_monster > 0:
            break

    sym = count_symbol(oriented_image, '#')
    sym_monster = count_symbol(monster, '#')

    return sym - sym_monster*num_monster


import unittest
class Test(unittest.TestCase):
    test_tile = [
        '#...',
        '.#.#',
        '.##.',
        '.#..',
    ]

    test_image = [
        '.##.....................',
        '#..#.............#..#...',
        '.....#..###........###..',
        '.#.....##.#..#..........',
        '....................#...',
        '..#....##....##....###..',
        '...#..#..#..#..#..#.....',
        '........................',
        '....#....##....##....###',
        '.....#..#..#..#..#..#...',
        '........................',
    ]

    test_pattern = [
        ' ## ',
        '#  #',
    ]

    def test_tile_border(self):
        target = [
            '#...', '.#..', '.#..', '#...' 
        ]
        border = tile_border(self.test_tile)
        self.assertEqual(border, target)

    def test_tile_vflip(self):
        target = [
            '...#',
            '#.#.',
            '.##.',
            '..#.'
        ]
        tile = tile_vflip(self.test_tile)
        self.assertEqual(tile, target)

    def test_border_rotcw(self):
        target = [
            '...#',
            '###.',
            '.#..',
            '..#.',
        ]
        tile = tile_rotcw(self.test_tile)
        self.assertEqual(tile, target)

    def test_remove_border(self):
        target = [
            '#.',
            '##'
        ]
        tile = tile_remove_border(self.test_tile)
        self.assertEqual(tile, target)

    def test_count_pattern(self):
        count = count_pattern(self.test_image, self.test_pattern)
        self.assertEqual(count, 6)
