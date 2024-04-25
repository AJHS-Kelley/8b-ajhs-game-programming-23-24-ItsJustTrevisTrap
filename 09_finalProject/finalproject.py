# Trevis you have almost nothing done at all for this project after almost three weeks of classtime. 

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

mazeBackground = pygame.image.load('Final  project/maze.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()        

    screen.blit(mazeBackground,(0,0))

    pygame.display.update()
    clock.tick(60)

