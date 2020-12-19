import re

mask_re = re.compile(r'mask = ([X01]*)')
mem_re  = re.compile(r'mem\[(\d*)\] = (\d*)')

def parse(inp):
    masks = []
    mems  = []

    current_mask = None
    for line in inp.splitlines():
        if match := mask_re.match(line):
            if current_mask:
                masks.append( (current_mask, mems) )
                mems = []
            current_mask = match.group(1)

        elif match := mem_re.match(line):
            addr = int(match.group(1))
            val  = int(match.group(2))
            mems.append((addr, val))

    masks.append( (current_mask, mems) )

    return masks

def bits_to_int(bits):
    m = 0
    for b in reversed(bits):
        m <<= 1
        m |= b
    return m

def apply_mask(mask, n):
    bits = []
    for d in reversed(mask):
        if d == 'X':
            bits.append(n & 1)
        elif d == '1':
            bits.append(1)
        else:
            bits.append(0)
        n >>= 1

    return bits_to_int(bits)

def decode_addr(mask, n):
    bits = []
    for d in reversed(mask):
        if d == 'X':
            bits.append(d)
        elif d == '1':
            bits.append(1)
        else:
            bits.append(n & 1)
        n >>= 1

    addrs = []
    canidates = [bits]

    while canidates:
        canidate = canidates.pop()

        if 'X' in canidate:
            idx = canidate.index('X')

            canidate[idx] = 0
            canidates.append(canidate)

            canidate = canidate.copy()
            canidate[idx] = 1
            canidates.append(canidate)
        else:
            addrs.append(bits_to_int(canidate))

    return addrs


def part1(inp):
    memory = {}

    for mask, mems in parse(inp):
        for addr, val in mems:
            memory[addr] = apply_mask(mask, val)

    return sum(memory.values())

def part2(inp):
    memory = {}

    for mask, mems in parse(inp):
        for addr, val in mems:
            for decoded in decode_addr(mask, addr):
                memory[decoded] = val

    return sum(memory.values())
