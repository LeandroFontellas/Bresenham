import pygame
import sys
import math
from primitives import *
import time

screen_size = (800, 600)

# Variaveis de estilo
background = white
foreground = black

pygame.init()
window = pygame.display.set_mode(screen_size)

pygame.display.set_caption('Trabalho computacao grafica')
window.fill(background)
pygame.display.flip()

# Cor 0
quadrado(window, 0, 50, 50, 50, black)
# Cor 1
quadrado(window, 50, 100, 50, 50, black)
# Cor 2
quadrado(window, 100, 150, 50, 50, black)
# Cor 3
quadrado(window, 150, 200, 50, 50, black)
# Cor 4
quadrado(window, 200, 250, 50, 50, black)
# Cor 5
quadrado(window, 250, 300, 50, 50, black)
# Cor 6
quadrado(window, 300, 350, 50, 50, black)
# Cor 7
quadrado(window, 350, 400, 50, 50, black)
# Cor 8
quadrado(window, 400, 450, 50, 50, black)
# Cor 9
quadrado(window, 450, 500, 50, 50, black)
# Cor 10
quadrado(window, 500, 550, 50, 50, black)
# Cor 11
quadrado(window, 550, 600, 50, 50, black)
# Cor 12
quadrado(window, 600, 650, 50, 50, black)
# Cor 13
quadrado(window, 650, 700, 50, 50, black)
# Cor 14
quadrado(window, 700, 750, 50, 50, black)
# Cor 15
quadrado(window, 750, 800, 50, 50, black)

# interface:

bresenham2(window, 50, 50, 800, 50, black)
bresenham2(window, 50, 50, 50, 600, black)
#Moldura da janela
bresenham2(window,0,0,0,600,black)
bresenham2(window,0,0,800,0,black)
bresenham2(window,800,0,800,600,black)
bresenham2(window,0,600,800,600,black)


# para as primitivas
# linha
quadrado(window, 50, 50, 50, 100, black)
bresenham2(window, 10, 60, 40, 90, black)
# retângulo
quadrado(window, 50, 50, 100, 150, black)
retangulo(window, (10, 120), (40, 140), black)
# quadrado
quadrado(window, 50, 50, 150, 200, black)
quadrado(window, 10, 40, 160, 180, black)
# círculo
quadrado(window, 50, 50, 200, 250, black)
circulo(window,24,325,40,325,black)
# polilinha
quadrado(window, 50, 50, 300, 350, black)
bresenham2(window, 10, 260, 20, 280, black)
bresenham2(window, 20, 280, 30, 260, black)
bresenham2(window, 30, 260, 40, 280, black)
# spline ou bezier
quadrado(window, 50, 50, 250, 300, black)
bezier(window,(10,210),(20,240),(45,240),black)
# polilinha
quadrado(window, 50, 50, 300, 350, black)
bresenham2(window,10,260,20,280,black)
bresenham2(window,20,280,30,260,black)
bresenham2(window,30,260,40,280,black)

CorAtual = black
global primitiva
primitiva=0
controle=1#controle
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                p1 = pygame.mouse.get_pos()
                if primitiva == 0:
                    if p1[0] > 0 and p1[1] > 50 and p1[0] < 50 and p1[1]<100:
                        primitiva=1#linha
                        continue
                    if p1[0] > 0 and p1[1]>100 and p1[0] <50 and p1[1]< 150:
                        primitiva=2#retangulo
                        continue
                    if p1[0]>0 and p1[1]>150 and p1[0]<50 and p1[1]<200:
                        primitiva=3#quadrado
                        continue
                    if p1[0]>0 and p1[1]>200 and p1[0]<50 and p1[1]<250:
                        primitiva=4#bezier
                        continue
                    if p1[0]>0 and p1[1]>250 and p1[0]<50 and p1[1]<300:
                        primitiva=5#polilinha
                        continue
                    if p1[0]>0 and p1[1]>300 and p1[0]<50 and p1[1]<350:
                        primitiva=6#circulo
                        continue
                if primitiva == 1:#linha
                    if controle ==1:
                        p2=pygame.mouse.get_pos()
                        controle+=1
                        continue
                    if controle ==2:
                        controle=1
                        bresenham(window,p1[0],p1[1],p2[0],p2[1],black)
                        primitiva =0
                        continue
                if primitiva == 2:#retangulo
                    if controle ==1:
                        p2=pygame.mouse.get_pos()
                        controle+=1
                        continue
                    if controle ==2:
                        controle=1
                        retangulo2(window,p1,p2,black)
                        primitiva=0
                        continue
                if primitiva ==3:#quadrado
                    if controle ==1:
                        p2=pygame.mouse.get_pos()
                        controle+=1
                        continue
                    if controle ==2:
                        controle=1
                        quadrado2(window,p1[0],p1[1],p2[0],p2[1],black)
                        primitiva=0
                        continue
                if primitiva ==4:#bezier
                    if controle ==1:
                        p2=pygame.mouse.get_pos()
                        controle+=1
                        continue
                    if controle==2:
                        p3=pygame.mouse.get_pos()
                        controle+=1
                        continue
                    if controle ==3:
                        controle=1
                        primitiva = 0
                        bezier2(window,p1,p3,p2,black)
                        continue
                if primitiva==5:#polilinha
                    if controle==1:
                        p2=pygame.mouse.get_pos()
                        controle+=1
                        bresenham(window,p1[0],p1[1],p2[0],p2[1],black)
                        p3=[0,0]
                        p3[0]=p2[0]
                        p3[1]=p2[1]
                        continue
                    if controle==2:
                        p2=pygame.mouse.get_pos()
                        bresenham(window,p3[0],p3[1],p2[0],p2[1],black)
                        p3[0]=p2[0]
                        p3[1]=p2[1]
                        if p2[0]>0 and p2[1]>50 and p2[0]<50 and p2[1]<600:
                            primitiva=0
                        continue
                if primitiva==6:#circulo
                    if controle==1:
                        p2=pygame.mouse.get_pos()
                        controle+=1
                        continue
                    if controle==2:
                        controle=1
                        circulo(window,p1[0],p1[1],p2[0],p2[1],black)
                        primitiva=0
                        continue






    pygame.display.update()
