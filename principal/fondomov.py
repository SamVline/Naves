import os
import pygame
from pygame.sprite import Sprite


class Fondo_():


screen = create_screen()
clock = pygame.time.Clock()  # get a pygame clock object
player = load_player_image()
background = load_background_image()
screen.blit(background, (0, 0))  # draw the background
position = player.get_rect()
screen.blit(player, position)  # draw the player
pygame.display.update()  # and show it all
for x in range(100):  # animate 100 frames
    screen.blit(background, position, position)  # erase
    position = position.move(2, 0)  # move player
    screen.blit(player, position)  # draw new player
    pygame.display.update()  # and show it all
    clock.tick(60)  # update 60 times per second


class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self):
        self.pos = self.pos.move(0, self.speed)
        if self.pos.right > 600:
            self.pos.left = 0


screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()  # get a pygame clock object
player = pygame.image.load('player.bmp').convert()
background = pygame.image.load('background.bmp').convert()
screen.blit(background, (0, 0))
objects = []
for x in range(10):  # create 10 objects</i>
    o = GameObject(player, x*40, x)
    objects.append(o)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)
