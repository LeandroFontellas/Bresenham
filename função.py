white = (255, 255, 255)


def bresenham_completo(screen, x1, y1, x2, y2):

    if x2 >= x1:
        dx = (x2-x1)  # estabelecimento do modulo de dx
        incx = 1  # da esquerda para a direita
    else:
        dx = (x1-x2)
        incx = -1

    if y2 >= y1:
        dy = (y2-y1)  # modulo de dy
        incy = 1  # de baixo para cima
    else:
        dy = (y1-y2)
        incy = -1  # de cima para baixo
    x = x1
    y = y1
    screen.set_at((x1, y1), white)

    if dx == 0:
        if incy > 0:
            for y in range(y, y2):  # Nao tenho ctz
                screen.set_at((x, y), white)
        else:
            for y in range(y2, y1):
                screen.set_at((x, y), white)
    elif dy == 0:
        if incx > 0:
            for x in range(x, x2):
                screen.set_at((x, y), white)
        else:
            for x in range(x2, x1):
                screen.set_at((x, y), white)
    else:
        if dx >= dy:
            d = (2*dy-dx)
            incE = 2*dy
            incNE = 2*(dy-dx)
            while x != x2:
                if d <= 0:
                    d = d+incE
                    x = x+incx
                else:
                    d = d+incNE
                    x = x+incx
                    y = y+incy
                screen.set_at((x, y), white)
        else:
            d = (2*dx-dy)
            incE = 2*dx
            incNE = 2*(dx-dy)
            while y != y2:
                if d <= 0:
                    d = d+incE
                    y = y+incy
                else:
                    d = d+incNE
                    y = y+incy
                    x = x+incx
                screen.set_at((x, y), white)
