'''
Program Name: American Flag
Program Description: Draw an American flag using graphics.py
Author: Christian Edge
Date created: 15 June 2019
Last modified: 17 June 2019
Notes of interest: Uses "time" module and graphics.py
'''

import time
from graphics import *

def main():

    #Declare variables
    flagWidth = 1.9
    flagHeight = 1
    stripeHeight = 0.0769
    blueWidth = 0.76
    blueHeight = 0.5385
    starWidth = 0.0633
    starHeight = 0.0538
    
    scalingFactor = 450

    #Declare window object
    window = GraphWin("American Flag", flagWidth * scalingFactor,
                      flagHeight * scalingFactor)
    window.setCoords(0,0,1.9,1)
    window.setBackground("white")
    
    #Declare red stripes, draw
    redStripe1 = Rectangle(Point(0,0), Point(flagWidth, stripeHeight))
    redStripe1.setFill("red")
    redStripe1.setOutline("")
    redStripe1.draw(window)
    for i in range(6):
        nextStripe = redStripe1.clone()
        nextStripe.move(0, stripeHeight * (2 * (i + 1)))
        nextStripe.draw(window)


    #Draw the blue rectangle
    blueRectangle = Rectangle(Point(0, flagHeight),
                              Point(blueWidth, blueHeight - stripeHeight))
    blueRectangle.setFill("blue")
    blueRectangle.setOutline("")
    blueRectangle.draw(window)


    #Declare a star
    star = Polygon(Point(starWidth, (flagHeight - starHeight) + 0.018),#top point
                       Point(starWidth + 0.007, (flagHeight - starHeight) + 0.001),#top inside Right
                       Point(starWidth + 0.023, (flagHeight - starHeight) + 0.001),#right upper
                       Point(starWidth + 0.01, (flagHeight - starHeight) - 0.01),#inside right lower
                       Point(starWidth + 0.02, (flagHeight - starHeight) - 0.029),#bottm right
                       Point(starWidth, (flagHeight - starHeight) - 0.017),#bottom middle
                       Point(starWidth - 0.02, (flagHeight - starHeight) - 0.029),#bottom left
                       Point(starWidth - 0.01, (flagHeight - starHeight) - 0.01),#inside left lower
                       Point(starWidth - 0.023, (flagHeight - starHeight) + 0.001),#left upper
                       Point(starWidth - 0.007, (flagHeight - starHeight) + 0.001))#top inside left, final point
    star.setFill("white")
    star.setOutline("")

    #Draw the stars. The first star is the top left. These loops clone that
    #star and move them in the X and Y coords as indicated
    #These nested loops handle the 5 rows of 6 stars
    for i in range(6):
        X_Star = star.clone()
        X_Star.move(i * starWidth * 2, 0)
        X_Star.draw(window)
        for j in range(4):
            Y_Star = X_Star.clone()
            Y_Star.move(0, -((j + 1) * starHeight * 2))
            Y_Star.draw(window)

    #The below nested loop will handle the 4 rows of 5 stars
    star2 = star.clone()
    star2.move(starWidth, -starHeight)
    star2.draw(window)
    
    for k in range(5):
        X_Star = star2.clone()
        X_Star.move(k * starWidth * 2, 0)
        X_Star.draw(window)
        for l in range(3):
            Y_Star = X_Star.clone()
            Y_Star.move(0, -((l + 1) * starHeight * 2))
            Y_Star.draw(window)
    

    window.getMouse()
    window.close()


    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")



#Run the program          
main()
