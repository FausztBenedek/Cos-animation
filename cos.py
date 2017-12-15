import pygame 
import math 
from tools import WIDTH, HEIGHT, BLACK
from circle import Circle
from motionBase import MotionBase
from function import Function

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Initialized declarations
rad = WIDTH//9
circle = Circle(screen, rad, [WIDTH//6, HEIGHT//2], 10)
function = Function(screen, rad, [WIDTH//3, HEIGHT//2], 10)
running = True
while running:
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False

    # Update
    MotionBase.upd()
    circle.upd()
    function.upd()

    # Draw
    screen.fill(BLACK)

    circle.drw()
    function.drw()

    pygame.display.flip()
