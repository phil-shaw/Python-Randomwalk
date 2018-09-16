import pygame
import random

from constants import *
from vector import vector

# Random Walker xpos, ypos, colour, stepsize, levy, trail
#
# xpos, ypos -   X and Y position of the walker startpoint
# colour     -   Colour of the walker and its trail
# stepsize   -   Number of pixels each step takes
# levy       -   Use Levy Flight True or False
# trail      -   Leave a trail True or False
#

class walker():

    def __init__(self, xpos, ypos, colour, stepsize, levy, trail):
        self.walkerVector = vector(xpos, ypos)
        self.walkerOldVector = vector(xpos, ypos)
        self.colour = colour
        self.stepsize = stepsize
        self.levy = levy
        self.trail = trail


    def saveoldpos(self):
        self.walkerOldVector.setVector(self.walkerVector.getVectorX(), self.walkerVector.getVectorY())

    def draw(self, screen):
        self.screen = screen

# Leave a Trail
        xpos = self.walkerVector.getVectorX()
        ypos = self.walkerVector.getVectorY()
        xoldpos = self.walkerOldVector.getVectorX()
        yoldpos = self.walkerOldVector.getVectorY()

        if self.trail == True:
            pygame.draw.line(self.screen, self.colour,
                             (xpos, ypos), (xoldpos, yoldpos))
        else:
            pygame.draw.line(self.screen, self.colour,
                             (xpos, ypos), (xpos, ypos))

    def update(self):
        self.saveoldpos()

        xr = random.randint(-1, 1) * self.stepsize
        yr = random.randint(-1, 1) * self.stepsize

        self.walkerVector.addVector(xr, yr)


# Use Levy Flight
        if self.levy == True:
            self.__levyflight()


# Screen Wrap
        if self.walkerVector.getVectorX() >= X_SIZE:
            self.walkerVector.setVectorX(0)
        if self.walkerVector.getVectorX() <= 0:
            self.walkerVector.setVectorX(X_SIZE)

        if self.walkerVector.getVectorY() >= Y_SIZE:
            self.walkerVector.setVectorY(0)
        if self.walkerVector.getVectorY() <= 0:
            self.walkerVector.setVectorY(Y_SIZE)



    def __levyflight(self):

        lv = random.randint(1, 100)

        if lv <= 1:
            xr = random.randint(-50, 50)
            yr = random.randint(-50, 50)
            self.walkerVector.addVector(xr, yr)