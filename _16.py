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

    path_positions = []
    walls = []
    start_pos = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            p = [x, y]
            if char == 'S':
                start_pos = p
            elif char == 'E':
                end_pos = p
            elif char == '.':
                path_positions.append(p)
            else:
                walls.append(p)

    def add(position, direction):
        addition = [[0, -1], [0, 1], [-1, 0], [1, 0]][direction]
        return [position[0] + addition[0], position[1] + addition[1]]

    # returns list of possible directions perpendicular to given direction
    def perp_routes(x, y, direction):
        directions = []
        to_check = [LEFT, RIGHT] if direction in [UP, DOWN] else [UP, DOWN]
        for checking_direction in to_check:
            d_pos = add([x, y], checking_direction)
            if the_map[d_pos[1]][d_pos[0]] != '#':
                directions.append(checking_direction)
        return directions

    possible_routes = []

    def try_route(x, y, move_direction, accumulated_pivots, accumulated_moves, visited):
        if accumulated_pivots > 1000:  # infinite loop
            return
        pos_in_front = [x, y]  # start where you are
        char_in_front = the_map[y][x]
        moving = False

        while char_in_front != '#':
            if pos_in_front in visited:
                # the_map[y][x] = '_'
                break
            visited.append([x, y])
            # the_map[y][x] = '_'
            x, y = pos_in_front  # move forward
            accumulated_moves += int(moving)
            moving = True

            # found one route
            if the_map[y][x] == 'E':
                route_stats = [accumulated_pivots, accumulated_moves]
                if route_stats not in possible_routes:
                    possible_routes.append(route_stats)
                # the_map[y][x] = 'E'
                break

            the_map[y][x] = str(accumulated_pivots)

            # branch off
            for branch_direction in perp_routes(x, y, move_direction):
                try_route(*add([x, y], branch_direction), branch_direction, accumulated_pivots + 1, accumulated_moves + 1, deepcopy(visited))

            pos_in_front = add([x, y], move_direction)
            char_in_front = the_map[pos_in_front[1]][pos_in_front[0]]

    try_route(start_pos[0], start_pos[1], RIGHT, 0, 0, [])

    lowest = 10e10
    for route_stats in possible_routes:
        score = (route_stats[0] * 1000) + route_stats[1]
        if score < lowest:
            lowest = score
    return lowest


def _b():
    lines = read_file(16).split('\n')
