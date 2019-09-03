'''
Program Name: Line Segments Ch4Ex08
Program Description: 
Author: Christian Edge
Date created: 14 June 2019
Last modified: 
Notes of interest: Uses "graphics.py" library
'''

from graphics import *
import math

def main():
    window = GraphWin("Line Segment Info", 400, 400)
    window.setCoords(-10, -10, 10, 10)
    
    message = Text(Point(0, -9.5), "Click on two endpoints to" +
                   " form a line segment.")
    message.draw(window)

    p1 = window.getMouse()
    p1.draw(window)
    p2 = window.getMouse()
    p2.draw(window)

    line = Line(p1,p2)
    line.draw(window)

    lineCenter = Circle(line.getCenter(), 0.15)
    lineCenter.setFill("cyan")
    lineCenter.draw(window)
    
    dx = p2.getX() - p1.getX()
    dy = p2.getY() - p1.getY()
    
    slope =  float(dy)/dx
    length = math.sqrt(dx * dx + dy * dy)
    
    message.setText("Length: " + str(round(length, 2)) +
                    "\tSlope : " +str(round(slope, 2))) 

    
    Text(Point(0,-7), "Click to quit").draw(window)
    window.getMouse()
    window.close()

    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110  Ch4Ex08 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")
    
#Run the program          
main()
