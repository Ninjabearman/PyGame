import pygame
from pygame.locals import *

#initialization
pygame.init()

isRunning = True
screenWidth = 300
screenHeight = 300
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Tic-Tac-Toe Game Using python")

# public variables
line_width = 6
marks = []
clicked = False
position = []
player = 1
winner = 0
gameOver = False
green = (0,255,0)
red = (255,0,0)
font = pygame.font.SysFont(None,40)
againRect = Rect(screenWidth // 2 - 80, screenHeight // 2, 160, 50)

#functions
def drawGrid():
    bg = (255,255,200)
    grid = (50,50,50)
    screen.fill(bg)
    for x in range(1,3):
        pygame.draw.line(screen,grid,(0,x *100),(screenWidth,x * 100),line_width)
        pygame.draw.line(screen,grid,(x *100,0),(x * 100,screenHeight),line_width)

for x in range(3):
    row = [0] * 3
    marks.append(row)

def drawMarks():
    xPos = 0
    for x in marks:
        yPos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,green,(xPos * 100 + 15, yPos * 100 + 15),(xPos * 100 + 85, yPos * 100 + 85),line_width)
                pygame.draw.line(screen,green,(xPos * 100 + 15, yPos * 100 + 85),(xPos * 100 + 85, yPos * 100 + 15),line_width)
            if y == -1:
                pygame.draw.circle(screen,red,(xPos * 100 + 50, yPos * 100 + 50),38,line_width)
            yPos += 1
        xPos += 1

def checkWinner():
    global winner
    global gameOver
    yPos = 0
    for x in marks:
        #check columns
        if sum(x)== 3:
            winner = 1
            gameOver = True
        if sum(x)== -3:
            winner = 2
            gameOver = True
        #check rows
        if marks[0][yPos] + marks[1][yPos]+ marks[2][yPos] == 3:
            winner = 1
            gameOver = True
        if marks[0][yPos] + marks[1][yPos]+ marks[2][yPos] == -3:
            winner = 2
            gameOver = True
        yPos += 1
    #check cross
    if marks[0][0] + marks[1][1] + marks[2][2] == 3 or marks[2][0] + marks[1][1] + marks[0][2] == 3:
        winner = 1
        gameOver = True
    if marks[0][0] + marks[1][1] + marks[2][2] == -3 or marks[2][0] + marks[1][1] + marks[0][2] == -3:
        winner = 2
        gameOver = True

def playerWinner(playerMsg):
        winTxtColor = (0,0,255)
        winTxt = playerMsg
        winImg = font.render(winTxt,True,winTxtColor)
        pygame.draw.rect(screen,green,(screenWidth // 2 * 100, screenHeight // 2 - 60, 200, 50))
        screen.blit(winImg,(screenWidth // 2 - 100, screenHeight // 2 - 50))

        playAgainTxt = "Play Again?"
        playAgainImg = font.render(playAgainTxt,True,winTxtColor)
        pygame.draw.rect(screen,green,againRect)
        screen.blit(playAgainImg,(screenWidth // 2 - 80, screenHeight // 2 + 10))

def draWinnerScrn(winner):
    msg = ""
    if winner == 0:
        msg = "No Player Wins!"
        playerWinner(msg)
    else:
        msg = "Player " + str(winner) + "wins!"
        playerWinner(msg)
while isRunning:
    #event handling
    drawGrid()
    drawMarks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if gameOver == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                position = pygame.mouse.get_pos()
                cell_x = position[0]
                cell_y = position[1]
                if marks[cell_x // 100][cell_y//100] == 0:
                    marks[cell_x // 100][cell_y//100] = player
                    player *= -1
                    checkWinner()
    if gameOver == True:
        draWinnerScrn(winner)
        if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and clicked == True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if againRect.collidepoint(pos):
                player = 1
                marks = []
                position = []
                gameOver = False
                winner = 0
                for x in range(3):
                    row = [0] * 3
                    marks.append(row)
    pygame.display.update()
pygame.quit()