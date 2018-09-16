import pygame, sys, random

from constants import *
from walker import walker

pygame.init()
windowSize = (X_SIZE, Y_SIZE)
screen = pygame.display.set_mode(windowSize)
screen.fill(BLACK)


clock = pygame.time.Clock()
r = random.randint(0,4)

w = walker(X_SIZE / 2, Y_SIZE / 2, BLUE, 1, True, True)
w2 = walker(X_SIZE / 2, Y_SIZE / 2, GREEN, 1, False, False)
w3 = walker(X_SIZE / 2, Y_SIZE / 2, RED, 1, False, False)

while 1:

    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    w.draw(screen)
    w2.draw(screen)
    w3.draw(screen)
    w.update()
    w2.update()
    w3.update()
    pygame.display.update()