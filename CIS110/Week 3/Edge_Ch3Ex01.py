'''
Program Name: Calculate Volume Ch3Ex01
Program Description: Calculates the volume and surface area of a
    sphere based on user input
Author: Christian Edge
Date created: 6 June 2019
Last modified: 7 June 2019
Notes of interest: Uses "time" and "math" modules
'''

import time
import math

def main():
    #Output instructions to user
    print("Welcome to the Sphere Volume Calculator. I calculate the " +
          "volume and surface area of a sphere based on a radius that " +
          "you input.\n")

    #Get and store user input
    radius = float(input("What is the radius of your sphere? :   "))

    #Perform calculations
    volume = 4.0 / 3.0 * math.pi * radius ** 3
    surfaceArea = 4.0 * math.pi * radius ** 2

    #Output data to user
    print("\nThe volume of your sphere is:", round(volume, 2), "cubed units.")
    print("The surface area of your sphere is:", round(surfaceArea, 2),
          "square units.")

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Calculate Volume Ch3Ex01 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

#Run the program          
main()
