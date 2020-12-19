dirs = {'N': (0, -1), 'S': (0, 1),
        'E': (1, 0), 'W': (-1, 0)}

compass = ['N', 'E', 'S', 'W']

def move(pos, d, value):
    x = pos[0] + value * d[0]
    y = pos[1] + value * d[1]
    return (x,y)

def turn(d, action, value):
    value //= 90
    idx = compass.index(d)
    if action == 'R':
        idx = (idx+value) % 4
    elif action == 'L':
        idx = idx - value
    return compass[idx]

def turn_waypoint(pos, action, value):
    value //= 90
    x, y = pos

    for _ in range(value):
        if action == 'R':
            x, y = -y, x
        elif action == 'L':
            x, y = y, -x
    return x, y


def part1(inp):
    ship_dir = 'E'
    ship_pos = (0,0)

    for step in inp.splitlines():
        action = step[0]
        value  = int(step[1:])

        if action in dirs:
            ship_pos = move(ship_pos, dirs[action], value)
        elif action == 'F':
            ship_pos = move(ship_pos, dirs[ship_dir], value)
        else:
            ship_dir = turn(ship_dir, action, value)

    return abs(ship_pos[0]) + abs(ship_pos[1])


def part2(inp):
    ship_pos = (0,0)
    waypoint_pos = (10, -1)

    for step in inp.splitlines():
        action = step[0]
        value  = int(step[1:])

        if action in dirs:
            waypoint_pos = move(waypoint_pos, dirs[action], value)
        elif action == 'F':
            ship_pos = move(ship_pos, waypoint_pos, value)
        else:
            waypoint_pos = turn_waypoint(waypoint_pos, action, value)

    return abs(ship_pos[0]) + abs(ship_pos[1])
