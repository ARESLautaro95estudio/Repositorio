from Enemy_1 import *
from player import * 
import sys
import pygame
from constantes import *
from auxiliarjoa import Auxiliar

class Platform:
    
    def __init__(self,x,y,w,h,type=0):
        
        self.image = Auxiliar.getSurfaceFromSpriteSheet("tile/sheet1.png",8,8)[1]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, GROUND_RECT_H)
        

    def draw(self,screen):
        '''Muestra el rectangulo donde colisiona para manterse arriba del bloque'''
        if(DEBUG):
            pass
            #pygame.draw.rect(screen,RED,self.rect)
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pass
    #pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
class Bush_1:
    def __init__(self,x,y):
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("mas_recursos/deserttileset/png/Objects/Bush (1).png",1,1)[:]
        self.frame=0
        self.animation=self.stay
        self.image= self.animation[self.frame]
        self.rect=self.image.get_rect()
        self.position = (x,y)
        self.live= True
    def draw(self,screen,):
        self.image = self.animation[self.frame]
      
        screen.blit(self.image,self.position)
    def colision(self,pos_x_y):
        pass

class Bush_2:
    def __init__(self,x,y):
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("mas_recursos/deserttileset/png/Objects/Tree.png",1,1)[:]
        self.frame=0
        self.animation=self.stay
        self.image= self.animation[self.frame]
        self.rect=self.image.get_rect()
        self.position = (x,y)

    def draw(self,screen,):
        self.image = self.animation[self.frame]
      
        screen.blit(self.image,self.position)

class Skull:
    def __init__(self,x,y):
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("mas_recursos/deserttileset/png/Objects/Skeleton.png",1,1)[:]
        self.frame=0
        self.animation=self.stay
        self.image= self.animation[self.frame]
        self.rect=self.image.get_rect()
        self.position = (x,y)
        self.live= True
        rect_ground_collition = False
        
    def draw(self,screen,):

        self.image = self.animation[self.frame]
        screen.blit(self.image,self.position)
    
    def colision(self,pos_x_y):
        pass

class Portal:

    def __init__(self,x,y,misiones):

        self.closed = Auxiliar.getSurfaceFromSpriteSheet("assets/portal/portal__x1_closed_png_1354837277.png",10,3)[:29]
        self.closing=Auxiliar.getSurfaceFromSpriteSheet("assets/portal/portal__x1_closing_png_1354837282.png",6,3)[:11]
        self.open= Auxiliar.getSurfaceFromSpriteSheet("assets/portal/portal__x1_open_png_1354837280.png",10,3)[:]
        self.opening = Auxiliar.getSurfaceFromSpriteSheet("assets/portal/portal__x1_opening_png_1354837278.png",10,1)[:]
        self.frame=0
        self.animation=self.closed
        self.image= self.animation[self.frame]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.rect_colition = (self.rect.x+25,self.rect.y+25,40,40)
        self.misiones = misiones
        self.tiempo_transcurrido=0
        self.habilitado = False
        
    def draw(self,screen,):
        
        self.image = self.animation[self.frame]     
        screen.blit(self.image,self.rect)
    
    def animations(self):

        if(self.frame < len(self.animation)-1):
            self.frame += 1 
        else:
            self.frame = 0

    def update(self,kills,pos_x_y,delta_ms):
      
        tiempo_casteo= delta_ms * 3
        print("aca entra")
        if kills < self.misiones:
            self.animation = self.closed
        elif kills ==self.misiones:
            self.tiempo_transcurrido +=delta_ms
            if self.tiempo_transcurrido < 300:
               
                # self.frame = 0
                # self.animations()
                self.animation= self.opening
                self.habilitado=True              
            elif self.tiempo_transcurrido > tiempo_casteo:             
                if not self.rect.colliderect(pos_x_y):
                    self.animation = self.open
                    self.habilitado=True
                elif self.rect.colliderect(pos_x_y):
                    self.animation = self.closing
      
class Block_1:

    def __init__(self,x,y,w,h,type=0):

        self.image = Auxiliar.getSurfaceFromSpriteSheet("tile/sheet1.png",8,8)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition =  pygame.Rect(self.rect.x,self.rect.y,self.rect.w,GROUND_RECT_H)  
        self.live= True
        
    def draw(self,screen):     
        if(DEBUG):
            #pygame.draw.rect(screen,RED,self.rect)
            pass
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pass
            #pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
    def colision(self,pos_x_y):
        pass

class Techos:

    def __init__(self,x,y,w,h,type=0):

        self.image = Auxiliar.getSurfaceFromSpriteSheet("tile/sheet1.png",8,8)[type]
        self.image = pygame.transform.scale(self.image,(w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect_ground_collition =  self.rect   
        self.live= True

    def draw(self,screen):     
        if(DEBUG):
            #pygame.draw.rect(screen,RED,self.rect)
            pass
        screen.blit(self.image,self.rect)
        if(DEBUG):
            pass
            #pygame.draw.rect(screen,GREEN,self.rect_ground_collition)

    def colision(self,pos_x_y):
        pass

class Fruit:

    def __init__(self,x,y,w,h,type=0):

        self.stay = Auxiliar.getSurfaceFromSpriteSheet("mas_recursos/PIXEL ADVENTURE/PIXEL ADVENTURE/Recursos/Items/Fruits/Bananas.png",17,1)[:]
        self.desapere = Auxiliar.getSurfaceFromSpriteSheet("mas_recursos/PIXEL ADVENTURE/PIXEL ADVENTURE/Recursos/Items/Fruits/Collected.png",6,1)
        self.frame = 0
        self.animation=self.stay
        self.image = self.animation[self.frame]
        self.live = True
        self.rect = self.image.get_rect()      
        self.rect.x = x
        self.rect.y = y       
        self.rect_ground_collition= pygame.Rect(self.rect.x+5, self.rect.y+5, 15,15)
        self.lista = []

    def draw(self,screen):

        if self.live:    
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0 
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
        else:
            pass

    def colision(self,pos_x_y,fruta):    
        
        if self.rect.colliderect(pos_x_y):
            self.lista.append(fruta)
            self.animation = self.desapere          
            self.live = False
