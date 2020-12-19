import collections

def part1(inp):
    adapters = [int(line) for line in inp.splitlines()]
    adapters = [0] + sorted(adapters) + [max(adapters)+3]
    diffs = [b-a for (a,b) in zip(adapters, adapters[1:])]

    return diffs.count(1) * diffs.count(3)


def part2(inp):
    adapters = [int(line) for line in inp.splitlines()]
    adapters = [0] + sorted(adapters) + [max(adapters)+3]

    paths = collections.defaultdict(int)
    paths[0] = 1

    for adapter in adapters:
        for diff in range(1,4):
            next_adapter = adapter + diff
            if next_adapter in adapters:
                paths[next_adapter] += paths[adapter]

    return paths[adapter]

