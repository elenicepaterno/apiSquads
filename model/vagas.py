from model.programador import Programador
from model.linguagem import Linguagem
from model.framework import Framework
from model.banco_dados import BancoDados


class Vagas(Programador, Linguagem, Framework, BancoDados):
    def __init__(self, nome_prog, nome_ling, nome_banco, nome_frame, id=None):
        self.nome_prog = nome_prog
        self.nome_ling = nome_ling
        self.nome_banco = nome_banco
        self.nome_frame = nome_frame
        self.id = id
    
    def get_nome_prog(self):
        return self.nome_prog

    def get_nome_ling(self):
        return self.nome_ling

    def get_nome_banco(self):
        return self.nome_banco

    def get_nome_frame(self):
        return self.nome_frame

    def get_id_vagas(self):
        return self.id
