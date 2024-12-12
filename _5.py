import pprint
import re
from copy import deepcopy

from utils import read_file


def _a():
    rules, pages = read_file(5).split('\n\n')

    items_before: dict[list] = {}  # items that should be before key
    items_after: dict[list] = {}  # items that should be after key

    for rule in rules.split('\n'):
        a, b = rule.split('|')

        if b in items_before.keys():
            items_before[b].append(a)
        else:
            items_before[b] = [a]

        if a in items_after.keys():
            items_after[a].append(b)
        else:
            items_after[a] = [b]

    correct_pages = []
    for page in pages.split('\n'):
        page = page.split(',')

        correct = True
        for i_num_a, num_a in enumerate(page):
            before = page[:i_num_a]
            after = page[i_num_a + 1:]

            for before_item in before:
                if num_a in items_after.keys() and before_item in items_after[num_a]:
                    correct = False

            for after_item in after:
                if num_a in items_before.keys() and after_item in items_before[num_a]:
                    correct = False
        if correct:
            correct_pages.append(page)

    sum = 0
    for page in correct_pages:
        inx = int((len(page) - 1) / 2)
        sum += int(page[inx])
    return sum


def _b():
    rules, pages = read_file(5).split('\n\n')

    items_before: dict[list] = {}  # items that should be before key
    items_after: dict[list] = {}  # items that should be after key

    for rule in rules.split('\n'):
        a, b = rule.split('|')

        if b in items_before.keys():
            items_before[b].append(a)
        else:
            items_before[b] = [a]

        if a in items_after.keys():
            items_after[a].append(b)
        else:
            items_after[a] = [b]

    incorrect_pages = []
    for page in pages.split('\n'):
        page = page.split(',')

        correct = True
        for i_num_a, num_a in enumerate(page):
            before = page[:i_num_a]
            after = page[i_num_a + 1:]

            for before_item in before:
                if num_a in items_after.keys() and before_item in items_after[num_a]:
                    correct = False

            for after_item in after:
                if num_a in items_before.keys() and after_item in items_before[num_a]:
                    correct = False
        if not correct:
            incorrect_pages.append(page)

    # correct the incorrect pages
    for i, page in enumerate(incorrect_pages):
        new_page = []
        for num in page:
            if len(new_page) == 0:
                new_page.append(num)
                continue

            inserted = False
            for inx, num_existing in enumerate(new_page):
                if num in items_after.keys() and num_existing in items_after[num]:
                    inserted = True
                    new_page.insert(inx, num)
                    break

            if not inserted:
                new_page.append(num)
        incorrect_pages[i] = new_page

    sum = 0
    for page in incorrect_pages:
        inx = int((len(page) - 1) / 2)
        sum += int(page[inx])
    return sum
