def parse(inp):
    inp = list(inp.splitlines())

    timestamp = int(inp[0])
    buses = list(inp[1].split(','))
    return timestamp, buses

def solve_part1(inp):
    timestamp, buses = parse(inp)
    buses = [int(bus) for bus in buses if bus != 'x']

    earliest = min((bus * (timestamp // bus + 1), bus) for bus in buses)
    return (earliest[0]-timestamp) * earliest[1]


def solve_part2(inp):
    _, buses = parse(inp)
    offsets = [(i, int(bus)) for i,bus in enumerate(buses) if bus != 'x']

    step = 1
    timestamp = 0
    for offset, bus in offsets:
        while (timestamp + offset) % bus != 0:
            timestamp += step
        step *= bus
    return timestamp
