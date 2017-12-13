import pygame 
import math 
from function import *
from tools import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Initialized declarations
function = Function(screen)
running = True
while running:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
    
    # Update
    function.upd()

    # Draw
    screen.fill(BLACK)
    function.drw()
    pygame.display.flip()
