'''
Program Name: Coffee Price Calculator Ch3Ex05
Program Description: Determine the cost of an order from Konditorei
    Coffee Shop
Author: Christian Edge
Date created: 6 June 2019
Last modified: 7 June 2019
Notes of interest: Uses "time" module
'''

import time

def main():
    #Introduction
    print("Welcome to the Coffee Price Calculator. \nI determine the " +
          "cost of an order from Konditorei Coffee Shop including " +
          "shipping.\n")

    #Get and store user input
    lbsCoffee = float(input("How many pounds of coffee would you like to " +
                            "order? : "))

    #Perform calculations
    coffeeCost = 10.5  * lbsCoffee
    shipping = (0.86 * lbsCoffee) + 1.5
    total = coffeeCost + shipping

    #Output data to user
    print("\nCost of coffee :", coffeeCost)
    print("Cost of shipping :", shipping)
    print("-----------------------------")
    print("Total Due : $", total)

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Coffee Price Calculator Ch3Ex05")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
