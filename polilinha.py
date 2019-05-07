# -*-coding utf-8-*-
import sys
import pygame
import time
import função

pygame.init()  # inicialização do pygame

window = pygame.display.set_mode((500, 500))  # cria uma janela

pygame.display.set_caption("Teste do bresenham")  # Altera o nome da janela
controle = 1
controle2 = 0
while True:

    for event in pygame.event.get():  # um loop para checar se os eventos estão ocorrendo exemplo mouse,click,teclar

        if event.type == pygame.QUIT:  # quando clica no x da janela ele para o jogo
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # botao esquerdo do mouse clicado
                if controle == 1 and controle2 == 0:
                    x1, y1 = pygame.mouse.get_pos()
                    controle += 1
                elif controle == 2 and controle2 == 0:
                    x2, y2 = pygame.mouse.get_pos()
                    controle = 1
                    função.bresenham_completo(window,x1,y1,x2,y2)
                    controle2 = 1
                elif controle == 1 and controle2 == 1:
                    x1=x2
                    y1=y2
                    x2,y2=pygame.mouse.get_pos()
                    função.bresenham_completo(window,x1,y1,x2,y2)
    time.sleep(0.03)
    pygame.display.update()  # refresh da janela
