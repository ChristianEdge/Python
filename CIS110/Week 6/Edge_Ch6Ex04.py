'''
Program Name: Ch6Ex04
Program Description: gives sum of first n natural numbers and
    sum of cubes of first n natural numbers
Author: Christian Edge
Date created: 28 June 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    print("This program returns the sum of the first n natural numbers and" +
          " the sum of the cubes of the first n natural numbers.\n")

    number = int(input("Enter a whole number : "))

    x = sumN(number)
    y = sumNCubes(number)

    print("\nThe sum of the first " + str(number) + " natural numbers is " +
          str(x))
    print("The sum of the cubes of the first " + str(number) + " natural " +
          "numbers is " + str(y))    

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Program Ch6Ex04 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Define functions
def sumN(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sumNCubes(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total

#Run the program          
main()
