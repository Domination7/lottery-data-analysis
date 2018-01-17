import csv


megaMillionTable = []
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

#   To read a value, the format is lotteryTable[row][column]

with open('MegaMillionsData.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        megaMillionTable.append(row)

#   Creates the table of all indexed lottery games
lotteryTable = []
lotteryTable.append("Mega Millions")


#   Choosing which lottery to view info of
counter = 0
for row in lotteryTable:
    print("{",counter,"}\t",row)
    
question = input("\nWhich lottery would you like to see? ")

question = input("Would you like to find a number? Y or N ")
if question == 'Y':
    rowValue = int(input("Row Number? "))
    colValue = int(input("Column Number? "))
    print(megaMillionTable[rowValue][colValue])

counter = 0
question = input("Would you like to see the numbers on a given day? Y or N ")
if question == 'Y':
    for i in megaMillionTable:
        if counter < 1:
            print("\n--- ",i[0]," ---")
            counter+=1
        else:
            print("{",counter,"}\t",i[0])
            counter+=1
