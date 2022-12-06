import pygame
from constantes import *
from constantes_gui import *
from auxiliarjoa import Auxiliar
from bullet import * 



class Player:
   
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_rate_ms,move_rate_ms,jump_height,vidas) -> None:

        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet("caracters/stink/walk.png",15,1,False,1,0.7)[:12]
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet("caracters/stink/walk.png",15,1,True,1,0.7)[:12]
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet("caracters/stink/idle.png",16,1,False,1,0.7)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet("caracters/stink/idle.png",16,1,True,1,0.7)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet("caracters/stink/jump33.png",33,1,False,1,0.7)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet("caracters/stink/jump33.png",33,1,True,1,0.7)
        
        self.frame = 0       
        self.puntos = 0
        self.move_x = 0
        self.move_y = 0
        self.speed_walk =  speed_walk       
        self.gravity = gravity
        self.jump_power = jump_power
        self.animation = self.stay_r
        self.direction = DIRECTION_R
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.is_jump = False
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido= 0
        self.frame_rate_ms = frame_rate_ms 
        self.tiempo_transcurrido_move = 0
        self.move_rate_ms = move_rate_ms
        self.y_start_jump = 0
        self.jump_height = jump_height
        self.shoot_done= False
        self.rect_ground_collition = pygame.Rect(self.rect.x + self.rect.w / 3, self.rect.y + self.rect.h - GROUND_RECT_H, self.rect.w / 3, GROUND_RECT_H)
        self.rect_pick_up_collition = pygame.Rect(self.rect.x+self.rect.w / 3 , self.rect.y , self.rect.w/3,100)#+ self.rect.h - GROUND_RECT_H,
        self.rect_gun = pygame.Rect(self.rect.x+60,self.rect.y+40,10,10)
        self.ammo = 1
        self.lista_balas = []
        self.vidas = vidas
        self.status_life = True
        self.puntos = 0
        self.coliciones_enemigas = 0
        self.contacto = 0
        self.col_techo = False
        self.colision_l= pygame.Rect(self.rect.x-3 , self.rect.y , self.rect.w/7,90)#+ self.rect.h - GROUND_RECT_H,
        self.colision_r= pygame.Rect(self.rect.x+45 , self.rect.y , self.rect.w/7,90)#+ self.rect.h - GROUND_RECT_H,
        self.lista_objetos = []
    def walk(self,direction):
        
        if(self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l)):
            self.frame = 0
            self.direction = direction
            if(direction == DIRECTION_R):
                
                self.move_x = self.speed_walk
                self.animation = self.walk_r

            else:

                self.move_x = -self.speed_walk
                self.animation = self.walk_l
        
    def jump(self,on_off = True):
          if not self.col_techo:
            if(on_off and self.is_jump == False):
                self.y_start_jump = self.rect.y
                if(self.direction == DIRECTION_R):
                    self.move_x = self.speed_walk
                    self.move_y = -self.jump_power
                    self.animation = self.jump_r
                else:
                    self.move_x = -self.speed_walk
                    self.move_y = -self.jump_power
                    self.animation = self.jump_l
                self.frame = 0
                self.is_jump = True
            if(on_off == False):
                self.is_jump = False
                self.stay()

    def stay(self):
        if(self.animation != self.stay_r and self.animation != self.stay_l):
            if(self.direction == DIRECTION_R):
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
    
    def shoot(self,lista_plataformas,lista_muros):
        self.lista_objetos = lista_plataformas+lista_muros
        if self.ammo >0 :

            self.lista_balas.append(Bala (self.rect_gun.x,self.rect_gun.y,self.direction,self.lista_objetos))

            self.ammo-= 1
       
    def reload(self):

        self.ammo = 1     
            
    def do_movement(self,delta_ms,lista_plataformas):

        self.tiempo_transcurrido_move += delta_ms
        if not self.col_techo:
            if(self.tiempo_transcurrido_move >= self.move_rate_ms):
                if(abs(self.y_start_jump)- abs(self.rect.y) > self.jump_height and self.is_jump):
                    self.move_y = 0
                self.tiempo_transcurrido_move = 0         
                self.add_x(self.move_x)
                self.add_y(self.move_y)
                if(self.is_on_platform(lista_plataformas) == False):
                    self.add_y(self.gravity)
                elif(self.is_jump): 
                    self.jump(False)
            
           
    def colition(self,lista_pos_x_y,delta_ms):
        '''
        recibe una lista de balas/enemigos y busca coliciones
        '''
        self.tiempo_transcurrido+=delta_ms   
        for enemigo in lista_pos_x_y:
            if self.rect.colliderect(enemigo.rect_weakpoint):               
                if self.tiempo_transcurrido >15000:
                    self.contacto = 1 
                    self.vidas -=1
                    self.coliciones_enemigas +=1
                    self.tiempo_transcurrido =0
        if self.vidas <1:
            self.status_life = False
            self.vidas=0

    def score(self,lista_loot):

       
        for loot in lista_loot:
            if not loot.live:
                self.puntos+= 25    
                lista_loot.remove(loot)   
        if self.puntos<1:
            self.puntos=0
        if self.coliciones_enemigas >0:
            self.puntos -=50
            self.coliciones_enemigas -=1
        
    def is_on_platform(self,lista_plataformas):

        retorno = False
        if(self.rect.y >= GROUND_LEVEL):     
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if(self.rect_ground_collition.colliderect(plataforma.rect_ground_collition)):
                    retorno = True
                    break   
        return retorno

    def detecta_muros(self,lista_muros,delta_ms):

        self.tiempo_transcurrido+=delta_ms
        for muro in lista_muros:
            if self.colision_r.colliderect(muro.rect):
                if self.tiempo_transcurrido > 300:
                    self.add_x(-15)
                    self.tiempo_transcurrido =0                  
            elif self.colision_l.colliderect(muro.rect):
                if self.tiempo_transcurrido > 300:
                    self.add_x(15)
                    self.tiempo_transcurrido=0
                          
    def detecta_techos(self,lista_techos,delta_ms):
        
        self.tiempo_transcurrido+=delta_ms
        for muro in lista_techos:
            if self.rect_pick_up_collition.colliderect(muro.rect):
                if muro.rect.y<49:
                    if self.tiempo_transcurrido > 200:
                        self.add_y(30) 
                        self.move_x =0          
                        self.tiempo_transcurrido =0
                        self.col_techo = True
                        self.is_jump = True
                        self.stay()                 
            else:
                self.col_techo = False   
                                    
    def add_x(self,delta_x):
        
        self.rect.x += delta_x
        self.rect_ground_collition.x += delta_x
        self.rect_pick_up_collition.x += delta_x
        self.rect_gun.x += delta_x
        self.colision_l.x += delta_x
        self.colision_r.x += delta_x

    def add_y(self,delta_y):

        self.rect.y += delta_y  
        self.rect_ground_collition.y += delta_y
        self.rect_pick_up_collition.y += delta_y
        self.rect_gun.y += delta_y
        self.colision_l.y += delta_y
        self.colision_r.y += delta_y

    def do_animation(self,delta_ms):
        self.tiempo_transcurrido_animation += delta_ms
        if(self.tiempo_transcurrido_animation >= self.frame_rate_ms):
            self.tiempo_transcurrido_animation = 0
            if(self.frame < len(self.animation) - 1):
                self.frame += 1 
            else: 
                self.frame = 0

    def update(self,delta_ms,lista_plataformas,lista_muros,lista_techos,lista_balas,lista_enemigos,lista_loot):
        self.tiempo_transcurrido += delta_ms
        if self.tiempo_transcurrido > self.frame_rate_ms:
            
            self.detecta_techos(lista_techos,delta_ms)
            self.do_movement(delta_ms,lista_plataformas)
            self.do_animation(delta_ms)
            self.detecta_muros(lista_muros,delta_ms)
            self.colition(lista_balas,delta_ms)
            self.colition(lista_enemigos,delta_ms)
            self.score(lista_loot)

                
    def draw(self,screen):
        if(DEBUG):
            # pygame.draw.rect(screen,RED,self.rect)
            # pygame.draw.rect(screen,GREEN,self.rect_ground_collition)
            #pygame.draw.rect(screen,RED,self.rect_pick_up_collition)
            #pygame.draw.rect(screen,RED,self.rect)

            # pygame.draw.rect(screen,BLUE,self.rect_gun)
            # pygame.draw.rect(screen,BLANCO,self.colision_r)
            # pygame.draw.rect(screen,NEGRO,self.colision_l)
            pass
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)

    def events(self,keys,lista_plataformas,lista_muros):

        if(keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_L)

        if(not keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]):
            self.walk(DIRECTION_R)

        if(not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()

        if(keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and not keys[pygame.K_SPACE]):
            self.stay()   

        if(keys[pygame.K_SPACE]):
            self.jump(True)
            
        if(keys[pygame.K_s]):     
            self.shoot(lista_plataformas,lista_muros)

        if(not keys[pygame.K_s]):
            self.reload()
       
           