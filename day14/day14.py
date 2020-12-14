#!/usr/bin/env python3
import re

memory, mask = dict(), dict()


def parse(line):
    if line[:4] == 'mask':
        return ('mask', (line[7:]))
    else:
        return ('mem', *map(int, re.findall(r'\[(\d+)\] = (\d+)', line)[0]))


def set_mask(new_mask):
    mask.clear()
    for i, value in enumerate(new_mask):
        if value != 'X': mask[i] = value


def poke(addr, val):
    bin_str = '{:036b}'.format(val)
    for i, b in mask.items():
        bin_str = bin_str[:i] + b + bin_str[i+1:]
    memory[addr] = int(bin_str, 2)


def solve_part_1(program):
    for op, *args in program:
        if op == 'mask':
            set_mask(*args)
        else:
            poke(*args)
    return sum(v for v in memory.values() if v != 0)


def solve_part_2(program):
    pass


if __name__ == "__main__":
    program = [parse(line.rstrip()) for line in open('test.txt').readlines()]
    print(f'{solve_part_1(program)}, {solve_part_2(program)}')