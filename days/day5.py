def decode_partion(part):
    n = 0
    for c in part:
        n *= 2
        if c in ['B', 'R']:
            n += 1
    return n

def get_row_col(line):
    row = decode_partion(line[:7])
    col = decode_partion(line[7:])
    return row, col

def get_seat_id(row, col):
    return row*8 + col

def parse(inp):
    for line in inp.splitlines():
        row, col = get_row_col(line)
        seat_id = get_seat_id(row, col)
        yield seat_id

def solve_part1(inp):
    seat_ids = parse(inp)
    return max(seat_ids)

def solve_part2(inp):
    seat_ids = list(parse(inp))
    start = min(seat_ids)
    end = max(seat_ids)

    for seat_id in range(start, end):
        if seat_id in seat_ids:
            continue
        return seat_id
