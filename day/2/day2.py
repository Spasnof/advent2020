from itertools import combinations
from dataclasses import dataclass
import re

@dataclass
class Policy:
    lowerbound: int
    upperbound: int
    letter: str


@dataclass
class Password:
    policy: Policy
    password: str


def process_line(line: str) -> Password:
    policy_raw, password = line.split(':')
    policy_range, letter = policy_raw.split(' ')
    lowerbound, upperbound = policy_range.split('-')
    return Password(
        Policy(int(lowerbound), int(upperbound), letter),
        str(password).strip()
    )

with open('input/input.txt','r', newline='\n') as file:
    lines = file.readlines()
    passwords = [process_line(line) for line in lines]
    valid_pws = 0
    for pw in passwords:
        # print(pw)
        matches = len(re.findall(pw.policy.letter, pw.password))
        if matches >= pw.policy.lowerbound and matches <= pw.policy.upperbound:
            print(pw, 'is valid')
            valid_pws += 1
    print(f'there are {valid_pws} valid passwords total')

    valid_pws = 0
    for pw in passwords:
        # offset the indexes to match a index 0 concept
        index1 = pw.policy.upperbound - 1
        index2 = pw.policy.lowerbound - 1
        letters = pw.password[index1] + pw.password[index2]
        matches = len(re.findall(pw.policy.letter, letters))
        if matches == 1:
            print(pw, 'is valid')
            valid_pws += 1
    print(f'there are {valid_pws} valid passwords total')