# store each line of a text as an element in lines
file = open('day4.txt', 'r')
lines = file.readlines()

pairs = 0

for line in lines:
    l_12, l_34 = line.split(",")
    l1, l2 = l_12.split("-")
    l3, l4 = l_34.split("-")
    l1 = int(l1)
    l2 = int(l2)
    l3 = int(l3)
    l4 = int(l4)
    if l1 <= l3 and l2 >= l3:
        pairs += 1
    elif l3 <= l1 and l4 >= l1:
        pairs += 1

print(pairs)
