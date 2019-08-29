'''
Program Name: Mars to Earth radio timer
Program Description: Calculates amount of time to send data from the Mars Curiosity
    rover to NASA
Author: Christian Edge
Date created: 3 June 2019
Last modified: 4 June 2019
Notes of interest: Uses "time" and "math" module
'''

import time
import math

def main():
    #Output introduction to user
    print("\n\tWelcome to the Mars-to-Earth radio timer.")
    print("I calculate the amount of time to send data from the Mars Curiosity rover to NASA.\n")

    print("\tMars' closest orbit to Earth is a distance of about 34 million miles." +
          "\nThe farthest apart they can be is about 249 million miles. \nThe " +
          "average distance is about 139 million miles.\n", end="\n")
    
    #Store values
    closestToEarth = 34 * pow(10,6)
    furthestFromEarth = 249 * pow(10,6)
    average = 139 * pow(10,6)

    SpeedOfLight = 186 * pow(10,3)

    #Time = Distance / Speed
    closestTime = closestToEarth / SpeedOfLight
    furthestTime = furthestFromEarth / SpeedOfLight
    averageTime = average / SpeedOfLight
        
    #Output the result to user
    print(" - Amount of time to send data - ")
    print("Closest to Earth:", round(closestTime, 1), "seconds")
    print("Furthest from Earth:", round(furthestTime, 1), "seconds")
    print("Average time:", round(averageTime, 1), "seconds")
    
    #Output to console the author, program, & date/time program was run
    print("\n\nAuthor: Christian Edge")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
