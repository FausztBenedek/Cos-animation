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
