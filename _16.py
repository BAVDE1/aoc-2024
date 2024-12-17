import itertools
import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

STRAIGHT_POINTS = 1
TURN_POINTS = 1000


def _a():
    lines = read_file(16).split('\n')
    the_map = [list(line) for line in lines]

    def add(position, direction):
        addition = [[0, -1], [0, 1], [-1, 0], [1, 0]][direction]
        return [position[0] + addition[0], position[1] + addition[1]]

    # returns list of possible directions perpendicular to given direction
    def perp_routes(pos, direction):
        directions = []
        to_check = [RIGHT, LEFT] if direction in [UP, DOWN] else [UP, DOWN]
        for i, checking_direction in enumerate(to_check):
            d_pos = add(pos, checking_direction)
            if the_map[d_pos[1]][d_pos[0]] != '#':
                directions.append(checking_direction)
        return directions

    start_pos = [[x, y] for y, line in enumerate(lines) for x, char in enumerate(line) if char == 'S'][0]
    possible_routes = []
    lowest_pivot = [140]
    lowest_score = [10e10]

    def try_route(position, move_direction, accumulated_pivots, accumulated_moves, visited):
        the_char = the_map[position[1]][position[0]]
        moving = False

        while the_char != '#':
            if position in visited:
                break
            accumulated_moves += int(moving)
            moving = True

            # found one route & check if score is less than the current lowest
            if the_char == 'E':
                route_stats = [accumulated_pivots, accumulated_moves]
                if route_stats not in possible_routes:
                    possible_routes.append(route_stats)

                    score = (route_stats[0] * 1000) + route_stats[1]
                    if score < lowest_score[0]:
                        lowest_pivot[0] = route_stats[0]
                        lowest_score[0] = score
                        print(lowest_pivot, lowest_score)
                break

            # branch off
            for branch_direction in perp_routes(position, move_direction):
                if accumulated_pivots + 1 > lowest_pivot[0]:  # don't even bother
                    return
                visited.append(position)
                try_route(add(position, branch_direction), branch_direction, accumulated_pivots + 1, accumulated_moves + 1, deepcopy(visited))

            position = add(position, move_direction)
            the_char = the_map[position[1]][position[0]]

    t = time.time()
    try_route(start_pos, RIGHT, 0, 0, [])
    print(time.time() - t)
    return lowest_score[0]


def _b():
    lines = read_file(16).split('\n')
