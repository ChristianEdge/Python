'''
Program Name: Ch8Ex04
Program Description: 
Author: Christian Edge
Date created: 22 July 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    #Intro
    print("\nI generate the Syracuse Sequence based on the " +
          "number you give me.\n")

    number = int(input("Please provide a number : "))

    print("Your sequence is : ")
    while number != 1:
        print(int(number), end = ' ')

        if number % 2 == 0:
            number = number / 2
        else:
            number = 3 * number + 1
    print(1)

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch8Ex04 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
