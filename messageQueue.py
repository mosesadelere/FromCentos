import pygame
from pygame.locals import *
from sys import exit

pygame.init()
SCREENSIZE = (800,600)
screen = pygame.display.set_mode(SCREENSIZE, 0, 32)

font = pygame.font.SysFont("arial", 16)
fontHeight = font.get_linesize()
event_text = []

while True:
    event = pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[int (-SCREENSIZE[1]/fontHeight) : ]

    if event.type == QUIT:
        exit()

    screen.fill((255,0,218))

    y = SCREENSIZE[1] - fontHeight

    for text in reversed(event_text):
        screen.blit(font.render(text, True, (0, 0, 0)), (0, y))
        y -= fontHeight

    pygame.display.update()