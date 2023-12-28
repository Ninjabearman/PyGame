import pygame ; from pygame.locals import *
import random

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
isHead = (255,0,0)
scoreFont = pygame.font.SysFont(None,40)


#game variables
game_Over = False
cellSize = 10
direction = 1 # 1 = up, 2 = right, 3 = down, 4 = left
updateSnake = 0
snakePosition = [[int(screenWidth / 2),int(screenHeight / 2)]]
snakePosition.append([int(screenWidth / 2),int(screenHeight / 2) + cellSize])
snakePosition.append([int(screenWidth / 2),int(screenHeight / 2) + cellSize * 2])
snakePosition.append([int(screenWidth / 2),int(screenHeight / 2) + cellSize * 3])
food = [0,0]
newPiece = [0,0]
newFood = True
foodColor = (200,50,50)
score = 0


def drawScreen():
    screen.fill(bg)

def displayScore():
    scoreTxt = 'Score: ' + str(score)
    scoreImg = scoreFont.render(scoreTxt,True,(0,0,255))
    screen.blit(scoreImg,(0,0))

def isGameOver(gameOver):
    #check snake has eaten itself
    headCount = 0
    for segment in snakePosition:
        if snakePosition[0] == segment and headCount > 0:
            gameOver = True
        headCount += 1
    
    #out of bounds
    if snakePosition[0][0] < 0 or snakePosition[0][0] > screenWidth or snakePosition[0][1] < 0 or snakePosition[0][1] > screenHeight:
        gameOver = True
    
    return gameOver

#game loop
while isRunning:
    drawScreen()
    displayScore()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                  direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                  direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                  direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                  direction = 4

    #create food
    if newFood:
        newFood = False
        food[0] = cellSize * random.randint(0,(screenWidth // cellSize)-1)
        food[1] = cellSize * random.randint(0,(screenHeight // cellSize)-1)

    #draw food
    pygame.draw.rect(screen,foodColor,(food[0],food[1],cellSize,cellSize))

    #snake/food collision
    if snakePosition[0] == food:
        newFood = True
        
        #snake grows
        newPiece = list(snakePosition[-1])
        if direction == 1:
            newPiece[1] += cellSize
        if direction == 3:
            newPiece[1] -= cellSize
        if direction == 2:
            newPiece[0] -= cellSize
        if direction == 4:
            newPiece[0] += cellSize

        snakePosition.append(newPiece)
        score += 1

    if updateSnake > 99:
         updateSnake = 0
         snakePosition = snakePosition[-1:] + snakePosition[:-1]
        
        #heading up
         if direction == 1:
            snakePosition[0][0] = snakePosition[1][0]
            snakePosition[0][1] = snakePosition[1][1] - cellSize
            gameOver = isGameOver(game_Over)
        #heading down
         if direction == 3:
            snakePosition[0][0] = snakePosition[1][0]
            snakePosition[0][1] = snakePosition[1][1] + cellSize
            gameOver = isGameOver(game_Over)
        #heading right
         if direction == 2:
            snakePosition[0][1] = snakePosition[1][1]
            snakePosition[0][0] = snakePosition[1][0] + cellSize
            gameOver = isGameOver(game_Over)
        #heading left
         if direction == 4:
            snakePosition[0][1] = snakePosition[1][1]
            snakePosition[0][0] = snakePosition[1][0] - cellSize
            gameOver = isGameOver(game_Over)

    head = 1
    for x in snakePosition:
        if head == 0:
            pygame.draw.rect(screen,bodyOuter,(x[0],x[1],cellSize,cellSize),cellSize)
            pygame.draw.rect(screen,bodyInner,(x[0] + 1,x[1] + 1,cellSize - 2,cellSize -2 ))
        if head == 1:
            pygame.draw.rect(screen,bodyOuter,(x[0],x[1],cellSize,cellSize),cellSize)
            pygame.draw.rect(screen,isHead,(x[0] + 1,x[1] + 1,cellSize - 2,cellSize -2 ))
            head = 0

    pygame.display.update()
    updateSnake += 1
pygame.quit()