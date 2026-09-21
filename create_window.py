import pygame, sys
from pygame.locals import *

pygame.init()
display = pygame.display.set_mode((700, 400))
pygame.display.set_caption("Hello World")
bg_color = ("white")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        display.fill(bg_color)
        pygame.display.update()