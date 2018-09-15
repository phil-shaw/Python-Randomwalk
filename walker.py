import pygame
import random

from constants import *

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
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
        self.stepsize = stepsize
        self.levy = levy
        self.trail = trail

        self.oldxpos = self.xpos
        self.oldypos = self.ypos



    def saveoldpos(self):
        self.oldxpos = self.xpos
        self.oldypos = self.ypos

    def draw(self, screen):
        self.screen = screen

# Leave a Trail
        if self.trail == True:
            pygame.draw.line(self.screen, self.colour, (self.xpos, self.ypos), (self.oldxpos, self.oldypos))
        else:
            pygame.draw.line(self.screen, self.colour, (self.xpos, self.ypos), (self.xpos, self.ypos))

    def update(self):

        self.saveoldpos()

        xr = random.randint(-1, 1) * self.stepsize
        yr = random.randint(-1, 1) * self.stepsize

        self.xpos += xr
        self.ypos += yr


# Use Levy Flight
        if self.levy == True:
            self.__levyflight()


# Screen Wrap
        if self.xpos >= X_SIZE:
            self.xpos = 0
            self.oldxpos = 0
        if self.xpos <= 0:
            self.xpos = X_SIZE
            self.oldxpos = X_SIZE

        if self.ypos >= Y_SIZE:
            self.ypos = 0
            self.oldypos = 0
        if self.ypos <= 0:
            self.ypos = Y_SIZE
            self.oldypos = Y_SIZE


    def __levyflight(self):

        lv = random.randint(1, 100)

        if lv <= 2:
            self.xpos += random.randint(-50, 50)
            self.ypos += random.randint(-50, 50)