'''
Program Name: Convert Program Ch2Ex01
Program Description: Converts degrees Celsius to Fahrenheit
Author: Christian Edge
Date created: 3 June 2019
Last modified: 3 June 2019
Notes of interest: Uses "time" module
'''

import time

def main():
    #Output introduction to user
    print("Welcome to the Conversion Program. I convert temperatures from\n" +
          "Celsius to Fahrenheit. Please enter a number.", end = "\n")
    
    #Get and store user input
    celsius = eval(input("What is the temperature in Celsius? "))

    #Perform the calculation and store it
    fahrenheit = 9 / 5 * celsius + 32
    
    #Output the result to user
    print("The temperature is", round(fahrenheit, 1), "degrees Fahrenheit. \n")
    
    #Output to console the author, program, & date/time program was run
    print("Christian Edge")
    print("CIS110 Convert Program Ch2Ex01")
    print(time.asctime(time.localtime(time.time())))
          
main()
