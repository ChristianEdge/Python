'''
Program Name: Ch9Ex11
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

    n = int(input("How many rolls to simulate? : "))
    hits = 0
    
    #Processing
    for i in range(n):
        if equalRolls(5):
            hits += 1
            
    printSummary(n, hits)
    outro()
#End main()
#****************

def intro():
    print("\n\t***Welcome to Ch9Ex11***\n")
    print("This program esitmates the probability of rolling five of a kind")
    print("on a single roll of 5 dice.\n\n")

def equalRolls(count):
    first = randrange(1, 7)
    for i in range(count - 1):
        roll = randrange(1, 7)
        if roll != first:
            return False
    return True

def printSummary(n, hits):
    print("Estimated probability : ", float(hits / n))

def outro():
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch9Ex11")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")


#Run the program          
if __name__ == '__main__':
    main()
