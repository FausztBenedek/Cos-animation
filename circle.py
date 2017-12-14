import pygame
import math
from motionBase import MotionBase
from tools import WHITE, YELLOW

class Circle(MotionBase):

    def __init__(self, surface, radius, center, ballWidth):
        super(Circle, self).__init__(surface, radius, center, ballWidth)
        self.vector = [math.sin(self.radian), math.cos(self.radian)]

    def upd(self):
        self.vector = [math.sin(self.radian), math.cos(self.radian)]

    def drw(self):
        self.__drwCoordinateSys()
        self.__drwUnitCircle()
        self.__drwBall()

    def __drwUnitCircle(self):
        pygame.draw.circle(self.surface, WHITE, self.center, self.radius, self.lineWidth)
    def __drwBall(self):
        pygame.draw.circle(self.surface, YELLOW, self.ballPos, self.ballWidth)
    def __drwCoordinateSys(self):
        start = list(self.center);             end = list(self.center)
        start[1] += int(self.radius * 1.2); end[1] -= int(self.radius *1.2)
        MotionBase._drwAxis(self.surface, start, end, self.lineWidth)

        start = list(self.center);             end = list(self.center)
        start[0] -= int(self.radius * 1.2); end[0] += int(self.radius *1.2)
        MotionBase._drwAxis(self.surface, start, end, self.lineWidth)

    @property
    def ballPos(self):
        vector = map(lambda x: x * self.radius, self.vector)
        return [int(x+y) for x,y in zip(self.center, vector)]

