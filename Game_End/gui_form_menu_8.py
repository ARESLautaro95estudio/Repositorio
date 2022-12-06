from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
import pygame 
import sys
class FormMenu_08(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)
        
        self.pausa = Button(master=self,x=0,y=0,w=90,h=40,color_background=None,color_border=None, on_click = self.on_click_boton ,on_click_param="Pausa",text="Pausa",font="Castellar",font_size=20,font_color=RED)    
        self.lista_widget = [self.pausa]
      
    def on_click_boton(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
        
    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:  
            aux_widget.draw()