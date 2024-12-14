import itertools
import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


def _a():
    stones = read_file(11).split(' ')

    blink_times = 25
    for blink_num in range(blink_times):
        new_stones = []
        for stone in stones:
            if int(stone) == 0:
                new_stones.append('1')
            elif len(stone) % 2 == 0:
                mid = int(len(stone)/2)
                new_stones.append(stone[:mid])
                new_stones.append(str(int(stone[mid:])))
            else:
                new_stones.append(str(int(stone) * 2024))
        stones = new_stones
    return len(stones)


def _b():
    stones = read_file(11).split(' ')
    blink_times = 75
    cache = {}

    def do_stone(the_stone: str, iteration: int):
        if iteration == blink_times:
            return 0

        key = f'{iteration}-{the_stone}'
        if key in cache:
            return cache[key]

        count = 0
        if int(the_stone) == 0:
            count += do_stone('1', iteration + 1)
        elif len(the_stone) % 2 == 0:
            mid = int(len(the_stone) * .5)
            count += do_stone(the_stone[:mid], iteration + 1)
            count += 1 + do_stone(str(int(the_stone[mid:])), iteration + 1)
        else:
            count += do_stone(str(int(the_stone) * 2024), iteration + 1)
        cache[key] = count
        return count

    total_count = len(stones)
    for starting_stone in stones:
        total_count += do_stone(starting_stone, 0)
    return total_count
