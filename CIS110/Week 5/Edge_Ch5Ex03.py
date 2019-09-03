'''
Program Name: Ch5Ex03
Program Description: program accepts an exam score and returns a grade
Author: Christian Edge
Date created: 24 June 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    print("This program accepts a quiz score and returns a grade.\n")

    score = int(input("Enter the exam score (0 - 100) : "))

    grades = ["F", "F", "F", "F", "F", "F", "D", "C", "B", "A", "A"]

    index = int(score) // 10

    final = grades[index]

    print("The grade is :", final)

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ch5Ex03")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
