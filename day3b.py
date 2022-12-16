# store each line of a text as an element in lines
file = open('day3.txt', 'r')
lines = file.readlines()

total = 0

def shared_cargo(cargo1, cargo2, cargo3):
    for char in cargo1:
        if (char in cargo2) and (char in cargo3):
            if ord(char) > 96:
                return ord(char) - 96
            else:
                return ord(char) - 38

groups = int(len(lines)/3)
for i in range(0, groups):
    total += shared_cargo(lines[3*i], lines[3*i+1], lines[3*i+2])

print(total)