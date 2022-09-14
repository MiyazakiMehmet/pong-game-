import pygame
from mainn import *

class Panel:
    def __init__(self,x,y,width,height):
        self.vel = 8
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def movement(self,up=True):
        if up:
            self.y -= self.vel
        if not up:
            self.y += self.vel

    def draw(self,win):
        pygame.draw.rect(win, "white",pygame.Rect(self.x,self.y,self.width,self.height))
