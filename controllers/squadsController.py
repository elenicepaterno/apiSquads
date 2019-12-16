from flask_restful import Resource
from flask import request
from dao.squads_dao import SquadsDao
from model.squads import Squads

class SquadsController(Resource):
    def __init__(self):
        self.dao = SquadsDao()

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
        self.dao.inserir(squad)
        return 'Squad concluido com sucesso!'
    
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