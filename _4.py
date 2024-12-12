import re
from copy import deepcopy

from utils import read_file


def _a():
    contents = read_file(4)
    total_found = len(re.findall('XMAS', contents) + re.findall('SAMX', contents))
    contents = contents.split("\n")

    def check_vertical(l):
        if i < 3:
            return 0

        found = 0
        for char_i, char in enumerate(l):
            if char != "X":
                continue

            match_num = 0
            for _ in range(4):
                if contents[i-match_num][char_i] == ["X", "M", "A", "S"][match_num]:
                    match_num += 1
                    if match_num == 4:
                        found += 1
                        break
                else:
                    break
        return found

    def check_diagonal(l, reverse=False):
        if i < 3:
            return 0

        found = 0
        for char_i, char in enumerate(l[3::-1 if reverse else 1]):
            if char != "X":
                continue

            match_num = 0
            for _ in range(4):
                if contents[i - match_num][char_i+3 - match_num] == ["X", "M", "A", "S"][match_num]:
                    match_num += 1
                    if match_num == 4:
                        found += 1
                        break
                else:
                    break
        return found

    i = 0
    for line in contents:
        total_found += check_vertical(line)
        total_found += check_diagonal(line)
        total_found += check_diagonal(line, True)
        i += 1

    i = 0
    for line in contents[::-1]:
        total_found += check_vertical(line)
        total_found += check_diagonal(line)
        total_found += check_diagonal(line, True)
        i += 1
    return total_found


def _b():
    contents = read_file(4)
