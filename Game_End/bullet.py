from constantes import *
from auxiliarjoa import *
import pygame

class Bala():

    def __init__(self,x,y,direction,objetos):
        
        self.bullet_r = Auxiliar.getSurfaceFromSpriteSheet("Recursos\Items\Fruits\Apple.png",17,1)[:]
        self.bullet_l = Auxiliar.getSurfaceFromSpriteSheet("Recursos\Items\Fruits\Apple.png",17,1,True)[:]
        self.direction = direction
        self.frame = 0
        self.animation = self.bullet_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()  
        self.rect.x = x
        self.rect.y = y
        self.rect_weakpoint = self.rect 
        self.move_x = 15
        self.move_y = 0
        self.live = True
        self.coldown = 0 
        self.objetos = objetos
        
    def draw(self,screen):

        screen.blit(self.image,self.rect)

    def update(self):
        
        if self.coldown > 0:
            self.coldown -= 1
            self.movement()
            if self.direction == DIRECTION_R:
                self.animation = self.bullet_r
            else:
                self.animation =self.bullet_l
        self.colition()

    def movement(self):
        if self.live:   
            if self.direction == DIRECTION_R:
                self.add_x(self.move_x)
                self.add_y(self.move_y)
            else:
                self.add_x(-self.move_x)
                self.add_y(self.move_y)
        
    def add_x(self,delta_x):   
        self.rect.x += delta_x
       
    def add_y(self,delta_y):
        self.rect.y += delta_y  
    
    def colition(self):
        for objeto in self.objetos:
            if self.rect_weakpoint.colliderect(objeto.rect):
                self.live = False

class manager_bullet():

    def __init__(self,player,screen,lista_enemy,delta_ms):
        self.player= player
        self.lista_enemigos = lista_enemy
        self.screen = screen
        self.delta_ms=delta_ms
        
    def  disparos_player(self):
        
        for balas in self.player_1.lista_balas:
            if balas.live :
                balas.draw(self.screen)
                balas.movement() 
                balas.update()
                self.buscar_enemigo(balas)
    
    def disparos_enemigos(self):
              
        for enemigo in self.lista_enemigos:
            for tiros in enemigo.lista_balas:
                if tiros.live :
                    tiros.draw(self.screen)
                    tiros.movement() 
                    tiros.update()
                    self.player_1.colition(tiros.rect,self.delta_ms) 
    
    def buscar_enemigos(self,balas):

        for enemy in self.lista_enemigos:
            enemy.colision(balas.rect)
           
