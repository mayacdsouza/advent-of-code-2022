# read input moves
file = open('day9.txt', 'r')
moves = file.readlines()

head = [0, 0]
tail = [0, 0]
tail_pos = []


def check_pos(head, tail):
    if abs(head[0]-tail[0]) == 1 and abs(head[1]-tail[1]) == 1:
        return True
    else:
        return False


for move in moves:
    direction, distance = move.split(' ')
    distance = int(distance)
    if direction == 'D':
        for i in range(0, distance):
            head[0] += 1
            if not check_pos(head, tail):
                tail[0] += 1
                if tail not in tail_pos:
                    tail_pos.append([tail[0],tail[1]])
    elif direction == 'U':
        for i in range(0, distance):
            head[0] -= 1
            if not check_pos(head, tail):
                tail[0] -= 1
                if tail not in tail_pos:
                    tail_pos.append([tail[0],tail[1]])
    elif direction == 'L':
        for i in range(0, distance):
            head[1] -= 1
            if not check_pos(head, tail):
                tail[1] -= 1
                if tail not in tail_pos:
                    tail_pos.append([tail[0],tail[1]])
    elif direction == 'R':
        for i in range(0, distance):
            head[1] += 1
            if not check_pos(head, tail):
                tail[1] += 1
                if tail not in tail_pos:
                    tail_pos.append([tail[0],tail[1]])

print((tail_pos))

