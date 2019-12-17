class Linguagem:
    def __init__(self, nome_ling=None, id=None):
        self.__nome_ling = nome_ling
        self.__id = id
    
    @property
    def nome_ling(self):
        return self.__nome_ling

    @property   
    def id_ling(self):
        return self.__id
