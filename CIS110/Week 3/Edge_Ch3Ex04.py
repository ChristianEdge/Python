'''
Program Name: Lightning Strike Calculator Ch2Ex04
Program Description: Determines distance to a lightning strike based
    on the amount of time elapsed between the lightning flash and the
    sound of thunder.
Author: Christian Edge
Date created: 6 June 2019
Last modified: 7 June 2019
Notes of interest: Uses "time" module
'''

import time

def main():
    #Introduction
    print("Welcome to the Lightning Strike Calculator. \nI determine " +
          "the distance you are to a lightning strike based on the " +
          "amount of time elapsed between the lightning flash and the " +
          "sound of thunder.\n")

    #Get and store user input
    seconds = float(input("How many seconds have passed since you saw " +
                          "the lightning strike? (Hint: You can use a " +
                          "decimal number): "))
    
    #Perform calculations
    #Sound travels roughly 1100 feet per second
    feet = 1100.0 * seconds
    #Divide by number of feet in a mile 
    distance = feet / 5280.0

    #Output data to user
    print("The distance is around", round(distance, 1), "miles")

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Lightning Strike Calculator Ch2Ex04")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
