'''
Program Name: Ch5Ex04
Program Description: program builds acronyms
Author: Christian Edge
Date created: 24 June 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    print("This program accepts a phrase and returns an acronym.\n")

    phrase = input("Enter a phrase: ")

    acronym = ""

    for word in phrase.split():
        acronym += word[0]

    acronym = acronym.upper()

    print(acronym, "is the acronym for '", phrase, "'")

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ch5Ex04")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
