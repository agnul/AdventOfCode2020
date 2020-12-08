#!/usr/bin/env python3
opcodes = {
    'acc': lambda op, ip, acc: (ip + 1, acc + op),
    'jmp': lambda op, ip, acc: (ip + op, acc),
    'nop': lambda op, ip, acc: (ip + 1, acc)
}

def run(program):
    ip, acc, seen = 0, 0, []
    while ip not in seen and ip < len(program):
        seen.append(ip)
        op, arg = program[ip].split()
        ip, acc = opcodes[op](int(arg), ip, acc)
    return (ip, acc)


def patch(program, addr):
    p = program.copy()
    p[addr] = 'jmp' + p[addr][3:] if p[addr][:3] == 'nop' else 'nop' + p[addr][3:]
    return p


def solve_part_1(program):
    return run(program)[1]


def solve_part_2(program):
    possible_fixes = [addr for addr, op in enumerate(program) if op[:3] in ('nop',  'jmp')]
    ip, acc, = 0, 0
    while ip < len(program) and len(possible_fixes) != 0:
        p = patch(program, possible_fixes.pop())
        ip, acc = run(p)

    return acc if ip >= len(p) else -1


if __name__ == "__main__":
    program = [l.rstrip() for l in open('input.txt').readlines()]
    print(f'{solve_part_1(program)}, {solve_part_2(program)}')
