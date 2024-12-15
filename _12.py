import itertools
import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


NEIGHBOUR_ADDITIONS = [[0, -1], [1, 0], [0, 1], [-1, 0]]

def _a():
    lines = read_file(12).split('\n')
    placed = []

    def find_relatives(x, y):
        needed_char = lines[y][x]

        f = []
        for neighbour in NEIGHBOUR_ADDITIONS:
            neighbour_pos = [x + neighbour[0], y + neighbour[1]]
            if neighbour_pos in placed:
                continue

            if neighbour_pos[0] < 0 or neighbour_pos[1] < 0 or neighbour_pos[0] > len(lines[0]) - 1 or neighbour_pos[1] > len(lines) - 1:
                continue

            neighbour_char = lines[neighbour_pos[1]][neighbour_pos[0]]
            if neighbour_char != needed_char:
                continue

            placed.append(neighbour_pos)
            f.append(neighbour_pos)
            f += find_relatives(neighbour_pos[0], neighbour_pos[1])
        return f

    # build groups
    groups = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            pos = [x, y]
            if pos in placed:
                continue

            placed.append(pos)
            found = [pos]
            found += find_relatives(x, y)
            groups.append(found)

    # find perimeters & add up total
    total = 0
    for group in groups:
        area = len(group)
        perimeter = 0
        for pos in group:
            for neighbour in NEIGHBOUR_ADDITIONS:
                neighbour_pos = [pos[0] + neighbour[0], pos[1] + neighbour[1]]
                if neighbour_pos not in group:
                    perimeter += 1
        total += area * perimeter
    return total


def _b():
    lines = read_file(12).split('\n')
    placed = []

    def add(position, addition):
        return [position[0] + addition[0], position[1] + addition[1]]

    def find_relatives(x, y):
        needed_char = lines[y][x]

        f = []
        for neighbour_add in NEIGHBOUR_ADDITIONS:
            neighbour_pos = add([x, y], neighbour_add)
            if neighbour_pos in placed:
                continue

            if neighbour_pos[0] < 0 or neighbour_pos[1] < 0 or neighbour_pos[0] > len(lines[0]) - 1 or neighbour_pos[
                1] > len(lines) - 1:
                continue

            neighbour_char = lines[neighbour_pos[1]][neighbour_pos[0]]
            if neighbour_char != needed_char:
                continue

            placed.append(neighbour_pos)
            f.append(neighbour_pos)
            f += find_relatives(neighbour_pos[0], neighbour_pos[1])
        return f

    # build groups
    groups = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            pos = [x, y]
            if pos in placed:
                continue

            placed.append(pos)
            found = [pos]
            found += find_relatives(x, y)
            groups.append(found)

    # find total
    total = 0
    for group in groups:
        area = len(group)

        # find all spaces surrounding the group
        perimeters = []
        for pos in group:
            for neighbour_add in NEIGHBOUR_ADDITIONS:
                neighbour_pos = add(pos, neighbour_add)
                if neighbour_pos not in group:
                    perimeters.append(neighbour_pos)

        checked_list = [[], [], [], []]  # 0: up, 1: down, 2: left, 3: right
        sides = 0

        # find sides
        for perimeter in perimeters:
            for direction, checked in enumerate(checked_list):
                if perimeter in checked:
                    continue

                check_direction = [[0, -1], [0, 1], [-1, 0], [1, 0]][direction]  # the order is important!
                if add(perimeter, check_direction) in group:
                    sides += 1
                else:
                    continue

                checked.append(perimeter)

                # move perpendicular to the checking direction (both ways)
                # until it runs out of perimeter, or the checking direction relative to the check_pos is not in the group
                def check_in_direction(addition):
                    check_pos = add(perimeter, addition)
                    while check_pos in perimeters:
                        checked.append(deepcopy(check_pos))
                        if add(check_pos, check_direction) not in group:  # nothing is there, stop!
                            break
                        check_pos = add(check_pos, addition)

                if direction < 2:
                    check_in_direction([1, 0])  # right
                    check_in_direction([-1, 0])  # left
                else:
                    check_in_direction([0, 1])  # down
                    check_in_direction([0, -1])  # up
        total += area * sides
    return total
