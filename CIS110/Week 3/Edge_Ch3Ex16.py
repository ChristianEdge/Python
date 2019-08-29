'''
Program Name: Fibonacci Sequence Ch03Ex16
Program Description: Determines the number in the Fibonacci sequence
    based on user input
Author: Christian Edge
Date created: 7 June 2019
Last modified: 7 June 2019
Notes of interest: Uses "time" module
'''

import time

def main():
    #Introduction
    print("Welcome to the Fibonacci Sequence Calculator. \nI determine the " +
          "number in the Fibonacci Sequence based on the number position " +
          "you give me.\n")

    #Get and store user input
    number = int(input("What position in the Fibonacci Sequence would " +
                         "you like? : "))

    #Perform calculations
    #The next number of the Fibonacci sequnece is the sum of the current
    #number and the previous number. The first two number are both 1s.
    currentNum, previousNum = 1, 1
    
    #We must subtract the first two positions from the users' input
    for i in range(number - 2):
        currentNum, previousNum = currentNum + previousNum, currentNum


    print("\nPosition", number, "of the Fibonacci sequence holds a value " +
          "of", currentNum)
    
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Fibonacci Sequence Ch03Ex16")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
