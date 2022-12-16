# store each line of a text as an element in lines
file = open('day2.txt', 'r')
lines = file.readlines()

points = 0

for line in lines:
    if line[2] == 'X':
        points += 0
        if line[0] == 'A':
            points += 3
        elif line[0] == 'B':
            points += 1
        else:
            points += 2


    elif line[2] == 'Y':
        points += 3
        if line[0] == 'A':
            points += 1
        elif line[0] == 'B':
            points += 2
        else:
            points += 3

    else:
        points +=6
        if line[0] == 'A':
            points += 2
        elif line[0] == 'B':
            points += 3
        else:
            points += 1

print(points)