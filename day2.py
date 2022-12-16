# store each line of a text as an element in lines
file = open('day2.txt', 'r')
lines = file.readlines()

points = 0

for line in lines:
    if line[2] == 'X':
        points += 1
        if line[0] == 'A':
            points += 3
        elif line[0] == 'C':
            points += 6

    elif line[2] == 'Y':
        points += 2
        if line[0] == 'B':
            points += 3
        elif line[0] == 'A':
            points += 6

    else:
        points +=3
        if line[0] == 'C':
            points += 3
        elif line[0] == 'B':
            points += 6

print(points)
