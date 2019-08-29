'''
Program Name: Ladder Length Calculator Ch3Ex10
Program Description: Determines the required length of a ladder
    to reach a given height and angle
Author: Christian Edge
Date created: 6 June 2019
Last modified: 6 June 2019
Notes of interest: Uses "time" amd "math" modules
'''

import time
import math

def main():
    #Introduction
    print("Welcome to the Ladder Length Calculator. \nI determine the " +
          "required length of a ladder to reach a given height and " +
          "angle.\n")

    #Get and store user input
    height = float(input("What is the height to be reached? : "))
    print()
    degrees = float(input("What is the angle of the ladder in degrees? : "))

    #Perform calculations
    radians = math.pi * degrees / 180
    length = height / math.sin(radians)

    #Output data to user
    print("\nThe ladder must be at least", math.ceil(length), "feet long.")

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ladder Length Calculator Ch3Ex10")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
