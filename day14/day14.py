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


def all_addresses(addr):
    float_count, bin_addr = 0, '{:036b}'.format(addr)
    for i in range(36):
        if i not in mask:
            bin_addr = bin_addr[:i] + 'X' + bin_addr[i+1:]
            float_count += 1
        elif mask[i] == '1':
            bin_addr = bin_addr[:i] + '1' + bin_addr[i+1:]
    for n in range(2 ** float_count):
        bits = '{:b}'.format(n).rjust(float_count, '0')
        new_addr = bin_addr
        for b in bits:
            new_addr = new_addr.replace('X', b, 1)
        yield int(new_addr, 2)


def solve_part_1(program):
    for op, *args in program:
        if op == 'mask':
            set_mask(*args)
        else:
            poke(*args)
    return sum(v for v in memory.values() if v != 0)


def solve_part_2(program):
    memory.clear()
    for op, *args in program:
        if op == 'mask':
            set_mask(*args)
        else:
            for a in all_addresses(args[0]):
                memory[a] = args[1]
    return sum(v for v in memory.values() if v != 0)


if __name__ == "__main__":
    program = [parse(line.rstrip()) for line in open('test.txt').readlines()]
    print(f'{solve_part_1(program)}, {solve_part_2(program)}')
