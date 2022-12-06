from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar
from gui_widget import Widget
import pygame
import sys
from sqlite_funciones import insertRow

class FormMenu_10(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active,puntos,lvl_actual):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)
        
        self.puntos = puntos
        self.lvl_actual = lvl_actual

        self.lvl = Button(master=self,x=550,y=200,w=140,h=40,color_background = None ,color_border = None, on_click = self.on_click_boton ,on_click_param="Menu",text="menu principal",font="Cooper",font_size=30,font_color=BLUE)          
        

        if self.lvl_actual == "Nivel uno":
            proximo_nivel = "LEVEL_2"
        elif self.lvl_actual=="Nivel dos":
            proximo_nivel = "LEVEL_3"
        elif self.lvl_actual=="Nivel tres":
            proximo_nivel ="Menu"
            
        self.next_lvl = Button(master=self,x=550,y=320,w=100,h=50,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param = "NIVELES" ,text="Next level ",font="Castellar",font_size=25,font_color=BLUE)            
        
        self.salir = Button(master=self,x=550,y=260,w=100,h=50,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton_0 ,on_click_param = "Start" ,text="SALIR ",font="Castellar",font_size=25,font_color=BLUE)  
        self.score = Widget(master_form=self,x=550,y=100,w=100,h=50,color_background = None ,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic_Border\Bars\Bar_Background03.png",text="{0}".format(self.puntos),font="Castellar",font_size=30,font_color=NEGRO)
        self.load_name = TextBox(master=self,x=500,y=45,w=200,h=50,color_background = None ,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic_Border\Bars\Bar_Background03.png",text ="Name",font="Castellar",font_size=21,font_color=NEGRO,on_click=None,on_click_param=None)
        self.guardar = Button(master=self,x=650,y=100,w=75,h=25,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.guardar_puntaje_nombre ,on_click_param = None,text="Guardar ",font="Castellar",font_size=12,font_color=BLUE)
        #self.iniciar_next_lvl()
       
        self.lista_widget = [self.lvl,self.salir,self.score,self.load_name,self.next_lvl,self.guardar]
    
    def iniciar_next_lvl(self):

        if self.lvl_actual == "Nivel uno":
            proximo_nivel = "LEVEL_2"
        elif self.lvl_actual=="Nivel dos":
            proximo_nivel = "LEVEL_3"
        elif self.lvl_actual=="Nivel tres":
            proximo_nivel ="Menu"
        
        self.next_lvl = Button(master=self,x=550,y=320,w=100,h=50,color_background=None,color_border=None,image_background=r"C:\Users\Ares\Cursada Lab 1\set_gui_01\Comic\Elements\Element23s.png", on_click = self.on_click_boton ,on_click_param = proximo_nivel ,text="Next level ",font="Castellar",font_size=25,font_color=BLUE)
        

    def on_click_boton_0(self,parametro):

        pygame.quit()
        sys.exit() 

    def on_click_boton(self, parametro):

        print(parametro)
        self.set_active(parametro)

    def guardar_puntaje_nombre(self,parametro):

        insertRow(self.load_name._text,self.puntos,self.lvl_actual)
            
    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)
   
    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:  
            aux_widget.draw()
