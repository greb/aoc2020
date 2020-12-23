from itertools import chain

def execute_steps(cups, n_steps):
    prev = None
    next_cup = {}

    for c in cups:
        if prev is None:
            start = c
        else:
            next_cup[prev] = c
        prev = c
    next_cup[c] = start

    curr = start
    for _ in range(n_steps):
        n1 = next_cup[curr]
        n2 = next_cup[n1]
        n3 = next_cup[n2]

        tail = next_cup[n3]
        next_cup[curr] = tail

        dest = curr
        while True:
            dest -= 1
            if dest == 0:
                dest = len(next_cup)
            if dest not in (n1,n2,n3):
                break

        next_cup[n3] = next_cup[dest]
        next_cup[dest] = n1
        curr = tail

    curr = 1
    while next_cup[curr] != 1:
        curr = next_cup[curr]
        yield curr


def part1(inp):
    cups = [int(c) for c in inp.strip()]

    gen = execute_steps(cups, 100)
    return ''.join(map(str, gen))


def part2(inp):
    cups = [int(c) for c in inp.strip()]
    cups = chain(cups, range(10, 1_000_001))

    gen = execute_steps(cups, 10_000_000)
    return next(gen) * next(gen)
