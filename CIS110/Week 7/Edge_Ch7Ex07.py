'''
Program Name: Ch7Ex07
Program Description: 
Author: Christian Edge
Date created: 15 July 2019
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    print("Babysitting calculator")
    
    startHrs, startMins = input("Enter start time : ").split(":")
    endHrs, endMins =input("Enter end time : ").split(":")
    

    start = int(startHrs) + float(startMins) / 60
    end = int(endHrs) + float(endMins) / 60

    if end < start:
        end += 24
        
    bedtime = 21.0

    if start < bedtime:
        if end < bedtime:
            primeHrs = end - start
            extraHrs = 0.0
        else:
            primeHrs = bedtime - start
            extraHrs = end - bedtime
    else:
        primeHrs = 0
        extraHrs = end - start

    pay = 2.5 * primeHrs + 1.75 * extraHrs

    print("Babysitters pay : ${0:0.2f}".format(pay))
        
    
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch7Ex07 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
