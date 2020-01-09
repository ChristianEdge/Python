'''
Program Name: Tic Tac Toe
Program Description: 
Author: Christian Edge
Date created: 01 Jan 2020
Last modified: Today
Notes of interest: Uses pygame, time, random modules
'''

import pygame
import random
import copy
import sys  #sys.exit() needed else pygame throws error
import ctypes   #pygame strectches on high DPI screens, see init()
from GameData import * #holds Window size, FPS, etc.
from Color import * #holds colors as uppercase words

class TicTacToe():
    """This class defines the game Tic Tac Toe. To run the game,
        instantiate the object and call its run() method."""

    def __init__(self):
        pygame.init() #Must initilize pygame once
        ctypes.windll.user32.SetProcessDPIAware() #Adjust for high DPI screens

        #Create window
        self.window = pygame.display.set_mode((GameData.WIN_WD, #Window width
                                               GameData.WIN_HT))#Window height
        pygame.display.set_caption(GameData.TITLE)
        self.clock = pygame.time.Clock()
        self.BG_COLOR = Color.BLACK
        pygame.key.set_repeat(0)  #Disables key repeat
        self.font = pygame.font.match_font(GameData.FONT_PLYR)
        #Game variables
        self.fieldX = GameData.BORDER
        self.fieldY = GameData.BORDER
        self.tile = GameData.TILE
        self.playerX = 'X'
        self.playerO = 'O'
        self.nullField = '-' #Empty spaces
        self.playerXscore = 0
        self.playerOscore = 0

    def new(self):
        """This method generates the conditions for a new game.
        It draws a new game board, sets variables"""
        self.window.fill(Color.BLACK)
        self.draw()
        self.gameBoard(self.tile, self.fieldX, self.fieldY, #Draws game
                       Color.WHITE, Color.GAINSBORO)
        #Update scores
        self.drawText(GameData.TILE + GameData.BORDER, #x
                      GameData.TILE * 3 + GameData.BORDER, #y
                      "Player Score: " + str(self.playerXscore),
                      GameData.TILE // 8, Color.GRAY)
        self.drawText(GameData.TILE * 2 + GameData.BORDER, #x
                      GameData.TILE * 3 + GameData.BORDER, #y
                      "Computer Score: " + str(self.playerOscore),
                      GameData.TILE // 8, Color.GRAY)
        self.playerTurn = True #Controls turn swapping, human player == True
        self.winner = False #Check for winner after each move
        self.gameField = [[self.nullField for x in range(3)] for x in range(3)]
        #3 lists of 3 items, representing the 9 spaces

    def intro(self):
        """This function defines the start menu screen."""
        runIntro = True

        while runIntro:
            #Wait for initial user event
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:   #Mouse main button click
                        runIntro = False
            #Quit events
                if event.type == pygame.QUIT: #Window 'X' button
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    
            #Fill the window
            self.window.fill(Color.BLACK)
            #Draw the text
            self.drawText(GameData.WIN_WD // 2,
                          GameData.WIN_HT // 2,
                          GameData.TITLE,
                          42, Color.BLUEWTR)#x, y, text, size, color
            #Update display
            self.draw()

    def endGame(self):
        """This function defines what happens at the end of each game."""
        #Draw buttons
        print("Endgame")
        size = GameData.TILE // 2
        #Button coordinates
        playBtnX = GameData.TILE + GameData.BORDER - size * 0.8
        playBtnY = GameData.TILE * 1.5 + GameData.BORDER - size * 0.2
        quitBtnX = GameData.TILE * 2 + GameData.BORDER - size * 0.8
        quitBtnY = GameData.TILE * 1.5 + GameData.BORDER - size * 0.2
        #Text coordinates
        playTxtX = GameData.TILE + GameData.BORDER - size * 0.8 + size / 2
        playTxtY = GameData.TILE * 1.5 + GameData.BORDER - size * 0.2 + size / 2
        quitTxtX = GameData.TILE * 2 + GameData.BORDER - size * 0.8 + size / 2
        quitTxtY = GameData.TILE * 1.5 + GameData.BORDER - size * 0.2 + size / 2
        endGame = True
        
        while endGame:
            mousePos = pygame.mouse.get_pos()
            #Mouse hover color change for buttons
            if (playBtnX < mousePos[0] < playBtnX + size and 
                playBtnY < mousePos[1]< playBtnY + size):
                self.drawButton(playBtnX, playBtnY, size, Color.LIGHTGREEN)
            else: self.drawButton(playBtnX, playBtnY, size, Color.GREEN)
            if (quitBtnX < mousePos[0] < quitBtnX + size and 
                quitBtnY < mousePos[1] < quitBtnY + size):
                self.drawButton(quitBtnX, quitBtnY, size, Color.LIGHTRED)
            else: self.drawButton(quitBtnX, quitBtnY, size, Color.RED)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouseX, mouseY = event.pos #Mouse main button click
                        if (playBtnX < mouseX < playBtnX + size and
                            playBtnY < mouseY < playBtnY + size):
                            #click inside confines of button
                            self.new()
                            endGame = False
                        if (quitBtnX < mouseX < quitBtnX + size and
                            quitBtnY < mouseY < quitBtnY + size):
                            self.quit()
            self.drawText(playTxtX, playTxtY, "Replay?", 32, Color.BLACK)
            self.drawText(quitTxtX, quitTxtY, "Quit", 32, Color.BLACK)
            self.draw()

    def events(self):
        """This method handles player inputs -> event.get() returns a list of events
        like user inputs every frame."""
        for event in pygame.event.get():
            #Mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   #Mouse main button click
                    mouseX, mouseY = self.convertMove(event.pos,
                                                    GameData.TILE, GameData.BORDER)
                    #Check validity of move against gameField[]
                    if (self.isValidMove(mouseX, mouseY, self.gameField) and
                    not self.winner and self.playerTurn):
                        #window, x, y, tile, color
                        self.drawX(self.window,
                                   GameData.BORDER + GameData.TILE * mouseX,
                                   GameData.BORDER + GameData.TILE * mouseY,
                                   GameData.TILE, Color.BLUE)
                        self.gameField[mouseY][mouseX] = 'X'
                        self.playerTurn = False
            #Quit events
            if event.type == pygame.QUIT: #Window 'X' button
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def update(self):
        """Updates the game every loop"""
        
        #Check for a winner
        if self.isWin(self.gameField, self.playerX):
            self.winner = True
            self.playerXscore += 1
            self.endGame()
            print("Winner : Player ")
            #Pause loop

        #Compter AI move
        self.ai(self.gameField)
        
        #Check for a winner
        if self.isWin(self.gameField, self.playerO):
            self.winner = True
            self.playerOscore += 1
            self.endGame()
            print("Winner : Player ", self.playerO)
            
        #Check for stalemate
        if self.isStalemate(self.gameField) and not self.winner:
            self.endGame()
            print("Stalemate")
        
    def draw(self):
        """Draws game every loop"""
        pygame.display.update() #Must go after each object's draw(). Better than flip()

          
    def run(self):
        """The run command runs a new set of games."""
        self.intro()

        self.new() #Draw new game board, reset variables

        #Game loop ******************************************
        self.running = True
        while self.running:
            self.events() #Check for player input
        
            self.update() #Process computer turn
                            
            self.draw() #Output to screen

            self.clock.tick(GameData.FPS)
            
        #End of game while loop *****************************

    def gameBoard(self, tile, x, y, bgColor, lnColor):
        """Define the game board background square and grid lines.
        There are borders to consider. One pixel in length is added
        to the background square to make sure it covers the grid
        lines (they were poking out)."""
        pygame.draw.rect(self.window, bgColor, (x, # starting x
                                                y, #starting y
                                                tile * 3 + 1,  #width
                                                tile * 3 + 1)) #height
        
        self.drawGrid(self.window, tile, self.fieldX, self.fieldY, lnColor)
      
    def drawGrid(self, window, tile, x, y, lnColor):
        """Creates the line grid."""
        for multip in range(1,3): #multiplier       
            pygame.draw.line(window,                #vertical lines
                             lnColor, 
                             (x,  tile * multip + y), #Start x, y
                             (tile * 3 + x, tile * multip + y),#End x, y
                             tile // 16)#Width
            
            pygame.draw.line(window,                #horizontal lines
                             lnColor,
                             (tile * multip + x, y), 
                             (tile * multip + x, tile * 3 + y),
                             tile // 16)
            

    def drawText(self, x, y, text, size, color):
        """This function draws text to the screen. Pass x and y coordinates,
        the text to display, and its size and color."""
        font = pygame.font.Font(self.font, size)
        textSurface = font.render(text, True, color)
        textRect = textSurface.get_rect()
        textRect.midtop = (x, y)
        self.window.blit(textSurface, textRect)
    
    def drawX(self, window, x, y, tile, color):
        """Draw an X. the x, y is the top left of the square where it will be drawn."""
        width = tile // 8 #Width of line
        space = tile // 8 #Space inside tile
        pygame.draw.line(window, color,
                         (x + space, y + space), (x + tile - space, y + tile - space),
                         width)
        pygame.draw.line(window, color,
                         (x + space, y + tile - space), (x + tile - space, y + space),
                         width)
        
    def drawO(self, window, x, y, tile, border, color):
        """Draws an O with a circle. The X an Y are the top left coordinates
        of the space to draw the circle."""
        #Tried pygame arc(), circle() is better
        center = tile // 2
        width = tile // 12
        space = tile // 8
        radius = tile // 2 - border
        pygame.draw.circle(window, color,
                           (x + center, y + center),
                           radius,
                           width)

    def drawButton(self, x, y, size, color):
        """Defines a button. Still need to define a button size."""
        pygame.draw.rect(self.window, color, (x, y, size * 1.5, size))

    def convertMove(self, tup, tile, border):
        """This method determines where a user clicked on a gameboard by returning
        a pair of numbers, 0-2, 0-2. These are array indices to be used in
        conjunction with the gameField list."""
        xPos = tup[0] // (tile + border)
        yPos = tup[1] // (tile + border)
        return xPos, yPos

    def isValidMove(self, x, y, arr):
        """Determines if a move is valid on the game board.
        It only needs to be an empty space to be valid"""
        if arr[y][x] == self.nullField:
            return True
        else: return False
                   
    def isWin(self, arr, playerXorO):
        winningString = playerXorO * 3 #Use player XorO to set value to check list against
        winner = False
        for i in range(3): 
            if "".join(arr[i]) == winningString: #If any list in the array contains all Xs or Os
                winner = True
                
            arr2 = [item[i] for item in arr] #If any of the columnar elements in eah sublist match
            if "".join(arr2) == winningString:
                winner = True
                
        #Check diagonals
        if str(arr[0][0]) + str(arr[1][1]) + str(arr[2][2]) == winningString:
            winner = True
        if str(arr[0][2]) + str(arr[1][1]) + str(arr[2][0]) == winningString:
            winner = True
            
        return winner

    def isStalemate(self, arr):
        #check if anything in array is empty
        moveLst = map(''.join, arr)
        if self.nullField not in ''.join(moveLst):
            return True
        else: return False
        
    def ai(self, arr):
        '''
        AI chooses move spaces in this order: 
        1. Check if next move wins game. If so, make that move.
        2. Check if player's next move wins game. If so, block it.
        3. Check the corners, choose a random available one.
        4. Check center, if clear make move.
        5. Check sides, choose a random available one
        '''
        if not self.playerTurn and not self.winner: #already in while loop so use 'if'
            #Check for winning positions, substitute 'O' and 'X' for each space
            for i in range(3):
                for j in range(3):
                    #Create deep copy of gameField we can modify
                    gameFieldCopy = copy.deepcopy(arr)
                    gameFieldCopy2 = copy.deepcopy(arr)
                    #Try replacing elements one at a time
                    if self.isValidMove(i, j, gameFieldCopy):
                        gameFieldCopy[j][i] = 'O'
                        gameFieldCopy2[j][i] = 'X'
                        if self.isWin(gameFieldCopy, self.playerO): #If this element produces a winning game
                            print("AI win")
                            #Assign the winning move
                            arr[j][i] = 'O'
                            #window, x, y, tile, border, color
                            self.drawO(self.window,
                                       GameData.BORDER + GameData.TILE * i,
                                       GameData.BORDER + GameData.TILE * j,
                                       GameData.TILE, GameData.BORDER, Color.RED)
                            self.playerTurn = True
                            return
                        elif self.isWin(gameFieldCopy2, self.playerX): #Prevent player win
                            print("AI blocks player win")
                            #Assign the winning move
                            arr[j][i] = 'O'
                            #window, x, y, tile, border, color
                            self.drawO(self.window,
                                       GameData.BORDER + GameData.TILE * i,
                                       GameData.BORDER + GameData.TILE * j,
                                       GameData.TILE, GameData.BORDER, Color.RED)
                            print(arr)
                            self.playerTurn = True
                            return
                            
            #Check four corners, choose random if multiple are available
            validCorner = []
            for m in [0, 2]:
                for n in [0, 2]:
                    if self.isValidMove(m, n, arr):
                        validCorner.append([m, n])
            if len(validCorner) > 0:
                x, y = validCorner[random.randrange(len(validCorner))]
                arr[y][x] = 'O'
                self.drawO(self.window, #window, x, y, tile, border, color
                            GameData.BORDER + GameData.TILE * x,
                            GameData.BORDER + GameData.TILE * y,
                            GameData.TILE, GameData.BORDER, Color.RED)
                self.playerTurn = True
                return
            #Else if there are no valid corners and the middle position
            #is free, move there
            elif self.isValidMove(1, 1, arr):
                arr[1][1] = 'O'
                self.drawO(self.window, #window, x, y, tile, border, color
                            GameData.BORDER + GameData.TILE * x,
                            GameData.BORDER + GameData.TILE * y,
                            GameData.TILE, GameData.BORDER, Color.RED)
                self.playerTurn = True
                return
            #Else choose a side space
            else:
                validSide = []
                if self.isValidMove(0, 1, arr):
                    validSide.append([0, 1])    #Top
                if self.isValidMove(1, 0, arr):
                    validSide.append([1, 0])    #Left
                if self.isValidMove(1, 2, arr):
                    validSide.append([1, 2])    #Right
                if self.isValidMove(2, 1, arr):
                    validSide.append([2, 1])    #Bottom
                if len(validSide) > 0:
                    x, y = validSide[random.randrange(len(validSide))]
                    arr[y][x] = 'O'
                    self.drawO(self.window, #window, x, y, tile, border, color
                               GameData.BORDER + GameData.TILE * x,
                               GameData.BORDER + GameData.TILE * y,
                               GameData.TILE, GameData.BORDER, Color.RED)
                    self.playerTurn = True
                    return
    #*******End define ai()*****************************
        
    def quit(self):
        pygame.display.quit()
        pygame.quit()
        sys.exit(0)
    
#Run the program          
game = TicTacToe()
game.run()
