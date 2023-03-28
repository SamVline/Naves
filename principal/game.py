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

    def bucle_principal(self):
        salir = False
        while not salir:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        salir = True

            # estado_teclado = pygame.key.get_pressed()
            # if estado_teclado[pygame.K_a]:
               # self.Nave.muevete(Nave.ARRIBA)

            # if estado_teclado[pygame.K_z]:
               # self.jugador1.muevete(Jugador.ABAJO)

            self.pantalla.fill(255, 250, 0)

            pygame.display.flip()
            self.reloj.tick(FPS)


if __name__ == "__main__":
    juego = Navesteroides()
    juego.bucle_principal()
