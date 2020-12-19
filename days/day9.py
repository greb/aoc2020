def validate_num(num, pre):
    for i, a in enumerate(pre):
        for b in pre[i+1:]:
            s = a+b
            if s == num and a != b:
                return True
    return False


def part1(inp):
    inp = [int(line) for line in inp.splitlines()]

    for i, num in enumerate(inp[25:]):
        pre = inp[i:i+25]
        if not validate_num(num, pre):
            return num

def part2(inp):
    target = part1(inp)
    inp = [int(line) for line in inp.splitlines()]

    for i in range(len(inp)):
        segment_sum = 0
        for j in range(i, len(inp)):
            segment_sum += inp[j]
            if segment_sum > target:
                break

            if segment_sum == target:
                segment = inp[i:j+1]
                if len(segment) < 2:
                    break

                return min(segment) + max(segment)


