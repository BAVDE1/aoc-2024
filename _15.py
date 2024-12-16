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
    lines, actions = read_file(15).split('\n\n')
    actions = actions.replace('\n', '')

    # build the map & find the robot
    robot_pos = []
    the_map = []
    for y, line in enumerate(lines.split('\n')):
        the_map.append([])
        for x, char in enumerate(line):
            char_a, char_b = '.', '.'
            if char == '@':
                robot_pos = [x*2, y]
                char_a = char
            if char == '#':
                char_a, char_b = '#', '#'
            if char == 'O':
                char_a, char_b = '[', ']'
            the_map[y].append(char_a)
            the_map[y].append(char_b)

    def add(position, direction):
        if direction is None:
            return position
        addition = [[0, -1], [0, 1], [-1, 0], [1, 0]][direction]
        return [position[0] + addition[0], position[1] + addition[1]]

    def push(x, y, direction, mock=False):
        char: str = the_map[y][x]

        if char == '@':
            next_x, next_y = add([x, y], direction)
            if push(next_x, next_y, direction):
                if not mock:
                    the_map[y][x] = '.'  # empty old pos
                    the_map[next_y][next_x] = char  # move
                return True
            return False

        if char in '[]':
            is_right = char == ']'
            # offset one or the other to either the left or the right
            pos_left = add([x, y], LEFT if is_right else None)
            pos_right = add([x, y], RIGHT if not is_right else None)
            next_x_l, next_y_l = add(pos_left, direction)
            next_x_r, next_y_r = add(pos_right, direction)

            if (direction in [UP, DOWN] and push(next_x_r, next_y_r, direction, True) and push(next_x_l, next_y_l, direction, True)) or \
                    (direction == LEFT and push(next_x_l, next_y_l, direction)) or \
                    (direction == RIGHT and push(next_x_r, next_y_r, direction)):
                if not mock:
                    if direction in [UP, DOWN]:
                        push(next_x_r, next_y_r, direction)  # run these again but without mocking
                        push(next_x_l, next_y_l, direction)
                    the_map[pos_left[1]][pos_left[0]] = '.'
                    the_map[pos_right[1]][pos_right[0]] = '.'
                    the_map[next_y_l][next_x_l] = '['
                    the_map[next_y_r][next_x_r] = ']'
                return True
            return False
        return char == '.'

    # move the robot!
    for action in actions:
        direction = {'^': UP, 'v': DOWN, '<': LEFT, '>': RIGHT}[action]
        if push(*robot_pos, direction):
            robot_pos = add(robot_pos, direction)  # update robot pos

    # # find final sum
    return sum([100 * y + x for y, line in enumerate(the_map) for x, char in enumerate(line) if char == '['])
