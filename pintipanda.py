from mainn import *
from pane import Panel
from ball import Ball
import pygame.font

running = True
pygame.init()
pygame.font.init()
#assignments
panel_left = Panel(0,screen_height//2 - panel_height//2,panel_width,panel_height)
panel_right = Panel(screen_width - panel_width,screen_height//2 - panel_height//2,panel_width,panel_height)
text_score = pygame.font.SysFont("comicsans", 30)
ball = Ball(screen_width//2,screen_height//2,10)

def draw(win):
    win.fill("black")
    panel_left.draw(win)
    panel_right.draw(win)
    ball.draw(win)
    show_score(left_score, right_score, win)
    pygame.draw.line(win,"white",(screen_width//2,0),(screen_width//2,screen_height),4)
    pygame.display.update()
    clock.tick(FPS)
def panel_movement(panel_left,panel_right):
    if keys[pygame.K_w] and panel_left.y >= 0:
        panel_left.movement(up=True)
    if keys[pygame.K_s] and panel_left.y + panel_height <= screen_height:
        panel_left.movement(up=False)
    if keys[pygame.K_UP] and panel_right.y >= 0:
        panel_right.movement(up=True)
    if keys[pygame.K_DOWN] and panel_right.y + panel_height <= screen_height:
        panel_right.movement(up=False)
def show_score(left_score,right_score,win):
    left_text = text_score.render(f"{str(left_score)}",True,"green")
    right_text = text_score.render(f"{str(right_score)}", True, "green")
    win.blit(left_text,(100,10))
    win.blit(right_text,(560, 10))

while running:
    keys = pygame.key.get_pressed()
    draw(WIN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if ball.x - ball.radius>= screen_width:
        left_score += 1
        ball.reset()
    elif ball.x <= 0:
        right_score += 1
        ball.reset()
    panel_movement(panel_left,panel_right)
    ball.move(panel_left,panel_right)
pygame.quit()


