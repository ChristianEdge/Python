'''
Program Name: Ch8Ex08
Program Description: 
Author: Christian Edge
Date created: 22 July 2019 
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():
    print("Euclid's GCD Algorithm\n")

    x, y = input("Enter 2 numbers (x, y) : ").split(",")

    print("The GCD of", x, "and", y, "is", gcd(int(x), int(y)))
    

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch8Ex08 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

def gcd(m, n):
    while m != 0:
        n, m = m, n % m
    return n

#Run the program          
main()
