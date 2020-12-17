#!/usr/bin/env python3
from collections import namedtuple
from itertools import product

Delta = namedtuple('Delta', 'x y z')
Range = namedtuple('Range', 'min max')
Cell = namedtuple('Cell', 'x y z')

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

def count_neigbours(cells, c):
    count = 0
    for d in deltas:
        if d == (0, 0, 0): continue
        if Cell(c.x + d.x, c.y + d.y, c.z + d.z) in cells:
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


def solve_part_1(cells):
    for _ in range(1, 7):
        rx = Range(min(c.x for c in cells), max(c.x for c in cells))
        ry = Range(min(c.y for c in cells), max(c.y for c in cells))
        rz = Range(min(c.z for c in cells), max(c.z for c in cells))
        cells = tick(cells, rx, ry, rz)
    return len(cells)


def solve_part_2():
    pass


if __name__ == "__main__":
    cells = set()
    for y, l in enumerate(open('test.txt').readlines()):
        for x, c in enumerate(l.rstrip()):
            if c == '#':
                cells.add(Cell(x, y, 0))
    print(f'{solve_part_1(cells)}, {solve_part_2()}')
