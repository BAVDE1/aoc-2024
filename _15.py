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


def _a():
    lines, actions = read_file(15).split('\n\n')
    actions = actions.replace('\n', '')

    # build the map & find the robot
    robot_pos = []
    the_map = []
    for y, line in enumerate(lines.split('\n')):
        the_map.append([])
        for x, char in enumerate(line):
            if char == '@':
                robot_pos = [x, y]
            the_map[y].append(char)

    def add(position, direction):
        addition = [[0, -1], [0, 1], [-1, 0], [1, 0]][direction]
        return [position[0] + addition[0], position[1] + addition[1]]

    def push(x, y, direction):
        char = the_map[y][x]
        if char == 'O' or char == '@':
            next_x, next_y = add([x, y], direction)
            if push(next_x, next_y, direction):
                the_map[next_y][next_x] = char  # move
                the_map[y][x] = '.'  # empty old pos
                return True
            return False
        return char == '.'

    # move the robot!
    for action in actions:
        direction = {'^': UP, 'v': DOWN, '<': LEFT, '>': RIGHT}[action]
        if push(*robot_pos, direction):
            robot_pos = add(robot_pos, direction)  # update robot pos

    # find final sum
    return sum([100 * y + x for y, line in enumerate(the_map) for x, char in enumerate(line) if char == 'O'])


def _b():
    contents = read_file(15).split('\n\n')
