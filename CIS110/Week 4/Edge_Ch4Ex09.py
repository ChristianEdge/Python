'''
Program Name: Draw Rectangle Ch4Ex09
Program Description: 
Author: Christian Edge
Date created: 14 June 2019
Last modified: 
Notes of interest: Uses "graphics.py" library
'''

from graphics import *
import math

def main():
    window = GraphWin("Rectangle Info", 500, 500)
    window.setCoords(0, 0, 10, 10)
    message = Text(Point(5, 1), "Click on opposite corners of a rectangle.").draw(window)

    p1 = window.getMouse()
    p1.draw(window)
    p2 = window.getMouse()

    rectangle = Rectangle(p1, p2)
    rectangle.setWidth(2)
    rectangle.draw(window)
    
    length = abs(p2.getX() - p1.getX())
    height = abs(p2.getY() - p1.getY())
    area = length * height
    perimeter = 2 * (length + height)

    message.setText("The perimeter is " + str(round(perimeter, 1)) +
                    "\nThe area is " + str(round(area, 1)))
    #Text(Point(5, 0.5), "The area is " + str(area)).draw(window)

    
    Text(Point(5, 2.25), "Click to quit").draw(window)
    window.getMouse()
    window.close()

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch4Ex09 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")
    
    
#Run the program          
main()
