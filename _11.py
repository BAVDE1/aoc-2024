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
        # print(stones)
    return len(stones)


def _b():
    stones = read_file(11).split(' ')
    blink_times = 25

    def do_stone(the_stone: str, iteration: int):
        if iteration == blink_times:
            return 0

        if int(the_stone) == 0:
            return do_stone('1', iteration + 1)
        elif len(the_stone) % 2 == 0:
            mid = int(len(the_stone) * .5)
            a = do_stone(the_stone[:mid], iteration + 1)
            return 1 + a + do_stone(str(int(the_stone[mid:])), iteration + 1)
        else:
            return do_stone(str(int(the_stone) * 2024), iteration + 1)

    total_count = len(stones)
    for starting_stone in stones:
        pass
        # print(starting_stone)
        # total_count += do_stone(starting_stone, 0)

        # print(tb, tc)
    return total_count
