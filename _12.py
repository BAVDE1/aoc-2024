import itertools
import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


def _a():
    lines = read_file(12).split('\n')
    placed = []

    def find_relatives(x, y):
        needed_char = lines[y][x]

        f = []
        for neighbour in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
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

    total = 0
    for group in groups:
        area = len(group)
        perimeter = 0
        for pos in group:
            for neighbour in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
                neighbour_pos = [pos[0] + neighbour[0], pos[1] + neighbour[1]]
                if neighbour_pos not in group:
                    perimeter += 1
        total += area * perimeter
    return total


def _b():
    lines = read_file(12).split('\n')
    placed = []

    def find_relatives(x, y):
        needed_char = lines[y][x]

        f = []
        for neighbour in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
            neighbour_pos = [x + neighbour[0], y + neighbour[1]]
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

    total = 0
    for group in groups:
        area = len(group)
        perimeters = []
        for pos in group:
            for neighbour in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
                neighbour_pos = [pos[0] + neighbour[0], pos[1] + neighbour[1]]
                if neighbour_pos not in group:
                    perimeters.append(neighbour_pos)

        checked_h = []
        checked_v = []
        checked_u = []
        checked_d = []
        checked_l = []
        checked_r = []
        checked_list = [checked_u, checked_d, checked_l, checked_r]
        sides = 0

        for perimeter in perimeters:
            # for direction, checked in enumerate(checked_list):
            #     if (direction < 2 and (perimeter in checked_l or perimeter in checked_r)) \
            #             or (direction > 1 and (perimeter in checked_u or perimeter in checked_d)):
            #         continue
            #
            #     check_direction = [[0, -1], [0, 1], [-1, 0], [1, 0]][direction]
            #     neighbour_pos = [perimeter[0] + check_direction[0], perimeter[1] + check_direction[1]]
            #     if neighbour_pos in group and neighbour_pos not in checked:
            #         checked.append(neighbour_pos)
            #         sides += 1
            #
            #     checked.append(perimeter)
            #     check_next = [perimeter[0] + check_direction[0], perimeter[1] + check_direction[1]]
            #     while check_next in perimeters:
            #         checked.append(deepcopy(check_next))
            #         check_next[0] += check_direction[0]
            #         check_next[1] += check_direction[1]

            if perimeter in checked_h and perimeter in checked_v:
                continue
            print(perimeter)
            if perimeter not in checked_v:
                # add sides of how many its touching
                for neighbour in [[-1, 0], [1, 0]]:
                    neighbour_pos = [perimeter[0] + neighbour[0], perimeter[1] + neighbour[1]]
                    if neighbour_pos in group:
                        print(neighbour_pos)
                        sides += 1

                checked_v.append(perimeter)
                up = [perimeter[0], perimeter[1] - 1]
                while up in perimeters:
                    checked_v.append(deepcopy(up))
                    up[1] -= 1
                down = [perimeter[0], perimeter[1] + 1]
                while down in perimeters:
                    checked_v.append(deepcopy(down))
                    down[1] += 1

            if perimeter not in checked_h:
                # add sides of how many its touching
                for neighbour in [[0, 1], [0, -1]]:
                    neighbour_pos = [perimeter[0] + neighbour[0], perimeter[1] + neighbour[1]]
                    if neighbour_pos in group:
                        print(neighbour_pos)
                        sides += 1

                checked_h.append(perimeter)
                left = [perimeter[0] - 1, perimeter[1]]
                while left in perimeters:
                    checked_h.append(deepcopy(left))
                    left[0] -= 1
                right = [perimeter[0] + 1, perimeter[1]]
                while right in perimeters:
                    checked_h.append(deepcopy(right))
                    right[0] += 1
        print(sides)
        total += area * sides
    return total
