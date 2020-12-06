#!/usr/bin/env python3
def read_groups(infile):
    groups, g = [], []
    for l in map(str.rstrip, open(infile).readlines()):
        if len(l) == 0:
            groups.append(g)
            g = []
        else:
            g.append(l)
    groups.append(g)
    return groups


def solve_part_1(groups):
    any_answers = []
    for g in groups:
        g_answers = set(c for c in g[0])
        for a in g[1:]:
            g_answers |= set(c for c in a)
        any_answers.append(g_answers)

    return sum([len(a) for a in any_answers])
    

def solve_part_2(groups):
    all_answers = []
    for g in groups:
        g_answers = set(c for c in g[0])
        for a in g[1:]:
            g_answers &= set(c for c in a)
        all_answers.append(g_answers)
        
    return sum([len(a) for a in all_answers])


if __name__ == "__main__":
    groups = read_groups('input.txt')
    print(f'{solve_part_1(groups)}, {solve_part_2(groups)}')
