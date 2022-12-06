import pygame
from pygame.locals import *
from gui_form import Form
from gui_button import Button
from constantes_gui import *
from constantes import *
from manager_nivel import *
from leer_json import Lector_json

class FormMenu_02(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)
        
        self.boton1 = Button(master=self,x=0,y=180,w=400,h=150,color_background=None,color_border=None, image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png",on_click = self.on_click_boton , on_click_param = "LEVEL_1" , text="Nivel 1",font="Castellar",font_size = 50 , font_color = RED)
        self.boton2 = Button(master=self,x=400,y=180,w=400,h=150,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton , on_click_param = "LEVEL_2" , text="Nivel 2",font="Castellar",font_size=  50 , font_color = RED)
        self.boton3 = Button(master=self,x=800,y=180,w=400,h=150,color_background=None,color_border=None, image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png",on_click = self.on_click_boton , on_click_param = "LEVEL_3" , text="Nivel 3",font="Castellar",font_size=  50 , font_color = RED)
        self.boton4 = Button(master=self,x=0,y=540,w=100,h=50,color_background=None,color_border=None, image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png",on_click = self.on_click_boton , on_click_param = "Menu" , text="back",font="Castellar",font_size=  25 , font_color = RED)        
        
        self.lista_widget = [self.boton1,self.boton2,self.boton3,self.boton4]

    def on_click_boton(self,parametro):
        self.set_active(parametro)
 
    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            if self.active:  
                aux_boton.draw()