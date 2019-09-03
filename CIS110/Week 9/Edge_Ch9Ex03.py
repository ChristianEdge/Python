'''
Program Name: Ch9Ex03
Program Description: 
Author: Christian Edge
Date created: 29 July 2019
Last modified: 
Notes of interest: Uses time module
'''

import time
import random

def main():
    intro()

    probA, probB, n = getInputs()

    #Processing
    winsA, winsB   = simNGames(n, probA, probB)
    
    printSummary(winsA, winsB)
    outro()
    
#End main()
#****************

def intro():
    print("\n\t***Welcome to Program Ch9Ex03***\n")
    print("This program simulates a game of volleyball between two players,")
    print("'A' & 'B'. The abilities of each player are indicated by a probability")
    print("(number between 0 and 1) that the player wins the point when serving.")
    print("Player A always serves first.")

def getInputs():
    a = float(input("Enter the probability that player A wins the serve (0 - 1) : "))
    b = float(input("Enter the probability that player B wins the serve (0 - 1) : "))
    n = int(input("How many games to simulate? : "))
    return a, b, n

def simNGames(n, probA, probB):
    winsA = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(i, probA, probB)
        if scoreA > scoreB:
            winsA += 1
    winsB = n - winsA
    return winsA, winsB

def simOneGame(n, probA, probB):
    if n % 2 == 0:
        serving = "B"
    else:
        serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random.random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random.random() < probB:
                scoreB += 1
            else:
                serving = "A"
    print("Player A score :", scoreA, "\tPlayer B score:", scoreB)
    return scoreA, scoreB

def gameOver(a, b):
    return (a >= 15 and a - b >= 2) or (b >= 15 and b - a >= 2)

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("\nGames simulated :", n)
    print("Wins for A: {0} ({1:0.1%})".format(winsA, (winsA / n)))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, (winsB / n)))

def outro():
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")


#Run the program          
if __name__ == '__main__':
    main()
