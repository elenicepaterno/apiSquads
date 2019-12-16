from flask_restful import Resource
from flask import request
from dao.squads_dao import SquadsDao
from model.squads import Squads
from service.verifica_dados import VerificaDados
from model.framework import Framework
from model.banco_dados import BancoDados
from model.linguagem import Linguagem
from model.programador import Programador


class SquadsController(Resource):
    def __init__(self):
        self.dao = SquadsDao()
        self.verificacao = VerificaDados()


    def get(self, id=None):
        if id:
            return self.dao.buscar_por_id(id)
        else:
            return self.dao.listar()            


    def post(self):
        programador = request.json['programador']
        linguagem = request.json['linguagem']
        framework = request.json['framework']
        banco_dados = request.json['banco_dados']
        squad = Squads(programador, linguagem, framework, banco_dados)

        programador = Programador(id=programador)
        linguagem = Linguagem(id=linguagem)
        framework = Framework(id=framework)
        banco_dados = BancoDados(id=banco_dados)

        if self.verificacao.verificar_squads(squad.__dict__):
            self.dao.inserir(programador, linguagem, framework, banco_dados)
            return 'Squad concluido com sucesso!'
        return 'Squad incorreta!'
    

    def delete(self, id):        
        self.dao.deletar(id)
        return 'Deletado'
    

    def put(self, id):
        programador = request.json['programador']
        linguagem = request.json['linguagem']
        framework = request.json['framework']
        banco_dados = request.json['banco_dados']
        squad = Squads(programador, linguagem, framework, banco_dados, id)
        self.dao.alterar(squad)
        return 'Alterado'