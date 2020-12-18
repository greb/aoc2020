import re

'''
def parse_expr(expr, pred=False):
    out = []
    ops = []

    for ch in expr:
        if ch.isspace():
            continue

        if ch.isdigit():
            out.append(int(ch))
            if ops and ops[-1] != '(':
                out.append(ops.pop())

        elif ch in '+*(':
            ops.append(ch)

        elif ch == ')':
            assert ops.pop() == '('
            if ops and ops[-1] != '(':
                out.append(ops.pop())

    return out


def rpn(tokens):
    stack = []

    for token in tokens:
        if isinstance(token, int):
            stack.append(token)
            continue

        a, b = stack.pop(), stack.pop()
        if token == '+':
            stack.append(a+b)
        elif token == '*':
            stack.append(a*b)

    return stack.pop()
'''

def apply_operator(ops, vals):
    op  = ops.pop()
    rhs = vals.pop()
    lhs = vals.pop()

    if op == '+':
        val = lhs + rhs
    elif op == '*':
        val = lhs * rhs
    vals.append(val)

def evaluate(expr, pred=None):
    tokens = re.findall(r'(\S)', expr)

    vals = []
    ops = []

    for token in tokens:
        if token.isdigit():
            vals.append(int(token))
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                apply_operator(ops, vals)
            assert ops.pop() == '('
        else:
            while (ops and ops[-1] != '(' and
                    (not pred or pred[ops[-1]] > pred[token])):
                apply_operator(ops, vals)
            ops.append(token)

    while ops:
        apply_operator(ops, vals)

    return vals.pop()

def solve_part1(inp):
    total = 0
    for line in inp.splitlines():
        total += evaluate(line)
    return total

def solve_part2(inp):
    pred = {'+': 1, '*': 0}
    total = 0
    for line in inp.splitlines():
        total += evaluate(line, pred)
    return total
