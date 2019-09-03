'''
Program Name: Ch7Ex06
Program Description: 
Author: Christian Edge
Date created: 15 Jul 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():
    print("\n\tWelcome to the Podunksville Speeding Fine Caclculator\n")

    limit = int(input("What is the speed limit on that road? : "))

    speed = int(input("How fast was the person driving? : "))

    fine = 50 + ((speed - limit) * 5)

    if speed > 90:
        fine += 200

    if speed <= limit:
        print("The speed is within the legal limit.")
    else:
        print("The fine is ${:.2f}.".format(fine))

    
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch7Ex06")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
