# read input data into forest
file = open('day8.txt', 'r')
forest = file.readlines()


def above(row, column, array):
    for i in range(0, row):
        if array[row][column] <= array[i][column]:
            return False
    return True


def left(row, column, array):
    for j in range(0, column):
        if array[row][column] <= array[row][j]:
            return False
    return True


def right(row, column, array):
    for j in range(column+1, len(array[0])):
        if array[row][column] <= array[row][j]:
            return False
    return True


def below(row, column, array):
    for i in range(row+1, len(array)):
        if array[row][column] <= array[i][column]:
            return False
    return True


def is_visible(row, column, array):
    """Returns True if tree is visible."""
    return below(row, column, array) or above(row, column, array) or right(row, column, array) or left(row, column, array)

# find total trees in forest
width = len(forest[0])-1
height = len(forest)
total_trees = width*height

# convert forest to an array
for i in range(0,height):
    row = []
    for j in range(0,width):
        row.append(int(forest[i][j]))
    forest[i] = row

# calculate trees visible because they are on the boundary of the forest
trees_visible = 2*(width+height)-4

# calculate trees visible in the interior (iterate through interior trees to check)
for i in range(1,height-1):
    for j in range(1, width-1):
        if is_visible(i,j,forest):
            trees_visible += 1

print(trees_visible)