import pygame
import sys
from pygame.locals import *
from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_widget import Widget
from sqlite_funciones import readRows

class FormMenu_03(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        self.back =Button(master=self,x=0,y=40,w=140,h=50,color_background=None,color_border=None,image_background="set_gui_01/Comic_Border/Elements/Element03s.png", on_click = self.on_click_boton ,on_click_param="Sonido",text="Back ",font="Castellar",font_size=25,font_color=RED)   
             
        self.scores = self.show_highscore()
        self.iniciar_table()
        
        self.lista_widget = [self.puntos,self.back,self.Nivel_uno,self.Nivel_dos,self.Nivel_tres, self.top_1_nivel1 ,self.top_2_nivel1, self.top_3_nivel1,self.top_1_nivel2 ,self.top_2_nivel2, self.top_3_nivel2,self.top_1_nivel3 ,self.top_2_nivel3, self.top_3_nivel3, ]

    def iniciar_table(self):
        
        self.puntos = Widget (master_form=self,x=15,y=-200,w=self.w,h=500,color_background = None ,color_border= None,image_background=None, text = "HIGHSCORE TABLE"  ,font="Castellar",font_size=30,font_color=BLANCO)
        self.Nivel_uno = Widget (master_form=self,x=355,y=80,w=150,h=50,color_background = None ,color_border= None,image_background=None, text ="NIVEL 1"  ,font="Castellar",font_size=30,font_color=RED)
        self.Nivel_dos= Widget (master_form=self,x=580,y=80,w=150,h=50,color_background = None ,color_border= None,image_background=None, text ="NIVEL 2"  ,font="Castellar",font_size=30,font_color=BLUE)
        self.Nivel_tres= Widget (master_form=self,x=805,y=80,w=150,h=50,color_background = None ,color_border= None,image_background=None, text ="NIVEL 3"  ,font="Castellar",font_size=30,font_color=MARRON)   
                                                                                                                                 
        
        self.top_1_nivel1 = Widget (master_form=self,x=150,y=125,w=600,h=50,color_background = None ,color_border= None,image_background=None, text =("{0}: {1}").format(self.scores[0][2],self.scores[0][3]) ,font="Castellar",font_size=25,font_color=RED)
        self.top_2_nivel1 = Widget (master_form=self,x=150,y=200,w=600,h=50,color_background = None ,color_border= None,image_background=None, text =("{0}: {1}").format(self.scores[1][2],self.scores[1][3]) ,font="Castellar",font_size=25,font_color=RED)
        self.top_3_nivel1 = Widget (master_form=self,x=150,y=300,w=600,h=50,color_background = None ,color_border= None,image_background=None, text =("{0}: {1}").format(self.scores[2][2],self.scores[2][3]) ,font="Castellar",font_size=25,font_color=RED)
        
        self.top_1_nivel2 = Widget (master_form=self,x=370,y=125,w=600,h=50,color_background = None ,color_border= None,image_background=None, text =("{0}: {1}").format(self.scores[3][2],self.scores[3][3]) ,font="Castellar",font_size=25,font_color=BLUE)
        self.top_2_nivel2 = Widget (master_form=self,x=370,y=200,w=600,h=50,color_background = None ,color_border= None,image_background=None, text =("{0}: {1}").format(self.scores[4][2],self.scores[4][3]) ,font="Castellar",font_size=25,font_color=BLUE)
        self.top_3_nivel2 = Widget (master_form=self,x=370,y=300,w=600,h=50,color_background = None ,color_border= None,image_background=None, text =("{0}: {1}").format(self.scores[5][2],self.scores[5][3]) ,font="Castellar",font_size=25,font_color=BLUE)
        
        self.top_1_nivel3 = Widget (master_form=self,x=600,y=125,w=600,h=50,color_background = None ,color_border= None,image_background=None, text =("{0}: {1}").format(self.scores[6][2],self.scores[6][3]) ,font="Castellar",font_size=25,font_color=MARRON)
        self.top_2_nivel3 = Widget (master_form=self,x=600,y=200,w=600,h=50,color_background = None ,color_border= None,image_background=None, text =("{0}: {1}").format(self.scores[7][2],self.scores[7][3]) ,font="Castellar",font_size=25,font_color=MARRON)
        self.top_3_nivel3 = Widget (master_form=self,x=600,y=300,w=600,h=50,color_background = None ,color_border= None,image_background=None, text =("{0}: {1}").format(self.scores[8][2],self.scores[8][3]) ,font="Castellar",font_size=25,font_color=MARRON)
       
    def on_click_boton(self, parametro):
        self.set_active(parametro)
       
    def on_click_boton3(self, parametro):
        pygame.quit()
        sys.exit() 

    def show_highscore(self):

        top=self.highscor_top3()
        return top    

    def update(self, lista_eventos):

        self.score = self.show_highscore()
        self.puntos.update(lista_eventos)
        self.Nivel_uno.update(lista_eventos)
        self.Nivel_dos.update(lista_eventos)
        self.Nivel_tres.update(lista_eventos)
        self.back.update(lista_eventos)

        self.top_1_nivel1.update(lista_eventos,("{0}: {1}").format(self.scores[0][2],self.scores[0][3])) 
        self.top_2_nivel1.update(lista_eventos,("{0}: {1}").format(self.scores[1][2],self.scores[1][3])) 
        self.top_3_nivel1.update(lista_eventos,("{0}: {1}").format(self.scores[2][2],self.scores[2][3]))

        self.top_1_nivel2.update(lista_eventos,("{0}: {1}").format(self.scores[3][2],self.scores[3][3]))
        self.top_2_nivel2.update(lista_eventos,("{0}: {1}").format(self.scores[4][2],self.scores[4][3]))
        self.top_3_nivel2.update(lista_eventos,("{0}: {1}").format(self.scores[5][2],self.scores[5][3])) 

        self.top_1_nivel3.update(lista_eventos,("{0}: {1}").format(self.scores[6][2],self.scores[6][3]))
        self.top_2_nivel3.update(lista_eventos,("{0}: {1}").format(self.scores[7][2],self.scores[7][3])) 
        self.top_3_nivel3.update(lista_eventos,("{0}: {1}").format(self.scores[8][2],self.scores[8][3]))

        
    def draw(self): 

        super().draw()
        for aux_widget in self.lista_widget:  
            aux_widget.draw()
           
    def highscor_top3(self):

        top_3 = readRows("Nivel uno") + readRows("Nivel dos") + readRows("Nivel tres")

        return top_3

    