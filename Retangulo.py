# -*-coding utf-8-*-
import sys
import pygame
import time
import função

pygame.init()

window = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Teste do bresenham")
controle = 1
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if controle == 1:
                    x1, y1 = pygame.mouse.get_pos()
                    controle += 1
                elif controle == 2:
                    x2, y2 = pygame.mouse.get_pos()
                    controle = 1
                    função.bresenham_completo(window,x1,y1,x2,y1)
                    função.bresenham_completo(window,x1,y1,x1,y2)
                    função.bresenham_completo(window,x1,y2,x2,y2)
                    função.bresenham_completo(window,x2,y1,x2,y2)

    time.sleep(0.03)
    pygame.display.update()  # refresh da janela