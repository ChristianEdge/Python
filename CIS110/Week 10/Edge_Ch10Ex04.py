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

    win = GraphWin("Three Button Monte", 350, 350 )
    win.setCoords(0.5, 0, 3.5, 3)
    
    b1 = Button(win, Point(1, 2), 0.75, 0.5, "Door 1")
    b1.activate()
    b2 = Button(win, Point(2, 2), 0.75, 0.5, "Door 2")
    b2.activate()
    b3 = Button(win, Point(3, 2), 0.75, 0.5, "Door 3")
    b3.activate()

    again = Button(win, Point(1.25, 0.5), 1, 0.5, "Play again")
    quitBtn = Button(win, Point(2.75, 0.5), 1, 0.5, "Quit")
    scoreBox = Text(Point(2, 1.5), "")
    scoreBox.draw(win)

    mess = Text(Point(2, 1), "Pick a door...")
    mess.setStyle('bold')
    mess.draw(win)

    playAgain = True
    hits = 0
    misses = 0

    while playAgain:
        mess.setText("Guess a door")
        pick = getDoorPick(win, b1, b2, b3)
        hits, misses = updateScore(pick, mess, scoreBox, hits, misses)
        playAgain = quitOrPlay(win, quitBtn, again)

    win.getMouse()
    win.close()
    #outro()
#End main()
#****************

def intro():
    print("\n\t***Welcome to Ch10Ex03***\n")
    print("\tThree Button Monte\n\n")

def getDoorPick(win, b1, b2, b3):
    choice = None
    while choice == None:
        pt = win.getMouse()
        for button in [b1, b2, b3]:
            if button.clicked(pt):
                choice = button
    choiceNum = int(choice.getLabel()[-1])
    return choiceNum

def updateScore(choice, msg, score, hits, misses):
    """Compares choice to a random number. Displays win or loss msg. """
    
    secret = randrange(1, 4)
    tally = "Wins : {0:2} \tLosses : {1:2}"

    if choice == secret:
        msg.setText("You win!")
        hits += 1
    else:
        msg.setText("You lose. The secret door was {0}".format(secret))
        misses += 1
    score.setText(tally.format(hits, misses))
    return hits, misses

def quitOrPlay(win, quitBtn, again):
    quitBtn.activate()
    again.activate()
    pt = win.getMouse()
    while not(quitBtn.clicked(pt) or again.clicked(pt)):
        pt = win.getMouse()
    ans = again.clicked(pt)
    quitBtn.deactivate()
    again.deactivate()
    return ans

def outro():
    #Output to console the author, program, & date/time program was run
    print("\nAuthor: Christian Edge")
    print("CIS110 Ch10Ex03 ")
    print(time.asctime(time.localtime(time.time())))
    input("\nPress <Enter> to Quit")


#Run the program          
if __name__ == '__main__':
    main()
