import re

def parse(inp):
    pattern = re.compile(r'(\d*)-(\d*) (.): (.*)')
    return pattern.findall(inp)

def part1(inp):
    inp = parse(inp)

    correct_cnt = 0
    for lo, hi, ch, pw in inp:
        cnt = pw.count(ch)
        lo = int(lo)
        hi = int(hi)

        if lo <= cnt <= hi:
            correct_cnt += 1

    return correct_cnt


def part2(inp):
    inp = parse(inp)

    correct_cnt = 0
    for lo, hi, ch, pw in inp:
        lo = pw[int(lo) - 1] == ch
        hi = pw[int(hi) - 1] == ch

        if (lo and not hi) or (not lo and hi):
            correct_cnt += 1

    return correct_cnt

