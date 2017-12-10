# Unit PYG02: Pygame Wall Ball Game version 1
'''
开发框架：
    引用
    初始化
    事件处理
    窗口刷新
'''

import pygame, sys                               # 引入

pygame.init()                                   # init()初始化
size = width, height = 600, 400                 # 一个元组，将来做为窗口的大小
speed = [1,1]                                   # 做为小球移动的速度，x方向及y方向
BLACK = 0,0,0                                   # 黑色RGB
screen = pygame.display.set_mode(size)          # 设置screen的大小为size
pygame.display.set_caption("Pygame壁球")        # 标题
ball = pygame.image.load("PYG02-ball.gif")      # 加载小球gif,支持JPG,PNG,GIF(非动画)等13种常用图片格式
ballrect = ball.get_rect()                      # Pygame使用内部定义的Surface对象表示所有载入的图像，.get_rect()方法返回一个覆盖图像的矩形Rect对象

while True:                                     # mainloop
    for event in pygame.event.get():            # 获取事件
        if event.type == pygame.QUIT:           # 响应退出事件
            pygame.quit()
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])# 矩形移动一个偏移量（speed[0],speed[1]）
    if ballrect.left == 0 or ballrect.right == width:     # 碰壁处理x轴
        speed[0] = -speed[0]
    if ballrect.top == 0 or ballrect.bottom == height:    # 碰壁处理y轴
        speed[1] = -speed[1]

    screen.fill(BLACK)                                  # 填充颜色
    screen.blit(ball, ballrect)                         # 将ball 打印到 ballrect位置上
    pygame.display.update()
