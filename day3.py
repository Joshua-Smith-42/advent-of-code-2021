

gammaRate = ''
epsilonRate = ''
lineCount = 0

numDigits = 12
columnSum = [0] * numDigits


for line in open("./day3DataSet.txt", "r"):
    lineCount += 1

    for i in range(numDigits):
        columnSum[i] += int(line[i])

for i in range(len(columnSum)):
    if columnSum[i] > lineCount/2:
        gammaRate += "1"
        epsilonRate += "0"
    else:
        gammaRate += "0"
        epsilonRate += "1"

print(gammaRate, epsilonRate)
        
gammaRate = int(gammaRate, 2)
epsilonRate = int(epsilonRate, 2)

powerConsumption = gammaRate * epsilonRate
print(powerConsumption)