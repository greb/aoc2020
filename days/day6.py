def parse_groups(inp):
    group = list()
    for line in inp.splitlines():
        if not line:
            yield group
            group = list()
        else:
            group.append(line)
    yield group


def part1(inp):
    cnt = 0

    for group in parse_groups(inp):
        ans = set()
        for g in group:
            ans.update(g)
        cnt += len(ans)
    return cnt

def part2(inp):
    cnt = 0

    for group in parse_groups(inp):
        ans = set(group[0])
        for g in group:
            ans.intersection_update(g)
        cnt += len(ans)
    return cnt


