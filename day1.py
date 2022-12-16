
# store each line of a text as an element in lines
file = open('day1.txt', 'r')
lines = file.readlines()

current_calories = 0
max_calories = 0
max2_calories = 0
max3_calories = 0

for line in lines:
    if len(line) == 1:
        if current_calories > max_calories:
            max3_calories = max2_calories
            max2_calories = max_calories
            max_calories = current_calories
        elif current_calories > max2_calories:
            max3_calories = max2_calories
            max2_calories = current_calories
        elif current_calories > max3_calories:
            max3_calories = current_calories
        current_calories = 0
    else:
        current_calories += int(line)

if current_calories > max_calories:
    max3_calories = max2_calories
    max2_calories = max_calories
    max_calories = current_calories
elif current_calories > max2_calories:
    max3_calories = max2_calories
    max2_calories = current_calories
elif current_calories > max3_calories:
    max3_calories = current_calories

print(max_calories + max2_calories + max3_calories)
