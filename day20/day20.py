#!/usr/bin/env python3
from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul

ID, N, E, S, W, NP, EP, SP, WP = 'id', 'n', 'e', 's', 'w', 'np', 'ep', 'sp', 'wp'

def parse_input(infile):
    tiles = []
    raw_tiles = open(infile).read().split('\n\n')
    for r in raw_tiles:
        id, *rows = r.splitlines()
        t = dict()
        t[ID] = id[5:-1]
        t[N], t[NP] = rows[0], rows[0][::-1]
        t[E] = ''.join(rr[-1] for rr in rows)
        t[EP] = ''.join(rr[-1] for rr in rows[::-1])
        t[S], t[SP] = rows[-1], rows[-1][::-1]
        t[W] = ''.join(rr[0] for rr in rows)
        t[WP] = ''.join(rr[0] for rr in rows[::-1])
        tiles.append(t)
    return tiles


def edges(tile):
    for e in N, E, S, W:
        yield tile[e]
        yield tile[e][::-1]

def solve_part_1(tiles):
    neighbours = defaultdict(lambda: 0)
    for t1, t2 in combinations(tiles, 2):
        if any((v1, v2) for v1 in t1.values() for v2 in t2.values() if v1 == v2):
            neighbours[t1[ID]] += 1
            neighbours[t2[ID]] += 1
    corners = [int(k) for k,v in neighbours.items() if v == 2]
    return reduce(mul, corners)


def solve_part_2():
    pass


if __name__ == "__main__":
    tiles = parse_input('input.txt')
    print(f'{solve_part_1(tiles)}, {solve_part_2()}')
