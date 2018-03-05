import csv
import time

#   The indexed lottery matrices
megaMillionTable = []
powerballTable = []
currentLottery = []

#   These are all the column numbers
date = 0
numOne = 1
numTwo = 2
numThree = 3
numFour = 4
numFive = 5
specialBall = 6   # Either Megaball or Powerball
whiteBallNum = 8
whiteBallCo = 9
whiteBallPer = 10
specialBallNum = 12  # Either Megaball or Powerball
specialBallCo = 13  # Either Megaball or Powerball
specialBallPer = 14  # Either Megaball or Powerball

checkLetter = True

#   To read a value, the format is lotteryTable[row][column]
with open('MegaMillionsData.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        megaMillionTable.append(row)

with open('PowerballData.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        powerballTable.append(row)


#   Creates the table of all indexed lottery games
lotteryTable = []
lotteryTable.append("Mega Millions")
lotteryTable.append("Powerball")



def changeLottery():
    counter = 0
    global question
    global currentName
    global currentLottery
    for row in lotteryTable:
        print("{",counter,"}\t",row)
        counter+=1
    question = int(input("\nWhich lottery would you like to see? -- "))
    if question == 0 :
        currentLottery = megaMillionTable
        currentName = "Mega Millions"
        
    if question == 1 :
        currentLottery = powerballTable
        currentName = "Powerball"
changeLottery() #First method executed

#   A main menu method, should be accessed after every method is complete
#   2 and 3 will be done in excel, than accessed through python
def mainMenu():
    print("\n-----------------------------------------------------")
    print("    The Current lottery is the",currentName)
    print("-----------------------------------------------------")
    print("{ 00 }  Change the lottery type being accessed")
    print("{ 01 }  View the winning numbers on a chosen day")
#    print("{ 02 }  Top 10 most popular numbers")
#    print("{ 03 }  Top 5 most popular powerball/megaball numbers")
    print("{ 04 }  Find any number")
#    print("{ 05 } Highest lottery value")
    print("{ 98 }  View raw data") 
    print("{ 99 }  Exit")
    answer = int(input("\nWhich data? "))
    if answer == 0:
        changeLottery()
        
    if answer == 1:
        numberGivenDay()
    
    if answer == 2:
        print("\n--- WIP ---\n")
    
    if answer == 3:
        print("\n--- WIP ---\n")
        
    if answer == 4:
        numberFind()
        
    if answer == 5:
        print("\n--- WIP --\n")
        
    if answer == 98:
        viewTable()
        
    if answer == 99:
        exit()
#    time.sleep(3)

#   Method for finding a number given coordinates for CSV file
def numberFind():
    rowValue = int(input("Row Number? "))
    colValue = int(input("Column Number? "))
    print(currentLottery[rowValue][colValue])
    time.sleep(3)
        
def numberGivenDay():
    counter = 0
    for i in currentLottery:
        if counter < 1:
            print("\n--- ",i[0]," ---")
            counter+=1
        else:
            if(i[0] != ""):
                print("{",counter,"}\t",i[0])
                counter+=1
                    
    question = int(input("\nWhich day? -- "))
    print()
    print(currentLottery[question][0],"---",currentLottery[question][1],"",currentLottery[question][2],"",currentLottery[question][3],"",currentLottery[question][4],"",currentLottery[question][5],"   ",currentLottery[question][6])
    time.sleep(3)
    
def viewTable():
    for row in currentLottery:
        print(row) 
    time.sleep(3)

while True:
    mainMenu()
                
