# store each line of a text as an element in lines
file = open('day5.txt', 'r')


def num_stacks(input_file):
    lines = input_file.readlines()
    stack_height = 0
    for line in lines:
        num = 1
        if str(num) in line:
            while str(num) in line:
                num += 1
            return num-1, stack_height
        stack_height += 1




number_of_stacks, stack_height = num_stacks(file)
stacks = []
for i in range(0, number_of_stacks):
    stacks.append('')
file = open('day5.txt', 'r')
lines = file.readlines()
for i in range(0, stack_height):
    line = lines[i]
    for j in range(0, number_of_stacks):
        index = 4*j+1
        if len(line) > index:
            if line[index] != ' ':
                stacks[j] += line[index]

for i in range(stack_height+2, len(lines)):
    line = lines[i].split('move ')
    line = line[1]
    line = line.split(' from ')
    num_blocks = int(line[0])
    line = line[1].split(' to ')
    start = int(line[0])-1
    end = int(line[1])-1
    stacks[end] = stacks[start][0:num_blocks]+stacks[end]
    stacks[start] = stacks[start][num_blocks:]

output_string = ''
for stack in stacks:
    output_string += stack[0]

print(output_string)