import re

req_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

passport_re = re.compile(r'(\S{3}):(\S*)')
hgt_re = re.compile(r'(\d*)(cm|in)')
hcl_re = re.compile(r'#[0-9a-f]{6}')
ecl_valid = set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])
pid_re = re.compile(r'[0-9]{9}$')

def parse(inp):
    passport = dict()

    for line in inp.splitlines():
        items = passport_re.findall(line)

        if not items:
            yield passport
            passport = dict()
        else:
            passport.update(items)
    yield passport

def part1(inp):
    valid_cnt = 0

    passports = parse(inp)
    for p in passports:
        if req_fields.issubset(p):
            valid_cnt += 1
    return valid_cnt


def part2(inp):
    valid_cnt = 0

    passports = parse(inp)
    for p in passports:
        if not req_fields.issubset(p):
            continue

        if not (1920 <= int(p['byr']) <= 2002):
            continue

        if not (2010 <= int(p['iyr']) <= 2020):
            continue

        if not (2020 <= int(p['eyr']) <= 2030):
            continue

        hgt_match = hgt_re.match(p['hgt'])
        if not hgt_match:
            continue

        hgt_val, hgt_unit = hgt_match.groups()
        if hgt_unit == 'cm':
            if not (150 <= int(hgt_val) <= 193):
                continue
        else:
            if not (59 <= int(hgt_val) <= 76):
                continue

        if not hcl_re.match(p['hcl']):
            continue

        if p['ecl'] not in ecl_valid:
            continue

        if not pid_re.match(p['pid']):
            continue

        valid_cnt += 1
    return valid_cnt
