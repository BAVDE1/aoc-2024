import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


def _a():
    lines = read_file(6).split('\n')

    facing = 0
    on_line = 0
    on_char = 0

    for i, line in enumerate(lines):
        if '^' in line:
            on_line = i
            on_char = line.index("^")
            break

    visited: list = [[on_char, on_line]]

    while True:
        def rotate():
            return (facing + 1) % 4

        try:
            if facing == 0 and lines[on_line - 1][on_char] == "#" or \
                    facing == 1 and lines[on_line][on_char + 1] == "#" or \
                    facing == 2 and lines[on_line +  1][on_char] == "#" or \
                    facing == 3 and lines[on_line][on_char - 1] == "#":
                facing = rotate()
                continue
        except IndexError:
            break

        movement = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        on_line += movement[facing][0]
        on_char += movement[facing][1]

        position = [on_char, on_line]
        if position not in visited:
            visited.append(position)
    return len(visited)


def _b():
    lines = read_file(6).split('\n')

    facing = 0
    on_line = 0
    on_char = 0

    for i, line in enumerate(lines):
        if '^' in line:
            on_line = i
            on_char = line.index("^")
            break

    og_pos = [on_char, on_line]

    obstacle_pos = [0, 0]
    obstacles_count = 0
    break_point = 20_000
    moves = 0

    while True:
        def move_obstacle():
            new_ob_pos = [0, obstacle_pos[1]]
            if obstacle_pos[0] == len(lines[0]) - 1:
                new_ob_pos[1] = obstacle_pos[1] + 1
            new_ob_pos[0] = (obstacle_pos[0] + 1) % len(lines[0])
            return new_ob_pos

        def check_completion():
            return obstacle_pos[1] > len(lines)

        # print(moves)
        if moves == break_point:
            obstacle_pos = move_obstacle()
            if obstacle_pos == og_pos:
                obstacle_pos = move_obstacle()
            on_char, on_line = og_pos
            moves = 0
            facing = 0
            obstacles_count += 1
            if check_completion():
                break

        def rotate():
            return (facing + 1) % 4

        try:
            if facing == 0 and lines[on_line - 1][on_char] == "#" or \
                    facing == 1 and lines[on_line][on_char + 1] == "#" or \
                    facing == 2 and lines[on_line + 1][on_char] == "#" or \
                    facing == 3 and lines[on_line][on_char - 1] == "#":
                facing = rotate()
                continue
        except IndexError:
            obstacle_pos = move_obstacle()
            if obstacle_pos == og_pos:
                obstacle_pos = move_obstacle()
            on_char, on_line = og_pos
            moves = 0
            facing = 0
            if check_completion():
                break

        movement = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        old_pos = [on_char, on_line]
        on_line += movement[facing][0]
        on_char += movement[facing][1]
        new_pos = [on_char, on_line]

        # move back and rotate
        if new_pos == obstacle_pos:
            on_char, on_line = old_pos
            facing = rotate()
            continue
        moves += 1

        # print("================================")
        # for ia, line in enumerate(lines):
        #     l = ""
        #     for ib, char in enumerate(line):
        #         if [ib, ia] == [on_char, on_line]:
        #             l += "^"
        #         elif [ib, ia] == obstacle_pos:
        #             l += "O"
        #         else:
        #             l += char
        #     print(l)
        # time.sleep(.2)

    return obstacles_count