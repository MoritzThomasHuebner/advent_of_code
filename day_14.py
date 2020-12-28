import numpy as np

instructions = []
with open('day_14_input.txt', 'r') as f:
    for i, line in enumerate(f.readlines()):
        instructions.append(line.strip('\n'))


class Program(object):

    def __init__(self, mask='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'):
        self.mask = mask
        self.memory = dict()

    def process_instruction(self, instruction):
        if instruction.startswith('mask'):
            self.mask = instruction.replace('mask = ', '')
        elif instruction.startswith('mem'):
            i = instruction.replace('mem[', '').replace(' = ', '').split(']')
            self.assign_value(address=i[0], value=i[1])

    def assign_value(self, address, value):
        value_string = str(bin(int(value))).replace('0b', '').zfill(len(self.mask))
        output_string = '0b'
        for v, m in zip(value_string, self.mask):
            if m == 'X':
                output_string += v
            else:
                output_string += m
        output = int(output_string, 2)
        self.memory[address] = output

    def compute_sum(self):
        return np.sum([int(v) for v in self.memory.values()])


p = Program()
for instruction in instructions:
    p.process_instruction(instruction=instruction)
print(p.compute_sum())


# Part 2


class ProgramPartTwo(Program):

    def assign_value(self, address, value):
        address_string = str(bin(int(address))).replace('0b', '').zfill(len(self.mask))
        target_address = ''
        for v, m in zip(address_string, self.mask):
            if m == '0':
                target_address += v
            else:
                target_address += m
        for a in self.get_addresses(target_address):
            if int(a, 2) == 29453753730:
                print()
            self.memory[int(a, 2)] = int(value)

    def get_addresses(self, address):
        if "X" in address:
            for replacement in ('0', '1'):
                yield from self.get_addresses(address.replace('X', replacement, 1))
        else:
            yield address

    def compute_sum(self):
        return sum(self.memory.values())


p2 = ProgramPartTwo()
for instruction in instructions:
    p2.process_instruction(instruction=instruction)
print(p2.compute_sum())
