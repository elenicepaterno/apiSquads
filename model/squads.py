from model.programador import Programador
from model.linguagem import Linguagem
from model.framework import Framework
from model.banco_dados import BancoDados


class Squads:
    def __init__(self, prog=Programador, ling=Linguagem, banco=BancoDados, frame=Framework, id=None):
        self.prog = prog
        self.ling = ling
        self.banco = banco
        self.frame = frame
        self.id = id
    
    def get_prog(self):
        return self.prog

    def get_ling(self):
        return self.ling

    def get_banco(self):
        return self.banco

    def get_frame(self):
        return self.frame

    def get_id_squad(self):
        return self.id

# p = Programador(id=1)
# Squads(p)

# lista()
# p = Programador('sdf',1)
# sq = Squads(p)