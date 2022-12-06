from pygame.locals import *
from constantes_gui import *
from gui_form_menu_1 import FormMenu_01
from gui_form_menu_2 import FormMenu_02
from gui_form_menu_0 import Form_menu_0
from gui_form_menu_3 import FormMenu_03
from gui_form_menu_4 import FormMenu_04
from gui_form_menu_5 import FormMenu_05
from gui_form_menu_6 import FormMenu_06
from gui_form_menu_7 import FormMenu_07
from gui_form_menu_8 import FormMenu_08
from gui_form_menu_9 import FormMenu_09
from leer_json import Lector_json
from manager_nivel import Stage
from gui_form_menu_10 import FormMenu_10

class Manager_do_formularios:
   
    def __init__(self,screen):
        
        self.screen = screen
        self.lvl_config= {}
        self.data_lvl_one = {}
        self.lvl_select = False
        self.lvl =0
        self.iniciador_de_formularios()

    def iniciador_de_formularios(self):
        
        self.start = Form_menu_0("Start", self.screen, 0, 0, ANCHO_VENTANA, ALTO_VENTANA, None, None,image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg", active=True)       
        self.menu = FormMenu_01 ("Menu",  self.screen , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False )              
        self.level_opcion = FormMenu_02 ("NIVELES", self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)       
        self.sonido = FormMenu_04 ("Sonido", self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)       
        self.high_score = FormMenu_03 ("High score", self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(GREEN_PERS),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)
        self.salir = FormMenu_06 ("Salir", self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)
        self.nivel_uno = FormMenu_07("LEVEL_1",self.screen,x=ANCHO_VENTANA/2,y=0,w=90,h=40,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)     
        self.nivel_dos = FormMenu_08("LEVEL_2",self.screen,x=ANCHO_VENTANA/2,y=0,w=90,h=40,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)                   
        self.nivel_tres = FormMenu_09("LEVEL_3",self.screen,x=ANCHO_VENTANA/2,y=0,w=90,h=40,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)     
        self.pausa = FormMenu_05 ("Pausa", self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False,is_pause=self.nivel_uno.set_pausa)    
        self.form_make=False
        self.form_make_highscore=False
        

    def formulario_end_game(self,lvl_actual):   

        self.end_lvl = FormMenu_10("FIN",self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(None),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False,puntos=self.puntaje_player(),lvl_actual=lvl_actual)

    def formulario_highscore(self):
        self.high_score = FormMenu_03 ("High score", self.menu.master_surface , 0, 0, ANCHO_VENTANA, ALTO_VENTANA,color_background=(GREEN_PERS),color_border=(None),image_background_form="C:/Users/Ares/Cursada Lab 1/Mundo.jpg",active=False)

    def puntaje_player(self):

        if self.lvl != 0:        
            return self.lvl.player.puntos
        else:
            return 0
            
    def lvl_maker(self,screen):
        self.form_make = False
        self.end_lvl = 0
        self.lvl_select= self.lvl_config
        self.lvl = Stage(self.lvl_select,screen)

    def call_json(self,parametro):

        json_full = Lector_json((r"C:\Users\Ares\Cursada Lab 1\Game_End\datas.json"))
        self.data_lvl_one = json_full.importar_json()
        self.lvl_config = self.data_lvl_one[parametro]
        return self.lvl_config

    def crea_lvl_uno(self,screen):

            self.call_json("nivel_uno")
            self.lvl_maker(screen)
            self.lvl_config.clear()
            self.data_lvl_one.clear()

    def crea_lvl_dos(self,screen):

            self.call_json("nivel_dos")
            self.lvl_maker(screen)
            self.lvl_config.clear()
            self.data_lvl_one.clear()

    def crea_lvl_tres(self,screen):

            self.call_json("nivel_tres")
            self.lvl_maker(screen)
            self.lvl_config.clear()
            self.data_lvl_one.clear()
           
    def update(self,screen,delta_ms,keys,lista_eventos,objetivos=0):
        
        self.update_menu(lista_eventos)
        self.update_lvl_opcion(lista_eventos)
        self.update_start(lista_eventos)
        self.update_highscore(lista_eventos)
        self.update_sonido(lista_eventos)
        self.update_pausa(lista_eventos)
        self.update_salir(lista_eventos)
        self.update_nivel_uno(screen,delta_ms,keys,lista_eventos,objetivos)
        self.update_nivel_dos(screen,delta_ms,keys,lista_eventos,objetivos)
        self.update_nivel_tres(screen,delta_ms,keys,lista_eventos,objetivos)
       
    def update_nivel_uno(self,screen,delta_ms,keys,lista_eventos,objetivos):

        if (self.nivel_uno.active):
            if self.lvl_select == False:
                self.crea_lvl_uno(screen)
                self.lvl_select = True
            if (self.lvl.estado_juego(screen)==False):
                    if not (self.form_make):
                        self.formulario_end_game("Nivel uno")
                        self.form_make=True                                                                    
                    self.end_lvl.update(lista_eventos)
                    self.end_lvl.draw()                  
            else:               
                self.puntaje_player()       
                self.lvl.update(screen,delta_ms,keys,objetivos,lista_eventos)
                self.nivel_uno.update(lista_eventos)
                self.nivel_uno.draw()

    def update_nivel_dos(self,screen,delta_ms,keys,lista_eventos,objetivos):
        
        if self.nivel_dos.active:    
            if self.lvl_select==False:
                self.crea_lvl_dos(screen)
                self.lvl_select=True                  
            if  (self.lvl.estado_juego(screen)==False): 
                if not (self.form_make):
                    self.formulario_end_game("Nivel dos")
                    self.form_make=True
                                                                         
                self.end_lvl.update(lista_eventos)
                self.end_lvl.draw()
            else:
                self.puntaje_player()                 
                self.lvl.update(screen,delta_ms,keys,objetivos,lista_eventos)
                self.nivel_dos.update(lista_eventos)
                self.nivel_dos.draw()
    
    def update_nivel_tres(self,screen,delta_ms,keys,lista_eventos,objetivos):

        if self.nivel_tres.active:          
            if self.lvl_select==False:
                self.crea_lvl_tres(screen)
                self.lvl_select=True

            if  (self.lvl.estado_juego(screen)==False):
                if not (self.form_make):
                    self.formulario_end_game("Nivel tres")
                    self.form_make=True
                                                                     
                self.end_lvl.update(lista_eventos)
                self.end_lvl.draw()                  
            else:
                self.puntaje_player()                
                self.lvl.update(screen,delta_ms,keys,objetivos,lista_eventos)
                self.nivel_tres.update(lista_eventos,True)
                self.nivel_tres.draw()

    def update_menu(self,lista_eventos):
        if(self.menu.active):                   
            self.menu.update(lista_eventos)
            self.menu.draw()
            self.lvl = 0
            self.lvl_select=False
    
    def update_lvl_opcion(self,lista_eventos):

        if(self.level_opcion.active):  
            self.level_opcion.update(lista_eventos)
            self.level_opcion.draw() 

    def update_start(self,lista_eventos):

        if(self.start.active):
            self.start.update(lista_eventos)
            self.start.draw()

    def update_highscore(self,lista_eventos):

        if(self.high_score.active):
            self.high_score.update(lista_eventos)
            self.high_score.draw()
            
    def update_sonido(self,lista_eventos):
        
        if(self.sonido.active):
            if self.form_make_highscore == False:
                self.formulario_highscore()
                self.form_make_highscore=True           
            self.sonido.update(lista_eventos)
            self.sonido.draw()
        else:
            self.form_make_highscore=False

    def update_pausa(self,lista_eventos):

        if(self.pausa.active):
            self.pausa.update(lista_eventos)
            self.pausa.draw() 

    def update_salir(self,lista_eventos):

        if(self.salir.active):
            self.salir.update(lista_eventos)
            self.salir.draw()  

