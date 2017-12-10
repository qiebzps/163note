'''
开发框架：
    引用
    初始化
    响应
        刷新
'''

# 引用
import pygame, sys

# 初始化
pygame.init()
size = width, height = 600,400
speed = [1,1]
black = 0,0,0

ball = pygame.image.load("ball.gif")      # 加载ball
ballrect = ball.get_rect()

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame游戏之旅")    # pygame只有一个窗口


# 响应
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           # 退出事件
            pygame.quit()
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    # 刷新
    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.update()
