import csv


lotteryTable = []
#   These are all the column numbers
date = 0
numOne = 1
numTwo = 2
numThree = 3
numFour = 4
numFive = 5
megaBall = 6
whiteBallNum = 9
whiteBallCo = 10
megaBallNum = 12
megaBallCo = 13


with open('MegaMillionsData.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        lotteryTable.append(row)

#   To read a value, the format is lotteryTable[row][column]


