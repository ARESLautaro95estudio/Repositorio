from constantes_gui import *
from gui_form import Form
from gui_button import Button
from gui_textbox import TextBox
from gui_progressbar import ProgressBar


class FormMenu_06(Form):

    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)

        self.niveles= Button(master=self,x=0,y=0,w=140,h=50,color_background=None,color_border=None,image_background="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Achievements.png", on_click = self.on_click_boton ,on_click_param="Level", text = " FOrmulario 6 " ,font="Castellar",font_size=25,font_color = RED)
        self.opciones = Button(master=self,x=0,y=60,w=140,h=50,color_background=None,color_border=None,image_background="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Achievements.png", on_click = self.on_click_boton ,on_click_param="Sonido", text = "FOrmulario 6 -" ,font="Castellar",font_size=25,font_color=BLUE)
        self.salir = Button(master=self,x=0,y=120,w=140,h=50,color_background=None,color_border=None,image_background="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Achievements.png", on_click = self.on_click_boton ,on_click_param="Start",text="FOrmulario 6 ",font="Castellar",font_size=25,font_color=RED)        
        
        self.txt1 = TextBox(master=self,x=200,y=50,w=240,h=50,color_background=None,color_border=None,image_background="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Leaderboard.png",text="SCORE",font="Castellar",font_size=30,font_color=BLUE)
        self.pb1 = ProgressBar(master=self,x=500,y=50,w=240,h=50,color_background=None,color_border=None,image_background="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Leaderboard.png",image_progress="C:/Users/Ares/Cursada Lab 1/Menu/Menu/Buttons/Achievements.png",value = 3, value_max=8)
        
        self.lista_widget = [self.niveles,self.opciones,self.salir,self.txt1,self.pb1]

    def on_click_boton(self, parametro):
        
        self.set_active(parametro)

    def update(self, lista_eventos):
        for aux_widget in self.lista_widget:
            aux_widget.update(lista_eventos)

    def draw(self): 
        super().draw()
        for aux_widget in self.lista_widget:  
            aux_widget.draw()