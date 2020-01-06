"""For use with the NumbersGame project"""

import pygame
from Color import *

class Player(pygame.sprite.Sprite):
    """Game Player sprite.
    Every pygame sprite object must have a self.image and a self.rect.
    self.rect refers to the rectangle that encpasulates the sprite in
    terms of coordinates (but also top, bottom, left, right, topleft, etc).
    self.image is what the sprite is currently displaying on the screen."""
    def __init__(self, game, x, y, TILE_SZ):
        self.groups = game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups) #Necessary for each sprite
        self.image = pygame.Surface((TILE_SZ - 2, TILE_SZ - 2)) #Surface in place of img
        self.image.fill(Color.SAND)
        self.rect = self.image.get_rect()
        self.rect.x = x + 2
        self.rect.y = y + 2
        self.xVel = 5 #velocity on x axis
        self.yVel = 5 #velocity on y axis

    def update(self):
        pass

    def moveRight(self):
        """Moves the sprite to the right. If it goes off-screen to the
        right, it respawns on the left."""
        if self.rect.left < 640:
            self.rect.x += 1 * self.xVel
        else:
            self.rect.right = 0

    def moveL(self):
        """Moves the sprite to the left."""
        
