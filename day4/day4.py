#!/usr/bin/env python3
from re import match, IGNORECASE

required_fields = [
    ('byr', lambda y: match(r'\d{4}', y) and between(y, 1920, 2002)),
    ('iyr', lambda y: match(r'\d{4}', y) and between(y, 2010, 2020)), 
    ('eyr', lambda y: match(r'\d{4}', y) and between(y, 2020, 2030)), 
    ('hgt', lambda h: match(r'\d+(in|cm)', h, IGNORECASE) and (between(h[:-2], 150, 193) if h[-2:] == 'cm' else between(h[:-2], 59, 76))), 
    ('hcl', lambda c: match(r'#[0-9a-f]{6}', c, IGNORECASE)), 
    ('ecl', lambda c: c.lower() in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')),
    ('pid', lambda i: match(r'^\d{9}$', i))
    ]

def between(s, lo, hi):
    return lo <= int(s) and int(s) <= hi


def parse_passports(infile):
    passports, p = [], dict()

    for l in map(str.rstrip, open(infile).readlines()):
        if len(l) == 0:
            passports.append(p)
            p = dict()
        for k, v in [kv.split(':') for kv in l.split()]:
            p[k] = v
    passports.append(p)
    return passports


def has_required_fields(passport):
    for (f, _) in required_fields:
        if f not in passport:
            return False
    return True


def has_valid_required_fields(passport):
    for k, is_valid in required_fields:
        if k not in passport or not is_valid(passport[k]):
            return False
    return True


def solve_part_1(passports):
    return len([p for p in passports if has_required_fields(p)])


def solve_part_2(passports):
    return len([p for p in passports if has_valid_required_fields(p)])


if __name__ == "__main__":
    passports = parse_passports('input.txt')
    print(f'{solve_part_1(passports)}, {solve_part_2(passports)}')
