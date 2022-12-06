import pygame
from bullet import Bala

class Manager_Bala :

    def __init__(self,data_player,lista_enemigos):

        self.player = data_player
        self.enemy_list = lista_enemigos

    def update(self,delta_ms,screen):

        for balas in self.player.lista_balas:
            if balas.live :
                for enemigo in self.enemy_list:
                    enemigo.colision(balas.rect,screen)

        for enemigo in self.enemy_list:
            self.player.colition(enemigo.lista_balas,delta_ms)
        
        for balas in self.player.lista_balas:
            if balas.live :
                balas.draw(screen)
                balas.movement() 
                balas.update()

        for enemigo in self.enemy_list:
            for bala in enemigo.lista_balas:
                if bala.live:
                    bala.draw(screen)
                    bala.movement() 
                    bala.update()
       
    def draw(self,screen):
        pass
