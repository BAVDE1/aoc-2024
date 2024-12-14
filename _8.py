import itertools
import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


def _a():
    lines = read_file(8).split('\n')

    points = [[x, y, char] for y, line in enumerate(lines) for x, char in enumerate(line) if char != '.']

    locations = []
    for inx_a, p_a in enumerate(points):
        for p_b in points:
            if p_a[:2] == p_b[:2] or p_a[2] != p_b[2]:
                continue

            distance = [p_a[0] - p_b[0], p_a[1] - p_b[1]]
            projection_a = [p_a[0] + distance[0], p_a[1] + distance[1]]
            projection_b = [p_b[0] - distance[0], p_b[1] - distance[1]]

            for proj in [projection_a, projection_b]:
                # outside of bounds
                if proj[0] < 0 or proj[1] < 0 or proj[0] > len(lines[0])-1 or proj[1] > len(lines)-1:
                    continue

                if proj not in locations:
                    locations.append(proj)
    return len(locations)


def _b():
    lines = read_file(8).split('\n')

    points = [[x, y, char] for y, line in enumerate(lines) for x, char in enumerate(line) if char != '.']

    locations = []
    for inx_a, p_a in enumerate(points):
        for p_b in points:
            if p_a[:2] == p_b[:2] or p_a[2] != p_b[2]:
                continue

            distance = [p_a[0] - p_b[0], p_a[1] - p_b[1]]
            projection_a = p_a[:2]
            projection_b = p_b[:2]

            for i, proj in enumerate([projection_a, projection_b]):
                # outside of bounds
                while not (proj[0] < 0 or proj[1] < 0 or proj[0] > len(lines[0])-1 or proj[1] > len(lines)-1):
                    if proj not in locations:
                        locations.append(proj[:2])

                    if i == 0:
                        proj[0] += distance[0]
                        proj[1] += distance[1]
                    else:
                        proj[0] -= distance[0]
                        proj[1] -= distance[1]
    return len(locations)
