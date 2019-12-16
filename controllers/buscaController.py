import sys
sys.path.append("C:/Users/900223/Desktop/apiSquads/")

from flask_restful import Resource
from flask import request
from dao.programador_dao import ProgramadorDao
from dao.framework_dao import FrameworkDao
from dao.linguagem_dao import LinguagemDao
from dao.banco_dao import BancoDao

class BuscaController(Resource):
    def __init__(self):
        self.prog_dao = ProgramadorDao()
        self.frame_dao = FrameworkDao()
        self.ling_dao = LinguagemDao()
        self.banco_dao = BancoDao()

    def get(self, tabela):
        if tabela == "programador":
            return self.prog_dao.listar()
        
        if tabela == "linguagem":
            return self.ling_dao.listar()
        
        if tabela == "framework":
            return self.frame_dao.listar()
        
        if tabela == "banco_dados":
            return self.banco_dao.listar()
        