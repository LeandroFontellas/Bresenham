import numpy
import pygame


def bezieringenuo(screen, p1, p2, p3):
    white = (255, 255, 255)
    for t in numpy.arange(0, 1, 0.005):
        omt = 1 - t
        omt2 = omt * omt
        omt3 = omt2 * omt
        t2 = t * t
        t3 = t2 * t
        x = omt3 * p1[0] + ((3 * omt2) * t * p1[0]) + (3 * omt * t2 * p2[0]) + t3 * p3[0]
        y = omt3 * p1[1] + ((3 * omt2) * t * p1[1]) + (3 * omt * t2 * p2[1]) + t3 * p3[1]
        x = int(numpy.floor(x))
        y = int(numpy.floor(y))

        screen.set_at((x, y), white)
        pygame.display.flip()
