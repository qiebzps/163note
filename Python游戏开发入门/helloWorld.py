# Unit PYG02: Pygame Hello World Game

import pygame, sys                          # 引入

pygame.init()                               # 初始化(对Pygame内部各功能模块进行初始化创建及变量设置，默认调用)
screen = pygame.display.set_mode((600,400)) # 窗口大小600x400
pygame.display.set_caption("Pygame游戏之旅")# 设置标题

# main loop
while True:
    for event in pygame.event.get():        # 响应事件
        if event.type == pygame.QUIT:       # 退出事件
            pygame.quit()
            sys.exit()
    pygame.display.update()                 # 刷新
    
