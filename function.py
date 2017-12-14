import pygame
import math
from tools import *
from circle import *
from motionBase import MotionBase

class Function(MotionBase):

    def __init__(self, surface, radius, center, ballWidth):
        super(Function, self).__init__(surface, radius, center, ballWidth)
        self.vector = [0, math.cos(self.radian)]

    def upd(self):
        self.vector = [0, math.cos(self.radian)]
            
    def drw(self):
        self.__drwCoordinateSys()
        self.__drwBall()

    def __drwCoordinateSys(self):
        start = list(self.center);             end = list(self.center)
        start[1] += int(self.radius * 1.2); end[1] -= int(self.radius *1.2)
        MotionBase._drwAxis(self.surface, start, end, self.lineWidth)

        start = list(self.center);             end = list(self.center)
        start[0] -= int(self.radius * 0.15);       end[0] = WIDTH
        MotionBase._drwAxis(self.surface, start, end, self.lineWidth)
    def __drwBall(self):
        pygame.draw.circle(self.surface, YELLOW, self.ballPos, self.ballWidth)

    @property
    def ballPos(self):
        vector = list(self.vector)
        vector[1] *= self.radius
        return [int(x+y) for x,y in zip(self.center, vector)]
