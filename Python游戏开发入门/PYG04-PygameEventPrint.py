# Unit PYG04: Pygame Event Print
import pygame, sys

pygame.init()

size = 600, 400
caption = "Pygame事件处理"

screen = pygame.display.set_mode(size)
pygame.display.set_caption(caption)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN]:", "#", event.key, event.mod)
            else: 
                print("[KEYDOWN]:",event.unicode, event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            print("[MOUSEMOTION]:", event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("[MOUSEBUTTONUP]:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]", event.pos, event.button)

                
    pygame.display.update()

