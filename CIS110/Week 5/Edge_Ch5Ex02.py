'''
Program Name: Ch5Ex02
Program Description: program accepts a quiz score and returns a grade
Author: Christian Edge
Date created: 24 June 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    print("This program accepts a quiz score and returns a grade.\n")

    score = int(input("Enter a quiz score (0 - 5) : "))

    grade = "FFDCBA"[score]

    print("The grade is :", grade)

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ch5Ex02")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
