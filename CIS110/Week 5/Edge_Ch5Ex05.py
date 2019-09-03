'''
Program Name: Ch5Ex05
Program Description: program gets value of letters in name
Author: Christian Edge
Date created: 24 June 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    print("This program returns the sum value of the letters in a name.\n")

    name = input("Enter a single name: ")

    sum = 0

    for letter in name.lower():
        sum += ord(letter) - (ord("a") - 1)
    
    print("\nThe value of the name", name, "is", sum)

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ch5Ex05")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
