'''
Program Name: Chaos Program Ch1Ex05
Program Description: Demonstrates chaotic behavior in computers
Author: Christian Edge
Date created: 28 May 2019
Date last modified: 28 May 2019
Notes of interest: Uses "time" module
'''

import time

def main():
    print("This program illustrates a chaotic function.")

    #Output instructions to user, get and store user input
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print?"))

    #Calculate and display output
    for i in range(n):
        x = 2.0 * x * (1-x)
        print(x)
    
    #Output to console the author, program, & date/time program was run
    print("Christian Edge")
    print("CIS110 Chaos Program Ch1Ex05")
    print(time.asctime(time.localtime(time.time())))

#Run Program          
main()
