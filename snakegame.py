from operator import truediv
from re import X
from turtle import speed
import pygame
import sys
import os
import random
import math

pygame.init()
pygame.display.set_caption("Snake Game")
pygame.font.init()
random.speed()

# we will declare global content definition

SPEED = 0.30
SNAKE_SIZE = 9
APPLE = SNAKE_SIZE
SEPARATION = 10
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
FPS = 25
KEY = {"UP": 1, "DOWN": 2, "LEFT": 3, "RIGHT": 4}

#we will initialisze screen
screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_HEIGHT), pygame.HWSURFACE)
#we have user hw surface which stands for hardware surface refers to using memory on the video card for storing
# draws as opposed to main memory

#resource
score_font = pygame.font.Font(None, 18)
score_numb_font = pygame.font.Font(None, 28)
game_over_font = pygame.font.Font(None, 48)
play_again_font = score_font
score_msg = score_font.render("Score : ", 1, pygame.Color("green"))
score_msg_size = score_font.size("Score")
background_color = pygame.Color(0,0,0) #we will fill bacground color as black
black = pygame.Color(0,0,0)

# for clock at the left corner
gameClock = pygame.time.Clock()

def checkCollision(posA, As, posB, Bs): # As in the size of a and Bs is the size of b
    if (posA.x < posB.x+Bs and posA.x+As > posB.x and posA.y < posB.y+Bs and posA.y+As > posB.y ):
        return True
    return False

#to check the boundaries here we are not listing boundaries liek it can pass through screen and come from other side

def checkLimits(snake):
    if (snake.x > SCREEN_WIDTH):
        snake.x = SNAKE_SIZE
    if (snake.x < 0):   #this will be checked when some part of snake is on other side and some on opposite side
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if (snake.y > SCREEN_HEIGHT):
        snake.y = SNAKE_SIZE
    if (snake.y < 0):   #this also same half half
        snake.y = SCREEN_HEIGHT - SNAKE_SIZE

#we will make class for food the snake let's name it as apple

class Apple:
    def __init__(self,x,y,state):
        self.x = x
        self.y = y
        self.state = state
        self.color = pygame.color.Color("orange")

    def draw(self, screen):
        pygame.draw.rect(screen,self.color,(self.x,self.y,APPLE_SIZE,APPLE_SIZE),0)

class segment:
    #initially snake will move in up direction
    self.x = x
    self.y = y
    self.direction = KEY["UP"]
    self.color = "white"

class snake:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.direction = KEY["UP"]
        self.stack = [] #initially it will be empty
        self.stack.append(self)
        blackBox = segment(self.x, self.y + SEPARATION)
        blackBox.color = "NULL"
        self.stack.append(blackBox)

#we will define moves of the snake
    def move(self):
        last_element = len(self.stack) - 1
        while(last_element is 0):
            self.stack[last_element].direction = self.stack[last_element].direction
            self.stack[last_element].x = self.stack[last_element - 1].x
            self.stack[last_element].y = self.stack[last_element - 1].y
            last_element -= 1
            if (len(self,stock) < 2):
                last_segment = self
            else:
                last_segment = self.stack.pop(last_element)
            last_segment.direction = self.stack[0].direction
            if(self.stack[0].direction == KEY["UP"]):
                last_segment.y = self.stack[0].y - (SPEED + FPS)
            elif(self.stack[0].direction == KEY["DOWN"]):
                last_segment.y = self.stack[0].y + (SPEED + FPS)
            elif(self.stack[0].direction == KEY["LEFT"]):
                last_segment.x = self.stack[0].x - (SPEED + FPS)
            elif(self.stack[0].direction == KEY["RIGHT"]):
                last_segment.x = self.stack[0].x + (SPEED + FPS)
            self.stack.insert(0,last_segment)


#we will define keys

def getKey():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return KEY["UP"]
            elif event.key == pygame.K_DOWN:
                return KEY["DOWN"]
            elif event.key == pygame.K_LEFT:
                return KEY["LEFT"]
            elif event.key == pygame.K_RIGHT:
                return KEY["RIGHT"]
            #for exit
            elif event.key == pygame.K_ESCAPE:
                return "exit"
            #if we want to continue playing again
            elif event.key == pygame.K_y:
                return "yes"
            #if we don't want to continue
            elif event.key == pygame.K_n:
                return "no"
        if event.type == pygame.QUIT:
            sys.exit(0)

def endGame():
    message = game_over_font.render("Game Over",1,pygame.Color("white"))
    message_play_again = play_again_font.render("Play Again ? (Y/N)",1,pygame.Color("green"))
    screen.blit(message,(320,240))
    screen.blit(message_play_again,(120+12, 240+40))

    pygame.display.flip()
    pygame.display.update()

    mKey = getKey()
    while(mKey != "exit"):
        if(mKey == "yes"):
            main()
        elif(mKey == "no"):
            break
        mKey = getKey()
        gameClock.tick(FPS)
    sys.exit(0)

def drawScore():
    score_numb = score_numb_font.render(str(score),1,pygame.Color("red"))
    screen.blit(score_msg, (SCREEN_WIDTH - score_msg_size[0]-60, 10))
    screen.blit(score_numb,(SCREEN_WIDTH - 45,14))

def drawGameTime():
    game_time = score_font.render("Time : "), 1,pygame.Color("white"))
    game_time_numb = score_numb_font.render(str(gameTime/1000),1,pygame.Color("white"))
    screen.blit(game_time,(10,10))
    screen.blit(game_time_numb,(100,14))

def exitScreen():
    pass

def main():
    score = 0
