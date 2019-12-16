from flask_restful import Resource
from flask import request
from model.tipo_bebida import TipoBebida
from dao.tipo_bebida_dao import TipoBebidaDao

class TipoBebidaController(Resource):
    def __init__(self):
        self.dao = TipoBebidaDao()
    
    def get(self, id=None):
        if id:
            return self.dao.buscar_por_id(id)
        else:
            return self.dao.listar()
    
    def post(self):
        nome = request.json['nome']
        descricao = request.json['descricao']
        tipo_bebida = TipoBebida(nome, descricao)
        self.dao.inserir(tipo_bebida)
        return 'Salvo'
    
    def delete(self, id):
        self.dao.deletar(id)
        return 'Excluiu'
    
    def put(self, id):
        nome = request.json['nome']
        descricao = request.json['descricao']
        tipo_bebida = TipoBebida(nome, descricao, id)
        self.dao.alterar(tipo_bebida)
        return 'Alterado'