
dataset = open("./day1DataSet.txt", "r")
previousLine = None
previousLine2 = None
previousLine3 = None
previousLine4 = None
currentCount = 0
currentLine = 0
for line in dataset:
    line = int(line)
    currentLine +=1
    if currentLine == 1 or currentLine == 2 or currentLine == 3:
        pass
    elif line > previousLine3:
        currentCount += 1
    previousLine4 = previousLine3
    previousLine3 = previousLine2
    previousLine2 = previousLine
    previousLine = line
print(currentCount)