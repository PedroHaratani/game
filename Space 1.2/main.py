import pygame,sys,os
from random import randint,uniform
from classes import Nave,Meteoro,Score
pygame.init()

width,height = 1200,720

display_surface = pygame.display.set_mode((width,height))
pygame.display.set_caption("Jogo Nave")
FPS = pygame.time.Clock()

group_sprite = pygame.sprite.Group()

nave = Nave(group_sprite)
dt = FPS.tick(60) /1000.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dt = FPS.tick(60) /1000.0
    #display_surface.blit(bg1,(0,0))
    #group_sprite.update(dt,laser_)
    pygame.display.update()