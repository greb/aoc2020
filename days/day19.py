def parse(inp):
    rules = {}
    lines = inp.splitlines()
    for i, line in enumerate(lines):
        if not line:
            break
        rule, terms = line.split(': ')
        if terms[0] == '"':
            rules[int(rule)] = terms[1]
        else:
            rules[int(rule)] = [[int(n) for n in t.split()]
                    for t in terms.split(' | ')]

    return rules, lines[i+1:]


def check_msg(msg, check, rules):
    if not msg:
        return len(check) == 0

    if len(check) == 0:
        return False

    terms = rules[check[0]]
    if isinstance(terms, str):
        if msg[0] == terms:
            return check_msg(msg[1:], check[1:], rules)
        return False
    else:
        for term in terms:
            if check_msg(msg, term + check[1:], rules):
                return True
        return False

def solve_part1(inp):
    rules, msgs = parse(inp)
    return sum(check_msg(msg, [0], rules) for msg in msgs)


def solve_part2(inp):
    rules, msgs = parse(inp)
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]
    return sum(check_msg(msg, [0], rules) for msg in msgs)
