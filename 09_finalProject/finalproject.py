# Trevis you have almost nothing done at all for this project after almost three weeks of classtime. 

import pygame
import random

#Constants
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 40
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE
PLAYER_SIZE = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 128, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create maze
maze = [[1 for _ in range(COLS)] for _ in range(ROWS)]

def generate_maze(x, y):
    maze[y][x] = 0
    
    directions = [(x, y-2), (x, y+2), (x-2, y), (x+2, y)]
    random.shuffle(directions)

    for dx, dy in directions:
        if 0 <= dx < COLS and 0 <= dy < ROWS and maze[dy][dx] == 1:
            maze[(y + dy) // 2][(x + dx) // 2] = 0
            generate_maze(dx, dy)
     
generate_maze(random.randrange(1, COLS, 2), random.randrange(1, ROWS, 2))

# Player
player_x = CELL_SIZE // 2
player_y = CELL_SIZE // 2

# Main loop
running = True
while running:
    for event in
pygame.event.get():
if event.type == 
pygame.QUIT:
running = False



