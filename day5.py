dataSet = open("./day5DataSet.txt", "r")

coords = []
def addSegment(startPoint, endPoint):
    (x1,y1) = [int(val) for val in startPoint]
    (x2,y2) = [int(val) for val in endPoint]
    (x , y) = (x1 , y1)

    
    if x1 == x2:
        while y != y2:
            coords.append((x , y))
            if y1 > y2:
                y -= 1
            else:
                y +=1
        coords.append((x , y))

    elif y1 == y2:
        while x != x2:
            coords.append((x , y))
            if x1 > x2:
                x -= 1
            else:
                x += 1
        coords.append((x , y))
    else:
        while x != x2 and y != y2:
            coords.append((x , y))
            if y1 > y2:
                y -=1
                if x1 > x2:
                    x -= 1
                else:
                    x += 1
            else:
                y += 1
                if x1 > x2:
                    x -= 1
                else:
                    x += 1
        coords.append((x , y))

def returnDuplicates(testList):
    seen = set()
    seen_twice = set(pt for pt in testList if pt in seen or seen.add(pt))
    return list(seen_twice)

            

for line in dataSet:
    line = line.strip()
    listEndPoints = line.split('->')
    startPoint = listEndPoints[0].strip().split(',')    
    endPoint = listEndPoints[1].strip().split(',')
    addSegment(startPoint , endPoint)
    duplicates = returnDuplicates(coords)
answer = len(duplicates)
print (answer)
    


