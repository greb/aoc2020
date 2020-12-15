from collections import defaultdict

def solve_part1(inp):
    nums = [int(n) for n in inp.split(',')]

    memory = {}
    for turn in range(2020):
        if turn < len(nums):
            spoken = nums[turn]
        elif recent is None:
            spoken = 0
        else:
            spoken = turn - (recent + 1)

        recent = memory.get(spoken)
        memory[spoken] = turn

    return spoken


def solve_part2(inp):
    nums = [int(n) for n in inp.split(',')]

    memory = {}
    for turn in range(30000000):
        if turn < len(nums):
            spoken = nums[turn]
        elif recent is None:
            spoken = 0
        else:
            spoken = turn - (recent + 1)

        recent = memory.get(spoken)
        memory[spoken] = turn

    return spoken


