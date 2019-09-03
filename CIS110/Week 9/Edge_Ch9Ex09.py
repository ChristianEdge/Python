'''
Program Name: Ch9Ex09
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

    n = int(input("How many trials for each start value? : "))

    print("\nStart | Probability of Bust")
    print("-" * 30)

    for start in range (1, 11):
        busts = simHands(n, start)
        print("{0:3}   | {1:12.2f}".format(start, busts / n))

    outro()
#End main()
#****************

def intro():
    print("\n\t***Welcome to Ch9Ex09***\n")
    print("\tThis program simulates a Blakjack dealer.\n\n")

def dealHand(start):
    total = start
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

def simHands(n, start):
    busts = 0
    for i in range(n):
        points = dealHand(start)
        if points > 21:
            busts += 1
    return busts

def outro():
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ch9Ex09")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")


#Run the program          
if __name__ == '__main__':
    main()
