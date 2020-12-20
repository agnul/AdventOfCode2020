#!/usr/bin/env python3

# Expr := Op
# Op := Val (('+'|'*') Val)*
# Val := n | '(' Expr ')'
def Op(line, i):
    ii, v1 = Val(line, i, Op)
    while ii < len(line) and line[ii] in ('+', '*'):
        if line[ii] == '+':
            ii, v2 = Val(line, ii + 1, Op)
            v1 += v2
        elif line[ii] == '*':
            ii, v2 = Val(line, ii + 1, Op)
            v1 *= v2
    return ii, v1 

# Expr := Prod 
# Prod := Sum ('*' Sum)*
# Sum := Val ('+' Val)*
# Val := n | '(' Expr ')' 
def Prod(line, i = 0):
    ii, v1 = Sum(line, i)
    while ii < len(line) and line[ii] == '*':
        if line[ii] == '*':
            ii, v2 = Sum(line, ii + 1)
            v1 *= v2
    return ii, v1
    

def Sum(line, i = 0):
    ii, v1 = Val(line, i, Prod)
    while ii < len(line):
        if line[ii] == '+':
            ii, v2 = Val(line, ii + 1, Prod)
            v1 += v2
        else:
            break
    return ii, v1


def Val(line, i, Expr):
    sym = line[i]
    if sym == '(':
        ii, vv = Expr(line, i + 1)
        return expect(line, ii, vv, ')')
    else:
        return i + 1, int(sym)


def expect(line, i, val, sym):
    if i >= len(line) or line[i] != sym:
        raise Exception(f'Invalid expression {line}, unbalanced PAREN error at pos {i}')
    else:
        return i + 1, val


def solve_part_1(operations):
    sum = 0
    for op in operations:
        op = op.replace('(', '( ')
        op = op.replace(')', ' )')

        i, val, = 0, 0
        while i < len(op.split()):
            i, val = Op(op.split(), i)
        sum += val
    return sum


def solve_part_2(operations):
    sum = 0
    for op in operations:
        op = op.replace('(', '( ')
        op = op.replace(')', ' )')

        i, val = 0, 0
        while i < len(op.split()):
            i, val = Prod(op.split(), i)
        sum += val
    return sum


if __name__ == "__main__":
    operations = [line.rstrip() for line in open('input.txt').readlines()]
    print(f'{solve_part_1(operations)}, {solve_part_2(operations)}')
