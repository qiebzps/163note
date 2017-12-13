# Unit PYG04: Pygame Wall Ball Game version 8
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
still = False                                                   # 小球静止还是移动

screen = pygame.display.set_mode(size, pygame.RESIZABLE)        # 屏幕大小可调
pygame.display.set_caption("Pygame壁球")

icon = pygame.image.load("ball.gif")
pygame.display.set_icon(icon)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

# 响应
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:                       # esc退出
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_LEFT:
                speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0]) - 1) * int(speed[0]/abs(speed[0]))
            elif event.key == pygame.K_RIGHT:
                speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
            elif event.key == pygame.K_UP:
                speed[1] = speed[1] + 1if speed[1] > 0 else speed[1] - 1
            elif event.key == pygame.K_DOWN:
                speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1] - 1) * int(speed[1]/abs(speed[1])))
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size[0], event.size[1]
            pygame.display.set_mode(size, pygame.RESIZABLE)
        elif event.type == pygame.MOUSEBUTTONDOWN:              # 对鼠标摁下事件的响应
            if event.button == 1:
                still = True
        elif event.type == pygame.MOUSEBUTTONUP:
            still = False
            if event.button == 1:
                ballrect = ballrect.move(event.pos[0]-ballrect.left, event.pos[1]-ballrect.top)
        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0] == 1:
                ballrect = ballrect.move(event.pos[0]-ballrect.left, event.pos[1]-ballrect.top)
    if pygame.display.get_active() and not still:                             # 窗口是否图标化
        ballrect = ballrect.move(speed[0],speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        if ballrect.right > width and ballrect.right + speed[0] > ballrect.right:
            speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        if ballrect.bottom > height and ballrect.bottom + speed[1] > ballrect.bottom:
            speed[1] = -speed[1]

    # 刷新
    screen.fill(black)
    screen.blit(ball, ballrect)
    fclock.tick(fps)
    pygame.display.update()
