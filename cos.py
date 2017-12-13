import pygame 
import math 
from function import *
from circle import Circle

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Initialized declarations
circle = Circle(screen, WIDTH//9, pos = [WIDTH//6, HEIGHT//2])
running = True
while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    
    # Update
    circle.upd()

    # Draw
    screen.fill(BLACK)
    circle.drw()
    pygame.display.flip()
