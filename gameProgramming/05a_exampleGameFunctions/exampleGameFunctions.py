# Example Game Functions Project, Trevis Brown, v0.0
#import pygame
import random

# Initialize pygame
#pygame.init()

# Set up the game window
width = 800
height = 600
#window = pygame.display.set_mode((width, height))
#pygame.display.set_caption("Racing Game")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set up the player car
car_width = 73
car_height = 82
#car_img = pygame.image.load("car.png")
#car_img = pygame.transform.scale(car_img, (car_width, car_height))
car_x = width // 2 - car_width // 2
car_y = height - car_height - 10
car_speed = 5     

# Set up the enemy car
enemy_width = 73
enemy_height = 82
#car_img = pygame.image.load("car.png")
#car_img = pygame.transform.scale(car_img, (car_width, car_height))
car_x = width // 2 - car_width // 2
car_y = height - car_height - 10
car_speed = 5

# Set up the team car 
team_width = 73
team_height = 82
#car_img = pygame.image.load("car.png")
#car_img = pygame.transform.scale(car_img, (car_width, car_height))
car_x = width // 2 - car_width // 2
car_y = height - car_height - 10
car_speed = 5

# Set up track
track_length = 500
track_time = 180
track_width = 250







