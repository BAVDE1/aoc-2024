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
        new_storage[-(i+1)] = '.'

        # all dots are at the end of the list
        if ''.join(new_storage).endswith('.' * free_space):
            break

    checksum = sum(list(i*int(char) for i, char in enumerate(new_storage) if char != '.'))
    return checksum


def _b():
    contents = read_file(9)
