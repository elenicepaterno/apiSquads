class TipoBebida:
    def __init__(self, nome, descricao, id=None):
        self.__nome = nome
        self.__descricao = descricao
        self.__id = id

    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def get_id_tipo_bebida(self):
        return self.__id