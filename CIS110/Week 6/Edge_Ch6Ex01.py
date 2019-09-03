'''
Program Name: CH6Ex01
Program Description: 
Author: Christian Edge
Date created: 
Last modified: 
Notes of interest: Uses "time" module
'''

import time

def main():

    print(oldMacDonald("cow", "moo"))
    print(oldMacDonald("pig", "oink"))
    print(oldMacDonald("chicken", "cluck"))

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Program Ch6Ex01")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

def oldMacDonald(animal, sound):
    return ("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n" +
    "And on the farm he had a " + animal + ", Ee-igh, Ee-igh, Oh!\n" +
    "With a " + sound + ", " + sound + " here and a " + sound + ", " +
    sound + " there.\n" +
    "Here a " + sound + ", there a " + sound + ", everywhere a " +
            sound + ", " + sound + ".\n" +
    "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!\n")

#Run the program          
main()
