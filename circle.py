import pygame
import math
from tools import * 

class Circle:

    def __init__(self, surface, radius, pos = [WIDTH//2, HEIGHT//2], thick = 10):
        self.radius = radius;       self.surface = surface
        self.pos = pos;             self.thick = thick
        self.deg = 0
        self.vector = [math.sin(self.radian), math.cos(self.radian)]

    def upd(self):
        self.deg += 1
        if self.deg == 360: self.deg = 0
        self.vector = [math.sin(self.radian), math.cos(self.radian)]

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
    def radian(self):
        return math.radians(self.deg)
    @property
    def edgepos(self):
        vector = map(lambda x: x * self.radius, self.vector)
        return [int(x+y) for x,y in zip(self.pos, vector)]
    @property
    def pathThickness(self):
        return self.thick//5

