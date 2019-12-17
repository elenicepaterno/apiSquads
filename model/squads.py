from model.programador import Programador
from model.linguagem import Linguagem
from model.framework import Framework
from model.banco_dados import BancoDados


class Squads:
    def __init__(self, prog=Programador, ling=Linguagem, banco=BancoDados, frame=Framework, id=None):
        self.__prog = prog
        self.__ling = ling
        self.__banco = banco
        self.__frame = frame
        self.__id = id
    
    @property
    def prog(self):
        return self.__prog

    @property
    def ling(self):
        return self.__ling
        
    @property
    def banco(self):
        return self.__banco

    @property
    def frame(self):
        return self.__frame

    @property
    def get_id_squad(self):
        return self.__id
