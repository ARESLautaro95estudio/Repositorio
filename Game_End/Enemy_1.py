from msilib.schema import Class
import pygame
from constantes import *
from constantes_gui import *
from bullet import * 
from auxiliarjoa import *

class Enemy_1 :

    def __init__(self,x,y,speed_walk,speed_run,gravity,frame_rate_ms):

        self.stay = Auxiliar.getSurfaceFromSpriteSheet("inhabitants/aligator/idle15H,9V,135L.png",15,9)[:]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("inhabitants/aligator/walk,3H,6V,16L.png",3,6)[:11]
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("inhabitants/aligator/walk,3H,6V,16L.png",3,6,True)[:11]
        self.die = Auxiliar.getSurfaceFromSpriteSheet("mas_recursos/deserttileset/png/Objects/Skeleton.png",1,1)[1:1]
        self.appere = Auxiliar.getSurfaceFromSpriteSheet("inhabitants/aligator/appear,3H,9V,25L.png",3,9)[:25] 
        self.frame = 0
        self.animation = self.stay
        self.image = self.animation [self.frame]
        self.live = True
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  
        self.rect_weakpoint = pygame.Rect (self.rect.x+130,self.rect.y+90, 40, 50)    
        self.avanzar = False
        self.move_x = 8
        self.move_y = 0  
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run   
        self.gravity = gravity
        self.rect_ground_collition = pygame.Rect(self.rect.x+50,self.rect.y+150,self.rect.w/6,GROUND_RECT_H)
        self.frame_rate_ms = frame_rate_ms
        self.lista_balas = []
        self.ammo = 1
        self.rect_radar = pygame.Rect(self.rect.x+50,self.rect.y+120,400,10)
        self.rect_gun = pygame.Rect(self.rect.x+60,self.rect.y+120,10,10)
        self.direction = DIRECTION_R
        self.rango_inicial = x
        self.rango_patrol = 100
        self.distancia_patrullada=0
        self.lista_objetos=[]
        
    def draw(self,screen):

        if self.live:
            # pygame.draw.rect(screen,RED,self.rect_weakpoint)
            # pygame.draw.rect(screen,BLUE,self.rect_ground_collition)
            # pygame.draw.rect(screen,BLUE,self.rect_radar)
            # pygame.draw.rect(screen,RED,self.rect_gun)
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)
       
    def update(self,delta_ms,lista_plataformas,pos_x_y,screen,lista_eventos=0):
        
        self.tiempo_transcurrido = 0   
        if self.live==1: 
            self.tiempo_transcurrido += delta_ms
            if self.tiempo_transcurrido > self.frame_rate_ms:  
                if(self.frame < len(self.animation) - 1):
                    self.frame += 1               
                else: 
                    self.frame = 0             
            self.add_x(self.move_x)
            self.add_y(self.move_y)
            self.shoot(pos_x_y)              
            if(self.is_on_platform(lista_plataformas) == False):
                self.add_y(self.gravity)            
    def move(self):     
        if self.live == True:
            if self.avanzar:
                if self.rect.x < (self.rango_inicial+self.rango_patrol):
                   
                    self.animation = self.walk_r
                    self.move_x = 2
                    self.rect_radar = pygame.Rect(self.rect.x+140,self.rect.y+120,400,10)
                    self.rect_weakpoint = pygame.Rect (self.rect.x+160,self.rect.y+90,48,65)
                    self.rect_ground_collition = pygame.Rect(self.rect.x+150,self.rect.y+150,self.rect.w/6,GROUND_RECT_H)
                    self.rect_gun = pygame.Rect(self.rect.x+200,self.rect.y+120,10,10)
                else:
                    self.avanzar = False
            else:
                if self.rect.x > (self.rango_inicial-self.rango_patrol):
                                 
                    self.animation = self.walk_l
                    self.move_x = -2
                    self.rect_radar = pygame.Rect(self.rect.x-200,self.rect.y+120,400,10)
                    self.rect_weakpoint = pygame.Rect (self.rect.x+35,self.rect.y+90,48,65)
                    self.rect_gun = pygame.Rect(self.rect.x*1.3,self.rect.y+120,10,10)
                    self.rect_ground_collition = pygame.Rect(self.rect.x+80,self.rect.y+150,self.rect.w/6,GROUND_RECT_H)
                    
                else:
                    self.avanzar = True      

    def shoot(self,pos_x_y):

        if self.rect_radar.colliderect(pos_x_y):
            if self.ammo > 0 :         
                self.lista_balas.append(Bala (self.rect_gun.x,self.rect_gun.y,self.direction,self.lista_objetos))
                self.ammo -= 1        
        else:
            self.reload()  
        
    def reload(self):

        self.ammo = 1   
        
    def is_on_platform(self,lista_plataformas):
        self.lista_objetos +=lista_plataformas
        retorno = False
        if(self.rect.y >= 320):    
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno
        
    def colision(self,pos_x_y,screen=0):

        if self.rect_weakpoint.colliderect(pos_x_y):
            self.animation = self.die
            self.move_x = 0           
            self.live = False
            self.rect_weakpoint = pygame.Rect (50000,50000,48,65)
            
    def add_x(self,delta_x):

        self.rect.x += delta_x    
        self.rect_weakpoint.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_radar.x += delta_x
        self.rect_gun.x += delta_x

    def add_y(self,delta_y):

        self.rect.y += delta_y    
        self.rect_weakpoint.y += delta_y
        self.rect_ground_collition.y += delta_y
        self.rect_radar.y += delta_y
        self.rect_gun.y += delta_y
    
class Enemy_02(Enemy_1):
    def __init__(self, x, y, speed_walk, speed_run, gravity):
        self.live =True
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("Recursos/Enemies/BlueBird/Flying (32x32).png",15,6)[:]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("Recursos/Enemies/AngryPig/Run (36x30).png",12,1)[:11]
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("Recursos/Enemies/AngryPig/Run (36x30).png",12,1,True)[:11]
        self.die = Auxiliar.getSurfaceFromSpriteSheet("mas_recursos/deserttileset/png/Objects/Skeleton.png",1,1)[1:1]
        #self.rect_weakpoint = pygame.Rect (self.rect.x+135,self.rect.y+90,48,65)
        self.frame = 0
        self.animation = self.stay
        self.image = self.animation [self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  
        self.rect_weakpoint = pygame.Rect (self.rect.x,self.rect.y, self.rect.w, 7)    
        self.avanzar = False
        self.move_x = 8
        self.move_y = 0  
        self.speed_walk =  speed_walk
        self.speed_run =  speed_run   
        self.gravity = gravity
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + 20 , self.rect.w , GROUND_RECT_H)
        self.frame_rate_ms=20
        self.rect_radar=pygame.Rect(self.rect.x-ANCHO_VENTANA,self.rect.y,4000,10)
        self.rect_gun= pygame.Rect(self.rect.x+3,self.rect.y,22,22)
        self.ammo = 1
        self.direction = DIRECTION_R
        self.lista_balas= []
        self.rango_inicial = x
        self.rango_patrol = 40
        self.lista_objetos=[]
        
    def draw(self, screen):
          if self.live:
            #pygame.draw.rect(screen,RED,self.rect_weakpoint)
            # pygame.draw.rect(screen,BLUE,self.rect_ground_collition)
            # pygame.draw.rect(screen,BLUE,self.rect_radar)
            # pygame.draw.rect(screen,RED,self.rect_gun)
            # pygame.draw.rect(screen,BLANCO,self.rect)
            self.image = self.animation[self.frame]
            screen.blit(self.image,self.rect)

        #return super().draw(screen)
    def move(self):
        if self.live == True:
            if self.avanzar:
                if self.rect.x < (self.rango_inicial+self.rango_patrol):
                   
                    self.animation = self.walk_r
                    self.move_x = 3
                    self.rect_weakpoint = pygame.Rect (self.rect.x+3,self.rect.y,22,22)
                    self.direction = DIRECTION_R
                else:
                    self.avanzar = False
            else:
                if self.rect.x > (self.rango_inicial-self.rango_patrol):    
                            
                    self.animation = self.walk_l
                    self.move_x = -3
                    self.rect_weakpoint = pygame.Rect (self.rect.x+3,self.rect.y,22,22)
                    self.direction = DIRECTION_L
                    
                else:
                    self.avanzar = True  
    
    def update(self, delta_ms, lista_plataformas,pos_x_y,screen,lista_eventos=0):
        super().update(delta_ms, lista_plataformas,pos_x_y,screen)

    def is_on_platform(self,lista_plataformas):
        self.lista_objetos+=lista_plataformas
        retorno = False
        if(self.rect_ground_collition.y >= 440):    
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno
                 
    def colision(self, pos_x_y,screen=0):
        return super().colision(pos_x_y,screen=0)
    def add_y(self, delta_y):
        return super().add_y(delta_y)
    def add_x(self, delta_x):
        return super().add_x(delta_x)