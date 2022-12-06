from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
import pygame 
from gui_widget import Widget
class FormMenu_04(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        #self.niveles= Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Achievements.png", on_click = self.on_click_boton1 ,on_click_param="Level", text = " Sonido " ,font="Stencil",font_size=25,font_color = RED)
        self.on = Button(master = self, x=353,y=210,w=140,h=50, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_sound , on_click_param = None, text = "ON" ,font="Castellar",font_size=25,font_color=RED)
        self.off = Button(master = self, x=740,y=210,w=140,h=50, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.off_sound , on_click_param = None , text = "OFF " ,font="Castellar",font_size=25,font_color=RED)        
        self.back_option = Button(master = self,x=0,y=540,w=100,h=50, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param="Pausa",text="BACK ",font="Castellar",font_size=25,font_color=RED)        
        self.puntaje =Button(master = self,x=500,y=50,w=240,h=70, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param="High score",text="Puntaje ",font="Castellar",font_size=30,font_color=RED)  
        self.soudn_text = Widget(master_form = self, x=500,y=130,w=240,h=50, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png",text="SONIDO",font="Castellar",font_size=30,font_color=RED)
        
        #self.reanudar =  Button(master = self,x=495,y=145,w=150,h=50, color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton_2 ,on_click_param=None,text="Reanudar ",font="Castellar",font_size=18,font_color=BLUE)     
        #self.pb1 = ProgressBar(master=self,x=200,y=20,w=240,h=50,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png",image_progress="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Achievements.png",value = 3, value_max=8)
        #self.niveles,self.soudn_text,self.pb1
        self.lista_widget = [self.back_option,self.on,self.off,self.soudn_text,self.puntaje]

    def on_click_boton(self, parametro): 
          
        self.set_active(parametro)

    def off_sound(self,parametro):

        pygame.mixer.music.set_volume(0.0)

    def on_sound(self,parametro):
        sonido_fondo = pygame.mixer.music.load("bg.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(110.0)
        
    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:  
            aux_widget.draw()
