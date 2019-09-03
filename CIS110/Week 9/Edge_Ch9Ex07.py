'''
Program Name: Ch9Ex07
Program Description: 
Author: Christian Edge
Date created: 29 July 2019
Last modified: 
Notes of interest: Uses time module
'''

import time
from random import randrange

def main():
    intro()

    n = int(input("How many games to simulate? : "))

    #Processing
    wins = simNGames(n)

    printSummary(wins, n)
    outro()
#End main()
#****************

def intro():
    print("\n\t***Welcome to Ch9Ex07***\n")
    print("This program establishes the probability of winning at craps\n")

def simNGames(n):
    wins= 0
    for i in range(n):
        if winCraps():
            wins += 1
    return wins

def winCraps():
    roll = rollDice()
    if roll == 7 or roll == 11:
        return True
    elif roll == 2 or roll == 3 or roll == 12:
        return False
    else:
        return rollForPoint(roll)

def rollDice():
    return randrange(1, 7) + randrange(1, 7)

def rollForPoint(toMake):
    roll = rollDice()
    while roll != 7 and roll != toMake:
        roll = rollDice()
    return roll == toMake
    
def printSummary(wins, n):
    print("\nThe player wins", wins, "games.")
    print("The probability of a win is : {0:0.2f}%".format(wins / n * 100))
    
def outro():
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch9Ex07")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")


#Run the program          
if __name__ == '__main__':
    main()
