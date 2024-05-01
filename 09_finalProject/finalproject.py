import pygame
import random

#Constants
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 40
ROWS = HEIGHT // CELL_SIZE
COLS = WIDTH // CELL_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create maze
maze = [[0 for _ in range(COLS)]]

def generated_maze(x, y):
    maze[y][x] = 1 





