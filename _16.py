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


def _a():
    lines = read_file(16).split('\n')
    the_map = [list(line) for line in lines]

    def add(position, direction):
        addition = [[0, -1], [0, 1], [-1, 0], [1, 0]][direction]
        return [position[0] + addition[0], position[1] + addition[1]]

    def get_neighbours(pos):
        lis = []
        for direction in [UP, DOWN, LEFT, RIGHT]:
            neighbour_pos = add(pos, direction)
            if the_map[neighbour_pos[1]][neighbour_pos[0]] != '#':
                lis.append(neighbour_pos)
        return lis

    positions = []
    start_pos = []
    for y, line in enumerate(lines):
        lis = []
        for x, char in enumerate(line):
            lis.append(False)
            if char == 'S':
                start_pos = [x, y]
        positions.append(lis)

    queue = deque()
    queue.append([start_pos, RIGHT, 0])

    cache = {}  # key: pos-direction, value: score

    lowest_score = 10e10
    while queue:
        pos, facing_direction, score = queue.popleft()

        key = f'{pos}-{facing_direction}'
        if key in cache and cache[key] < score:  # already found a better route this way, don't bother
            continue
        cache[key] = score

        if the_map[pos[1]][pos[0]] == 'E':
            if score < lowest_score:
                lowest_score = score
            continue

        moves = [UP, DOWN, LEFT, RIGHT]
        moves.remove([DOWN, UP, RIGHT, LEFT][facing_direction])
        for direction in moves:
            next_pos = add(pos, direction)
            if the_map[next_pos[1]][next_pos[0]] == '#':
                continue
            next_score = score + (1 if direction == facing_direction else 1001)
            queue.append([next_pos, direction, next_score])
    return lowest_score


def _b():
    pass
