#!/usr/bin/env python3
commands = {
    'F': lambda hdg, pos, arg: forward(hdg, *pos, arg),
    'N': lambda hdg, pos, arg: (hdg, (pos[0], pos[1] + arg)),
    'S': lambda hdg, pos, arg: (hdg, (pos[0], pos[1] - arg)),
    'E': lambda hdg, pos, arg: (hdg, (pos[0] + arg, pos[1])),
    'W': lambda hdg, pos, arg: (hdg, (pos[0] - arg, pos[1])),
    'R': lambda hdg, pos, arg: ((hdg + arg) % 360, pos),
    'L': lambda hdg, pos, arg: ((hdg - arg) % 360, pos),
}

wp_commands = {
    'F': lambda w, s, arg: (w, (s[0] + arg * w[0], s[1] + arg * w[1])),
    'N': lambda w, s, arg: ((w[0], w[1] + arg), s),
    'S': lambda w, s, arg: ((w[0], w[1] - arg), s),
    'E': lambda w, s, arg: ((w[0] + arg, w[1]), s),
    'W': lambda w, s, arg: ((w[0] - arg, w[1]), s),
    'R': lambda w, s, arg: (rotate(*w, arg), s),
    'L': lambda w, s, arg: (rotate(*w, -arg), s),
}


def forward(hdg, x, y, arg):
    if hdg == 0:
        return hdg, (x, y + arg)
    elif hdg == 90:
        return hdg, (x + arg, y)
    elif hdg == 180:
        return hdg, (x, y - arg)
    elif hdg == 270:
        return hdg, (x - arg, y)


def rotate(x, y, arg):
    if arg == 90 or arg == -270:
        return (y, -x)
    elif arg == 180 or arg == -180:
        return (-x, -y)
    elif arg == 270 or arg == -90:
        return (-y, x)


def solve_part_1(instr):
    heading, position = 90, (0, 0)
    for c, n in instr:
        heading, position = commands[c](heading, position, n)
    return abs(position[0]) + abs(position[1])


def solve_part_2(instr):
    waypoint, ship = (10, 1), (0, 0)
    for c, n in instr:
        waypoint, ship = wp_commands[c](waypoint, ship, n)
    return abs(ship[0]) + abs(ship[1])


if __name__ == "__main__":
    instr = [(ll[0], int(ll[1:])) for ll in open('input.txt').readlines()]
    print(f'{solve_part_1(instr)}, {solve_part_2(instr)}')
