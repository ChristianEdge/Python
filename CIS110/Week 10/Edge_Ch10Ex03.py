'''
Program Name: 
Program Description: 
Author: Christian Edge
Date created: 
Last modified: 
Notes of interest: Uses time module
'''

import time
from random import randrange
from graphics import *
from button import Button

def main():

    #intro()

    win = GraphWin("Three Button Monte", 350, 100)
    win.setCoords(0.5, 0, 3.5, 3)
    b1 = Button(win, Point(1, 2), 0.75, 1, "Door 1")
    b1.activate()
    b2 = Button(win, Point(2, 2), 0.75, 1, "Door 2")
    b2.activate()
    b3 = Button(win, Point(3, 2), 0.75, 1, "Door 3")
    b3.activate()

    mess = Text(Point(2, 0.75), "Pick a door...")
    mess.setStyle('bold')
    mess.draw(win)

    secret = randrange(1, 4)
    choice = None

    #Processing
    while choice == None:
        pt = win.getMouse()
        for button in [b1, b2, b3]:
            if button.clicked(pt):
                choice = button
    choiceNum = int(choice.getLabel()[-1])

    if choiceNum == secret:
        mess.setText("You win!")
    else:
        mess.setText("You lose. The secret door was {0}".format(secret))
    

    win.getMouse()
    win.close()
    #outro()
#End main()
#****************

def intro():
    print("\n\t***Welcome to Ch10Ex03***\n")
    print("\tThree Button Monte\n\n")

def outro():
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ch10Ex03 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")


#Run the program          
if __name__ == '__main__':
    main()
