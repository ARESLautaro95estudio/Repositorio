from msilib.schema import Class
import pygame
from constantes import *
from constantes_gui import *
from bullet import * 
from auxiliarjoa import *
from Enemy_1 import Enemy_1
from formulario_pelea import Quest
import random

class Enemigo_03(Enemy_1):

    def __init__(self,x,y,speed_walk,speed_run,gravity,frame_rate_ms,lista_preguntas):
        super().__init__(x,y,speed_walk,speed_run,gravity,frame_rate_ms)
        self.stay = Auxiliar.getSurfaceFromSpriteSheet("inhabitants/cooking_vendor/idle.png",21,17,True,1,0.7)[:]
        self.talk = Auxiliar.getSurfaceFromSpriteSheet("inhabitants/cooking_vendor/talk.png",5,8,True,1,0.7)[:34]
        self.frame = 0
        self.animation = self.stay
        self.image = self.animation [self.frame]
        self.live = True
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y  
        self.move_y = 0
        self.speed_run = speed_run
        self.speed_walk = speed_walk
        self.rect_weakpoint = pygame.Rect (self.rect.x+50,self.rect.y+40, self.rect.w/2,self.rect.h-40)   
        self.gravity = gravity
        self.rect_ground_collition = pygame.Rect(self.rect.x+50,self.rect.y+150,self.rect.w,GROUND_RECT_H)
        self.frame_rate_ms = frame_rate_ms
        self.lista_preguntas = lista_preguntas
        self.lista_balas = []
        self.question = False
        self.text_battle = False
        self.res = False
        
    def draw(self, screen):
       
        # pygame.draw.rect(screen,RED,self.rect_weakpoint)
        # pygame.draw.rect(screen,BLUE,self.rect_ground_collition)
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def pregunta(self,screen):

        s = random.choice(self.lista_preguntas)
        x=60
        y=60
        self.text_battle = Quest("Pregunta",screen,x,y,700,300,BLANCO,None,"dialogo.png",True,s)

    def move(hola):
        pass

    def update(self, delta_ms, lista_plataformas, pos_x_y,screen,lista_eventos):
     
        if not(self.question):
            self.colision(pos_x_y,screen)
        self.tiempo_transcurrido = 0     
        if self.live: 
            self.tiempo_transcurrido += delta_ms  
            if self.tiempo_transcurrido > 30:  
                if(self.frame < len(self.animation) - 1):               
                    self.frame += 1               
                else: 
                    self.frame = 0             
            self.add_y(self.move_y)             
            if(self.is_on_platform(lista_plataformas) == False):
                self.add_y(self.gravity)
        if self.question:
            self.text_battle.update_r(lista_eventos)
            self.text_battle.draw()
            self.res = self.text_battle.acierto
            if self.text_battle.acierto:
                self.live=False
                self.text_battle.active=False
         
    def is_on_platform(self, lista_plataformas):
        
        retorno = False
        if(self.rect.y >= 340):    
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno

    def colision(self, pos_x_y,screen):
        if not self.question:
            if self.rect_weakpoint.colliderect(pos_x_y):
                self.frame=0
                self.animation = self.talk
                self.question = True
                self.pregunta(screen)

    def add_y(self, delta_y):

        self.rect.y += delta_y   
        self.rect_weakpoint.y += delta_y       
        self.rect_ground_collition.y += delta_y