import pygame
import math

#Screen sides
WIDTH = 700; HEIGHT = 500
#Colors
BLACK = (0, 0, 0);          WHITE = (255, 255, 255)
YELLOW = (255, 255, 0);     RED = (255, 0, 0)

#Functions
def getNormalized(vector):
    summa = vector[0] + vector[1]
    vector[0] /= summa
    vector[1] /= summa
    return vector

def getReversed(vector):
    return [-x for x in vector]

def getProduct(vector, number):
    return [number * x for x in vector]

def getRotatedUnitVector(vector, degree):
    actualDeg = math.degrees(math.asin(vector[0])) 
    actualDeg += degree
    return [math.sin(math.radians(actualDeg)), 
            math.cos(math.radians(actualDeg))
           ]

def drwAxis(surface, start, end, thickness):
    drw = pygame.draw.line
    drw(surface, WHITE, start, end, thickness)

    vector = [x-y for x, y in zip(end, start)]
    vector = getNormalized(vector)
    vector = getReversed(vector)
    left =  getRotatedUnitVector(vector, -30)
    right = getRotatedUnitVector(vector, 30) 
    left = getProduct(left, 10)
    right= getProduct(right,10)

    left = [x + y for x, y in zip(left , end)]
    right= [x + y for x, y in zip(right, end)]
    print(vector)
    drw(surface, WHITE, end, left, thickness)
    drw(surface, WHITE, end, right, thickness)


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
        start = list(self.pos);             end = list(self.pos) 
        start[1] += int(self.radius * 1.2); end[1] -= int(self.radius *1.2)
        drwAxis(self.surface, start, end, self.pathThickness)

        start = list(self.pos);             end = list(self.pos) 
        start[0] -= int(self.radius * 1.2); end[0] += int(self.radius *1.2)
        drwAxis(self.surface, start, end, self.pathThickness)

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
