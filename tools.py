import pygame
import math

#Screen sides
WIDTH = 900; HEIGHT = 400
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
    drw(surface, WHITE, end, left, thickness)
    drw(surface, WHITE, end, right, thickness)
