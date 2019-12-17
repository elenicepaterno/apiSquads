class Framework:
    def __init__(self, nome_frame=None, id=None):
        self.__nome_frame = nome_frame
        self.__id = id
    
    @property
    def nome_frame(self):
        return self.__nome_frame

    @property
    def id_frame(self):
        return self.__id
