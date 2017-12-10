# Unit PYG02: Pygame Wall Ball Game version 2
'''
开发框架：
    引用
    初始化
    响应
        刷新
'''

# 引用
import pygame, sys
from pygame.locals import *

# 初始化
pygame.init()
size = width, height = 600, 400
speed = [1, 1]
black = 0, 0, 0
fps = 300
fclock = pygame.time.Clock()                                    # 创建一个Clock对象，用于操作时间                    

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame壁球")

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

# 响应
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # 刷新
    screen.fill(black)
    screen.blit(ball, ballrect)
    fclock.tick(fps)
    pygame.display.update()
