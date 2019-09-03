'''
Program Name: Ch8Ex01
Program Description: 
Author: Christian Edge
Date created: 22 July 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    #Intro
    print("\nI determine the number in the Fibonacci Sequence based on the " +
          "number position you give me.\n")

    #Prompt/store user input
    number = int(input("What position in the Fibonacci Sequence would " +
                         "you like? : "))

    #Processing
    currentNum, previousNum = 1, 1

    for i in range(number - 2):
        currentNum, previousNum = currentNum + previousNum, currentNum

    #Output
    print("\nPosition", number, "of the Fibonacci sequence holds a value " +
          "of", currentNum)

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch8Ex01 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
