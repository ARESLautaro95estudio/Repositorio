import pygame
from pygame.locals import *
from gui_widget import Widget
from gui_button import Button
from constantes_gui import *

class Form():
    forms_dict = {}

    def __init__(self ,name ,master_surface, x, y, w, h, color_background, color_border,image_background_form, active = False ):
                
        self.forms_dict[name] = self
        self.master_surface = master_surface
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color_background = color_background
        self.color_border = color_border
                                          
        self.surface = pygame.Surface((w,h))
        self.slave_rect = self.surface.get_rect()
        self.slave_rect.x = x
        self.slave_rect.y = y
        self.active = active
        # self.image_background_form = pygame.image.load(image_background_form)
        # self.image_background_form_2 = pygame.transform.scale(self.image_background_form,(ANCHO_VENTANA,ALTO_VENTANA))
        self.x = x
        self.y = y

        if(image_background_form != None):
            self.image_background_form = pygame.image.load(image_background_form)
            self.image_background_form_2 = pygame.transform.scale(self.image_background_form,(self.w,self.h))  
            self.render()
        else:
            #self.image_background_form= master_surface
            self.render()
                   
    def set_active(self, name):

        for aux_form in self.forms_dict.values():
            aux_form.active = False
        self.forms_dict[name].active = True

    def render(self):

        if self.image_background_form_2 != None:
            self.surface.blit(self.image_background_form_2,(0,0))

    def update(self,lista_eventos):
        pass

    def draw(self):
         
        self.master_surface.blit(self.surface,self.slave_rect)
        self.render()


class FormMenu(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        self.boton1 = Button(master=self,x=100,y=50,w=800,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="1234",text="MENU",font="Verdana",font_size=30,font_color=(0,255,0))
        self.boton2 = Button(master=self,x=200,y=50,w=200,h=50,color_background=(255,0,0),color_border=(255,0,255),on_click=self.on_click_boton1,on_click_param="8",text="MENU 2",font="Verdana",font_size=30,font_color=(0,255,0))
        self.lista_widget = [self.boton1,self.boton2]

    def on_click_boton1(self, parametro):
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_boton in self.lista_widget:
            aux_boton.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_boton in self.lista_widget:    
            aux_boton.draw()