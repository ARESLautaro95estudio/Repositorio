import pygame
import sys
from constantes import *
from pygame.locals import *  
from manager_gui import Manager_do_formularios
screen = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
pygame.mixer.init()
sonido_fondo = pygame.mixer.music.load("bg.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)
pygame.init()
clock = pygame.time.Clock()
imagen_fondo = pygame.image.load("forest/all.png").convert_alpha()
imagen_fondo = pygame.transform.scale(imagen_fondo,(ANCHO_VENTANA,ALTO_VENTANA))
game = Manager_do_formularios(screen)

while True:
    keys = pygame.key.get_pressed()
    lista_eventos = pygame.event.get()
    for event in pygame.event.get():                                                                            
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit() 
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    game.update(screen,delta_ms,keys,lista_eventos)
    pygame.display.flip()
    