#!/usr/bin/env python3
def parse(infile):
    lines = open(infile).read()
    deck_a, deck_b = lines.split("\n\n")
    deck_a = [int(c) for c in deck_a.splitlines()[1:]]
    deck_b = [int(c) for c in deck_b.splitlines()[1:]]
    return deck_a, deck_b


def hash(deck_a, deck_b):
    a = ','.join(map(str, deck_a))
    b = ','.join(map(str, deck_b))
    return f'{a}|{b}'


def play(deck_a, deck_b):
    while len(deck_a) and len(deck_b):
        a, deck_a = deck_a[0], deck_a[1:]
        b, deck_b = deck_b[0], deck_b[1:]
        if a > b:
            deck_a.append(a)
            deck_a.append(b)
        else:
            deck_b.append(b)
            deck_b.append(a)
    return ('A', deck_a) if len(deck_a) else ('B', deck_b)


def play_rec(deck_a, deck_b):
    seen = set()
    while len(deck_a) and len(deck_b):
        if hash(deck_a, deck_b) in seen:
            return ('A', deck_a)
        else:
            seen.add(hash(deck_a, deck_b))

        a, deck_a = deck_a[0], deck_a[1:]
        b, deck_b = deck_b[0], deck_b[1:]
        if a <= len(deck_a) and b <= len(deck_b):
            w, _ = play_rec(deck_a[:a], deck_b[:b])
        else:
            w = 'A' if a > b else 'B'

        if w == 'A':
            deck_a.append(a)
            deck_a.append(b)
        else:
            deck_b.append(b)
            deck_b.append(a)

    return ('A', deck_a) if len(deck_a) else ('B', deck_b)


def solve_part_1(deck_a, deck_b):
    _, winner = play(deck_a, deck_b)
    return sum((len(winner) - i) * c for i, c in enumerate(winner))


def solve_part_2(deck_a, deck_b):
    _, winner = play_rec(deck_a, deck_b)
    return sum((len(winner) - i) * c for i, c in enumerate(winner))


if __name__ == "__main__":
    deck_a, deck_b = parse('input.txt')
    print(f'{solve_part_1(deck_a, deck_b)}, {solve_part_2(deck_a,  deck_b)}')
