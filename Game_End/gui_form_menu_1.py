import pygame
import sys
from pygame.locals import *
from constantes_gui import *
from gui_form import Form
from gui_button import Button

class FormMenu_01(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        self.niveles= Button(master=self,x=290,y=100,w=140,h=50,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param = "NIVELES", text = " Niveles " ,font="Castellar",font_size=25,font_color = BLUE)        
        self.opciones = Button(master=self,x=700,y=100,w=150,h=50,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param = "Sonido" , text = "OPCIONES" ,font="Castellar",font_size=25,font_color=BLUE)
        self.salir = Button(master=self,x=500,y=500,w=90,h=50,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton_0 ,on_click_param = "Start" ,text="SALIR ",font="Castellar",font_size=25,font_color=BLUE)        
     
        self.lista_widget = [self.niveles,self.opciones,self.salir]

    def on_click_boton(self, parametro):
        self.set_active(parametro)

    def on_click_boton_0(self,parametro):
        pygame.quit()
        sys.exit() 
        
    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:  
            aux_widget.draw()