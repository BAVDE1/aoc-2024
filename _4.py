import pprint
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
                if contents[i - match_num][char_i] == ["X", "M", "A", "S"][match_num]:
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

        if reverse:
            l = ''.join([c_ for c_ in l[::-1]])

        found = 0
        for char_i, char in enumerate(l[3:]):
            if char != "X":
                continue

            match_num = 0
            for _ in range(4):
                checking_line = contents[i - match_num]
                if reverse:
                    checking_line = ''.join([c_ for c_ in checking_line[::-1]])

                if checking_line[char_i + 3 - match_num] == ["X", "M", "A", "S"][match_num]:
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

    contents = [c for c in contents[::-1]]

    i = 0
    for line in contents:
        total_found += check_vertical(line)
        total_found += check_diagonal(line)
        total_found += check_diagonal(line, True)
        i += 1
    return total_found


def _b():
    contents = read_file(4).split("\n")

    def check_for_x_mas(l):
        if i == 0 or i == len(l) - 1:
            return 0

        found = 0
        for char_i, char in enumerate(l[1:-1]):
            if char != "A":
                continue

            check = [
                contents[i - 1][char_i], contents[i - 1][char_i + 2],
                contents[i + 1][char_i], contents[i + 1][char_i + 2],
            ]

            check_a = ["M", "M", "S", "S"]
            check_b = ["M", "S", "M", "S"]
            if check == check_a or check[::-1] == check_a or \
                    check == check_b or check[::-1] == check_b:
                found += 1
        return found

    total_found = 0
    for i, line in enumerate(contents):
        total_found += int(check_for_x_mas(line))
    return total_found
