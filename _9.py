import itertools
import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


def _a():
    contents = read_file(9)

    id = 0
    block = []
    all_storage = []

    # create all storage
    for i, char in enumerate(contents):
        if i % 2 == 0:
            block = [str(id)] * int(char)
        else:
            block += ['.'] * int(char)
            id += 1
            all_storage += block
    if not block[-1] == '.':
        all_storage += block

    # sort into new storage
    free_space = all_storage.count('.')
    new_storage = deepcopy(all_storage)
    for i, char in enumerate(all_storage[::-1]):
        if char == '.':
            continue

        new_storage[new_storage.index('.')] = char
        new_storage[-(i + 1)] = '.'

        # all dots are at the end of the list
        if ''.join(new_storage).endswith('.' * free_space):
            break

    checksum = sum(list(i * int(char) for i, char in enumerate(new_storage) if char != '.'))
    return checksum


def _b():
    contents = read_file(9)

    id = 0
    block = []
    all_storage = []

    # create all storage
    for i, char in enumerate(contents):
        if i % 2 == 0:
            block = [[str(id)] * int(char)]
        else:
            if char != '0':
                block += [['.'] * int(char)]
            id += 1
            all_storage += block
    if not block[-1] == '.':
        all_storage += block

    # sort into new storage
    new_storage = deepcopy(all_storage)
    for section in all_storage[::-1]:
        if '.' in section:
            continue

        section_inx = new_storage.index(section)
        space_needed = len(section)
        space_inx = [_i for _i, item in enumerate(new_storage[:section_inx]) if
                     item[0] == '.' and len(item) >= space_needed]

        # no space :(
        if len(space_inx) == 0:
            continue

        # remove space where section is to be moved into
        space_inx = space_inx[0]
        space = len(new_storage[space_inx])
        if space == space_needed:
            new_storage.pop(space_inx)
        else:
            new_storage[space_inx] = ['.'] * (space - space_needed)

        # place section
        new_storage.insert(space_inx, section)

        # override old section with empty space
        old_inx = new_storage.index(section, space_inx + 1)
        new_storage[old_inx] = ['.'] * space_needed

        # merge empty spaces if they're next to each other
        if new_storage[old_inx - 1][0] == '.':
            new_storage[old_inx - 1] += new_storage[old_inx]
            new_storage.pop(old_inx)
            old_inx -= 1
        if old_inx + 1 < len(new_storage) and new_storage[old_inx + 1][0] == '.':
            new_storage[old_inx + 1] += new_storage[old_inx]
            new_storage.pop(old_inx)

    new_storage = [num for section in new_storage for num in section]
    checksum = sum(list(i * int(num) for i, num in enumerate(new_storage) if num != '.'))
    return checksum
