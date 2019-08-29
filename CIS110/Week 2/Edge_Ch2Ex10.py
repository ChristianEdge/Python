'''
Program Name: Convert Distance Program Ch2Ex10
Program Description: Converts distance from kilometers to miles
Author: Christian Edge
Date created: 3 June 2019
Last modified: 3 June 2019
Notes of interest: Uses "time" module
'''

import time

def main():
    #Output introduction to user
    print("Welcome to the Distance Conversion Program. I convert distances from\n" +
          "kilometers to miles.", end = "\n")
    
    #Get and store user input
    kilometers = eval(input("What is the distance in kilometers? "))
        
    #Perform the calculation and store it
    miles = kilometers * 0.62
        
    #Output the result to user
    print(round(kilometers, 1), "kilometers is around", round(miles, 1),
          "miles.")
    
    #Output to console the author, program, & date/time program was run
    print("\n\nChristian Edge")
    print("CIS110 Convert Distance Program Ch2Ex10")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
