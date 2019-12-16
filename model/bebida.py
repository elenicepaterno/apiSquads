from model.tipo_bebida import TipoBebida

class Bebida(TipoBebida):
    def __init__(self, nome, teor, tipo_bebida, id=None):
        self.__nome = nome
        self.__teor = teor
        self.__tipo_bebida = tipo_bebida
        self.__id = id
    
    def get_nome_bebida(self):
        return self.__nome

    def get_teor_bebida(self):
        return self.__teor
    
    def get_tipo_bebida(self):
        return self.__tipo_bebida

    def get_id_bebida(self):
        return self.__id
