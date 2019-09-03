'''
Program Name: Ch8Ex07
Program Description: 
Author: Christian Edge
Date created: 
Last modified: 
Notes of interest: Uses "time" module
'''

import time
import math

def main():
    
    print("Goldbach Conjecture")

    number = int(input("Please input an even number : "))

    if number % 2:
        print(number, "is not even.")
    else:
        prime1 = goldbach(number)
        prime2 = number - prime1
        print("{0} + {1} = {2}".format(prime1, prime2, number))

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch8Ex07 ")
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

def goldbach(x):
    cand = 3
    while cand < x / 2:
        other = x - cand
        if isPrime(cand) and isPrime(other):
            return cand
        cand += 2

#Run the program          
main()
