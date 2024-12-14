import itertools
import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


def _a():
    lines = read_file(10).split('\n')
    trail_heads = [[x, y] for y, line in enumerate(lines) for x, char in enumerate(line) if char == '0']

    def find_next(x, y):
        current_num = int(lines[y][x])

        found = []
        for neighbour in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
            neighbour_pos = [x + neighbour[0], y + neighbour[1]]

            if neighbour_pos[0] < 0 or neighbour_pos[1] < 0 or neighbour_pos[0] > len(lines[0]) - 1 or neighbour_pos[1] > len(lines) - 1:
                continue

            neighbour_num = int(lines[neighbour_pos[1]][neighbour_pos[0]])
            if current_num + 1 == neighbour_num:
                if neighbour_num == 9:  # YAR WE FOUND ONE
                    if neighbour_pos not in found:
                        found.append(neighbour_pos)
                    continue

                for pos in find_next(*neighbour_pos):
                    if pos not in found:
                        found.append(pos)
        return found

    final_count = 0
    for th in trail_heads:
        th_found = find_next(th[0], th[1])
        final_count += len(th_found)
    return final_count


def _b():
    lines = read_file(10).split('\n')
    trail_heads = [[x, y] for y, line in enumerate(lines) for x, char in enumerate(line) if char == '0']

    def find_next(x, y):
        current_num = int(lines[y][x])

        found = []
        for neighbour in [[0, -1], [1, 0], [0, 1], [-1, 0]]:
            neighbour_pos = [x + neighbour[0], y + neighbour[1]]

            if neighbour_pos[0] < 0 or neighbour_pos[1] < 0 or neighbour_pos[0] > len(lines[0]) - 1 or neighbour_pos[
                1] > len(lines) - 1:
                continue

            neighbour_num = int(lines[neighbour_pos[1]][neighbour_pos[0]])
            if current_num + 1 == neighbour_num:
                if neighbour_num == 9:  # YAR WE FOUND ONE
                    found.append(neighbour_pos)
                    continue

                for pos in find_next(*neighbour_pos):
                    found.append(pos)
        return found

    final_count = 0
    for th in trail_heads:
        th_found = find_next(th[0], th[1])
        final_count += len(th_found)
    return final_count
