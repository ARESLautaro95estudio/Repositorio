from manager_terreno import Terreno
from manager_materiales import Materiales
from manager_bullet import Manager_Bala
from player import Player
from Enemy_1 import Enemy_02
from Enemy_1 import Enemy_1
import pygame
from constantes import *
import random
from enemigo_03 import Enemigo_03

class Stage:

    def __init__(self,json_data,screen):

        self.json = json_data
        self.screen = screen        
        self.misiones = 0      
        self.terreno = []            
        self.materiales = []              
        self.enemigos = []
        self.enemigo_static = []            
        self.scenario= []           
        self.portales = []           
        self.bala= 0
        self.iniciador()
        self.json.clear()

    def iniciador(self):
     
        self.armado_de_terreno()
        self.objetivos()
        self.player = self.armado_de_personaje()
        self.armado_de_enemigos()
        self.armado_de_materiales()
        self.armado_de_balas()
        self.el_unificador()
        
    def armado_de_terreno(self):
        '''
        Llama a objeto Terreno creando una lista estos objetos tienen metodo(draw/update/colicion)
        Incluye(Muros/plataformas/Techos)
        '''
        self.terreno = Terreno(self.json["plataformas"],self.json["Muros"],self.json["Techos"],self.screen)

    def armado_de_materiales(self):
        '''
        Llama a objeto Materiales creando una lista estos objetos tienen metodo(draw/update/colicion)
        Incluye(Fruits/Portal)
        ''' 
        loot_config = self.json["loot"]
        portal_x = self.json["portal"]["pos_x"]
        portal_y = self.json["portal"]["pos_y"]
        self.materiales = Materiales(loot_config,portal_x,portal_y, self.misiones)
        loot_config.clear()
        
    def objetivos(self):

        for enemigos_eliminados in self.enemigos:
            if enemigos_eliminados.live == False:
                pass
           
    def update(self,screen,delta_ms,keys,objetivos,lista_eventos):
        '''
        Recibe el screen , delta(tiempo),teclas(get_presed) desde el main
        Mantiene actualizado el objeto llamando a los metodos de los objetos involucrados.
        Ejecuta el metodo .draw y busca coliciones.
        '''    
        self.bala.update(delta_ms,screen)  
        self.update_player(screen,keys,delta_ms)    
        self.update_materiales(screen)
        self.update_scenario(screen)  
        self.hud(screen)
        self.estado_juego(screen)
        self.update_enemy(delta_ms,screen,lista_eventos)
        #self.materiales.portal.update()

    def update_enemy_Static(self,delta_ms,screen):
        
        for enemy in self.enemigo_static:
            enemy.update(delta_ms,self.terreno.plataformas_lista,self.player.rect)
            enemy.draw()

    def update_materiales(self,screen):
        for fruta in self.materiales.lista_loot:
            fruta.draw(screen)
            fruta.colision(self.player.rect_pick_up_collition,fruta)

    def update_scenario(self,screen):
        
        for things in self.scenario:
            things.draw(screen)

    def update_player(self,screen,keys,delta_ms):
        self.player.draw(screen)      
        self.player.events(keys,self.terreno.plataformas_lista,self.terreno.muros_lista )
        self.player.update(delta_ms , self.terreno.plataformas_lista , self.terreno.muros_lista , self.terreno.techos_lista ,self.enemigos,self.enemigos,self.materiales.lista_loot)
    
    def update_enemy(self,delta_ms,screen,lista_eventos):
        for enemy in self.enemigos:
            enemy.draw(screen)  
            enemy.update(delta_ms,self.terreno.plataformas_lista,self.player.rect,screen,lista_eventos)   
            enemy.move()
            if enemy.live == False:
                self.player.puntos+= 100
                self.misiones -=1
                self.enemigos.remove(enemy)

    def el_unificador(self):
        '''
        Unifica todos los objetos en una sola lista para iterarla con .draw(screen)
        '''
        self.scenario+=self.terreno.plataformas_lista
        self.scenario+=self.terreno.techos_lista
        self.scenario+=self.terreno.muros_lista
        self.scenario+= self.materiales.lista_portal
        self.scenario+= self.enemigo_static
            
    def armado_de_balas (self):
        '''
        Unifica objetos materiales,terrenos,enemigos y personaje
        (SUMA LISTAS Y LA DUPLICO UNA PARA DIBUJAR Y OTRA PARA RASTREAR COORDENADAS)
        '''
        self.bala = Manager_Bala(self.player,self.enemigos)

    def armado_de_personaje(self):
        x=self.json["Player"]["pos_x"]
        y=self.json["Player"]["pos_y"]

        return Player(x,y,speed_walk=6,gravity=8,jump_power=25,frame_rate_ms=40,move_rate_ms=10,jump_height=140,vidas=3)
        
    def armado_de_enemigos(self):

        cantidad=self.json["Enemigo"]["lagarto"]["cantidad"] 

        self.misiones = cantidad + self.json["Enemigo"]["pork"]["cantidad"]  +self.json["Enemigo"]["Hongo"]["cantidad"]  
        x=1
        pos_X =self.json["Enemigo"]["lagarto"]["pos_x"]
        loc =pos_X+100
        for crear in range(cantidad):
            if x < ANCHO_VENTANA-loc:
                    self.enemigos.append(Enemy_1 ( pos_X+x,self.json["Enemigo"]["pork"]["pos_y"],9,10,12,40))
                    s = random.sample(range(40,800),1)
                    x=s[0]        
        x=1
        pos_X =self.json["Enemigo"]["pork"]["pos_x"]
        loc =pos_X+100
        for crear in range(self.json["Enemigo"]["pork"]["cantidad"]):
            if x < ANCHO_VENTANA-loc and x >0:
                self.enemigos.append(Enemy_02 (pos_X+x,self.json["Enemigo"]["pork"]["pos_y"],12,12,40))
                x+=180
            else:         
                s = random.sample(range(40,800),1)
                x=s[0]

        pos_X =self.json["Enemigo"]["Hongo"]["pos_x"] 
        loc =pos_X+100
        x=1       
        for crear in range(self.json["Enemigo"]["Hongo"]["cantidad"]):
            if x < ANCHO_VENTANA-loc:
                self.enemigos.append(Enemigo_03 (pos_X+x ,self.json["Enemigo"]["Hongo"]["pos_y"] ,12 ,12 ,13 ,40, self.json["Enemigo"]["Hongo"]["lista_preguntas"]))
                s = random.sample(range(50,800),1)
                x=s[0]
            else:         
                s = random.sample(range(40,800),1)
                x=s[0]
       
    def estado_juego(self,screen):
        
        if self.misiones==0:
            self.materiales.portal.open       
            if self.player.rect_pick_up_collition.colliderect(self.materiales.portal.rect_colition):
                return False               
        if not(self.player.status_life):
            return False
                     
    def hud(self,screen):
        '''LLeva la cuenta '''     
        lifecont = pygame.font.Font(None,50)
        score = pygame.font.Font(None,50)
        life = lifecont.render("Vidas: {0}".format(self.player.vidas),0,(GREEN))
        screen.blit(life,(1000,10))
        puntos = score.render("SCORE: {0}".format(self.player.puntos),0,(GREEN))
        screen.blit(puntos,(10,10))
