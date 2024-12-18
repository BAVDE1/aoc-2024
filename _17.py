import math
import re
from copy import deepcopy

from utils import read_file


def _a():
    registers, instructions = read_file(17).split('\n\n')
    registers = [int(n) for n in re.findall('\d+', registers)]
    instructions = [int(n) for n in re.findall('\d+', instructions)]

    output = []
    instruction_pointer = [0]  # in a list so value can be set in nested functions

    def get_register_value(register_char: str):
        return registers[{'a': 0, 'b': 1, 'c': 2}[register_char.lower()]]

    def set_register_value(register_char: str, value):
        registers[{'a': 0, 'b': 1, 'c': 2}[register_char.lower()]] = value

    def get_combo_value(operand):
        if operand < 4:
            return operand
        return {4: get_register_value('a'), 5: get_register_value('b'), 6: get_register_value('c')}[operand]

    def do_division(into_register: str, operand):
        result = get_register_value('a') / (2 ** get_combo_value(operand))
        set_register_value(into_register, math.floor(result))

    # division into a
    def adv(operand):
        do_division('a', operand)
        return 2

    # bitwise xor into b
    def bxl(operand):
        set_register_value('b', get_register_value('b') ^ operand)
        return 2

    # modulo
    def bst(operand):
        set_register_value('b', get_combo_value(operand) % 8)
        return 2

    # nothing if reg a is 0, else jump to literal operand
    def jnz(operand):
        if get_register_value('a') == 0:
            return 2
        instruction_pointer[0] = operand
        return 0

    # bitwise xor of b and c, into b
    def bxc(operand):
        set_register_value('b', get_register_value('b') ^ get_register_value('c'))
        return 2

    # output
    def out(operand):
        output.append(get_combo_value(operand) % 8)
        return 2

    # division into b
    def bdv(operand):
        do_division('b', operand)
        return 2

    # division into c
    def cdv(operand):
        do_division('c', operand)
        return 2

    instruction_jump_table = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}
    while instruction_pointer[0] < len(instructions):
        ptr = instruction_pointer[0]
        opcode, operand = instructions[ptr], instructions[ptr+1]

        pointer_addition = instruction_jump_table[opcode].__call__(operand)
        instruction_pointer[0] += pointer_addition
    return ','.join([str(o) for o in output])


def _b():
    registers, instructions = read_file(17).split('\n\n')
    registers = []
    instructions = [int(n) for n in re.findall('\d+', instructions)]

    output = []
    expected_output = deepcopy(instructions)
    instruction_pointer = [0]  # in a list so value can be set in nested functions

    def get_register_value(register_char: str):
        return registers[{'a': 0, 'b': 1, 'c': 2}[register_char.lower()]]

    def set_register_value(register_char: str, value):
        registers[{'a': 0, 'b': 1, 'c': 2}[register_char.lower()]] = value

    def get_combo_value(operand):
        if operand < 4:
            return operand
        return {4: get_register_value('a'), 5: get_register_value('b'), 6: get_register_value('c')}[operand]

    def do_division(into_register: str, operand):
        result = get_register_value('a') / (2 ** get_combo_value(operand))
        set_register_value(into_register, math.floor(result))

    # division into a
    def adv(operand):
        do_division('a', operand)
        return 2

    # bitwise xor into b
    def bxl(operand):
        set_register_value('b', get_register_value('b') ^ operand)
        return 2

    # modulo
    def bst(operand):
        set_register_value('b', get_combo_value(operand) % 8)
        return 2

    # nothing if reg a is 0, else jump to literal operand
    def jnz(operand):
        if get_register_value('a') == 0:
            return 2
        instruction_pointer[0] = operand
        return 0

    # bitwise xor of b and c, into b
    def bxc(operand):
        set_register_value('b', get_register_value('b') ^ get_register_value('c'))
        return 2

    # output
    def out(operand):
        output.append(get_combo_value(operand) % 8)
        return 2

    # division into b
    def bdv(operand):
        do_division('b', operand)
        return 2

    # division into c
    def cdv(operand):
        do_division('c', operand)
        return 2

    instruction_jump_table = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

    i = 0
    while output != expected_output:
        registers = [i, 0, 0]
        instruction_pointer[0] = 0
        i += 1
        output = []

        while instruction_pointer[0] < len(instructions):
            ptr = instruction_pointer[0]
            opcode, operand = instructions[ptr], instructions[ptr+1]

            pointer_addition = instruction_jump_table[opcode].__call__(operand)
            instruction_pointer[0] += pointer_addition
    return i-1
