from gui_button import Button
from constantes_gui import *
from constantes import *
from gui_form import FormMenu
from gui_textbox import TextBox
from gui_widget import Widget
import re
class Quest(FormMenu):
    
    def __init__(self,name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active,ask):
        super().__init__(name,master_surface,x,y,w,h,color_background,color_border,image_background_form,active)
        self.w=w
        self.respuesta = False
        self.ask = ask
        self.question = self.ask.keys()
        
        self.crea_answ()
        self.sanitizacion_datos()
    
        self.opcion_a = Button (master=self,x=80,y=120,w=50,h=75,color_background=None,color_border=None, image_background=r"set_gui_01\Comic\Elements\Element12.png",on_click = self.on_click_boton1 , on_click_param = self.respuesta_a , text="A",font="Castellar",font_size = 18 , font_color = NEGRO)
        self.opcion_b = Button(master=self,x=240,y=120,w=50,h=75,color_background=None,color_border=None, image_background=r"set_gui_01\Comic\Elements\Element12.png",on_click = self.on_click_boton1 , on_click_param = self.respuesta_b , text="B",font="Castellar",font_size = 18 , font_color = NEGRO)
        self.opcion_c =Button (master=self,x=380,y=120,w=50,h=75,color_background=None,color_border=None, image_background=r"set_gui_01\Comic\Elements\Element12.png",on_click = self.on_click_boton1 , on_click_param = self.respuesta_c , text="C",font="Castellar",font_size = 18 , font_color = NEGRO)
        
        self.surface.set_colorkey(NEGRO)   
        self.pregunta = Widget(master_form=self,x=15,y=0,w=self.w,h=75,color_background = None ,color_border= None,image_background=None, text = self.question ,font="Castellar",font_size=22,font_color=NEGRO)
        self.lista_widget = [self.pregunta,self.opcion_a,self.opcion_b,self.opcion_c]
        #self.soudn_text = TextBox(master = self, x=500,y=120,w=240,h=50, color_background=BLUE,color_border=None,image_background=None,text="SONIDO",font="Castellar",font_size=30,font_color=GREEN)
        self.acierto = False
        self.error = False
        
    
    def on_click_boton1(self, parametro):
        if parametro == 0:
            
            return self.error

        if  parametro ==1:
            self.acierto = True
            return self.acierto
        #super().on_click_boton1(parametro)
        self.set_active(parametro)


    def update_r(self, lista_eventos):
        for widget in self.lista_widget:
            widget.update(lista_eventos)

    def draw(self):
        super().draw()
        for widget in self.lista_widget:
            widget.draw()

    def sanitizacion_datos(self):
        llave_dict = str(self.question)
        string_sucio = re.split( "'",llave_dict)
        palabra=""
        for letra in string_sucio[1]:
            if letra == "/":
                letra = ("\n")
            palabra+=letra
        self.question = str(palabra)   
        return  self.question             
        # llave = self.question
        # llave_str = str( llave )
        # pregunta = re.split( "'",llave_str)
        # palabra=""
        # for letra in pregunta[1]:
        #     if letra == "/":       
        #         letra = ("\n")
        #     palabra+=letra    
        # self.question = palabra
       
    def crea_answ(self):
        answer = self.ask.values()
        # testeo = teste.values()
        # list(testeo)[0][0]

        self.respuesta_a=(list(answer)[0][0])
        self.respuesta_b=(list(answer)[0][1])
        self.respuesta_c=(list(answer)[0][2])
        answer = []
        