import itertools
import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


WIDTH = 101  # 101
HEIGHT = 103  # 103


def _a():
    robots = read_file(14).split('\n')

    def add(position, addition_pos):
        return [position[0] + addition_pos[0], position[1] + addition_pos[1]]

    def mul(position, mul):
        return [position[0] * mul, position[1] * mul]

    final_positions = []
    for robot in robots:
        x, y, v_x, v_y = re.findall('\d+|-\d+', robot)
        pos = [int(x), int(y)]
        vel = [int(v_x), int(v_y)]

        vel = mul(vel, 100)
        pos = add(pos, vel)
        pos = [pos[0] % WIDTH, pos[1] % HEIGHT]
        final_positions.append(pos)

    quadrants = [[[], []], [[], []]]  # up [left, right], down [left, right]
    for final_pos in final_positions:
        x, y = final_pos
        if y == math.floor(HEIGHT / 2) or x == math.floor(WIDTH / 2):
            continue
        quadrants[y < math.floor(HEIGHT / 2)][x < math.floor(WIDTH / 2)].append(final_pos)

    total_score = 1
    for semi in quadrants:
        for quad in semi:
            total_score *= len(quad)
    return total_score


def _b():
    robots = read_file(14).split('\n')

    def add(position, addition_pos):
        return [position[0] + addition_pos[0], position[1] + addition_pos[1]]

    def mul(position, mul):
        return [position[0] * mul, position[1] * mul]

    positions = []
    velocities = []
    for robot in robots:
        x, y, v_x, v_y = re.findall('\d+|-\d+', robot)
        positions.append([int(x), int(y)])
        velocities.append([int(v_x), int(v_y)])

    lowest_score = 10e10
    lowest_second = 0
    for second in range(0, WIDTH * HEIGHT):
        second_positions = []
        for i, position in enumerate(positions):
            vel = mul(velocities[i], second)
            pos = add(position, vel)
            second_positions.append([pos[0] % WIDTH, pos[1] % HEIGHT])

        quadrants = [[[], []], [[], []]]  # up [left, right], down [left, right]
        for final_pos in second_positions:
            x, y = final_pos
            if y == math.floor(HEIGHT / 2) or x == math.floor(WIDTH / 2):
                continue
            quadrants[y < math.floor(HEIGHT / 2)][x < math.floor(WIDTH / 2)].append(final_pos)

        total_score = 1
        for semi in quadrants:
            for quad in semi:
                total_score *= len(quad)

        # find the tree!
        if total_score < lowest_score:
            lowest_score = total_score
            lowest_second = second
    return lowest_second
