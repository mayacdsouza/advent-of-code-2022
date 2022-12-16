file = open('day6.txt', 'r')
lines = file.readlines()
line = lines[0]

def find_marker(input_string, unique):
    for i in range(0, len(input_string)-unique+1):
        index1 = i
        index2 = i+1
        index3 = i+unique
        counter = 0
        while counter < unique-1 and input_string[index1] not in input_string[index2:index3]:
            index1 +=1
            index2 +=1
            counter += 1
            if counter == unique-1:
                    return i+unique

print(find_marker(line, 14))