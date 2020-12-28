#!/usr/bin/env python3
def pick(succ, cur):
    return [succ[cur], succ[succ[cur]], succ[succ[succ[cur]]]]


def find_destination(c, picked, max=9):
    d = c - 1 if c > 1 else max
    while d in picked:
        d = d - 1 if d > 1 else max
    return d


def play(succ, rounds, max=9):
    cur = cups[0]
    for _ in range(rounds):
        picked = pick(succ, cur)
        dst = find_destination(cur, picked, max)
        succ[cur] = succ[picked[-1]]
        succ[dst], succ[picked[-1]] = picked[0], succ[dst]
        cur = succ[cur]
    return succ


def solve_part_1(cups):
    succ = [None] * (len(cups) + 1)
    for p, n in zip(cups, cups[1:] + [cups[0]]): succ[p] = n

    succ = play(succ, 100)

    res = [succ[1]]
    for _ in range(7):
        res.append(succ[res[-1]])
    return ''.join(map(str, res))


def solve_part_2(cups):
    succ = [None] * (1_000_000 + 1)
    for p, n in zip(cups, cups[1:] + [cups[0]]):
        succ[p] = n if n != cups[0] else 10
    for i in range(10, 1_000_000): succ[i] = i + 1
    succ[-1] = cups[0]

    succ = play(succ, 10_000_000, 1_000_000)

    return succ[1] * succ[succ[1]]


if __name__ == "__main__":
    cups = list(map(int, (c for c in '186524973')))
    print(f'{solve_part_1(cups)}, {solve_part_2(cups)}')
