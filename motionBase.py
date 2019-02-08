import pygame
import math
from tools import WHITE


class MotionBase(object):

    __deg = 0
    __dDeg = 1
    
    def __init__(self, surface, radius, center, ballWidth):
        self.surface = surface
        self.radius = radius
        self.center = center
        self.__ballWidth = ballWidth

    @classmethod
    def upd(cls):
        cls.__deg += cls.__dDeg
        if cls.__deg >= 360: cls.__deg = 0

    @classmethod
    def _drwAxis(cls, surface, start, end, lineWidth):
        pygame.draw.line(surface, WHITE, start, end, lineWidth)

    @property
    def radian(self):           return math.radians(self.__deg)
    @property
    def dDeg(self):             return self.__dDeg
    @property
    def deg(self):              return self.__deg
    @property
    def ballWidth(self):        return self.__ballWidth
    @property
    def lineWidth(self):        return int(self.ballWidth/5)
