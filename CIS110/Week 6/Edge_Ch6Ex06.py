'''
Program Name: Ch6Ex06
Program Description: 
Author: Christian Edge
Date created: 28 June 2019
Last modified: 
Notes of interest: Uses "time" module, Graphics.py, math
'''

import time
import math
from graphics import *

def main():

    window = GraphWin("Draw A Triagle", 500, 500)
    window.setCoords(0.0, 0.0, 10.0, 10.0)

    msg = Text(Point(5,0.5), "Click on 3 points")
    msg.draw(window)

    point1 = window.getMouse()
    point1.draw(window)
    point2 = window.getMouse()
    point2.draw(window)
    point3 = window.getMouse()
    point3.draw(window)

    tri = Polygon(point1, point2, point3)
    tri.setFill("peachpuff")
    tri.setOutline("cyan")
    tri.draw(window)

    d1 = distance(point1, point2)
    d2 = distance(point2, point3)
    d3 = distance(point3, point1)

    msg.setText("Perimeter: %0.2f \tArea: %0.2f" % ((d1 + d2 + d3),
                                                  triArea(d1, d2, d3)))
    

    window.getMouse()
    window.close()

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Program Ch6Ex06 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")

def square(x):
    return x ** 2

def distance(p1, p2):
    return (math.sqrt(square(p2.getX() - p1.getX()) +
            square(p2.getY() - p1.getY())))

def triArea(a, b, c):
    s = (a + b + c) / 2.0
    return math.sqrt(s * (s-a) * (s-b) * (s-c))


#Run the program          
main()
