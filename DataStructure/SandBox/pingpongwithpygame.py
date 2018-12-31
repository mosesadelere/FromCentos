import pygame
from pygame.locals import *
from random import *
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600), 0, 32)
pygame.display.set_caption('Ping Pong Game')
running = True
print(pygame.K_s)
while running == True:

    paddle_colorA = (255, 255, 255)
    paddle_colorB = (255, 0, 0)
    ball_color = ((0), (255), (0))
    xA, yA = 0, 275
    paddle_posB = [790, 275]
    ball_position = [400, 300]
    ball_radius = 10
    width, lenght = 10, 50
    #print(pygame.K_DOWN)
    #color = 255, 255, 0
    #screen.lock()
    padA = pygame.Rect(xA, yA, width, lenght)
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, paddle_colorA, padA)
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
                pygame.quit()
            elif event.key == K_r:
                yA = yA + 100
            elif event.key == K_w:
                yA = yA - 100

    #pressedKey = pygame.key.get_pressed()
    #if pressedKey[pygame.K_SPACE] == 1:
     #   yA += 100
    #if pressedKey[pygame.K_RIGHT] == 275:
     #   yA -= 100
    #if pressedKey[pygame.K_UP] == 273:
     #   paddle_posB[1] += 10
    #if pressedKey[pygame.K_DOWN] == 274:
     #   paddle_posB[1] -= 10


    """
    if event.type == K_a:
        paddleA.move(0, -10)
    if event.type == K_b:
        paddleA.move(0, 10)
    if event.type == K_UP:
        paddleB.move(0, -10)
    if event.type == K_DOWN:
        paddleB.move(0, 10)"""
    #paddleB = pygame.draw.rect(screen, paddle_colorB, Rect(paddle_posB, paddle_size))
    #ball = pygame.draw.circle(screen, ball_color, ball_position, ball_radius)

    #screen.unlock()
    pygame.display.flip()
    #pygame.display.update()