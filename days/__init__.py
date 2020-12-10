import importlib
import os
import os.path

import requests

input_dir = 'inputs'

def fetch_input(day, forced=False):
    if not os.path.exists(input_dir):
        os.mkdir(input_dir)

    input_file = os.path.join(input_dir, str(day))
    if os.path.exists(input_file) and not forced:
        return

    if not os.path.exists('session'):
        raise Exception('Missing session token file')

    with open('session', 'tr') as token_file:
        session_token = token_file.read().strip()

    input_url = f'https://adventofcode.com/2020/day/{day}/input'
    cookies = {'session': session_token}

    with requests.get(input_url, cookies=cookies) as resp:
        resp.raise_for_status()
        with open(input_file, 'wb') as input_handle:
            input_handle.write(resp.content)

def get_input(day):
    fetch_input(day)
    input_file = os.path.join(input_dir, str(day))
    with open(input_file, 'rt') as input_handle:
        return input_handle.read()

def load_day(day):
    module_name = f'days.day{day}'
    module = importlib.import_module(module_name)
    return module
