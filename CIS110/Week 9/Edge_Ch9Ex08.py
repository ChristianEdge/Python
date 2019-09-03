'''
Program Name: Ch9Ex08
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

    n = int(input("How many games to simluate? : "))
    busts = 0    

    #Processing
    for i in range(n):
        points = dealHand()
        if points > 21:
            busts += 1

    printSummary(n, busts)
    outro()
#End main()
#****************

def intro():
    print("\n\t***Welcome to Ch9Ex08***\n")
    print("\tThis program simulates a Blakjack dealer.\n\n")

def dealHand():
    total = 0
    hasAce = False
    while total < 17:
        card = randrange(1,14)
        if card == 1:
            hasAce = True
        total += BJValue(card)
        if hasAce:
            total = adjForAce(total)
    return total

def BJValue(card):
    if card > 10:
        return 10
    else:
        return card

def adjForAce(total):
    if 16 < total + 10 < 22:
        return total + 10
    else:
        return total

def printSummary(n, busts):
    print("\nIn {0} hands dealer busted {1} times.".format(n, busts))
    print("Probability : ", float(busts / n))

def outro():
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ch9Ex08")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")


#Run the program          
if __name__ == '__main__':
    main()
