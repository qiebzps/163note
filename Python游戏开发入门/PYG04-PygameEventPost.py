# Unit PYG04: Pygame Event Post

import pygame, sys                          # 引入

pygame.init()                               # 初始化(对Pygame内部各功能模块进行初始化创建及变量设置，默认调用)
size = (600,400)
caption = "Pygame游戏之旅"
screen = pygame.display.set_mode(size) # 窗口大小600x400
pygame.display.set_caption(caption)# 设置标题
fps = 1
fclock = pygame.time.Clock()
num = 1

# main loop
while True:
    uevent = pygame.event.Event(pygame.KEYDOWN, {"unicode":123, "key":pygame.K_SPACE, "mod":pygame.KMOD_ALT})
    pygame.event.post(uevent)
    num = num + 1
    for event in pygame.event.get():        # 响应事件
        if event.type == pygame.QUIT:       # 退出事件
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN {}]:".format(num), "#", event.key, event.mod)
            else:
                print("[KEYDOWN {}]:".format(num), event.unicode, event.key, event.mod)
    pygame.display.update()                 # 刷新
    fclock.tick(fps)
    
