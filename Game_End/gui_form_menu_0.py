import pygame
from pygame.locals import *
from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar

class Form_menu_0(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        self.boton_start = Button (self,400,100,w=400,h=300,color_background=None,color_border=None, image_background = r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png" ,text="START",font="Castellar",font_size=70,font_color=RED,on_click=self.on_click,on_click_param = "Menu")
        self.lista_widget=[self.boton_start]

    def on_click(self,parametro):
        self.set_active(parametro)

    def update(self,lista_eventos):

        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self):
        super().draw()
        for aux_widget in self.lista_widget:  
            aux_widget.draw()