import random
random.seed()

class diceGame:
    diceTable = []
    nDice = 0
    points = 0
    def __init__(self):
        pass

    def calPoints(self):
        tabCopy = self.diceTable.copy()
        points = 0
        for x in tabCopy:
            if tabCopy.count(x) > 1:
                points += x*tabCopy.count(x)
                while tabCopy.count(x) != 0:
                    tabCopy.pop(tabCopy.index(x))
        self.points = points

    def throw(self):
        while self.nDice < 3 or self.nDice > 10: self.nDice = int(input("Ile kostek chcesz rzucić?(3 - 10): "))
        for x in range(0, self.nDice): 
            self.diceTable.append(random.randint(1,6))
            print(f"Kostka {x+1}: {self.diceTable[x]}")
        self.calPoints()

    def play(self):
        self.throw()
        print("Liczba uzyskanych punktów:", self.points)
        if input("Jeszcze raz? (t/n): ") == "t":
            self.diceTable.clear()
            self.play()

game = diceGame()
game.play()