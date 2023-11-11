import pygame ; from pygame.locals import *

#intialization
pygame.init()

#screen
pygame.display.set_caption("Snake Game using Python")
isRunning = True
screenWidth = 600
screenHeight = 600
screen = pygame.display.set_mode((screenWidth,screenHeight))

#colors
bg = (255,200,150)
bodyInner = (50,175,25)
bodyOuter = (100,100,200)

#game variables
cellSize = 10
snakePosition = [[int(screenWidth / 2),int(screenHeight / 2)]]
snakePosition.append([int(screenWidth / 2),int(screenHeight / 2) * cellSize])
snakePosition.append([int(screenWidth / 2),int(screenHeight / 2) * cellSize * 2])
snakePosition.append([int(screenWidth / 2),int(screenHeight / 2) * cellSize * 3])

def drawScreen():
    screen.fill(bg)

#game loop
while isRunning:
    drawScreen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False

    for x in snakePosition:
        pygame.draw.rect(screen,bodyOuter,(x[0],x[1],cellSize,cellSize))
        pygame.draw.rect(screen,bodyInner,(x[0] + 1,x[1] + 1,cellSize -2,cellSize - 2))

    pygame.display.update()
pygame.quit()