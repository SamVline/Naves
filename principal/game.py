import os
import pygame
from pygame.sprite import Sprite

# miniatura y nombre de la ventana #

pygame.display.set_caption("Navesteroides")

### Variables ###

ALTO = 800
ANCHO = 1000
ALTO_NAVE = ALTO/20
ANCHO_NAVE = 50
MARGEN = ANCHO_NAVE/2
FPS = 60
VEL_NAVE = 12
CBLANCO = (255, 255, 180)
VEL_ROCA = 10
TAM_ROCA = 20


class Nave_imagen(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join("resources", "sprites", "navecita.png")
        )
        self.rect = self.image.get_rect()


class Nave(pygame.Rect):
    ARRIBA = True
    ABAJO = False
    VELOCIDAD = VEL_NAVE

    def __init__(self, pos_x, pos_y):
        super(Nave, self).__init__(pos_x, pos_y, ANCHO_NAVE, ALTO_NAVE)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, CBLANCO, self)

    def muevete(self, direccion):
        if direccion == self.ARRIBA:
            self.y = self.y - self.VELOCIDAD
            if self.y < 0:
                self.y = 0

        else:
            self.y = self.y + self.VELOCIDAD
            if self.y > ALTO-ALTO_NAVE:
                self.y = ALTO-ALTO_NAVE


class Navesteroides:

    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.reloj = pygame.time.Clock()

        ruta_icono = os.path.join(
            "resources", "sprites", "PNG", "Parts", "icono.png")
        ruta_fondo = os.path.join(
            "resources", "sprites", "Fondos", "Fondo1.jpg")
        ruta_nave = os.path.join(
            "resources", "sprites", "navecita.png")

        icono = pygame.image.load(ruta_icono)
        pygame.display.set_icon(icono)

        self.fondo = pygame.image.load(ruta_fondo)
        self.nave_imagen = pygame.image.load(ruta_nave)

        pos_y = (ALTO-ALTO_NAVE)/2
        pos_x = (ANCHO_NAVE)
        self.Nave = Nave(pos_x, pos_y)

        pygame.font.init()

    def bucle_principal(self):
        x = 0
        y = 0
        salir = False
        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        salir = True

            estado_teclado = pygame.key.get_pressed()
            if estado_teclado[pygame.K_a]:
                self.Nave.muevete(Nave.ARRIBA)

            if estado_teclado[pygame.K_z]:
                self.Nave.muevete(Nave.ABAJO)

            # AÑADIR AQUI LA IMAGEN DE NAVE

            # self.pantalla.fill((12, 0, 0))  # AÑADIR AQUI LA IMAGEN DE FONDO

            x_relativa = x % self.fondo.get_rect().width
            self.pantalla.blit(
                self.fondo, (x_relativa - self.fondo.get_rect().width, 0))
            if x_relativa < ANCHO:
                self.pantalla.blit(self.fondo, (x_relativa, 0))

            x -= 2

            self.pantalla.blit(self.nave_imagen, (x, y))

            self.Nave.pintame(self.pantalla)
            pygame.display.flip()

            self.reloj.tick(FPS)


if __name__ == "__main__":
    juego = Navesteroides()
    juego.bucle_principal()
