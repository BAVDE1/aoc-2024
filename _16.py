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

    start_pos = [[x, y] for y, line in enumerate(lines) for x, char in enumerate(line) if char == 'S'][0]

    cache = {}  # key: pos-direction, value: lowest score at that pos & direction
    lowest_score = 10e10
    queue = deque()
    queue.append([start_pos, RIGHT, 0])

    while queue:
        pos, facing_direction, score = queue.popleft()

        # already found a better route this way, don't bother
        key = f'{pos}-{facing_direction}'
        if key in cache and cache[key] < score:
            continue
        cache[key] = score

        # found one!
        if the_map[pos[1]][pos[0]] == 'E':
            if score < lowest_score:
                lowest_score = score
            continue

        # move to next position/s
        moves = [UP, DOWN, LEFT, RIGHT]
        moves.remove([DOWN, UP, RIGHT, LEFT][facing_direction])  # don't move backwards lol
        for direction in moves:
            next_pos = add(pos, direction)
            if the_map[next_pos[1]][next_pos[0]] == '#':
                continue
            next_score = score + (1 if direction == facing_direction else 1001)
            queue.append([next_pos, direction, next_score])
    return lowest_score


def _b():
    lines = read_file(16).split('\n')
    the_map = [list(line) for line in lines]

    def add(position, direction):
        addition = [[0, -1], [0, 1], [-1, 0], [1, 0]][direction]
        return [position[0] + addition[0], position[1] + addition[1]]

    start_pos = [[x, y] for y, line in enumerate(lines) for x, char in enumerate(line) if char == 'S'][0]

    cache = {}  # key: pos-direction, value: lowest score at that pos & direction
    lowest_score = 10e10
    queue = deque()
    queue.append([start_pos, RIGHT, 0, ''])

    best_paths_points = []
    while queue:
        pos, facing_direction, score, path = queue.popleft()

        # already found a better route this way, don't bother
        key = f'{pos}-{facing_direction}'
        if key in cache and cache[key] < score:
            continue
        cache[key] = score

        # found one!
        if the_map[pos[1]][pos[0]] == 'E':
            if score < lowest_score:
                lowest_score = score
                best_paths_points.clear()
            if score == lowest_score:
                for p in path.split(']'):
                    if p not in best_paths_points:
                        best_paths_points.append(p)
            continue

        # move to next position/s
        moves = [UP, DOWN, LEFT, RIGHT]
        moves.remove([DOWN, UP, RIGHT, LEFT][facing_direction])  # don't move backwards lol
        for direction in moves:
            next_pos = add(pos, direction)
            if the_map[next_pos[1]][next_pos[0]] == '#':
                continue
            next_score = score + (1 if direction == facing_direction else 1001)
            new_path = f'{path}{next_pos}'
            queue.append([next_pos, direction, next_score, new_path])
    return len(best_paths_points)
