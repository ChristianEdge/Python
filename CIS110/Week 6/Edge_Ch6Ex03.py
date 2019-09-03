'''
Program Name: Ch6Ex03
Program Description: Calculates the volume and surface area of a
    sphere based on user input
Author: Christian Edge
Date created: 28 June 2019
Last modified: 
Notes of interest: Uses "time" and "math" module
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
    volume = sphereVolume(radius)
    area = sphereArea(radius)

    #Output data to user
    print("\nThe volume of your sphere is:", round(volume, 2), "cubed units.")
    print("The surface area of your sphere is:", round(area, 2), "square units.")

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Calculate Volume Ch6Ex03 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

def sphereArea(radius):
    return 4.0 * math.pi * radius ** 2

def sphereVolume(radius):
    return 4.0 / 3.0 * math.pi * radius ** 3

#Run the program          
main()
