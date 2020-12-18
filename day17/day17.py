#!/usr/bin/env python3
from collections import namedtuple
from itertools import product

Delta = namedtuple('Delta', 'x y z')
Delta4 = namedtuple('Delta', 'x y z w')
Range = namedtuple('Range', 'min max')
Cell = namedtuple('Cell', 'x y z')
Cell4 = namedtuple('Cell', 'x y z w')


#deltas = (
#    Delta(-1, -1, -1), Delta(-1,  0, -1), Delta(-1,  1, -1),
#    Delta( 0, -1, -1), Delta( 0,  0, -1), Delta( 0,  1, -1),
#    Delta( 1, -1, -1), Delta( 1,  0, -1), Delta( 1,  1, -1),
#    Delta(-1, -1,  0), Delta(-1,  0,  0), Delta(-1,  1,  0),
#    Delta( 0, -1,  0),                    Delta( 0,  1,  0),
#    Delta( 1, -1,  0), Delta( 1,  0,  0), Delta( 1,  1,  0),
#    Delta(-1, -1,  1), Delta(-1,  0,  1), Delta(-1,  1,  1),
#    Delta( 0, -1,  1), Delta( 0,  0,  1), Delta( 0,  1,  1),
#    Delta( 1, -1,  1), Delta( 1,  0,  1), Delta( 1,  1,  1)
#)

deltas = [Delta(*d) for d in product(range(-1, 2), repeat=3)]
deltas4 = [Delta4(*d) for d in product(range(-1, 2), repeat=4)]

#dd = (Delta(*d) for d in product(range(-1, 2), repeat=3))


def count_neigbours(cells, c):
    count = 0
    for d in deltas:
        if d == (0, 0, 0): continue
        if Cell(c.x + d.x, c.y + d.y, c.z + d.z) in cells:
            count += 1
    return count


def count_neigbours4(cells, c):
    count = 0
    for d in deltas4:
        if d == (0, 0, 0, 0): continue
        if Cell4(c.x + d.x, c.y + d.y, c.z + d.z, c.w + d.w) in cells:
            count += 1
    return count


def tick(cells, rx, ry, rz):
    new_cells = set()
    for x in range(rx.min -1, rx.max + 2):
        for y in range(ry.min -1, ry.max + 2):
            for z in range(rz.min -1, rz.max + 2):
                c = Cell(x, y, z)
                n = count_neigbours(cells, c)
                if c in cells and (n == 2 or n == 3):
                    new_cells.add(c)
                elif c not in cells and n == 3:
                    new_cells.add(c)
    return new_cells


def tick4(cells, rx, ry, rz, rw):
    new_cells = set()
    for x in range(rx.min -1, rx.max + 2):
        for y in range(ry.min -1, ry.max + 2):
            for z in range(rz.min -1, rz.max + 2):
                for w in range(rw.min -1, rw.max + 2):
                    c = Cell4(x, y, z, w)
                    n = count_neigbours4(cells, c)
                    if c in cells and (n == 2 or n == 3):
                        new_cells.add(c)
                    elif c not in cells and n == 3:
                        new_cells.add(c)
    return new_cells


def solve_part_1(cells):
    for t in range(1, 7):
        rx = Range(min(c.x for c in cells), max(c.x for c in cells))
        ry = Range(min(c.y for c in cells), max(c.y for c in cells))
        rz = Range(min(c.z for c in cells), max(c.z for c in cells))
        cells = tick(cells, rx, ry, rz)
    return len(cells)


def solve_part_2(cells):
    for t in range(1, 7):
        rx = Range(min(c.x for c in cells), max(c.x for c in cells))
        ry = Range(min(c.y for c in cells), max(c.y for c in cells))
        rz = Range(min(c.z for c in cells), max(c.z for c in cells))
        rw = Range(min(c.w for c in cells), max(c.w for c in cells))
        cells = tick4(cells, rx, ry, rz, rw)
    return len(cells)


if __name__ == "__main__":
    cells, cells4 = set(), set()
    for y, l in enumerate(open('input.txt').readlines()):
        for x, c in enumerate(l.rstrip()):
            if c == '#':
                cells.add(Cell(x, y, 0))
                cells4.add(Cell4(x, y, 0, 0))
    print(f'{solve_part_1(cells)}, {solve_part_2(cells4)}')
