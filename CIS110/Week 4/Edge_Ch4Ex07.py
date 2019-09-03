'''
Program Name: Circle Intersection Ch4Ex07
Program Description: 
Author: Christian Edge
Date created: 14 June 2019
Last modified: 
Notes of interest: Uses "graphics.py" library
'''

from graphics import *
import math

def main():
    print("This program computes the intersection of a circle")
    print("and a horizontal line.")
    print()
    
    radius = float(input("Enter the radius of the circle: "))
    y_intrsct = float(input ("Enter the y-intersect of the line: "))

    window = GraphWin("Circle Intersection") 
    window.setCoords(-10, -10, 10, 10)

    Circle(Point(0, 0), radius).draw(window)
    Line(Point(-10, y_intrsct), Point(10, y_intrsct).draw(window))
    x = math.sqrt(radius * radius - y_intrsct * y_intrsct)

    print ("The values of intersection are ", -x, x)
    
    p1 = Circle(Point(x, y_intrsct), 0.25)
    p1.setOutline("red")
    p1.setFill("red")
    p1.draw(window)
    
    p2 = p1.clone()
    p2.move(-2 *  x, 0)
    p2.draw(window)

    
    Text(Point(0,-7), "Click to quit").draw(window)
    window.getMouse()
    window.close()

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Program Ch4Ex07 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")
    
#Run the program          
main()
