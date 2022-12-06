from Objetos_actual import *

class Terreno:

    '''
    Es un objeto que crea una lista de objetos que forman parte del escenario. (No inlcuye objetos que interactuen mas alla de una coision)
    '''

    def __init__(self,plataformas_config,muros_config,techo_config ,screen):
        
        '''
        Props recibidas de un json 
        '''       
        self.plataformas_config = plataformas_config 
        self.muros_config = muros_config 
        self.techo_config = techo_config
        self.screen = screen
        self.lista_terreno=[]
        self.muros_lista = []
        self.techos_lista = []
        self.plataformas_lista = []

        self.crea_muros()
        self.crea_techos()
        self.crea_plataforma()
        self.unificador()

    def unificador(self):
        self.lista_terreno=self.plataformas_lista+self.muros_lista+ self.techos_lista

    def crea_plataforma(self):
        '''
        Crea objetos con parametros recibidos de un json y los adiere a una lista final
        '''
        for i in range(self.plataformas_config["set_01"]["cantidad"]):         
            self.plataformas_lista.append(Block_1(self.plataformas_config["set_01"]["pos_x"][i], self.plataformas_config["set_01"]["pos_y"][i],40,50,5))

        for i in range(self.plataformas_config["set_02"]["cantidad"]):         
            self.plataformas_lista.append(Block_1(self.plataformas_config["set_02"]["pos_x"][i], self.plataformas_config["set_02"]["pos_y"][i],40,50,5))

        for i in range(self.plataformas_config["set_03"]["cantidad"]):         
            self.plataformas_lista.append(Block_1(self.plataformas_config["set_03"]["pos_x"][i], self.plataformas_config["set_03"]["pos_y"][i],40,50,5))

        for i in range(self.plataformas_config["set_04"]["cantidad"]):         
            self.plataformas_lista.append(Block_1(self.plataformas_config["set_04"]["pos_x"][i], self.plataformas_config["set_04"]["pos_y"][i],40,50,1))

        for i in range(self.plataformas_config["set_05"]["cantidad"]):         
            self.plataformas_lista.append(Block_1(self.plataformas_config["set_05"]["pos_x"][i], self.plataformas_config["set_05"]["pos_y"][i],40,50,1))

    
    def crea_muros(self):
        '''
        Crea objetos con parametros recibidos de un json y los adiere a una lista final
        '''
        for i in range(self.muros_config["set_01"]["cantidad"]):         
            self.muros_lista.append(Block_1(self.muros_config["set_01"]["pos_x"][i], self.muros_config["set_01"]["pos_y"][i],40,50,25))

        for i in range(self.muros_config["set_02"]["cantidad"]):         
            self.muros_lista.append(Block_1(self.muros_config["set_02"]["pos_x"][i], self.muros_config["set_02"]["pos_y"][i],40,50,25))

        for i in range(self.muros_config["set_03"]["cantidad"]):         
            self.muros_lista.append(Block_1(self.muros_config["set_03"]["pos_x"][i], self.muros_config["set_03"]["pos_y"][i],40,50,25))

        for i in range(self.muros_config["set_04"]["cantidad"]):         
            self.muros_lista.append(Block_1(self.muros_config["set_04"]["pos_x"][i], self.muros_config["set_04"]["pos_y"][i],40,50,25))

      

    def crea_techos(self):
        '''
        Crea objetos con parametros recibidos de un json y los adiere a una lista final
        '''
        for i in range(self.techo_config["set_01"]["cantidad"]):         
            self.techos_lista.append(Block_1(self.techo_config["set_01"]["pos_x"][i], self.techo_config["set_01"]["pos_y"][i],80,20,24))

        for i in range(self.techo_config["set_02"]["cantidad"]):         
            self.techos_lista.append(Block_1(self.techo_config["set_02"]["pos_x"][i], self.techo_config["set_02"]["pos_y"][i],40,20,24))

        for i in range(self.techo_config["set_03"]["cantidad"]):         
            self.techos_lista.append(Block_1(self.techo_config["set_03"]["pos_x"][i], self.techo_config["set_03"]["pos_y"][i],40,20,24))

        for i in range(self.techo_config["set_04"]["cantidad"]):         
            self.techos_lista.append(Block_1(self.techo_config["set_04"]["pos_x"][i], self.techo_config["set_04"]["pos_y"][i],40,20,24))

       

    def update(self):
        '''
        Llama a las funciones que crean objetos para obtener la lista final del objeto Terreno
        '''
        for terreno in self.lista_terreno:
            terreno.draw(self.screen)
