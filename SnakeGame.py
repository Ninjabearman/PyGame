import pygame ; from pygame.locals import *

#intialization
pygame.init()

screenWidth = 600
screenHeight = 600
isRunning = True

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Snake Game using Python")

while isRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    pygame.display.update()
pygame.quit()