import re
import collections

def parse(inp):
    rules = {}
    tickets = []
    rule_pattern = re.compile(r'([a-z ]*): (\d*)-(\d*) or (\d*)-(\d*)')

    parsing_rules = True
    for line in inp.splitlines():
        if m := rule_pattern.match(line):
            rules[m[1]] = [int(n) for n in m.groups()[1:]]
        elif line and line[0].isdigit():
            ticket = [int(n) for n in line.split(',')]
            tickets.append(ticket)
    return rules, tickets


def check_value(val, bounds):
    a1, a2, b1, b2 = bounds
    return a1 <= val <= a2 or b1 <= val <= b2


def ticket_errors(rules, ticket):
    errors = 0

    for val in ticket:
        checks = (check_value(val, b) for b in rules.values())
        if not any(checks):
            errors += val

    return errors


def part1(inp):
    rules, tickets = parse(inp)

    errors = 0
    for ticket in tickets[1:]:
        errors += ticket_errors(rules, ticket)

    return errors


def part2(inp):
    rules, tickets = parse(inp)

    valids = []
    for ticket in tickets:
        if not ticket_errors(rules, ticket):
            valids.append(ticket)

    canidates = collections.defaultdict(set)
    for row in range(len(valids[0])):
        row_vals = [v[row] for v in valids]
        for rule, bounds in rules.items():
            if all(check_value(v, bounds) for v in row_vals):
                canidates[rule].add(row)

    canidates = sorted(canidates.items(), key=lambda c: len(c[1]))
    checked_rows = set()
    answer = 1
    for rule, rows in canidates:
        row = (rows - checked_rows).pop()
        checked_rows.add(row)

        if rule.startswith('departure'):
            answer *= tickets[0][row]

    return answer

