class Layout:
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
            (1, 1), (1, 0), (1, -1), (0, -1)]

    def __init__(self, inp):
        self.layout = list(inp.splitlines())
        self.h      = len(self.layout)
        self.w      = len(self.layout[0])

    def count_occupied(self):
        cnt = 0
        for row in self.layout:
            for seat in row:
                if seat == '#':
                    cnt += 1
        return cnt


    def count_far_neighbors(self, cy, cx):
        cnt = 0
        for dy, dx in self.dirs:
            y, x = cy + dy, cx + dx
            while 0 <= y < self.h and 0 <= x < self.h:
                if self.layout[y][x] == '#':
                    cnt += 1
                    break
                elif self.layout[y][x] == 'L':
                    break
                y, x = y + dy, x + dx
        return cnt


    def count_occupied_neighbors(self, cy, cx):
        cnt = 0
        for dy, dx in self.dirs:
            y, x = cy + dy, cx + dx
            if (0 <= y < self.h and 0 <= x < self.w and
                    self.layout[y][x] == '#'):
                cnt += 1
        return cnt

    def apply_round(self, part2=False):
        new_layout = []
        change_cnt = 0

        for y, row in enumerate(self.layout):
            new_row = ['.'] * len(row)
            for x, seat in enumerate(row):
                if seat == '.':
                    continue

                if part2:
                    limit = 5
                    cnt = self.count_far_neighbors(y, x)
                else:
                    limit = 4
                    cnt = self.count_occupied_neighbors(y, x)

                if seat == 'L' and cnt == 0:
                    new_row[x] = '#'
                    change_cnt += 1
                elif seat == '#' and cnt >= limit:
                    new_row[x] = 'L'
                    change_cnt += 1
                else:
                    new_row[x] = seat

            new_layout.append(''.join(new_row))

        self.layout = new_layout
        return change_cnt


def solve_part1(inp):
    layout = Layout(inp)

    while True:
        change_cnt = layout.apply_round()
        if change_cnt == 0:
            break

    return layout.count_occupied()


def solve_part2(inp):
    layout = Layout(inp)

    while True:
        change_cnt = layout.apply_round(part2=True)
        if change_cnt == 0:
            break

    return layout.count_occupied()
