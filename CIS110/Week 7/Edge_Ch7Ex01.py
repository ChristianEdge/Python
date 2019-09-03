'''
Program Name: Ch7Ex01
Program Description: 
Author: Christian Edge
Date created: 15 Jul 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    print("\n\tWelcome to Wage Calculator\n")

    hrs = float(input("Enter the number of hours worked : "))
    rate = float(input("Enter the hourly rate : "))

    wages = 0

    if hrs > 40:
        wages = (40 * rate) + ((hrs % 40) * (rate * 1.5))
    else:
        wages = hrs * rate
        
    print("Weekly wages : ${:.2f}".format(wages))

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 CH7Ex01")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
