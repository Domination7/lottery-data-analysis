import csv

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
lotteryTable.append("Powerball")


#   Choosing which lottery to view info of
counter = 0
for row in lotteryTable:
    print("{",counter,"}\t",row)
    counter+=1
   
question = int(input("\nWhich lottery would you like to see? -- "))

#   This is the current lottery chosen by the user
if question == 0 :
    currentLottery = megaMillionTable

if question == 1 :
    currentLottery = powerballTable
   
#   A main menu method, should be accessed after every method is complete
def mainMenu():
    print("\n{ 0 }  Change the lottery type being accessed")
    print("{ 1 }  View the winning numbers on a chosen day")
    print("{ 2 }  Top 10 most popular numbers")
    print("{ 3 }  Top 5 most popular powerball/megaball numbers")
    print("{ 4 }  Find any number")
    answer = int(input("\nWhich data? "))
    if answer == 1:
        print("Maybe later")
    
    if answer == 2:
        print("Maybe Later")
    
    if answer == 3:
        print("Maybe Later")
        
    if answer == 4:
        numberFind()

#   Method for finding a number given coordinates for CSV file
def numberFind():
    if question == 'Y':
        rowValue = int(input("Row Number? "))
        colValue = int(input("Column Number? "))
        print(currentLottery[rowValue][colValue])


mainMenu()
#   Printing all the dates stored of the given lottery
counter = 0
question = input("\nWould you like to see the numbers on a given day? Y or N -- ")
if question == 'Y':
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
                
