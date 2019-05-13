# -*- coding: utf-8 -*-
import sys,pygame, time,funcao_bezier


pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 0))
pygame.display.flip()

white = (255, 255, 255)
controle = 1

while True:

    for event in pygame.event.get():  # um loop para checar se os eventos estão ocorrendo exemplo mouse,click,teclar

        if event.type == pygame.QUIT:  # quando clica no x da janela ele para o jogo
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # botao esquerdo do mouse clicado
                if controle == 1:
                    x = pygame.mouse.get_pos()
                    controle += 1
                elif controle == 2:
                    y = pygame.mouse.get_pos()
                    controle +=1
                elif controle == 3:
                    z = pygame.mouse.get_pos()
                    controle=1
                    funcao_bezier.bezieringenuo(screen,x,y,z)
    time.sleep(0.03)
    pygame.display.update()
