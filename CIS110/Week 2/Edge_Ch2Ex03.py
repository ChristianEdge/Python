'''
Program Name: Avg2 Program Ch2Ex03
Program Description: Computes average of 3 numbers
Author: Christian Edge
Date created: 3 June 2019
Last modified: 3 June 2019
Notes of interest: Uses "time" module
'''

import time

def main():
    #Output introduction to user
    print("Welcome to the Three Averages Program. I compute the average of three " +
          "exam scores.\n", end = "\n")
    
    #Get and store user input
    x, y, z = eval(input("Enter three scores separated by a comma: "))

    #Perform the calculation and store it
    average = (x + y + z) / 3
    
    #Output the result to user
    print("The average score is: ", round(average, 2))
    
    #Output to console the author, program, & date/time program was run
    print("\nChristian Edge")
    print("CIS110 Avg2 Program Ch2Ex03")
    print(time.asctime(time.localtime(time.time())))
    input("\n\nPress <Enter> to Quit\n\n")

#Run the program          
main()
