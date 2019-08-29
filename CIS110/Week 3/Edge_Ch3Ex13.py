'''
Program Name: Sum of a Series Ch3Ex13
Program Description: Outputs the sum of a series of numbers input by the
    user
Author: Christian Edge
Date created: 7 June 2019 
Last modified: 7 June 2019
Notes of interest: Uses "time" module
'''

import time

def main():
    #Introduction
    print("Welcome to the Sum of a Series program. I give you the sum " +
          "of a list of numbers you give me. First, tell me...")

    #Prompt user for input and store
    length = int(input("How many items are in your list? : "))
    print()

    total = 0.0

    #Loop the user-specified number of times
    #Prompt for input and add to total
    for i in range(length):
        total += float(input("What is the next number on your list? : "))

    #Output data to user
    print("\nThe sum of your numbers is", total)

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Sum of a Series Ch3Ex13")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
