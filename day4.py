dataSet = open("./day4DataSet.txt", "r")

numbersCalled = 0

class BingoSquare:
    def __init__(self, number):
        self.number= int(number)
        self.marked= False
    def __repr__(self):
        if self.marked:
            return 'X'
        return str(self.number)    

class BingoCard:
    def __init__(self):
        self.rows = []
    
    def addRow(self, row):
        self.rows.append([BingoSquare(num) for num in row.split()])
    
    def __repr__(self):
        return f'{self.rows}'
    
    def isrowwinner(self, row):
        for sqaure in row:
            if not sqaure.marked:
                return False
        return True

    def iscolumnwinner(self, column):
        for row in self.rows:
            if not row[column].marked:
                return False
        return True

    def isWinner(self):
        for row in self.rows:
            if self.isrowwinner(row):
                return True
        for i in range(5):
            if self.iscolumnwinner(i):
                return True
        return False

    def marknumber(self, number):
        for row in self.rows:
            for square in row:
                if square.number == number:
                    square.marked = True
                    return self.isWinner()
        return False
    
    def getscore(self):
        score = 0
        for row in self.rows:
            for sqaure in row:
                if not sqaure.marked:
                    score += sqaure.number
        return score


card = None
allCards = []
winningCards = []

for line in dataSet:
    line = line.strip()

    if not numbersCalled:
        numbersCalled = [int(num) for num in line.split(',')]
        continue

    if not line:
        if card:
            allCards.append(card)

        card = BingoCard()
        continue

    card.addRow(line)

allCards.append(card)

for num in numbersCalled:
    for card in allCards:
        winner = card.marknumber(num)

        if winner:
            if card not in winningCards:
                winningCards.append(card)
            print(num, card.getscore())
            answer = num * card.getscore()
            print(answer)
            if len(winningCards) == len(allCards):
                exit()

