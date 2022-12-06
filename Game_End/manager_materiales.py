from Objetos_actual import Fruit
from Objetos_actual import Portal
from Objetos_actual import Skull
from Objetos_actual import Bush_1

class Materiales:

    def __init__(self,loot_config,portal_x,portal_y,misiones):
        '''
        Crea una lista para todos los objetos que cree y establece los parametros recibidos del json como props.
        '''
        self.lista_materiales = []

        self.loot_config = loot_config  
        self.porta_x = portal_x
        self.porta_y = portal_y
        self.lista_loot= []
        self.lista_portal= []
        self.crea_loot()
        self.crea_portal(misiones)
      
    def crea_loot(self):
        '''
        Crea objetos loot con parametros de json y los agrega a la lista materiales
        '''
        for i  in range( self.loot_config["set_01"]["cantidad"] ):

            self.lista_materiales.append(Fruit(self.loot_config ["set_01"]["pos_x"][i],self.loot_config["set_01"]["pos_y"][i],34,25,1))
            self.lista_loot.append(Fruit(self.loot_config ["set_01"]["pos_x"][i],self.loot_config["set_01"]["pos_y"][i],34,25,1))
                              
        for i  in range( self.loot_config["set_02"]["cantidad"] ):
            self.lista_materiales.append(Fruit(self.loot_config ["set_02"]["pos_x"][i],self.loot_config["set_02"]["pos_y"][i],34,25,1))
            self.lista_loot.append(Fruit(self.loot_config["set_02"]["pos_x"][i],self.loot_config["set_02"]["pos_y"][i],34,25,1))      

        for i  in range(self.loot_config["set_03"]["cantidad"]):

            self.lista_materiales.append(Fruit(self.loot_config ["set_03"]["pos_x"][i],self.loot_config["set_03"]["pos_y"][i],34,25,1))
            self.lista_loot.append(Fruit(self.loot_config["set_03"]["pos_x"][i],self.loot_config ["set_03"]["pos_y"][i],34,25,1))         

        for i  in range( self.loot_config["set_04"]["cantidad"] ):

            self.lista_materiales.append(Fruit(  self.loot_config ["set_04"]["pos_x"][i],  self.loot_config ["set_04"]["pos_y"][i],34,25,1))
            self.lista_loot.append(Fruit(  self.loot_config ["set_04"]["pos_x"][i],  self.loot_config ["set_04"]["pos_y"][i],34,25,1))
                              
        self.loot_config.clear()

    def crea_portal(self,misiones):
        '''
        Crea objetos loot con parametros de json y los agrega a la lista materiales
        '''
        self.lista_materiales.append(Portal(self.porta_x,self.porta_y,misiones))
        self.lista_portal.append(Portal(self.porta_x,self.porta_y,misiones))
        self.portal = Portal(self.porta_x,self.porta_y,misiones)

    def update(self,pos_x_y,delta_ms,objetivos):
        '''
        Llama a las funciones que crean objetos para obtener la lista final del objeto Materiales
        '''
        for loot in self.lista_loot:
            loot.colision(pos_x_y)
        self.portal.update(objetivos,pos_x_y,delta_ms)        
                    
               