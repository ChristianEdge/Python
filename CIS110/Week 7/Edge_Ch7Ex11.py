'''
Program Name: Ch7Ex11
Program Description: 
Author: Christian Edge
Date created: 15 Jul 2017
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    print("\n\tLeap Year Calculator\n")
    
    year = int(input("Input a year : "))

    #0 == False, any non-zero value == True
    if not year % 400 or (year % 100 and not year % 4):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
        
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ch7Ex11 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
