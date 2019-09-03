'''
Program Name: Ch6Ex07
Program Description: finds the value in the Fibonacci sequence
    based on its index number
Author: Christian Edge
Date created: 28 June 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():
    print("\n\tNth Fibonacci Number Program\n")

    number = int(input("Enter n: "))

    print("The Fibonacci value is ", fibo(number))

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Program Ch6Ex07 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")


def fibo(n):
    curr, prev = 1, 1
    for i in range(n - 2):
        curr, prev = curr + prev, curr
    return curr

#Run the program          
main()
