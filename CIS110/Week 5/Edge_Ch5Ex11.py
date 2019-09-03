'''
Program Name: Ch5Ex11
Program Description: program illustrates a chaotic function
Author: Christian Edge
Date created: 24 June 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    print("This program illustrates a chaotic function.\n")

    x1 = float(input("Enter the first seed between 0 and 1 : "))
    x2 = float(input("Enter the second seed between 0 and 1 : "))
    print()

    print("index   ", x1, "    ", x2)
    print("---------------------------")

    for i in range(1, 11):
        x1 = 3.9 * x1 * (1 - x1)
        x2 = 3.9 * x2 * (1 - x2)
        print("{0:2}{1:15.6f}{2:10.6f}".format(i, x1, x2))

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ch5Ex11")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
