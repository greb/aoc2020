import argparse
import os
import os.path


import days

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['run', 'fetch'])
    parser.add_argument('day', type=int, choices=range(1,26),
        help='Solve day number N')

    args = parser.parse_args()

    if args.command == 'run':
        inp = days.get_input(args.day)

        day = days.load_day(args.day)
        if hasattr(day, 'solve_part1'):
            print(day.solve_part1(inp))
        
        if hasattr(day, 'solve_part2'):
            print(day.solve_part2(inp))

