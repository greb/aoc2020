def part1(inp):
    entries = sorted(int(e) for e in inp.split())

    for i, a in enumerate(entries):
        for b in entries[i+1:]:
            if a+b == 2020:
                return a*b

def part2(inp):
    entries = sorted(int(e) for e in inp.split())

    for i, a in enumerate(entries):
        for j, b in enumerate(entries[i+1:]):
            for c in entries[j+1:]:
                s = a+b+c
                if s > 2020:
                    break
                if s == 2020:
                    return a*b*c
