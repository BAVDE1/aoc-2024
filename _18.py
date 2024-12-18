import itertools
import math
import pprint
import re
import time
from copy import deepcopy
from collections import deque

from utils import read_file


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

BYTES = 1024
WIDTH = 70
HEIGHT = 70


def _a():
    contents = read_file(18).split('\n')[:BYTES]
    corrupted_spaces = [[int(num) for num in line.split(',')] for line in contents]
    allowed_spaces = [[False if [x, y] in corrupted_spaces else True for x in range(WIDTH+1)] for y in range(HEIGHT+1)]

    def add(position, direction):
        addition = [[0, -1], [0, 1], [-1, 0], [1, 0]][direction]
        return [position[0] + addition[0], position[1] + addition[1]]

    start_pos = [0, 0]
    end_pos = [WIDTH, HEIGHT]

    lowest_move_c = 10e10
    queue = [[start_pos, 0]]
    visited = []

    t = time.time()
    while queue:
        # queue = sorted(queue, key=lambda i: i[1])
        pos, move_c = queue.pop(0)

        # found one!
        if pos == end_pos:
            if move_c < lowest_move_c:
                lowest_move_c = move_c
                break
            continue

        # move to next position/s
        moves = [UP, DOWN, LEFT, RIGHT]
        for direction in moves:
            next_pos = add(pos, direction)
            if (next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] > WIDTH or next_pos[1] > HEIGHT) \
                    or not allowed_spaces[next_pos[1]][next_pos[0]] \
                    or next_pos in visited:
                continue
            visited.append(next_pos)
            queue.append([next_pos, move_c + 1])
    print(time.time() - t)
    return lowest_move_c


def _b():
    contents = read_file(18).split('\n')
    all_corrupted_spaces = [[int(num) for num in line.split(',')] for line in contents]

    def add(position, direction):
        addition = [[0, -1], [0, 1], [-1, 0], [1, 0]][direction]
        return [position[0] + addition[0], position[1] + addition[1]]

    end_pos = [WIDTH, HEIGHT]
    blocked = False
    bytes = 1024

    ascending = False
    addition = 1000

    while not blocked:
        bytes += math.ceil(addition) if ascending else -math.ceil(addition)
        lowest_move_c = 10e10
        queue = deque()
        queue.append([[0, 0], 0])
        visited = []

        allowed_spaces = [[False if [x, y] in all_corrupted_spaces[:bytes] else True for x in range(WIDTH + 1)] for y in
                          range(HEIGHT + 1)]

        while queue:
            pos, move_c = queue.popleft()

            # found one!
            if pos == end_pos:
                if move_c < lowest_move_c:
                    lowest_move_c = move_c
                continue

            # move to next position/s
            moves = [UP, DOWN, LEFT, RIGHT]
            for direction in moves:
                next_pos = add(pos, direction)
                if (next_pos[0] < 0 or next_pos[1] < 0 or next_pos[0] > WIDTH or next_pos[1] > HEIGHT) \
                        or not allowed_spaces[next_pos[1]][next_pos[0]] \
                        or next_pos in visited:
                    continue
                visited.append(next_pos)
                queue.append([next_pos, move_c + 1])

        # flip the checking direction
        if (ascending and lowest_move_c == 10e10) or (not ascending and lowest_move_c < 10e10):
            ascending = not ascending
            addition /= 2

            if addition < .2:
                blocked = lowest_move_c == 10e10
    return all_corrupted_spaces[bytes-1]
