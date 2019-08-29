'''
Program Name: Convert Program Ch2Ex09
Program Description: Converts degrees Fahrenheit to Celsius
Author: Christian Edge
Date created: 3 June 2019
Last modified: 3 June 2019
Notes of interest: Uses "time" module
'''

import time

def main():
    #Output introduction to user
    print("Welcome to the Conversion Program. I convert temperatures from\n" +
          "Fahrenheit to Celsius.", end = "\n")
    
    #Get and store user input
    fahrenheit = eval(input("What is the temperature in Fahrenheit? "))
        
    #Perform the calculation and store it
    celsius = (fahrenheit - 32) / (9 / 5)
        
    #Output the result to user
    print("The temperature is", round(celsius, 1), "degrees Celsius. \n")
    
    #Output to console the author, program, & date/time program was run
    print("\nChristian Edge")
    print("CIS110 Convert Program Ch2Ex09")
    print(time.asctime(time.localtime(time.time())))
    input("\n\nPress <Enter> to Quit\n\n")

#Run the program          
main()
