import argparse
import importlib
import os
import os.path
import sys

import requests

year = 2020
input_dir = 'inputs'

def fetch_input(day, forced=False):
    if not os.path.exists(input_dir):
        os.mkdir(input_dir)

    input_file = os.path.join(input_dir, str(day))
    if forced or not os.path.exists(input_file):
        if not os.path.exists('session'):
            raise Exception('Missing session token file')

        with open('session', 'tr') as token_file:
            session_token = token_file.read().strip()

        input_url = f'https://adventofcode.com/{year}/day/{day}/input'
        cookies = {'session': session_token}

        with requests.get(input_url, cookies=cookies) as resp:
            resp.raise_for_status()
            with open(input_file, 'wb') as input_handle:
                input_handle.write(resp.content)

    with open(input_file, 'rt') as input_handle:
        return input_handle.read()

def load_day(day):
    module_name = f'days.day{day}'
    module = importlib.import_module(module_name)
    return module

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['dump', 'run'])
    parser.add_argument('-f', '--force-fetch', action='store_true')
    parser.add_argument('day', type=int, choices=range(1,26),
        help='Solve day number N')

    args = parser.parse_args()
    inp = fetch_input(args.day, args.force_fetch)

    if args.command == 'run':
        day = load_day(args.day)

        if hasattr(day, 'solve_part1'):
            print(day.solve_part1(inp))

        if hasattr(day, 'solve_part2'):
            print(day.solve_part2(inp))

    elif args.command == 'dump':
        for line in inp.splitlines():
            print(line)
