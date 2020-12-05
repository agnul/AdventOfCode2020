#!/usr/bin/env python3
def find_seat_id(boarding_pass):
    lo, hi = 0, 1024
    for c in boarding_pass:
        m = int((lo + hi) / 2)
        (lo, hi) = (lo, m) if c == 'F' or c == 'L' else (m, hi)
    return lo

def solve_part_1(boarding_passes):
    return max([find_seat_id(p) for p in boarding_passes])


def solve_part_2(boarding_passes):
    seats = [0] * 1024
    for p in boarding_passes:
        seats[find_seat_id(p)] = 1
    for i in range(1, 1023):
        if seats[i - 1:i + 2] == [1, 0, 1]:
            return i
    return -1


if __name__ == "__main__":
    passes = [l.rstrip() for l in open('input.txt').readlines()]
    print(f'{solve_part_1(passes)}, {solve_part_2(passes)}')
