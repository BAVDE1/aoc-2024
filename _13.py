import itertools
import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


def _a():
    lines = read_file(13).split('\n\n')

    tokens_used = 0
    for machine in lines:
        btn_a, btn_b, goal = machine.split('\n')
        a_x_addition, a_y_addition = re.findall('\d\d', btn_a)
        a_x_addition, a_y_addition = int(a_x_addition), int(a_y_addition)
        b_x_addition, b_y_addition = re.findall('\d\d', btn_b)
        b_x_addition, b_y_addition = int(b_x_addition), int(b_y_addition)
        x_goal, y_goal = re.findall('\d+', goal)
        x_goal, y_goal = int(x_goal), int(y_goal)

        value_x, value_y = 0, 0
        a_press, b_press = 0, 0
        while value_x != x_goal or value_y != y_goal:
            b_press += 1
            if b_press > 100:
                a_press += 1
                if a_press > 100:
                    break
                b_press = 0

            value_x = (a_press * a_x_addition) + (b_press * b_x_addition)
            value_y = (a_press * a_y_addition) + (b_press * b_y_addition)

        if a_press != 101 and b_press != 101:
            tokens_used += (3*a_press) + b_press
        # print((3*a_press) + b_press, a_press, b_press, value_x, value_y)
    return tokens_used


def _b():

    lines = read_file(13).split('\n\n')

    tokens_used = 0
    for machine in lines:
        btn_a, btn_b, goal = machine.split('\n')
        a_x_addition, a_y_addition = re.findall('\d\d', btn_a)
        a_x_addition, a_y_addition = int(a_x_addition), int(a_y_addition)
        b_x_addition, b_y_addition = re.findall('\d\d', btn_b)
        b_x_addition, b_y_addition = int(b_x_addition), int(b_y_addition)
        x_goal, y_goal = re.findall('\d+', goal)
        x_goal, y_goal = int(x_goal) * 10_000_000_000_000, int(y_goal) * 10_000_000_000_000

        value_x, value_y = 0, 0
        a_press, b_press = 0, 0

        # while value_x != x_goal or value_y != y_goal:
        #     b_press += 1
        #     if b_press > 10_000_000_000_000:
        #         a_press += 1
        #         if a_press > 10_000_000_000_000:
        #             break
        #         b_press = 0
        #
        #     value_x = (a_press * a_x_addition) + (b_press * b_x_addition)
        #     value_y = (a_press * a_y_addition) + (b_press * b_y_addition)

        if a_press != 10_000_000_000_001 and b_press != 10_000_000_000_001:
            tokens_used += (3*a_press) + b_press
        # print((3*a_press) + b_press, a_press, b_press, value_x, value_y)
    return tokens_used