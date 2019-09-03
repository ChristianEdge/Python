'''
Program Name: Ch6Ex12
Program Description: 
Author: Christian Edge
Date created: 28 June 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():
    '''
    The pseudocode in the video tells us to prompt the user for a list
    of numbers, but you ask us to test the function by assigning a list
    "nums" to a range of 15.
    Additionally, on the submission page the instructions tells us to test
    a range of 17.
    I opted to skip the user input and test the function with two different
    lists of appropriate ranges
    '''

    nums1 = list(range(15))
    nums2 = list(range(17))

    print("\n\tList one: ", nums1)
    print("\tSum of list one: ", sumList(nums1))
    print("\n\tList two: ", nums2)
    print("\tSum of list two: ", sumList(nums2))

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Program Ch6Ex12 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

def sumList(nums):
    total = 0
    for i in nums:
        total += i
    return total

#Run the program          
main()
