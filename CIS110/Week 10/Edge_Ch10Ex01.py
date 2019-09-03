'''
Program Name: Ch10Ex01
Program Description: 
Author: Christian Edge
Date created: 5 August 2019
Last modified: 
Notes of interest: Uses time module
'''
from math import sin, cos, radians

class Projectile:
    """The Projectile class handles simulation of real-world projectiles (like
    cannonballs) in 2 dimensions using trigonomic formula distance = rate * time.
    Constructor parameters: 'agl' = launch angle (in degrees). 'vel' = launch
    velocity (meters per second). 'h' = height at launch (meters). """
    def __init__(self, agl, vel, h):
        self.xPos = 0.0     #Starting position
        self.yPos = h       #Starting position
        theta = radians(agl)
        self.xVel = vel * cos(theta)    #Velocity of x
        self.yVel = vel * sin(theta)    #Velocity of y
        self.maxHeight = h

    def getX(self):
        return self.xPos

    def getY(self):
        return self.yPos

    def update(self, time):
        self.xPos += time * self.xVel
        yVelT = self.yVel - 9.8 * time      #Decrease of yvel to gravity
        self.yPos += time * (self.yVel + yVelT) / 2.0
        self.yVel = yVelT
        if self.yVel > 0:
            self.maxHeight = self.yPos

    def getMaxHeight(self):
        return self.maxHeight
        
    
def getInput():
    agl = float(input("Enter the launch angle : "))
    vel = float(input("Enter the launch velocity : "))
    h = float(input("Enter the launch height : "))
    time = float(input("Enter the time interval between calculations : "))
    return agl, vel, h, time        

def main():
    print("\n\t**Cannonball Simulation**\n\n")
    agl, vel, h, time = getInput()
    proj = Projectile(agl, vel, h)
    while proj.getY() >= 0:
        proj.update(time)
    print("\n\nDistance traveled : {0:0.1f} meters.".format(proj.getX()))
    print("Maimum height : {0:0.1f} meters.".format(proj.getMaxHeight()))

if __name__ == "__main__":
    main()
