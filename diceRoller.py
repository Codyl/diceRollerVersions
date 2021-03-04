import math
import random

class DiceRoller:
    # Total times the dice has been rolled
    # What the die currently shows was rolled
    # The number of times each number has been rolled
    # For example if I had a 6 sided die
    # and I roll the following numbers: 1, 1, 6, 3, 3
    # the output could be: 1:2, 2:0, 3:2, 4:0, 5:0, 6:1
    def __init__(self,totalSides):
        self.totalSides = totalSides
        self.diceRolls = []
    def getRandomNumber (self,max): 
        return math.ceil(random.random() * max)

dice = DiceRoller(6)
for roll in range(6):
    dice.diceRolls.append(dice.getRandomNumber(dice.totalSides))
    print('Current Dice Rolls: ')
    for roll in dice.diceRolls:
        print(roll)
    print('Total Dice Rolls: ')
    print(len(dice.diceRolls))
print('Dice Roll History: ')
for side in range(1,dice.totalSides+1):
    print('{}:{}'.format(side,dice.diceRolls.count(side)))