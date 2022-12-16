# store each line of a text as an element in lines
file = open('day3.txt', 'r')
lines = file.readlines()

total = 0

def shared_cargo(cargo1, cargo2):
    for char in cargo1:
        if char in cargo2:
            if ord(char) > 96:
                return ord(char) - 96
            else:
                return ord(char) - 38


for line in lines:
    length = int((len(line)-1)/2)
    c1 = line[:length]
    c2 = line[length:]
    total += shared_cargo(c1, c2)

print(total)
