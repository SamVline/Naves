import pygame

### Variables ###

ALTO = 800
ANCHO = 1000
ALTO_NAVE = ALTO/25
ANCHO_NAVE = ANCHO/25
MARGEN = ANCHO_NAVE/2
FPS = 30
VEL_NAVE = 10
VEL_ROCA = 10
TAM_ROCA = 20


class Navesteroides:

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.reloj = pygame.time.Clock()

        pos_y = (ALTO-ALTO_NAVE)/2
        pos_x = (MARGEN)

        pygame.font.init()
