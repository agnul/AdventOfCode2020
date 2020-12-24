#!/usr/bin/env python3
def parse(fname):
    rules, messages = dict(), []
    for ll in map(str.rstrip, open(fname).readlines()):
        if ': ' in ll:
            left, right = ll.replace('"', '').split(': ')
            if len(right) == 1:
                rules[left] = right
            else:
                rules[left] = [alt.split() for alt in right.split('|')]
        elif ll:
            messages.append(ll)
    return rules, messages


def consume_sequence(rules, sequence, message):
    """ Consume prefixes of message matching rules in sequence"""
    if not sequence:
        # no rules left to match, return whatever's left of message
        yield message
    else:
        s, *sequence = sequence
        # Consume prefixes matching first rule in sequence...
        for message in consume(rules, s, message):
            # ... and try to match what's left to the rest of the sequence  
            yield from consume_sequence(rules, sequence, message)


def consume(rules, r, message):
    """ Consume any prefix of string S matching rule R """
    if isinstance(rules[r], list):
        for rr in rules[r]:
            yield from consume_sequence(rules, rr, message)
    elif message and rules[r] == message[0]:
        yield message[1:]


def match(rules, message):
    """ Try matching message by removing valid prefixes. The 
    whole message is valid if nothing is left after applying 
    all the rules"""
    return any(m == '' for m in consume(rules, '0', message))


def solve_part_1(rules, messages):
    return sum(match(rules, m) for m in messages)


def solve_part_2(rules, messages):
    rules['8'] = [['42'], ['42', '8']]
    rules['11'] = [['42', '31'], ['42', '11', '31']]
    return sum(match(rules, m) for m in messages)


if __name__ == "__main__":
    rules, messages = parse('input.txt')
    print(f'{solve_part_1(rules, messages)}, {solve_part_2(rules, messages)}')
