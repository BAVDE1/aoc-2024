from utils import read_file


def _a():
    contents = read_file(1).replace('\n', '   ')

    list_a = contents.split('   ')[0::2]
    list_a.sort()
    list_b = contents.split('   ')[1::2]
    list_b.sort()

    sum = 0
    for i in range(len(list_a)):
        sum += abs(int(list_a[i]) - int(list_b[i]))
    return sum


def _b():
    contents = read_file(1).replace('\n', '   ')

    list_a = contents.split('   ')[0::2]
    list_a.sort()
    list_b = contents.split('   ')[1::2]
    list_b.sort()

    sum = 0
    for num in list_b:
        if num in list_a:
            sum += int(num) * list_a.count(num)
    return sum
