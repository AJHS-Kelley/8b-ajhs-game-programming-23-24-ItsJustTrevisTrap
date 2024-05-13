# Trevis Brown

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
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False

sky_surface = pygame.image.load('img/maze.png').convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
# Player movement

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if maze[player_y // CELL_SIZE][player_x // CELL_SIZE 1] == 0:
            player_x -= CELL_SIZE
        elif keys[pygame.K_RIGHT]:
            if maze[player_y // CELL_SIZE][player_x // CELL_SIZE + 1] == 0:
                player_x += CELL_SIZE
        elif keys[pygame.K_UP]:
            if maze[player_y // CELL_SIZE - 1][player_x // CELL_SIZE] == 0:
                player_y -= CELL_SIZE
        elif keys[pygame.K_DOWN]:
            if maze[player_y // CELL_SIZE + 1][player_x // CELL_SIZE] == 0:
                player_y += CELL_SIZE

    # Draw maze
    screen.fill(BLACK)
    for y in range(ROWS):
        for x in range(COLS):
            if maze[y][x] == 1: pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw player
    pygame.draw.circle(screen, GREEN, (player_x, player_y), PLAYER_SIZE)

    pygame.display.flip()
    clock.tick(60)

    pygame.quit









