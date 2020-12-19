def parse(inp):
    return inp.splitlines()

def count_trees(inp, sx, sy):
    cx, cy = 0, 0

    tree_cnt = 0
    while cy < len(inp):
        if cx >= len(inp[cy]):
            cx -= len(inp[cy])

        if inp[cy][cx] == '#':
            tree_cnt += 1

        cx += sx
        cy += sy

    return tree_cnt


def part1(inp):
    inp = parse(inp)
    return count_trees(inp, 3, 1)


def part2(inp):
    inp = parse(inp)

    tree_cnt = 1
    slopes = [ (1,1), (3,1), (5,1), (7,1), (1, 2) ]
    for sx, sy in slopes:
        tree_cnt *= count_trees(inp, sx, sy)

    return tree_cnt
