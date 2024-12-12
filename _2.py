from copy import deepcopy

from utils import read_file


def _a():
    contents = read_file(2).replace('\n', '   ')
    reports = contents.split('  ')

    safe = 0
    for report in reports:
        report = report.strip().split(' ')
        is_safe = True
        positive = None

        for i in range(len(report) - 1):
            diff = int(report[i]) - int(report[i+1])
            if positive is None:
                positive = diff > 0
            if (diff > 0) != positive or diff == 0 or abs(diff) > 3:
                is_safe = False
                break
        safe += 1 if is_safe else 0
    return safe


def _b():
    def is_safe(r):
        is_r_safe = True
        positive = None
        for i in range(len(r) - 1):
            diff = int(r[i]) - int(r[i + 1])
            if positive is None:
                positive = diff > 0

            if (diff > 0) != positive or diff == 0 or abs(diff) > 3:
                is_r_safe = False
                break
        return is_r_safe

    contents = read_file(2).replace('\n', '   ')
    reports = contents.split('  ')
    unsafe_reports = []

    safe = 0
    for report in reports:
        report = report.strip().split(' ')
        if is_safe(report):
            safe += 1
        else:
            unsafe_reports.append(report)

    for u_report in unsafe_reports:
        for i in range(len(u_report)):
            dampened_report = deepcopy(u_report)
            dampened_report.pop(i)
            if is_safe(dampened_report):
                safe += 1
                break

    return safe
