import pygame

white = (255, 255, 255)


# Esta funcao funciona apenas
# para o primeiro quadrante
def bresenham(screen, x1, y1, x2, y2):
    # carrega no fb o pixel (x1,y1)
    screen.set_at((x1, y1), white)
    # computa os deltas necessarios
    dx = x2 - x1
    dy = y2 - y1
    dy2 = 2 * dy
    dydx2 = dy2 - 2 * dx
    pant = dy2 - dx
    x = x1
    y = y1

    for i in range(dx):
        if pant < 0:
            screen.set_at((x + 1, y), white)
            pant = pant + dy2
        else:
            screen.set_at((x + 1, y + 1), white)
            pant = pant + dydx2
            y += 1
        x += 1
    pygame.display.flip()


def ROUND(n):
    return int(n+0.5)


def dda(screen, x1, y1, x2, y2):
    x, y = x1, y1
    length = (x2-x1)
    if length <= (y2-y1):
        length = y2 - y1
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    screen.set_at((ROUND(x), ROUND(y)), white)

    for i in range(length):
        x += dx
        y += dy
        screen.set_at((ROUND(x), ROUND(y)), white)
    pygame.display.flip()