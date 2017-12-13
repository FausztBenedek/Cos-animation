import pygame
import math

#Screen sides
WIDTH = 700; HEIGHT = 500
#Colors
BLACK = (0, 0, 0);          WHITE = (255, 255, 255)
YELLOW = (255, 255, 0);     RED = (255, 0, 0)


class Circle:

    def __init__(self, surface, radius, pos = [WIDTH//2, HEIGHT//2], thick = 10):
        self.radius = radius;       self.surface = surface
        self.pos = pos;             self.thick = thick
        self.deg = 0
        self.vector = [math.sin(self.rad), math.cos(self.rad)]

    def upd(self):
        self.deg += 1
        if self.deg == 360: self.deg = 0
        self.vector = [math.sin(self.rad), math.cos(self.rad)]

    def drw(self):
        self._drwCoordinateSys()
        self._drwUnitCircle()
        self._drwMovingCircle()
        
    def _drwUnitCircle(self):
        pygame.draw.circle(self.surface, WHITE, self.pos, self.radius, self.pathThickness)
    def _drwMovingCircle(self):
        pygame.draw.circle(self.surface, YELLOW, self.edgepos, self.thick)
    def _drwCoordinateSys(self):
        drw = pygame.draw.line
        start = list(self.pos);           end = list(self.pos) 
        start[1] += int(self.radius * 1.2)
        end[1] -= int(self.radius *1.2)

        drw(self.surface, WHITE, start, end, self.pathThickness)
        start = list(self.pos);           end = list(self.pos) 
        start[0] += int(self.radius * 1.2)
        end[0] -= int(self.radius *1.2)
        drw(self.surface, WHITE, start, end, self.pathThickness)

    @property
    def rad(self):
        return math.radians(self.deg)
    @property
    def edgepos(self):
        vector = map(lambda x: x * self.radius, self.vector)
        return [int(x+y) for x,y in zip(self.pos, vector)] 
    @property
    def pathThickness(self):
        return self.thick//5


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Initialized declarations
circle = Circle(screen, 100)
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
