import pygame
import math
from tools import *
from circle import *

class Function:

    def __init__(self, screen):
        self.unitCircle = Circle(screen, WIDTH//9, pos = [WIDTH//6, HEIGHT//2])
        
        self.screen = screen

    def upd(self):
        self.unitCircle.upd()
            
    def drw(self):
        self.unitCircle.drw()
