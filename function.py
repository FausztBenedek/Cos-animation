import pygame
import math
from tools import *
from circle import *
from motionBase import MotionBase

class Function(MotionBase):

    def __init__(self, surface, radius, center, ballWidth):
        super(Function, self).__init__(surface, radius, center, ballWidth)
        self.vector = [0, math.cos(self.radian)]

        self.prePos = []
        self.howManyPrePos = WIDTH - self.center[0]
        for i in range(self.howManyPrePos):
            self.prePos.append(self.center)
        
  
    def upd(self):
        self.vector = [0, math.cos(self.radian)]
        for i in range(self.howManyPrePos):
            self.prePos[i][0] += 1
        self.prePos.pop(0)
        self.prePos.append(self.center)

    def drw(self):
        self.__drwCoordinateSys()
        self.__drwBall()
   
    def __drwCos(self):
        for i in range(len(self.prePos)-1):
            pygame.draw.line(self.surface, WHITE, self.prePos[i], self.prePos[i-1], self.lineWidth)

    def __drwCoordinateSys(self):
        start = list(self.center);           end = list(self.center)
        start[1] += int(self.radius * 1.2);  end[1] -= int(self.radius *1.2)
        MotionBase._drwAxis(self.surface, start, end, self.lineWidth)

        start = list(self.center);           end = list(self.center)
        start[0] -= int(self.radius * 0.15); end[0] = WIDTH
        MotionBase._drwAxis(self.surface, start, end, self.lineWidth)
    def __drwBall(self):
        pygame.draw.circle(self.surface, YELLOW, self.ballPos, self.ballWidth)

    @property
    def ballPos(self):
        vector = list(self.vector)
        vector[1] *= self.radius
        return [int(x+y) for x,y in zip(self.center, vector)]
