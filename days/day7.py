def parse_rules(inp):
    rules = dict()
    for line in inp.splitlines():
        segs = line.split()
        container = segs[0] + ' ' + segs[1]

        offset = 4
        bags = []
        while offset < len(segs):
            amount = segs[offset]
            if amount == 'no':
                break
            bag = segs[offset+1] + ' ' + segs[offset+2]
            bags.append((int(amount), bag))
            offset += 4

        rules[container] = bags
    return rules

def solve_part1(inp):
    rules = parse_rules(inp)
    stack = ['shiny gold']
    visited = set()

    cnt = 0
    while stack:
        current = stack.pop()
        for container, bags in rules.items():
            if container in visited:
                continue

            for _, bag in bags:
                if current == bag:
                    stack.append(container)
                    visited.add(container)
                    cnt += 1
    return cnt


def solve_part2(inp):
    rules = parse_rules(inp)
    stack = [(1, 'shiny gold')]

    cnt = 0
    while stack:
        mult, container = stack.pop()

        for bag_cnt, bag in rules[container]:
            bag_cnt *= mult
            cnt += bag_cnt
            stack.append((bag_cnt, bag))

    return cnt
