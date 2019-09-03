'''
Program Name: Ch8Ex06
Program Description: 
Author: Christian Edge
Date created: 22 July 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time
import math

def main():
    print("Test for Prime Numbers\n")

    number = int(input("Enter an upper limit of primes : "))


    print("\nPrimes : 1 2", end = ' ')
    for i in range(2, number + 1):
        if isPrime(i):
            print(i, end = ' ')
    print("\nEnd")

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch8Ex06 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")
    

def isPrime(number):
    if number % 2 == 0:
        return False
    factor = 3
    while factor <= math.sqrt(number):
        if number % factor == 0:
            return False
        factor += 2
    return True

#Run the program          
main()
