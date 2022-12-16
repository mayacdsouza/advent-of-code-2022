file = open('day6.txt', 'r')
lines = file.readlines()
line = lines[0]

def find_marker(input_string):
    for i in range(0, len(input_string)-3):
        if input_string[i] not in input_string[i+1:i+4]:
            if input_string[i+1] not in input_string[i+2:i+4]:
                if input_string[i+2] != input_string[i+3]:
                    return i+4

print(find_marker(line))