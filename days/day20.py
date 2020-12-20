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

def tile_transforms(tile):
    # Because of symmetries 4 rotations and 1 vert flip for each
    # rotation is enough to get all transforms
    yield tile
    yield tile_vflip(tile)

    for _ in range(3):
        tile = tile_rotcw(tile)
        yield tile
        yield tile_vflip(tile)

def tile_remove_border(tile):
    return [row[1:-1] for row in tile[1:-1]]

def prepare_tiles(tiles):
    prepared = {}
    for num, tile in tiles.items():
        tile_data = []
        for transform in tile_transforms(tile):
            border = tile_border(transform)
            tile_data.append( (transform, border) )
        prepared[num] = tile_data
    return prepared


def find_order(tiles, size, order=[], x=0, y=0):
    if y == size:
        return order

    if x == size:
        return find_order(tiles, size, order, 0, y+1)

    matches = []
    for num, tile_data in tiles.items():
        if num in (a[0] for a in order):
            continue

        for transform, border in tile_data:
            tile_index = y*size + x

            if x > 0:
                # has left neighbor
                _, _, n_border = order[tile_index - 1]
                if border[3] != n_border[1]:
                    continue

            if y > 0:
                # has top neighbor
                _, _, n_border = order[tile_index - size]
                if border[0] != n_border[2]:
                    continue

            matches.append( (num, transform, border) )

    for match in matches:
        found = find_order(tiles, size, order + [match], x+1, y)
        if found:
            return found

    return None


def corner_product(order, size):
    prod = 1
    indices = [0, size-1, size*(size-1), (size-1*size-1)]

    for idx in indices:
        prod *= order[idx][0]
    return prod


def part1(inp):
    tiles = parse(inp)

    size = int(math.sqrt(len(tiles)))
    tiles = prepare_tiles(tiles)
    order = find_order(tiles, size)

    return corner_product(order, size)


def generate_image(order, size):
    tiles = [tile_remove_border(a[1]) for a in order]
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
    tiles = prepare_tiles(tiles)
    order = find_order(tiles, size)
    image = generate_image(order, size)

    for oriented_image in tile_transforms(image):
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
