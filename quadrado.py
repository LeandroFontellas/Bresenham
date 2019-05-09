# -*-coding utf-8-*-
import sys
import pygame
import time
import função
import math

pygame.init()  # inicialização do pygame

window = pygame.display.set_mode((500, 500))  # cria uma janela

pygame.display.set_caption("Teste do bresenham")  # Altera o nome da janela
controle = 1
while True:

    for event in pygame.event.get():  # um loop para checar se os eventos estão ocorrendo exemplo mouse,click,teclar

        if event.type == pygame.QUIT:  # quando clica no x da janela ele para o jogo
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # botao esquerdo do mouse clicado
                if controle == 1:
                    x1, y1 = pygame.mouse.get_pos()
                    controle += 1
                elif controle == 2:
                    x2, y2 = pygame.mouse.get_pos()
                    controle = 1
                    if y1==y2 or x1 == x2:
                        if x1==x2:
                            if x1>x2:
                                distancia=y2-y1
                            else:
                                distancia=y1-y2

                            função.bresenham_completo(window,x2,y2,x2+distancia,y2)
                            função.bresenham_completo(window,x2,y2,x2,y2+distancia)
                            função.bresenham_completo(window,x2+distancia,y2,x2+distancia,y2+distancia)
                            função.bresenham_completo(window,x2,y2+distancia,x2+distancia,y2+distancia)
                        elif y1==y2:
                            if y1>y2:
                                distancia=x2-x1
                            else:
                                distancia=x1-x2

                            função.bresenham_completo(window, x2, y2, x2 + distancia, y2)
                            função.bresenham_completo(window, x2, y2, x2, y2 + distancia)
                            função.bresenham_completo(window, x2 + distancia, y2, x2 + distancia, y2 + distancia)
                            função.bresenham_completo(window, x2, y2 + distancia, x2 + distancia, y2 + distancia)
                    else:
                        if y2>y1 and x2>x1:
                            distancia=int(math.sqrt(((y2-y1)*(y2-y1))+((x2-x1)*(x2-x1))))
                            função.bresenham_completo(window, x1, y1, x1 + distancia, y1)
                            função.bresenham_completo(window, x1, y1, x1, y1 + distancia)
                            função.bresenham_completo(window, x1 + distancia, y1, x1 + distancia, y1 + distancia)
                            função.bresenham_completo(window, x1, y1 + distancia, x1 + distancia, y1 + distancia)
                        elif y2>y1 and x2<x1:
                            distancia = int(math.sqrt(((y2 - y1) * (y2 - y1)) + ((x1 - x2) * (x1 - x2))))
                            função.bresenham_completo(window, x1, y1, x1 - distancia, y1)
                            função.bresenham_completo(window, x1, y1, x1, y1 + distancia)
                            função.bresenham_completo(window, x1 - distancia, y1, x1 - distancia, y1 + distancia)
                            função.bresenham_completo(window, x1, y1 + distancia, x1 - distancia, y1 + distancia)
                        elif y2<y1 and x2>x1:
                            distancia = int(math.sqrt(((y1 - y2) * (y1 - y2)) + ((x1 - x2) * (x1 - x2))))
                            função.bresenham_completo(window, x1, y1, x1 + distancia, y1)
                            função.bresenham_completo(window, x1, y1, x1, y1 - distancia)
                            função.bresenham_completo(window, x1 + distancia, y1, x1 + distancia, y1 - distancia)
                            função.bresenham_completo(window, x1, y1 - distancia, x1 + distancia, y1 - distancia)
                        else:
                            distancia = int(math.sqrt(((y1 - y2) * (y1 - y2)) + ((x2 - x1) * (x2 - x1))))
                            função.bresenham_completo(window, x1, y1, x1 - distancia, y1)
                            função.bresenham_completo(window, x1, y1, x1, y1 - distancia)
                            função.bresenham_completo(window, x1 - distancia, y1, x1 - distancia, y1 - distancia)
                            função.bresenham_completo(window, x1, y1 - distancia, x1 - distancia, y1 - distancia)





    time.sleep(0.03)
    pygame.display.update()  # refresh da janela
