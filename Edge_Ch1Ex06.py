'''
Program Name: Chaos Program Ch1Ex06
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
    x2 = x
    x3 = x

    #Calculate and display output
    for i in range(100):
        x = 3.9 * x * (1-x)
        x2 = 3.9 * (x2 - x2 * x2)
        x3 = 3.9 * x3 - 3.9 * x3 * x3
        print(x, x2, x3)
    
    #Output to console the author, program, & date/time program was run
    print("Christian Edge")
    print("CIS110 Chaos Program Ch1Ex06")
    print(time.asctime(time.localtime(time.time())))

#Run the program          
main()
