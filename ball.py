
from mainn import *


class Ball:
    def __init__(self,x,y,radius):

        self.game_over = False
        self.vel_x = 4
        self.vel_y = 4
        self.x = self.xoriginal = x
        self.y = self.yoriginal = y
        self.radius = radius

    def move(self,panel_left,panel_right):
        self.x += self.vel_x
        self.y -= self.vel_y

        if self.y - self.radius <= 0:
            self.vel_y *= -1
        elif self.y + self.radius >= screen_height:
            self.vel_y *= -1
        if self.y >= panel_right.y and self.y <= panel_right.y + panel_height:
            if self.x + self.radius >= panel_right.x:
                self.vel_x *= -1
        if self.y >= panel_left.y and self.y <= panel_left.y + panel_height:
            if self.x - self.radius <= panel_left.x + panel_width:
                self.vel_x *= -1

    def reset(self):
        self.y = self.yoriginal
        self.x = self.xoriginal

    def draw(self,win):
        pygame.draw.circle(win,"white",(self.x,self.y),self.radius)
