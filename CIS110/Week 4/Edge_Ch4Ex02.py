'''
Program Name: Archery Target Ch4Ex02
Program Description: 
Author: Christian Edge
Date created: 12 June 2019
Last modified: 
Notes of interest: Uses "graphics.py" library
'''

from graphics import *

def main():
    window = GraphWin("Archery Target", 400,400)
    window.setCoords(-6,-6,6,6)
    window.setBackground("gray")

    center = Point(0,0)

    c1 = Circle(center, 5)
    c1.setFill("white")
    c1.draw(window)
    
    c2 = Circle(center, 4)
    c2.setFill("black")
    c2.draw(window)
    
    c3 = Circle(center, 3)
    c3.setFill("blue")
    c3.draw(window)

    c4 = Circle(center, 2)
    c4.setFill("red")
    c4.draw(window)

    c5 = Circle(center, 1)
    c5.setFill("yellow")
    c5.draw(window)

    Text(Point(0,-5.5), "Click to quit").draw(window)
    window.getMouse()
    window.close()

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Program Ch4Ex02")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

    
#Run the program          
main()
