#!/usr/bin/env python3
deltas = (
    (-1, -1), (-1,  0), (-1,  1),
    ( 0, -1),           ( 0,  1),
    ( 1, -1), ( 1,  0), ( 1,  1)
)

def count_neighbours(seats, r, c, max_r, max_c):
    count = 0
    for dr, dc in deltas:
        i, j = r + dr, c + dc
        if 0 <= i < max_r and 0 <= j < max_c:
            count += seats[i][j] == '#'
    return count


def count_neighbours_los(seats, r, c, max_r, max_c):
    count = 0
    for dr, dc in deltas:
        i, j = r + dr, c + dc
        while 0 <= i < max_r and 0 <= j < max_c:
            if seats[i][j] != '.':
                count += seats[i][j] == '#'
                break;
            i, j = i + dr, j + dc
    return count


def evolve(seats, threshold, counter):
    rows, columns = len(seats), len(seats[0])
    next_ = [''] * rows
    did_change = False
    for r in range(0, rows):
        for c in range(0, columns):
            count = counter(seats, r, c, rows, columns)
            if seats[r][c] == '.':
                next_[r] += '.'
            elif seats[r][c] == 'L' and count == 0:
                next_[r] += '#'
                did_change |= True
            elif seats[r][c] == '#' and count >= threshold:
                next_[r] += 'L'
                did_change |= True
            else:
                next_[r] += seats[r][c]
    return next_, did_change


def solve_part_1(seats):
    did_change = True
    while did_change:
        seats, did_change = evolve(seats, 4, count_neighbours)
    return sum(r.count('#') for r in seats)


def solve_part_2(seats):
    did_change = True
    while did_change:
        seats, did_change = evolve(seats, 5, count_neighbours_los)
    return sum(r.count('#') for r in seats)


if __name__ == "__main__":
    seats = [l.rstrip() for l in open('input.txt').readlines()]
    print(f'{solve_part_1(seats)}, {solve_part_2(seats)}')
