class Programador:
    def __init__(self, nome_prog=None, id=None):
        self.__nome_prog = nome_prog
        self.__id = id
    
    @property   
    def nome_prog(self):
        return self.__nome_prog

    @property
    def id_prog(self):
        return self.__id
