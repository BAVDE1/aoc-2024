import re
from copy import deepcopy

from utils import read_file

find_mul_regex = re.compile('mul\(\d+,\d+\)')
find_nums_regex = re.compile('\d+')


def _a():
    contents = read_file(3)
    matches = re.findall(find_mul_regex, contents)

    sum = 0
    for match in matches:
        nums = re.findall(find_nums_regex, match)
        sum += int(nums[0]) * int(nums[1])
    return sum


find_mul_regex_b = re.compile("mul\(\d+,\d+\)|don't\(\)|do\(\)")

def _b():
    contents = read_file(3)
    matches = re.findall(find_mul_regex_b, contents)

    sum = 0
    enabled = True
    for match in matches:
        if match in ["don't()", "do()"]:
            enabled = match == "do()"
            continue

        if enabled:
            nums = re.findall(find_nums_regex, match)
            sum += int(nums[0]) * int(nums[1])
    return sum
