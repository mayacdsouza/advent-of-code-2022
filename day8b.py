# read input data into forest
file = open('day8.txt', 'r')
forest = file.readlines()

def above(row, column, array):
    score = 0
    for i in range(row-1, -1, -1):
        if array[row][column] > array[i][column]:
            score += 1
        else:
            return score+1
    return score


def left(row, column, array):
    score = 0
    for j in range(column-1, -1, -1):
        if array[row][column] > array[row][j]:
            score += 1
        else:
            return score+1
    return score


def right(row, column, array):
    score = 0
    for j in range(column+1, len(array[0])):
        if array[row][column] > array[row][j]:
            score += 1
        else:
            return score+1
    return score


def below(row, column, array):
    score = 0
    for i in range(row+1, len(array)):
        if array[row][column] > array[i][column]:
            score += 1
        else:
            return score+1
    return score


def scenic_score(row, column, array):
    """Returns scenic score of tree."""
    return below(row, column, array) * above(row, column, array) * right(row, column, array) * left(row, column, array)

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

#calculate max_scenic score (iterate through interior trees to check)
max_scenic_score = 0
for i in range(1,height-1):
    for j in range(1, width-1):
        current_score = scenic_score(i, j, forest)
        if current_score > max_scenic_score:
            max_scenic_score = current_score

print(max_scenic_score)