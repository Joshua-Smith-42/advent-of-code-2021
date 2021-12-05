

dataset = open("./day2DataSet.txt", "r")

horizontalPosition = 0
aim = 0
depth = 0

for line in dataset:
    value = int(line[-2:])
    direction = str(line[:-2])
    if direction == "up " or direction == "down ":
        if direction == "up ":
            value = -value
        aim += value
    else:
        horizontalPosition += value
        depth += aim * value
answer = horizontalPosition * depth
print(answer)
