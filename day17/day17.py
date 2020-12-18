#!/usr/bin/env python3
from collections import namedtuple
from itertools import product
from operator import itemgetter

Range = namedtuple('Range', 'min max')


def bounds(cells, dim):
    for d in range(dim):
        yield Range(
            min(map(itemgetter(d), (c for c in cells))), 
            max(map(itemgetter(d), (c for c in cells)))
            )


def count_neigbours(cells, c):
    count, ranges = 0, ((cc - 1, cc, cc + 1) for cc in c)
    count = sum(cc in cells for cc in product(*ranges))
    count -= c in cells
    return count


def tick(cells, rx, ry, rz):
    new_cells = set()
    for x in range(rx.min -1, rx.max + 2):
        for y in range(ry.min -1, ry.max + 2):
            for z in range(rz.min -1, rz.max + 2):
                c = (x, y, z)
                n = count_neigbours(cells, c)
                if (c in cells and n in (2, 3)) or n == 3:
                    new_cells.add(c)
    return new_cells


def tick4(cells, rx, ry, rz, rw):
    new_cells = set()
    for x in range(rx.min -1, rx.max + 2):
        for y in range(ry.min -1, ry.max + 2):
            for z in range(rz.min -1, rz.max + 2):
                for w in range(rw.min -1, rw.max + 2):
                    c = (x, y, z, w)
                    n = count_neigbours(cells, c)
                    if (c in cells and n in (2,3)) or n == 3:
                        new_cells.add(c)
    return new_cells


def solve_part_1(cells):
    for _ in range(6):
        rx, ry, rz = (b for b in bounds(cells, 3))
        cells = tick(cells, rx, ry, rz)
    return len(cells)


def solve_part_2(cells):
    for _ in range(6):
        rx, ry, rz, rw = (b for b in bounds(cells, 4))
        cells = tick4(cells, rx, ry, rz, rw)
    return len(cells)


if __name__ == "__main__":
    part_1, part_2 = set(), set()
    for y, l in enumerate(open('input.txt').readlines()):
        for x, c in enumerate(l.rstrip()):
            if c == '#':
                part_1.add((x, y, 0))
                part_2.add((x, y, 0, 0))
    print(f'{solve_part_1(part_1)}, {solve_part_2(part_2)}')
