import itertools
import math
import pprint
import re
import time
from copy import deepcopy

from utils import read_file


def _a():
    lines = read_file(7).split('\n')

    total = 0
    for line in lines:
        expected, values = line.split(': ')
        expected = int(expected)
        values = [int(v) for v in values.split(' ')]

        # keep trying combinations until one works or no more combinations
        for combination in itertools.product('+*', repeat=len(values)-1):
            result = values[0]
            for i, value in enumerate(values[1:]):
                if combination[i] == '+':
                    result += value
                else:
                    result *= value

            # found!
            if result == expected:
                total += expected
                break
    return total


def _b():
    lines = read_file(7).split('\n')

    total = 0
    for line in lines:
        expected, values = line.split(': ')
        expected = int(expected)
        values = [int(v) for v in values.split(' ')]

        # keep trying combinations until one works or no more combinations
        for combination in itertools.product('+*|', repeat=len(values) - 1):
            result = values[0]
            for i, value in enumerate(values[1:]):
                if combination[i] == '+':
                    result += value
                elif combination[i] == '*':
                    result *= value
                else:
                    result = int(str(result) + str(value))

            # found!
            if result == expected:
                total += expected
                break
    return total
