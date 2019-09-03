'''
Program Name: Ch7Ex08
Program Description: 
Author: Christian Edge
Date created: 15 July 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():
    print("\n\tAge/Citizenship Requirements for Congress\n")
    
    age = int(input("What is the person's age in years? : "))
    ctzn = int(input("How many years have they been a citizen of the US? : "))

    if age >= 30 and ctzn >= 9:
        print("This person is eligible to serve in both the Senate and the House.")
    elif age >= 25 and ctzn >= 7:
        print("This person is eligible to serve in the House of Representatives.")
    else:
        print("This person is ineligible to serve in the Senate or House.")

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch7Ex08")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
