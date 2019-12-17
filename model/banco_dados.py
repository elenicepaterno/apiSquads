class BancoDados:
    def __init__(self, nome_banco=None, id=None):
        self.__nome_banco = nome_banco
        self.__id = id
    
    @property
    def nome_banco(self):
        return self.__nome_banco

    @property
    def id_banco(self):
        return self.__id